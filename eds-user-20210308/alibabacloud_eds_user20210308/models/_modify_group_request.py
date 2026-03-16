# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyGroupRequest(DaraModel):
    def __init__(
        self,
        business_channel: str = None,
        description: str = None,
        group_id: str = None,
        new_group_name: str = None,
    ):
        self.business_channel = business_channel
        # The new description of the user group.
        self.description = description
        # The ID of the user group.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The name of the new user group.
        # 
        # This parameter is required.
        self.new_group_name = new_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_channel is not None:
            result['BusinessChannel'] = self.business_channel

        if self.description is not None:
            result['Description'] = self.description

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.new_group_name is not None:
            result['NewGroupName'] = self.new_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessChannel') is not None:
            self.business_channel = m.get('BusinessChannel')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('NewGroupName') is not None:
            self.new_group_name = m.get('NewGroupName')

        return self

