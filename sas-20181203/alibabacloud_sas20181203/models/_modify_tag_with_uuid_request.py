# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyTagWithUuidRequest(DaraModel):
    def __init__(
        self,
        machine_types: str = None,
        tag_id: str = None,
        tag_list: str = None,
        target: str = None,
        uuid_list: str = None,
    ):
        # The type of the asset to query. If you do not specify this parameter, the tags of all asset types are queried. Valid values:
        # 
        # *   **ecs**: server
        # *   **cloud_product**: Alibaba Cloud service
        self.machine_types = machine_types
        # The ID of the tag that you want to manage.
        # 
        # >  You can call the [DescribeGroupedTags](~~DescribeGroupedTags~~) operation to query the IDs of tags.
        self.tag_id = tag_id
        # The names of the tags that you want to manage. Separate multiple tag names with commas (,).
        # 
        # >  You can call the [DescribeGroupedTags](~~DescribeGroupedTags~~) operation to query the names of tags.
        # 
        # This parameter is required.
        self.tag_list = tag_list
        # The details of the server for which you want to manage the tag. The value of this parameter is in the JSON format and contains the following fields:
        # 
        # *   **Target**: the UUID of the server that you want to add or remove.
        # 
        # *   **targetType**: the method by which the server is added. Valid values:
        # 
        #     *   **uuid**: by server
        #     *   **groupId**: by server group
        # 
        # *   **flag**: the operation that you want to perform on the server. Valid values:
        # 
        #     *   **del**: removes the tag from the server.
        #     *   **add**: adds the tag to the server.
        self.target = target
        # The UUIDs of the servers.
        # 
        # >  You can call the [DescribeCloudCenterInstances](~~DescribeCloudCenterInstances~~) operation to query the UUIDs of servers.
        self.uuid_list = uuid_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.machine_types is not None:
            result['MachineTypes'] = self.machine_types

        if self.tag_id is not None:
            result['TagId'] = self.tag_id

        if self.tag_list is not None:
            result['TagList'] = self.tag_list

        if self.target is not None:
            result['Target'] = self.target

        if self.uuid_list is not None:
            result['UuidList'] = self.uuid_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MachineTypes') is not None:
            self.machine_types = m.get('MachineTypes')

        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')

        if m.get('TagList') is not None:
            self.tag_list = m.get('TagList')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        if m.get('UuidList') is not None:
            self.uuid_list = m.get('UuidList')

        return self

