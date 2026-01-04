# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateGroupRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        group_external_id: str = None,
        group_name: str = None,
        instance_id: str = None,
    ):
        # The description of the group. The value can be up to 256 characters in length.
        self.description = description
        # The external ID of the group, which can be used to associate the group with an external system. By default, the external ID is the group ID. The value can be up to 64 characters in length.
        self.group_external_id = group_external_id
        # The name of the group. The name can be up to 64 characters in length.
        # 
        # This parameter is required.
        self.group_name = group_name
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.group_external_id is not None:
            result['GroupExternalId'] = self.group_external_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupExternalId') is not None:
            self.group_external_id = m.get('GroupExternalId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

