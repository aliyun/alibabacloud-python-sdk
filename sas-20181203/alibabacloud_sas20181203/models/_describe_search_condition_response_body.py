# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeSearchConditionResponseBody(DaraModel):
    def __init__(
        self,
        condition_list: List[main_models.DescribeSearchConditionResponseBodyConditionList] = None,
        request_id: str = None,
    ):
        # An array that consists of the filter conditions.
        self.condition_list = condition_list
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.condition_list:
            for v1 in self.condition_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ConditionList'] = []
        if self.condition_list is not None:
            for k1 in self.condition_list:
                result['ConditionList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.condition_list = []
        if m.get('ConditionList') is not None:
            for k1 in m.get('ConditionList'):
                temp_model = main_models.DescribeSearchConditionResponseBodyConditionList()
                self.condition_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeSearchConditionResponseBodyConditionList(DaraModel):
    def __init__(
        self,
        condition_type: str = None,
        filter_conditions: str = None,
        name: str = None,
        name_key: str = None,
    ):
        # The type of the filter condition. Valid values:
        # 
        # *   **system**: default filter conditions.
        # *   **user**: custom filter conditions.
        self.condition_type = condition_type
        # The filter condition. The value of this parameter is in the JSON format and contains the following fields:
        # 
        # *   **filterParams**: the parameters of the filter condition. The value of this field is in the JSON format and contains the following fields:
        # 
        #     *   **labelKey**: the key for rendering.
        # 
        #     *   **label**: the display name.
        # 
        #     *   **value**: the value of the filter condition. The value of this field is in the JSON format and contains the following fields:
        # 
        #         *   **name**: the name of the filter item.
        #         *   **value**: the value of the filter item.
        # 
        # *   **LogicalExp**: the logical relationship among the filter conditions. Valid values:
        # 
        #     *   **AND**: The filter conditions are evaluated by using a logical **AND**.
        #     *   **OR**: The filter conditions are evaluated by using a logical **OR**.
        # 
        # >  If the value of **ConditionType** is **system**, **labelKey** is returned. The labelKey field is used only for internationalization rendering.
        self.filter_conditions = filter_conditions
        # The filter condition name.
        self.name = name
        # The key of the filter condition name.
        self.name_key = name_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.condition_type is not None:
            result['ConditionType'] = self.condition_type

        if self.filter_conditions is not None:
            result['FilterConditions'] = self.filter_conditions

        if self.name is not None:
            result['Name'] = self.name

        if self.name_key is not None:
            result['NameKey'] = self.name_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConditionType') is not None:
            self.condition_type = m.get('ConditionType')

        if m.get('FilterConditions') is not None:
            self.filter_conditions = m.get('FilterConditions')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NameKey') is not None:
            self.name_key = m.get('NameKey')

        return self

