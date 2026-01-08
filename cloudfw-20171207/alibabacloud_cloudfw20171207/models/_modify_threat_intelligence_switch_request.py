# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class ModifyThreatIntelligenceSwitchRequest(DaraModel):
    def __init__(
        self,
        category_list: List[main_models.ModifyThreatIntelligenceSwitchRequestCategoryList] = None,
    ):
        self.category_list = category_list

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.category_list = []
        if m.get('CategoryList') is not None:
            for k1 in m.get('CategoryList'):
                temp_model = main_models.ModifyThreatIntelligenceSwitchRequestCategoryList()
                self.category_list.append(temp_model.from_map(k1))

        return self

class ModifyThreatIntelligenceSwitchRequestCategoryList(DaraModel):
    def __init__(
        self,
        action: str = None,
        category_id: str = None,
        enable_status: str = None,
    ):
        self.action = action
        self.category_id = category_id
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

        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.enable_status is not None:
            result['EnableStatus'] = self.enable_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('EnableStatus') is not None:
            self.enable_status = m.get('EnableStatus')

        return self

