# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeNetworksResponseBody(DaraModel):
    def __init__(
        self,
        networks: main_models.DescribeNetworksResponseBodyNetworks = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The VPCs.
        self.networks = networks
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned on each page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries in the list.
        self.total_count = total_count

    def validate(self):
        if self.networks:
            self.networks.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.networks is not None:
            result['Networks'] = self.networks.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Networks') is not None:
            temp_model = main_models.DescribeNetworksResponseBodyNetworks()
            self.networks = temp_model.from_map(m.get('Networks'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeNetworksResponseBodyNetworks(DaraModel):
    def __init__(
        self,
        network: List[main_models.DescribeNetworksResponseBodyNetworksNetwork] = None,
    ):
        self.network = network

    def validate(self):
        if self.network:
            for v1 in self.network:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Network'] = []
        if self.network is not None:
            for k1 in self.network:
                result['Network'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.network = []
        if m.get('Network') is not None:
            for k1 in m.get('Network'):
                temp_model = main_models.DescribeNetworksResponseBodyNetworksNetwork()
                self.network.append(temp_model.from_map(k1))

        return self

class DescribeNetworksResponseBodyNetworksNetwork(DaraModel):
    def __init__(
        self,
        cidr_block: str = None,
        created_time: str = None,
        description: str = None,
        ens_region_id: str = None,
        gateway_route_table_id: str = None,
        network_acl_id: str = None,
        network_id: str = None,
        network_name: str = None,
        route_table_id: str = None,
        route_table_ids: main_models.DescribeNetworksResponseBodyNetworksNetworkRouteTableIds = None,
        router_table_id: str = None,
        secondary_cidr_blocks: main_models.DescribeNetworksResponseBodyNetworksNetworkSecondaryCidrBlocks = None,
        status: str = None,
        tags: main_models.DescribeNetworksResponseBodyNetworksNetworkTags = None,
        v_switch_ids: main_models.DescribeNetworksResponseBodyNetworksNetworkVSwitchIds = None,
    ):
        # The IPv4 CIDR block of the network.
        self.cidr_block = cidr_block
        # The timestamp when the instance was created. Unit: milliseconds.
        self.created_time = created_time
        # The description of the network.
        self.description = description
        # The ID of the edge node.
        self.ens_region_id = ens_region_id
        # The ID of the gateway route table.
        self.gateway_route_table_id = gateway_route_table_id
        # The ID of the network access control list (ACL).
        self.network_acl_id = network_acl_id
        # The ID of the network.
        self.network_id = network_id
        # The name of the network.
        self.network_name = network_name
        # The ID of the route table.
        self.route_table_id = route_table_id
        # The IDs of the route tables.
        self.route_table_ids = route_table_ids
        # The route table ID.
        self.router_table_id = router_table_id
        self.secondary_cidr_blocks = secondary_cidr_blocks
        # The status of the network. Valid values:
        # 
        # *   Pending
        # *   Available
        self.status = status
        self.tags = tags
        # The list of vSwitches in the network.
        self.v_switch_ids = v_switch_ids

    def validate(self):
        if self.route_table_ids:
            self.route_table_ids.validate()
        if self.secondary_cidr_blocks:
            self.secondary_cidr_blocks.validate()
        if self.tags:
            self.tags.validate()
        if self.v_switch_ids:
            self.v_switch_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.description is not None:
            result['Description'] = self.description

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.gateway_route_table_id is not None:
            result['GatewayRouteTableId'] = self.gateway_route_table_id

        if self.network_acl_id is not None:
            result['NetworkAclId'] = self.network_acl_id

        if self.network_id is not None:
            result['NetworkId'] = self.network_id

        if self.network_name is not None:
            result['NetworkName'] = self.network_name

        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id

        if self.route_table_ids is not None:
            result['RouteTableIds'] = self.route_table_ids.to_map()

        if self.router_table_id is not None:
            result['RouterTableId'] = self.router_table_id

        if self.secondary_cidr_blocks is not None:
            result['SecondaryCidrBlocks'] = self.secondary_cidr_blocks.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('GatewayRouteTableId') is not None:
            self.gateway_route_table_id = m.get('GatewayRouteTableId')

        if m.get('NetworkAclId') is not None:
            self.network_acl_id = m.get('NetworkAclId')

        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')

        if m.get('NetworkName') is not None:
            self.network_name = m.get('NetworkName')

        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')

        if m.get('RouteTableIds') is not None:
            temp_model = main_models.DescribeNetworksResponseBodyNetworksNetworkRouteTableIds()
            self.route_table_ids = temp_model.from_map(m.get('RouteTableIds'))

        if m.get('RouterTableId') is not None:
            self.router_table_id = m.get('RouterTableId')

        if m.get('SecondaryCidrBlocks') is not None:
            temp_model = main_models.DescribeNetworksResponseBodyNetworksNetworkSecondaryCidrBlocks()
            self.secondary_cidr_blocks = temp_model.from_map(m.get('SecondaryCidrBlocks'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeNetworksResponseBodyNetworksNetworkTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('VSwitchIds') is not None:
            temp_model = main_models.DescribeNetworksResponseBodyNetworksNetworkVSwitchIds()
            self.v_switch_ids = temp_model.from_map(m.get('VSwitchIds'))

        return self

class DescribeNetworksResponseBodyNetworksNetworkVSwitchIds(DaraModel):
    def __init__(
        self,
        v_switch_id: List[str] = None,
    ):
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

class DescribeNetworksResponseBodyNetworksNetworkTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeNetworksResponseBodyNetworksNetworkTagsTag] = None,
    ):
        self.tag = tag

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
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeNetworksResponseBodyNetworksNetworkTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeNetworksResponseBodyNetworksNetworkTagsTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        tag_key: str = None,
        tag_value: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        self.tag_key = tag_key
        self.tag_value = tag_value
        # The bandwidth.
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

        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeNetworksResponseBodyNetworksNetworkSecondaryCidrBlocks(DaraModel):
    def __init__(
        self,
        secondary_cidr_block: List[str] = None,
    ):
        self.secondary_cidr_block = secondary_cidr_block

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.secondary_cidr_block is not None:
            result['SecondaryCidrBlock'] = self.secondary_cidr_block

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecondaryCidrBlock') is not None:
            self.secondary_cidr_block = m.get('SecondaryCidrBlock')

        return self

class DescribeNetworksResponseBodyNetworksNetworkRouteTableIds(DaraModel):
    def __init__(
        self,
        route_table_id: List[str] = None,
    ):
        self.route_table_id = route_table_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')

        return self

