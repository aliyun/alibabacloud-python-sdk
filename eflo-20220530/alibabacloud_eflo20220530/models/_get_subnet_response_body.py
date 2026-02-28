# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eflo20220530 import models as main_models
from darabonba.model import DaraModel

class GetSubnetResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: main_models.GetSubnetResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The response data.
        self.content = content
        # The error message. (If the instance is in the Exception state, the exception cause is prompted.)
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.content is not None:
            result['Content'] = self.content.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Content') is not None:
            temp_model = main_models.GetSubnetResponseBodyContent()
            self.content = temp_model.from_map(m.get('Content'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetSubnetResponseBodyContent(DaraModel):
    def __init__(
        self,
        available_ips: int = None,
        cidr: str = None,
        create_time: str = None,
        gmt_modified: str = None,
        lb_count: int = None,
        message: str = None,
        nc_count: int = None,
        network_interface_count: int = None,
        private_ip_count: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        status: str = None,
        subnet_id: str = None,
        subnet_name: str = None,
        tags: List[main_models.GetSubnetResponseBodyContentTags] = None,
        tenant_id: str = None,
        type: str = None,
        vpd_base_info: main_models.GetSubnetResponseBodyContentVpdBaseInfo = None,
        vpd_id: str = None,
        zone_id: str = None,
    ):
        # The number of available IP addresses.
        self.available_ips = available_ips
        # The CIDR block of the Subnet.
        # 
        # *   The network segment of the subnet must be a proper subset of the network segment of Lingjun to which it belongs, and the mask must be between 16 bits and 29 bits, which can provide 8 to 65536 addresses. For example, the CIDR block of the Lingjun CIDR block is 192.168.0.0/16, and the CIDR blocks of the subnets under the Lingjun CIDR block are 192.168.0.0/17 to 192.168.0.0/29.
        # *   The first and last three IP addresses of each subnet segment are reserved by the system. For example, the CIDR blocks of the subnet are 192.168.1.0/24,192.168.1.0, 192.168.1.253, 192.168.1.254, and 192.168.1.255.
        self.cidr = cidr
        # The time when the activation code was created.
        self.create_time = create_time
        # The time when the O\\&M task was modified.
        self.gmt_modified = gmt_modified
        # The number of SLB.
        self.lb_count = lb_count
        # The error message. (If the instance is in the Exception state, the exception cause is prompted.)
        self.message = message
        # The number of NCs.
        self.nc_count = nc_count
        # Number of Lingjun network interface controller
        self.network_interface_count = network_interface_count
        # The total number of secondary private IP addresses.
        self.private_ip_count = private_ip_count
        # The region ID.
        self.region_id = region_id
        # The ID of your Alibaba Cloud resource group.
        self.resource_group_id = resource_group_id
        # The status of the cache reserve instance.
        self.status = status
        # The ID of the Lingjun subnet instance.
        self.subnet_id = subnet_id
        # The name of the Lingjun subnet instance.
        self.subnet_name = subnet_name
        # The tag information.
        # 
        # You can specify up to 20 tags.
        self.tags = tags
        # The tenant ID.
        self.tenant_id = tenant_id
        # Lingjun Subnet Usage Type; optional; optional. Valid values:
        # 
        # *   **Empty for common data types**
        # *   **OOB** :OOB type
        # *   **LB**: LB type
        self.type = type
        # The information about the network segment of Lingjun.
        self.vpd_base_info = vpd_base_info
        # The ID of the Lingjun CIDR block.
        self.vpd_id = vpd_id
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()
        if self.vpd_base_info:
            self.vpd_base_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_ips is not None:
            result['AvailableIps'] = self.available_ips

        if self.cidr is not None:
            result['Cidr'] = self.cidr

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.lb_count is not None:
            result['LbCount'] = self.lb_count

        if self.message is not None:
            result['Message'] = self.message

        if self.nc_count is not None:
            result['NcCount'] = self.nc_count

        if self.network_interface_count is not None:
            result['NetworkInterfaceCount'] = self.network_interface_count

        if self.private_ip_count is not None:
            result['PrivateIpCount'] = self.private_ip_count

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['Status'] = self.status

        if self.subnet_id is not None:
            result['SubnetId'] = self.subnet_id

        if self.subnet_name is not None:
            result['SubnetName'] = self.subnet_name

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.type is not None:
            result['Type'] = self.type

        if self.vpd_base_info is not None:
            result['VpdBaseInfo'] = self.vpd_base_info.to_map()

        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableIps') is not None:
            self.available_ips = m.get('AvailableIps')

        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('LbCount') is not None:
            self.lb_count = m.get('LbCount')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NcCount') is not None:
            self.nc_count = m.get('NcCount')

        if m.get('NetworkInterfaceCount') is not None:
            self.network_interface_count = m.get('NetworkInterfaceCount')

        if m.get('PrivateIpCount') is not None:
            self.private_ip_count = m.get('PrivateIpCount')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubnetId') is not None:
            self.subnet_id = m.get('SubnetId')

        if m.get('SubnetName') is not None:
            self.subnet_name = m.get('SubnetName')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetSubnetResponseBodyContentTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('VpdBaseInfo') is not None:
            temp_model = main_models.GetSubnetResponseBodyContentVpdBaseInfo()
            self.vpd_base_info = temp_model.from_map(m.get('VpdBaseInfo'))

        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class GetSubnetResponseBodyContentVpdBaseInfo(DaraModel):
    def __init__(
        self,
        cidr: str = None,
        create_time: str = None,
        vpd_id: str = None,
        vpd_name: str = None,
    ):
        # The CIDR block of the VPD.
        # 
        # *   We recommend that you use an RFC private endpoint as the Lingjun CIDR block, such as 10.0.0.0/8,172.16.0.0/12,192.168.0.0/16. In scenarios where the Doringjun CIDR block is connected to each other or where the Lingjun CIDR block is connected to a VPC, make sure that the addresses do not conflict with each other.
        # *   You can also use a custom CIDR block other than 100.64.0.0/10, 224.0.0.0/4, 127.0.0.0/8, or 169.254.0.0/16 and their subnets as the primary IPv4 CIDR block of the VPD.
        self.cidr = cidr
        # The time when the activation code was created.
        self.create_time = create_time
        # The ID of the Lingjun CIDR block.
        self.vpd_id = vpd_id
        # The name of the Lingjun CIDR block.
        self.vpd_name = vpd_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr is not None:
            result['Cidr'] = self.cidr

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id

        if self.vpd_name is not None:
            result['VpdName'] = self.vpd_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')

        if m.get('VpdName') is not None:
            self.vpd_name = m.get('VpdName')

        return self

class GetSubnetResponseBodyContentTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key.
        # 
        # You cannot specify an empty string as a tag key. It can be up to 64 characters in length and cannot start with aliyun or acs:. It cannot contain http:// or https://.
        # 
        # You can specify at most 20 tag keys in each call.
        self.tag_key = tag_key
        # The value of the tag that is added to the resource.
        # 
        # The tag value can be empty or a string of up to 128 characters. It cannot start with aliyun or acs:, and cannot contain http:// or https://.
        # 
        # Each key-value pair must be unique. You can specify values for at most 20 tag keys in each call.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

