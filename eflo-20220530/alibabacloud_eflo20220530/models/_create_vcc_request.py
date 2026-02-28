# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eflo20220530 import models as main_models
from darabonba.model import DaraModel

class CreateVccRequest(DaraModel):
    def __init__(
        self,
        access_could_service: bool = None,
        bandwidth: int = None,
        bgp_asn: int = None,
        bgp_cidr: str = None,
        cen_id: str = None,
        cen_owner_id: str = None,
        connection_type: str = None,
        description: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        tag: List[main_models.CreateVccRequestTag] = None,
        v_switch_id: str = None,
        vcc_id: str = None,
        vcc_name: str = None,
        vpc_id: str = None,
        vpd_id: str = None,
        zone_id: str = None,
    ):
        # Enabled access to cloud services. Optional values:
        # 
        # *   **true**: Enable access to cloud services
        # *   **false**: Do not enable access to cloud services
        self.access_could_service = access_could_service
        # The bandwidth. Unit: Mbit /s. The minimum value is 1000, representing 1Gbps bandwidth; the maximum value is 400000, representing 400Gbps bandwidth.
        # 
        # >  1Gbps = 1000Mbps
        self.bandwidth = bandwidth
        # bgp as number
        self.bgp_asn = bgp_asn
        # Internet segment, on-premises input, off-premises default
        self.bgp_cidr = bgp_cidr
        # CEN Instance ID
        self.cen_id = cen_id
        # Account to which cen belongs
        self.cen_owner_id = cen_owner_id
        # The connection mode. Valid values:
        # 
        # *   **VPC**
        # *   **CEN (CENTR)**
        self.connection_type = connection_type
        # The description of the document.
        self.description = description
        # The region ID.
        self.region_id = region_id
        # The resource group ID.
        # 
        # For more information about resource groups, see [Resource groups](https://help.aliyun.com/document_detail/94475.htm?spm=a2c4g.11186623.0.0.29e15d7akXhpuu).
        self.resource_group_id = resource_group_id
        # The tag information.
        # 
        # You can specify up to 20 tags.
        self.tag = tag
        # The ID of the vSwitch. [Virtual Private Cloud VSwitch](https://help.aliyun.com/document_detail/100380.html).
        # 
        # You can call the [DescribeVSwitches](https://help.aliyun.com/document_detail/35748.html) operation to query created vSwitches.
        self.v_switch_id = v_switch_id
        # The ID of the Lingjun connection instance.
        self.vcc_id = vcc_id
        # Lingjun Connection Name
        self.vcc_name = vcc_name
        # Virtual Private Cloud IDs; [What is Virtual Private Cloud](https://help.aliyun.com/document_detail/34217.html)
        # 
        # You can call the [DescribeVpcs](https://help.aliyun.com/document_detail/35739.html#demo-0) operation to query the specified VPC.
        self.vpc_id = vpc_id
        # Lingjun CIDR block instance ID
        self.vpd_id = vpd_id
        # The zone ID of the disk.
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
        if self.access_could_service is not None:
            result['AccessCouldService'] = self.access_could_service

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.bgp_asn is not None:
            result['BgpAsn'] = self.bgp_asn

        if self.bgp_cidr is not None:
            result['BgpCidr'] = self.bgp_cidr

        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.cen_owner_id is not None:
            result['CenOwnerId'] = self.cen_owner_id

        if self.connection_type is not None:
            result['ConnectionType'] = self.connection_type

        if self.description is not None:
            result['Description'] = self.description

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vcc_id is not None:
            result['VccId'] = self.vcc_id

        if self.vcc_name is not None:
            result['VccName'] = self.vcc_name

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessCouldService') is not None:
            self.access_could_service = m.get('AccessCouldService')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('BgpAsn') is not None:
            self.bgp_asn = m.get('BgpAsn')

        if m.get('BgpCidr') is not None:
            self.bgp_cidr = m.get('BgpCidr')

        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('CenOwnerId') is not None:
            self.cen_owner_id = m.get('CenOwnerId')

        if m.get('ConnectionType') is not None:
            self.connection_type = m.get('ConnectionType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateVccRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VccId') is not None:
            self.vcc_id = m.get('VccId')

        if m.get('VccName') is not None:
            self.vcc_name = m.get('VccName')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class CreateVccRequestTag(DaraModel):
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
        # Each key-value pair must be unique. You can specify values for at most 20 tag keys in each call.
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

