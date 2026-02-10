# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartVirusScanTaskRequest(DaraModel):
    def __init__(
        self,
        target_info: str = None,
    ):
        # The asset on which you want to perform a virus scan task. You can select servers or server groups to scan for viruses. The value is a string that consists of JSON arrays. Each element in a JSON array is a JSON struct that contains the following fields:
        # 
        # *   **type**: the type of the asset on which you want to perform a virus scan task. Valid values:
        # 
        #     *   **groupId**: server group.
        #     *   **uuid**: server.
        # 
        # *   **name**: the name of the server or server group.
        # 
        # *   **target**: the asset on which you want to perform a virus scan task. Valid values:
        # 
        #     *   If you set **type** to **groupId**, you must set this field to the ID of the server group. You can call the [DescribeAllGroups](~~DescribeAllGroups~~) operation to query the IDs of server groups.
        #     *   If you set **type** to **uuid**, you must set this field to the UUID of the server. You can call the [DescribeCloudCenterInstances](~~DescribeCloudCenterInstances~~) operation to query the UUIDs of servers.
        # 
        # This parameter is required.
        self.target_info = target_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.target_info is not None:
            result['TargetInfo'] = self.target_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TargetInfo') is not None:
            self.target_info = m.get('TargetInfo')

        return self

