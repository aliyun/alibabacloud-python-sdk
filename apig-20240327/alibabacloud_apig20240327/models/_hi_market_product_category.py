# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class HiMarketProductCategory(DaraModel):
    def __init__(
        self,
        category_id: str = None,
        description: str = None,
        icon: main_models.HiMarketIcon = None,
        name: str = None,
    ):
        self.category_id = category_id
        self.description = description
        self.icon = icon
        self.name = name

    def validate(self):
        if self.icon:
            self.icon.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_id is not None:
            result['categoryId'] = self.category_id

        if self.description is not None:
            result['description'] = self.description

        if self.icon is not None:
            result['icon'] = self.icon.to_map()

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('categoryId') is not None:
            self.category_id = m.get('categoryId')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('icon') is not None:
            temp_model = main_models.HiMarketIcon()
            self.icon = temp_model.from_map(m.get('icon'))

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

