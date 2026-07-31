# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeNatGatewaysResponseBody(DaraModel):
    def __init__(
        self,
        nat_gateways: main_models.DescribeNatGatewaysResponseBodyNatGateways = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.nat_gateways = nat_gateways
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.nat_gateways:
            self.nat_gateways.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.nat_gateways is not None:
            result['NatGateways'] = self.nat_gateways.to_map()

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
        if m.get('NatGateways') is not None:
            temp_model = main_models.DescribeNatGatewaysResponseBodyNatGateways()
            self.nat_gateways = temp_model.from_map(m.get('NatGateways'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeNatGatewaysResponseBodyNatGateways(DaraModel):
    def __init__(
        self,
        nat_gateway: List[main_models.DescribeNatGatewaysResponseBodyNatGatewaysNatGateway] = None,
    ):
        self.nat_gateway = nat_gateway

    def validate(self):
        if self.nat_gateway:
            for v1 in self.nat_gateway:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NatGateway'] = []
        if self.nat_gateway is not None:
            for k1 in self.nat_gateway:
                result['NatGateway'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nat_gateway = []
        if m.get('NatGateway') is not None:
            for k1 in m.get('NatGateway'):
                temp_model = main_models.DescribeNatGatewaysResponseBodyNatGatewaysNatGateway()
                self.nat_gateway.append(temp_model.from_map(k1))

        return self

class DescribeNatGatewaysResponseBodyNatGatewaysNatGateway(DaraModel):
    def __init__(
        self,
        bandwidth_package_ids: main_models.DescribeNatGatewaysResponseBodyNatGatewaysNatGatewayBandwidthPackageIds = None,
        business_status: str = None,
        creation_time: str = None,
        description: str = None,
        forward_table_ids: main_models.DescribeNatGatewaysResponseBodyNatGatewaysNatGatewayForwardTableIds = None,
        instance_charge_type: str = None,
        name: str = None,
        nat_gateway_id: str = None,
        region_id: str = None,
        spec: str = None,
        status: str = None,
        vpc_id: str = None,
    ):
        self.bandwidth_package_ids = bandwidth_package_ids
        self.business_status = business_status
        self.creation_time = creation_time
        self.description = description
        self.forward_table_ids = forward_table_ids
        self.instance_charge_type = instance_charge_type
        self.name = name
        self.nat_gateway_id = nat_gateway_id
        self.region_id = region_id
        self.spec = spec
        self.status = status
        self.vpc_id = vpc_id

    def validate(self):
        if self.bandwidth_package_ids:
            self.bandwidth_package_ids.validate()
        if self.forward_table_ids:
            self.forward_table_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth_package_ids is not None:
            result['BandwidthPackageIds'] = self.bandwidth_package_ids.to_map()

        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.forward_table_ids is not None:
            result['ForwardTableIds'] = self.forward_table_ids.to_map()

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.name is not None:
            result['Name'] = self.name

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.spec is not None:
            result['Spec'] = self.spec

        if self.status is not None:
            result['Status'] = self.status

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthPackageIds') is not None:
            temp_model = main_models.DescribeNatGatewaysResponseBodyNatGatewaysNatGatewayBandwidthPackageIds()
            self.bandwidth_package_ids = temp_model.from_map(m.get('BandwidthPackageIds'))

        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ForwardTableIds') is not None:
            temp_model = main_models.DescribeNatGatewaysResponseBodyNatGatewaysNatGatewayForwardTableIds()
            self.forward_table_ids = temp_model.from_map(m.get('ForwardTableIds'))

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class DescribeNatGatewaysResponseBodyNatGatewaysNatGatewayForwardTableIds(DaraModel):
    def __init__(
        self,
        forward_table_id: List[str] = None,
    ):
        self.forward_table_id = forward_table_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.forward_table_id is not None:
            result['ForwardTableId'] = self.forward_table_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForwardTableId') is not None:
            self.forward_table_id = m.get('ForwardTableId')

        return self

class DescribeNatGatewaysResponseBodyNatGatewaysNatGatewayBandwidthPackageIds(DaraModel):
    def __init__(
        self,
        bandwidth_package_id: List[str] = None,
    ):
        self.bandwidth_package_id = bandwidth_package_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')

        return self

