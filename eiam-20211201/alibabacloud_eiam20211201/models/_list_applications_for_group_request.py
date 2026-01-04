# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListApplicationsForGroupRequest(DaraModel):
    def __init__(
        self,
        application_ids: List[str] = None,
        group_id: str = None,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # 非必填，如果填写则可以基于应用ID进行过滤，列表中最多包含100个元素。
        self.application_ids = application_ids
        # 组的唯一标识。
        # 
        # This parameter is required.
        self.group_id = group_id
        # IDaaS EIAM实例的ID。
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # 当前查询的列表页码，默认为1。
        self.page_number = page_number
        # 当前查询的列表页码，默认为20。
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_ids is not None:
            result['ApplicationIds'] = self.application_ids

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationIds') is not None:
            self.application_ids = m.get('ApplicationIds')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

