# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


class AssignLeniPrivateIpAddressRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        elastic_network_interface_id: str = None,
        private_ip_address: str = None,
        region_id: str = None,
    ):
        # The idempotent identifier.
        self.client_token = client_token
        # The description of the response code.
        self.description = description
        # Lingjun Elastic Network Interface ID.
        # 
        # This parameter is required.
        self.elastic_network_interface_id = elastic_network_interface_id
        # Lingjun Elastic Network Interface secondary private network IP (automatically assigned by default).
        self.private_ip_address = private_ip_address
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.elastic_network_interface_id is not None:
            result['ElasticNetworkInterfaceId'] = self.elastic_network_interface_id
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ElasticNetworkInterfaceId') is not None:
            self.elastic_network_interface_id = m.get('ElasticNetworkInterfaceId')
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AssignLeniPrivateIpAddressResponseBodyContent(TeaModel):
    def __init__(
        self,
        elastic_network_interface_id: str = None,
        ip_name: str = None,
    ):
        # Lingjun Elastic Network Interface ID.
        self.elastic_network_interface_id = elastic_network_interface_id
        # Lingjun Elastic Network Interface secondary private IP unique identifier.
        self.ip_name = ip_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.elastic_network_interface_id is not None:
            result['ElasticNetworkInterfaceId'] = self.elastic_network_interface_id
        if self.ip_name is not None:
            result['IpName'] = self.ip_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ElasticNetworkInterfaceId') is not None:
            self.elastic_network_interface_id = m.get('ElasticNetworkInterfaceId')
        if m.get('IpName') is not None:
            self.ip_name = m.get('IpName')
        return self


class AssignLeniPrivateIpAddressResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: AssignLeniPrivateIpAddressResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        # 
        # >  This parameter is returned only if Resource Access Management (RAM) permission verification failed.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The response data.
        self.content = content
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = AssignLeniPrivateIpAddressResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AssignLeniPrivateIpAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AssignLeniPrivateIpAddressResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AssignLeniPrivateIpAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssignPrivateIpAddressRequest(TeaModel):
    def __init__(
        self,
        assign_mac: bool = None,
        client_token: str = None,
        description: str = None,
        network_interface_id: str = None,
        private_ip_address: str = None,
        region_id: str = None,
        skip_config: bool = None,
        subnet_id: str = None,
    ):
        # Specifies whether to assign a mac address.
        self.assign_mac = assign_mac
        # By default, popApi is not ignored and idempotent
        self.client_token = client_token
        # The description of the variable.
        self.description = description
        # The ID of the network interface controller.
        # 
        # This parameter is required.
        self.network_interface_id = network_interface_id
        # The secondary private IP address.
        self.private_ip_address = private_ip_address
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The default value is false. If you set the value to true, the secondary private IP address application process can be accelerated.
        # 
        # >  For more information, submit a ticket.
        self.skip_config = skip_config
        # It belongs to the Lingjun subnet.
        # 
        # This parameter is required.
        self.subnet_id = subnet_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assign_mac is not None:
            result['AssignMac'] = self.assign_mac
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.skip_config is not None:
            result['SkipConfig'] = self.skip_config
        if self.subnet_id is not None:
            result['SubnetId'] = self.subnet_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssignMac') is not None:
            self.assign_mac = m.get('AssignMac')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SkipConfig') is not None:
            self.skip_config = m.get('SkipConfig')
        if m.get('SubnetId') is not None:
            self.subnet_id = m.get('SubnetId')
        return self


class AssignPrivateIpAddressResponseBodyContent(TeaModel):
    def __init__(
        self,
        ip_name: str = None,
        network_interface_id: str = None,
    ):
        # The unique IP identifier.
        self.ip_name = ip_name
        # Lingjun network interface controller ID.
        self.network_interface_id = network_interface_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_name is not None:
            result['IpName'] = self.ip_name
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpName') is not None:
            self.ip_name = m.get('IpName')
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')
        return self


class AssignPrivateIpAddressResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: AssignPrivateIpAddressResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The detailed reason why the access was denied.
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = AssignPrivateIpAddressResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AssignPrivateIpAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AssignPrivateIpAddressResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AssignPrivateIpAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociateVpdCidrBlockRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        secondary_cidr_block: str = None,
        vpd_id: str = None,
    ):
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The additional CIDR block.
        # 
        # This parameter is required.
        self.secondary_cidr_block = secondary_cidr_block
        # The ID of the Lingjun CIDR block.
        # 
        # This parameter is required.
        self.vpd_id = vpd_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.secondary_cidr_block is not None:
            result['SecondaryCidrBlock'] = self.secondary_cidr_block
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecondaryCidrBlock') is not None:
            self.secondary_cidr_block = m.get('SecondaryCidrBlock')
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        return self


class AssociateVpdCidrBlockResponseBodyContent(TeaModel):
    def __init__(
        self,
        vpd_id: str = None,
    ):
        # The ID of the Lingjun CIDR block.
        self.vpd_id = vpd_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        return self


class AssociateVpdCidrBlockResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: AssociateVpdCidrBlockResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The detailed reason why the access was denied.
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = AssociateVpdCidrBlockResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AssociateVpdCidrBlockResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AssociateVpdCidrBlockResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AssociateVpdCidrBlockResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachElasticNetworkInterfaceRequest(TeaModel):
    def __init__(
        self,
        elastic_network_interface_id: str = None,
        node_id: str = None,
        region_id: str = None,
    ):
        # The ID of the ENI.
        # 
        # This parameter is required.
        self.elastic_network_interface_id = elastic_network_interface_id
        # The ID of the node.
        # 
        # This parameter is required.
        self.node_id = node_id
        # The region ID of the disk.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.elastic_network_interface_id is not None:
            result['ElasticNetworkInterfaceId'] = self.elastic_network_interface_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ElasticNetworkInterfaceId') is not None:
            self.elastic_network_interface_id = m.get('ElasticNetworkInterfaceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AttachElasticNetworkInterfaceResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: Any = None,
        message: str = None,
        request_id: str = None,
    ):
        # The detailed reason why the access was denied.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # Response body
        self.content = content
        # The message returned.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.content is not None:
            result['Content'] = self.content
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
            self.content = m.get('Content')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AttachElasticNetworkInterfaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AttachElasticNetworkInterfaceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AttachElasticNetworkInterfaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateElasticNetworkInterfaceRequestTag(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateElasticNetworkInterfaceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        enable_jumbo_frame: bool = None,
        node_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        security_group_id: str = None,
        tag: List[CreateElasticNetworkInterfaceRequestTag] = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # The POP API is not ignored by default and is used for idempotence.
        self.client_token = client_token
        # The description of the response code.
        self.description = description
        # Whether to enable the jumbo frame capability
        self.enable_jumbo_frame = enable_jumbo_frame
        # The ID of the Lingjun node.
        self.node_id = node_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        # The ID of the security group.
        self.security_group_id = security_group_id
        self.tag = tag
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id
        # The ID of the VPC.
        # 
        # >  If the NodeId parameter is empty, the VpcId parameter is required. If the NodeId parameter is not empty, the VpcId parameter is optional.
        self.vpc_id = vpc_id
        # The zone ID.
        # 
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.enable_jumbo_frame is not None:
            result['EnableJumboFrame'] = self.enable_jumbo_frame
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnableJumboFrame') is not None:
            self.enable_jumbo_frame = m.get('EnableJumboFrame')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateElasticNetworkInterfaceRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateElasticNetworkInterfaceResponseBodyContent(TeaModel):
    def __init__(
        self,
        elastic_network_interface_id: str = None,
        node_id: str = None,
    ):
        # Lingjun Elastic Network Interface ID.
        self.elastic_network_interface_id = elastic_network_interface_id
        # The ID of the Lingjun node.
        self.node_id = node_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.elastic_network_interface_id is not None:
            result['ElasticNetworkInterfaceId'] = self.elastic_network_interface_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ElasticNetworkInterfaceId') is not None:
            self.elastic_network_interface_id = m.get('ElasticNetworkInterfaceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class CreateElasticNetworkInterfaceResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: CreateElasticNetworkInterfaceResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial. This parameter is returned only if Resource Access Management (RAM) permission verification failed.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The response data.
        self.content = content
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = CreateElasticNetworkInterfaceResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateElasticNetworkInterfaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateElasticNetworkInterfaceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateElasticNetworkInterfaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateErRequestTag(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateErRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        er_name: str = None,
        master_zone_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        tag: List[CreateErRequestTag] = None,
    ):
        # The description of the document.
        self.description = description
        # Lingjun HUB Name
        # 
        # This parameter is required.
        self.er_name = er_name
        # Primary Zone
        # 
        # This parameter is required.
        self.master_zone_id = master_zone_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Resource group instance ID
        self.resource_group_id = resource_group_id
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.er_name is not None:
            result['ErName'] = self.er_name
        if self.master_zone_id is not None:
            result['MasterZoneId'] = self.master_zone_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ErName') is not None:
            self.er_name = m.get('ErName')
        if m.get('MasterZoneId') is not None:
            self.master_zone_id = m.get('MasterZoneId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateErRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class CreateErResponseBodyContent(TeaModel):
    def __init__(
        self,
        er_id: str = None,
    ):
        # Lingjun HUB ID
        self.er_id = er_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.er_id is not None:
            result['ErId'] = self.er_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')
        return self


class CreateErResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: CreateErResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The detailed information about the failed permission verification.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The response parameters.
        self.content = content
        # The error message. (If the instance is in the Exception state, the exception cause is prompted.)
        self.message = message
        # Request ID of the current request
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = CreateErResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateErResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateErResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateErResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateErAttachmentRequest(TeaModel):
    def __init__(
        self,
        auto_receive_all_route: bool = None,
        er_attachment_name: str = None,
        er_id: str = None,
        instance_id: str = None,
        instance_type: str = None,
        region_id: str = None,
        resource_tenant_id: str = None,
    ):
        # Indicates whether to automatically receive all routes from all instances under the Lingjun HUB. Valid values:
        # 
        # *   **true**: received automatically.
        # *   **false**: Not received.
        # 
        # This parameter is required.
        self.auto_receive_all_route = auto_receive_all_route
        # The name of the network instance connection.
        # 
        # This parameter is required.
        self.er_attachment_name = er_attachment_name
        # Lingjun HUB ID.
        # 
        # This parameter is required.
        self.er_id = er_id
        # The ID of the network instance. Valid values: **VPD** and **VCC**.
        # 
        # For more information, see [What is Lingjun?](https://help.aliyun.com/document_detail/444430.html)
        # 
        # You can query **Lingjun CIDR Block** and **Lingjun Connection** by [ListVpds](https://help.aliyun.com/document_detail/2331077.html) and [ListVccs](https://help.aliyun.com/document_detail/2399526.html?) respectively.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The category of the instance. Valid values:
        # 
        # *   **VPD**: indicates the Lingjun CIDR block.
        # *   **VCC**: indicates a Lingjun connection.
        # 
        # This parameter is required.
        self.instance_type = instance_type
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the tenant to which the resource belongs. This parameter is required for cross-account resources.
        self.resource_tenant_id = resource_tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_receive_all_route is not None:
            result['AutoReceiveAllRoute'] = self.auto_receive_all_route
        if self.er_attachment_name is not None:
            result['ErAttachmentName'] = self.er_attachment_name
        if self.er_id is not None:
            result['ErId'] = self.er_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_tenant_id is not None:
            result['ResourceTenantId'] = self.resource_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoReceiveAllRoute') is not None:
            self.auto_receive_all_route = m.get('AutoReceiveAllRoute')
        if m.get('ErAttachmentName') is not None:
            self.er_attachment_name = m.get('ErAttachmentName')
        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceTenantId') is not None:
            self.resource_tenant_id = m.get('ResourceTenantId')
        return self


class CreateErAttachmentResponseBodyContent(TeaModel):
    def __init__(
        self,
        er_attachment_id: str = None,
    ):
        # The ID of the network connection instance.
        self.er_attachment_id = er_attachment_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.er_attachment_id is not None:
            result['ErAttachmentId'] = self.er_attachment_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErAttachmentId') is not None:
            self.er_attachment_id = m.get('ErAttachmentId')
        return self


class CreateErAttachmentResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: CreateErAttachmentResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The detailed information about the failed permission verification.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The response data.
        self.content = content
        # The error message. (If the instance is in the Exception state, the exception cause is displayed.)
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = CreateErAttachmentResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateErAttachmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateErAttachmentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateErAttachmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateErRouteMapRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        destination_cidr_block: str = None,
        er_id: str = None,
        reception_instance_id: str = None,
        reception_instance_owner: str = None,
        reception_instance_type: str = None,
        region_id: str = None,
        route_map_action: str = None,
        route_map_num: int = None,
        transmission_instance_id: str = None,
        transmission_instance_owner: str = None,
        transmission_instance_type: str = None,
    ):
        # Policy description
        self.description = description
        # Destination CIDR Block
        self.destination_cidr_block = destination_cidr_block
        # Lingjun HUB ID
        # 
        # This parameter is required.
        self.er_id = er_id
        # The ID of the destination instance.
        # 
        # This parameter is required.
        self.reception_instance_id = reception_instance_id
        # The tenant to which the route receiving instance belongs.
        self.reception_instance_owner = reception_instance_owner
        # The type of the destination instance. Valid values:
        # 
        # *   **VPD**: Lingjun network segment.
        # *   **VCC**: Lingjun Connection.
        # 
        # This parameter is required.
        self.reception_instance_type = reception_instance_type
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Policy behavior; optional values:
        # 
        # *   **permit**: Allow
        # *   **deny**: Rejected
        # 
        # This parameter is required.
        self.route_map_action = route_map_action
        # The ID of the policy.
        # 
        # A smaller sequence number indicates a lower priority. When a route is matched, a policy with a higher priority is preferentially matched.
        # 
        # **Valid values: 1001 to 2000**\
        # 
        # This parameter is required.
        self.route_map_num = route_map_num
        # The ID of the source instance.
        # 
        # This parameter is required.
        self.transmission_instance_id = transmission_instance_id
        # The tenant to which the route publish instance belongs
        self.transmission_instance_owner = transmission_instance_owner
        # The type of the source instance. Valid values:
        # 
        # *   **VPD**: Lingjun network segment.
        # *   **VCC**: Lingjun Connection.
        # 
        # This parameter is required.
        self.transmission_instance_type = transmission_instance_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        if self.er_id is not None:
            result['ErId'] = self.er_id
        if self.reception_instance_id is not None:
            result['ReceptionInstanceId'] = self.reception_instance_id
        if self.reception_instance_owner is not None:
            result['ReceptionInstanceOwner'] = self.reception_instance_owner
        if self.reception_instance_type is not None:
            result['ReceptionInstanceType'] = self.reception_instance_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.route_map_action is not None:
            result['RouteMapAction'] = self.route_map_action
        if self.route_map_num is not None:
            result['RouteMapNum'] = self.route_map_num
        if self.transmission_instance_id is not None:
            result['TransmissionInstanceId'] = self.transmission_instance_id
        if self.transmission_instance_owner is not None:
            result['TransmissionInstanceOwner'] = self.transmission_instance_owner
        if self.transmission_instance_type is not None:
            result['TransmissionInstanceType'] = self.transmission_instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')
        if m.get('ReceptionInstanceId') is not None:
            self.reception_instance_id = m.get('ReceptionInstanceId')
        if m.get('ReceptionInstanceOwner') is not None:
            self.reception_instance_owner = m.get('ReceptionInstanceOwner')
        if m.get('ReceptionInstanceType') is not None:
            self.reception_instance_type = m.get('ReceptionInstanceType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RouteMapAction') is not None:
            self.route_map_action = m.get('RouteMapAction')
        if m.get('RouteMapNum') is not None:
            self.route_map_num = m.get('RouteMapNum')
        if m.get('TransmissionInstanceId') is not None:
            self.transmission_instance_id = m.get('TransmissionInstanceId')
        if m.get('TransmissionInstanceOwner') is not None:
            self.transmission_instance_owner = m.get('TransmissionInstanceOwner')
        if m.get('TransmissionInstanceType') is not None:
            self.transmission_instance_type = m.get('TransmissionInstanceType')
        return self


class CreateErRouteMapResponseBodyContent(TeaModel):
    def __init__(
        self,
        er_route_map_id: str = None,
    ):
        # routing policy ID
        self.er_route_map_id = er_route_map_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.er_route_map_id is not None:
            result['ErRouteMapId'] = self.er_route_map_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErRouteMapId') is not None:
            self.er_route_map_id = m.get('ErRouteMapId')
        return self


class CreateErRouteMapResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: CreateErRouteMapResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial. This parameter is returned only if Resource Access Management (RAM) authentication failed.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The response parameters.
        self.content = content
        # The error message. (If the instance is in the Exception state, the exception cause is prompted.)
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = CreateErRouteMapResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateErRouteMapResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateErRouteMapResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateErRouteMapResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSubnetRequestTag(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateSubnetRequest(TeaModel):
    def __init__(
        self,
        cidr: str = None,
        region_id: str = None,
        subnet_name: str = None,
        tag: List[CreateSubnetRequestTag] = None,
        type: str = None,
        vpd_id: str = None,
        zone_id: str = None,
    ):
        # The CIDR block of the Subnet.
        # 
        # *   The network segment of the subnet must be a proper subset of the network segment of Lingjun to which it belongs, and the mask must be between 16 bits and 29 bits, which can provide 8 to 65536 addresses. For example, the CIDR block of the Lingjun CIDR block is 192.168.0.0/16, and the CIDR blocks of the subnets under the Lingjun CIDR block are 192.168.0.0/17 to 192.168.0.0/29.
        # *   The first and last three IP addresses of each subnet segment are reserved by the system. For example, the CIDR blocks of the subnet are 192.168.1.0/24,192.168.1.0, 192.168.1.253, 192.168.1.254, and 192.168.1.255.
        # 
        # This parameter is required.
        self.cidr = cidr
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Lingjun subnet instance name
        # 
        # This parameter is required.
        self.subnet_name = subnet_name
        # The tag information.
        # 
        # You can specify up to 20 tags.
        self.tag = tag
        # Lingjun Subnet Usage Type; optional; optional. Valid values:
        # 
        # *   **If you do not set this field for a common type**\
        # *   **OOB** :OOB type
        # *   **LB**: LB type
        self.type = type
        # The ID of the Lingjun CIDR block.
        # 
        # This parameter is required.
        self.vpd_id = vpd_id
        # The zone ID.
        # 
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr is not None:
            result['Cidr'] = self.cidr
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.subnet_name is not None:
            result['SubnetName'] = self.subnet_name
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
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
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateSubnetRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateSubnetResponseBodyContent(TeaModel):
    def __init__(
        self,
        subnet_id: str = None,
    ):
        # Lingjun subnet instance ID
        self.subnet_id = subnet_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.subnet_id is not None:
            result['SubnetId'] = self.subnet_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubnetId') is not None:
            self.subnet_id = m.get('SubnetId')
        return self


class CreateSubnetResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: CreateSubnetResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The detailed information about the failed permission verification.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The response parameters.
        self.content = content
        # The error message. (If the instance is in the Exception state, the exception cause is prompted.)
        self.message = message
        # The request ID, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = CreateSubnetResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateSubnetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSubnetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateSubnetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVccRequestTag(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateVccRequest(TeaModel):
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
        tag: List[CreateVccRequestTag] = None,
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
        # *   **VPC**\
        # *   **CEN (CENTR)**\
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
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
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
            for k in m.get('Tag'):
                temp_model = CreateVccRequestTag()
                self.tag.append(temp_model.from_map(k))
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


class CreateVccResponseBodyContent(TeaModel):
    def __init__(
        self,
        vcc_id: str = None,
    ):
        # The ID of the Lingjun connection instance.
        self.vcc_id = vcc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vcc_id is not None:
            result['VccId'] = self.vcc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VccId') is not None:
            self.vcc_id = m.get('VccId')
        return self


class CreateVccResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: CreateVccResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The detailed information about the failed permission verification.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The returned data.
        self.content = content
        # response message, if the success request is
        self.message = message
        # Request ID of the current request
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = CreateVccResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateVccResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateVccResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateVccResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVccGrantRuleRequest(TeaModel):
    def __init__(
        self,
        er_id: str = None,
        grant_tenant_id: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # Lingjun HUB ID
        # 
        # This parameter is required.
        self.er_id = er_id
        # Authorized Tenant ID
        # 
        # This parameter is required.
        self.grant_tenant_id = grant_tenant_id
        # Network Instance ID
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.er_id is not None:
            result['ErId'] = self.er_id
        if self.grant_tenant_id is not None:
            result['GrantTenantId'] = self.grant_tenant_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')
        if m.get('GrantTenantId') is not None:
            self.grant_tenant_id = m.get('GrantTenantId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateVccGrantRuleResponseBodyContent(TeaModel):
    def __init__(
        self,
        grant_rule_id: str = None,
    ):
        # Authorized resource primary key ID
        self.grant_rule_id = grant_rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.grant_rule_id is not None:
            result['GrantRuleId'] = self.grant_rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GrantRuleId') is not None:
            self.grant_rule_id = m.get('GrantRuleId')
        return self


class CreateVccGrantRuleResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: CreateVccGrantRuleResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial. This parameter is returned only if Resource Access Management (RAM) permission verification failed.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The response parameters.
        self.content = content
        # The error message. (If the instance is in the Exception state, the exception cause is prompted.)
        self.message = message
        # Request ID of the current request
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = CreateVccGrantRuleResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateVccGrantRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateVccGrantRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateVccGrantRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVccRouteEntryRequest(TeaModel):
    def __init__(
        self,
        destination_cidr_block: str = None,
        region_id: str = None,
        vcc_id: str = None,
    ):
        # Destination CIDR block
        self.destination_cidr_block = destination_cidr_block
        # The region ID.
        self.region_id = region_id
        # The ID of the Lingjun connection instance.
        self.vcc_id = vcc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vcc_id is not None:
            result['VccId'] = self.vcc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VccId') is not None:
            self.vcc_id = m.get('VccId')
        return self


class CreateVccRouteEntryResponseBodyContent(TeaModel):
    def __init__(
        self,
        vcc_route_entry_id: str = None,
    ):
        # The ID of the route entry.
        self.vcc_route_entry_id = vcc_route_entry_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vcc_route_entry_id is not None:
            result['VccRouteEntryId'] = self.vcc_route_entry_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VccRouteEntryId') is not None:
            self.vcc_route_entry_id = m.get('VccRouteEntryId')
        return self


class CreateVccRouteEntryResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: CreateVccRouteEntryResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The detailed information about the failed permission verification.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The returned data.
        self.content = content
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = CreateVccRouteEntryResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateVccRouteEntryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateVccRouteEntryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateVccRouteEntryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVpdRequestSubnets(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateVpdRequestTag(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateVpdRequest(TeaModel):
    def __init__(
        self,
        cidr: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        subnets: List[CreateVpdRequestSubnets] = None,
        tag: List[CreateVpdRequestTag] = None,
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
            for k in self.subnets:
                if k:
                    k.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr is not None:
            result['Cidr'] = self.cidr
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Subnets'] = []
        if self.subnets is not None:
            for k in self.subnets:
                result['Subnets'].append(k.to_map() if k else None)
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
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
            for k in m.get('Subnets'):
                temp_model = CreateVpdRequestSubnets()
                self.subnets.append(temp_model.from_map(k))
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateVpdRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VpdName') is not None:
            self.vpd_name = m.get('VpdName')
        return self


class CreateVpdResponseBodyContent(TeaModel):
    def __init__(
        self,
        subnet_ids: List[str] = None,
        vpd_id: str = None,
    ):
        # Lingjun subnet ID list
        self.subnet_ids = subnet_ids
        # Lingjun CIDR block instance ID
        self.vpd_id = vpd_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.subnet_ids is not None:
            result['SubnetIds'] = self.subnet_ids
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubnetIds') is not None:
            self.subnet_ids = m.get('SubnetIds')
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        return self


class CreateVpdResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: CreateVpdResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the failed permission verification.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The response parameters.
        self.content = content
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = CreateVpdResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateVpdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateVpdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateVpdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVpdGrantRuleRequest(TeaModel):
    def __init__(
        self,
        er_id: str = None,
        grant_tenant_id: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # Lingjun HUB ID
        # 
        # This parameter is required.
        self.er_id = er_id
        # Authorized Tenant ID
        # 
        # This parameter is required.
        self.grant_tenant_id = grant_tenant_id
        # Network Instance ID
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.er_id is not None:
            result['ErId'] = self.er_id
        if self.grant_tenant_id is not None:
            result['GrantTenantId'] = self.grant_tenant_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')
        if m.get('GrantTenantId') is not None:
            self.grant_tenant_id = m.get('GrantTenantId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateVpdGrantRuleResponseBodyContent(TeaModel):
    def __init__(
        self,
        grant_rule_id: str = None,
    ):
        # Authorized resource primary key ID
        self.grant_rule_id = grant_rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.grant_rule_id is not None:
            result['GrantRuleId'] = self.grant_rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GrantRuleId') is not None:
            self.grant_rule_id = m.get('GrantRuleId')
        return self


class CreateVpdGrantRuleResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: CreateVpdGrantRuleResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The response parameters.
        self.content = content
        # The error message. (If the instance is in the Exception state, the exception cause is prompted.)
        self.message = message
        # Request ID of the current request
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = CreateVpdGrantRuleResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateVpdGrantRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateVpdGrantRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateVpdGrantRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteElasticNetworkInterfaceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        elastic_network_interface_id: str = None,
        region_id: str = None,
    ):
        # By default, popApi is not ignored and idempotent
        self.client_token = client_token
        # Lingjun Elastic Network Interface ID
        # 
        # This parameter is required.
        self.elastic_network_interface_id = elastic_network_interface_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.elastic_network_interface_id is not None:
            result['ElasticNetworkInterfaceId'] = self.elastic_network_interface_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ElasticNetworkInterfaceId') is not None:
            self.elastic_network_interface_id = m.get('ElasticNetworkInterfaceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteElasticNetworkInterfaceResponseBodyContent(TeaModel):
    def __init__(
        self,
        elastic_network_interface_id: str = None,
        node_id: str = None,
    ):
        # Lingjun Elastic Network Interface ID
        self.elastic_network_interface_id = elastic_network_interface_id
        # Lingjun Node ID
        self.node_id = node_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.elastic_network_interface_id is not None:
            result['ElasticNetworkInterfaceId'] = self.elastic_network_interface_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ElasticNetworkInterfaceId') is not None:
            self.elastic_network_interface_id = m.get('ElasticNetworkInterfaceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class DeleteElasticNetworkInterfaceResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: DeleteElasticNetworkInterfaceResponseBodyContent = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = DeleteElasticNetworkInterfaceResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteElasticNetworkInterfaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteElasticNetworkInterfaceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteElasticNetworkInterfaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteErRequest(TeaModel):
    def __init__(
        self,
        er_id: str = None,
        region_id: str = None,
    ):
        # Lingjun HUB Instance ID
        # 
        # This parameter is required.
        self.er_id = er_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.er_id is not None:
            result['ErId'] = self.er_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteErResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: Any = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # Response body
        self.content = content
        # The error message. (If the instance is in the Exception state, the exception cause is prompted.)
        self.message = message
        # Request ID of the current request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.content is not None:
            result['Content'] = self.content
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
            self.content = m.get('Content')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteErResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteErResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteErResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteErAttachmentRequest(TeaModel):
    def __init__(
        self,
        er_attachment_id: str = None,
        er_id: str = None,
        region_id: str = None,
    ):
        # The ID of the network connection instance.
        # 
        # This parameter is required.
        self.er_attachment_id = er_attachment_id
        # Lingjun HUB Id
        # 
        # This parameter is required.
        self.er_id = er_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.er_attachment_id is not None:
            result['ErAttachmentId'] = self.er_attachment_id
        if self.er_id is not None:
            result['ErId'] = self.er_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErAttachmentId') is not None:
            self.er_attachment_id = m.get('ErAttachmentId')
        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteErAttachmentResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: Any = None,
        message: str = None,
        request_id: str = None,
    ):
        # 访问被拒绝的详细原因。
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The response content. If a resource has dependent resources, the existing dependent resources are returned.
        self.content = content
        # response message, if the success request is
        self.message = message
        # Request ID of the current request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.content is not None:
            result['Content'] = self.content
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
            self.content = m.get('Content')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteErAttachmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteErAttachmentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteErAttachmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteErRouteMapRequest(TeaModel):
    def __init__(
        self,
        er_id: str = None,
        er_route_map_ids: List[str] = None,
        region_id: str = None,
    ):
        # Lingjun HUB ID
        # 
        # This parameter is required.
        self.er_id = er_id
        # routing policy Instance ID List
        # 
        # This parameter is required.
        self.er_route_map_ids = er_route_map_ids
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.er_id is not None:
            result['ErId'] = self.er_id
        if self.er_route_map_ids is not None:
            result['ErRouteMapIds'] = self.er_route_map_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')
        if m.get('ErRouteMapIds') is not None:
            self.er_route_map_ids = m.get('ErRouteMapIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteErRouteMapResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: Any = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # Response body
        self.content = content
        # The error message. (If the instance is in the Exception state, the exception cause is prompted.)
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.content is not None:
            result['Content'] = self.content
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
            self.content = m.get('Content')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteErRouteMapResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteErRouteMapResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteErRouteMapResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSubnetRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        subnet_id: str = None,
        vpd_id: str = None,
        zone_id: str = None,
    ):
        # The region ID of the disk.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Lingjun subnet ID
        # 
        # This parameter is required.
        self.subnet_id = subnet_id
        # Lingjun CIDR block ID
        # 
        # This parameter is required.
        self.vpd_id = vpd_id
        # Zone
        # 
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.subnet_id is not None:
            result['SubnetId'] = self.subnet_id
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SubnetId') is not None:
            self.subnet_id = m.get('SubnetId')
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DeleteSubnetResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: Any = None,
        message: str = None,
        request_id: str = None,
    ):
        # The detailed reason why the access was denied.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # Response content (if the resource has dependent resources, the existing dependent resources will be returned)
        self.content = content
        # The error message. (If the instance is in the Exception state, the exception cause is prompted.)
        self.message = message
        # The request ID, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.content is not None:
            result['Content'] = self.content
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
            self.content = m.get('Content')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteSubnetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSubnetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteSubnetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVccGrantRuleRequest(TeaModel):
    def __init__(
        self,
        er_id: str = None,
        grant_rule_id: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # Lingjun HUB ID
        self.er_id = er_id
        # Authorization Entry ID
        # 
        # This parameter is required.
        self.grant_rule_id = grant_rule_id
        # Network Instance ID
        self.instance_id = instance_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.er_id is not None:
            result['ErId'] = self.er_id
        if self.grant_rule_id is not None:
            result['GrantRuleId'] = self.grant_rule_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')
        if m.get('GrantRuleId') is not None:
            self.grant_rule_id = m.get('GrantRuleId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteVccGrantRuleResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: Any = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        # 
        # >  This parameter is returned only if Resource Access Management (RAM) permission verification failed.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # Response body
        self.content = content
        # The error message. (If the instance is in the Exception state, the exception cause is prompted.)
        self.message = message
        # Request ID of the current request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.content is not None:
            result['Content'] = self.content
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
            self.content = m.get('Content')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteVccGrantRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteVccGrantRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteVccGrantRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVccRouteEntryRequest(TeaModel):
    def __init__(
        self,
        destination_cidr_block: str = None,
        region_id: str = None,
        vcc_id: str = None,
        vcc_route_entry_id: str = None,
    ):
        # Destination CIDR block
        self.destination_cidr_block = destination_cidr_block
        # The region ID.
        self.region_id = region_id
        # The ID of the Lingjun connection instance.
        self.vcc_id = vcc_id
        # The ID of the route entry.
        self.vcc_route_entry_id = vcc_route_entry_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vcc_id is not None:
            result['VccId'] = self.vcc_id
        if self.vcc_route_entry_id is not None:
            result['VccRouteEntryId'] = self.vcc_route_entry_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VccId') is not None:
            self.vcc_id = m.get('VccId')
        if m.get('VccRouteEntryId') is not None:
            self.vcc_route_entry_id = m.get('VccRouteEntryId')
        return self


class DeleteVccRouteEntryResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: Any = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # Response body
        self.content = content
        # The returned message.
        self.message = message
        # Request ID of the current request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.content is not None:
            result['Content'] = self.content
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
            self.content = m.get('Content')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteVccRouteEntryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteVccRouteEntryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteVccRouteEntryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVpdRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        vpd_id: str = None,
    ):
        # The ID of the region in which the instance resides.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the Lingjun CIDR block.
        # 
        # This parameter is required.
        self.vpd_id = vpd_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        return self


class DeleteVpdResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: Any = None,
        message: str = None,
        request_id: str = None,
    ):
        # The detailed reason why the access was denied.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The response parameters. (If a dependent resource exists, the existing dependent resource is returned.)
        self.content = content
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.content is not None:
            result['Content'] = self.content
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
            self.content = m.get('Content')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteVpdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteVpdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteVpdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVpdGrantRuleRequest(TeaModel):
    def __init__(
        self,
        er_id: str = None,
        grant_rule_id: str = None,
        grant_tenant_id: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # Lingjun HUB ID
        self.er_id = er_id
        # Authorization Entry ID
        # 
        # This parameter is required.
        self.grant_rule_id = grant_rule_id
        # Authorized Tenant ID
        self.grant_tenant_id = grant_tenant_id
        # Network Instance ID
        self.instance_id = instance_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.er_id is not None:
            result['ErId'] = self.er_id
        if self.grant_rule_id is not None:
            result['GrantRuleId'] = self.grant_rule_id
        if self.grant_tenant_id is not None:
            result['GrantTenantId'] = self.grant_tenant_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')
        if m.get('GrantRuleId') is not None:
            self.grant_rule_id = m.get('GrantRuleId')
        if m.get('GrantTenantId') is not None:
            self.grant_tenant_id = m.get('GrantTenantId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteVpdGrantRuleResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: Any = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # Response body
        self.content = content
        # The error message. (If the instance is in the Exception state, the exception cause is prompted.)
        self.message = message
        # Request ID of the current request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.content is not None:
            result['Content'] = self.content
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
            self.content = m.get('Content')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteVpdGrantRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteVpdGrantRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteVpdGrantRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSlrRequest(TeaModel):
    def __init__(
        self,
        resource_group_id: str = None,
    ):
        # The ID of the resource group to which the RAM instance belongs.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeSlrResponseBodyContent(TeaModel):
    def __init__(
        self,
        has_role: bool = None,
    ):
        # Whether the role exists
        self.has_role = has_role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_role is not None:
            result['HasRole'] = self.has_role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasRole') is not None:
            self.has_role = m.get('HasRole')
        return self


class DescribeSlrResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: DescribeSlrResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The information about the request denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The returned data.
        self.content = content
        # The error message. (If the instance is in the Exception state, the exception cause is prompted.)
        self.message = message
        # Request ID of the current request
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = DescribeSlrResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeSlrResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSlrResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeSlrResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachElasticNetworkInterfaceRequest(TeaModel):
    def __init__(
        self,
        elastic_network_interface_id: str = None,
        node_id: str = None,
        region_id: str = None,
    ):
        # The ID of the ENI.
        # 
        # This parameter is required.
        self.elastic_network_interface_id = elastic_network_interface_id
        # The ID of the node.
        # 
        # This parameter is required.
        self.node_id = node_id
        # The region ID of the disk.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.elastic_network_interface_id is not None:
            result['ElasticNetworkInterfaceId'] = self.elastic_network_interface_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ElasticNetworkInterfaceId') is not None:
            self.elastic_network_interface_id = m.get('ElasticNetworkInterfaceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DetachElasticNetworkInterfaceResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        # The detailed reason why the access was denied.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # Response
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetachElasticNetworkInterfaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetachElasticNetworkInterfaceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DetachElasticNetworkInterfaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDestinationCidrBlockRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
    ):
        # Instance ID
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Region ID
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetDestinationCidrBlockResponseBodyContent(TeaModel):
    def __init__(
        self,
        destination_cidr_block: List[str] = None,
    ):
        # List of destination CIDR block information for the current network instance
        self.destination_cidr_block = destination_cidr_block

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        return self


class GetDestinationCidrBlockResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: GetDestinationCidrBlockResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code
        self.code = code
        # Response content
        self.content = content
        # Error message. (Indicates the reason for the anomaly when the instance status is abnormal.)
        self.message = message
        # ID of this request
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetDestinationCidrBlockResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDestinationCidrBlockResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDestinationCidrBlockResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDestinationCidrBlockResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetElasticNetworkInterfaceRequest(TeaModel):
    def __init__(
        self,
        elastic_network_interface_id: str = None,
        region_id: str = None,
    ):
        # Lingjun Elastic Network Interface ID
        # 
        # This parameter is required.
        self.elastic_network_interface_id = elastic_network_interface_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.elastic_network_interface_id is not None:
            result['ElasticNetworkInterfaceId'] = self.elastic_network_interface_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ElasticNetworkInterfaceId') is not None:
            self.elastic_network_interface_id = m.get('ElasticNetworkInterfaceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetElasticNetworkInterfaceResponseBodyContentIpv6Addresses(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetElasticNetworkInterfaceResponseBodyContentPrivateIpAddresses(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetElasticNetworkInterfaceResponseBodyContentTags(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetElasticNetworkInterfaceResponseBodyContent(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        elastic_network_interface_id: str = None,
        enable_jumbo_frame: bool = None,
        gateway: str = None,
        gmt_modified: str = None,
        ip: str = None,
        ipv_6addresses: List[GetElasticNetworkInterfaceResponseBodyContentIpv6Addresses] = None,
        mac: str = None,
        mask: str = None,
        message: str = None,
        node_id: str = None,
        private_ip_addresses: List[GetElasticNetworkInterfaceResponseBodyContentPrivateIpAddresses] = None,
        region_id: str = None,
        resource_group_id: str = None,
        security_group_id: str = None,
        status: str = None,
        tags: List[GetElasticNetworkInterfaceResponseBodyContentTags] = None,
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
            for k in self.ipv_6addresses:
                if k:
                    k.validate()
        if self.private_ip_addresses:
            for k in self.private_ip_addresses:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            for k in self.ipv_6addresses:
                result['Ipv6Addresses'].append(k.to_map() if k else None)
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
            for k in self.private_ip_addresses:
                result['PrivateIpAddresses'].append(k.to_map() if k else None)
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
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
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
            for k in m.get('Ipv6Addresses'):
                temp_model = GetElasticNetworkInterfaceResponseBodyContentIpv6Addresses()
                self.ipv_6addresses.append(temp_model.from_map(k))
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
            for k in m.get('PrivateIpAddresses'):
                temp_model = GetElasticNetworkInterfaceResponseBodyContentPrivateIpAddresses()
                self.private_ip_addresses.append(temp_model.from_map(k))
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
            for k in m.get('Tags'):
                temp_model = GetElasticNetworkInterfaceResponseBodyContentTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class GetElasticNetworkInterfaceResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: GetElasticNetworkInterfaceResponseBodyContent = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetElasticNetworkInterfaceResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetElasticNetworkInterfaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetElasticNetworkInterfaceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetElasticNetworkInterfaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetErRequest(TeaModel):
    def __init__(
        self,
        er_id: str = None,
        region_id: str = None,
    ):
        # Lingjun HUB ID
        # 
        # This parameter is required.
        self.er_id = er_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.er_id is not None:
            result['ErId'] = self.er_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetErResponseBodyContentErAttachments(TeaModel):
    def __init__(
        self,
        across: bool = None,
        auto_receive_all_route: bool = None,
        create_time: str = None,
        er_attachment_id: str = None,
        er_attachment_name: str = None,
        er_id: str = None,
        gmt_modified: str = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_type: str = None,
        message: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_tenant_id: str = None,
        status: str = None,
        tenant_id: str = None,
    ):
        # Cross-account
        self.across = across
        # Receive all routes automatically
        self.auto_receive_all_route = auto_receive_all_route
        # The time when the data address was created.
        self.create_time = create_time
        # The connection ID of the Lingjun HUB network instance.
        self.er_attachment_id = er_attachment_id
        # Network Instance Name
        self.er_attachment_name = er_attachment_name
        # Lingjun HUB Instance ID
        self.er_id = er_id
        # The time when the agent was last modified.
        self.gmt_modified = gmt_modified
        # The instance ID.
        self.instance_id = instance_id
        # The name of the ECU.
        self.instance_name = instance_name
        # Instance type: VPD and VCC
        # 
        # Valid value:
        # 
        # *   VCC: Lingjun Connection.
        # *   VPD: Lingjun network segment.
        self.instance_type = instance_type
        # The returned message.
        self.message = message
        # The synchronized region where the ECS instances are deployed.
        self.region_id = region_id
        # Resource group instance ID
        self.resource_group_id = resource_group_id
        # The ID of the tenant to which the resource belongs.
        self.resource_tenant_id = resource_tenant_id
        # The status of the intervention entry. Valid value:
        self.status = status
        # The ID of the tenant.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.across is not None:
            result['Across'] = self.across
        if self.auto_receive_all_route is not None:
            result['AutoReceiveAllRoute'] = self.auto_receive_all_route
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.er_attachment_id is not None:
            result['ErAttachmentId'] = self.er_attachment_id
        if self.er_attachment_name is not None:
            result['ErAttachmentName'] = self.er_attachment_name
        if self.er_id is not None:
            result['ErId'] = self.er_id
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.message is not None:
            result['Message'] = self.message
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_tenant_id is not None:
            result['ResourceTenantId'] = self.resource_tenant_id
        if self.status is not None:
            result['Status'] = self.status
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Across') is not None:
            self.across = m.get('Across')
        if m.get('AutoReceiveAllRoute') is not None:
            self.auto_receive_all_route = m.get('AutoReceiveAllRoute')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ErAttachmentId') is not None:
            self.er_attachment_id = m.get('ErAttachmentId')
        if m.get('ErAttachmentName') is not None:
            self.er_attachment_name = m.get('ErAttachmentName')
        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceTenantId') is not None:
            self.resource_tenant_id = m.get('ResourceTenantId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class GetErResponseBodyContentErRouteEntrys(TeaModel):
    def __init__(
        self,
        destination_cidr_block: str = None,
        er_id: str = None,
        er_route_entry_id: str = None,
        gmt_modified: str = None,
        next_hop_id: str = None,
        next_hop_type: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_tenant_id: str = None,
        route_type: str = None,
        status: str = None,
        tenant_id: str = None,
    ):
        # Destination CIDR Block
        self.destination_cidr_block = destination_cidr_block
        # Lingjun HUB Instance ID
        self.er_id = er_id
        # The ID of the route entry.
        self.er_route_entry_id = er_route_entry_id
        # The time when the cluster was updated.
        self.gmt_modified = gmt_modified
        # Next Hop Instance
        self.next_hop_id = next_hop_id
        # Next Hop Instance Type
        self.next_hop_type = next_hop_type
        # The region ID.
        self.region_id = region_id
        # Resource group instance ID
        self.resource_group_id = resource_group_id
        # The ID of the tenant to which the resource belongs.
        self.resource_tenant_id = resource_tenant_id
        # Route type
        self.route_type = route_type
        # The status of the intervention entry. Valid value:
        self.status = status
        # The ID of the tenant.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        if self.er_id is not None:
            result['ErId'] = self.er_id
        if self.er_route_entry_id is not None:
            result['ErRouteEntryId'] = self.er_route_entry_id
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.next_hop_id is not None:
            result['NextHopId'] = self.next_hop_id
        if self.next_hop_type is not None:
            result['NextHopType'] = self.next_hop_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_tenant_id is not None:
            result['ResourceTenantId'] = self.resource_tenant_id
        if self.route_type is not None:
            result['RouteType'] = self.route_type
        if self.status is not None:
            result['Status'] = self.status
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')
        if m.get('ErRouteEntryId') is not None:
            self.er_route_entry_id = m.get('ErRouteEntryId')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('NextHopId') is not None:
            self.next_hop_id = m.get('NextHopId')
        if m.get('NextHopType') is not None:
            self.next_hop_type = m.get('NextHopType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceTenantId') is not None:
            self.resource_tenant_id = m.get('ResourceTenantId')
        if m.get('RouteType') is not None:
            self.route_type = m.get('RouteType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class GetErResponseBodyContentErRouteMaps(TeaModel):
    def __init__(
        self,
        action: str = None,
        create_time: str = None,
        description: str = None,
        destination_cidr_block: str = None,
        er_id: str = None,
        er_route_map_id: str = None,
        er_route_map_name: str = None,
        gmt_modified: str = None,
        message: str = None,
        reception_instance_id: str = None,
        reception_instance_name: str = None,
        reception_instance_owner: str = None,
        reception_instance_type: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        route_map_num: int = None,
        status: str = None,
        tenant_id: str = None,
        transmission_instance_id: str = None,
        transmission_instance_name: str = None,
        transmission_instance_owner: str = None,
        transmission_instance_type: str = None,
    ):
        # Policy behavior
        # 
        # Valid value:
        # 
        # *   deny: rejects the.
        # *   permit: The allows.
        self.action = action
        # The time when the data address was created.
        self.create_time = create_time
        # Policy description
        self.description = description
        # Destination CIDR Block
        self.destination_cidr_block = destination_cidr_block
        # Lingjun HUB ID
        self.er_id = er_id
        # routing policy ID
        self.er_route_map_id = er_route_map_id
        # The name of the routing policy.
        self.er_route_map_name = er_route_map_name
        # The time when the agent was last modified.
        self.gmt_modified = gmt_modified
        # The message that is returned.
        self.message = message
        # The ID of the destination instance.
        self.reception_instance_id = reception_instance_id
        # The name of the destination instance.
        self.reception_instance_name = reception_instance_name
        # The tenant to which the destination instance belongs.
        self.reception_instance_owner = reception_instance_owner
        # The type of the destination instance.
        self.reception_instance_type = reception_instance_type
        # The region ID.
        self.region_id = region_id
        # Resource group instance ID
        self.resource_group_id = resource_group_id
        # Policy sequence number (1001-2000)
        self.route_map_num = route_map_num
        # The status of the intervention entry. Valid value:
        self.status = status
        # The ID of the tenant.
        self.tenant_id = tenant_id
        # The ID of the source instance.
        self.transmission_instance_id = transmission_instance_id
        # Source instance name
        self.transmission_instance_name = transmission_instance_name
        # The tenant to which the source instance belongs.
        self.transmission_instance_owner = transmission_instance_owner
        # The type of the source instance.
        self.transmission_instance_type = transmission_instance_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        if self.er_id is not None:
            result['ErId'] = self.er_id
        if self.er_route_map_id is not None:
            result['ErRouteMapId'] = self.er_route_map_id
        if self.er_route_map_name is not None:
            result['ErRouteMapName'] = self.er_route_map_name
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.message is not None:
            result['Message'] = self.message
        if self.reception_instance_id is not None:
            result['ReceptionInstanceId'] = self.reception_instance_id
        if self.reception_instance_name is not None:
            result['ReceptionInstanceName'] = self.reception_instance_name
        if self.reception_instance_owner is not None:
            result['ReceptionInstanceOwner'] = self.reception_instance_owner
        if self.reception_instance_type is not None:
            result['ReceptionInstanceType'] = self.reception_instance_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.route_map_num is not None:
            result['RouteMapNum'] = self.route_map_num
        if self.status is not None:
            result['Status'] = self.status
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.transmission_instance_id is not None:
            result['TransmissionInstanceId'] = self.transmission_instance_id
        if self.transmission_instance_name is not None:
            result['TransmissionInstanceName'] = self.transmission_instance_name
        if self.transmission_instance_owner is not None:
            result['TransmissionInstanceOwner'] = self.transmission_instance_owner
        if self.transmission_instance_type is not None:
            result['TransmissionInstanceType'] = self.transmission_instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')
        if m.get('ErRouteMapId') is not None:
            self.er_route_map_id = m.get('ErRouteMapId')
        if m.get('ErRouteMapName') is not None:
            self.er_route_map_name = m.get('ErRouteMapName')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ReceptionInstanceId') is not None:
            self.reception_instance_id = m.get('ReceptionInstanceId')
        if m.get('ReceptionInstanceName') is not None:
            self.reception_instance_name = m.get('ReceptionInstanceName')
        if m.get('ReceptionInstanceOwner') is not None:
            self.reception_instance_owner = m.get('ReceptionInstanceOwner')
        if m.get('ReceptionInstanceType') is not None:
            self.reception_instance_type = m.get('ReceptionInstanceType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RouteMapNum') is not None:
            self.route_map_num = m.get('RouteMapNum')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('TransmissionInstanceId') is not None:
            self.transmission_instance_id = m.get('TransmissionInstanceId')
        if m.get('TransmissionInstanceName') is not None:
            self.transmission_instance_name = m.get('TransmissionInstanceName')
        if m.get('TransmissionInstanceOwner') is not None:
            self.transmission_instance_owner = m.get('TransmissionInstanceOwner')
        if m.get('TransmissionInstanceType') is not None:
            self.transmission_instance_type = m.get('TransmissionInstanceType')
        return self


class GetErResponseBodyContentTags(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetErResponseBodyContent(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        er_attachments: List[GetErResponseBodyContentErAttachments] = None,
        er_id: str = None,
        er_name: str = None,
        er_route_entrys: List[GetErResponseBodyContentErRouteEntrys] = None,
        er_route_maps: List[GetErResponseBodyContentErRouteMaps] = None,
        gmt_modified: str = None,
        master_zone_id: str = None,
        message: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        status: str = None,
        tags: List[GetErResponseBodyContentTags] = None,
        tenant_id: str = None,
    ):
        # The time when the data address was created.
        self.create_time = create_time
        # Description
        self.description = description
        # Network instance information list
        self.er_attachments = er_attachments
        # Lingjun HUB Instance ID
        self.er_id = er_id
        # Lingjun HUB Instance Name
        self.er_name = er_name
        # The list of route entry information.
        self.er_route_entrys = er_route_entrys
        # routing policy information list
        self.er_route_maps = er_route_maps
        # The time when the agent was last modified.
        self.gmt_modified = gmt_modified
        # Primary Zone
        self.master_zone_id = master_zone_id
        # The message that is returned.
        self.message = message
        # The region ID.
        self.region_id = region_id
        # Resource group instance ID
        self.resource_group_id = resource_group_id
        # The status of the intervention entry. Valid value:
        self.status = status
        self.tags = tags
        # The ID of the tenant.
        self.tenant_id = tenant_id

    def validate(self):
        if self.er_attachments:
            for k in self.er_attachments:
                if k:
                    k.validate()
        if self.er_route_entrys:
            for k in self.er_route_entrys:
                if k:
                    k.validate()
        if self.er_route_maps:
            for k in self.er_route_maps:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        result['ErAttachments'] = []
        if self.er_attachments is not None:
            for k in self.er_attachments:
                result['ErAttachments'].append(k.to_map() if k else None)
        if self.er_id is not None:
            result['ErId'] = self.er_id
        if self.er_name is not None:
            result['ErName'] = self.er_name
        result['ErRouteEntrys'] = []
        if self.er_route_entrys is not None:
            for k in self.er_route_entrys:
                result['ErRouteEntrys'].append(k.to_map() if k else None)
        result['ErRouteMaps'] = []
        if self.er_route_maps is not None:
            for k in self.er_route_maps:
                result['ErRouteMaps'].append(k.to_map() if k else None)
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.master_zone_id is not None:
            result['MasterZoneId'] = self.master_zone_id
        if self.message is not None:
            result['Message'] = self.message
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.status is not None:
            result['Status'] = self.status
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.er_attachments = []
        if m.get('ErAttachments') is not None:
            for k in m.get('ErAttachments'):
                temp_model = GetErResponseBodyContentErAttachments()
                self.er_attachments.append(temp_model.from_map(k))
        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')
        if m.get('ErName') is not None:
            self.er_name = m.get('ErName')
        self.er_route_entrys = []
        if m.get('ErRouteEntrys') is not None:
            for k in m.get('ErRouteEntrys'):
                temp_model = GetErResponseBodyContentErRouteEntrys()
                self.er_route_entrys.append(temp_model.from_map(k))
        self.er_route_maps = []
        if m.get('ErRouteMaps') is not None:
            for k in m.get('ErRouteMaps'):
                temp_model = GetErResponseBodyContentErRouteMaps()
                self.er_route_maps.append(temp_model.from_map(k))
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('MasterZoneId') is not None:
            self.master_zone_id = m.get('MasterZoneId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = GetErResponseBodyContentTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class GetErResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: GetErResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The response parameters.
        self.content = content
        # Information returned when the call fails
        self.message = message
        # Request ID of the current request
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetErResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetErResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetErResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetErResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetErAttachmentRequest(TeaModel):
    def __init__(
        self,
        er_attachment_id: str = None,
        er_id: str = None,
        region_id: str = None,
    ):
        # The ID of the Lingjun HUB network connection instance.
        # 
        # This parameter is required.
        self.er_attachment_id = er_attachment_id
        # Lingjun HUB ID.
        # 
        # This parameter is required.
        self.er_id = er_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.er_attachment_id is not None:
            result['ErAttachmentId'] = self.er_attachment_id
        if self.er_id is not None:
            result['ErId'] = self.er_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErAttachmentId') is not None:
            self.er_attachment_id = m.get('ErAttachmentId')
        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetErAttachmentResponseBodyContent(TeaModel):
    def __init__(
        self,
        across: bool = None,
        auto_receive_all_route: bool = None,
        create_time: str = None,
        er_attachment_id: str = None,
        er_attachment_name: str = None,
        er_id: str = None,
        gmt_modified: str = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_type: str = None,
        message: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_tenant_id: str = None,
        status: str = None,
        tenant_id: str = None,
    ):
        # Whether cross-account. Valid values:
        # 
        # *   **true**: The network instance is a cross-account resource.
        # *   **false**: The current network instance is a resource of the current account.
        self.across = across
        # Indicates whether to automatically receive all routes from all instances under the Lingjun HUB. Valid values:
        # 
        # *   **true**: received automatically.
        # *   **false**: Not received.
        self.auto_receive_all_route = auto_receive_all_route
        # The time when the activation code was created.
        self.create_time = create_time
        # The ID of the Lingjun HUB network instance.
        self.er_attachment_id = er_attachment_id
        # The name of the Lingjun HUB network instance.
        self.er_attachment_name = er_attachment_name
        # The ID of the Lingjun HUB instance.
        self.er_id = er_id
        # The time when the O\\&M task was modified.
        self.gmt_modified = gmt_modified
        # The ID of the network instance. Valid values: **VPD** and **VCC**.
        # 
        # For more information, see [What is Lingjun?](https://help.aliyun.com/document_detail/444430.html)
        # 
        # You can query **Lingjun CIDR blocks** and **Lingjun connections** by [ListVpds](https://help.aliyun.com/document_detail/2331077.html) and [ListVccs](https://help.aliyun.com/document_detail/2399526.html?) respectively.
        self.instance_id = instance_id
        # The instance name.
        self.instance_name = instance_name
        # The database type. Valid values:
        # 
        # *   **VPD**: indicates the Lingjun CIDR block.
        # *   **VCC**: indicates a Lingjun connection.
        self.instance_type = instance_type
        # The returned message.
        self.message = message
        # The region ID.
        self.region_id = region_id
        # Resource group instance ID
        self.resource_group_id = resource_group_id
        # The ID of the tenant to which the resource belongs.
        self.resource_tenant_id = resource_tenant_id
        # The status of the cache reserve instance. Valid values:
        # 
        # *   **Available**: Normal.
        # *   **Not Available**: Not available.
        # *   **Executing**: The task is being executed.
        # *   **Deleting**: The account is being deleted
        self.status = status
        # The tenant ID.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.across is not None:
            result['Across'] = self.across
        if self.auto_receive_all_route is not None:
            result['AutoReceiveAllRoute'] = self.auto_receive_all_route
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.er_attachment_id is not None:
            result['ErAttachmentId'] = self.er_attachment_id
        if self.er_attachment_name is not None:
            result['ErAttachmentName'] = self.er_attachment_name
        if self.er_id is not None:
            result['ErId'] = self.er_id
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.message is not None:
            result['Message'] = self.message
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_tenant_id is not None:
            result['ResourceTenantId'] = self.resource_tenant_id
        if self.status is not None:
            result['Status'] = self.status
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Across') is not None:
            self.across = m.get('Across')
        if m.get('AutoReceiveAllRoute') is not None:
            self.auto_receive_all_route = m.get('AutoReceiveAllRoute')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ErAttachmentId') is not None:
            self.er_attachment_id = m.get('ErAttachmentId')
        if m.get('ErAttachmentName') is not None:
            self.er_attachment_name = m.get('ErAttachmentName')
        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceTenantId') is not None:
            self.resource_tenant_id = m.get('ResourceTenantId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class GetErAttachmentResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: GetErAttachmentResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The response data.
        self.content = content
        # The error message. (If the instance is in the Exception state, the exception cause is displayed.)
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetErAttachmentResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetErAttachmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetErAttachmentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetErAttachmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetErRouteEntryRequest(TeaModel):
    def __init__(
        self,
        er_id: str = None,
        er_route_entry_id: str = None,
        region_id: str = None,
    ):
        # Lingjun HUB ID
        # 
        # This parameter is required.
        self.er_id = er_id
        # The ID of the route entry.
        # 
        # This parameter is required.
        self.er_route_entry_id = er_route_entry_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.er_id is not None:
            result['ErId'] = self.er_id
        if self.er_route_entry_id is not None:
            result['ErRouteEntryId'] = self.er_route_entry_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')
        if m.get('ErRouteEntryId') is not None:
            self.er_route_entry_id = m.get('ErRouteEntryId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetErRouteEntryResponseBodyContent(TeaModel):
    def __init__(
        self,
        destination_cidr_block: str = None,
        er_id: str = None,
        er_route_entry_id: str = None,
        gmt_modified: str = None,
        next_hop_id: str = None,
        next_hop_type: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        route_type: str = None,
        status: str = None,
        tenant_id: str = None,
    ):
        # Destination CIDR Block
        self.destination_cidr_block = destination_cidr_block
        # Lingjun HUB Instance ID
        self.er_id = er_id
        # The ID of the route entry.
        self.er_route_entry_id = er_route_entry_id
        # The time when the cluster was updated.
        self.gmt_modified = gmt_modified
        # Next Hop Instance
        self.next_hop_id = next_hop_id
        # Next Hop Instance Type
        self.next_hop_type = next_hop_type
        # The region ID.
        self.region_id = region_id
        # Resource group instance ID
        self.resource_group_id = resource_group_id
        # Route type
        self.route_type = route_type
        # The status of the intervention entry. Valid value:
        self.status = status
        # The ID of the tenant.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        if self.er_id is not None:
            result['ErId'] = self.er_id
        if self.er_route_entry_id is not None:
            result['ErRouteEntryId'] = self.er_route_entry_id
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.next_hop_id is not None:
            result['NextHopId'] = self.next_hop_id
        if self.next_hop_type is not None:
            result['NextHopType'] = self.next_hop_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.route_type is not None:
            result['RouteType'] = self.route_type
        if self.status is not None:
            result['Status'] = self.status
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')
        if m.get('ErRouteEntryId') is not None:
            self.er_route_entry_id = m.get('ErRouteEntryId')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('NextHopId') is not None:
            self.next_hop_id = m.get('NextHopId')
        if m.get('NextHopType') is not None:
            self.next_hop_type = m.get('NextHopType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RouteType') is not None:
            self.route_type = m.get('RouteType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class GetErRouteEntryResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: GetErRouteEntryResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The returned data.
        self.content = content
        # The error message. (If the instance is in the Exception state, the exception cause is prompted.)
        self.message = message
        # Request ID of the current request
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetErRouteEntryResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetErRouteEntryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetErRouteEntryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetErRouteEntryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetErRouteMapRequest(TeaModel):
    def __init__(
        self,
        er_id: str = None,
        er_route_map_id: str = None,
        region_id: str = None,
    ):
        # Lingjun HUB ID
        # 
        # This parameter is required.
        self.er_id = er_id
        # routing policy ID
        # 
        # This parameter is required.
        self.er_route_map_id = er_route_map_id
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.er_id is not None:
            result['ErId'] = self.er_id
        if self.er_route_map_id is not None:
            result['ErRouteMapId'] = self.er_route_map_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')
        if m.get('ErRouteMapId') is not None:
            self.er_route_map_id = m.get('ErRouteMapId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetErRouteMapResponseBodyContent(TeaModel):
    def __init__(
        self,
        action: str = None,
        description: str = None,
        destination_cidr_block: str = None,
        er_id: str = None,
        er_route_map_id: str = None,
        er_route_map_name: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        message: str = None,
        reception_instance_id: str = None,
        reception_instance_name: str = None,
        reception_instance_owner: str = None,
        reception_instance_type: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        route_map_num: int = None,
        status: str = None,
        tenant_id: str = None,
        transmission_instance_id: str = None,
        transmission_instance_name: str = None,
        transmission_instance_owner: str = None,
        transmission_instance_type: str = None,
    ):
        # Policy behavior; optional values:
        # 
        # *   **permit**: Allow
        # *   **deny**: Rejected
        self.action = action
        # Policy description
        self.description = description
        # Destination CIDR block
        self.destination_cidr_block = destination_cidr_block
        # Lingjun HUB ID
        self.er_id = er_id
        # Lingjun HUB routing policy ID
        self.er_route_map_id = er_route_map_id
        # Lingjun HUB routing policy Name
        self.er_route_map_name = er_route_map_name
        # The time when the data address was created.
        self.gmt_create = gmt_create
        # The time when the agent was last modified.
        self.gmt_modified = gmt_modified
        # The message that is returned.
        self.message = message
        # Receive Instance ID
        self.reception_instance_id = reception_instance_id
        # Receive Instance Name
        self.reception_instance_name = reception_instance_name
        # The tenant to which the receiving instance belongs
        self.reception_instance_owner = reception_instance_owner
        # The type of the received instance. Optional values:
        # 
        # *   **VPD**: Lingjun network segment.
        # *   **VCC**: Lingjun Connection.
        self.reception_instance_type = reception_instance_type
        # The region ID.
        self.region_id = region_id
        # Resource group instance ID
        self.resource_group_id = resource_group_id
        # The ID of the policy.
        # 
        # A smaller sequence number indicates a lower priority. When a route is matched, a policy with a higher priority is preferentially matched.
        # 
        # **Valid values: 1001 to 2000**\
        self.route_map_num = route_map_num
        # The status of the cache reserve instance. Valid values:
        # 
        # *   **Available**\
        # *   **Not Available**: Unavailable
        # *   **Executing**: Executing
        # *   **Deleting**: The node is being deleted.
        self.status = status
        # The ID of the tenant.
        self.tenant_id = tenant_id
        # Release Instance ID
        self.transmission_instance_id = transmission_instance_id
        # Release Instance Name
        self.transmission_instance_name = transmission_instance_name
        # The tenant to which the published instance belongs
        self.transmission_instance_owner = transmission_instance_owner
        # Publish instance type; optional values:
        # 
        # *   **VPD**: Lingjun network segment.
        # *   **VCC**: Lingjun Connection.
        self.transmission_instance_type = transmission_instance_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.description is not None:
            result['Description'] = self.description
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        if self.er_id is not None:
            result['ErId'] = self.er_id
        if self.er_route_map_id is not None:
            result['ErRouteMapId'] = self.er_route_map_id
        if self.er_route_map_name is not None:
            result['ErRouteMapName'] = self.er_route_map_name
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.message is not None:
            result['Message'] = self.message
        if self.reception_instance_id is not None:
            result['ReceptionInstanceId'] = self.reception_instance_id
        if self.reception_instance_name is not None:
            result['ReceptionInstanceName'] = self.reception_instance_name
        if self.reception_instance_owner is not None:
            result['ReceptionInstanceOwner'] = self.reception_instance_owner
        if self.reception_instance_type is not None:
            result['ReceptionInstanceType'] = self.reception_instance_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.route_map_num is not None:
            result['RouteMapNum'] = self.route_map_num
        if self.status is not None:
            result['Status'] = self.status
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.transmission_instance_id is not None:
            result['TransmissionInstanceId'] = self.transmission_instance_id
        if self.transmission_instance_name is not None:
            result['TransmissionInstanceName'] = self.transmission_instance_name
        if self.transmission_instance_owner is not None:
            result['TransmissionInstanceOwner'] = self.transmission_instance_owner
        if self.transmission_instance_type is not None:
            result['TransmissionInstanceType'] = self.transmission_instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')
        if m.get('ErRouteMapId') is not None:
            self.er_route_map_id = m.get('ErRouteMapId')
        if m.get('ErRouteMapName') is not None:
            self.er_route_map_name = m.get('ErRouteMapName')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ReceptionInstanceId') is not None:
            self.reception_instance_id = m.get('ReceptionInstanceId')
        if m.get('ReceptionInstanceName') is not None:
            self.reception_instance_name = m.get('ReceptionInstanceName')
        if m.get('ReceptionInstanceOwner') is not None:
            self.reception_instance_owner = m.get('ReceptionInstanceOwner')
        if m.get('ReceptionInstanceType') is not None:
            self.reception_instance_type = m.get('ReceptionInstanceType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RouteMapNum') is not None:
            self.route_map_num = m.get('RouteMapNum')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('TransmissionInstanceId') is not None:
            self.transmission_instance_id = m.get('TransmissionInstanceId')
        if m.get('TransmissionInstanceName') is not None:
            self.transmission_instance_name = m.get('TransmissionInstanceName')
        if m.get('TransmissionInstanceOwner') is not None:
            self.transmission_instance_owner = m.get('TransmissionInstanceOwner')
        if m.get('TransmissionInstanceType') is not None:
            self.transmission_instance_type = m.get('TransmissionInstanceType')
        return self


class GetErRouteMapResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: GetErRouteMapResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The returned data.
        self.content = content
        # The error message. (If the instance is in the Exception state, the exception cause is prompted.)
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetErRouteMapResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetErRouteMapResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetErRouteMapResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetErRouteMapResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFabricTopologyRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        lni_ids: List[str] = None,
        node_ids: List[str] = None,
        region_id: str = None,
        vpc_id: str = None,
        vpd_id: str = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # Lingjun network interface controller ID List
        self.lni_ids = lni_ids
        # Node ID list
        self.node_ids = node_ids
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the virtual private cloud (VPC).
        self.vpc_id = vpc_id
        # Lingjun CIDR block ID
        self.vpd_id = vpd_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.lni_ids is not None:
            result['LniIds'] = self.lni_ids
        if self.node_ids is not None:
            result['NodeIds'] = self.node_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('LniIds') is not None:
            self.lni_ids = m.get('LniIds')
        if m.get('NodeIds') is not None:
            self.node_ids = m.get('NodeIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        return self


class GetFabricTopologyResponseBodyContentTopoInfo(TeaModel):
    def __init__(
        self,
        layer_name: str = None,
        layer_type: str = None,
        next_layer: List[Any] = None,
    ):
        # The resource name.
        self.layer_name = layer_name
        # Hierarchical resource types
        # 
        # Valid value:
        # 
        # *   core: core layer.
        # *   node: Lingjun node.
        # *   lni: lingjun network interface controller.
        # *   spine: backbone layer.
        # *   leaf: access layer
        self.layer_type = layer_type
        # Next Level
        self.next_layer = next_layer

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.layer_name is not None:
            result['LayerName'] = self.layer_name
        if self.layer_type is not None:
            result['LayerType'] = self.layer_type
        if self.next_layer is not None:
            result['NextLayer'] = self.next_layer
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LayerName') is not None:
            self.layer_name = m.get('LayerName')
        if m.get('LayerType') is not None:
            self.layer_type = m.get('LayerType')
        if m.get('NextLayer') is not None:
            self.next_layer = m.get('NextLayer')
        return self


class GetFabricTopologyResponseBodyContent(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        region_id: str = None,
        topo_info: List[GetFabricTopologyResponseBodyContentTopoInfo] = None,
        vpc_id: str = None,
        vpd_id: str = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # The region ID.
        self.region_id = region_id
        # network interface controller Topology Information
        self.topo_info = topo_info
        # The ID of the virtual private cloud (VPC).
        self.vpc_id = vpc_id
        # Lingjun CIDR block ID
        self.vpd_id = vpd_id

    def validate(self):
        if self.topo_info:
            for k in self.topo_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['TopoInfo'] = []
        if self.topo_info is not None:
            for k in self.topo_info:
                result['TopoInfo'].append(k.to_map() if k else None)
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.topo_info = []
        if m.get('TopoInfo') is not None:
            for k in m.get('TopoInfo'):
                temp_model = GetFabricTopologyResponseBodyContentTopoInfo()
                self.topo_info.append(temp_model.from_map(k))
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        return self


class GetFabricTopologyResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: GetFabricTopologyResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The response parameters.
        self.content = content
        # The returned message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetFabricTopologyResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetFabricTopologyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFabricTopologyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetFabricTopologyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLeniPrivateIpAddressRequest(TeaModel):
    def __init__(
        self,
        elastic_network_interface_id: str = None,
        ip_name: str = None,
        region_id: str = None,
    ):
        # Lingjun Elastic Network Interface ID.
        # 
        # This parameter is required.
        self.elastic_network_interface_id = elastic_network_interface_id
        # Lingjun Elastic Network Interface secondary private IP unique identifier.
        # 
        # This parameter is required.
        self.ip_name = ip_name
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.elastic_network_interface_id is not None:
            result['ElasticNetworkInterfaceId'] = self.elastic_network_interface_id
        if self.ip_name is not None:
            result['IpName'] = self.ip_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ElasticNetworkInterfaceId') is not None:
            self.elastic_network_interface_id = m.get('ElasticNetworkInterfaceId')
        if m.get('IpName') is not None:
            self.ip_name = m.get('IpName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetLeniPrivateIpAddressResponseBodyContent(TeaModel):
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
        resource_group_id: str = None,
        status: str = None,
    ):
        # The description.
        self.description = description
        # Lingjun Elastic Network Interface ID.
        self.elastic_network_interface_id = elastic_network_interface_id
        # The time when the activation code was created.
        self.gmt_create = gmt_create
        # The time when the certificate was updated.
        self.gmt_modified = gmt_modified
        # Lingjun Elastic Network Interface secondary private IP unique identifier.
        self.ip_name = ip_name
        # The returned message.
        self.message = message
        # Lingjun Elastic Network Interface secondary private IP address.
        self.private_ip_address = private_ip_address
        # The region ID.
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        # The task status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
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
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetLeniPrivateIpAddressResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: GetLeniPrivateIpAddressResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The response data.
        self.content = content
        # The message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetLeniPrivateIpAddressResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetLeniPrivateIpAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLeniPrivateIpAddressResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetLeniPrivateIpAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLniPrivateIpAddressRequest(TeaModel):
    def __init__(
        self,
        ip_name: str = None,
        network_interface_id: str = None,
        region_id: str = None,
    ):
        # IP unique identifier
        # 
        # This parameter is required.
        self.ip_name = ip_name
        # Lingjun network interface controller ID
        # 
        # This parameter is required.
        self.network_interface_id = network_interface_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_name is not None:
            result['IpName'] = self.ip_name
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpName') is not None:
            self.ip_name = m.get('IpName')
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetLniPrivateIpAddressResponseBodyContent(TeaModel):
    def __init__(
        self,
        description: str = None,
        gmt_create: str = None,
        ip_address_mac: str = None,
        ip_name: str = None,
        message: str = None,
        network_interface_id: str = None,
        private_ip_address: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        status: str = None,
        subnet_id: str = None,
    ):
        # The instance description.
        self.description = description
        # The time when the data address was created.
        self.gmt_create = gmt_create
        # MAC address of the secondary private network
        self.ip_address_mac = ip_address_mac
        # IP unique identifier
        self.ip_name = ip_name
        # The error message. (If the instance is in the Exception state, the exception cause is prompted.)
        self.message = message
        # Lingjun network interface controller ID
        self.network_interface_id = network_interface_id
        # The secondary private IP address of the Lingjun network interface controller.
        self.private_ip_address = private_ip_address
        # The region ID.
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        # The state of the rule.
        self.status = status
        # The subnet instance ID.
        self.subnet_id = subnet_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.ip_address_mac is not None:
            result['IpAddressMac'] = self.ip_address_mac
        if self.ip_name is not None:
            result['IpName'] = self.ip_name
        if self.message is not None:
            result['Message'] = self.message
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.status is not None:
            result['Status'] = self.status
        if self.subnet_id is not None:
            result['SubnetId'] = self.subnet_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('IpAddressMac') is not None:
            self.ip_address_mac = m.get('IpAddressMac')
        if m.get('IpName') is not None:
            self.ip_name = m.get('IpName')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubnetId') is not None:
            self.subnet_id = m.get('SubnetId')
        return self


class GetLniPrivateIpAddressResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: GetLniPrivateIpAddressResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The response parameters.
        self.content = content
        # The error message. (If the instance is in the Exception state, the exception cause is prompted.)
        self.message = message
        # The request ID, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetLniPrivateIpAddressResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetLniPrivateIpAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLniPrivateIpAddressResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetLniPrivateIpAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNetworkInterfaceRequest(TeaModel):
    def __init__(
        self,
        network_interface_id: str = None,
        region_id: str = None,
        subnet_id: str = None,
    ):
        # Lingjun network interface controller ID
        # 
        # This parameter is required.
        self.network_interface_id = network_interface_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Subnet of Lingjun
        self.subnet_id = subnet_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.subnet_id is not None:
            result['SubnetId'] = self.subnet_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SubnetId') is not None:
            self.subnet_id = m.get('SubnetId')
        return self


class GetNetworkInterfaceResponseBodyContentPrivateIpAddressMacGroup(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetNetworkInterfaceResponseBodyContentSubnetBaseInfo(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetNetworkInterfaceResponseBodyContentTags(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetNetworkInterfaceResponseBodyContentVpdBaseInfo(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetNetworkInterfaceResponseBodyContent(TeaModel):
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
        private_ip_address_mac_group: List[GetNetworkInterfaceResponseBodyContentPrivateIpAddressMacGroup] = None,
        quota: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        service_mac: str = None,
        status: str = None,
        subnet_base_info: GetNetworkInterfaceResponseBodyContentSubnetBaseInfo = None,
        tags: List[GetNetworkInterfaceResponseBodyContentTags] = None,
        tenant_id: str = None,
        vpd_base_info: GetNetworkInterfaceResponseBodyContentVpdBaseInfo = None,
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
        self.resource_group_id = resource_group_id
        # Service network interface controller address
        self.service_mac = service_mac
        # The status of the intervention entry. Valid value:
        self.status = status
        # Lingjun subnet (Subnet) basic information
        self.subnet_base_info = subnet_base_info
        self.tags = tags
        # The ID of the tenant.
        self.tenant_id = tenant_id
        # Basic information of Lingjun network segment (VPD)
        self.vpd_base_info = vpd_base_info
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.private_ip_address_mac_group:
            for k in self.private_ip_address_mac_group:
                if k:
                    k.validate()
        if self.subnet_base_info:
            self.subnet_base_info.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.vpd_base_info:
            self.vpd_base_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            for k in self.private_ip_address_mac_group:
                result['PrivateIpAddressMacGroup'].append(k.to_map() if k else None)
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
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
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
            for k in m.get('PrivateIpAddressMacGroup'):
                temp_model = GetNetworkInterfaceResponseBodyContentPrivateIpAddressMacGroup()
                self.private_ip_address_mac_group.append(temp_model.from_map(k))
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
            temp_model = GetNetworkInterfaceResponseBodyContentSubnetBaseInfo()
            self.subnet_base_info = temp_model.from_map(m['SubnetBaseInfo'])
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = GetNetworkInterfaceResponseBodyContentTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('VpdBaseInfo') is not None:
            temp_model = GetNetworkInterfaceResponseBodyContentVpdBaseInfo()
            self.vpd_base_info = temp_model.from_map(m['VpdBaseInfo'])
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class GetNetworkInterfaceResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: GetNetworkInterfaceResponseBodyContent = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetNetworkInterfaceResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetNetworkInterfaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetNetworkInterfaceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetNetworkInterfaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNodeInfoForPodRequest(TeaModel):
    def __init__(
        self,
        node_id: str = None,
        region_id: str = None,
    ):
        # The ID of the node for this operation.
        # 
        # This parameter is required.
        self.node_id = node_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetNodeInfoForPodResponseBodyContent(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        hdeni_quota: int = None,
        leni_quota: int = None,
        leni_sip_quota: int = None,
        lni_sip_quota: int = None,
        node_id: str = None,
        region_id: str = None,
        v_switches: List[str] = None,
        vpc_id: str = None,
        zone_id: str = None,
        hdeni_ipv_6sip_quota: int = None,
        hdeni_sip_quota: int = None,
        leni_ipv_6sip_quota: int = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # Lingjun Gaomi network interface controller quota
        self.hdeni_quota = hdeni_quota
        # Lingjun Elastic Network Interface quota, including system type
        self.leni_quota = leni_quota
        # Lingjun Elastic Network Interface Secondary Private IP Quota
        self.leni_sip_quota = leni_sip_quota
        # Lingjun network interface controller Secondary Private IP Quota
        self.lni_sip_quota = lni_sip_quota
        # The ID of the node for this operation.
        self.node_id = node_id
        # The region ID.
        self.region_id = region_id
        # List of VSwitches that can apply for IP addresses on this node
        self.v_switches = v_switches
        # The ID of the Virtual Private Cloud to which the current node belongs.
        self.vpc_id = vpc_id
        # The zone ID.
        self.zone_id = zone_id
        self.hdeni_ipv_6sip_quota = hdeni_ipv_6sip_quota
        self.hdeni_sip_quota = hdeni_sip_quota
        self.leni_ipv_6sip_quota = leni_ipv_6sip_quota

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.hdeni_quota is not None:
            result['HdeniQuota'] = self.hdeni_quota
        if self.leni_quota is not None:
            result['LeniQuota'] = self.leni_quota
        if self.leni_sip_quota is not None:
            result['LeniSipQuota'] = self.leni_sip_quota
        if self.lni_sip_quota is not None:
            result['LniSipQuota'] = self.lni_sip_quota
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.v_switches is not None:
            result['VSwitches'] = self.v_switches
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.hdeni_ipv_6sip_quota is not None:
            result['hdeniIpv6SipQuota'] = self.hdeni_ipv_6sip_quota
        if self.hdeni_sip_quota is not None:
            result['hdeniSipQuota'] = self.hdeni_sip_quota
        if self.leni_ipv_6sip_quota is not None:
            result['leniIpv6SipQuota'] = self.leni_ipv_6sip_quota
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('HdeniQuota') is not None:
            self.hdeni_quota = m.get('HdeniQuota')
        if m.get('LeniQuota') is not None:
            self.leni_quota = m.get('LeniQuota')
        if m.get('LeniSipQuota') is not None:
            self.leni_sip_quota = m.get('LeniSipQuota')
        if m.get('LniSipQuota') is not None:
            self.lni_sip_quota = m.get('LniSipQuota')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VSwitches') is not None:
            self.v_switches = m.get('VSwitches')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('hdeniIpv6SipQuota') is not None:
            self.hdeni_ipv_6sip_quota = m.get('hdeniIpv6SipQuota')
        if m.get('hdeniSipQuota') is not None:
            self.hdeni_sip_quota = m.get('hdeniSipQuota')
        if m.get('leniIpv6SipQuota') is not None:
            self.leni_ipv_6sip_quota = m.get('leniIpv6SipQuota')
        return self


class GetNodeInfoForPodResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: GetNodeInfoForPodResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the failed permission verification.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The response parameters.
        self.content = content
        # The error message. (If the instance is in the Exception state, the exception cause is prompted.)
        self.message = message
        # Request ID of the current request
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetNodeInfoForPodResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetNodeInfoForPodResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetNodeInfoForPodResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetNodeInfoForPodResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSubnetRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        subnet_id: str = None,
        vpd_id: str = None,
    ):
        # The region ID of the data center.
        self.region_id = region_id
        # The ID of the Lingjun subnet instance.
        # 
        # This parameter is required.
        self.subnet_id = subnet_id
        # The ID of the CIDR block to which Lingjun belongs.
        self.vpd_id = vpd_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.subnet_id is not None:
            result['SubnetId'] = self.subnet_id
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SubnetId') is not None:
            self.subnet_id = m.get('SubnetId')
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        return self


class GetSubnetResponseBodyContentTags(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetSubnetResponseBodyContentVpdBaseInfo(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetSubnetResponseBodyContent(TeaModel):
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
        tags: List[GetSubnetResponseBodyContentTags] = None,
        tenant_id: str = None,
        type: str = None,
        vpd_base_info: GetSubnetResponseBodyContentVpdBaseInfo = None,
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
        # *   **Empty for common data types**\
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
            for k in self.tags:
                if k:
                    k.validate()
        if self.vpd_base_info:
            self.vpd_base_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
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
            for k in m.get('Tags'):
                temp_model = GetSubnetResponseBodyContentTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VpdBaseInfo') is not None:
            temp_model = GetSubnetResponseBodyContentVpdBaseInfo()
            self.vpd_base_info = temp_model.from_map(m['VpdBaseInfo'])
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class GetSubnetResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: GetSubnetResponseBodyContent = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetSubnetResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSubnetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSubnetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetSubnetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVccRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        enable_page: bool = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        vcc_id: str = None,
    ):
        # By default, popApi is not ignored and idempotent
        self.client_token = client_token
        # Paging Parameters: The current parameters are obsolete.
        self.enable_page = enable_page
        # Paging Parameters: The current parameters are obsolete.
        self.page_number = page_number
        # Paging Parameters: The current parameters are obsolete.
        self.page_size = page_size
        # The region ID.
        self.region_id = region_id
        # The ID of the Lingjun connection instance.
        # 
        # This parameter is required.
        self.vcc_id = vcc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.enable_page is not None:
            result['EnablePage'] = self.enable_page
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vcc_id is not None:
            result['VccId'] = self.vcc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('EnablePage') is not None:
            self.enable_page = m.get('EnablePage')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VccId') is not None:
            self.vcc_id = m.get('VccId')
        return self


class GetVccResponseBodyContentAliyunRouterInfo(TeaModel):
    def __init__(
        self,
        local_gateway_ip: str = None,
        mask: str = None,
        pc_id: str = None,
        peer_gateway_ip: str = None,
        vbr_id: str = None,
        vlan_id: str = None,
    ):
        # IPv4 address of Alibaba Cloud-side interconnection
        self.local_gateway_ip = local_gateway_ip
        # Masking
        self.mask = mask
        # Express Connect circuit ID
        self.pc_id = pc_id
        # Lingjun Side Interconnection IPv4 Address
        self.peer_gateway_ip = peer_gateway_ip
        # The ID of the VBR.
        self.vbr_id = vbr_id
        # VLAN ID of the VBR
        self.vlan_id = vlan_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_gateway_ip is not None:
            result['LocalGatewayIp'] = self.local_gateway_ip
        if self.mask is not None:
            result['Mask'] = self.mask
        if self.pc_id is not None:
            result['PcId'] = self.pc_id
        if self.peer_gateway_ip is not None:
            result['PeerGatewayIp'] = self.peer_gateway_ip
        if self.vbr_id is not None:
            result['VbrId'] = self.vbr_id
        if self.vlan_id is not None:
            result['VlanId'] = self.vlan_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalGatewayIp') is not None:
            self.local_gateway_ip = m.get('LocalGatewayIp')
        if m.get('Mask') is not None:
            self.mask = m.get('Mask')
        if m.get('PcId') is not None:
            self.pc_id = m.get('PcId')
        if m.get('PeerGatewayIp') is not None:
            self.peer_gateway_ip = m.get('PeerGatewayIp')
        if m.get('VbrId') is not None:
            self.vbr_id = m.get('VbrId')
        if m.get('VlanId') is not None:
            self.vlan_id = m.get('VlanId')
        return self


class GetVccResponseBodyContentCisRouterInfoCcInfos(TeaModel):
    def __init__(
        self,
        cc_id: str = None,
        local_gateway_ip: str = None,
        remote_gateway_ip: str = None,
        status: str = None,
        subnet_mask: str = None,
        vlan_id: str = None,
    ):
        # Leased Line ID
        self.cc_id = cc_id
        # Lingjun Side Interconnection IPv4 Address
        self.local_gateway_ip = local_gateway_ip
        # Lingjun Side Interconnection IPv4 Address
        self.remote_gateway_ip = remote_gateway_ip
        # The state of the rule.
        self.status = status
        # Subnet mask
        self.subnet_mask = subnet_mask
        # Vlan ID of the leased line
        self.vlan_id = vlan_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cc_id is not None:
            result['CcId'] = self.cc_id
        if self.local_gateway_ip is not None:
            result['LocalGatewayIp'] = self.local_gateway_ip
        if self.remote_gateway_ip is not None:
            result['RemoteGatewayIp'] = self.remote_gateway_ip
        if self.status is not None:
            result['Status'] = self.status
        if self.subnet_mask is not None:
            result['SubnetMask'] = self.subnet_mask
        if self.vlan_id is not None:
            result['VlanId'] = self.vlan_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CcId') is not None:
            self.cc_id = m.get('CcId')
        if m.get('LocalGatewayIp') is not None:
            self.local_gateway_ip = m.get('LocalGatewayIp')
        if m.get('RemoteGatewayIp') is not None:
            self.remote_gateway_ip = m.get('RemoteGatewayIp')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubnetMask') is not None:
            self.subnet_mask = m.get('SubnetMask')
        if m.get('VlanId') is not None:
            self.vlan_id = m.get('VlanId')
        return self


class GetVccResponseBodyContentCisRouterInfo(TeaModel):
    def __init__(
        self,
        cc_infos: List[GetVccResponseBodyContentCisRouterInfoCcInfos] = None,
        ccr_id: str = None,
    ):
        # Leased Line Information List
        self.cc_infos = cc_infos
        # The ID of the on-cloud router instance.
        self.ccr_id = ccr_id

    def validate(self):
        if self.cc_infos:
            for k in self.cc_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CcInfos'] = []
        if self.cc_infos is not None:
            for k in self.cc_infos:
                result['CcInfos'].append(k.to_map() if k else None)
        if self.ccr_id is not None:
            result['CcrId'] = self.ccr_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cc_infos = []
        if m.get('CcInfos') is not None:
            for k in m.get('CcInfos'):
                temp_model = GetVccResponseBodyContentCisRouterInfoCcInfos()
                self.cc_infos.append(temp_model.from_map(k))
        if m.get('CcrId') is not None:
            self.ccr_id = m.get('CcrId')
        return self


class GetVccResponseBodyContentErInfos(TeaModel):
    def __init__(
        self,
        connections: int = None,
        create_time: str = None,
        description: str = None,
        er_id: str = None,
        er_name: str = None,
        gmt_modified: str = None,
        master_zone_id: str = None,
        message: str = None,
        region_id: str = None,
        route_maps: int = None,
        status: str = None,
        tenant_id: str = None,
    ):
        # Connections
        self.connections = connections
        # The time when the data address was created.
        self.create_time = create_time
        # Description
        self.description = description
        # Lingjun HUB ID
        self.er_id = er_id
        # Lingjun HUB Instance Name
        self.er_name = er_name
        # The time when the agent was last modified.
        self.gmt_modified = gmt_modified
        # Primary Zone
        self.master_zone_id = master_zone_id
        # The message that is returned.
        self.message = message
        # Lingjun HUB Region Information
        self.region_id = region_id
        # Number of routing policy
        self.route_maps = route_maps
        # The status of the intervention entry. Valid value:
        self.status = status
        # The ID of the tenant.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connections is not None:
            result['Connections'] = self.connections
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.er_id is not None:
            result['ErId'] = self.er_id
        if self.er_name is not None:
            result['ErName'] = self.er_name
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.master_zone_id is not None:
            result['MasterZoneId'] = self.master_zone_id
        if self.message is not None:
            result['Message'] = self.message
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.route_maps is not None:
            result['RouteMaps'] = self.route_maps
        if self.status is not None:
            result['Status'] = self.status
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Connections') is not None:
            self.connections = m.get('Connections')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')
        if m.get('ErName') is not None:
            self.er_name = m.get('ErName')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('MasterZoneId') is not None:
            self.master_zone_id = m.get('MasterZoneId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RouteMaps') is not None:
            self.route_maps = m.get('RouteMaps')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class GetVccResponseBodyContentTags(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetVccResponseBodyContentVbrInfosVbrBgpPeers(TeaModel):
    def __init__(
        self,
        bgp_group_id: str = None,
        bgp_peer_id: str = None,
        peer_asn: str = None,
        peer_ip_address: str = None,
        status: str = None,
    ):
        # BGP Group ID
        self.bgp_group_id = bgp_group_id
        # BGP peer ID
        self.bgp_peer_id = bgp_peer_id
        # Peer AS No.
        self.peer_asn = peer_asn
        # BGP peer IP address
        self.peer_ip_address = peer_ip_address
        # The status of the BGP peer. Valid values:
        # 
        # *   Pending: pending
        # *   Available: The route is available.
        # *   Modifying: being modified
        # *   Deleting: The IPv4 gateway is being deleted.
        # *   Deleted
        # *   Not Available
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bgp_group_id is not None:
            result['BgpGroupId'] = self.bgp_group_id
        if self.bgp_peer_id is not None:
            result['BgpPeerId'] = self.bgp_peer_id
        if self.peer_asn is not None:
            result['PeerAsn'] = self.peer_asn
        if self.peer_ip_address is not None:
            result['PeerIpAddress'] = self.peer_ip_address
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BgpGroupId') is not None:
            self.bgp_group_id = m.get('BgpGroupId')
        if m.get('BgpPeerId') is not None:
            self.bgp_peer_id = m.get('BgpPeerId')
        if m.get('PeerAsn') is not None:
            self.peer_asn = m.get('PeerAsn')
        if m.get('PeerIpAddress') is not None:
            self.peer_ip_address = m.get('PeerIpAddress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetVccResponseBodyContentVbrInfos(TeaModel):
    def __init__(
        self,
        cen_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        status: str = None,
        vbr_bgp_peers: List[GetVccResponseBodyContentVbrInfosVbrBgpPeers] = None,
        vbr_id: str = None,
    ):
        # CEN ID
        self.cen_id = cen_id
        # The time when the data address was created.
        self.gmt_create = gmt_create
        # The time when the agent was last modified.
        self.gmt_modified = gmt_modified
        # The status of the VBR. Valid values:
        # 
        # *   unconfirmed
        # *   active: The VPN gateway is in a normal state.
        # *   terminating: The connection is being terminated.
        # *   terminated: The connection is terminated.
        # *   recovering: The task is being recovered.
        # *   deleting: The GDN is being deleted.
        # *   Available: The service is available.
        self.status = status
        # BGP neighbor information list
        self.vbr_bgp_peers = vbr_bgp_peers
        # The ID of the border router.
        self.vbr_id = vbr_id

    def validate(self):
        if self.vbr_bgp_peers:
            for k in self.vbr_bgp_peers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.status is not None:
            result['Status'] = self.status
        result['VbrBgpPeers'] = []
        if self.vbr_bgp_peers is not None:
            for k in self.vbr_bgp_peers:
                result['VbrBgpPeers'].append(k.to_map() if k else None)
        if self.vbr_id is not None:
            result['VbrId'] = self.vbr_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.vbr_bgp_peers = []
        if m.get('VbrBgpPeers') is not None:
            for k in m.get('VbrBgpPeers'):
                temp_model = GetVccResponseBodyContentVbrInfosVbrBgpPeers()
                self.vbr_bgp_peers.append(temp_model.from_map(k))
        if m.get('VbrId') is not None:
            self.vbr_id = m.get('VbrId')
        return self


class GetVccResponseBodyContentVpdBaseInfo(TeaModel):
    def __init__(
        self,
        cidr: str = None,
        create_time: str = None,
        vpd_id: str = None,
        vpd_name: str = None,
    ):
        # Network address segment
        self.cidr = cidr
        # The time when the data address was created.
        self.create_time = create_time
        # Lingjun CIDR block instance ID
        self.vpd_id = vpd_id
        # Lingjun CIDR block instance name
        self.vpd_name = vpd_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetVccResponseBodyContent(TeaModel):
    def __init__(
        self,
        access_point_id: str = None,
        aliyun_router_info: List[GetVccResponseBodyContentAliyunRouterInfo] = None,
        attach_er_status: bool = None,
        bandwidth: int = None,
        bandwidth_str: str = None,
        bgp_asn: str = None,
        bgp_cidr: str = None,
        cen_id: str = None,
        cen_owner_id: str = None,
        cis_router_info: List[GetVccResponseBodyContentCisRouterInfo] = None,
        commodity_code: str = None,
        connection_type: str = None,
        create_time: str = None,
        current_node: str = None,
        duration: str = None,
        er_infos: List[GetVccResponseBodyContentErInfos] = None,
        expiration_date: str = None,
        gmt_modified: str = None,
        internet_charge_type: str = None,
        line_operator: str = None,
        message: str = None,
        pay_type: str = None,
        port_type: str = None,
        pricing_cycle: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        spec: str = None,
        status: str = None,
        tags: List[GetVccResponseBodyContentTags] = None,
        tenant_id: str = None,
        v_switch_id: str = None,
        vbr_infos: List[GetVccResponseBodyContentVbrInfos] = None,
        vcc_id: str = None,
        vcc_name: str = None,
        vpc_id: str = None,
        vpd_base_info: GetVccResponseBodyContentVpdBaseInfo = None,
        vpd_id: str = None,
        zone_id: str = None,
    ):
        # Express Connect circuit access point ID:
        # 
        # *   **ap-cn-wulanchabu-jn-ts-A**: Ulanqab-Jining-A
        # *   **ap-cn-heyuan-yc-ts-SA127**: Heyuan-Yuancheng-A
        self.access_point_id = access_point_id
        # Alibaba Cloud route information list
        self.aliyun_router_info = aliyun_router_info
        # Whether Lingjun HUB has been bound to a network instance
        # 
        # *   **true**: Bound
        # *   **false**: unbound
        self.attach_er_status = attach_er_status
        # bandwidth
        self.bandwidth = bandwidth
        # The bandwidth of the port.
        self.bandwidth_str = bandwidth_str
        # BGP AS number
        self.bgp_asn = bgp_asn
        # BGP CIDR block
        self.bgp_cidr = bgp_cidr
        # The ID of the CEN instance; [What is the CEN?](https://help.aliyun.com/document_detail/181681.html)
        # 
        # You can call the [DescribeCens](https://help.aliyun.com/document_detail/468215.htm) to query the information of CEN instances under the current Alibaba Cloud account.
        self.cen_id = cen_id
        # Account to which the CEN belongs
        self.cen_owner_id = cen_owner_id
        # Lingjun Network Routing Information List
        self.cis_router_info = cis_router_info
        # Commodity code
        self.commodity_code = commodity_code
        # The connection mode. Valid values:
        # 
        # *   **VPC**\
        # *   **CENTR**\
        self.connection_type = connection_type
        # The time when the data address was created.
        self.create_time = create_time
        # Current Node
        self.current_node = current_node
        # Cycle
        self.duration = duration
        # List of bound Lingjun HUB information
        self.er_infos = er_infos
        # The time when the application expired.
        self.expiration_date = expiration_date
        # The time when the agent was last modified.
        self.gmt_modified = gmt_modified
        # The billing method for network usage.
        # 
        # *   **PayByTraffic**: pay-by-traffic
        # *   **PayByBandwidth**: pay-by-bandwidth
        self.internet_charge_type = internet_charge_type
        # The connectivity provider of the Express Connect circuit. Valid values:
        # 
        # *   **CO**: other connectivity providers in the Chinese mainland
        self.line_operator = line_operator
        # The error message. (If the instance is in the Exception state, the exception cause is prompted.)
        self.message = message
        # The billing method of the instance. Valid values:
        # 
        # *   **PREPAY**: subscription
        # *   **POSTPAY**: pay-as-you-go
        self.pay_type = pay_type
        # The port type of the Express Connect circuit. Valid values:
        # 
        # *   **100GBase-LR**: 100,000 megabytes of single-mode optical port (10 km)
        self.port_type = port_type
        # The billing cycle. Valid values:
        # 
        # *   **Month**: Billed on a monthly basis
        # *   **Year**: Billed on an annual basis
        self.pricing_cycle = pricing_cycle
        # The region ID.
        self.region_id = region_id
        # The ID of your Alibaba Cloud resource group.
        # 
        # For more information about resource groups, see [Resource groups](https://help.aliyun.com/document_detail/94475.htm).
        self.resource_group_id = resource_group_id
        # Specification; value:
        # 
        # *   **Large**: Large
        self.spec = spec
        # The status of the cache reserve instance. Valid values:
        # 
        # *   **Available**: Normal.
        # *   **Not Available**: Not available.
        # *   **Executing**: The task is being executed.
        # *   **Deleting**: The account is being deleted
        self.status = status
        # The tag information.
        # 
        # You can specify up to 20 tags.
        self.tags = tags
        # The ID of the tenant.
        self.tenant_id = tenant_id
        # The ID of the vSwitch. [Virtual Private Cloud VSwitch](https://help.aliyun.com/document_detail/100380.html).
        # 
        # You can call the [DescribeVSwitches](https://help.aliyun.com/document_detail/35748.html) operation to query created vSwitches.
        self.v_switch_id = v_switch_id
        # Information list of border routers
        self.vbr_infos = vbr_infos
        # The ID of the Lingjun connection instance.
        self.vcc_id = vcc_id
        # The name of the Lingjun connection instance.
        self.vcc_name = vcc_name
        # Virtual Private Cloud IDs; [What is Virtual Private Cloud](https://help.aliyun.com/document_detail/34217.html)
        # 
        # You can call the [DescribeVpcs](https://help.aliyun.com/document_detail/35739.html#demo-0) operation to query the specified VPC.
        self.vpc_id = vpc_id
        # Lingjun network segment information (applicable to the scene where the old version of Lingjun connection is directly bound to Lingjun network segment)
        self.vpd_base_info = vpd_base_info
        # Lingjun CIDR block instance ID
        self.vpd_id = vpd_id
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.aliyun_router_info:
            for k in self.aliyun_router_info:
                if k:
                    k.validate()
        if self.cis_router_info:
            for k in self.cis_router_info:
                if k:
                    k.validate()
        if self.er_infos:
            for k in self.er_infos:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.vbr_infos:
            for k in self.vbr_infos:
                if k:
                    k.validate()
        if self.vpd_base_info:
            self.vpd_base_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_point_id is not None:
            result['AccessPointId'] = self.access_point_id
        result['AliyunRouterInfo'] = []
        if self.aliyun_router_info is not None:
            for k in self.aliyun_router_info:
                result['AliyunRouterInfo'].append(k.to_map() if k else None)
        if self.attach_er_status is not None:
            result['AttachErStatus'] = self.attach_er_status
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.bandwidth_str is not None:
            result['BandwidthStr'] = self.bandwidth_str
        if self.bgp_asn is not None:
            result['BgpAsn'] = self.bgp_asn
        if self.bgp_cidr is not None:
            result['BgpCidr'] = self.bgp_cidr
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.cen_owner_id is not None:
            result['CenOwnerId'] = self.cen_owner_id
        result['CisRouterInfo'] = []
        if self.cis_router_info is not None:
            for k in self.cis_router_info:
                result['CisRouterInfo'].append(k.to_map() if k else None)
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.connection_type is not None:
            result['ConnectionType'] = self.connection_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.current_node is not None:
            result['CurrentNode'] = self.current_node
        if self.duration is not None:
            result['Duration'] = self.duration
        result['ErInfos'] = []
        if self.er_infos is not None:
            for k in self.er_infos:
                result['ErInfos'].append(k.to_map() if k else None)
        if self.expiration_date is not None:
            result['ExpirationDate'] = self.expiration_date
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.line_operator is not None:
            result['LineOperator'] = self.line_operator
        if self.message is not None:
            result['Message'] = self.message
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.port_type is not None:
            result['PortType'] = self.port_type
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.spec is not None:
            result['Spec'] = self.spec
        if self.status is not None:
            result['Status'] = self.status
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        result['VbrInfos'] = []
        if self.vbr_infos is not None:
            for k in self.vbr_infos:
                result['VbrInfos'].append(k.to_map() if k else None)
        if self.vcc_id is not None:
            result['VccId'] = self.vcc_id
        if self.vcc_name is not None:
            result['VccName'] = self.vcc_name
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpd_base_info is not None:
            result['VpdBaseInfo'] = self.vpd_base_info.to_map()
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessPointId') is not None:
            self.access_point_id = m.get('AccessPointId')
        self.aliyun_router_info = []
        if m.get('AliyunRouterInfo') is not None:
            for k in m.get('AliyunRouterInfo'):
                temp_model = GetVccResponseBodyContentAliyunRouterInfo()
                self.aliyun_router_info.append(temp_model.from_map(k))
        if m.get('AttachErStatus') is not None:
            self.attach_er_status = m.get('AttachErStatus')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('BandwidthStr') is not None:
            self.bandwidth_str = m.get('BandwidthStr')
        if m.get('BgpAsn') is not None:
            self.bgp_asn = m.get('BgpAsn')
        if m.get('BgpCidr') is not None:
            self.bgp_cidr = m.get('BgpCidr')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('CenOwnerId') is not None:
            self.cen_owner_id = m.get('CenOwnerId')
        self.cis_router_info = []
        if m.get('CisRouterInfo') is not None:
            for k in m.get('CisRouterInfo'):
                temp_model = GetVccResponseBodyContentCisRouterInfo()
                self.cis_router_info.append(temp_model.from_map(k))
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('ConnectionType') is not None:
            self.connection_type = m.get('ConnectionType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CurrentNode') is not None:
            self.current_node = m.get('CurrentNode')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        self.er_infos = []
        if m.get('ErInfos') is not None:
            for k in m.get('ErInfos'):
                temp_model = GetVccResponseBodyContentErInfos()
                self.er_infos.append(temp_model.from_map(k))
        if m.get('ExpirationDate') is not None:
            self.expiration_date = m.get('ExpirationDate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('LineOperator') is not None:
            self.line_operator = m.get('LineOperator')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('PortType') is not None:
            self.port_type = m.get('PortType')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = GetVccResponseBodyContentTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        self.vbr_infos = []
        if m.get('VbrInfos') is not None:
            for k in m.get('VbrInfos'):
                temp_model = GetVccResponseBodyContentVbrInfos()
                self.vbr_infos.append(temp_model.from_map(k))
        if m.get('VccId') is not None:
            self.vcc_id = m.get('VccId')
        if m.get('VccName') is not None:
            self.vcc_name = m.get('VccName')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpdBaseInfo') is not None:
            temp_model = GetVccResponseBodyContentVpdBaseInfo()
            self.vpd_base_info = temp_model.from_map(m['VpdBaseInfo'])
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class GetVccResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: GetVccResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The response parameters.
        self.content = content
        # The error message. (If the instance is in the Exception state, the exception cause is prompted.)
        self.message = message
        # Request ID of the current request
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetVccResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetVccResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetVccResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetVccResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVccGrantRuleRequest(TeaModel):
    def __init__(
        self,
        er_id: str = None,
        grant_rule_id: str = None,
        grant_tenant_id: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # Lingjun HUB Instance ID
        self.er_id = er_id
        # Authorized Resource Instance ID
        # 
        # This parameter is required.
        self.grant_rule_id = grant_rule_id
        # Authorized Tenant ID
        self.grant_tenant_id = grant_tenant_id
        # Authorized Instance ID
        self.instance_id = instance_id
        # The ID of the region. This parameter is required.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.er_id is not None:
            result['ErId'] = self.er_id
        if self.grant_rule_id is not None:
            result['GrantRuleId'] = self.grant_rule_id
        if self.grant_tenant_id is not None:
            result['GrantTenantId'] = self.grant_tenant_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')
        if m.get('GrantRuleId') is not None:
            self.grant_rule_id = m.get('GrantRuleId')
        if m.get('GrantTenantId') is not None:
            self.grant_tenant_id = m.get('GrantTenantId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetVccGrantRuleResponseBodyContent(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        er_id: str = None,
        grant_rule_id: str = None,
        grant_tenant_id: str = None,
        instance_id: str = None,
        instance_name: str = None,
        product: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        tenant_id: str = None,
        used: bool = None,
    ):
        # The time when the data address was created.
        self.create_time = create_time
        # Lingjun HUB Instance ID
        self.er_id = er_id
        # Authorized Resource ID
        self.grant_rule_id = grant_rule_id
        # Authorized Tenant ID
        self.grant_tenant_id = grant_tenant_id
        # Network Instance ID
        self.instance_id = instance_id
        # Network Instance Name
        self.instance_name = instance_name
        # Network Product Code:
        # 
        # *   **VPD**: Lingjun CIDR block
        # *   **VCC**: Lingjun Connection
        self.product = product
        # The region ID.
        self.region_id = region_id
        # Resource group instance ID
        self.resource_group_id = resource_group_id
        # The ID of the tenant.
        self.tenant_id = tenant_id
        # Whether the current authorization information has been used; optional values:
        # 
        # *   **true**: Used
        # *   **false**: Not used
        self.used = used

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.er_id is not None:
            result['ErId'] = self.er_id
        if self.grant_rule_id is not None:
            result['GrantRuleId'] = self.grant_rule_id
        if self.grant_tenant_id is not None:
            result['GrantTenantId'] = self.grant_tenant_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.product is not None:
            result['Product'] = self.product
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.used is not None:
            result['Used'] = self.used
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')
        if m.get('GrantRuleId') is not None:
            self.grant_rule_id = m.get('GrantRuleId')
        if m.get('GrantTenantId') is not None:
            self.grant_tenant_id = m.get('GrantTenantId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Used') is not None:
            self.used = m.get('Used')
        return self


class GetVccGrantRuleResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: GetVccGrantRuleResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The returned data.
        self.content = content
        # The error message. (If the instance is in the Exception state, the exception cause is prompted.)
        self.message = message
        # Request ID of the current request
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetVccGrantRuleResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetVccGrantRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetVccGrantRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetVccGrantRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVccRouteEntryRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        vcc_id: str = None,
        vcc_route_entry_id: str = None,
    ):
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Lingjun Connection ID
        # 
        # This parameter is required.
        self.vcc_id = vcc_id
        # The ID of the route entry.
        # 
        # This parameter is required.
        self.vcc_route_entry_id = vcc_route_entry_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vcc_id is not None:
            result['VccId'] = self.vcc_id
        if self.vcc_route_entry_id is not None:
            result['VccRouteEntryId'] = self.vcc_route_entry_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VccId') is not None:
            self.vcc_id = m.get('VccId')
        if m.get('VccRouteEntryId') is not None:
            self.vcc_route_entry_id = m.get('VccRouteEntryId')
        return self


class GetVccRouteEntryResponseBodyContent(TeaModel):
    def __init__(
        self,
        destination_cidr_block: str = None,
        gmt_modified: str = None,
        message: str = None,
        next_hop_id: str = None,
        next_hop_type: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        route_type: str = None,
        status: str = None,
        tenant_id: str = None,
        vcc_id: str = None,
        vcc_route_entry_id: str = None,
    ):
        # Destination CIDR Block
        self.destination_cidr_block = destination_cidr_block
        # The time when the agent was last modified.
        self.gmt_modified = gmt_modified
        # The message that is returned.
        self.message = message
        # Next Hop Instance
        self.next_hop_id = next_hop_id
        # Next Hop Type
        self.next_hop_type = next_hop_type
        # The region ID.
        self.region_id = region_id
        # Resource group instance ID
        self.resource_group_id = resource_group_id
        # Route type
        self.route_type = route_type
        # The status of the intervention entry. Valid value:
        self.status = status
        # The ID of the tenant.
        self.tenant_id = tenant_id
        # The ID of the Lingjun connection instance.
        self.vcc_id = vcc_id
        # The ID of the route entry.
        self.vcc_route_entry_id = vcc_route_entry_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.message is not None:
            result['Message'] = self.message
        if self.next_hop_id is not None:
            result['NextHopId'] = self.next_hop_id
        if self.next_hop_type is not None:
            result['NextHopType'] = self.next_hop_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.route_type is not None:
            result['RouteType'] = self.route_type
        if self.status is not None:
            result['Status'] = self.status
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.vcc_id is not None:
            result['VccId'] = self.vcc_id
        if self.vcc_route_entry_id is not None:
            result['VccRouteEntryId'] = self.vcc_route_entry_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextHopId') is not None:
            self.next_hop_id = m.get('NextHopId')
        if m.get('NextHopType') is not None:
            self.next_hop_type = m.get('NextHopType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RouteType') is not None:
            self.route_type = m.get('RouteType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('VccId') is not None:
            self.vcc_id = m.get('VccId')
        if m.get('VccRouteEntryId') is not None:
            self.vcc_route_entry_id = m.get('VccRouteEntryId')
        return self


class GetVccRouteEntryResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: GetVccRouteEntryResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The response parameters.
        self.content = content
        # The error message. (If the instance is in the Exception state, the exception cause is prompted.)
        self.message = message
        # Request ID of the current request
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetVccRouteEntryResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetVccRouteEntryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetVccRouteEntryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetVccRouteEntryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVpdRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        vpd_id: str = None,
    ):
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the VPD instance.
        # 
        # This parameter is required.
        self.vpd_id = vpd_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        return self


class GetVpdResponseBodyContentErInfos(TeaModel):
    def __init__(
        self,
        connections: int = None,
        create_time: str = None,
        description: str = None,
        er_id: str = None,
        er_name: str = None,
        gmt_modified: str = None,
        master_zone_id: str = None,
        message: str = None,
        region_id: str = None,
        route_maps: int = None,
        status: str = None,
        tenant_id: str = None,
    ):
        # The number of connections.
        self.connections = connections
        # The time when the activation code was created.
        self.create_time = create_time
        # The description of the synchronization task.
        self.description = description
        # The ID of the Elastic Router (ER) instance.
        self.er_id = er_id
        # Elastic Router (ER) Instance Name
        self.er_name = er_name
        # The time when the O\\&M task was modified.
        self.gmt_modified = gmt_modified
        # The primary zone.
        self.master_zone_id = master_zone_id
        # The returned message.
        self.message = message
        # The ID of the region to which the Elastic Router (ER) belongs.
        self.region_id = region_id
        # The number of routing policy.
        self.route_maps = route_maps
        # The task status.
        self.status = status
        # The tenant ID.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connections is not None:
            result['Connections'] = self.connections
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.er_id is not None:
            result['ErId'] = self.er_id
        if self.er_name is not None:
            result['ErName'] = self.er_name
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.master_zone_id is not None:
            result['MasterZoneId'] = self.master_zone_id
        if self.message is not None:
            result['Message'] = self.message
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.route_maps is not None:
            result['RouteMaps'] = self.route_maps
        if self.status is not None:
            result['Status'] = self.status
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Connections') is not None:
            self.connections = m.get('Connections')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')
        if m.get('ErName') is not None:
            self.er_name = m.get('ErName')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('MasterZoneId') is not None:
            self.master_zone_id = m.get('MasterZoneId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RouteMaps') is not None:
            self.route_maps = m.get('RouteMaps')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class GetVpdResponseBodyContentTags(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetVpdResponseBodyContent(TeaModel):
    def __init__(
        self,
        attach_er_status: bool = None,
        cidr: str = None,
        create_time: str = None,
        er_infos: List[GetVpdResponseBodyContentErInfos] = None,
        gmt_modified: str = None,
        message: str = None,
        nc_count: int = None,
        network_interface_count: int = None,
        private_ip_count: int = None,
        quota: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        secondary_cidr_blocks: List[str] = None,
        service_cidr: str = None,
        status: str = None,
        subnet_count: int = None,
        tags: List[GetVpdResponseBodyContentTags] = None,
        tenant_id: str = None,
        vpd_id: str = None,
        vpd_name: str = None,
    ):
        # Whether the Lingjun HUB(ER) has been bound.
        # 
        # *   **true**: ER is bound.
        # *   **false**: No ER is bound.
        self.attach_er_status = attach_er_status
        # The CIDR block.
        self.cidr = cidr
        # The time when the activation code was created.
        self.create_time = create_time
        # The information of the bound Lingjun HUB(ER).
        self.er_infos = er_infos
        # The time when the O\\&M task was modified.
        self.gmt_modified = gmt_modified
        # The error message. (If the instance is in the Exception state, the exception cause is prompted.)
        self.message = message
        # The number of NCs.
        self.nc_count = nc_count
        # Number of Lingjun network interface controller.
        self.network_interface_count = network_interface_count
        # The total number of secondary private IP addresses.
        self.private_ip_count = private_ip_count
        # The total quota information.
        self.quota = quota
        # The region ID.
        self.region_id = region_id
        # The ID of your Alibaba Cloud resource group.
        # 
        # For more information about resource groups, see [Resource groups](https://help.aliyun.com/document_detail/94475.htm?spm=a2c4g.11186623.0.0.29e15d7akXhpuu).
        self.resource_group_id = resource_group_id
        # The list of additional CIDR blocks.
        self.secondary_cidr_blocks = secondary_cidr_blocks
        # Internal Service CIDR block.
        self.service_cidr = service_cidr
        # The current state of the instance.
        # 
        # Valid value:
        # 
        # *   Not Available: Not Available.
        # *   Available: Normal: Available: Normal.
        # *   Deleting: Deleting: Deleting: Deleting.
        # *   Executing: executing: Executing: executing.
        self.status = status
        # The number of subnets.
        self.subnet_count = subnet_count
        # The tag information.
        # 
        # You can specify up to 20 tags.
        self.tags = tags
        # The tenant ID.
        self.tenant_id = tenant_id
        # The ID of the VPD instance.
        self.vpd_id = vpd_id
        # The name of the Lingjun CIDR block.
        self.vpd_name = vpd_name

    def validate(self):
        if self.er_infos:
            for k in self.er_infos:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attach_er_status is not None:
            result['AttachErStatus'] = self.attach_er_status
        if self.cidr is not None:
            result['Cidr'] = self.cidr
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        result['ErInfos'] = []
        if self.er_infos is not None:
            for k in self.er_infos:
                result['ErInfos'].append(k.to_map() if k else None)
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.message is not None:
            result['Message'] = self.message
        if self.nc_count is not None:
            result['NcCount'] = self.nc_count
        if self.network_interface_count is not None:
            result['NetworkInterfaceCount'] = self.network_interface_count
        if self.private_ip_count is not None:
            result['PrivateIpCount'] = self.private_ip_count
        if self.quota is not None:
            result['Quota'] = self.quota
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.secondary_cidr_blocks is not None:
            result['SecondaryCidrBlocks'] = self.secondary_cidr_blocks
        if self.service_cidr is not None:
            result['ServiceCidr'] = self.service_cidr
        if self.status is not None:
            result['Status'] = self.status
        if self.subnet_count is not None:
            result['SubnetCount'] = self.subnet_count
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        if self.vpd_name is not None:
            result['VpdName'] = self.vpd_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachErStatus') is not None:
            self.attach_er_status = m.get('AttachErStatus')
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        self.er_infos = []
        if m.get('ErInfos') is not None:
            for k in m.get('ErInfos'):
                temp_model = GetVpdResponseBodyContentErInfos()
                self.er_infos.append(temp_model.from_map(k))
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NcCount') is not None:
            self.nc_count = m.get('NcCount')
        if m.get('NetworkInterfaceCount') is not None:
            self.network_interface_count = m.get('NetworkInterfaceCount')
        if m.get('PrivateIpCount') is not None:
            self.private_ip_count = m.get('PrivateIpCount')
        if m.get('Quota') is not None:
            self.quota = m.get('Quota')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecondaryCidrBlocks') is not None:
            self.secondary_cidr_blocks = m.get('SecondaryCidrBlocks')
        if m.get('ServiceCidr') is not None:
            self.service_cidr = m.get('ServiceCidr')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubnetCount') is not None:
            self.subnet_count = m.get('SubnetCount')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = GetVpdResponseBodyContentTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        if m.get('VpdName') is not None:
            self.vpd_name = m.get('VpdName')
        return self


class GetVpdResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: GetVpdResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The data returned.
        self.content = content
        # The additional information that is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetVpdResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetVpdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetVpdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetVpdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVpdGrantRuleRequest(TeaModel):
    def __init__(
        self,
        er_id: str = None,
        grant_rule_id: str = None,
        grant_tenant_id: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # Lingjun HUB Instance Id
        self.er_id = er_id
        # Authorized Resource Instance ID
        # 
        # This parameter is required.
        self.grant_rule_id = grant_rule_id
        # Authorized Tenant ID
        self.grant_tenant_id = grant_tenant_id
        # Authorized Instance ID
        self.instance_id = instance_id
        # The ID of the region. This parameter is required.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.er_id is not None:
            result['ErId'] = self.er_id
        if self.grant_rule_id is not None:
            result['GrantRuleId'] = self.grant_rule_id
        if self.grant_tenant_id is not None:
            result['GrantTenantId'] = self.grant_tenant_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')
        if m.get('GrantRuleId') is not None:
            self.grant_rule_id = m.get('GrantRuleId')
        if m.get('GrantTenantId') is not None:
            self.grant_tenant_id = m.get('GrantTenantId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetVpdGrantRuleResponseBodyContent(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        er_id: str = None,
        grant_rule_id: str = None,
        grant_tenant_id: str = None,
        instance_id: str = None,
        instance_name: str = None,
        product: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        tenant_id: str = None,
        used: bool = None,
    ):
        # The time when the data address was created.
        self.create_time = create_time
        # Lingjun HUB Instance ID
        self.er_id = er_id
        # Authorized Resource ID
        self.grant_rule_id = grant_rule_id
        # Authorized Tenant ID
        self.grant_tenant_id = grant_tenant_id
        # Network Instance ID
        self.instance_id = instance_id
        # Network Instance Name
        self.instance_name = instance_name
        # Network Product Code:
        # 
        # *   **VPD**: Lingjun CIDR block
        # *   **VCC**: Lingjun Connection
        self.product = product
        # The region ID.
        self.region_id = region_id
        # Resource group instance ID
        self.resource_group_id = resource_group_id
        # The ID of the tenant.
        self.tenant_id = tenant_id
        # Whether the current authorization information has been used; default is false
        self.used = used

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.er_id is not None:
            result['ErId'] = self.er_id
        if self.grant_rule_id is not None:
            result['GrantRuleId'] = self.grant_rule_id
        if self.grant_tenant_id is not None:
            result['GrantTenantId'] = self.grant_tenant_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.product is not None:
            result['Product'] = self.product
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.used is not None:
            result['Used'] = self.used
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')
        if m.get('GrantRuleId') is not None:
            self.grant_rule_id = m.get('GrantRuleId')
        if m.get('GrantTenantId') is not None:
            self.grant_tenant_id = m.get('GrantTenantId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Used') is not None:
            self.used = m.get('Used')
        return self


class GetVpdGrantRuleResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: GetVpdGrantRuleResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The response parameters.
        self.content = content
        # The error message. (If the instance is in the Exception state, the exception cause is prompted.)
        self.message = message
        # Request ID of the current request
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetVpdGrantRuleResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetVpdGrantRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetVpdGrantRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetVpdGrantRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVpdRouteEntryRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        vpd_id: str = None,
        vpd_route_entry_id: str = None,
    ):
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Lingjun CIDR block instance ID
        # 
        # This parameter is required.
        self.vpd_id = vpd_id
        # The ID of the route entry instance.
        # 
        # This parameter is required.
        self.vpd_route_entry_id = vpd_route_entry_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        if self.vpd_route_entry_id is not None:
            result['VpdRouteEntryId'] = self.vpd_route_entry_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        if m.get('VpdRouteEntryId') is not None:
            self.vpd_route_entry_id = m.get('VpdRouteEntryId')
        return self


class GetVpdRouteEntryResponseBodyContent(TeaModel):
    def __init__(
        self,
        destination_cidr_block: str = None,
        gmt_modified: str = None,
        next_hop_id: str = None,
        next_hop_type: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        route_type: str = None,
        status: str = None,
        tenant_id: str = None,
        vpd_id: str = None,
        vpd_route_entry_id: str = None,
    ):
        # Destination CIDR block
        self.destination_cidr_block = destination_cidr_block
        # The time when the agent was last modified.
        self.gmt_modified = gmt_modified
        # Next Hop Instance
        self.next_hop_id = next_hop_id
        # Next Hop Instance Type
        self.next_hop_type = next_hop_type
        # The region ID.
        self.region_id = region_id
        # Resource group instance ID
        self.resource_group_id = resource_group_id
        # Route type
        self.route_type = route_type
        # The status of the intervention entry. Valid value:
        self.status = status
        # The ID of the tenant.
        self.tenant_id = tenant_id
        # Lingjun CIDR block instance ID
        self.vpd_id = vpd_id
        # Lingjun CIDR block route entry ID
        self.vpd_route_entry_id = vpd_route_entry_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.next_hop_id is not None:
            result['NextHopId'] = self.next_hop_id
        if self.next_hop_type is not None:
            result['NextHopType'] = self.next_hop_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.route_type is not None:
            result['RouteType'] = self.route_type
        if self.status is not None:
            result['Status'] = self.status
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        if self.vpd_route_entry_id is not None:
            result['VpdRouteEntryId'] = self.vpd_route_entry_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('NextHopId') is not None:
            self.next_hop_id = m.get('NextHopId')
        if m.get('NextHopType') is not None:
            self.next_hop_type = m.get('NextHopType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RouteType') is not None:
            self.route_type = m.get('RouteType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        if m.get('VpdRouteEntryId') is not None:
            self.vpd_route_entry_id = m.get('VpdRouteEntryId')
        return self


class GetVpdRouteEntryResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: GetVpdRouteEntryResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The response parameters.
        self.content = content
        # The error message. (If the instance is in the Exception state, the exception cause is prompted.)
        self.message = message
        # Request ID of the current request
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetVpdRouteEntryResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetVpdRouteEntryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetVpdRouteEntryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetVpdRouteEntryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitializeVccRequest(TeaModel):
    def __init__(
        self,
        resource_group_id: str = None,
    ):
        # The resource group ID.
        # 
        # For more information about resource groups, see [Resource groups](https://help.aliyun.com/document_detail/94475.htm?spm=a2c4g.11186623.0.0.29e15d7akXhpuu).
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class InitializeVccResponseBodyContent(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        role_name: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # Linked Role of Lingjun Connection Instance (AliyunServiceRoleForEfloVcc)
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class InitializeVccResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: InitializeVccResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The response parameters.
        self.content = content
        # The error message. (If the instance is in the Exception state, the exception cause is prompted.)
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = InitializeVccResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class InitializeVccResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InitializeVccResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = InitializeVccResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListElasticNetworkInterfacesRequestTag(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListElasticNetworkInterfacesRequest(TeaModel):
    def __init__(
        self,
        elastic_network_interface_id: str = None,
        ip: str = None,
        network_type: str = None,
        node_id: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        status: str = None,
        tag: List[ListElasticNetworkInterfacesRequestTag] = None,
        type: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # Lingjun Elastic Network Interface ID
        self.elastic_network_interface_id = elastic_network_interface_id
        # The IP address of the BE cluster.
        self.ip = ip
        # The network type.
        # 
        # Valid value:
        # 
        # *   Tenant: Tenant.
        # *   VPC
        self.network_type = network_type
        # The ID of the node.
        self.node_id = node_id
        # The page number of the page to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: 20.
        self.page_size = page_size
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        # The status of the enterprise-level snapshot policy.
        # 
        # Valid value:
        # 
        # *   Create Failed: the creation failure.
        # *   Delete Failed: the that failed to be deleted.
        # *   Executing
        # *   Available: The template is available.
        # *   Deleting
        self.status = status
        self.tag = tag
        # The type of the variable.
        # 
        # Valid value:
        # 
        # *   CUSTOM: custom type.
        # *   DEFAULT: system type.
        self.type = type
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The ID of the virtual private cloud (VPC).
        self.vpc_id = vpc_id
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.elastic_network_interface_id is not None:
            result['ElasticNetworkInterfaceId'] = self.elastic_network_interface_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.status is not None:
            result['Status'] = self.status
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
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
        if m.get('ElasticNetworkInterfaceId') is not None:
            self.elastic_network_interface_id = m.get('ElasticNetworkInterfaceId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListElasticNetworkInterfacesRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListElasticNetworkInterfacesResponseBodyContentDataTags(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListElasticNetworkInterfacesResponseBodyContentData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        elastic_network_interface_id: str = None,
        gateway: str = None,
        gmt_modified: str = None,
        ip: str = None,
        mac: str = None,
        mask: str = None,
        message: str = None,
        node_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        security_group_id: str = None,
        status: str = None,
        tags: List[ListElasticNetworkInterfacesResponseBodyContentDataTags] = None,
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
        # vswitch gateway address
        self.gateway = gateway
        # The time when the agent was last modified.
        self.gmt_modified = gmt_modified
        # The IP address of the BE cluster.
        self.ip = ip
        # mac address
        self.mac = mac
        # vswitch mask bits
        self.mask = mask
        # The error message.
        self.message = message
        # The ID of the node.
        self.node_id = node_id
        # The region ID.
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        # The ID of the security group.
        self.security_group_id = security_group_id
        # The status of the intervention entry. Valid value:
        self.status = status
        self.tags = tags
        # network interface controller type, the default type DEFAULT cannot be manually released
        # 
        # Valid value:
        # 
        # *   CUSTOM: custom type.
        # *   DEFAULT: system type.
        self.type = type
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id
        # The ID of the virtual private cloud (VPC).
        self.vpc_id = vpc_id
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.elastic_network_interface_id is not None:
            result['ElasticNetworkInterfaceId'] = self.elastic_network_interface_id
        if self.gateway is not None:
            result['Gateway'] = self.gateway
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.mask is not None:
            result['Mask'] = self.mask
        if self.message is not None:
            result['Message'] = self.message
        if self.node_id is not None:
            result['NodeId'] = self.node_id
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
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
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
        if m.get('Gateway') is not None:
            self.gateway = m.get('Gateway')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('Mask') is not None:
            self.mask = m.get('Mask')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
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
            for k in m.get('Tags'):
                temp_model = ListElasticNetworkInterfacesResponseBodyContentDataTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListElasticNetworkInterfacesResponseBodyContent(TeaModel):
    def __init__(
        self,
        data: List[ListElasticNetworkInterfacesResponseBodyContentData] = None,
        total: int = None,
    ):
        # lingjun Elastic Network Interface information list
        self.data = data
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListElasticNetworkInterfacesResponseBodyContentData()
                self.data.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListElasticNetworkInterfacesResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: ListElasticNetworkInterfacesResponseBodyContent = None,
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
        # Request ID of the current request
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListElasticNetworkInterfacesResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListElasticNetworkInterfacesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListElasticNetworkInterfacesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListElasticNetworkInterfacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListErAttachmentsRequest(TeaModel):
    def __init__(
        self,
        auto_receive_all_route: bool = None,
        enable_page: bool = None,
        er_attachment_id: str = None,
        er_attachment_name: str = None,
        er_id: str = None,
        instance_id: str = None,
        instance_type: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_tenant_id: str = None,
        status: str = None,
    ):
        # Whether to automatically receive all routes from all instances under this Lingjun HUB. Valid values:
        # 
        # *   **true**: received automatically.
        # *   **false**: Not received.
        self.auto_receive_all_route = auto_receive_all_route
        # Specifies whether to enable paged query. Valid values:
        # 
        # *   **true**: enables paged query.
        # *   **false**: Paged query is not enabled.
        self.enable_page = enable_page
        # The ID of the network instance connection
        self.er_attachment_id = er_attachment_id
        # The name of the network instance connection.
        self.er_attachment_name = er_attachment_name
        # The ID of the Lingjun HUB instance.
        # 
        # This parameter is required.
        self.er_id = er_id
        # The ID of the network instance. Valid values: **VPD** and **VCC**.
        # 
        # For more information, see [What is Lingjun?](https://help.aliyun.com/document_detail/444430.html)
        # 
        # You can query **Lingjun CIDR blocks** and **Lingjun connections** by [ListVpds](https://help.aliyun.com/document_detail/2331077.html) and [ListVccs](https://help.aliyun.com/document_detail/2399526.html?) respectively.
        self.instance_id = instance_id
        # The mitigation plan of the instance. Valid values:
        # 
        # *   **VPD**: indicates the Lingjun CIDR block.
        # *   **VCC**: indicates a Lingjun connection.
        self.instance_type = instance_type
        # The page number to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 20.
        self.page_size = page_size
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Resource group instance ID
        self.resource_group_id = resource_group_id
        # The ID of the tenant to which the instance belongs.
        self.resource_tenant_id = resource_tenant_id
        # The status of the CLB instance. Valid values:
        # 
        # *   **Available**: Normal.
        # *   **Not Available**: Not available.
        # *   **Executing**: The task is being executed.
        # *   **Deleting**: The account is being deleted
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_receive_all_route is not None:
            result['AutoReceiveAllRoute'] = self.auto_receive_all_route
        if self.enable_page is not None:
            result['EnablePage'] = self.enable_page
        if self.er_attachment_id is not None:
            result['ErAttachmentId'] = self.er_attachment_id
        if self.er_attachment_name is not None:
            result['ErAttachmentName'] = self.er_attachment_name
        if self.er_id is not None:
            result['ErId'] = self.er_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_tenant_id is not None:
            result['ResourceTenantId'] = self.resource_tenant_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoReceiveAllRoute') is not None:
            self.auto_receive_all_route = m.get('AutoReceiveAllRoute')
        if m.get('EnablePage') is not None:
            self.enable_page = m.get('EnablePage')
        if m.get('ErAttachmentId') is not None:
            self.er_attachment_id = m.get('ErAttachmentId')
        if m.get('ErAttachmentName') is not None:
            self.er_attachment_name = m.get('ErAttachmentName')
        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceTenantId') is not None:
            self.resource_tenant_id = m.get('ResourceTenantId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListErAttachmentsResponseBodyContentData(TeaModel):
    def __init__(
        self,
        across: bool = None,
        auto_receive_all_route: bool = None,
        create_time: str = None,
        er_attachment_id: str = None,
        er_attachment_name: str = None,
        er_id: str = None,
        gmt_modified: str = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_type: str = None,
        message: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_tenant_id: str = None,
        status: str = None,
        tenant_id: str = None,
    ):
        # Whether to cross accounts. Valid values:
        # 
        # *   **true**: The network instance is a cross-account resource.
        # *   **false**: The current network instance is a resource of the current account.
        self.across = across
        # Whether to automatically receive all routes from all instances under this Lingjun HUB. Valid values:
        # 
        # *   **true**: received automatically.
        # *   **false**: Not received.
        self.auto_receive_all_route = auto_receive_all_route
        # The time when the activation code was created.
        self.create_time = create_time
        # The ID of the Lingjun HUB network instance.
        self.er_attachment_id = er_attachment_id
        # The name of the Lingjun HUB network instance.
        self.er_attachment_name = er_attachment_name
        # The ID of the Lingjun HUB instance.
        self.er_id = er_id
        # The time when the O\\&M task was modified.
        self.gmt_modified = gmt_modified
        # The ID of the network instance. Valid values: **VPD** and **VCC**.
        # 
        # For more information, see [What is Lingjun?](https://help.aliyun.com/document_detail/444430.html)
        # 
        # You can query **Lingjun CIDR blocks** and **Lingjun connections** by [ListVpds](https://help.aliyun.com/document_detail/2331077.html) and [ListVccs](https://help.aliyun.com/document_detail/2399526.html) respectively.
        self.instance_id = instance_id
        # The instance name.
        self.instance_name = instance_name
        # The database type. Valid values:
        # 
        # *   **VPD**: indicates the Lingjun CIDR block.
        # *   **VCC**: indicates a Lingjun connection.
        self.instance_type = instance_type
        # The returned message.
        self.message = message
        # Lingjun HUB region information.
        self.region_id = region_id
        # Resource group instance ID
        self.resource_group_id = resource_group_id
        # The ID of the tenant to which the resource belongs.
        self.resource_tenant_id = resource_tenant_id
        # The status of the cache reserve instance. Valid values:
        # 
        # *   **Available**: Normal.
        # *   **Not Available**: Not available.
        # *   **Executing**: The task is being executed.
        # *   **Deleting**: The account is being deleted
        self.status = status
        # The tenant ID.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.across is not None:
            result['Across'] = self.across
        if self.auto_receive_all_route is not None:
            result['AutoReceiveAllRoute'] = self.auto_receive_all_route
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.er_attachment_id is not None:
            result['ErAttachmentId'] = self.er_attachment_id
        if self.er_attachment_name is not None:
            result['ErAttachmentName'] = self.er_attachment_name
        if self.er_id is not None:
            result['ErId'] = self.er_id
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.message is not None:
            result['Message'] = self.message
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_tenant_id is not None:
            result['ResourceTenantId'] = self.resource_tenant_id
        if self.status is not None:
            result['Status'] = self.status
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Across') is not None:
            self.across = m.get('Across')
        if m.get('AutoReceiveAllRoute') is not None:
            self.auto_receive_all_route = m.get('AutoReceiveAllRoute')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ErAttachmentId') is not None:
            self.er_attachment_id = m.get('ErAttachmentId')
        if m.get('ErAttachmentName') is not None:
            self.er_attachment_name = m.get('ErAttachmentName')
        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceTenantId') is not None:
            self.resource_tenant_id = m.get('ResourceTenantId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class ListErAttachmentsResponseBodyContent(TeaModel):
    def __init__(
        self,
        data: List[ListErAttachmentsResponseBodyContentData] = None,
        total: int = None,
    ):
        # The list of Lingjun HUB network instances.
        self.data = data
        # The total number of entries that are returned.
        self.total = total

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListErAttachmentsResponseBodyContentData()
                self.data.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListErAttachmentsResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: ListErAttachmentsResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The data returned.
        self.content = content
        # The error message. (If the instance is in the Exception state, the exception cause is displayed.)
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListErAttachmentsResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListErAttachmentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListErAttachmentsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListErAttachmentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListErRouteEntriesRequest(TeaModel):
    def __init__(
        self,
        destination_cidr_block: str = None,
        enable_page: bool = None,
        er_id: str = None,
        ignore_detailed_route_entry: bool = None,
        instance_id: str = None,
        next_hop_id: str = None,
        next_hop_type: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        route_type: str = None,
        status: str = None,
    ):
        # Destination CIDR Block
        self.destination_cidr_block = destination_cidr_block
        # Specifies whether to enable pagination query.
        self.enable_page = enable_page
        # Lingjun HUB ID
        # 
        # This parameter is required.
        self.er_id = er_id
        # Filter 32 detailed CIDR blocks. Default value: true
        self.ignore_detailed_route_entry = ignore_detailed_route_entry
        # Network Instance ID
        self.instance_id = instance_id
        # Next Hop Instance
        self.next_hop_id = next_hop_id
        # Next Hop Instance Type
        self.next_hop_type = next_hop_type
        # The page number of the page to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 20.
        self.page_size = page_size
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Resource group instance ID
        self.resource_group_id = resource_group_id
        # Route type
        self.route_type = route_type
        # The status of the enterprise-level snapshot policy.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        if self.enable_page is not None:
            result['EnablePage'] = self.enable_page
        if self.er_id is not None:
            result['ErId'] = self.er_id
        if self.ignore_detailed_route_entry is not None:
            result['IgnoreDetailedRouteEntry'] = self.ignore_detailed_route_entry
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.next_hop_id is not None:
            result['NextHopId'] = self.next_hop_id
        if self.next_hop_type is not None:
            result['NextHopType'] = self.next_hop_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.route_type is not None:
            result['RouteType'] = self.route_type
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        if m.get('EnablePage') is not None:
            self.enable_page = m.get('EnablePage')
        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')
        if m.get('IgnoreDetailedRouteEntry') is not None:
            self.ignore_detailed_route_entry = m.get('IgnoreDetailedRouteEntry')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NextHopId') is not None:
            self.next_hop_id = m.get('NextHopId')
        if m.get('NextHopType') is not None:
            self.next_hop_type = m.get('NextHopType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RouteType') is not None:
            self.route_type = m.get('RouteType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListErRouteEntriesResponseBodyContentData(TeaModel):
    def __init__(
        self,
        destination_cidr_block: str = None,
        er_id: str = None,
        er_route_entry_id: str = None,
        gmt_modified: str = None,
        next_hop_id: str = None,
        next_hop_type: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_tenant_id: str = None,
        route_type: str = None,
        status: str = None,
        tenant_id: str = None,
    ):
        # Destination CIDR Block
        self.destination_cidr_block = destination_cidr_block
        # Lingjun HUB Instance ID
        self.er_id = er_id
        # The ID of the route entry.
        self.er_route_entry_id = er_route_entry_id
        # The time when the cluster was updated.
        self.gmt_modified = gmt_modified
        # Next Hop Instance
        self.next_hop_id = next_hop_id
        # Next Hop Instance Type
        self.next_hop_type = next_hop_type
        # The region ID.
        self.region_id = region_id
        # Resource group instance ID
        self.resource_group_id = resource_group_id
        # The ID of the tenant to which the resource belongs.
        self.resource_tenant_id = resource_tenant_id
        # Route type
        self.route_type = route_type
        # The task status. Valid values:
        # 
        # *   Synchronizing
        # *   Available
        self.status = status
        # The ID of the tenant.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        if self.er_id is not None:
            result['ErId'] = self.er_id
        if self.er_route_entry_id is not None:
            result['ErRouteEntryId'] = self.er_route_entry_id
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.next_hop_id is not None:
            result['NextHopId'] = self.next_hop_id
        if self.next_hop_type is not None:
            result['NextHopType'] = self.next_hop_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_tenant_id is not None:
            result['ResourceTenantId'] = self.resource_tenant_id
        if self.route_type is not None:
            result['RouteType'] = self.route_type
        if self.status is not None:
            result['Status'] = self.status
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')
        if m.get('ErRouteEntryId') is not None:
            self.er_route_entry_id = m.get('ErRouteEntryId')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('NextHopId') is not None:
            self.next_hop_id = m.get('NextHopId')
        if m.get('NextHopType') is not None:
            self.next_hop_type = m.get('NextHopType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceTenantId') is not None:
            self.resource_tenant_id = m.get('ResourceTenantId')
        if m.get('RouteType') is not None:
            self.route_type = m.get('RouteType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class ListErRouteEntriesResponseBodyContent(TeaModel):
    def __init__(
        self,
        data: List[ListErRouteEntriesResponseBodyContentData] = None,
        total: int = None,
    ):
        # Lingjun HUB Route Entry Information List
        self.data = data
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListErRouteEntriesResponseBodyContentData()
                self.data.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListErRouteEntriesResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: ListErRouteEntriesResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The response parameters.
        self.content = content
        # The error message. (If the instance is in the Exception state, the exception cause is prompted.)
        self.message = message
        # Request ID of the current request
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListErRouteEntriesResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListErRouteEntriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListErRouteEntriesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListErRouteEntriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListErRouteMapsRequest(TeaModel):
    def __init__(
        self,
        destination_cidr_block: str = None,
        enable_page: bool = None,
        er_id: str = None,
        er_route_map_id: str = None,
        er_route_map_num: int = None,
        page_number: int = None,
        page_size: int = None,
        reception_instance_id: str = None,
        reception_instance_name: str = None,
        reception_instance_type: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        route_map_action: str = None,
        transmission_instance_id: str = None,
        transmission_instance_name: str = None,
        transmission_instance_type: str = None,
    ):
        # Destination CIDR Block
        self.destination_cidr_block = destination_cidr_block
        # Specifies whether to enable paged query.
        self.enable_page = enable_page
        # Elastic Router ID
        # 
        # This parameter is required.
        self.er_id = er_id
        # routing policy ID
        self.er_route_map_id = er_route_map_id
        # Policy number (default for automatic creation is 3000; The value range of the policy number manually created by the user is 1001-2000)
        self.er_route_map_num = er_route_map_num
        # The page number of the page to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: 10.
        self.page_size = page_size
        # Receive Instance ID
        self.reception_instance_id = reception_instance_id
        # Receive Instance Name
        self.reception_instance_name = reception_instance_name
        # The type of the received instance. Optional values:
        # 
        # *   **VPD**: Lingjun network segment.
        # *   **VCC**: Lingjun Connection.
        self.reception_instance_type = reception_instance_type
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Resource group instance ID
        self.resource_group_id = resource_group_id
        # Policy behavior; optional values:
        # 
        # *   **permit**: Allow
        # *   **deny**: Rejected
        self.route_map_action = route_map_action
        # Release Instance ID
        self.transmission_instance_id = transmission_instance_id
        # Release Instance Name
        self.transmission_instance_name = transmission_instance_name
        # The type of the published instance. Optional values:
        # 
        # *   **VPD**: Lingjun network segment.
        # *   **VCC**: Lingjun Connection.
        self.transmission_instance_type = transmission_instance_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        if self.enable_page is not None:
            result['EnablePage'] = self.enable_page
        if self.er_id is not None:
            result['ErId'] = self.er_id
        if self.er_route_map_id is not None:
            result['ErRouteMapId'] = self.er_route_map_id
        if self.er_route_map_num is not None:
            result['ErRouteMapNum'] = self.er_route_map_num
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.reception_instance_id is not None:
            result['ReceptionInstanceId'] = self.reception_instance_id
        if self.reception_instance_name is not None:
            result['ReceptionInstanceName'] = self.reception_instance_name
        if self.reception_instance_type is not None:
            result['ReceptionInstanceType'] = self.reception_instance_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.route_map_action is not None:
            result['RouteMapAction'] = self.route_map_action
        if self.transmission_instance_id is not None:
            result['TransmissionInstanceId'] = self.transmission_instance_id
        if self.transmission_instance_name is not None:
            result['TransmissionInstanceName'] = self.transmission_instance_name
        if self.transmission_instance_type is not None:
            result['TransmissionInstanceType'] = self.transmission_instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        if m.get('EnablePage') is not None:
            self.enable_page = m.get('EnablePage')
        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')
        if m.get('ErRouteMapId') is not None:
            self.er_route_map_id = m.get('ErRouteMapId')
        if m.get('ErRouteMapNum') is not None:
            self.er_route_map_num = m.get('ErRouteMapNum')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ReceptionInstanceId') is not None:
            self.reception_instance_id = m.get('ReceptionInstanceId')
        if m.get('ReceptionInstanceName') is not None:
            self.reception_instance_name = m.get('ReceptionInstanceName')
        if m.get('ReceptionInstanceType') is not None:
            self.reception_instance_type = m.get('ReceptionInstanceType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RouteMapAction') is not None:
            self.route_map_action = m.get('RouteMapAction')
        if m.get('TransmissionInstanceId') is not None:
            self.transmission_instance_id = m.get('TransmissionInstanceId')
        if m.get('TransmissionInstanceName') is not None:
            self.transmission_instance_name = m.get('TransmissionInstanceName')
        if m.get('TransmissionInstanceType') is not None:
            self.transmission_instance_type = m.get('TransmissionInstanceType')
        return self


class ListErRouteMapsResponseBodyContentData(TeaModel):
    def __init__(
        self,
        action: str = None,
        create_time: str = None,
        description: str = None,
        destination_cidr_block: str = None,
        er_id: str = None,
        er_route_map_id: str = None,
        gmt_modified: str = None,
        message: str = None,
        reception_instance_id: str = None,
        reception_instance_name: str = None,
        reception_instance_owner: str = None,
        reception_instance_type: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        route_map_num: int = None,
        status: str = None,
        tenant_id: str = None,
        transmission_instance_id: str = None,
        transmission_instance_name: str = None,
        transmission_instance_owner: str = None,
        transmission_instance_type: str = None,
    ):
        # Policy behavior; optional values:
        # 
        # *   **permit**: Allow
        # *   **deny**: Prohibited
        self.action = action
        # The time when the data address was created.
        self.create_time = create_time
        # Policy description
        self.description = description
        # Destination CIDR Block
        self.destination_cidr_block = destination_cidr_block
        # Lingjun HUB ID
        self.er_id = er_id
        # routing policy ID
        self.er_route_map_id = er_route_map_id
        # The time when the agent was last modified.
        self.gmt_modified = gmt_modified
        # The message that is returned.
        self.message = message
        # Receive Instance ID
        self.reception_instance_id = reception_instance_id
        # Receive Instance Name
        self.reception_instance_name = reception_instance_name
        # The tenant to which the receiving instance belongs
        self.reception_instance_owner = reception_instance_owner
        # The type of the received instance. Possible values:
        # 
        # *   **VPD**: Lingjun network segment.
        # *   **VCC**: Lingjun Connection.
        self.reception_instance_type = reception_instance_type
        # The region ID.
        self.region_id = region_id
        # Resource group instance ID
        self.resource_group_id = resource_group_id
        # The ID of the policy.
        # 
        # A smaller sequence number indicates a lower priority. When a route is matched, a policy with a higher priority is preferentially matched.
        # 
        # **Valid values: 1001 to 2000**\
        self.route_map_num = route_map_num
        # Status The status of the instance. Valid values:
        # 
        # *   **Available**\
        # *   **Not Available**: Unavailable
        # *   **Executing**: Executing
        # *   **Deleting**: The node is being deleted.
        self.status = status
        # The ID of the tenant.
        self.tenant_id = tenant_id
        # Release Instance ID
        self.transmission_instance_id = transmission_instance_id
        # Release Instance Name
        self.transmission_instance_name = transmission_instance_name
        # The tenant to which the published instance belongs
        self.transmission_instance_owner = transmission_instance_owner
        # The type of the published instance. Possible values:
        # 
        # *   **VPD**: Lingjun network segment.
        # *   **VCC**: Lingjun Connection.
        self.transmission_instance_type = transmission_instance_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        if self.er_id is not None:
            result['ErId'] = self.er_id
        if self.er_route_map_id is not None:
            result['ErRouteMapId'] = self.er_route_map_id
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.message is not None:
            result['Message'] = self.message
        if self.reception_instance_id is not None:
            result['ReceptionInstanceId'] = self.reception_instance_id
        if self.reception_instance_name is not None:
            result['ReceptionInstanceName'] = self.reception_instance_name
        if self.reception_instance_owner is not None:
            result['ReceptionInstanceOwner'] = self.reception_instance_owner
        if self.reception_instance_type is not None:
            result['ReceptionInstanceType'] = self.reception_instance_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.route_map_num is not None:
            result['RouteMapNum'] = self.route_map_num
        if self.status is not None:
            result['Status'] = self.status
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.transmission_instance_id is not None:
            result['TransmissionInstanceId'] = self.transmission_instance_id
        if self.transmission_instance_name is not None:
            result['TransmissionInstanceName'] = self.transmission_instance_name
        if self.transmission_instance_owner is not None:
            result['TransmissionInstanceOwner'] = self.transmission_instance_owner
        if self.transmission_instance_type is not None:
            result['TransmissionInstanceType'] = self.transmission_instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')
        if m.get('ErRouteMapId') is not None:
            self.er_route_map_id = m.get('ErRouteMapId')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ReceptionInstanceId') is not None:
            self.reception_instance_id = m.get('ReceptionInstanceId')
        if m.get('ReceptionInstanceName') is not None:
            self.reception_instance_name = m.get('ReceptionInstanceName')
        if m.get('ReceptionInstanceOwner') is not None:
            self.reception_instance_owner = m.get('ReceptionInstanceOwner')
        if m.get('ReceptionInstanceType') is not None:
            self.reception_instance_type = m.get('ReceptionInstanceType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RouteMapNum') is not None:
            self.route_map_num = m.get('RouteMapNum')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('TransmissionInstanceId') is not None:
            self.transmission_instance_id = m.get('TransmissionInstanceId')
        if m.get('TransmissionInstanceName') is not None:
            self.transmission_instance_name = m.get('TransmissionInstanceName')
        if m.get('TransmissionInstanceOwner') is not None:
            self.transmission_instance_owner = m.get('TransmissionInstanceOwner')
        if m.get('TransmissionInstanceType') is not None:
            self.transmission_instance_type = m.get('TransmissionInstanceType')
        return self


class ListErRouteMapsResponseBodyContent(TeaModel):
    def __init__(
        self,
        data: List[ListErRouteMapsResponseBodyContentData] = None,
        total: int = None,
    ):
        # routing policy information list
        self.data = data
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListErRouteMapsResponseBodyContentData()
                self.data.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListErRouteMapsResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: ListErRouteMapsResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The response parameters.
        self.content = content
        # The error message. (If the instance is in the Exception state, the exception cause is prompted.)
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListErRouteMapsResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListErRouteMapsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListErRouteMapsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListErRouteMapsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListErsRequestTag(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListErsRequest(TeaModel):
    def __init__(
        self,
        enable_page: bool = None,
        er_id: str = None,
        er_name: str = None,
        instance_id: str = None,
        instance_type: str = None,
        master_zone_id: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        tag: List[ListErsRequestTag] = None,
    ):
        # Specifies whether to enable paged query. Valid values:
        # 
        # *   true: enables paged query.
        # *   false: Paged query is disabled.
        self.enable_page = enable_page
        # The ID of the Lingjun HUB instance.
        self.er_id = er_id
        # Lingjun HUB name.
        self.er_name = er_name
        # The ID of the network instance.
        self.instance_id = instance_id
        # The type of the attached network instance. Valid values:
        # 
        # *   **VPD**\
        # *   **VCC**\
        self.instance_type = instance_type
        # The primary zone.
        self.master_zone_id = master_zone_id
        # The page number to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: 10.
        self.page_size = page_size
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Resource group instance ID
        self.resource_group_id = resource_group_id
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_page is not None:
            result['EnablePage'] = self.enable_page
        if self.er_id is not None:
            result['ErId'] = self.er_id
        if self.er_name is not None:
            result['ErName'] = self.er_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.master_zone_id is not None:
            result['MasterZoneId'] = self.master_zone_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnablePage') is not None:
            self.enable_page = m.get('EnablePage')
        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')
        if m.get('ErName') is not None:
            self.er_name = m.get('ErName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('MasterZoneId') is not None:
            self.master_zone_id = m.get('MasterZoneId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListErsRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListErsResponseBodyContentDataTags(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListErsResponseBodyContentData(TeaModel):
    def __init__(
        self,
        connections: int = None,
        create_time: str = None,
        description: str = None,
        er_id: str = None,
        er_name: str = None,
        gmt_modified: str = None,
        master_zone_id: str = None,
        message: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        route_maps: int = None,
        status: str = None,
        tags: List[ListErsResponseBodyContentDataTags] = None,
        tenant_id: str = None,
    ):
        # The number of connections to the Lingjun HUB network instance.
        self.connections = connections
        # The time when the activation code was created.
        self.create_time = create_time
        # The description of the synchronization task.
        self.description = description
        # The ID of the Lingjun HUB instance.
        self.er_id = er_id
        # The name of the Lingjun HUB instance.
        self.er_name = er_name
        # The time when the O\\&M task was modified.
        self.gmt_modified = gmt_modified
        # The primary zone.
        self.master_zone_id = master_zone_id
        # The returned message.
        self.message = message
        # The region ID.
        self.region_id = region_id
        # Resource group instance ID
        self.resource_group_id = resource_group_id
        # Number of Lingjun HUB routing policy.
        self.route_maps = route_maps
        # The task status.
        self.status = status
        self.tags = tags
        # The tenant ID.
        self.tenant_id = tenant_id

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connections is not None:
            result['Connections'] = self.connections
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.er_id is not None:
            result['ErId'] = self.er_id
        if self.er_name is not None:
            result['ErName'] = self.er_name
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.master_zone_id is not None:
            result['MasterZoneId'] = self.master_zone_id
        if self.message is not None:
            result['Message'] = self.message
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.route_maps is not None:
            result['RouteMaps'] = self.route_maps
        if self.status is not None:
            result['Status'] = self.status
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Connections') is not None:
            self.connections = m.get('Connections')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')
        if m.get('ErName') is not None:
            self.er_name = m.get('ErName')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('MasterZoneId') is not None:
            self.master_zone_id = m.get('MasterZoneId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RouteMaps') is not None:
            self.route_maps = m.get('RouteMaps')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListErsResponseBodyContentDataTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class ListErsResponseBodyContent(TeaModel):
    def __init__(
        self,
        data: List[ListErsResponseBodyContentData] = None,
        total: int = None,
    ):
        # lingjun hub information list.
        self.data = data
        # The total number of entries.
        self.total = total

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListErsResponseBodyContentData()
                self.data.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListErsResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: ListErsResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The response data.
        self.content = content
        # The error message. (If the instance is in the Exception state, the exception cause is displayed.)
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListErsResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListErsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListErsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListErsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstancesByNcdRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_type: str = None,
        max_ncd: int = None,
        region_id: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The parameter that specifies the instance type.
        # 
        # Valid value:
        # 
        # *   node: Lingjun node.
        # *   lni: lingjun network interface controller.
        # 
        # This parameter is required.
        self.instance_type = instance_type
        # Maximum network communication distance
        # 
        # This parameter is required.
        self.max_ncd = max_ncd
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.max_ncd is not None:
            result['MaxNcd'] = self.max_ncd
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('MaxNcd') is not None:
            self.max_ncd = m.get('MaxNcd')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListInstancesByNcdResponseBodyContentInstanceInfos(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        ncd: int = None,
    ):
        # The instance ID.
        self.instance_id = instance_id
        # network communication distance
        self.ncd = ncd

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ncd is not None:
            result['Ncd'] = self.ncd
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Ncd') is not None:
            self.ncd = m.get('Ncd')
        return self


class ListInstancesByNcdResponseBodyContent(TeaModel):
    def __init__(
        self,
        instance_infos: List[ListInstancesByNcdResponseBodyContentInstanceInfos] = None,
        instance_type: str = None,
        max_ncd: int = None,
        source_instance_id: str = None,
    ):
        # A collection of instances whose network communication distance from the source instance ID does not exceed maxNcd
        self.instance_infos = instance_infos
        # Instance Type
        # 
        # Valid value:
        # 
        # *   node: Lingjun node.
        # *   lni: lingjun network interface controller.
        self.instance_type = instance_type
        # Maximum communication distance between nodes
        self.max_ncd = max_ncd
        # The ID of the source instance.
        self.source_instance_id = source_instance_id

    def validate(self):
        if self.instance_infos:
            for k in self.instance_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceInfos'] = []
        if self.instance_infos is not None:
            for k in self.instance_infos:
                result['InstanceInfos'].append(k.to_map() if k else None)
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.max_ncd is not None:
            result['MaxNcd'] = self.max_ncd
        if self.source_instance_id is not None:
            result['SourceInstanceId'] = self.source_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_infos = []
        if m.get('InstanceInfos') is not None:
            for k in m.get('InstanceInfos'):
                temp_model = ListInstancesByNcdResponseBodyContentInstanceInfos()
                self.instance_infos.append(temp_model.from_map(k))
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('MaxNcd') is not None:
            self.max_ncd = m.get('MaxNcd')
        if m.get('SourceInstanceId') is not None:
            self.source_instance_id = m.get('SourceInstanceId')
        return self


class ListInstancesByNcdResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: ListInstancesByNcdResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The response parameters.
        self.content = content
        # The returned message.
        self.message = message
        # Request ID of the current request
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListInstancesByNcdResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListInstancesByNcdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInstancesByNcdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListInstancesByNcdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLeniPrivateIpAddressesRequest(TeaModel):
    def __init__(
        self,
        elastic_network_interface_id: str = None,
        ip_name: str = None,
        page_number: int = None,
        page_size: int = None,
        private_ip_address: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        status: str = None,
    ):
        # Lingjun Elastic Network Interface ID.
        self.elastic_network_interface_id = elastic_network_interface_id
        # Lingjun Elastic Network Interface secondary private IP unique identifier.
        self.ip_name = ip_name
        # The page number returned.
        self.page_number = page_number
        # The number of entries to return on each page.
        self.page_size = page_size
        # Lingjun Elastic Network Interface secondary private IP.
        self.private_ip_address = private_ip_address
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        # The status of the image build command risk.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.elastic_network_interface_id is not None:
            result['ElasticNetworkInterfaceId'] = self.elastic_network_interface_id
        if self.ip_name is not None:
            result['IpName'] = self.ip_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ElasticNetworkInterfaceId') is not None:
            self.elastic_network_interface_id = m.get('ElasticNetworkInterfaceId')
        if m.get('IpName') is not None:
            self.ip_name = m.get('IpName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListLeniPrivateIpAddressesResponseBodyContentData(TeaModel):
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
        # The description.
        self.description = description
        # Lingjun Elastic Network Interface ID.
        self.elastic_network_interface_id = elastic_network_interface_id
        # The time when the activation code was created.
        self.gmt_create = gmt_create
        # The time when the certificate was updated.
        self.gmt_modified = gmt_modified
        # Lingjun Elastic Network Interface secondary private IP unique identifier.
        self.ip_name = ip_name
        # The response message.
        self.message = message
        # Lingjun Elastic Network Interface secondary private IP address.
        self.private_ip_address = private_ip_address
        # The region ID.
        self.region_id = region_id
        # The task status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListLeniPrivateIpAddressesResponseBodyContent(TeaModel):
    def __init__(
        self,
        data: List[ListLeniPrivateIpAddressesResponseBodyContentData] = None,
        resource_group_id: str = None,
        total: int = None,
    ):
        # The response parameters.
        self.data = data
        self.resource_group_id = resource_group_id
        # The total number of entries.
        self.total = total

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListLeniPrivateIpAddressesResponseBodyContentData()
                self.data.append(temp_model.from_map(k))
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListLeniPrivateIpAddressesResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: ListLeniPrivateIpAddressesResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The response data.
        self.content = content
        # The returned message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListLeniPrivateIpAddressesResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListLeniPrivateIpAddressesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListLeniPrivateIpAddressesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListLeniPrivateIpAddressesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLniPrivateIpAddressRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        enable_page: bool = None,
        ip: str = None,
        ip_name: str = None,
        network_interface_id: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # The description of the variable.
        self.description = description
        # Whether pagination is required
        self.enable_page = enable_page
        # network interface controller IP address
        self.ip = ip
        # IP unique identifier
        self.ip_name = ip_name
        # Lingjun network interface controller ID
        self.network_interface_id = network_interface_id
        # The page number of the returned page.
        self.page_number = page_number
        # Obtain the index number of the current mouse click for an animation
        self.page_size = page_size
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.enable_page is not None:
            result['EnablePage'] = self.enable_page
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.ip_name is not None:
            result['IpName'] = self.ip_name
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnablePage') is not None:
            self.enable_page = m.get('EnablePage')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('IpName') is not None:
            self.ip_name = m.get('IpName')
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ListLniPrivateIpAddressResponseBodyContentData(TeaModel):
    def __init__(
        self,
        description: str = None,
        gmt_create: str = None,
        ip_address_mac: str = None,
        ip_name: str = None,
        message: str = None,
        network_interface_id: str = None,
        private_ip_address: str = None,
        region_id: str = None,
        status: str = None,
    ):
        # The instance description.
        self.description = description
        # The time when the data address was created.
        self.gmt_create = gmt_create
        # MAC address of the secondary private network
        self.ip_address_mac = ip_address_mac
        # IP unique identifier
        self.ip_name = ip_name
        # The error message. (If the instance is in the Exception state, the exception cause is prompted.)
        self.message = message
        # Lingjun network interface controller ID
        self.network_interface_id = network_interface_id
        # Secondary private IP address of Lingjun network interface controller
        self.private_ip_address = private_ip_address
        # The region ID.
        self.region_id = region_id
        # The status of the intervention entry. Valid value:
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.ip_address_mac is not None:
            result['IpAddressMac'] = self.ip_address_mac
        if self.ip_name is not None:
            result['IpName'] = self.ip_name
        if self.message is not None:
            result['Message'] = self.message
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id
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
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('IpAddressMac') is not None:
            self.ip_address_mac = m.get('IpAddressMac')
        if m.get('IpName') is not None:
            self.ip_name = m.get('IpName')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListLniPrivateIpAddressResponseBodyContent(TeaModel):
    def __init__(
        self,
        data: List[ListLniPrivateIpAddressResponseBodyContentData] = None,
        resource_group_id: str = None,
        total: int = None,
    ):
        # The returned result.
        self.data = data
        self.resource_group_id = resource_group_id
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListLniPrivateIpAddressResponseBodyContentData()
                self.data.append(temp_model.from_map(k))
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListLniPrivateIpAddressResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: ListLniPrivateIpAddressResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The response parameters.
        self.content = content
        # The error message. (If the instance is in the Exception state, the exception cause is prompted.)
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListLniPrivateIpAddressResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListLniPrivateIpAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListLniPrivateIpAddressResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListLniPrivateIpAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNetworkInterfacesRequestTag(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListNetworkInterfacesRequest(TeaModel):
    def __init__(
        self,
        enable_page: bool = None,
        ip: str = None,
        network_interface_id: str = None,
        node_id: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        subnet_id: str = None,
        tag: List[ListNetworkInterfacesRequestTag] = None,
        vpd_id: str = None,
    ):
        # Specifies whether pagination is required.
        self.enable_page = enable_page
        # network interface controller the IP address.
        self.ip = ip
        # Lingjun network interface controller ID.
        self.network_interface_id = network_interface_id
        # The ID of the machine to which the instance belongs.
        self.node_id = node_id
        # The number of the page to return.
        self.page_number = page_number
        # The current number of pages.
        self.page_size = page_size
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        # The ID of the instance to which the Lingjun subnet belongs.
        self.subnet_id = subnet_id
        self.tag = tag
        # The ID of the VPD.
        self.vpd_id = vpd_id

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_page is not None:
            result['EnablePage'] = self.enable_page
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.subnet_id is not None:
            result['SubnetId'] = self.subnet_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnablePage') is not None:
            self.enable_page = m.get('EnablePage')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SubnetId') is not None:
            self.subnet_id = m.get('SubnetId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListNetworkInterfacesRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        return self


class ListNetworkInterfacesResponseBodyContentDataPrivateIpAddressMacGroup(TeaModel):
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
        # Secondary private MAC address.
        self.ip_address_mac = ip_address_mac
        # The unique IP identifier.
        self.ip_name = ip_name
        # The error message. (If the instance is in the Exception state, the exception cause is prompted.)
        self.message = message
        # The secondary private IP address.
        self.private_ip_address = private_ip_address
        # The status of the cache reserve instance.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListNetworkInterfacesResponseBodyContentDataSubnetBaseInfo(TeaModel):
    def __init__(
        self,
        cidr: str = None,
        create_time: str = None,
        subnet_id: str = None,
        subnet_name: str = None,
    ):
        # The network segment of the Subnet.
        # 
        # *   The network segment of the subnet must be a proper subset of the network segment of Lingjun to which it belongs, and the mask must be between 16 bits and 29 bits, which can provide 8 to 65536 addresses. For example, the CIDR block of the Lingjun CIDR block is 192.168.0.0/16, and the CIDR blocks of the subnets under the Lingjun CIDR block are 192.168.0.0/17 to 192.168.0.0/29.
        # *   The first and last three IP addresses of each subnet segment are reserved by the system. For example, the CIDR blocks of the subnet are 192.168.1.0/24,192.168.1.0, 192.168.1.253, 192.168.1.254, and 192.168.1.255.
        # 
        # For more information about CIDR blocks, see the [What is CIDR?](https://www.alibabacloud.com/help/doc-detail/40637.htm#title-gu4-uzk-12r) section in the "Network FAQ" topic.
        # 
        # This parameter is left empty by default.
        self.cidr = cidr
        # The time when the activation code was created.
        self.create_time = create_time
        # The ID of the Subnet instance.
        self.subnet_id = subnet_id
        # The name of the Subnet instance.
        self.subnet_name = subnet_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListNetworkInterfacesResponseBodyContentDataTags(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListNetworkInterfacesResponseBodyContentDataVpdBaseInfo(TeaModel):
    def __init__(
        self,
        cidr: str = None,
        create_time: str = None,
        vpd_id: str = None,
        vpd_name: str = None,
    ):
        # The network segment of Lingjun network segment (VPD).
        # 
        # *   We recommend that you use an RFC private endpoint as the Lingjun CIDR block, such as 10.0.0.0/8,172.16.0.0/12,192.168.0.0/16. In scenarios where the Doringjun CIDR block is connected to each other or where the Lingjun CIDR block is connected to a VPC, make sure that the addresses do not conflict with each other.
        # *   You can also use a custom CIDR block other than 100.64.0.0/10, 224.0.0.0/4, 127.0.0.0/8, or 169.254.0.0/16 and their subnets as the primary IPv4 CIDR block of the VPD. This parameter is left empty by default.
        self.cidr = cidr
        # The time when the activation code was created.
        self.create_time = create_time
        # The ID of the VPD instance.
        self.vpd_id = vpd_id
        # The name of the VPD instance.
        self.vpd_name = vpd_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListNetworkInterfacesResponseBodyContentData(TeaModel):
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
        private_ip_address_mac_group: List[ListNetworkInterfacesResponseBodyContentDataPrivateIpAddressMacGroup] = None,
        quota: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        service_mac: str = None,
        status: str = None,
        subnet_base_info: ListNetworkInterfacesResponseBodyContentDataSubnetBaseInfo = None,
        tags: List[ListNetworkInterfacesResponseBodyContentDataTags] = None,
        tenant_id: str = None,
        vpd_base_info: ListNetworkInterfacesResponseBodyContentDataVpdBaseInfo = None,
        zone_id: str = None,
    ):
        # The time when the activation code was created.
        self.create_time = create_time
        # The port number of the AD server.
        self.ethernet = ethernet
        # The gateway.
        self.gateway = gateway
        # The IP address of the instance.
        self.ip = ip
        # The NC type.
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
        # Lingjun network interface controller ID.
        self.network_interface_id = network_interface_id
        # The port name.
        self.network_interface_name = network_interface_name
        # The ID of the machine to which the instance belongs.
        self.node_id = node_id
        # Secondary Private IP\\&MAC Address Collection
        self.private_ip_address_mac_group = private_ip_address_mac_group
        # network interface controller private secondary IP quota.
        self.quota = quota
        # The region ID.
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        # The address of the service network interface controller.
        self.service_mac = service_mac
        # The task status.
        self.status = status
        # Lingjun subnet (Subnet) basic information.
        self.subnet_base_info = subnet_base_info
        self.tags = tags
        # The tenant ID.
        self.tenant_id = tenant_id
        # Lingjun network segment (VPD) basic information.
        self.vpd_base_info = vpd_base_info
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.private_ip_address_mac_group:
            for k in self.private_ip_address_mac_group:
                if k:
                    k.validate()
        if self.subnet_base_info:
            self.subnet_base_info.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.vpd_base_info:
            self.vpd_base_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            for k in self.private_ip_address_mac_group:
                result['PrivateIpAddressMacGroup'].append(k.to_map() if k else None)
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
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
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
            for k in m.get('PrivateIpAddressMacGroup'):
                temp_model = ListNetworkInterfacesResponseBodyContentDataPrivateIpAddressMacGroup()
                self.private_ip_address_mac_group.append(temp_model.from_map(k))
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
            temp_model = ListNetworkInterfacesResponseBodyContentDataSubnetBaseInfo()
            self.subnet_base_info = temp_model.from_map(m['SubnetBaseInfo'])
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListNetworkInterfacesResponseBodyContentDataTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('VpdBaseInfo') is not None:
            temp_model = ListNetworkInterfacesResponseBodyContentDataVpdBaseInfo()
            self.vpd_base_info = temp_model.from_map(m['VpdBaseInfo'])
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListNetworkInterfacesResponseBodyContent(TeaModel):
    def __init__(
        self,
        data: List[ListNetworkInterfacesResponseBodyContentData] = None,
        total: int = None,
    ):
        # The response parameters.
        self.data = data
        # The total number of entries that are returned.
        self.total = total

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListNetworkInterfacesResponseBodyContentData()
                self.data.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListNetworkInterfacesResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: ListNetworkInterfacesResponseBodyContent = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListNetworkInterfacesResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListNetworkInterfacesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListNetworkInterfacesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListNetworkInterfacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNodeInfosForPodRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        node_id: str = None,
        region_id: str = None,
        zone_id: str = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # The ID of the node for this operation.
        self.node_id = node_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListNodeInfosForPodResponseBodyContent(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        hdeni_quota: int = None,
        leni_quota: int = None,
        leni_sip_quota: int = None,
        lni_sip_quota: int = None,
        node_id: str = None,
        region_id: str = None,
        v_switches: List[str] = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # Lingjun Gaomi network interface controller quota
        self.hdeni_quota = hdeni_quota
        # Lingjun Elastic Network Interface quota, excluding system type
        self.leni_quota = leni_quota
        # Lingjun Elastic Network Interface Secondary Private IP Quota
        self.leni_sip_quota = leni_sip_quota
        # Lingjun network interface controller Secondary Private IP Quota
        self.lni_sip_quota = lni_sip_quota
        # The ID of the node for this operation.
        self.node_id = node_id
        # The region ID.
        self.region_id = region_id
        # List of VSwitches to which IP addresses can be applied for this node
        self.v_switches = v_switches
        # The ID of the Virtual Private Cloud to which the current node belongs.
        self.vpc_id = vpc_id
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.hdeni_quota is not None:
            result['HdeniQuota'] = self.hdeni_quota
        if self.leni_quota is not None:
            result['LeniQuota'] = self.leni_quota
        if self.leni_sip_quota is not None:
            result['LeniSipQuota'] = self.leni_sip_quota
        if self.lni_sip_quota is not None:
            result['LniSipQuota'] = self.lni_sip_quota
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.v_switches is not None:
            result['VSwitches'] = self.v_switches
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('HdeniQuota') is not None:
            self.hdeni_quota = m.get('HdeniQuota')
        if m.get('LeniQuota') is not None:
            self.leni_quota = m.get('LeniQuota')
        if m.get('LeniSipQuota') is not None:
            self.leni_sip_quota = m.get('LeniSipQuota')
        if m.get('LniSipQuota') is not None:
            self.lni_sip_quota = m.get('LniSipQuota')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VSwitches') is not None:
            self.v_switches = m.get('VSwitches')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListNodeInfosForPodResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: List[ListNodeInfosForPodResponseBodyContent] = None,
        message: str = None,
        request_id: str = None,
    ):
        # The information about the request denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # Response body
        self.content = content
        # The returned message.
        self.message = message
        # Request ID of the current request
        self.request_id = request_id

    def validate(self):
        if self.content:
            for k in self.content:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        result['Content'] = []
        if self.content is not None:
            for k in self.content:
                result['Content'].append(k.to_map() if k else None)
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
        self.content = []
        if m.get('Content') is not None:
            for k in m.get('Content'):
                temp_model = ListNodeInfosForPodResponseBodyContent()
                self.content.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListNodeInfosForPodResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListNodeInfosForPodResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListNodeInfosForPodResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSubnetsRequestTag(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListSubnetsRequest(TeaModel):
    def __init__(
        self,
        enable_page: bool = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        status: str = None,
        subnet_id: str = None,
        subnet_name: str = None,
        tag: List[ListSubnetsRequestTag] = None,
        type: str = None,
        vpd_id: str = None,
        zone_id: str = None,
    ):
        # Specifies whether to query by page. Optional values:
        # 
        # *   **true**: Enable pagination query
        # *   **false**: Pagination query is disabled
        self.enable_page = enable_page
        # The number of the page to return. The value must be greater than 0. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.page_size = page_size
        # The region ID of the disk.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID.
        # 
        # For more information about resource groups, see [Resource groups](https://help.aliyun.com/document_detail/94475.htm?spm=a2c4g.11186623.0.0.29e15d7akXhpuu).
        self.resource_group_id = resource_group_id
        # The status of the CLB instance. Valid values:
        # 
        # *   **Available**: Normal
        # *   **Not Available**: Unavailable
        # *   **Executing**: Executing
        # *   **Deleting**: The node is being deleted.
        self.status = status
        # Lingjun subnet instance ID
        self.subnet_id = subnet_id
        # Lingjun subnet instance name
        self.subnet_name = subnet_name
        # The tag information.
        # 
        # You can specify up to 20 tags.
        self.tag = tag
        # Lingjun Subnet Usage Type; optional; optional. Valid values:
        # 
        # *   **If you do not set this field for a common type**\
        # *   **OOB** :OOB type
        # *   **LB**: LB type
        self.type = type
        # The ID of the Lingjun CIDR block.
        self.vpd_id = vpd_id
        # The zone ID of the disk.
        self.zone_id = zone_id

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_page is not None:
            result['EnablePage'] = self.enable_page
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
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
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnablePage') is not None:
            self.enable_page = m.get('EnablePage')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
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
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListSubnetsRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListSubnetsResponseBodyContentDataTags(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListSubnetsResponseBodyContentDataVpdBaseInfo(TeaModel):
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
        # The time when the data address was created.
        self.create_time = create_time
        # Lingjun CIDR block instance ID
        self.vpd_id = vpd_id
        # Lingjun CIDR block instance name
        self.vpd_name = vpd_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListSubnetsResponseBodyContentData(TeaModel):
    def __init__(
        self,
        cidr: str = None,
        create_time: str = None,
        gmt_modified: str = None,
        message: str = None,
        nc_count: int = None,
        network_interface_count: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        status: str = None,
        subnet_id: str = None,
        subnet_name: str = None,
        tags: List[ListSubnetsResponseBodyContentDataTags] = None,
        tenant_id: str = None,
        type: str = None,
        vpd_base_info: ListSubnetsResponseBodyContentDataVpdBaseInfo = None,
        vpd_id: str = None,
        zone_id: str = None,
    ):
        # The CIDR block of the Subnet.
        # 
        # *   The network segment of the subnet must be a proper subset of the network segment of Lingjun to which it belongs, and the mask must be between 16 bits and 29 bits, which can provide 8 to 65536 addresses. For example, the CIDR block of the Lingjun CIDR block is 192.168.0.0/16, and the CIDR blocks of the subnets under the Lingjun CIDR block are 192.168.0.0/17 to 192.168.0.0/29.
        # *   The first and last three IP addresses of each subnet segment are reserved by the system. For example, the CIDR blocks of the subnet are 192.168.1.0/24,192.168.1.0, 192.168.1.253, 192.168.1.254, and 192.168.1.255.
        self.cidr = cidr
        # The time when the data address was created.
        self.create_time = create_time
        # The time when the agent was last modified.
        self.gmt_modified = gmt_modified
        # The error message. (If the instance is in the Exception state, the exception cause is prompted.)
        self.message = message
        # Number of NCs
        self.nc_count = nc_count
        # Number of Lingjun network interface controller
        self.network_interface_count = network_interface_count
        # The region ID.
        self.region_id = region_id
        # The ID of your Alibaba Cloud resource group.
        # 
        # For more information about resource groups, see [Resource groups](https://help.aliyun.com/document_detail/94475.htm?spm=a2c4g.11186623.0.0.29e15d7akXhpuu).
        self.resource_group_id = resource_group_id
        # The status of the cache reserve instance. Valid values:
        # 
        # *   **Available**: Normal
        # *   **Not Available**: Unavailable
        # *   **Executing**: Executing
        # *   **Deleting**: The node is being deleted.
        self.status = status
        # Lingjun subnet instance ID
        self.subnet_id = subnet_id
        # Lingjun subnet instance name
        self.subnet_name = subnet_name
        # The tag information.
        # 
        # You can specify up to 20 tags.
        self.tags = tags
        # The ID of the tenant.
        self.tenant_id = tenant_id
        # Lingjun Subnet Usage Type; optional; optional. Valid values:
        # 
        # *   **If you do not set this field for a common type**\
        # *   **OOB** :OOB type
        # *   **LB**: LB type
        self.type = type
        # vpd basic information
        self.vpd_base_info = vpd_base_info
        # The ID of the Lingjun CIDR block.
        self.vpd_id = vpd_id
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.vpd_base_info:
            self.vpd_base_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr is not None:
            result['Cidr'] = self.cidr
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.message is not None:
            result['Message'] = self.message
        if self.nc_count is not None:
            result['NcCount'] = self.nc_count
        if self.network_interface_count is not None:
            result['NetworkInterfaceCount'] = self.network_interface_count
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
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
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
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NcCount') is not None:
            self.nc_count = m.get('NcCount')
        if m.get('NetworkInterfaceCount') is not None:
            self.network_interface_count = m.get('NetworkInterfaceCount')
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
            for k in m.get('Tags'):
                temp_model = ListSubnetsResponseBodyContentDataTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VpdBaseInfo') is not None:
            temp_model = ListSubnetsResponseBodyContentDataVpdBaseInfo()
            self.vpd_base_info = temp_model.from_map(m['VpdBaseInfo'])
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListSubnetsResponseBodyContent(TeaModel):
    def __init__(
        self,
        data: List[ListSubnetsResponseBodyContentData] = None,
        total: int = None,
    ):
        # Lingjun subnet information list
        self.data = data
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListSubnetsResponseBodyContentData()
                self.data.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListSubnetsResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: ListSubnetsResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The response parameters.
        self.content = content
        # The returned message.
        self.message = message
        # Request ID of the current request
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListSubnetsResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListSubnetsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSubnetsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListSubnetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVccFlowInfosRequest(TeaModel):
    def __init__(
        self,
        direction: str = None,
        from_: int = None,
        metric_name: str = None,
        region_id: str = None,
        to: int = None,
        vcc_id: str = None,
    ):
        # Direction
        # 
        # Valid value:
        # 
        # *   IN: inbound.
        # *   OUT: the outbound.
        self.direction = direction
        # The start time. The default value is 5 minutes ago.
        self.from_ = from_
        # Metric
        # 
        # Valid value:
        # 
        # *   totalPacketsRate: Total Packet Rate.
        # *   dropBytesRate: the of the stream drop rate.
        # *   dropPacketsRate: Dropped Packet Rate.
        # *   totalBytesRate: the total streaming rate.
        # *   passBytesRate: by stream rate.
        # *   passPacketsRate: by packet rate.
        self.metric_name = metric_name
        # The region ID.
        self.region_id = region_id
        # The end time. The default time is the current time.
        self.to = to
        # Lingjun Connection ID
        self.vcc_id = vcc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.from_ is not None:
            result['From'] = self.from_
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.to is not None:
            result['To'] = self.to
        if self.vcc_id is not None:
            result['VccId'] = self.vcc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('To') is not None:
            self.to = m.get('To')
        if m.get('VccId') is not None:
            self.vcc_id = m.get('VccId')
        return self


class ListVccFlowInfosResponseBodyContentData(TeaModel):
    def __init__(
        self,
        direction: str = None,
        metric_name: str = None,
        region_id: str = None,
        timestamp: int = None,
        value: float = None,
        vcc_id: str = None,
    ):
        # The direction.
        self.direction = direction
        # The metric. Valid values:
        self.metric_name = metric_name
        # The region ID.
        self.region_id = region_id
        # Time
        self.timestamp = timestamp
        # Value
        self.value = value
        # Lingjun Connection ID
        self.vcc_id = vcc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.value is not None:
            result['Value'] = self.value
        if self.vcc_id is not None:
            result['VccId'] = self.vcc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('VccId') is not None:
            self.vcc_id = m.get('VccId')
        return self


class ListVccFlowInfosResponseBodyContent(TeaModel):
    def __init__(
        self,
        data: List[ListVccFlowInfosResponseBodyContentData] = None,
        total: int = None,
    ):
        # Lingjun Connection Traffic Information
        self.data = data
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListVccFlowInfosResponseBodyContentData()
                self.data.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListVccFlowInfosResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: ListVccFlowInfosResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # 访问被拒绝的详细原因。
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The returned data.
        self.content = content
        # Response
        self.message = message
        # Request ID of the current request
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListVccFlowInfosResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListVccFlowInfosResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListVccFlowInfosResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListVccFlowInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVccGrantRulesRequest(TeaModel):
    def __init__(
        self,
        enable_page: bool = None,
        er_id: str = None,
        for_select: bool = None,
        grant_rule_id: str = None,
        grant_tenant_id: str = None,
        instance_id: str = None,
        instance_name: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # Specifies whether to enable paged query. Optional values:
        # 
        # *   **true**: Enable pagination query
        # *   **false**: Pagination query is disabled
        self.enable_page = enable_page
        # Lingjun HUB ID
        self.er_id = er_id
        # Use the drop-down box
        self.for_select = for_select
        # Authorization Entry ID
        self.grant_rule_id = grant_rule_id
        # Authorized Tenant ID
        self.grant_tenant_id = grant_tenant_id
        # Network Instance ID
        self.instance_id = instance_id
        # Instance name
        self.instance_name = instance_name
        # The page number of the page to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: 20.
        self.page_size = page_size
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Resource group instance ID
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_page is not None:
            result['EnablePage'] = self.enable_page
        if self.er_id is not None:
            result['ErId'] = self.er_id
        if self.for_select is not None:
            result['ForSelect'] = self.for_select
        if self.grant_rule_id is not None:
            result['GrantRuleId'] = self.grant_rule_id
        if self.grant_tenant_id is not None:
            result['GrantTenantId'] = self.grant_tenant_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnablePage') is not None:
            self.enable_page = m.get('EnablePage')
        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')
        if m.get('ForSelect') is not None:
            self.for_select = m.get('ForSelect')
        if m.get('GrantRuleId') is not None:
            self.grant_rule_id = m.get('GrantRuleId')
        if m.get('GrantTenantId') is not None:
            self.grant_tenant_id = m.get('GrantTenantId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ListVccGrantRulesResponseBodyContentData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        er_id: str = None,
        grant_rule_id: str = None,
        grant_tenant_id: str = None,
        instance_id: str = None,
        instance_name: str = None,
        product: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        tenant_id: str = None,
        used: bool = None,
    ):
        # The time when the data address was created.
        self.create_time = create_time
        # Lingjun HUB ID
        self.er_id = er_id
        # Cross-account authorization information Instance ID
        self.grant_rule_id = grant_rule_id
        # Authorized Tenant ID
        self.grant_tenant_id = grant_tenant_id
        # Network Instance ID
        self.instance_id = instance_id
        # The name of the ECU.
        self.instance_name = instance_name
        # The type of the authorized product. Valid values:
        # 
        # *   **VPD**: indicates a VPD instance of the Lingjun network segment.
        # *   **VCC**: indicates that Lingjun connects to the VCC instance.
        self.product = product
        # The region ID.
        self.region_id = region_id
        # Resource group instance ID
        self.resource_group_id = resource_group_id
        # The ID of the tenant.
        self.tenant_id = tenant_id
        # Whether the current cross-account resource has been bound to the cross-account Lingjun HUB. Valid values:
        # 
        # *   **true**: Used
        # *   **false**: Not used
        self.used = used

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.er_id is not None:
            result['ErId'] = self.er_id
        if self.grant_rule_id is not None:
            result['GrantRuleId'] = self.grant_rule_id
        if self.grant_tenant_id is not None:
            result['GrantTenantId'] = self.grant_tenant_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.product is not None:
            result['Product'] = self.product
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.used is not None:
            result['Used'] = self.used
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')
        if m.get('GrantRuleId') is not None:
            self.grant_rule_id = m.get('GrantRuleId')
        if m.get('GrantTenantId') is not None:
            self.grant_tenant_id = m.get('GrantTenantId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Used') is not None:
            self.used = m.get('Used')
        return self


class ListVccGrantRulesResponseBodyContent(TeaModel):
    def __init__(
        self,
        data: List[ListVccGrantRulesResponseBodyContentData] = None,
        total: int = None,
    ):
        # List of cross-account authorization information of Lingjun connection
        self.data = data
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListVccGrantRulesResponseBodyContentData()
                self.data.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListVccGrantRulesResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: ListVccGrantRulesResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The response parameters.
        self.content = content
        # The returned message.
        self.message = message
        # Request ID of the current request
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListVccGrantRulesResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListVccGrantRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListVccGrantRulesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListVccGrantRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVccRouteEntriesRequest(TeaModel):
    def __init__(
        self,
        destination_cidr_block: str = None,
        enable_page: bool = None,
        ignore_detailed_route_entry: bool = None,
        next_hop_id: str = None,
        next_hop_type: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        route_type: str = None,
        status: str = None,
        vcc_id: str = None,
        vpd_route_entry_id: str = None,
    ):
        # Destination CIDR block
        self.destination_cidr_block = destination_cidr_block
        # Specifies whether to enable pagination query.
        self.enable_page = enable_page
        # Filter 32 detailed CIDR blocks. Default value: true
        self.ignore_detailed_route_entry = ignore_detailed_route_entry
        # Next Hop Instance
        self.next_hop_id = next_hop_id
        # Next Hop Instance Type
        self.next_hop_type = next_hop_type
        # The page number of the page to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: 20.
        self.page_size = page_size
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Resource group instance ID
        self.resource_group_id = resource_group_id
        # Route type
        self.route_type = route_type
        # The status of the enterprise-level snapshot policy.
        self.status = status
        # The ID of the Lingjun connection instance.
        # 
        # This parameter is required.
        self.vcc_id = vcc_id
        # Lingjun CIDR block route entry instance ID
        self.vpd_route_entry_id = vpd_route_entry_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        if self.enable_page is not None:
            result['EnablePage'] = self.enable_page
        if self.ignore_detailed_route_entry is not None:
            result['IgnoreDetailedRouteEntry'] = self.ignore_detailed_route_entry
        if self.next_hop_id is not None:
            result['NextHopId'] = self.next_hop_id
        if self.next_hop_type is not None:
            result['NextHopType'] = self.next_hop_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.route_type is not None:
            result['RouteType'] = self.route_type
        if self.status is not None:
            result['Status'] = self.status
        if self.vcc_id is not None:
            result['VccId'] = self.vcc_id
        if self.vpd_route_entry_id is not None:
            result['VpdRouteEntryId'] = self.vpd_route_entry_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        if m.get('EnablePage') is not None:
            self.enable_page = m.get('EnablePage')
        if m.get('IgnoreDetailedRouteEntry') is not None:
            self.ignore_detailed_route_entry = m.get('IgnoreDetailedRouteEntry')
        if m.get('NextHopId') is not None:
            self.next_hop_id = m.get('NextHopId')
        if m.get('NextHopType') is not None:
            self.next_hop_type = m.get('NextHopType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RouteType') is not None:
            self.route_type = m.get('RouteType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VccId') is not None:
            self.vcc_id = m.get('VccId')
        if m.get('VpdRouteEntryId') is not None:
            self.vpd_route_entry_id = m.get('VpdRouteEntryId')
        return self


class ListVccRouteEntriesResponseBodyContentData(TeaModel):
    def __init__(
        self,
        destination_cidr_block: str = None,
        gmt_modified: str = None,
        message: str = None,
        next_hop_id: str = None,
        next_hop_type: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_tenant_id: str = None,
        route_type: str = None,
        status: str = None,
        tenant_id: str = None,
        vcc_id: str = None,
        vcc_route_entry_id: str = None,
    ):
        # Destination CIDR block
        self.destination_cidr_block = destination_cidr_block
        # The time when the cluster was updated.
        self.gmt_modified = gmt_modified
        # The returned message.
        self.message = message
        # Next Hop Instance
        self.next_hop_id = next_hop_id
        # Next Hop Type
        self.next_hop_type = next_hop_type
        # The region ID.
        self.region_id = region_id
        # Resource group instance ID
        self.resource_group_id = resource_group_id
        # The ID of the tenant to which the resource belongs.
        self.resource_tenant_id = resource_tenant_id
        # Route type
        self.route_type = route_type
        # The status of the intervention entry. Valid value:
        self.status = status
        # The ID of the tenant.
        self.tenant_id = tenant_id
        # The ID of the Lingjun connection instance.
        self.vcc_id = vcc_id
        # The ID of the route entry.
        self.vcc_route_entry_id = vcc_route_entry_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.message is not None:
            result['Message'] = self.message
        if self.next_hop_id is not None:
            result['NextHopId'] = self.next_hop_id
        if self.next_hop_type is not None:
            result['NextHopType'] = self.next_hop_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_tenant_id is not None:
            result['ResourceTenantId'] = self.resource_tenant_id
        if self.route_type is not None:
            result['RouteType'] = self.route_type
        if self.status is not None:
            result['Status'] = self.status
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.vcc_id is not None:
            result['VccId'] = self.vcc_id
        if self.vcc_route_entry_id is not None:
            result['VccRouteEntryId'] = self.vcc_route_entry_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextHopId') is not None:
            self.next_hop_id = m.get('NextHopId')
        if m.get('NextHopType') is not None:
            self.next_hop_type = m.get('NextHopType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceTenantId') is not None:
            self.resource_tenant_id = m.get('ResourceTenantId')
        if m.get('RouteType') is not None:
            self.route_type = m.get('RouteType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('VccId') is not None:
            self.vcc_id = m.get('VccId')
        if m.get('VccRouteEntryId') is not None:
            self.vcc_route_entry_id = m.get('VccRouteEntryId')
        return self


class ListVccRouteEntriesResponseBodyContent(TeaModel):
    def __init__(
        self,
        data: List[ListVccRouteEntriesResponseBodyContentData] = None,
        total: int = None,
    ):
        # List of Lingjun Connection Route Entries
        self.data = data
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListVccRouteEntriesResponseBodyContentData()
                self.data.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListVccRouteEntriesResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: ListVccRouteEntriesResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The response parameters.
        self.content = content
        # response message, if the success request is
        self.message = message
        # Request ID of the current request
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListVccRouteEntriesResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListVccRouteEntriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListVccRouteEntriesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListVccRouteEntriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVccsRequestTag(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListVccsRequest(TeaModel):
    def __init__(
        self,
        bandwidth: int = None,
        cen_id: str = None,
        enable_page: bool = None,
        ex_status: str = None,
        filter_er_id: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        status: str = None,
        tag: List[ListVccsRequestTag] = None,
        vcc_id: str = None,
        vpc_id: str = None,
        vpd_id: str = None,
    ):
        # The peak bandwidth of the Lingjun connection instance. Unit: Mbit/s. Valid values: 1000 to 400000
        self.bandwidth = bandwidth
        # The ID of the CEN instance; [What is the CEN?](https://help.aliyun.com/document_detail/181681.html)
        # 
        # You can call the [DescribeCens](https://help.aliyun.com/document_detail/468215.htm) to query the information of CEN instances under the current Alibaba Cloud account.
        self.cen_id = cen_id
        # Specifies whether to enable paged query. Optional values:
        # 
        # *   **true**: Enable pagination query
        # *   **false**: Pagination query is disabled
        self.enable_page = enable_page
        # Excludes all data in the specified status. If the status parameter exists, ExStatus does not take effect.
        self.ex_status = ex_status
        # Filter queries by Lingjun HUB instance ID
        self.filter_er_id = filter_er_id
        # The page number of the page to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: 20.
        self.page_size = page_size
        # The region ID.
        self.region_id = region_id
        # The resource group ID.
        # 
        # For more information about resource groups, see [Resource groups](https://help.aliyun.com/document_detail/94475.htm?spm=a2c4g.11186623.0.0.29e15d7akXhpuu).
        self.resource_group_id = resource_group_id
        # The instance status.
        self.status = status
        # The tag information.
        # 
        # You can specify up to 20 tags.
        self.tag = tag
        # The ID of the Lingjun connection instance.
        self.vcc_id = vcc_id
        # Virtual Private Cloud IDs; [What is Virtual Private Cloud](https://help.aliyun.com/document_detail/34217.html)
        # 
        # You can call the [DescribeVpcs](https://help.aliyun.com/document_detail/35739.html#demo-0) operation to query the specified VPC.
        self.vpc_id = vpc_id
        # Lingjun CIDR block instance ID
        self.vpd_id = vpd_id

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.enable_page is not None:
            result['EnablePage'] = self.enable_page
        if self.ex_status is not None:
            result['ExStatus'] = self.ex_status
        if self.filter_er_id is not None:
            result['FilterErId'] = self.filter_er_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.status is not None:
            result['Status'] = self.status
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.vcc_id is not None:
            result['VccId'] = self.vcc_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('EnablePage') is not None:
            self.enable_page = m.get('EnablePage')
        if m.get('ExStatus') is not None:
            self.ex_status = m.get('ExStatus')
        if m.get('FilterErId') is not None:
            self.filter_er_id = m.get('FilterErId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListVccsRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VccId') is not None:
            self.vcc_id = m.get('VccId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        return self


class ListVccsResponseBodyContentDataErInfos(TeaModel):
    def __init__(
        self,
        connections: int = None,
        create_time: str = None,
        description: str = None,
        er_id: str = None,
        er_name: str = None,
        gmt_modified: str = None,
        master_zone_id: str = None,
        message: str = None,
        region_id: str = None,
        route_maps: int = None,
        status: str = None,
        tenant_id: str = None,
    ):
        # Connections
        self.connections = connections
        # The time when the data address was created.
        self.create_time = create_time
        # Description
        self.description = description
        # Elastic Router ID
        self.er_id = er_id
        # ER instance name
        self.er_name = er_name
        # The time when the agent was last modified.
        self.gmt_modified = gmt_modified
        # Primary Zone
        self.master_zone_id = master_zone_id
        # The message that is returned.
        self.message = message
        # ER region information
        self.region_id = region_id
        # Number of routing policy
        self.route_maps = route_maps
        # The status of the intervention entry. Valid value:
        self.status = status
        # The ID of the tenant.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connections is not None:
            result['Connections'] = self.connections
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.er_id is not None:
            result['ErId'] = self.er_id
        if self.er_name is not None:
            result['ErName'] = self.er_name
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.master_zone_id is not None:
            result['MasterZoneId'] = self.master_zone_id
        if self.message is not None:
            result['Message'] = self.message
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.route_maps is not None:
            result['RouteMaps'] = self.route_maps
        if self.status is not None:
            result['Status'] = self.status
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Connections') is not None:
            self.connections = m.get('Connections')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')
        if m.get('ErName') is not None:
            self.er_name = m.get('ErName')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('MasterZoneId') is not None:
            self.master_zone_id = m.get('MasterZoneId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RouteMaps') is not None:
            self.route_maps = m.get('RouteMaps')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class ListVccsResponseBodyContentDataTags(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListVccsResponseBodyContentDataVpdBaseInfo(TeaModel):
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
        # The time when the data address was created.
        self.create_time = create_time
        # Lingjun CIDR block instance ID
        self.vpd_id = vpd_id
        # Lingjun CIDR block instance name
        self.vpd_name = vpd_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListVccsResponseBodyContentData(TeaModel):
    def __init__(
        self,
        access_point_id: str = None,
        bandwidth_str: str = None,
        bgp_asn: str = None,
        bgp_cidr: str = None,
        cen_id: str = None,
        cen_owner_id: str = None,
        commodity_code: str = None,
        connection_type: str = None,
        create_time: str = None,
        current_node: str = None,
        er_infos: List[ListVccsResponseBodyContentDataErInfos] = None,
        expiration_date: str = None,
        gmt_modified: str = None,
        line_operator: str = None,
        message: str = None,
        port_type: str = None,
        rate: float = None,
        region_id: str = None,
        resource_group_id: str = None,
        spec: str = None,
        status: str = None,
        tags: List[ListVccsResponseBodyContentDataTags] = None,
        task_id: str = None,
        tenant_id: str = None,
        vcc_id: str = None,
        vcc_name: str = None,
        vpc_id: str = None,
        vpd_base_info: ListVccsResponseBodyContentDataVpdBaseInfo = None,
        vpd_id: str = None,
        zone_id: str = None,
    ):
        # Express Connect circuit access point ID:
        # 
        # *   **ap-cn-wulanchabu-jn-ts-A**: Ulanqab-Jining-A
        # *   **ap-cn-heyuan-yc-ts-SA127**: Heyuan-Yuancheng-A
        self.access_point_id = access_point_id
        # The bandwidth of the port.
        self.bandwidth_str = bandwidth_str
        # bgp as number
        self.bgp_asn = bgp_asn
        # bgp network segment
        self.bgp_cidr = bgp_cidr
        # The ID of the CEN instance; [What is the CEN?](https://help.aliyun.com/document_detail/181681.html)
        # 
        # You can call the [DescribeCens](https://help.aliyun.com/document_detail/468215.htm) to query the information of CEN instances under the current Alibaba Cloud account.
        self.cen_id = cen_id
        # Account to which cen belongs
        self.cen_owner_id = cen_owner_id
        # Commodity code
        self.commodity_code = commodity_code
        # The connection mode. Valid values:
        # 
        # *   **VPC**\
        # *   **CENTR**\
        self.connection_type = connection_type
        # The time when the data address was created.
        self.create_time = create_time
        # Current process node
        self.current_node = current_node
        # List of bound Lingjun HUB information
        self.er_infos = er_infos
        # The time when the application expired.
        self.expiration_date = expiration_date
        # The time when the cluster was updated.
        self.gmt_modified = gmt_modified
        # The connectivity provider of the Express Connect circuit. Valid values:
        # 
        # *   **CO**: other connectivity providers in the Chinese mainland
        self.line_operator = line_operator
        # The error message. (If the instance is in the Exception state, the exception cause is prompted.)
        self.message = message
        # The port type of the Express Connect circuit. Valid values:
        # 
        # *   **100GBase-LR**: 100,000 megabytes of single-mode optical port (10 km)
        self.port_type = port_type
        # Process progress; value returns 0 to 1; not started is null
        self.rate = rate
        # The region ID.
        self.region_id = region_id
        # The ID of your Alibaba Cloud resource group.
        # 
        # For more information about resource groups, see [Resource groups](https://help.aliyun.com/document_detail/94475.htm?spm=a2c4g.11186623.0.0.29e15d7akXhpuu).
        self.resource_group_id = resource_group_id
        # The compute specification.
        self.spec = spec
        # The state of the rule.
        self.status = status
        # The tag information.
        # 
        # You can specify up to 20 tags.
        self.tags = tags
        # The job ID.
        self.task_id = task_id
        # The ID of the tenant.
        self.tenant_id = tenant_id
        # The ID of the Lingjun connection instance.
        self.vcc_id = vcc_id
        # The name of the Lingjun connection instance.
        self.vcc_name = vcc_name
        # Virtual Private Cloud IDs; [What is Virtual Private Cloud](https://help.aliyun.com/document_detail/34217.html)
        # 
        # You can call the [DescribeVpcs](https://help.aliyun.com/document_detail/35739.html#demo-0) operation to query the specified VPC.
        self.vpc_id = vpc_id
        # Lingjun network segment information (applicable to the scene where the old version of Lingjun connection is directly bound to Lingjun network segment)
        self.vpd_base_info = vpd_base_info
        # Lingjun CIDR block instance ID
        self.vpd_id = vpd_id
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.er_infos:
            for k in self.er_infos:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.vpd_base_info:
            self.vpd_base_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_point_id is not None:
            result['AccessPointId'] = self.access_point_id
        if self.bandwidth_str is not None:
            result['BandwidthStr'] = self.bandwidth_str
        if self.bgp_asn is not None:
            result['BgpAsn'] = self.bgp_asn
        if self.bgp_cidr is not None:
            result['BgpCidr'] = self.bgp_cidr
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.cen_owner_id is not None:
            result['CenOwnerId'] = self.cen_owner_id
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.connection_type is not None:
            result['ConnectionType'] = self.connection_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.current_node is not None:
            result['CurrentNode'] = self.current_node
        result['ErInfos'] = []
        if self.er_infos is not None:
            for k in self.er_infos:
                result['ErInfos'].append(k.to_map() if k else None)
        if self.expiration_date is not None:
            result['ExpirationDate'] = self.expiration_date
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.line_operator is not None:
            result['LineOperator'] = self.line_operator
        if self.message is not None:
            result['Message'] = self.message
        if self.port_type is not None:
            result['PortType'] = self.port_type
        if self.rate is not None:
            result['Rate'] = self.rate
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.spec is not None:
            result['Spec'] = self.spec
        if self.status is not None:
            result['Status'] = self.status
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.vcc_id is not None:
            result['VccId'] = self.vcc_id
        if self.vcc_name is not None:
            result['VccName'] = self.vcc_name
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpd_base_info is not None:
            result['VpdBaseInfo'] = self.vpd_base_info.to_map()
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessPointId') is not None:
            self.access_point_id = m.get('AccessPointId')
        if m.get('BandwidthStr') is not None:
            self.bandwidth_str = m.get('BandwidthStr')
        if m.get('BgpAsn') is not None:
            self.bgp_asn = m.get('BgpAsn')
        if m.get('BgpCidr') is not None:
            self.bgp_cidr = m.get('BgpCidr')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('CenOwnerId') is not None:
            self.cen_owner_id = m.get('CenOwnerId')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('ConnectionType') is not None:
            self.connection_type = m.get('ConnectionType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CurrentNode') is not None:
            self.current_node = m.get('CurrentNode')
        self.er_infos = []
        if m.get('ErInfos') is not None:
            for k in m.get('ErInfos'):
                temp_model = ListVccsResponseBodyContentDataErInfos()
                self.er_infos.append(temp_model.from_map(k))
        if m.get('ExpirationDate') is not None:
            self.expiration_date = m.get('ExpirationDate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('LineOperator') is not None:
            self.line_operator = m.get('LineOperator')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PortType') is not None:
            self.port_type = m.get('PortType')
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListVccsResponseBodyContentDataTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('VccId') is not None:
            self.vcc_id = m.get('VccId')
        if m.get('VccName') is not None:
            self.vcc_name = m.get('VccName')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpdBaseInfo') is not None:
            temp_model = ListVccsResponseBodyContentDataVpdBaseInfo()
            self.vpd_base_info = temp_model.from_map(m['VpdBaseInfo'])
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListVccsResponseBodyContent(TeaModel):
    def __init__(
        self,
        data: List[ListVccsResponseBodyContentData] = None,
        total: int = None,
    ):
        # Lingjun Connection Information List
        self.data = data
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListVccsResponseBodyContentData()
                self.data.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListVccsResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: ListVccsResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The response parameters.
        self.content = content
        # The error message. (If the instance is in the Exception state, the exception cause is prompted.)
        self.message = message
        # Request ID of the current request
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListVccsResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListVccsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListVccsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListVccsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVpdGrantRulesRequest(TeaModel):
    def __init__(
        self,
        enable_page: bool = None,
        er_id: str = None,
        for_select: bool = None,
        grant_rule_id: str = None,
        grant_tenant_id: str = None,
        instance_id: str = None,
        instance_name: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # Specifies whether to enable pagination query.
        self.enable_page = enable_page
        # Lingjun HUB Instance ID
        self.er_id = er_id
        # Use the drop-down box
        self.for_select = for_select
        # Authorization Entry ID
        self.grant_rule_id = grant_rule_id
        # Authorized Tenant ID
        self.grant_tenant_id = grant_tenant_id
        # The ID of the network instance that you want to query.
        self.instance_id = instance_id
        # Instance name
        self.instance_name = instance_name
        # The page number of the page to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: 10.
        self.page_size = page_size
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Resource group instance ID
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_page is not None:
            result['EnablePage'] = self.enable_page
        if self.er_id is not None:
            result['ErId'] = self.er_id
        if self.for_select is not None:
            result['ForSelect'] = self.for_select
        if self.grant_rule_id is not None:
            result['GrantRuleId'] = self.grant_rule_id
        if self.grant_tenant_id is not None:
            result['GrantTenantId'] = self.grant_tenant_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnablePage') is not None:
            self.enable_page = m.get('EnablePage')
        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')
        if m.get('ForSelect') is not None:
            self.for_select = m.get('ForSelect')
        if m.get('GrantRuleId') is not None:
            self.grant_rule_id = m.get('GrantRuleId')
        if m.get('GrantTenantId') is not None:
            self.grant_tenant_id = m.get('GrantTenantId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ListVpdGrantRulesResponseBodyContentData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        er_id: str = None,
        grant_rule_id: str = None,
        grant_tenant_id: str = None,
        instance_id: str = None,
        instance_name: str = None,
        product: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        tenant_id: str = None,
        used: bool = None,
    ):
        # The time when the data address was created.
        self.create_time = create_time
        # The current network sample is authorized to the specified Lingjun HUB sample ID.
        self.er_id = er_id
        # Authorization Entry ID
        self.grant_rule_id = grant_rule_id
        # The ID of the tenant to which the current instance is authorized.
        self.grant_tenant_id = grant_tenant_id
        # Lingjun CIDR block instance ID
        self.instance_id = instance_id
        # The name of the ECU.
        self.instance_name = instance_name
        # The type of the authorized product. Valid values:
        # 
        # *   **VPD**: indicates a VPD instance of the Lingjun network segment.
        # *   **VCC**: indicates that Lingjun connects to the VCC instance.
        # 
        # The caller does not need to specify.
        self.product = product
        # The region ID.
        self.region_id = region_id
        # Resource group instance ID
        self.resource_group_id = resource_group_id
        # The ID of the tenant.
        self.tenant_id = tenant_id
        # Whether the current authorized instance has been bound
        self.used = used

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.er_id is not None:
            result['ErId'] = self.er_id
        if self.grant_rule_id is not None:
            result['GrantRuleId'] = self.grant_rule_id
        if self.grant_tenant_id is not None:
            result['GrantTenantId'] = self.grant_tenant_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.product is not None:
            result['Product'] = self.product
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.used is not None:
            result['Used'] = self.used
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')
        if m.get('GrantRuleId') is not None:
            self.grant_rule_id = m.get('GrantRuleId')
        if m.get('GrantTenantId') is not None:
            self.grant_tenant_id = m.get('GrantTenantId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Used') is not None:
            self.used = m.get('Used')
        return self


class ListVpdGrantRulesResponseBodyContent(TeaModel):
    def __init__(
        self,
        data: List[ListVpdGrantRulesResponseBodyContentData] = None,
        total: int = None,
    ):
        # Lingjun CIDR block authorization information list
        self.data = data
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListVpdGrantRulesResponseBodyContentData()
                self.data.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListVpdGrantRulesResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: ListVpdGrantRulesResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The HTTP status code.
        self.code = code
        # The response parameters.
        self.content = content
        # The error message. (If the instance is in the Exception state, the exception cause is prompted.)
        self.message = message
        # Request ID of the current request
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListVpdGrantRulesResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListVpdGrantRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListVpdGrantRulesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListVpdGrantRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVpdRouteEntriesRequest(TeaModel):
    def __init__(
        self,
        destination_cidr_block: str = None,
        enable_page: bool = None,
        ignore_detailed_route_entry: bool = None,
        next_hop_id: str = None,
        next_hop_type: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        route_type: str = None,
        status: str = None,
        vpd_id: str = None,
        vpd_route_entry_id: str = None,
    ):
        # Destination CIDR block
        self.destination_cidr_block = destination_cidr_block
        # Specifies whether to enable paged query. Optional values:
        # 
        # *   **true**: Enable pagination query
        # *   **false**: Pagination query is disabled
        self.enable_page = enable_page
        # Filter 32 detailed CIDR blocks. Default value: true
        self.ignore_detailed_route_entry = ignore_detailed_route_entry
        # Next Hop Instance
        self.next_hop_id = next_hop_id
        # Next Hop Instance Type
        self.next_hop_type = next_hop_type
        # The page number of the page to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 20.
        self.page_size = page_size
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Resource group instance ID
        self.resource_group_id = resource_group_id
        # Route type
        self.route_type = route_type
        # The status of the enterprise-level snapshot policy.
        self.status = status
        # Lingjun CIDR block instance ID
        # 
        # This parameter is required.
        self.vpd_id = vpd_id
        # Lingjun CIDR block route entry instance ID
        self.vpd_route_entry_id = vpd_route_entry_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        if self.enable_page is not None:
            result['EnablePage'] = self.enable_page
        if self.ignore_detailed_route_entry is not None:
            result['IgnoreDetailedRouteEntry'] = self.ignore_detailed_route_entry
        if self.next_hop_id is not None:
            result['NextHopId'] = self.next_hop_id
        if self.next_hop_type is not None:
            result['NextHopType'] = self.next_hop_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.route_type is not None:
            result['RouteType'] = self.route_type
        if self.status is not None:
            result['Status'] = self.status
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        if self.vpd_route_entry_id is not None:
            result['VpdRouteEntryId'] = self.vpd_route_entry_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        if m.get('EnablePage') is not None:
            self.enable_page = m.get('EnablePage')
        if m.get('IgnoreDetailedRouteEntry') is not None:
            self.ignore_detailed_route_entry = m.get('IgnoreDetailedRouteEntry')
        if m.get('NextHopId') is not None:
            self.next_hop_id = m.get('NextHopId')
        if m.get('NextHopType') is not None:
            self.next_hop_type = m.get('NextHopType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RouteType') is not None:
            self.route_type = m.get('RouteType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        if m.get('VpdRouteEntryId') is not None:
            self.vpd_route_entry_id = m.get('VpdRouteEntryId')
        return self


class ListVpdRouteEntriesResponseBodyContentData(TeaModel):
    def __init__(
        self,
        destination_cidr_block: str = None,
        gmt_modified: str = None,
        next_hop_id: str = None,
        next_hop_type: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_tenant_id: str = None,
        route_type: str = None,
        status: str = None,
        tenant_id: str = None,
        vpd_id: str = None,
        vpd_route_entry_id: str = None,
    ):
        # Destination CIDR block
        self.destination_cidr_block = destination_cidr_block
        # The time when the cluster was updated.
        self.gmt_modified = gmt_modified
        # Next Hop Instance
        self.next_hop_id = next_hop_id
        # Next Hop Instance Type
        self.next_hop_type = next_hop_type
        # The region ID.
        self.region_id = region_id
        # Resource group instance ID
        self.resource_group_id = resource_group_id
        # The ID of the tenant to which the resource belongs.
        self.resource_tenant_id = resource_tenant_id
        # Route type
        self.route_type = route_type
        # The status of the intervention entry. Valid value:
        self.status = status
        # The ID of the tenant.
        self.tenant_id = tenant_id
        # Lingjun CIDR block instance ID
        self.vpd_id = vpd_id
        # The ID of the route entry.
        self.vpd_route_entry_id = vpd_route_entry_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.next_hop_id is not None:
            result['NextHopId'] = self.next_hop_id
        if self.next_hop_type is not None:
            result['NextHopType'] = self.next_hop_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_tenant_id is not None:
            result['ResourceTenantId'] = self.resource_tenant_id
        if self.route_type is not None:
            result['RouteType'] = self.route_type
        if self.status is not None:
            result['Status'] = self.status
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        if self.vpd_route_entry_id is not None:
            result['VpdRouteEntryId'] = self.vpd_route_entry_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('NextHopId') is not None:
            self.next_hop_id = m.get('NextHopId')
        if m.get('NextHopType') is not None:
            self.next_hop_type = m.get('NextHopType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceTenantId') is not None:
            self.resource_tenant_id = m.get('ResourceTenantId')
        if m.get('RouteType') is not None:
            self.route_type = m.get('RouteType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        if m.get('VpdRouteEntryId') is not None:
            self.vpd_route_entry_id = m.get('VpdRouteEntryId')
        return self


class ListVpdRouteEntriesResponseBodyContent(TeaModel):
    def __init__(
        self,
        data: List[ListVpdRouteEntriesResponseBodyContentData] = None,
        total: int = None,
    ):
        # Lingjun CIDR block route entry list
        self.data = data
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListVpdRouteEntriesResponseBodyContentData()
                self.data.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListVpdRouteEntriesResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: ListVpdRouteEntriesResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The response parameters.
        self.content = content
        # The error message. (If the instance is in the Exception state, the exception cause is prompted.)
        self.message = message
        # Request ID of the current request
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListVpdRouteEntriesResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListVpdRouteEntriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListVpdRouteEntriesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListVpdRouteEntriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVpdsRequestTag(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListVpdsRequest(TeaModel):
    def __init__(
        self,
        enable_page: bool = None,
        filter_er_id: str = None,
        for_select: bool = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        status: str = None,
        tag: List[ListVpdsRequestTag] = None,
        vpd_id: str = None,
        vpd_name: str = None,
        with_dependence: bool = None,
        without_vcc: bool = None,
    ):
        # Specifies whether to enable paged query.
        self.enable_page = enable_page
        # Queries the network segments of Lingjun that are not bound to a specified Lingjun HUB.
        self.filter_er_id = filter_er_id
        # If you select a drop-down list, only the basic information (including the instance ID and instance name) is returned. Possible values:
        # 
        # *   **true**: Select Query Use from the drop-down list.
        # *   **false**: Normal queries are used.
        self.for_select = for_select
        # The page number of the page to return. Start value: 1 Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID.
        # 
        # For more information about resource groups, see [Resource groups](https://help.aliyun.com/document_detail/94475.htm?spm=a2c4g.11186623.0.0.29e15d7akXhpuu).
        self.resource_group_id = resource_group_id
        # The status of the CLB instance. Valid values:
        # 
        # *   **Available**: Normal.
        # *   **Not Available**: Not available.
        # *   **Executing**: The task is being executed.
        # *   **Deleting**: The account is being deleted
        self.status = status
        # The tag information.
        # 
        # You can specify up to 20 tags.
        self.tag = tag
        # The ID of the VPD instance.
        self.vpd_id = vpd_id
        # The name of the VPD instance.
        self.vpd_name = vpd_name
        # Specifies whether to include the dependent resource information. We recommend that you do not query the dependent resource information when you query by page. You can query the dependent resource information separately when you delete it. Possible values:
        # 
        # *   **true**: with dependency information.
        # *   **false**: does not include dependency information.
        self.with_dependence = with_dependence
        # Queries the information about a Lingjun CIDR block that is not bound to a Lingjun connection. Possible values:
        # 
        # *   **true**: filters out VPDs that have been bound to VCC
        # *   **false**: does not filter VPD that has been bound to VCC
        self.without_vcc = without_vcc

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_page is not None:
            result['EnablePage'] = self.enable_page
        if self.filter_er_id is not None:
            result['FilterErId'] = self.filter_er_id
        if self.for_select is not None:
            result['ForSelect'] = self.for_select
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.status is not None:
            result['Status'] = self.status
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        if self.vpd_name is not None:
            result['VpdName'] = self.vpd_name
        if self.with_dependence is not None:
            result['WithDependence'] = self.with_dependence
        if self.without_vcc is not None:
            result['WithoutVcc'] = self.without_vcc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnablePage') is not None:
            self.enable_page = m.get('EnablePage')
        if m.get('FilterErId') is not None:
            self.filter_er_id = m.get('FilterErId')
        if m.get('ForSelect') is not None:
            self.for_select = m.get('ForSelect')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListVpdsRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        if m.get('VpdName') is not None:
            self.vpd_name = m.get('VpdName')
        if m.get('WithDependence') is not None:
            self.with_dependence = m.get('WithDependence')
        if m.get('WithoutVcc') is not None:
            self.without_vcc = m.get('WithoutVcc')
        return self


class ListVpdsResponseBodyContentDataErInfos(TeaModel):
    def __init__(
        self,
        connections: int = None,
        create_time: str = None,
        description: str = None,
        er_id: str = None,
        er_name: str = None,
        gmt_modified: str = None,
        master_zone_id: str = None,
        message: str = None,
        region_id: str = None,
        route_maps: int = None,
        status: str = None,
        tenant_id: str = None,
    ):
        # The number of connections.
        self.connections = connections
        # The time when the activation code was created.
        self.create_time = create_time
        # The description of the synchronization task.
        self.description = description
        # The ID of the Elastic Router (ER) instance.
        self.er_id = er_id
        # The name of the Lingjun HUB(ER) instance.
        self.er_name = er_name
        # The time when the O\\&M task was modified.
        self.gmt_modified = gmt_modified
        # The primary zone.
        self.master_zone_id = master_zone_id
        # The returned message.
        self.message = message
        # The supported region.
        self.region_id = region_id
        # The number of routing policy.
        self.route_maps = route_maps
        # The task status.
        self.status = status
        # The tenant ID.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connections is not None:
            result['Connections'] = self.connections
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.er_id is not None:
            result['ErId'] = self.er_id
        if self.er_name is not None:
            result['ErName'] = self.er_name
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.master_zone_id is not None:
            result['MasterZoneId'] = self.master_zone_id
        if self.message is not None:
            result['Message'] = self.message
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.route_maps is not None:
            result['RouteMaps'] = self.route_maps
        if self.status is not None:
            result['Status'] = self.status
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Connections') is not None:
            self.connections = m.get('Connections')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')
        if m.get('ErName') is not None:
            self.er_name = m.get('ErName')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('MasterZoneId') is not None:
            self.master_zone_id = m.get('MasterZoneId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RouteMaps') is not None:
            self.route_maps = m.get('RouteMaps')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class ListVpdsResponseBodyContentDataTags(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListVpdsResponseBodyContentData(TeaModel):
    def __init__(
        self,
        cidr: str = None,
        create_time: str = None,
        dependence: Dict[str, Any] = None,
        er_infos: List[ListVpdsResponseBodyContentDataErInfos] = None,
        gmt_modified: str = None,
        message: str = None,
        nc_count: int = None,
        network_interface_count: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        secondary_cidr_blocks: List[str] = None,
        service_cidr: str = None,
        status: str = None,
        subnet_count: int = None,
        tags: List[ListVpdsResponseBodyContentDataTags] = None,
        tenant_id: str = None,
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
        # Dependencies.
        self.dependence = dependence
        # The information list of the bound Lingjun HUB(ER).
        self.er_infos = er_infos
        # The time when the O\\&M task was modified.
        self.gmt_modified = gmt_modified
        # The returned message.
        self.message = message
        # nc quantity.
        self.nc_count = nc_count
        # Number of Lingjun network interface controller
        self.network_interface_count = network_interface_count
        # The region ID.
        self.region_id = region_id
        # The ID of your Alibaba Cloud resource group.
        # 
        # For more information about resource groups, see [Resource groups](https://help.aliyun.com/document_detail/94475.htm?spm=a2c4g.11186623.0.0.29e15d7akXhpuu).
        self.resource_group_id = resource_group_id
        # The list of additional CIDR blocks.
        self.secondary_cidr_blocks = secondary_cidr_blocks
        # The Service CIDR block.
        self.service_cidr = service_cidr
        # The task status.
        self.status = status
        # The number of subnets.
        self.subnet_count = subnet_count
        # The tag information.
        # 
        # You can specify up to 20 tags.
        self.tags = tags
        # The tenant ID.
        self.tenant_id = tenant_id
        # The ID of the VPD instance.
        self.vpd_id = vpd_id
        # The name of the VPD.
        self.vpd_name = vpd_name

    def validate(self):
        if self.er_infos:
            for k in self.er_infos:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr is not None:
            result['Cidr'] = self.cidr
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dependence is not None:
            result['Dependence'] = self.dependence
        result['ErInfos'] = []
        if self.er_infos is not None:
            for k in self.er_infos:
                result['ErInfos'].append(k.to_map() if k else None)
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.message is not None:
            result['Message'] = self.message
        if self.nc_count is not None:
            result['NcCount'] = self.nc_count
        if self.network_interface_count is not None:
            result['NetworkInterfaceCount'] = self.network_interface_count
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.secondary_cidr_blocks is not None:
            result['SecondaryCidrBlocks'] = self.secondary_cidr_blocks
        if self.service_cidr is not None:
            result['ServiceCidr'] = self.service_cidr
        if self.status is not None:
            result['Status'] = self.status
        if self.subnet_count is not None:
            result['SubnetCount'] = self.subnet_count
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
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
        if m.get('Dependence') is not None:
            self.dependence = m.get('Dependence')
        self.er_infos = []
        if m.get('ErInfos') is not None:
            for k in m.get('ErInfos'):
                temp_model = ListVpdsResponseBodyContentDataErInfos()
                self.er_infos.append(temp_model.from_map(k))
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NcCount') is not None:
            self.nc_count = m.get('NcCount')
        if m.get('NetworkInterfaceCount') is not None:
            self.network_interface_count = m.get('NetworkInterfaceCount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecondaryCidrBlocks') is not None:
            self.secondary_cidr_blocks = m.get('SecondaryCidrBlocks')
        if m.get('ServiceCidr') is not None:
            self.service_cidr = m.get('ServiceCidr')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubnetCount') is not None:
            self.subnet_count = m.get('SubnetCount')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListVpdsResponseBodyContentDataTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        if m.get('VpdName') is not None:
            self.vpd_name = m.get('VpdName')
        return self


class ListVpdsResponseBodyContent(TeaModel):
    def __init__(
        self,
        data: List[ListVpdsResponseBodyContentData] = None,
        total: int = None,
    ):
        # The returned data.
        self.data = data
        # The total number of entries that are returned.
        self.total = total

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListVpdsResponseBodyContentData()
                self.data.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListVpdsResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: ListVpdsResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The response data.
        self.content = content
        # The additional information that is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListVpdsResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListVpdsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListVpdsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListVpdsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryInstanceNcdRequest(TeaModel):
    def __init__(
        self,
        instance_id_1: str = None,
        instance_id_2: str = None,
        instance_type: str = None,
        region_id: str = None,
    ):
        # Instance 1ID
        # 
        # This parameter is required.
        self.instance_id_1 = instance_id_1
        # Instance 2ID
        # 
        # This parameter is required.
        self.instance_id_2 = instance_id_2
        # The parameter that specifies the instance type.
        # 
        # Valid value:
        # 
        # *   node: Lingjun node.
        # *   lni: lingjun network interface controller.
        # 
        # This parameter is required.
        self.instance_type = instance_type
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id_1 is not None:
            result['InstanceId1'] = self.instance_id_1
        if self.instance_id_2 is not None:
            result['InstanceId2'] = self.instance_id_2
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId1') is not None:
            self.instance_id_1 = m.get('InstanceId1')
        if m.get('InstanceId2') is not None:
            self.instance_id_2 = m.get('InstanceId2')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class QueryInstanceNcdResponseBodyContent(TeaModel):
    def __init__(
        self,
        instance_id_1: str = None,
        instance_id_2: str = None,
        instance_type: str = None,
        ncd: int = None,
    ):
        # Instance 1ID
        self.instance_id_1 = instance_id_1
        # Instance 2ID
        self.instance_id_2 = instance_id_2
        # Instance Type
        # 
        # Valid value:
        # 
        # *   node: Lingjun node.
        # *   lni: lingjun network interface controller.
        self.instance_type = instance_type
        # network communication distance between instances
        self.ncd = ncd

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id_1 is not None:
            result['InstanceId1'] = self.instance_id_1
        if self.instance_id_2 is not None:
            result['InstanceId2'] = self.instance_id_2
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.ncd is not None:
            result['Ncd'] = self.ncd
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId1') is not None:
            self.instance_id_1 = m.get('InstanceId1')
        if m.get('InstanceId2') is not None:
            self.instance_id_2 = m.get('InstanceId2')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Ncd') is not None:
            self.ncd = m.get('Ncd')
        return self


class QueryInstanceNcdResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: QueryInstanceNcdResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The response parameters.
        self.content = content
        # The returned message.
        self.message = message
        # Request ID of the current request
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = QueryInstanceNcdResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryInstanceNcdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryInstanceNcdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryInstanceNcdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefundVccRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        vcc_id: str = None,
    ):
        # Region
        self.region_id = region_id
        # Lingjun Connection ID
        self.vcc_id = vcc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vcc_id is not None:
            result['VccId'] = self.vcc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VccId') is not None:
            self.vcc_id = m.get('VccId')
        return self


class RefundVccResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: Any = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        # 
        # >  This parameter is returned only if Resource Access Management (RAM) permission verification failed.
        self.access_denied_detail = access_denied_detail
        # The response status code
        self.code = code
        # Response content
        self.content = content
        # Response message, which is \\"success\\" if the request succeeds
        self.message = message
        # Request ID of the current request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.content is not None:
            result['Content'] = self.content
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
            self.content = m.get('Content')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RefundVccResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RefundVccResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RefundVccResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RetryVccRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        vcc_id: str = None,
    ):
        # The region ID.
        self.region_id = region_id
        # Lingjun Connection ID
        self.vcc_id = vcc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vcc_id is not None:
            result['VccId'] = self.vcc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VccId') is not None:
            self.vcc_id = m.get('VccId')
        return self


class RetryVccResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: Any = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The returned data.
        self.content = content
        # The error message.
        self.message = message
        # Request ID of the current request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.content is not None:
            result['Content'] = self.content
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
            self.content = m.get('Content')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RetryVccResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RetryVccResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RetryVccResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnAssignPrivateIpAddressRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        ip_name: str = None,
        network_interface_id: str = None,
        private_ip_address: str = None,
        region_id: str = None,
        subnet_id: str = None,
    ):
        # By default, popApi is not ignored and idempotent
        self.client_token = client_token
        # IP unique identifier
        # 
        # This parameter is required.
        self.ip_name = ip_name
        # Lingjun network interface controller ID
        # 
        # This parameter is required.
        self.network_interface_id = network_interface_id
        # The private IP address of the instance.
        self.private_ip_address = private_ip_address
        # Region
        # 
        # This parameter is required.
        self.region_id = region_id
        # Subnet
        # 
        # This parameter is required.
        self.subnet_id = subnet_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.ip_name is not None:
            result['IpName'] = self.ip_name
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.subnet_id is not None:
            result['SubnetId'] = self.subnet_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('IpName') is not None:
            self.ip_name = m.get('IpName')
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SubnetId') is not None:
            self.subnet_id = m.get('SubnetId')
        return self


class UnAssignPrivateIpAddressResponseBodyContent(TeaModel):
    def __init__(
        self,
        ip_name: str = None,
        network_interface_id: str = None,
    ):
        # IP unique identifier
        self.ip_name = ip_name
        # Lingjun network interface controller ID
        self.network_interface_id = network_interface_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_name is not None:
            result['IpName'] = self.ip_name
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpName') is not None:
            self.ip_name = m.get('IpName')
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')
        return self


class UnAssignPrivateIpAddressResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: UnAssignPrivateIpAddressResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The response parameters.
        self.content = content
        # The error message. (If the instance is in the Exception state, the exception cause is prompted.)
        self.message = message
        # Request ID of the current request
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = UnAssignPrivateIpAddressResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UnAssignPrivateIpAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnAssignPrivateIpAddressResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UnAssignPrivateIpAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnAssociateVpdCidrBlockRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        secondary_cidr_block: str = None,
        vpd_id: str = None,
    ):
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The additional CIDR block.
        # 
        # This parameter is required.
        self.secondary_cidr_block = secondary_cidr_block
        # The ID of the Lingjun CIDR block.
        # 
        # This parameter is required.
        self.vpd_id = vpd_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.secondary_cidr_block is not None:
            result['SecondaryCidrBlock'] = self.secondary_cidr_block
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecondaryCidrBlock') is not None:
            self.secondary_cidr_block = m.get('SecondaryCidrBlock')
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        return self


class UnAssociateVpdCidrBlockResponseBodyContent(TeaModel):
    def __init__(
        self,
        vpd_id: str = None,
    ):
        # The ID of the Lingjun CIDR block.
        self.vpd_id = vpd_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        return self


class UnAssociateVpdCidrBlockResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: UnAssociateVpdCidrBlockResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # 访问被拒绝详细信息。
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The response data.
        self.content = content
        # The error message. (If the instance is in the Exception state, the exception cause is prompted.)
        self.message = message
        # Request ID of the current request
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = UnAssociateVpdCidrBlockResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UnAssociateVpdCidrBlockResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnAssociateVpdCidrBlockResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UnAssociateVpdCidrBlockResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnassignLeniPrivateIpAddressRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        elastic_network_interface_id: str = None,
        ip_name: str = None,
        region_id: str = None,
    ):
        # The idempotent identifier.
        self.client_token = client_token
        # Lingjun Elastic Network Interface ID.
        # 
        # This parameter is required.
        self.elastic_network_interface_id = elastic_network_interface_id
        # Lingjun Elastic Network Interface secondary private IP unique identifier.
        # 
        # This parameter is required.
        self.ip_name = ip_name
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.elastic_network_interface_id is not None:
            result['ElasticNetworkInterfaceId'] = self.elastic_network_interface_id
        if self.ip_name is not None:
            result['IpName'] = self.ip_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ElasticNetworkInterfaceId') is not None:
            self.elastic_network_interface_id = m.get('ElasticNetworkInterfaceId')
        if m.get('IpName') is not None:
            self.ip_name = m.get('IpName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UnassignLeniPrivateIpAddressResponseBodyContent(TeaModel):
    def __init__(
        self,
        elastic_network_interface_id: str = None,
        ip_name: str = None,
    ):
        # Lingjun Elastic Network Interface ID.
        self.elastic_network_interface_id = elastic_network_interface_id
        # Lingjun Elastic Network Interface secondary private IP unique identifier.
        self.ip_name = ip_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.elastic_network_interface_id is not None:
            result['ElasticNetworkInterfaceId'] = self.elastic_network_interface_id
        if self.ip_name is not None:
            result['IpName'] = self.ip_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ElasticNetworkInterfaceId') is not None:
            self.elastic_network_interface_id = m.get('ElasticNetworkInterfaceId')
        if m.get('IpName') is not None:
            self.ip_name = m.get('IpName')
        return self


class UnassignLeniPrivateIpAddressResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: UnassignLeniPrivateIpAddressResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The response data.
        self.content = content
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = UnassignLeniPrivateIpAddressResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UnassignLeniPrivateIpAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnassignLeniPrivateIpAddressResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UnassignLeniPrivateIpAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateElasticNetworkInterfaceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        elastic_network_interface_id: str = None,
        region_id: str = None,
        security_group_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The description of the variable.
        self.description = description
        # Lingjun Elastic Network Interface ID
        # 
        # This parameter is required.
        self.elastic_network_interface_id = elastic_network_interface_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the security group.
        self.security_group_id = security_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.elastic_network_interface_id is not None:
            result['ElasticNetworkInterfaceId'] = self.elastic_network_interface_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ElasticNetworkInterfaceId') is not None:
            self.elastic_network_interface_id = m.get('ElasticNetworkInterfaceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        return self


class UpdateElasticNetworkInterfaceResponseBodyContent(TeaModel):
    def __init__(
        self,
        elastic_network_interface_id: str = None,
        node_id: str = None,
    ):
        # Lingjun Elastic Network Interface ID
        self.elastic_network_interface_id = elastic_network_interface_id
        # Lingjun Node ID
        self.node_id = node_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.elastic_network_interface_id is not None:
            result['ElasticNetworkInterfaceId'] = self.elastic_network_interface_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ElasticNetworkInterfaceId') is not None:
            self.elastic_network_interface_id = m.get('ElasticNetworkInterfaceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class UpdateElasticNetworkInterfaceResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: UpdateElasticNetworkInterfaceResponseBodyContent = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = UpdateElasticNetworkInterfaceResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateElasticNetworkInterfaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateElasticNetworkInterfaceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateElasticNetworkInterfaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateErRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        er_id: str = None,
        er_name: str = None,
        region_id: str = None,
    ):
        # The description of the document.
        self.description = description
        # Lingjun HUB Instance ID
        # 
        # This parameter is required.
        self.er_id = er_id
        # Parameter
        self.er_name = er_name
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.er_id is not None:
            result['ErId'] = self.er_id
        if self.er_name is not None:
            result['ErName'] = self.er_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')
        if m.get('ErName') is not None:
            self.er_name = m.get('ErName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateErResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: Dict[str, Any] = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The returned data.
        self.content = content
        # The error message. (If the instance is in the Exception state, the exception cause is prompted.)
        self.message = message
        # Request ID of the current request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.content is not None:
            result['Content'] = self.content
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
            self.content = m.get('Content')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateErResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateErResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateErResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateErAttachmentRequest(TeaModel):
    def __init__(
        self,
        er_attachment_id: str = None,
        er_attachment_name: str = None,
        er_id: str = None,
        region_id: str = None,
    ):
        # The connection ID of the Lingjun HUB network instance.
        # 
        # This parameter is required.
        self.er_attachment_id = er_attachment_id
        # Lingjun HUB Network Instance Connection Name
        self.er_attachment_name = er_attachment_name
        # Lingjun HUB ID
        # 
        # This parameter is required.
        self.er_id = er_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.er_attachment_id is not None:
            result['ErAttachmentId'] = self.er_attachment_id
        if self.er_attachment_name is not None:
            result['ErAttachmentName'] = self.er_attachment_name
        if self.er_id is not None:
            result['ErId'] = self.er_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErAttachmentId') is not None:
            self.er_attachment_id = m.get('ErAttachmentId')
        if m.get('ErAttachmentName') is not None:
            self.er_attachment_name = m.get('ErAttachmentName')
        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateErAttachmentResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: Dict[str, Any] = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The response parameters.
        self.content = content
        # The error message. (If the instance is in the Exception state, the exception cause is prompted.)
        self.message = message
        # Request ID of the current request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.content is not None:
            result['Content'] = self.content
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
            self.content = m.get('Content')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateErAttachmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateErAttachmentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateErAttachmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateErRouteMapRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        er_id: str = None,
        er_route_map_id: str = None,
        region_id: str = None,
    ):
        # The description of the document.
        self.description = description
        # Lingjun HUB ID
        # 
        # This parameter is required.
        self.er_id = er_id
        # routing policy ID
        # 
        # This parameter is required.
        self.er_route_map_id = er_route_map_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.er_id is not None:
            result['ErId'] = self.er_id
        if self.er_route_map_id is not None:
            result['ErRouteMapId'] = self.er_route_map_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')
        if m.get('ErRouteMapId') is not None:
            self.er_route_map_id = m.get('ErRouteMapId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateErRouteMapResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: Dict[str, Any] = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The response parameters.
        self.content = content
        # The error message. (If the instance is in the Exception state, the exception cause is prompted.)
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.content is not None:
            result['Content'] = self.content
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
            self.content = m.get('Content')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateErRouteMapResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateErRouteMapResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateErRouteMapResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLeniPrivateIpAddressRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        elastic_network_interface_id: str = None,
        ip_name: str = None,
        region_id: str = None,
    ):
        # The description of the ECS instances.
        # 
        # This parameter is required.
        self.description = description
        # Lingjun Elastic Network Interface ID.
        # 
        # This parameter is required.
        self.elastic_network_interface_id = elastic_network_interface_id
        # Lingjun Elastic Network Interface secondary private IP unique identifier.
        # 
        # This parameter is required.
        self.ip_name = ip_name
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.elastic_network_interface_id is not None:
            result['ElasticNetworkInterfaceId'] = self.elastic_network_interface_id
        if self.ip_name is not None:
            result['IpName'] = self.ip_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ElasticNetworkInterfaceId') is not None:
            self.elastic_network_interface_id = m.get('ElasticNetworkInterfaceId')
        if m.get('IpName') is not None:
            self.ip_name = m.get('IpName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateLeniPrivateIpAddressResponseBodyContent(TeaModel):
    def __init__(
        self,
        elastic_network_interface_id: str = None,
        ip_name: str = None,
    ):
        # Lingjun Elastic Network Interface ID.
        self.elastic_network_interface_id = elastic_network_interface_id
        # Lingjun Elastic Network Interface secondary private IP unique identifier.
        self.ip_name = ip_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.elastic_network_interface_id is not None:
            result['ElasticNetworkInterfaceId'] = self.elastic_network_interface_id
        if self.ip_name is not None:
            result['IpName'] = self.ip_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ElasticNetworkInterfaceId') is not None:
            self.elastic_network_interface_id = m.get('ElasticNetworkInterfaceId')
        if m.get('IpName') is not None:
            self.ip_name = m.get('IpName')
        return self


class UpdateLeniPrivateIpAddressResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: UpdateLeniPrivateIpAddressResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The response data.
        self.content = content
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = UpdateLeniPrivateIpAddressResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateLeniPrivateIpAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateLeniPrivateIpAddressResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateLeniPrivateIpAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSubnetRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        subnet_id: str = None,
        subnet_name: str = None,
        vpd_id: str = None,
        zone_id: str = None,
    ):
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The subnet instance ID.
        # 
        # This parameter is required.
        self.subnet_id = subnet_id
        # The new name for the subnet instance.
        self.subnet_name = subnet_name
        # The ID of the VPD to which the subnet belongs.
        # 
        # This parameter is required.
        self.vpd_id = vpd_id
        # The zone ID.
        # 
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.subnet_id is not None:
            result['SubnetId'] = self.subnet_id
        if self.subnet_name is not None:
            result['SubnetName'] = self.subnet_name
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SubnetId') is not None:
            self.subnet_id = m.get('SubnetId')
        if m.get('SubnetName') is not None:
            self.subnet_name = m.get('SubnetName')
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class UpdateSubnetResponseBodyContent(TeaModel):
    def __init__(
        self,
        subnet_id: str = None,
    ):
        # The subnet instance ID.
        self.subnet_id = subnet_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.subnet_id is not None:
            result['SubnetId'] = self.subnet_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubnetId') is not None:
            self.subnet_id = m.get('SubnetId')
        return self


class UpdateSubnetResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: UpdateSubnetResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The response content.
        self.content = content
        # The message that is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = UpdateSubnetResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateSubnetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateSubnetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateSubnetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateVccRequest(TeaModel):
    def __init__(
        self,
        bandwidth: int = None,
        order_id: str = None,
        region_id: str = None,
        vcc_id: str = None,
        vcc_name: str = None,
    ):
        # The peak bandwidth of the Lingjun connection instance. Unit: Mbit/s. Valid values: 1000 to 400000
        self.bandwidth = bandwidth
        # The ID of the order placed on the instance.
        self.order_id = order_id
        # The region ID.
        self.region_id = region_id
        # The ID of the Lingjun connection instance.
        # 
        # This parameter is required.
        self.vcc_id = vcc_id
        # The name of the Lingjun connection instance.
        self.vcc_name = vcc_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vcc_id is not None:
            result['VccId'] = self.vcc_id
        if self.vcc_name is not None:
            result['VccName'] = self.vcc_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VccId') is not None:
            self.vcc_id = m.get('VccId')
        if m.get('VccName') is not None:
            self.vcc_name = m.get('VccName')
        return self


class UpdateVccResponseBodyContent(TeaModel):
    def __init__(
        self,
        vcc_id: str = None,
    ):
        # The ID of the Lingjun connection instance.
        self.vcc_id = vcc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vcc_id is not None:
            result['VccId'] = self.vcc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VccId') is not None:
            self.vcc_id = m.get('VccId')
        return self


class UpdateVccResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: UpdateVccResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The response parameters.
        self.content = content
        # The error message. (If the instance is in the Exception state, the exception cause is prompted.)
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = UpdateVccResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateVccResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateVccResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateVccResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateVpdRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        vpd_id: str = None,
        vpd_name: str = None,
    ):
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the VPD instance.
        # 
        # This parameter is required.
        self.vpd_id = vpd_id
        # The name of the VPD instance.
        self.vpd_name = vpd_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        if self.vpd_name is not None:
            result['VpdName'] = self.vpd_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        if m.get('VpdName') is not None:
            self.vpd_name = m.get('VpdName')
        return self


class UpdateVpdResponseBodyContent(TeaModel):
    def __init__(
        self,
        vpd_id: str = None,
    ):
        # The ID of the VPD instance.
        self.vpd_id = vpd_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        return self


class UpdateVpdResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: UpdateVpdResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The response data.
        self.content = content
        # The additional information that is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = UpdateVpdResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateVpdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateVpdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateVpdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


