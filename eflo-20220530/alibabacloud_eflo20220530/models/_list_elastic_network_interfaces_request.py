# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eflo20220530 import models as main_models
from darabonba.model import DaraModel

class ListElasticNetworkInterfacesRequest(DaraModel):
    def __init__(
        self,
        elastic_network_interface_id: str = None,
        ip: str = None,
        network_type: str = None,
        node_id: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        status: str = None,
        tag: List[main_models.ListElasticNetworkInterfacesRequestTag] = None,
        type: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # Lingjun Elastic Network Interface ID
        self.elastic_network_interface_id = elastic_network_interface_id
        # The IP address of the BE cluster.
        self.ip = ip
        # The network type.
        # 
        # Valid value:
        # 
        # *   Tenant: Tenant.
        # *   VPC
        self.network_type = network_type
        # The ID of the node.
        self.node_id = node_id
        # The page number of the page to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: 20.
        self.page_size = page_size
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The status of the enterprise-level snapshot policy.
        # 
        # Valid value:
        # 
        # *   Create Failed: the creation failure.
        # *   Delete Failed: the that failed to be deleted.
        # *   Executing
        # *   Available: The template is available.
        # *   Deleting
        self.status = status
        # List of Tags
        self.tag = tag
        # The type of the variable.
        # 
        # Valid value:
        # 
        # *   CUSTOM: custom type.
        # *   DEFAULT: system type.
        self.type = type
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The ID of the virtual private cloud (VPC).
        self.vpc_id = vpc_id
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.elastic_network_interface_id is not None:
            result['ElasticNetworkInterfaceId'] = self.elastic_network_interface_id

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['Status'] = self.status

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ElasticNetworkInterfaceId') is not None:
            self.elastic_network_interface_id = m.get('ElasticNetworkInterfaceId')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListElasticNetworkInterfacesRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class ListElasticNetworkInterfacesRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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

