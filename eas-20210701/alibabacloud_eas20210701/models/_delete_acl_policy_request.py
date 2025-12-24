# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eas20210701 import models as main_models
from darabonba.model import DaraModel

class DeleteAclPolicyRequest(DaraModel):
    def __init__(
        self,
        acl_policy_list: List[main_models.DeleteAclPolicyRequestAclPolicyList] = None,
        vpc_id: str = None,
    ):
        # The whitelisted IP CIDR blocks in the VPC that can access the private gateway.
        self.acl_policy_list = acl_policy_list
        # The ID of the virtual private cloud (VPC). For more information about how to obtain the VPC ID, see DescribeVpcs.
        self.vpc_id = vpc_id

    def validate(self):
        if self.acl_policy_list:
            for v1 in self.acl_policy_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AclPolicyList'] = []
        if self.acl_policy_list is not None:
            for k1 in self.acl_policy_list:
                result['AclPolicyList'].append(k1.to_map() if k1 else None)

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.acl_policy_list = []
        if m.get('AclPolicyList') is not None:
            for k1 in m.get('AclPolicyList'):
                temp_model = main_models.DeleteAclPolicyRequestAclPolicyList()
                self.acl_policy_list.append(temp_model.from_map(k1))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class DeleteAclPolicyRequestAclPolicyList(DaraModel):
    def __init__(
        self,
        comment: str = None,
        entry: str = None,
    ):
        # The comment on the IP CIDR block in the VPC that can access the private gateway.
        self.comment = comment
        # The IP CIDR block in the VPC that can access the private gateway.
        self.entry = entry

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.entry is not None:
            result['Entry'] = self.entry

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('Entry') is not None:
            self.entry = m.get('Entry')

        return self

