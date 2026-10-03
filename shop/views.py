from django.shortcuts import get_object_or_404, redirect, render
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.http import require_POST

from .models import Product


# ---------- Home: search + filter + sort ----------
def home(request):
    q = request.GET.get("q", "").strip()
    category = request.GET.get("category", "")
    sort = request.GET.get("sort", "")

    products = Product.objects.all()
    if q:
        products = products.filter(name__icontains=q)
    if category:
        products = products.filter(category=category)
    if sort == "low":
        products = products.order_by("price", "name")
    elif sort == "high":
        products = products.order_by("-price", "name")

    return render(request, "home.html", {
        "products": products,
        "categories": Product.objects.order_by("category").values_list("category", flat=True).distinct(),
        "q": q, "category": category, "sort": sort,
    })


# ---------- Cart (stored in the session) ----------
@require_POST
def cart_add(request, pk):
    get_object_or_404(Product, pk=pk)
    cart = request.session.get("cart", {})
    cart[str(pk)] = cart.get(str(pk), 0) + 1
    request.session["cart"] = cart
    # stay on the same page (keeps search/filter), but only to a safe local URL
    nxt = request.POST.get("next", "")
    if url_has_allowed_host_and_scheme(nxt, allowed_hosts={request.get_host()}):
        return redirect(nxt)
    return redirect("home")


def cart_view(request):
    cart = request.session.get("cart", {})
    products = Product.objects.in_bulk([int(pk) for pk in cart])
    items, total = [], 0
    for pk, qty in cart.items():
        product = products.get(int(pk))
        if product:
            subtotal = product.price * qty
            total += subtotal
            items.append({"product": product, "qty": qty, "subtotal": subtotal})
    return render(request, "cart.html", {"items": items, "total": total})


@require_POST
def cart_change(request, pk, action):
    cart = request.session.get("cart", {})
    key = str(pk)
    if key in cart:
        if action == "plus":
            cart[key] += 1
        elif action == "minus":
            cart[key] -= 1
        if action == "remove" or cart[key] <= 0:
            del cart[key]
    request.session["cart"] = cart
    return redirect("cart")


@require_POST
def place_order(request):
    request.session["cart"] = {}
    return redirect("order_success")


def order_success(request):
    return render(request, "order_success.html")
