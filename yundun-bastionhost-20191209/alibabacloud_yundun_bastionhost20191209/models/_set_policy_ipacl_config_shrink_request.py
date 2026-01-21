# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetPolicyIPAclConfigShrinkRequest(DaraModel):
    def __init__(
        self,
        ipacl_config_shrink: str = None,
        instance_id: str = None,
        policy_id: str = None,
        region_id: str = None,
    ):
        # The access control settings for source IP addresses.
        # 
        # This parameter is required.
        self.ipacl_config_shrink = ipacl_config_shrink
        # The bastion host ID.
        # 
        # > You can call the DescribeInstances operation to query the bastion host ID.[](~~153281~~)
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the control policy that you want to modify.
        # 
        # >  You can call the [ListPolicies](https://help.aliyun.com/document_detail/2758876.html) operation to query the control policy ID.
        # 
        # This parameter is required.
        self.policy_id = policy_id
        # The region ID of the bastion host.
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
        if self.ipacl_config_shrink is not None:
            result['IPAclConfig'] = self.ipacl_config_shrink

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IPAclConfig') is not None:
            self.ipacl_config_shrink = m.get('IPAclConfig')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

