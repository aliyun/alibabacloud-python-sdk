# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smartag20180313 import models as main_models
from darabonba.model import DaraModel

class DescribeCloudConnectNetworksResponseBody(DaraModel):
    def __init__(
        self,
        cloud_connect_networks: main_models.DescribeCloudConnectNetworksResponseBodyCloudConnectNetworks = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.cloud_connect_networks = cloud_connect_networks
        # The page number.
        self.page_number = page_number
        # The number of entries to return on each page for paging in a paged query.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.cloud_connect_networks:
            self.cloud_connect_networks.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cloud_connect_networks is not None:
            result['CloudConnectNetworks'] = self.cloud_connect_networks.to_map()

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
        if m.get('CloudConnectNetworks') is not None:
            temp_model = main_models.DescribeCloudConnectNetworksResponseBodyCloudConnectNetworks()
            self.cloud_connect_networks = temp_model.from_map(m.get('CloudConnectNetworks'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeCloudConnectNetworksResponseBodyCloudConnectNetworks(DaraModel):
    def __init__(
        self,
        cloud_connect_network: List[main_models.DescribeCloudConnectNetworksResponseBodyCloudConnectNetworksCloudConnectNetwork] = None,
    ):
        self.cloud_connect_network = cloud_connect_network

    def validate(self):
        if self.cloud_connect_network:
            for v1 in self.cloud_connect_network:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CloudConnectNetwork'] = []
        if self.cloud_connect_network is not None:
            for k1 in self.cloud_connect_network:
                result['CloudConnectNetwork'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cloud_connect_network = []
        if m.get('CloudConnectNetwork') is not None:
            for k1 in m.get('CloudConnectNetwork'):
                temp_model = main_models.DescribeCloudConnectNetworksResponseBodyCloudConnectNetworksCloudConnectNetwork()
                self.cloud_connect_network.append(temp_model.from_map(k1))

        return self

class DescribeCloudConnectNetworksResponseBodyCloudConnectNetworksCloudConnectNetwork(DaraModel):
    def __init__(
        self,
        associated_cen_id: str = None,
        associated_cen_owner_id: str = None,
        associated_cen_status: str = None,
        associated_cloud_box_count: str = None,
        associated_vpc_status: str = None,
        available_cloud_box_count: str = None,
        ccn_id: str = None,
        cen_status_error_code: str = None,
        cen_status_error_message: str = None,
        cidr_block: str = None,
        create_time: int = None,
        description: str = None,
        interworking_status: str = None,
        name: str = None,
        new_agw: bool = None,
        processing_cen_id: str = None,
        resource_group_id: str = None,
        snat_cidr_block: str = None,
        subnet: str = None,
        tags: main_models.DescribeCloudConnectNetworksResponseBodyCloudConnectNetworksCloudConnectNetworkTags = None,
        tr_network_config: main_models.DescribeCloudConnectNetworksResponseBodyCloudConnectNetworksCloudConnectNetworkTrNetworkConfig = None,
        vpc_network_config: main_models.DescribeCloudConnectNetworksResponseBodyCloudConnectNetworksCloudConnectNetworkVpcNetworkConfig = None,
        vpc_status_error_code: str = None,
        vpc_status_error_message: str = None,
    ):
        self.associated_cen_id = associated_cen_id
        self.associated_cen_owner_id = associated_cen_owner_id
        self.associated_cen_status = associated_cen_status
        self.associated_cloud_box_count = associated_cloud_box_count
        self.associated_vpc_status = associated_vpc_status
        self.available_cloud_box_count = available_cloud_box_count
        self.ccn_id = ccn_id
        self.cen_status_error_code = cen_status_error_code
        self.cen_status_error_message = cen_status_error_message
        self.cidr_block = cidr_block
        self.create_time = create_time
        self.description = description
        self.interworking_status = interworking_status
        self.name = name
        self.new_agw = new_agw
        self.processing_cen_id = processing_cen_id
        self.resource_group_id = resource_group_id
        self.snat_cidr_block = snat_cidr_block
        self.subnet = subnet
        self.tags = tags
        self.tr_network_config = tr_network_config
        self.vpc_network_config = vpc_network_config
        self.vpc_status_error_code = vpc_status_error_code
        self.vpc_status_error_message = vpc_status_error_message

    def validate(self):
        if self.tags:
            self.tags.validate()
        if self.tr_network_config:
            self.tr_network_config.validate()
        if self.vpc_network_config:
            self.vpc_network_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.associated_cen_id is not None:
            result['AssociatedCenId'] = self.associated_cen_id

        if self.associated_cen_owner_id is not None:
            result['AssociatedCenOwnerId'] = self.associated_cen_owner_id

        if self.associated_cen_status is not None:
            result['AssociatedCenStatus'] = self.associated_cen_status

        if self.associated_cloud_box_count is not None:
            result['AssociatedCloudBoxCount'] = self.associated_cloud_box_count

        if self.associated_vpc_status is not None:
            result['AssociatedVpcStatus'] = self.associated_vpc_status

        if self.available_cloud_box_count is not None:
            result['AvailableCloudBoxCount'] = self.available_cloud_box_count

        if self.ccn_id is not None:
            result['CcnId'] = self.ccn_id

        if self.cen_status_error_code is not None:
            result['CenStatusErrorCode'] = self.cen_status_error_code

        if self.cen_status_error_message is not None:
            result['CenStatusErrorMessage'] = self.cen_status_error_message

        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.interworking_status is not None:
            result['InterworkingStatus'] = self.interworking_status

        if self.name is not None:
            result['Name'] = self.name

        if self.new_agw is not None:
            result['NewAgw'] = self.new_agw

        if self.processing_cen_id is not None:
            result['ProcessingCenId'] = self.processing_cen_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.snat_cidr_block is not None:
            result['SnatCidrBlock'] = self.snat_cidr_block

        if self.subnet is not None:
            result['Subnet'] = self.subnet

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.tr_network_config is not None:
            result['TrNetworkConfig'] = self.tr_network_config.to_map()

        if self.vpc_network_config is not None:
            result['VpcNetworkConfig'] = self.vpc_network_config.to_map()

        if self.vpc_status_error_code is not None:
            result['VpcStatusErrorCode'] = self.vpc_status_error_code

        if self.vpc_status_error_message is not None:
            result['VpcStatusErrorMessage'] = self.vpc_status_error_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociatedCenId') is not None:
            self.associated_cen_id = m.get('AssociatedCenId')

        if m.get('AssociatedCenOwnerId') is not None:
            self.associated_cen_owner_id = m.get('AssociatedCenOwnerId')

        if m.get('AssociatedCenStatus') is not None:
            self.associated_cen_status = m.get('AssociatedCenStatus')

        if m.get('AssociatedCloudBoxCount') is not None:
            self.associated_cloud_box_count = m.get('AssociatedCloudBoxCount')

        if m.get('AssociatedVpcStatus') is not None:
            self.associated_vpc_status = m.get('AssociatedVpcStatus')

        if m.get('AvailableCloudBoxCount') is not None:
            self.available_cloud_box_count = m.get('AvailableCloudBoxCount')

        if m.get('CcnId') is not None:
            self.ccn_id = m.get('CcnId')

        if m.get('CenStatusErrorCode') is not None:
            self.cen_status_error_code = m.get('CenStatusErrorCode')

        if m.get('CenStatusErrorMessage') is not None:
            self.cen_status_error_message = m.get('CenStatusErrorMessage')

        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InterworkingStatus') is not None:
            self.interworking_status = m.get('InterworkingStatus')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NewAgw') is not None:
            self.new_agw = m.get('NewAgw')

        if m.get('ProcessingCenId') is not None:
            self.processing_cen_id = m.get('ProcessingCenId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SnatCidrBlock') is not None:
            self.snat_cidr_block = m.get('SnatCidrBlock')

        if m.get('Subnet') is not None:
            self.subnet = m.get('Subnet')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeCloudConnectNetworksResponseBodyCloudConnectNetworksCloudConnectNetworkTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('TrNetworkConfig') is not None:
            temp_model = main_models.DescribeCloudConnectNetworksResponseBodyCloudConnectNetworksCloudConnectNetworkTrNetworkConfig()
            self.tr_network_config = temp_model.from_map(m.get('TrNetworkConfig'))

        if m.get('VpcNetworkConfig') is not None:
            temp_model = main_models.DescribeCloudConnectNetworksResponseBodyCloudConnectNetworksCloudConnectNetworkVpcNetworkConfig()
            self.vpc_network_config = temp_model.from_map(m.get('VpcNetworkConfig'))

        if m.get('VpcStatusErrorCode') is not None:
            self.vpc_status_error_code = m.get('VpcStatusErrorCode')

        if m.get('VpcStatusErrorMessage') is not None:
            self.vpc_status_error_message = m.get('VpcStatusErrorMessage')

        return self

class DescribeCloudConnectNetworksResponseBodyCloudConnectNetworksCloudConnectNetworkVpcNetworkConfig(DaraModel):
    def __init__(
        self,
        cidr_allocation_mode: str = None,
        region_binding_list: main_models.DescribeCloudConnectNetworksResponseBodyCloudConnectNetworksCloudConnectNetworkVpcNetworkConfigRegionBindingList = None,
        subnet: str = None,
    ):
        self.cidr_allocation_mode = cidr_allocation_mode
        self.region_binding_list = region_binding_list
        self.subnet = subnet

    def validate(self):
        if self.region_binding_list:
            self.region_binding_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr_allocation_mode is not None:
            result['CidrAllocationMode'] = self.cidr_allocation_mode

        if self.region_binding_list is not None:
            result['RegionBindingList'] = self.region_binding_list.to_map()

        if self.subnet is not None:
            result['Subnet'] = self.subnet

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrAllocationMode') is not None:
            self.cidr_allocation_mode = m.get('CidrAllocationMode')

        if m.get('RegionBindingList') is not None:
            temp_model = main_models.DescribeCloudConnectNetworksResponseBodyCloudConnectNetworksCloudConnectNetworkVpcNetworkConfigRegionBindingList()
            self.region_binding_list = temp_model.from_map(m.get('RegionBindingList'))

        if m.get('Subnet') is not None:
            self.subnet = m.get('Subnet')

        return self

class DescribeCloudConnectNetworksResponseBodyCloudConnectNetworksCloudConnectNetworkVpcNetworkConfigRegionBindingList(DaraModel):
    def __init__(
        self,
        region_binding: List[main_models.DescribeCloudConnectNetworksResponseBodyCloudConnectNetworksCloudConnectNetworkVpcNetworkConfigRegionBindingListRegionBinding] = None,
    ):
        self.region_binding = region_binding

    def validate(self):
        if self.region_binding:
            for v1 in self.region_binding:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RegionBinding'] = []
        if self.region_binding is not None:
            for k1 in self.region_binding:
                result['RegionBinding'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region_binding = []
        if m.get('RegionBinding') is not None:
            for k1 in m.get('RegionBinding'):
                temp_model = main_models.DescribeCloudConnectNetworksResponseBodyCloudConnectNetworksCloudConnectNetworkVpcNetworkConfigRegionBindingListRegionBinding()
                self.region_binding.append(temp_model.from_map(k1))

        return self

class DescribeCloudConnectNetworksResponseBodyCloudConnectNetworksCloudConnectNetworkVpcNetworkConfigRegionBindingListRegionBinding(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        relay_cidr_block: str = None,
        status: str = None,
        vpc_cidr_block: str = None,
        vpc_id: str = None,
    ):
        self.region_id = region_id
        self.relay_cidr_block = relay_cidr_block
        self.status = status
        self.vpc_cidr_block = vpc_cidr_block
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.relay_cidr_block is not None:
            result['RelayCidrBlock'] = self.relay_cidr_block

        if self.status is not None:
            result['Status'] = self.status

        if self.vpc_cidr_block is not None:
            result['VpcCidrBlock'] = self.vpc_cidr_block

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RelayCidrBlock') is not None:
            self.relay_cidr_block = m.get('RelayCidrBlock')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VpcCidrBlock') is not None:
            self.vpc_cidr_block = m.get('VpcCidrBlock')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class DescribeCloudConnectNetworksResponseBodyCloudConnectNetworksCloudConnectNetworkTrNetworkConfig(DaraModel):
    def __init__(
        self,
        cidr_allocation_mode: str = None,
        region_binding_list: main_models.DescribeCloudConnectNetworksResponseBodyCloudConnectNetworksCloudConnectNetworkTrNetworkConfigRegionBindingList = None,
        subnet: str = None,
    ):
        self.cidr_allocation_mode = cidr_allocation_mode
        self.region_binding_list = region_binding_list
        self.subnet = subnet

    def validate(self):
        if self.region_binding_list:
            self.region_binding_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr_allocation_mode is not None:
            result['CidrAllocationMode'] = self.cidr_allocation_mode

        if self.region_binding_list is not None:
            result['RegionBindingList'] = self.region_binding_list.to_map()

        if self.subnet is not None:
            result['Subnet'] = self.subnet

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrAllocationMode') is not None:
            self.cidr_allocation_mode = m.get('CidrAllocationMode')

        if m.get('RegionBindingList') is not None:
            temp_model = main_models.DescribeCloudConnectNetworksResponseBodyCloudConnectNetworksCloudConnectNetworkTrNetworkConfigRegionBindingList()
            self.region_binding_list = temp_model.from_map(m.get('RegionBindingList'))

        if m.get('Subnet') is not None:
            self.subnet = m.get('Subnet')

        return self

class DescribeCloudConnectNetworksResponseBodyCloudConnectNetworksCloudConnectNetworkTrNetworkConfigRegionBindingList(DaraModel):
    def __init__(
        self,
        region_binding: List[main_models.DescribeCloudConnectNetworksResponseBodyCloudConnectNetworksCloudConnectNetworkTrNetworkConfigRegionBindingListRegionBinding] = None,
    ):
        self.region_binding = region_binding

    def validate(self):
        if self.region_binding:
            for v1 in self.region_binding:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RegionBinding'] = []
        if self.region_binding is not None:
            for k1 in self.region_binding:
                result['RegionBinding'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region_binding = []
        if m.get('RegionBinding') is not None:
            for k1 in m.get('RegionBinding'):
                temp_model = main_models.DescribeCloudConnectNetworksResponseBodyCloudConnectNetworksCloudConnectNetworkTrNetworkConfigRegionBindingListRegionBinding()
                self.region_binding.append(temp_model.from_map(k1))

        return self

class DescribeCloudConnectNetworksResponseBodyCloudConnectNetworksCloudConnectNetworkTrNetworkConfigRegionBindingListRegionBinding(DaraModel):
    def __init__(
        self,
        cidr_block: str = None,
        region_id: str = None,
        relay_cidr_block: str = None,
        status: str = None,
        transit_router_id: str = None,
    ):
        self.cidr_block = cidr_block
        self.region_id = region_id
        self.relay_cidr_block = relay_cidr_block
        self.status = status
        self.transit_router_id = transit_router_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.relay_cidr_block is not None:
            result['RelayCidrBlock'] = self.relay_cidr_block

        if self.status is not None:
            result['Status'] = self.status

        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RelayCidrBlock') is not None:
            self.relay_cidr_block = m.get('RelayCidrBlock')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')

        return self

class DescribeCloudConnectNetworksResponseBodyCloudConnectNetworksCloudConnectNetworkTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeCloudConnectNetworksResponseBodyCloudConnectNetworksCloudConnectNetworkTagsTag] = None,
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
                temp_model = main_models.DescribeCloudConnectNetworksResponseBodyCloudConnectNetworksCloudConnectNetworkTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeCloudConnectNetworksResponseBodyCloudConnectNetworksCloudConnectNetworkTagsTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
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

