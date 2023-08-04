import pytest
import json

pytestmark = pytest.mark.django_db


class TestCategoryEndpointes:
    endpoint = "/api/category/"

    def test_category_get(self, category_factory, api_client):
        category_factory.create_batch(4)
        response = api_client().get(self.endpoint)
        # Asserts
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 4


class TestBrandEndpointes:
    endpoint = "/api/brand/"

    def test_brand_get(self, brand_factory, api_client):
        brand_factory.create_batch(4)
        response = api_client().get(self.endpoint)
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 4


class TestProductEndpointes:
    endpoint = "/api/product/"

    def test_product_get(self, product_factory, api_client):
        product_factory.create_batch(4)
        response = api_client().get(self.endpoint)
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 4
