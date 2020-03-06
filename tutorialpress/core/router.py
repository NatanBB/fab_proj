from rest_framework import routers

from tutorialpress.core.views import PublicacaoViewSet

router = routers.SimpleRouter()
router.register("publicacoes", PublicacaoViewSet)
