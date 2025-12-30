# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eflo_controller20221215 import models as main_models
from darabonba.model import DaraModel

class ListNodeGroupsResponseBody(DaraModel):
    def __init__(
        self,
        groups: List[main_models.ListNodeGroupsResponseBodyGroups] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The node groups.
        self.groups = groups
        # The token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

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

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.groups = []
        if m.get('Groups') is not None:
            for k1 in m.get('Groups'):
                temp_model = main_models.ListNodeGroupsResponseBodyGroups()
                self.groups.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListNodeGroupsResponseBodyGroups(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        create_time: str = None,
        description: str = None,
        file_system_mount_enabled: bool = None,
        group_id: str = None,
        group_name: str = None,
        image_id: str = None,
        image_name: str = None,
        machine_type: str = None,
        node_count: int = None,
        update_time: str = None,
        virtual_gpu_enabled: bool = None,
        zone_id: str = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # The cluster name.
        self.cluster_name = cluster_name
        # The creation time.
        self.create_time = create_time
        # The description.
        self.description = description
        # Indicates whether file storage mounting is supported.
        self.file_system_mount_enabled = file_system_mount_enabled
        # The group ID.
        self.group_id = group_id
        # The group name.
        self.group_name = group_name
        # The image ID.
        self.image_id = image_id
        # The image name.
        self.image_name = image_name
        # The instance type.
        self.machine_type = machine_type
        # The number of nodes.
        self.node_count = node_count
        # The update time.
        self.update_time = update_time
        # Whether to enable gpu virtualization or not
        self.virtual_gpu_enabled = virtual_gpu_enabled
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.file_system_mount_enabled is not None:
            result['FileSystemMountEnabled'] = self.file_system_mount_enabled

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        if self.machine_type is not None:
            result['MachineType'] = self.machine_type

        if self.node_count is not None:
            result['NodeCount'] = self.node_count

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.virtual_gpu_enabled is not None:
            result['VirtualGpuEnabled'] = self.virtual_gpu_enabled

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FileSystemMountEnabled') is not None:
            self.file_system_mount_enabled = m.get('FileSystemMountEnabled')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('MachineType') is not None:
            self.machine_type = m.get('MachineType')

        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('VirtualGpuEnabled') is not None:
            self.virtual_gpu_enabled = m.get('VirtualGpuEnabled')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

