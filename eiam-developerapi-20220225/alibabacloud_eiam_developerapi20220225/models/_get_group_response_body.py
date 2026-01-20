# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetGroupResponseBody(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        description: str = None,
        group_external_id: str = None,
        group_id: str = None,
        group_name: str = None,
        group_source_id: str = None,
        group_source_type: str = None,
        instance_id: str = None,
        update_time: int = None,
    ):
        # The time when the group was created. The value is a UNIX timestamp. Unit: milliseconds.
        self.create_time = create_time
        # The group description.
        self.description = description
        # The external ID of the group.
        self.group_external_id = group_external_id
        # The group ID.
        self.group_id = group_id
        # The group name.
        self.group_name = group_name
        # The source ID of the group.
        self.group_source_id = group_source_id
        # The source type of the group. Valid values: build_in, ding_talk, ad, and ldap.
        self.group_source_type = group_source_type
        # The instance ID.
        self.instance_id = instance_id
        # The time when the group was last updated. The value is a UNIX timestamp. Unit: milliseconds.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.description is not None:
            result['description'] = self.description

        if self.group_external_id is not None:
            result['groupExternalId'] = self.group_external_id

        if self.group_id is not None:
            result['groupId'] = self.group_id

        if self.group_name is not None:
            result['groupName'] = self.group_name

        if self.group_source_id is not None:
            result['groupSourceId'] = self.group_source_id

        if self.group_source_type is not None:
            result['groupSourceType'] = self.group_source_type

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('groupExternalId') is not None:
            self.group_external_id = m.get('groupExternalId')

        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')

        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')

        if m.get('groupSourceId') is not None:
            self.group_source_id = m.get('groupSourceId')

        if m.get('groupSourceType') is not None:
            self.group_source_type = m.get('groupSourceType')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        return self

