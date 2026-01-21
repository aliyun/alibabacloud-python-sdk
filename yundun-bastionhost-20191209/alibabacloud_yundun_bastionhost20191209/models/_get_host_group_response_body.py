# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_yundun_bastionhost20191209 import models as main_models
from darabonba.model import DaraModel

class GetHostGroupResponseBody(DaraModel):
    def __init__(
        self,
        host_group: main_models.GetHostGroupResponseBodyHostGroup = None,
        request_id: str = None,
    ):
        # The returned detailed information about the asset group.
        self.host_group = host_group
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.host_group:
            self.host_group.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host_group is not None:
            result['HostGroup'] = self.host_group.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostGroup') is not None:
            temp_model = main_models.GetHostGroupResponseBodyHostGroup()
            self.host_group = temp_model.from_map(m.get('HostGroup'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetHostGroupResponseBodyHostGroup(DaraModel):
    def __init__(
        self,
        comment: str = None,
        host_group_id: str = None,
        host_group_name: str = None,
    ):
        # The remarks of the asset group.
        self.comment = comment
        # The asset group ID.
        self.host_group_id = host_group_id
        # The name of the asset group.
        self.host_group_name = host_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id

        if self.host_group_name is not None:
            result['HostGroupName'] = self.host_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')

        if m.get('HostGroupName') is not None:
            self.host_group_name = m.get('HostGroupName')

        return self

