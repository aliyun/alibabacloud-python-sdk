# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeStorageGatewayResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        storage_gateways: List[main_models.DescribeStorageGatewayResponseBodyStorageGateways] = None,
        total_count: int = None,
    ):
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # Default value: 10.
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        # The list information.
        self.storage_gateways = storage_gateways
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.storage_gateways:
            for v1 in self.storage_gateways:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['StorageGateways'] = []
        if self.storage_gateways is not None:
            for k1 in self.storage_gateways:
                result['StorageGateways'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.storage_gateways = []
        if m.get('StorageGateways') is not None:
            for k1 in m.get('StorageGateways'):
                temp_model = main_models.DescribeStorageGatewayResponseBodyStorageGateways()
                self.storage_gateways.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeStorageGatewayResponseBodyStorageGateways(DaraModel):
    def __init__(
        self,
        cidr_block: str = None,
        creation_time: str = None,
        description: str = None,
        ens_region_id: str = None,
        service_ip: str = None,
        status: str = None,
        storage_gateway_id: str = None,
        storage_gateway_name: str = None,
        storage_gateway_type: int = None,
        vpc_id: str = None,
    ):
        # The internal CIDR block.
        self.cidr_block = cidr_block
        # The time when the storage gateway was created. The time is displayed in UTC.
        self.creation_time = creation_time
        # The description of the storage gateway.
        self.description = description
        # The ID of the node.
        self.ens_region_id = ens_region_id
        # The IP address of the service.
        self.service_ip = service_ip
        # The status of the storage gateway. Valid values:
        # 
        # *   creating
        # *   available
        # *   deleting
        # *   deleted
        self.status = status
        # The ID of the storage gateway.
        self.storage_gateway_id = storage_gateway_id
        # The name of the storage gateway.
        self.storage_gateway_name = storage_gateway_name
        # The type of the storage gateway. Default value: 1, which indicates iSCSI.
        self.storage_gateway_type = storage_gateway_type
        # The ID of the VPC.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.service_ip is not None:
            result['ServiceIp'] = self.service_ip

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_gateway_id is not None:
            result['StorageGatewayId'] = self.storage_gateway_id

        if self.storage_gateway_name is not None:
            result['StorageGatewayName'] = self.storage_gateway_name

        if self.storage_gateway_type is not None:
            result['StorageGatewayType'] = self.storage_gateway_type

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('ServiceIp') is not None:
            self.service_ip = m.get('ServiceIp')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageGatewayId') is not None:
            self.storage_gateway_id = m.get('StorageGatewayId')

        if m.get('StorageGatewayName') is not None:
            self.storage_gateway_name = m.get('StorageGatewayName')

        if m.get('StorageGatewayType') is not None:
            self.storage_gateway_type = m.get('StorageGatewayType')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

