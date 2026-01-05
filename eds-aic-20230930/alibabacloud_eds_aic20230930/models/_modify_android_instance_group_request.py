# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyAndroidInstanceGroupRequest(DaraModel):
    def __init__(
        self,
        instance_group_id: str = None,
        new_instance_group_name: str = None,
        policy_group_id: str = None,
        stream_mode: int = None,
    ):
        # The ID of the instance group.
        self.instance_group_id = instance_group_id
        # The new name of the instance group.
        # 
        # > 
        # 
        # *   The name can be up to 30 characters in length. It can contain letters, digits, colons (:), underscores (_), periods (.), or hyphens (-). It must start with letters but cannot start with http:// or https://.
        self.new_instance_group_name = new_instance_group_name
        # The ID of the policy.
        self.policy_group_id = policy_group_id
        self.stream_mode = stream_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_group_id is not None:
            result['InstanceGroupId'] = self.instance_group_id

        if self.new_instance_group_name is not None:
            result['NewInstanceGroupName'] = self.new_instance_group_name

        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id

        if self.stream_mode is not None:
            result['StreamMode'] = self.stream_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceGroupId') is not None:
            self.instance_group_id = m.get('InstanceGroupId')

        if m.get('NewInstanceGroupName') is not None:
            self.new_instance_group_name = m.get('NewInstanceGroupName')

        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')

        if m.get('StreamMode') is not None:
            self.stream_mode = m.get('StreamMode')

        return self

