# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetPolicyApprovalConfigShrinkRequest(DaraModel):
    def __init__(
        self,
        approval_config_shrink: str = None,
        instance_id: str = None,
        policy_id: str = None,
        project_id: int = None,
        region_id: str = None,
    ):
        # The O&M approval configuration in the control policy.
        # 
        # This parameter is required.
        self.approval_config_shrink = approval_config_shrink
        # The Bastionhost instance ID.
        # > You can call the DescribeInstances operation to obtain the Bastionhost instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the control policy that you want to modify.
        # > You can call the [ListPolicies](https://help.aliyun.com/document_detail/2758876.html) operation to obtain the value of this parameter.
        # 
        # This parameter is required.
        self.policy_id = policy_id
        # The project ID.
        self.project_id = project_id
        # The region ID of the Bastionhost instance.
        # > For the mappings between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.approval_config_shrink is not None:
            result['ApprovalConfig'] = self.approval_config_shrink

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovalConfig') is not None:
            self.approval_config_shrink = m.get('ApprovalConfig')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

