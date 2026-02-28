# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eflo20220530 import models as main_models
from darabonba.model import DaraModel

class CreateVpdRequest(DaraModel):
    def __init__(
        self,
        cidr: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        subnets: List[main_models.CreateVpdRequestSubnets] = None,
        tag: List[main_models.CreateVpdRequestTag] = None,
        vpd_name: str = None,
    ):
        # The CIDR block of the VPD.
        # 
        # *   We recommend that you use an RFC private endpoint as the Lingjun CIDR block, such as 10.0.0.0/8,172.16.0.0/12,192.168.0.0/16. In scenarios where the Doringjun CIDR block is connected to each other or where the Lingjun CIDR block is connected to a VPC, make sure that the addresses do not conflict with each other.
        # *   You can also use a custom CIDR block other than 100.64.0.0/10, 224.0.0.0/4, 127.0.0.0/8, or 169.254.0.0/16 and their subnets as the primary IPv4 CIDR block of the VPD.
        # 
        # This parameter is required.
        self.cidr = cidr
        # The region ID of the disk.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID.
        # 
        # For more information about resource groups, see [Resource groups](https://help.aliyun.com/document_detail/94475.htm?spm=a2c4g.11186623.0.0.29e15d7akXhpuu).
        self.resource_group_id = resource_group_id
        # Lingjun subnet information list
        self.subnets = subnets
        # A tag.
        self.tag = tag
        # Lingjun CIDR block instance name
        # 
        # This parameter is required.
        self.vpd_name = vpd_name

    def validate(self):
        if self.subnets:
            for v1 in self.subnets:
                 if v1:
                    v1.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr is not None:
            result['Cidr'] = self.cidr

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Subnets'] = []
        if self.subnets is not None:
            for k1 in self.subnets:
                result['Subnets'].append(k1.to_map() if k1 else None)

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.vpd_name is not None:
            result['VpdName'] = self.vpd_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.subnets = []
        if m.get('Subnets') is not None:
            for k1 in m.get('Subnets'):
                temp_model = main_models.CreateVpdRequestSubnets()
                self.subnets.append(temp_model.from_map(k1))

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateVpdRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('VpdName') is not None:
            self.vpd_name = m.get('VpdName')

        return self

class CreateVpdRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the VPN attachment.
        # 
        # You cannot specify an empty string as a tag key. It can be up to 64 characters in length and cannot start with aliyun or acs:. It cannot contain http:// or https://.
        # 
        # You can specify at most 20 tag keys in each call.
        self.key = key
        # The tag value of the VPN connection.
        # 
        # The tag value can be empty or a string of up to 128 characters. It cannot start with aliyun or acs:, and cannot contain http:// or https://.
        # 
        # Each tag key corresponds to a tag value. You can enter a maximum of 20 tag values at a time.
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

class CreateVpdRequestSubnets(DaraModel):
    def __init__(
        self,
        cidr: str = None,
        region_id: str = None,
        subnet_name: str = None,
        type: str = None,
        zone_id: str = None,
    ):
        # The CIDR block of the Subnet.
        # 
        # *   The network segment of the subnet must be a proper subset of the network segment of Lingjun to which it belongs, and the mask must be between 16 bits and 29 bits, which can provide 8 to 65536 addresses. For example, the CIDR block of the Lingjun CIDR block is 192.168.0.0/16, and the CIDR blocks of the subnets under the Lingjun CIDR block are 192.168.0.0/17 to 192.168.0.0/29.
        # *   The first and last three IP addresses of each subnet segment are reserved by the system. For example, the CIDR blocks of the subnet are 192.168.1.0/24,192.168.1.0, 192.168.1.253, 192.168.1.254, and 192.168.1.255.
        self.cidr = cidr
        # The region in which the instance resides.
        self.region_id = region_id
        # Lingjun subnet instance name
        self.subnet_name = subnet_name
        # Lingjun Subnet Usage Type; optional; optional. Valid values:
        # 
        # *   **Generic type is not specified**.
        # *   **OOB** :OOB type
        # *   **LB**: LB type
        self.type = type
        # The zone ID of the disk.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr is not None:
            result['Cidr'] = self.cidr

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.subnet_name is not None:
            result['SubnetName'] = self.subnet_name

        if self.type is not None:
            result['Type'] = self.type

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SubnetName') is not None:
            self.subnet_name = m.get('SubnetName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

