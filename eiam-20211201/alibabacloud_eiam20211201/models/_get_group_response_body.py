# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class GetGroupResponseBody(DaraModel):
    def __init__(
        self,
        group: main_models.GetGroupResponseBodyGroup = None,
        request_id: str = None,
    ):
        # The information about the account group.
        self.group = group
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.group:
            self.group.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group is not None:
            result['Group'] = self.group.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Group') is not None:
            temp_model = main_models.GetGroupResponseBodyGroup()
            self.group = temp_model.from_map(m.get('Group'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetGroupResponseBodyGroup(DaraModel):
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
        # The time at which the group was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_time = create_time
        # The description of the group.
        self.description = description
        # The external ID of the group, which can be used to associate the group with an external system. By default, the external ID is the group ID.
        self.group_external_id = group_external_id
        # The group ID.
        self.group_id = group_id
        # The name of the group.
        self.group_name = group_name
        # The source ID of the group. By default, the source ID is the instance ID.
        self.group_source_id = group_source_id
        # The source type of the group. Only build_in may be returned, which indicates that the group was created in IDaaS.
        # 
        # *build_in:Create By Self.
        self.group_source_type = group_source_type
        # The instance ID.
        self.instance_id = instance_id
        # The time at which the group was last updated. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.group_external_id is not None:
            result['GroupExternalId'] = self.group_external_id

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.group_source_id is not None:
            result['GroupSourceId'] = self.group_source_id

        if self.group_source_type is not None:
            result['GroupSourceType'] = self.group_source_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupExternalId') is not None:
            self.group_external_id = m.get('GroupExternalId')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('GroupSourceId') is not None:
            self.group_source_id = m.get('GroupSourceId')

        if m.get('GroupSourceType') is not None:
            self.group_source_type = m.get('GroupSourceType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

