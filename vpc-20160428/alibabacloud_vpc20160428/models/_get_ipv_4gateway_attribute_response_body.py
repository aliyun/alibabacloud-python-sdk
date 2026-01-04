# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class GetIpv4GatewayAttributeResponseBody(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        enabled: bool = None,
        ipv_4gateway_description: str = None,
        ipv_4gateway_id: str = None,
        ipv_4gateway_name: str = None,
        ipv_4gateway_route_table_id: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        status: str = None,
        tags: List[main_models.GetIpv4GatewayAttributeResponseBodyTags] = None,
        vpc_id: str = None,
    ):
        # The time when the IPv4 gateway was created.
        self.create_time = create_time
        # Indicates whether the IPv4 gateway is activated. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.enabled = enabled
        # The description of the IPv4 gateway.
        self.ipv_4gateway_description = ipv_4gateway_description
        # The ID of the IPv4 gateway.
        self.ipv_4gateway_id = ipv_4gateway_id
        # The name of the IPv4 gateway.
        self.ipv_4gateway_name = ipv_4gateway_name
        # The ID of the route table associated with the IPv4 gateway.
        self.ipv_4gateway_route_table_id = ipv_4gateway_route_table_id
        # The request ID.
        self.request_id = request_id
        # The ID of the resource group to which the IPv4 gateway belongs.
        self.resource_group_id = resource_group_id
        # The status of the IPv4 gateway. Valid values:
        # 
        # *   **Creating**
        # *   **Created**
        # *   **Modifying**
        # *   **Deleting**
        # *   **Deleted**
        # *   **Activating**
        self.status = status
        # The tag list.
        self.tags = tags
        # The ID of the VPC with which the IPv4 gateway is associated.
        self.vpc_id = vpc_id

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.ipv_4gateway_description is not None:
            result['Ipv4GatewayDescription'] = self.ipv_4gateway_description

        if self.ipv_4gateway_id is not None:
            result['Ipv4GatewayId'] = self.ipv_4gateway_id

        if self.ipv_4gateway_name is not None:
            result['Ipv4GatewayName'] = self.ipv_4gateway_name

        if self.ipv_4gateway_route_table_id is not None:
            result['Ipv4GatewayRouteTableId'] = self.ipv_4gateway_route_table_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('Ipv4GatewayDescription') is not None:
            self.ipv_4gateway_description = m.get('Ipv4GatewayDescription')

        if m.get('Ipv4GatewayId') is not None:
            self.ipv_4gateway_id = m.get('Ipv4GatewayId')

        if m.get('Ipv4GatewayName') is not None:
            self.ipv_4gateway_name = m.get('Ipv4GatewayName')

        if m.get('Ipv4GatewayRouteTableId') is not None:
            self.ipv_4gateway_route_table_id = m.get('Ipv4GatewayRouteTableId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetIpv4GatewayAttributeResponseBodyTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class GetIpv4GatewayAttributeResponseBodyTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N added to the resource.
        self.key = key
        # The value of tag N added to the resource.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

