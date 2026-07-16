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
        # Description. The maximum length is 256 characters.
        self.description = description
        # Group external ID, used for association with external systems. The default value is the group ID. The maximum length is 64 characters.
        self.group_external_id = group_external_id
        # Group name. The maximum length is 64 characters.
        # 
        # This parameter is required.
        self.group_name = group_name
        # Instance ID.
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

