# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CategoryAttributeMatchRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        image_url: List[str] = None,
        item_spec: str = None,
        sku: str = None,
        source_category: str = None,
        source_platform: str = None,
        target_platform: str = None,
        title: str = None,
    ):
        # The product details.
        self.description = description
        # The product image URLs. A maximum of 10 images are supported.
        self.image_url = image_url
        # The product attributes that describe the product characteristics.
        # 
        # This parameter is required.
        self.item_spec = item_spec
        # The product SKU title.
        # 
        # This parameter is required.
        self.sku = sku
        # The product category on the source platform.
        # 
        # This parameter is required.
        self.source_category = source_category
        # The source platform from which the product originates.
        # 
        # This parameter is required.
        self.source_platform = source_platform
        # The target listing platform. Currently, only temu is supported.
        # 
        # This parameter is required.
        self.target_platform = target_platform
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
        if self.description is not None:
            result['Description'] = self.description

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.item_spec is not None:
            result['ItemSpec'] = self.item_spec

        if self.sku is not None:
            result['Sku'] = self.sku

        if self.source_category is not None:
            result['SourceCategory'] = self.source_category

        if self.source_platform is not None:
            result['SourcePlatform'] = self.source_platform

        if self.target_platform is not None:
            result['TargetPlatform'] = self.target_platform

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('ItemSpec') is not None:
            self.item_spec = m.get('ItemSpec')

        if m.get('Sku') is not None:
            self.sku = m.get('Sku')

        if m.get('SourceCategory') is not None:
            self.source_category = m.get('SourceCategory')

        if m.get('SourcePlatform') is not None:
            self.source_platform = m.get('SourcePlatform')

        if m.get('TargetPlatform') is not None:
            self.target_platform = m.get('TargetPlatform')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

