# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eflo20220530 import models as main_models
from darabonba.model import DaraModel

class GetElasticNetworkInterfaceResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: main_models.GetElasticNetworkInterfaceResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The response parameters.
        self.content = content
        # The return message.
        self.message = message
        # The ID of the request.
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
            temp_model = main_models.GetElasticNetworkInterfaceResponseBodyContent()
            self.content = temp_model.from_map(m.get('Content'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetElasticNetworkInterfaceResponseBodyContent(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        elastic_network_interface_id: str = None,
        enable_jumbo_frame: bool = None,
        gateway: str = None,
        gmt_modified: str = None,
        ip: str = None,
        ipv_6addresses: List[main_models.GetElasticNetworkInterfaceResponseBodyContentIpv6Addresses] = None,
        mac: str = None,
        mask: str = None,
        message: str = None,
        node_id: str = None,
        private_ip_addresses: List[main_models.GetElasticNetworkInterfaceResponseBodyContentPrivateIpAddresses] = None,
        region_id: str = None,
        resource_group_id: str = None,
        security_group_id: str = None,
        status: str = None,
        tags: List[main_models.GetElasticNetworkInterfaceResponseBodyContentTags] = None,
        type: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # The time when the data address was created.
        self.create_time = create_time
        # The instance description.
        self.description = description
        # Lingjun Elastic Network Interface ID
        self.elastic_network_interface_id = elastic_network_interface_id
        # Whether to enable the jumboFrame capability
        self.enable_jumbo_frame = enable_jumbo_frame
        # vswitch gateway address
        self.gateway = gateway
        # The time when the agent was last modified.
        self.gmt_modified = gmt_modified
        # Elastic Network Interface IP
        self.ip = ip
        # IPV6 address
        self.ipv_6addresses = ipv_6addresses
        # mac address
        self.mac = mac
        # vswitch mask bits
        self.mask = mask
        # The error message.
        self.message = message
        # Lingjun Node ID
        self.node_id = node_id
        # Secondary private IP address
        self.private_ip_addresses = private_ip_addresses
        # The region ID.
        self.region_id = region_id
        # 资源组实例ID
        self.resource_group_id = resource_group_id
        # The ID of the security group.
        self.security_group_id = security_group_id
        # The state of the private gateway.
        # 
        # Valid value:
        # 
        # *   Create Failed: the creation failure.
        # *   Delete Failed: the that failed to be deleted.
        # *   Executing
        # *   Available
        # *   Deleting
        self.status = status
        # The details of the resource tags.
        self.tags = tags
        # NIC Type
        # 
        # Valid value:
        # 
        # *   CUSTOM: custom type.
        # *   DEFAULT: system type.
        self.type = type
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id
        # VPC ID
        self.vpc_id = vpc_id
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.ipv_6addresses:
            for v1 in self.ipv_6addresses:
                 if v1:
                    v1.validate()
        if self.private_ip_addresses:
            for v1 in self.private_ip_addresses:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.elastic_network_interface_id is not None:
            result['ElasticNetworkInterfaceId'] = self.elastic_network_interface_id

        if self.enable_jumbo_frame is not None:
            result['EnableJumboFrame'] = self.enable_jumbo_frame

        if self.gateway is not None:
            result['Gateway'] = self.gateway

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.ip is not None:
            result['Ip'] = self.ip

        result['Ipv6Addresses'] = []
        if self.ipv_6addresses is not None:
            for k1 in self.ipv_6addresses:
                result['Ipv6Addresses'].append(k1.to_map() if k1 else None)

        if self.mac is not None:
            result['Mac'] = self.mac

        if self.mask is not None:
            result['Mask'] = self.mask

        if self.message is not None:
            result['Message'] = self.message

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        result['PrivateIpAddresses'] = []
        if self.private_ip_addresses is not None:
            for k1 in self.private_ip_addresses:
                result['PrivateIpAddresses'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ElasticNetworkInterfaceId') is not None:
            self.elastic_network_interface_id = m.get('ElasticNetworkInterfaceId')

        if m.get('EnableJumboFrame') is not None:
            self.enable_jumbo_frame = m.get('EnableJumboFrame')

        if m.get('Gateway') is not None:
            self.gateway = m.get('Gateway')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        self.ipv_6addresses = []
        if m.get('Ipv6Addresses') is not None:
            for k1 in m.get('Ipv6Addresses'):
                temp_model = main_models.GetElasticNetworkInterfaceResponseBodyContentIpv6Addresses()
                self.ipv_6addresses.append(temp_model.from_map(k1))

        if m.get('Mac') is not None:
            self.mac = m.get('Mac')

        if m.get('Mask') is not None:
            self.mask = m.get('Mask')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        self.private_ip_addresses = []
        if m.get('PrivateIpAddresses') is not None:
            for k1 in m.get('PrivateIpAddresses'):
                temp_model = main_models.GetElasticNetworkInterfaceResponseBodyContentPrivateIpAddresses()
                self.private_ip_addresses.append(temp_model.from_map(k1))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetElasticNetworkInterfaceResponseBodyContentTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class GetElasticNetworkInterfaceResponseBodyContentTags(DaraModel):
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

class GetElasticNetworkInterfaceResponseBodyContentPrivateIpAddresses(DaraModel):
    def __init__(
        self,
        description: str = None,
        elastic_network_interface_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        ip_name: str = None,
        message: str = None,
        private_ip_address: str = None,
        region_id: str = None,
        status: str = None,
    ):
        # The instance description.
        self.description = description
        # Lingjun Elastic Network Interface ID
        self.elastic_network_interface_id = elastic_network_interface_id
        # The time when the data address was created.
        self.gmt_create = gmt_create
        # The time when the cluster was updated.
        self.gmt_modified = gmt_modified
        # Lingjun Elastic Network Interface Secondary Private IP Unique Identifier
        self.ip_name = ip_name
        # The returned message.
        self.message = message
        # Lingjun Elastic Network Interface secondary private IP address
        self.private_ip_address = private_ip_address
        # The region ID.
        self.region_id = region_id
        # The status of the intervention entry. Valid value:
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

        if self.elastic_network_interface_id is not None:
            result['ElasticNetworkInterfaceId'] = self.elastic_network_interface_id

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.ip_name is not None:
            result['IpName'] = self.ip_name

        if self.message is not None:
            result['Message'] = self.message

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ElasticNetworkInterfaceId') is not None:
            self.elastic_network_interface_id = m.get('ElasticNetworkInterfaceId')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('IpName') is not None:
            self.ip_name = m.get('IpName')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetElasticNetworkInterfaceResponseBodyContentIpv6Addresses(DaraModel):
    def __init__(
        self,
        description: str = None,
        elastic_network_interface_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        ip_name: str = None,
        ipv_6address: str = None,
        message: str = None,
        region_id: str = None,
        status: str = None,
    ):
        # The instance description.
        self.description = description
        # Lingjun Elastic Network Interface ID
        self.elastic_network_interface_id = elastic_network_interface_id
        # The time when the data address was created.
        self.gmt_create = gmt_create
        # The time when the cluster was updated.
        self.gmt_modified = gmt_modified
        # IPV6 unique identifier
        self.ip_name = ip_name
        # IPV6 address
        self.ipv_6address = ipv_6address
        # The error message. (If the instance is in the Exception state, the exception cause is prompted.)
        self.message = message
        # The region ID.
        self.region_id = region_id
        # The status of the intervention entry. Valid value:
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

        if self.elastic_network_interface_id is not None:
            result['ElasticNetworkInterfaceId'] = self.elastic_network_interface_id

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.ip_name is not None:
            result['IpName'] = self.ip_name

        if self.ipv_6address is not None:
            result['Ipv6Address'] = self.ipv_6address

        if self.message is not None:
            result['Message'] = self.message

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ElasticNetworkInterfaceId') is not None:
            self.elastic_network_interface_id = m.get('ElasticNetworkInterfaceId')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('IpName') is not None:
            self.ip_name = m.get('IpName')

        if m.get('Ipv6Address') is not None:
            self.ipv_6address = m.get('Ipv6Address')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

