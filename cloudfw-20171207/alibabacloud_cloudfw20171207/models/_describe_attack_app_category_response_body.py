# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeAttackAppCategoryResponseBody(DaraModel):
    def __init__(
        self,
        app_categories: List[main_models.DescribeAttackAppCategoryResponseBodyAppCategories] = None,
        request_id: str = None,
    ):
        self.app_categories = app_categories
        self.request_id = request_id

    def validate(self):
        if self.app_categories:
            for v1 in self.app_categories:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AppCategories'] = []
        if self.app_categories is not None:
            for k1 in self.app_categories:
                result['AppCategories'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_categories = []
        if m.get('AppCategories') is not None:
            for k1 in m.get('AppCategories'):
                temp_model = main_models.DescribeAttackAppCategoryResponseBodyAppCategories()
                self.app_categories.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAttackAppCategoryResponseBodyAppCategories(DaraModel):
    def __init__(
        self,
        attack_apps: List[str] = None,
        category_name: str = None,
    ):
        self.attack_apps = attack_apps
        self.category_name = category_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attack_apps is not None:
            result['AttackApps'] = self.attack_apps

        if self.category_name is not None:
            result['CategoryName'] = self.category_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttackApps') is not None:
            self.attack_apps = m.get('AttackApps')

        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')

        return self

