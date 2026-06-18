# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QuerySkillGroupsRequest(DaraModel):
    def __init__(
        self,
        channel_type: int = None,
        client_token: str = None,
        department_id: int = None,
        instance_id: str = None,
        page_no: int = None,
        page_size: int = None,
    ):
        # The channel type of the skill group. Valid values:
        # 
        # - **0**: Returns all skill groups.
        # - **1**: Hotline skill group.
        # - **2**: Online skill group.
        # - **3**: Online and hotline skill group.
        # - **4**: Ticket skill group.
        # - **5**: Hotline and ticket skill group.
        # - **6**: Online and ticket skill group.
        # - **7**: Online, hotline, and ticket skill group.
        self.channel_type = channel_type
        # A unique ID for the customer request. Used for idempotency validation. You can generate it using UUID.
        self.client_token = client_token
        # The department ID.
        self.department_id = department_id
        # The Artificial Intelligence Cloud Call Service (AICCS) instance ID.  
        # You can obtain it from **Instance Management** in the left-side navigation pane of the [Artificial Intelligence Cloud Call Service console](https://aiccs.console.aliyun.com/overview).
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The current page number. The value must be greater than **0**. Default Value: **1**.
        # 
        # This parameter is required.
        self.page_no = page_no
        # Page size. The value must be greater than **0**. Default value: **20**.
        # 
        # This parameter is required.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.department_id is not None:
            result['DepartmentId'] = self.department_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

