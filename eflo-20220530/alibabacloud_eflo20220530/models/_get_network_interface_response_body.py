# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eflo20220530 import models as main_models
from darabonba.model import DaraModel

class GetNetworkInterfaceResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: main_models.GetNetworkInterfaceResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The response data. (If a resource has dependent resources, the existing dependent resources are returned.)
        self.content = content
        # The error message. (If the instance is in the Exception state, the exception cause is prompted.)
        self.message = message
        # Request ID of the current request
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
            temp_model = main_models.GetNetworkInterfaceResponseBodyContent()
            self.content = temp_model.from_map(m.get('Content'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetNetworkInterfaceResponseBodyContent(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        ethernet: List[str] = None,
        gateway: str = None,
        ip: str = None,
        nc_type: str = None,
        network_interface_id: str = None,
        network_interface_name: str = None,
        node_id: str = None,
        private_ip_address_mac_group: List[main_models.GetNetworkInterfaceResponseBodyContentPrivateIpAddressMacGroup] = None,
        quota: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        service_mac: str = None,
        status: str = None,
        subnet_base_info: main_models.GetNetworkInterfaceResponseBodyContentSubnetBaseInfo = None,
        tags: List[main_models.GetNetworkInterfaceResponseBodyContentTags] = None,
        tenant_id: str = None,
        vpd_base_info: main_models.GetNetworkInterfaceResponseBodyContentVpdBaseInfo = None,
        zone_id: str = None,
    ):
        # The time when the data address was created.
        self.create_time = create_time
        # Port
        self.ethernet = ethernet
        # Gateway
        self.gateway = gateway
        # The IP address of the BE cluster.
        self.ip = ip
        # NC Type
        # 
        # Valid value:
        # 
        # *   CUSTOM_LNI_INTEGRATION: two-network one-in-one architecture Lingjun hosting network interface controller.
        # *   CPU: CPU machine.
        # *   ELASTIC_6.2: Machine
        # *   GPU: GPU machine.
        # *   DEFAULT: the old CPU machine.
        # *   CUSTOM_LNI: two network separation architecture Lingjun hosting network interface controller.
        self.nc_type = nc_type
        # Lingjun network interface controller ID
        self.network_interface_id = network_interface_id
        # ENI Name
        self.network_interface_name = network_interface_name
        # The ID of the host.
        self.node_id = node_id
        # Secondary Private IP\\&MAC Address Collection
        self.private_ip_address_mac_group = private_ip_address_mac_group
        # network interface controller private secondary IP limit
        self.quota = quota
        # The region ID.
        self.region_id = region_id
        # Resource group instance ID
        self.resource_group_id = resource_group_id
        # Service network interface controller address
        self.service_mac = service_mac
        # The status of the intervention entry. Valid value:
        self.status = status
        # Lingjun subnet (Subnet) basic information
        self.subnet_base_info = subnet_base_info
        # The details of the resource tags.
        self.tags = tags
        # The ID of the tenant.
        self.tenant_id = tenant_id
        # Basic information of Lingjun network segment (VPD)
        self.vpd_base_info = vpd_base_info
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.private_ip_address_mac_group:
            for v1 in self.private_ip_address_mac_group:
                 if v1:
                    v1.validate()
        if self.subnet_base_info:
            self.subnet_base_info.validate()
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
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.ethernet is not None:
            result['Ethernet'] = self.ethernet

        if self.gateway is not None:
            result['Gateway'] = self.gateway

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.nc_type is not None:
            result['NcType'] = self.nc_type

        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id

        if self.network_interface_name is not None:
            result['NetworkInterfaceName'] = self.network_interface_name

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        result['PrivateIpAddressMacGroup'] = []
        if self.private_ip_address_mac_group is not None:
            for k1 in self.private_ip_address_mac_group:
                result['PrivateIpAddressMacGroup'].append(k1.to_map() if k1 else None)

        if self.quota is not None:
            result['Quota'] = self.quota

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.service_mac is not None:
            result['ServiceMac'] = self.service_mac

        if self.status is not None:
            result['Status'] = self.status

        if self.subnet_base_info is not None:
            result['SubnetBaseInfo'] = self.subnet_base_info.to_map()

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.vpd_base_info is not None:
            result['VpdBaseInfo'] = self.vpd_base_info.to_map()

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Ethernet') is not None:
            self.ethernet = m.get('Ethernet')

        if m.get('Gateway') is not None:
            self.gateway = m.get('Gateway')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('NcType') is not None:
            self.nc_type = m.get('NcType')

        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')

        if m.get('NetworkInterfaceName') is not None:
            self.network_interface_name = m.get('NetworkInterfaceName')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        self.private_ip_address_mac_group = []
        if m.get('PrivateIpAddressMacGroup') is not None:
            for k1 in m.get('PrivateIpAddressMacGroup'):
                temp_model = main_models.GetNetworkInterfaceResponseBodyContentPrivateIpAddressMacGroup()
                self.private_ip_address_mac_group.append(temp_model.from_map(k1))

        if m.get('Quota') is not None:
            self.quota = m.get('Quota')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ServiceMac') is not None:
            self.service_mac = m.get('ServiceMac')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubnetBaseInfo') is not None:
            temp_model = main_models.GetNetworkInterfaceResponseBodyContentSubnetBaseInfo()
            self.subnet_base_info = temp_model.from_map(m.get('SubnetBaseInfo'))

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetNetworkInterfaceResponseBodyContentTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('VpdBaseInfo') is not None:
            temp_model = main_models.GetNetworkInterfaceResponseBodyContentVpdBaseInfo()
            self.vpd_base_info = temp_model.from_map(m.get('VpdBaseInfo'))

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class GetNetworkInterfaceResponseBodyContentVpdBaseInfo(DaraModel):
    def __init__(
        self,
        cidr: str = None,
        create_time: str = None,
        vpd_id: str = None,
        vpd_name: str = None,
    ):
        # The network segment of the Lingjun subnet.
        # 
        # *   The network segment of the subnet must be a proper subset of the network segment of Lingjun to which it belongs, and the mask must be between 16 bits and 29 bits, which can provide 8 to 65536 addresses. For example, the CIDR block of the Lingjun CIDR block is 192.168.0.0/16, and the CIDR blocks of the subnets under the Lingjun CIDR block are 192.168.0.0/17 to 192.168.0.0/29.
        # *   The first and last three IP addresses of each subnet segment are reserved by the system. For example, the CIDR blocks of the subnet are 192.168.1.0/24,192.168.1.0, 192.168.1.253, 192.168.1.254, and 192.168.1.255.
        # 
        # For more information about CIDR blocks, see the [What is CIDR?](https://www.alibabacloud.com/help/doc-detail/40637.htm#title-gu4-uzk-12r) section in the "Network FAQ" topic.
        # 
        # This parameter is left empty by default.
        self.cidr = cidr
        # The time when the data address was created.
        self.create_time = create_time
        # The ID of the VPD instance.
        self.vpd_id = vpd_id
        # The name of the VPD instance.
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

class GetNetworkInterfaceResponseBodyContentTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
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

class GetNetworkInterfaceResponseBodyContentSubnetBaseInfo(DaraModel):
    def __init__(
        self,
        cidr: str = None,
        create_time: str = None,
        subnet_id: str = None,
        subnet_name: str = None,
    ):
        # Network address segment
        self.cidr = cidr
        # The time when the data address was created.
        self.create_time = create_time
        # The ID of the Subnet instance.
        self.subnet_id = subnet_id
        # The name of the Subnet instance.
        self.subnet_name = subnet_name

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

        if self.subnet_id is not None:
            result['SubnetId'] = self.subnet_id

        if self.subnet_name is not None:
            result['SubnetName'] = self.subnet_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('SubnetId') is not None:
            self.subnet_id = m.get('SubnetId')

        if m.get('SubnetName') is not None:
            self.subnet_name = m.get('SubnetName')

        return self

class GetNetworkInterfaceResponseBodyContentPrivateIpAddressMacGroup(DaraModel):
    def __init__(
        self,
        description: str = None,
        ip_address_mac: str = None,
        ip_name: str = None,
        message: str = None,
        private_ip_address: str = None,
        status: str = None,
    ):
        # The instance description.
        self.description = description
        # Secondary private MAC address
        self.ip_address_mac = ip_address_mac
        # IP unique identifier
        self.ip_name = ip_name
        # The error message. (If the instance is in the Exception state, the exception cause is prompted.)
        self.message = message
        # Secondary private IP address
        self.private_ip_address = private_ip_address
        # The state of the rule.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.ip_address_mac is not None:
            result['IpAddressMac'] = self.ip_address_mac

        if self.ip_name is not None:
            result['IpName'] = self.ip_name

        if self.message is not None:
            result['Message'] = self.message

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('IpAddressMac') is not None:
            self.ip_address_mac = m.get('IpAddressMac')

        if m.get('IpName') is not None:
            self.ip_name = m.get('IpName')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

