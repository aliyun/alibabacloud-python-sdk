# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudsso20210515 import models as main_models
from darabonba.model import DaraModel

class CreateGroupResponseBody(DaraModel):
    def __init__(
        self,
        group: main_models.CreateGroupResponseBodyGroup = None,
        request_id: str = None,
    ):
        # The information about the group.
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
            temp_model = main_models.CreateGroupResponseBodyGroup()
            self.group = temp_model.from_map(m.get('Group'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateGroupResponseBodyGroup(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        group_id: str = None,
        group_name: str = None,
        provision_type: str = None,
        update_time: str = None,
    ):
        # The time when the group was created.
        self.create_time = create_time
        # The description of the group.
        self.description = description
        # The ID of the group.
        self.group_id = group_id
        # The name of the group.
        self.group_name = group_name
        # The type of the group. The value is fixed as Manual, which indicates that the group is manually created.
        self.provision_type = provision_type
        # The time when the information about the group was modified.
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

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.provision_type is not None:
            result['ProvisionType'] = self.provision_type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('ProvisionType') is not None:
            self.provision_type = m.get('ProvisionType')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

