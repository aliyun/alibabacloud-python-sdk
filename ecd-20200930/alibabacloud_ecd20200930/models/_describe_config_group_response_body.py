# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeConfigGroupResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribeConfigGroupResponseBodyData] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The configuration groups.
        self.data = data
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

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
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeConfigGroupResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeConfigGroupResponseBodyData(DaraModel):
    def __init__(
        self,
        bind_count: int = None,
        bind_count_map: Dict[str, int] = None,
        description: str = None,
        group_id: str = None,
        inner_timer_desc: str = None,
        inner_timer_name: str = None,
        is_bind: bool = None,
        is_update: bool = None,
        name: str = None,
        product_type: str = None,
        status: str = None,
        type: str = None,
    ):
        # The number of resources that are bound to the configuration group.
        self.bind_count = bind_count
        # The number of bound cloud computers.
        self.bind_count_map = bind_count_map
        # The description of the configuration group.
        self.description = description
        # The ID of the configuration group.
        self.group_id = group_id
        self.inner_timer_desc = inner_timer_desc
        self.inner_timer_name = inner_timer_name
        self.is_bind = is_bind
        self.is_update = is_update
        # The name of the configuration group.
        self.name = name
        # The service type of the configuration group.
        # 
        # Valid values:
        # 
        # *   CLOUD_DESKTOP: the cloud computer service.
        self.product_type = product_type
        # The state of the configuration group.
        # 
        # Valid values:
        # 
        # *   AVAILABLE: The configuration group is available.
        # *   UNAVAILABLE: The configuration group is deleted.
        # *   DELETING: The configuration group is being deleted.
        # *   UPDATING: The configuration group is being modified.
        self.status = status
        # The type of the configuration group.
        # 
        # Valid values:
        # 
        # *   Timer: the scheduled task type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bind_count is not None:
            result['BindCount'] = self.bind_count

        if self.bind_count_map is not None:
            result['BindCountMap'] = self.bind_count_map

        if self.description is not None:
            result['Description'] = self.description

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.inner_timer_desc is not None:
            result['InnerTimerDesc'] = self.inner_timer_desc

        if self.inner_timer_name is not None:
            result['InnerTimerName'] = self.inner_timer_name

        if self.is_bind is not None:
            result['IsBind'] = self.is_bind

        if self.is_update is not None:
            result['IsUpdate'] = self.is_update

        if self.name is not None:
            result['Name'] = self.name

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindCount') is not None:
            self.bind_count = m.get('BindCount')

        if m.get('BindCountMap') is not None:
            self.bind_count_map = m.get('BindCountMap')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('InnerTimerDesc') is not None:
            self.inner_timer_desc = m.get('InnerTimerDesc')

        if m.get('InnerTimerName') is not None:
            self.inner_timer_name = m.get('InnerTimerName')

        if m.get('IsBind') is not None:
            self.is_bind = m.get('IsBind')

        if m.get('IsUpdate') is not None:
            self.is_update = m.get('IsUpdate')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

