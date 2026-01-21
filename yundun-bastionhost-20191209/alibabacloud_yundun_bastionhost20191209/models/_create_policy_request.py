# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePolicyRequest(DaraModel):
    def __init__(
        self,
        comment: str = None,
        instance_id: str = None,
        policy_name: str = None,
        priority: str = None,
        region_id: str = None,
    ):
        # The remarks of the control policy. The remarks can be up to 500 characters in length.
        self.comment = comment
        # The ID of the bastion host for which you want to create a control policy.
        # 
        # > You can call the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to query the ID of the bastion host.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the control policy. The name can be up to 128 characters in length.
        # 
        # This parameter is required.
        self.policy_name = policy_name
        # The priority of the control policy.
        # 
        # *   Valid values: 1 to 100. The default value is 1, which indicates the highest priority.
        # *   You can configure the same priority for different control policies. If multiple control policies have the same priority, the control policy that is created at the latest point in time has the highest priority. If a command control policy and a command approval policy contain the same commands, the commands are prioritized in descending order: reject, allow, and approve. In access control policies, a blacklist has a higher priority than a whitelist.
        self.priority = priority
        # The region ID of the bastion host for which you want to create a control policy.
        # 
        # >  For more information about the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
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

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

