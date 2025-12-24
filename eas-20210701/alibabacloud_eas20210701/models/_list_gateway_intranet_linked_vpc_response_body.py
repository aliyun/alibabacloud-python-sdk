# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eas20210701 import models as main_models
from darabonba.model import DaraModel

class ListGatewayIntranetLinkedVpcResponseBody(DaraModel):
    def __init__(
        self,
        gateway_id: str = None,
        intranet_linked_vpc_list: List[main_models.ListGatewayIntranetLinkedVpcResponseBodyIntranetLinkedVpcList] = None,
        request_id: str = None,
    ):
        # The private gateway ID.
        self.gateway_id = gateway_id
        # The internal endpoints.
        self.intranet_linked_vpc_list = intranet_linked_vpc_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.intranet_linked_vpc_list:
            for v1 in self.intranet_linked_vpc_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id

        result['IntranetLinkedVpcList'] = []
        if self.intranet_linked_vpc_list is not None:
            for k1 in self.intranet_linked_vpc_list:
                result['IntranetLinkedVpcList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')

        self.intranet_linked_vpc_list = []
        if m.get('IntranetLinkedVpcList') is not None:
            for k1 in m.get('IntranetLinkedVpcList'):
                temp_model = main_models.ListGatewayIntranetLinkedVpcResponseBodyIntranetLinkedVpcList()
                self.intranet_linked_vpc_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListGatewayIntranetLinkedVpcResponseBodyIntranetLinkedVpcList(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        authoritative_dns_enabled: bool = None,
        ip: str = None,
        security_group_id: str = None,
        status: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        self.account_id = account_id
        self.authoritative_dns_enabled = authoritative_dns_enabled
        # The IP address.
        self.ip = ip
        # The security group ID.
        self.security_group_id = security_group_id
        # The state of the private gateway.
        # 
        # Valid values:
        # 
        # *   Creating
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     The private gateway is being created.
        # 
        #     <!-- -->
        # 
        # *   Running
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     The private gateway is running.
        # 
        #     <!-- -->
        self.status = status
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The virtual private cloud (VPC) ID.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.authoritative_dns_enabled is not None:
            result['AuthoritativeDnsEnabled'] = self.authoritative_dns_enabled

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.status is not None:
            result['Status'] = self.status

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('AuthoritativeDnsEnabled') is not None:
            self.authoritative_dns_enabled = m.get('AuthoritativeDnsEnabled')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

