# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ListGroupsResponseBody(DaraModel):
    def __init__(
        self,
        groups: List[main_models.ListGroupsResponseBodyGroups] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Account group list.
        self.groups = groups
        # Request ID.
        self.request_id = request_id
        # Total number of matched entries. The maximum number of entries returned in a single request is determined by pageSize.
        self.total_count = total_count

    def validate(self):
        if self.groups:
            for v1 in self.groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Groups'] = []
        if self.groups is not None:
            for k1 in self.groups:
                result['Groups'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.groups = []
        if m.get('Groups') is not None:
            for k1 in m.get('Groups'):
                temp_model = main_models.ListGroupsResponseBodyGroups()
                self.groups.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListGroupsResponseBodyGroups(DaraModel):
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
        # Group creation time in Unix timestamp format, in milliseconds.
        self.create_time = create_time
        # Group description.
        self.description = description
        # Group external ID, used for association with external systems. Defaults to the account group ID.
        self.group_external_id = group_external_id
        # Group ID.
        self.group_id = group_id
        # Group name.
        self.group_name = group_name
        # Group source ID. If created by importing from other sources, this is the external source ID. Defaults to the instance ID.
        self.group_source_id = group_source_id
        # Group source type. Currently, only self-built is supported. Valid values:
        # - build_in: self-built.
        self.group_source_type = group_source_type
        # Instance ID.
        self.instance_id = instance_id
        # Group last update time in Unix timestamp format, in milliseconds.
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

