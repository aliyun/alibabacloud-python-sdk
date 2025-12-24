# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAclPolicyShrinkRequest(DaraModel):
    def __init__(
        self,
        acl_policy_list_shrink: str = None,
        vpc_id: str = None,
    ):
        # The whitelisted IP CIDR blocks in the VPC that can access the private gateway.
        self.acl_policy_list_shrink = acl_policy_list_shrink
        # The ID of the virtual private cloud (VPC). For more information about how to obtain the VPC ID, see DescribeVpcs.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_policy_list_shrink is not None:
            result['AclPolicyList'] = self.acl_policy_list_shrink

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclPolicyList') is not None:
            self.acl_policy_list_shrink = m.get('AclPolicyList')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

