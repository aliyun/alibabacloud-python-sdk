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
        self.channel_type = channel_type
        self.client_token = client_token
        self.department_id = department_id
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.page_no = page_no
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

