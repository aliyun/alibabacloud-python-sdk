# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class ListGatewayAuthorizedSecurityGroupRulesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListGatewayAuthorizedSecurityGroupRulesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code.
        self.code = code
        # The returned data.
        self.data = data
        # The response message returned.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.ListGatewayAuthorizedSecurityGroupRulesResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListGatewayAuthorizedSecurityGroupRulesResponseBodyData(DaraModel):
    def __init__(
        self,
        items: List[main_models.ListGatewayAuthorizedSecurityGroupRulesResponseBodyDataItems] = None,
    ):
        # The security group rules.
        self.items = items

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.ListGatewayAuthorizedSecurityGroupRulesResponseBodyDataItems()
                self.items.append(temp_model.from_map(k1))

        return self

class ListGatewayAuthorizedSecurityGroupRulesResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        auth_cidrs: List[str] = None,
        description: str = None,
        ip_protocol: str = None,
        port_range: str = None,
        security_group_id: str = None,
        security_group_name: str = None,
        security_group_rule_id: str = None,
        source_security_group_id: str = None,
        vpc_id: str = None,
    ):
        # The list of authorized CIDR blocks.
        self.auth_cidrs = auth_cidrs
        # The rule description.
        self.description = description
        # The protocol. Valid values:
        # 
        # *   TCP
        self.ip_protocol = ip_protocol
        # The port range.
        self.port_range = port_range
        # The security group ID.
        self.security_group_id = security_group_id
        # The security group name.
        self.security_group_name = security_group_name
        # The rule ID.
        self.security_group_rule_id = security_group_rule_id
        # The ID of the source security group.
        self.source_security_group_id = source_security_group_id
        # The virtual private cloud (VPC) ID.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_cidrs is not None:
            result['authCidrs'] = self.auth_cidrs

        if self.description is not None:
            result['description'] = self.description

        if self.ip_protocol is not None:
            result['ipProtocol'] = self.ip_protocol

        if self.port_range is not None:
            result['portRange'] = self.port_range

        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id

        if self.security_group_name is not None:
            result['securityGroupName'] = self.security_group_name

        if self.security_group_rule_id is not None:
            result['securityGroupRuleId'] = self.security_group_rule_id

        if self.source_security_group_id is not None:
            result['sourceSecurityGroupId'] = self.source_security_group_id

        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authCidrs') is not None:
            self.auth_cidrs = m.get('authCidrs')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('ipProtocol') is not None:
            self.ip_protocol = m.get('ipProtocol')

        if m.get('portRange') is not None:
            self.port_range = m.get('portRange')

        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')

        if m.get('securityGroupName') is not None:
            self.security_group_name = m.get('securityGroupName')

        if m.get('securityGroupRuleId') is not None:
            self.security_group_rule_id = m.get('securityGroupRuleId')

        if m.get('sourceSecurityGroupId') is not None:
            self.source_security_group_id = m.get('sourceSecurityGroupId')

        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')

        return self

