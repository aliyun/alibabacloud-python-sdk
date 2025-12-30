# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateNodeGroupRequest(DaraModel):
    def __init__(
        self,
        file_system_mount_enabled: bool = None,
        image_id: str = None,
        key_pair_name: str = None,
        login_password: str = None,
        new_node_group_name: str = None,
        node_group_id: str = None,
        user_data: str = None,
    ):
        # Whether file storage mounting is supported
        self.file_system_mount_enabled = file_system_mount_enabled
        # The default image ID of the node group. If not set, it will not change.
        self.image_id = image_id
        # Key pair name.
        self.key_pair_name = key_pair_name
        # Login password for machines within the node group
        self.login_password = login_password
        # Node group name
        self.new_node_group_name = new_node_group_name
        # Node group ID
        self.node_group_id = node_group_id
        # User-defined script
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_system_mount_enabled is not None:
            result['FileSystemMountEnabled'] = self.file_system_mount_enabled

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name

        if self.login_password is not None:
            result['LoginPassword'] = self.login_password

        if self.new_node_group_name is not None:
            result['NewNodeGroupName'] = self.new_node_group_name

        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemMountEnabled') is not None:
            self.file_system_mount_enabled = m.get('FileSystemMountEnabled')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')

        if m.get('LoginPassword') is not None:
            self.login_password = m.get('LoginPassword')

        if m.get('NewNodeGroupName') is not None:
            self.new_node_group_name = m.get('NewNodeGroupName')

        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

