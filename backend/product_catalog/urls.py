from product_catalog.models import Product
from product_catalog.routes.router import CustomRouter
from product_catalog.views.product.product_view import ProductViewSet

router = CustomRouter()

router.register('product', ProductViewSet, base_name=Product.__name__)
router.register('product/{pk}/attributes/', ProductViewSet, base_name=Product.__name__)
router.register('product/{pk}/prices/', ProductViewSet, base_name=Product.__name__)

urlpatterns = router.urls
