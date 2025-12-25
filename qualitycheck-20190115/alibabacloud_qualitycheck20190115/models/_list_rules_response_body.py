# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_qualitycheck20190115 import models as main_models
from darabonba.model import DaraModel

class ListRulesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        count: int = None,
        data: List[main_models.ListRulesResponseBodyData] = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.count = count
        self.data = data
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.count is not None:
            result['Count'] = self.count

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListRulesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListRulesResponseBodyData(DaraModel):
    def __init__(
        self,
        business_category_name_list: List[str] = None,
        comments: str = None,
        create_time: str = None,
        name: str = None,
        rid: int = None,
        rule_type: int = None,
        type: int = None,
        type_name: str = None,
    ):
        self.business_category_name_list = business_category_name_list
        self.comments = comments
        self.create_time = create_time
        self.name = name
        self.rid = rid
        self.rule_type = rule_type
        self.type = type
        self.type_name = type_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_category_name_list is not None:
            result['BusinessCategoryNameList'] = self.business_category_name_list

        if self.comments is not None:
            result['Comments'] = self.comments

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.name is not None:
            result['Name'] = self.name

        if self.rid is not None:
            result['Rid'] = self.rid

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        if self.type is not None:
            result['Type'] = self.type

        if self.type_name is not None:
            result['TypeName'] = self.type_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessCategoryNameList') is not None:
            self.business_category_name_list = m.get('BusinessCategoryNameList')

        if m.get('Comments') is not None:
            self.comments = m.get('Comments')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Rid') is not None:
            self.rid = m.get('Rid')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')

        return self

