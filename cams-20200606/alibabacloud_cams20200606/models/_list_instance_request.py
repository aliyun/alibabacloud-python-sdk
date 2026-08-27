# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListInstanceRequest(DaraModel):
    def __init__(
        self,
        bind_id: str = None,
        channel_type: str = None,
        filter_str: str = None,
        instance_id: str = None,
        instance_name: str = None,
        is_bind: bool = None,
        page_index: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        submit_time: str = None,
    ):
        self.bind_id = bind_id
        # The channel type. Valid values:
        # 
        # - **whatsapp**
        # 
        # - **messenger**
        # - **instagram**
        # 
        # <props="intl">- **viber**
        self.channel_type = channel_type
        # The filter condition.
        self.filter_str = filter_str
        # The instance ID. Only non-Alibaba Cloud hosts are supported.
        self.instance_id = instance_id
        # The instance name.
        self.instance_name = instance_name
        self.is_bind = is_bind
        # The page number.
        self.page_index = page_index
        # The number of records per page.
        self.page_size = page_size
        # The ID of the enterprise resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        # The submit time.
        self.submit_time = submit_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bind_id is not None:
            result['BindId'] = self.bind_id

        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type

        if self.filter_str is not None:
            result['FilterStr'] = self.filter_str

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.is_bind is not None:
            result['IsBind'] = self.is_bind

        if self.page_index is not None:
            result['PageIndex'] = self.page_index

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindId') is not None:
            self.bind_id = m.get('BindId')

        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')

        if m.get('FilterStr') is not None:
            self.filter_str = m.get('FilterStr')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('IsBind') is not None:
            self.is_bind = m.get('IsBind')

        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')

        return self

