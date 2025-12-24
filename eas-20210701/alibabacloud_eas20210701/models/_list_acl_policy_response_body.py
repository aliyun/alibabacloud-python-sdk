# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eas20210701 import models as main_models
from darabonba.model import DaraModel

class ListAclPolicyResponseBody(DaraModel):
    def __init__(
        self,
        gateway_id: str = None,
        internet_acl_policy_list: List[main_models.ListAclPolicyResponseBodyInternetAclPolicyList] = None,
        intranet_vpc_acl_policy_list: List[main_models.ListAclPolicyResponseBodyIntranetVpcAclPolicyList] = None,
        request_id: str = None,
    ):
        # The private gateway ID.
        self.gateway_id = gateway_id
        # The access control policies of the private gateway over the Internet.
        self.internet_acl_policy_list = internet_acl_policy_list
        # The access control policies of the private gateway over the internal network.
        self.intranet_vpc_acl_policy_list = intranet_vpc_acl_policy_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.internet_acl_policy_list:
            for v1 in self.internet_acl_policy_list:
                 if v1:
                    v1.validate()
        if self.intranet_vpc_acl_policy_list:
            for v1 in self.intranet_vpc_acl_policy_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id

        result['InternetAclPolicyList'] = []
        if self.internet_acl_policy_list is not None:
            for k1 in self.internet_acl_policy_list:
                result['InternetAclPolicyList'].append(k1.to_map() if k1 else None)

        result['IntranetVpcAclPolicyList'] = []
        if self.intranet_vpc_acl_policy_list is not None:
            for k1 in self.intranet_vpc_acl_policy_list:
                result['IntranetVpcAclPolicyList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')

        self.internet_acl_policy_list = []
        if m.get('InternetAclPolicyList') is not None:
            for k1 in m.get('InternetAclPolicyList'):
                temp_model = main_models.ListAclPolicyResponseBodyInternetAclPolicyList()
                self.internet_acl_policy_list.append(temp_model.from_map(k1))

        self.intranet_vpc_acl_policy_list = []
        if m.get('IntranetVpcAclPolicyList') is not None:
            for k1 in m.get('IntranetVpcAclPolicyList'):
                temp_model = main_models.ListAclPolicyResponseBodyIntranetVpcAclPolicyList()
                self.intranet_vpc_acl_policy_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListAclPolicyResponseBodyIntranetVpcAclPolicyList(DaraModel):
    def __init__(
        self,
        acl_policy_list: List[main_models.ListAclPolicyResponseBodyIntranetVpcAclPolicyListAclPolicyList] = None,
        vpc_id: str = None,
    ):
        # The whitelisted IP CIDR blocks in the VPC that can access the private gateway over the internal network.
        self.acl_policy_list = acl_policy_list
        # The VPC ID. For more information about how to obtain the VPC ID, see DescribeVpcs.
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
                temp_model = main_models.ListAclPolicyResponseBodyIntranetVpcAclPolicyListAclPolicyList()
                self.acl_policy_list.append(temp_model.from_map(k1))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class ListAclPolicyResponseBodyIntranetVpcAclPolicyListAclPolicyList(DaraModel):
    def __init__(
        self,
        comment: str = None,
        entry: str = None,
    ):
        # The comment on the IP CIDR block in the VPC that can access the private gateway over the internal network.
        self.comment = comment
        # The IP CIDR block in the VPC that can access the private gateway over the internal network.
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

class ListAclPolicyResponseBodyInternetAclPolicyList(DaraModel):
    def __init__(
        self,
        acl_policy_list: List[main_models.ListAclPolicyResponseBodyInternetAclPolicyListAclPolicyList] = None,
    ):
        # The whitelisted IP CIDR blocks in the VPC that can access the private gateway over the Internet.
        self.acl_policy_list = acl_policy_list

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.acl_policy_list = []
        if m.get('AclPolicyList') is not None:
            for k1 in m.get('AclPolicyList'):
                temp_model = main_models.ListAclPolicyResponseBodyInternetAclPolicyListAclPolicyList()
                self.acl_policy_list.append(temp_model.from_map(k1))

        return self

class ListAclPolicyResponseBodyInternetAclPolicyListAclPolicyList(DaraModel):
    def __init__(
        self,
        comment: str = None,
        entry: str = None,
    ):
        # The comment on the IP CIDR block in the VPC that can access the private gateway over the Internet.
        self.comment = comment
        # The IP CIDR block in the VPC that can access the private gateway over the Internet.
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

