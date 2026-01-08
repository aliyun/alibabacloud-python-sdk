# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeThreatIntelligenceSwitchResponseBody(DaraModel):
    def __init__(
        self,
        category_list: List[main_models.DescribeThreatIntelligenceSwitchResponseBodyCategoryList] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.category_list = category_list
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.category_list:
            for v1 in self.category_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CategoryList'] = []
        if self.category_list is not None:
            for k1 in self.category_list:
                result['CategoryList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.category_list = []
        if m.get('CategoryList') is not None:
            for k1 in m.get('CategoryList'):
                temp_model = main_models.DescribeThreatIntelligenceSwitchResponseBodyCategoryList()
                self.category_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeThreatIntelligenceSwitchResponseBodyCategoryList(DaraModel):
    def __init__(
        self,
        action: str = None,
        category_describe: str = None,
        category_id: str = None,
        category_name: str = None,
        category_parent_id: str = None,
        enable_status: int = None,
    ):
        self.action = action
        self.category_describe = category_describe
        self.category_id = category_id
        self.category_name = category_name
        self.category_parent_id = category_parent_id
        self.enable_status = enable_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.category_describe is not None:
            result['CategoryDescribe'] = self.category_describe

        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.category_name is not None:
            result['CategoryName'] = self.category_name

        if self.category_parent_id is not None:
            result['CategoryParentId'] = self.category_parent_id

        if self.enable_status is not None:
            result['EnableStatus'] = self.enable_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('CategoryDescribe') is not None:
            self.category_describe = m.get('CategoryDescribe')

        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')

        if m.get('CategoryParentId') is not None:
            self.category_parent_id = m.get('CategoryParentId')

        if m.get('EnableStatus') is not None:
            self.enable_status = m.get('EnableStatus')

        return self

