# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeVpcFirewallAclGroupListResponseBody(DaraModel):
    def __init__(
        self,
        acl_group_list: List[main_models.DescribeVpcFirewallAclGroupListResponseBodyAclGroupList] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information about the access control policy groups.
        self.acl_group_list = acl_group_list
        # The ID of the request.
        self.request_id = request_id
        # The total number of the policy groups that are returned.
        self.total_count = total_count

    def validate(self):
        if self.acl_group_list:
            for v1 in self.acl_group_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AclGroupList'] = []
        if self.acl_group_list is not None:
            for k1 in self.acl_group_list:
                result['AclGroupList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.acl_group_list = []
        if m.get('AclGroupList') is not None:
            for k1 in m.get('AclGroupList'):
                temp_model = main_models.DescribeVpcFirewallAclGroupListResponseBodyAclGroupList()
                self.acl_group_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeVpcFirewallAclGroupListResponseBodyAclGroupList(DaraModel):
    def __init__(
        self,
        acl_config: main_models.DescribeVpcFirewallAclGroupListResponseBodyAclGroupListAclConfig = None,
        acl_group_id: str = None,
        acl_group_name: str = None,
        acl_rule_count: int = None,
        is_default: bool = None,
        member_uid: str = None,
    ):
        # ACL engine mode.
        self.acl_config = acl_config
        # The ID of the policy group.
        # 
        # Valid values:
        # 
        # *   If the VPC firewall is used to protect a Cloud Enterprise Network (CEN) instance, the value of this parameter is the ID of the CEN instance.
        # 
        #     Example: cen-ervw0g12b5jbw\\*\\*\\*\\*
        # 
        # *   If the VPC firewall is used to protect an Express Connect circuit, the value of this parameter is the instance ID of the VPC firewall.
        # 
        #     Example: vfw-a42bbb7b887148c9\\*\\*\\*\\*
        self.acl_group_id = acl_group_id
        # The name of the policy group. Valid values:
        # 
        # *   If the VPC firewall is used to protect a CEN instance, the value of this parameter is the name of the CEN instance.
        # *   If the VPC firewall is used to protect an Express Connect circuit, the value of this parameter is the instance name of the VPC firewall.
        self.acl_group_name = acl_group_name
        # The number of access control policies in the policy group.
        self.acl_rule_count = acl_rule_count
        # Whether it is the default firewall. Values:
        # 
        # *   **true**: It is the default firewall.
        # *   **false**: It is not the default firewall.
        self.is_default = is_default
        # The UID of the member that is managed by your Alibaba Cloud account.
        self.member_uid = member_uid

    def validate(self):
        if self.acl_config:
            self.acl_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_config is not None:
            result['AclConfig'] = self.acl_config.to_map()

        if self.acl_group_id is not None:
            result['AclGroupId'] = self.acl_group_id

        if self.acl_group_name is not None:
            result['AclGroupName'] = self.acl_group_name

        if self.acl_rule_count is not None:
            result['AclRuleCount'] = self.acl_rule_count

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclConfig') is not None:
            temp_model = main_models.DescribeVpcFirewallAclGroupListResponseBodyAclGroupListAclConfig()
            self.acl_config = temp_model.from_map(m.get('AclConfig'))

        if m.get('AclGroupId') is not None:
            self.acl_group_id = m.get('AclGroupId')

        if m.get('AclGroupName') is not None:
            self.acl_group_name = m.get('AclGroupName')

        if m.get('AclRuleCount') is not None:
            self.acl_rule_count = m.get('AclRuleCount')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')

        return self

class DescribeVpcFirewallAclGroupListResponseBodyAclGroupListAclConfig(DaraModel):
    def __init__(
        self,
        strict_mode: int = None,
    ):
        # Specifies Whether strict mode is enabled. Valid values:
        # *   1: yes
        # *   0: no
        self.strict_mode = strict_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.strict_mode is not None:
            result['StrictMode'] = self.strict_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StrictMode') is not None:
            self.strict_mode = m.get('StrictMode')

        return self

