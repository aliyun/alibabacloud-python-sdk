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
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of the CCN instances.
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
        associated_cloud_box_count: str = None,
        available_cloud_box_count: str = None,
        ccn_id: str = None,
        cidr_block: str = None,
        create_time: int = None,
        description: str = None,
        interworking_status: str = None,
        name: str = None,
        new_agw: bool = None,
        resource_group_id: str = None,
        snat_cidr_block: str = None,
        subnet: str = None,
        tags: main_models.DescribeCloudConnectNetworksResponseBodyCloudConnectNetworksCloudConnectNetworkTags = None,
    ):
        self.associated_cen_id = associated_cen_id
        self.associated_cen_owner_id = associated_cen_owner_id
        self.associated_cloud_box_count = associated_cloud_box_count
        self.available_cloud_box_count = available_cloud_box_count
        self.ccn_id = ccn_id
        self.cidr_block = cidr_block
        self.create_time = create_time
        self.description = description
        self.interworking_status = interworking_status
        self.name = name
        self.new_agw = new_agw
        self.resource_group_id = resource_group_id
        self.snat_cidr_block = snat_cidr_block
        self.subnet = subnet
        self.tags = tags

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.associated_cen_id is not None:
            result['AssociatedCenId'] = self.associated_cen_id

        if self.associated_cen_owner_id is not None:
            result['AssociatedCenOwnerId'] = self.associated_cen_owner_id

        if self.associated_cloud_box_count is not None:
            result['AssociatedCloudBoxCount'] = self.associated_cloud_box_count

        if self.available_cloud_box_count is not None:
            result['AvailableCloudBoxCount'] = self.available_cloud_box_count

        if self.ccn_id is not None:
            result['CcnId'] = self.ccn_id

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

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.snat_cidr_block is not None:
            result['SnatCidrBlock'] = self.snat_cidr_block

        if self.subnet is not None:
            result['Subnet'] = self.subnet

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociatedCenId') is not None:
            self.associated_cen_id = m.get('AssociatedCenId')

        if m.get('AssociatedCenOwnerId') is not None:
            self.associated_cen_owner_id = m.get('AssociatedCenOwnerId')

        if m.get('AssociatedCloudBoxCount') is not None:
            self.associated_cloud_box_count = m.get('AssociatedCloudBoxCount')

        if m.get('AvailableCloudBoxCount') is not None:
            self.available_cloud_box_count = m.get('AvailableCloudBoxCount')

        if m.get('CcnId') is not None:
            self.ccn_id = m.get('CcnId')

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

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SnatCidrBlock') is not None:
            self.snat_cidr_block = m.get('SnatCidrBlock')

        if m.get('Subnet') is not None:
            self.subnet = m.get('Subnet')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeCloudConnectNetworksResponseBodyCloudConnectNetworksCloudConnectNetworkTags()
            self.tags = temp_model.from_map(m.get('Tags'))

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

