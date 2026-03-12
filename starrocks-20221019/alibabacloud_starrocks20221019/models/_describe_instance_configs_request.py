# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeInstanceConfigsRequest(DaraModel):
    def __init__(
        self,
        allow_modify: bool = None,
        config_key: str = None,
        config_type: str = None,
        description: str = None,
        instance_id: str = None,
        need_total: bool = None,
        node_group_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.allow_modify = allow_modify
        self.config_key = config_key
        self.config_type = config_type
        self.description = description
        # This parameter is required.
        self.instance_id = instance_id
        self.need_total = need_total
        self.node_group_id = node_group_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_modify is not None:
            result['AllowModify'] = self.allow_modify

        if self.config_key is not None:
            result['ConfigKey'] = self.config_key

        if self.config_type is not None:
            result['ConfigType'] = self.config_type

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.need_total is not None:
            result['NeedTotal'] = self.need_total

        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowModify') is not None:
            self.allow_modify = m.get('AllowModify')

        if m.get('ConfigKey') is not None:
            self.config_key = m.get('ConfigKey')

        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NeedTotal') is not None:
            self.need_total = m.get('NeedTotal')

        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

