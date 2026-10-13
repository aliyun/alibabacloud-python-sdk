# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class UpdateProductCategoryRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        icon: main_models.HiMarketIcon = None,
        name: str = None,
    ):
        # The description of the product category. The description can be up to 500 characters in length.
        self.description = description
        # The icon of the product category. The icon consists of two fields: icon type (type) and icon information (value).
        self.icon = icon
        # The name of the product category. The name can be up to 100 characters in length.
        self.name = name

    def validate(self):
        if self.icon:
            self.icon.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.icon is not None:
            result['icon'] = self.icon.to_map()

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('icon') is not None:
            temp_model = main_models.HiMarketIcon()
            self.icon = temp_model.from_map(m.get('icon'))

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

