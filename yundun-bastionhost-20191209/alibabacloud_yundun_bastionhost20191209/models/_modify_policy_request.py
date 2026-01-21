# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyPolicyRequest(DaraModel):
    def __init__(
        self,
        comment: str = None,
        instance_id: str = None,
        policy_id: str = None,
        policy_name: str = None,
        priority: str = None,
        region_id: str = None,
    ):
        # The new remarks of the control policy.
        self.comment = comment
        # The ID of the bastion host to which the control policy to modify belongs.
        # 
        # > You can call the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to query the bastion host ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the control policy that you want to modify.
        # 
        # This parameter is required.
        self.policy_id = policy_id
        # The new name of the control policy.
        self.policy_name = policy_name
        # The priority of the modified control policy. Valid values: 1 to 100. The smaller the value, the higher the priority. Default value: 1.
        self.priority = priority
        # The region ID of the bastion host to which the control policy to modify belongs.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

