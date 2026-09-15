# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitProductMatchRequest(DaraModel):
    def __init__(
        self,
        brand_name: str = None,
        category: str = None,
        image_url: str = None,
        item_id: str = None,
        product_url: str = None,
        shop_name: str = None,
        title: str = None,
    ):
        # The product brand. If this value is not specified, the system attempts to extract the brand from the shop name.
        self.brand_name = brand_name
        # The Miaojie product category. Currently used for extension and auditing purposes.
        self.category = category
        # The HTTP or HTTPS URL of the product main image.
        # 
        # This parameter is required.
        self.image_url = image_url
        # The Miaojie product ID.
        # 
        # This parameter is required.
        self.item_id = item_id
        # The HTTP or HTTPS URL of the product detail page.
        self.product_url = product_url
        # The shop name. This value is also used as the extraction source when the brand name is missing.
        # 
        # This parameter is required.
        self.shop_name = shop_name
        # The product title.
        # 
        # This parameter is required.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.brand_name is not None:
            result['BrandName'] = self.brand_name

        if self.category is not None:
            result['Category'] = self.category

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.item_id is not None:
            result['ItemId'] = self.item_id

        if self.product_url is not None:
            result['ProductUrl'] = self.product_url

        if self.shop_name is not None:
            result['ShopName'] = self.shop_name

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BrandName') is not None:
            self.brand_name = m.get('BrandName')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')

        if m.get('ProductUrl') is not None:
            self.product_url = m.get('ProductUrl')

        if m.get('ShopName') is not None:
            self.shop_name = m.get('ShopName')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

