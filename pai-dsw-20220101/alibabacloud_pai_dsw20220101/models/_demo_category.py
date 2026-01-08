# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pai_dsw20220101 import models as main_models
from darabonba.model import DaraModel

class DemoCategory(DaraModel):
    def __init__(
        self,
        category_code: str = None,
        category_name: str = None,
        order: int = None,
        sub_categories: List[main_models.DemoCategory] = None,
    ):
        self.category_code = category_code
        self.category_name = category_name
        self.order = order
        self.sub_categories = sub_categories

    def validate(self):
        if self.sub_categories:
            for v1 in self.sub_categories:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_code is not None:
            result['CategoryCode'] = self.category_code

        if self.category_name is not None:
            result['CategoryName'] = self.category_name

        if self.order is not None:
            result['Order'] = self.order

        result['SubCategories'] = []
        if self.sub_categories is not None:
            for k1 in self.sub_categories:
                result['SubCategories'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryCode') is not None:
            self.category_code = m.get('CategoryCode')

        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        self.sub_categories = []
        if m.get('SubCategories') is not None:
            for k1 in m.get('SubCategories'):
                temp_model = main_models.DemoCategory()
                self.sub_categories.append(temp_model.from_map(k1))

        return self

