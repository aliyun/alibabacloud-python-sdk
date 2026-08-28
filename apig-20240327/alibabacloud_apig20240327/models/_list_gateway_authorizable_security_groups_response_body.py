# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class ListGatewayAuthorizableSecurityGroupsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListGatewayAuthorizableSecurityGroupsResponseBodyData = None,
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
            temp_model = main_models.ListGatewayAuthorizableSecurityGroupsResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListGatewayAuthorizableSecurityGroupsResponseBodyData(DaraModel):
    def __init__(
        self,
        items: List[main_models.ListGatewayAuthorizableSecurityGroupsResponseBodyDataItems] = None,
    ):
        # The security groups.
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
                temp_model = main_models.ListGatewayAuthorizableSecurityGroupsResponseBodyDataItems()
                self.items.append(temp_model.from_map(k1))

        return self

class ListGatewayAuthorizableSecurityGroupsResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        name: str = None,
        security_group_id: str = None,
        type: str = None,
        vpc_id: str = None,
    ):
        # The security group name.
        self.name = name
        # The security group ID.
        self.security_group_id = security_group_id
        # The type of the security group. Valid values:
        # 
        # *   Normal: general security group
        # *   Enterprise: enterprise security group
        self.type = type
        # The virtual private cloud (VPC) ID.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id

        if self.type is not None:
            result['type'] = self.type

        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')

        return self

