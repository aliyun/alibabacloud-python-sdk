# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeSensitiveSwitchResponseBody(DaraModel):
    def __init__(
        self,
        open_count: int = None,
        request_id: str = None,
        total_count: int = None,
        user_sensitive_data_switch_list: List[main_models.DescribeSensitiveSwitchResponseBodyUserSensitiveDataSwitchList] = None,
    ):
        self.open_count = open_count
        self.request_id = request_id
        self.total_count = total_count
        self.user_sensitive_data_switch_list = user_sensitive_data_switch_list

    def validate(self):
        if self.user_sensitive_data_switch_list:
            for v1 in self.user_sensitive_data_switch_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.open_count is not None:
            result['OpenCount'] = self.open_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['UserSensitiveDataSwitchList'] = []
        if self.user_sensitive_data_switch_list is not None:
            for k1 in self.user_sensitive_data_switch_list:
                result['UserSensitiveDataSwitchList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpenCount') is not None:
            self.open_count = m.get('OpenCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.user_sensitive_data_switch_list = []
        if m.get('UserSensitiveDataSwitchList') is not None:
            for k1 in m.get('UserSensitiveDataSwitchList'):
                temp_model = main_models.DescribeSensitiveSwitchResponseBodyUserSensitiveDataSwitchList()
                self.user_sensitive_data_switch_list.append(temp_model.from_map(k1))

        return self

class DescribeSensitiveSwitchResponseBodyUserSensitiveDataSwitchList(DaraModel):
    def __init__(
        self,
        category_name: str = None,
        description: str = None,
        sensitive_category: str = None,
        sensitive_level: str = None,
        switch_status: int = None,
    ):
        self.category_name = category_name
        self.description = description
        self.sensitive_category = sensitive_category
        self.sensitive_level = sensitive_level
        self.switch_status = switch_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_name is not None:
            result['CategoryName'] = self.category_name

        if self.description is not None:
            result['Description'] = self.description

        if self.sensitive_category is not None:
            result['SensitiveCategory'] = self.sensitive_category

        if self.sensitive_level is not None:
            result['SensitiveLevel'] = self.sensitive_level

        if self.switch_status is not None:
            result['SwitchStatus'] = self.switch_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('SensitiveCategory') is not None:
            self.sensitive_category = m.get('SensitiveCategory')

        if m.get('SensitiveLevel') is not None:
            self.sensitive_level = m.get('SensitiveLevel')

        if m.get('SwitchStatus') is not None:
            self.switch_status = m.get('SwitchStatus')

        return self

