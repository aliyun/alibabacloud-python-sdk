# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class DescribeCenAttachedChildInstanceAttributeResponseBody(DaraModel):
    def __init__(
        self,
        cen_id: str = None,
        child_instance_attach_time: str = None,
        child_instance_attributes: main_models.DescribeCenAttachedChildInstanceAttributeResponseBodyChildInstanceAttributes = None,
        child_instance_id: str = None,
        child_instance_name: str = None,
        child_instance_owner_id: int = None,
        child_instance_region_id: str = None,
        child_instance_type: str = None,
        managed_service: str = None,
        request_id: str = None,
        status: str = None,
    ):
        # The ID of the CEN instance.
        self.cen_id = cen_id
        # The time when the network instance was attached to the CEN instance.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddThh:mmZ format. The time is displayed in UTC.
        self.child_instance_attach_time = child_instance_attach_time
        # The details about the network instance.
        self.child_instance_attributes = child_instance_attributes
        # The ID of the network instance.
        self.child_instance_id = child_instance_id
        # The name of the network instance.
        self.child_instance_name = child_instance_name
        # The ID of the Alibaba Cloud account to which the network instance belongs.
        self.child_instance_owner_id = child_instance_owner_id
        # The region ID of the network instance.
        self.child_instance_region_id = child_instance_region_id
        # The type of the network instance. Valid values:
        # 
        # *   **VPC**: VPC
        # *   **VBR**: VBR
        # *   **CCN**: CCN instance
        self.child_instance_type = child_instance_type
        self.managed_service = managed_service
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the network instance is attached to the CEN instance.
        # 
        # *   **Attaching**: The network instance is being attached to the CEN instance.
        # *   **Attached**: The network instance is attached to the CEN instance.
        # *   **Detaching**: The network instance is being detached from the CEN instance.
        self.status = status

    def validate(self):
        if self.child_instance_attributes:
            self.child_instance_attributes.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.child_instance_attach_time is not None:
            result['ChildInstanceAttachTime'] = self.child_instance_attach_time

        if self.child_instance_attributes is not None:
            result['ChildInstanceAttributes'] = self.child_instance_attributes.to_map()

        if self.child_instance_id is not None:
            result['ChildInstanceId'] = self.child_instance_id

        if self.child_instance_name is not None:
            result['ChildInstanceName'] = self.child_instance_name

        if self.child_instance_owner_id is not None:
            result['ChildInstanceOwnerId'] = self.child_instance_owner_id

        if self.child_instance_region_id is not None:
            result['ChildInstanceRegionId'] = self.child_instance_region_id

        if self.child_instance_type is not None:
            result['ChildInstanceType'] = self.child_instance_type

        if self.managed_service is not None:
            result['ManagedService'] = self.managed_service

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('ChildInstanceAttachTime') is not None:
            self.child_instance_attach_time = m.get('ChildInstanceAttachTime')

        if m.get('ChildInstanceAttributes') is not None:
            temp_model = main_models.DescribeCenAttachedChildInstanceAttributeResponseBodyChildInstanceAttributes()
            self.child_instance_attributes = temp_model.from_map(m.get('ChildInstanceAttributes'))

        if m.get('ChildInstanceId') is not None:
            self.child_instance_id = m.get('ChildInstanceId')

        if m.get('ChildInstanceName') is not None:
            self.child_instance_name = m.get('ChildInstanceName')

        if m.get('ChildInstanceOwnerId') is not None:
            self.child_instance_owner_id = m.get('ChildInstanceOwnerId')

        if m.get('ChildInstanceRegionId') is not None:
            self.child_instance_region_id = m.get('ChildInstanceRegionId')

        if m.get('ChildInstanceType') is not None:
            self.child_instance_type = m.get('ChildInstanceType')

        if m.get('ManagedService') is not None:
            self.managed_service = m.get('ManagedService')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeCenAttachedChildInstanceAttributeResponseBodyChildInstanceAttributes(DaraModel):
    def __init__(
        self,
        cidr_block: str = None,
        ipv_6cidr_block: str = None,
        ipv_6cidr_blocks: main_models.DescribeCenAttachedChildInstanceAttributeResponseBodyChildInstanceAttributesIpv6CidrBlocks = None,
        secondary_cidr_blocks: main_models.DescribeCenAttachedChildInstanceAttributeResponseBodyChildInstanceAttributesSecondaryCidrBlocks = None,
    ):
        # The IPv4 CIDR block of the VPC.
        self.cidr_block = cidr_block
        # The IPv6 CIDR block of the VPC.
        self.ipv_6cidr_block = ipv_6cidr_block
        # The IPv6 CIDR blocks of the VPC.
        self.ipv_6cidr_blocks = ipv_6cidr_blocks
        # The information about the VPC secondary CIDR block.
        self.secondary_cidr_blocks = secondary_cidr_blocks

    def validate(self):
        if self.ipv_6cidr_blocks:
            self.ipv_6cidr_blocks.validate()
        if self.secondary_cidr_blocks:
            self.secondary_cidr_blocks.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block

        if self.ipv_6cidr_block is not None:
            result['Ipv6CidrBlock'] = self.ipv_6cidr_block

        if self.ipv_6cidr_blocks is not None:
            result['Ipv6CidrBlocks'] = self.ipv_6cidr_blocks.to_map()

        if self.secondary_cidr_blocks is not None:
            result['SecondaryCidrBlocks'] = self.secondary_cidr_blocks.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')

        if m.get('Ipv6CidrBlock') is not None:
            self.ipv_6cidr_block = m.get('Ipv6CidrBlock')

        if m.get('Ipv6CidrBlocks') is not None:
            temp_model = main_models.DescribeCenAttachedChildInstanceAttributeResponseBodyChildInstanceAttributesIpv6CidrBlocks()
            self.ipv_6cidr_blocks = temp_model.from_map(m.get('Ipv6CidrBlocks'))

        if m.get('SecondaryCidrBlocks') is not None:
            temp_model = main_models.DescribeCenAttachedChildInstanceAttributeResponseBodyChildInstanceAttributesSecondaryCidrBlocks()
            self.secondary_cidr_blocks = temp_model.from_map(m.get('SecondaryCidrBlocks'))

        return self

class DescribeCenAttachedChildInstanceAttributeResponseBodyChildInstanceAttributesSecondaryCidrBlocks(DaraModel):
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
            result['secondaryCidrBlock'] = self.secondary_cidr_block

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('secondaryCidrBlock') is not None:
            self.secondary_cidr_block = m.get('secondaryCidrBlock')

        return self

class DescribeCenAttachedChildInstanceAttributeResponseBodyChildInstanceAttributesIpv6CidrBlocks(DaraModel):
    def __init__(
        self,
        ipv_6cidr_block: List[main_models.DescribeCenAttachedChildInstanceAttributeResponseBodyChildInstanceAttributesIpv6CidrBlocksIpv6CidrBlock] = None,
    ):
        self.ipv_6cidr_block = ipv_6cidr_block

    def validate(self):
        if self.ipv_6cidr_block:
            for v1 in self.ipv_6cidr_block:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ipv6CidrBlock'] = []
        if self.ipv_6cidr_block is not None:
            for k1 in self.ipv_6cidr_block:
                result['ipv6CidrBlock'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ipv_6cidr_block = []
        if m.get('ipv6CidrBlock') is not None:
            for k1 in m.get('ipv6CidrBlock'):
                temp_model = main_models.DescribeCenAttachedChildInstanceAttributeResponseBodyChildInstanceAttributesIpv6CidrBlocksIpv6CidrBlock()
                self.ipv_6cidr_block.append(temp_model.from_map(k1))

        return self

class DescribeCenAttachedChildInstanceAttributeResponseBodyChildInstanceAttributesIpv6CidrBlocksIpv6CidrBlock(DaraModel):
    def __init__(
        self,
        ipv_6cidr_block: str = None,
        ipv_6isp: str = None,
    ):
        # The IPv6 CIDR block of the VPC.
        self.ipv_6cidr_block = ipv_6cidr_block
        # The type of the IPv6 CIDR block of the VPC. Valid values:
        # 
        # *   BGP (default): Alibaba Cloud Border Gateway Protocol (BGP) IPv6
        # *   ChinaMobile: China Mobile (single line)
        # *   ChinaUnicom: China Unicom (single line)
        # *   ChinaTelecom: China Telecom (single line)
        # 
        # >  If you are on the whitelist of single-line bandwidth, you can set this parameter to ChinaTelecom, ChinaUnicom, or ChinaMobile.
        self.ipv_6isp = ipv_6isp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipv_6cidr_block is not None:
            result['Ipv6CidrBlock'] = self.ipv_6cidr_block

        if self.ipv_6isp is not None:
            result['Ipv6Isp'] = self.ipv_6isp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ipv6CidrBlock') is not None:
            self.ipv_6cidr_block = m.get('Ipv6CidrBlock')

        if m.get('Ipv6Isp') is not None:
            self.ipv_6isp = m.get('Ipv6Isp')

        return self

