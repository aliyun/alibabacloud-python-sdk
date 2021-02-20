# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AddNetworkInterfaceToInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        networks: str = None,
    ):
        self.instance_id = instance_id
        self.networks = networks

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.networks is not None:
            result['Networks'] = self.networks
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Networks') is not None:
            self.networks = m.get('Networks')
        return self


class AddNetworkInterfaceToInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddNetworkInterfaceToInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddNetworkInterfaceToInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddNetworkInterfaceToInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AllocateEipAddressRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
        ens_region_id: str = None,
        count: int = None,
        min_count: int = None,
    ):
        self.version = version
        self.ens_region_id = ens_region_id
        self.count = count
        self.min_count = min_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.count is not None:
            result['Count'] = self.count
        if self.min_count is not None:
            result['MinCount'] = self.min_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('MinCount') is not None:
            self.min_count = m.get('MinCount')
        return self


class AllocateEipAddressResponseBodyEipAddressesEipAddress(TeaModel):
    def __init__(
        self,
        eip: str = None,
    ):
        self.eip = eip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.eip is not None:
            result['Eip'] = self.eip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Eip') is not None:
            self.eip = m.get('Eip')
        return self


class AllocateEipAddressResponseBodyEipAddresses(TeaModel):
    def __init__(
        self,
        eip_address: List[AllocateEipAddressResponseBodyEipAddressesEipAddress] = None,
    ):
        self.eip_address = eip_address

    def validate(self):
        if self.eip_address:
            for k in self.eip_address:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['EipAddress'] = []
        if self.eip_address is not None:
            for k in self.eip_address:
                result['EipAddress'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.eip_address = []
        if m.get('EipAddress') is not None:
            for k in m.get('EipAddress'):
                temp_model = AllocateEipAddressResponseBodyEipAddressesEipAddress()
                self.eip_address.append(temp_model.from_map(k))
        return self


class AllocateEipAddressResponseBody(TeaModel):
    def __init__(
        self,
        biz_status_code: str = None,
        eip_addresses: AllocateEipAddressResponseBodyEipAddresses = None,
        request_id: str = None,
    ):
        self.biz_status_code = biz_status_code
        self.eip_addresses = eip_addresses
        self.request_id = request_id

    def validate(self):
        if self.eip_addresses:
            self.eip_addresses.validate()

    def to_map(self):
        result = dict()
        if self.biz_status_code is not None:
            result['BizStatusCode'] = self.biz_status_code
        if self.eip_addresses is not None:
            result['EipAddresses'] = self.eip_addresses.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizStatusCode') is not None:
            self.biz_status_code = m.get('BizStatusCode')
        if m.get('EipAddresses') is not None:
            temp_model = AllocateEipAddressResponseBodyEipAddresses()
            self.eip_addresses = temp_model.from_map(m['EipAddresses'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AllocateEipAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AllocateEipAddressResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AllocateEipAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociateEipAddressRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
        ens_region_id: str = None,
        eip: str = None,
        instance_id_internet_ip: str = None,
    ):
        self.version = version
        self.ens_region_id = ens_region_id
        self.eip = eip
        self.instance_id_internet_ip = instance_id_internet_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.eip is not None:
            result['Eip'] = self.eip
        if self.instance_id_internet_ip is not None:
            result['InstanceIdInternetIp'] = self.instance_id_internet_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('Eip') is not None:
            self.eip = m.get('Eip')
        if m.get('InstanceIdInternetIp') is not None:
            self.instance_id_internet_ip = m.get('InstanceIdInternetIp')
        return self


class AssociateEipAddressResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AssociateEipAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AssociateEipAddressResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AssociateEipAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachEnsInstancesRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
        instance_id: str = None,
        scripts: str = None,
    ):
        self.version = version
        self.instance_id = instance_id
        self.scripts = scripts

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.scripts is not None:
            result['Scripts'] = self.scripts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Scripts') is not None:
            self.scripts = m.get('Scripts')
        return self


class AttachEnsInstancesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AttachEnsInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AttachEnsInstancesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AttachEnsInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AuthorizeSecurityGroupRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
        ip_protocol: str = None,
        port_range: str = None,
        security_group_id: str = None,
        policy: str = None,
        priority: int = None,
        source_cidr_ip: str = None,
        source_port_range: str = None,
    ):
        self.version = version
        self.ip_protocol = ip_protocol
        self.port_range = port_range
        self.security_group_id = security_group_id
        self.policy = policy
        self.priority = priority
        self.source_cidr_ip = source_cidr_ip
        self.source_port_range = source_port_range

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol
        if self.port_range is not None:
            result['PortRange'] = self.port_range
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.source_cidr_ip is not None:
            result['SourceCidrIp'] = self.source_cidr_ip
        if self.source_port_range is not None:
            result['SourcePortRange'] = self.source_port_range
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')
        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('SourceCidrIp') is not None:
            self.source_cidr_ip = m.get('SourceCidrIp')
        if m.get('SourcePortRange') is not None:
            self.source_port_range = m.get('SourcePortRange')
        return self


class AuthorizeSecurityGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AuthorizeSecurityGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AuthorizeSecurityGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AuthorizeSecurityGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AuthorizeSecurityGroupEgressRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
        ip_protocol: str = None,
        port_range: str = None,
        security_group_id: str = None,
        policy: str = None,
        priority: int = None,
        dest_cidr_ip: str = None,
        source_port_range: str = None,
    ):
        self.version = version
        self.ip_protocol = ip_protocol
        self.port_range = port_range
        self.security_group_id = security_group_id
        self.policy = policy
        self.priority = priority
        self.dest_cidr_ip = dest_cidr_ip
        self.source_port_range = source_port_range

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol
        if self.port_range is not None:
            result['PortRange'] = self.port_range
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.dest_cidr_ip is not None:
            result['DestCidrIp'] = self.dest_cidr_ip
        if self.source_port_range is not None:
            result['SourcePortRange'] = self.source_port_range
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')
        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('DestCidrIp') is not None:
            self.dest_cidr_ip = m.get('DestCidrIp')
        if m.get('SourcePortRange') is not None:
            self.source_port_range = m.get('SourcePortRange')
        return self


class AuthorizeSecurityGroupEgressResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AuthorizeSecurityGroupEgressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AuthorizeSecurityGroupEgressResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AuthorizeSecurityGroupEgressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckQuotaRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        resource_attribute: str = None,
        group_uuid: str = None,
    ):
        self.ali_uid = ali_uid
        self.resource_attribute = resource_attribute
        self.group_uuid = group_uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.resource_attribute is not None:
            result['ResourceAttribute'] = self.resource_attribute
        if self.group_uuid is not None:
            result['GroupUuid'] = self.group_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('ResourceAttribute') is not None:
            self.resource_attribute = m.get('ResourceAttribute')
        if m.get('GroupUuid') is not None:
            self.group_uuid = m.get('GroupUuid')
        return self


class CheckQuotaResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: int = None,
        data: str = None,
        msg: str = None,
        desc: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.code = code
        self.data = data
        self.msg = msg
        self.desc = desc

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.desc is not None:
            result['Desc'] = self.desc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        return self


class CheckQuotaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CheckQuotaResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CheckQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateApplicationRequest(TeaModel):
    def __init__(
        self,
        template: str = None,
        timeout: int = None,
    ):
        self.template = template
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.template is not None:
            result['Template'] = self.template
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        return self


class CreateApplicationResponseBody(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_id: str = None,
    ):
        self.app_id = app_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateApplicationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEnsServiceRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
        ens_service_id: str = None,
        order_type: str = None,
    ):
        self.version = version
        self.ens_service_id = ens_service_id
        self.order_type = order_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.ens_service_id is not None:
            result['EnsServiceId'] = self.ens_service_id
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('EnsServiceId') is not None:
            self.ens_service_id = m.get('EnsServiceId')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        return self


class CreateEnsServiceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        request_id: str = None,
    ):
        self.code = code
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateEnsServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateEnsServiceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateEnsServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEPInstanceRequest(TeaModel):
    def __init__(
        self,
        epninstance_type: str = None,
        epninstance_name: str = None,
        internet_charge_type: str = None,
        networking_model: str = None,
        internet_max_bandwidth_out: int = None,
    ):
        self.epninstance_type = epninstance_type
        self.epninstance_name = epninstance_name
        self.internet_charge_type = internet_charge_type
        self.networking_model = networking_model
        self.internet_max_bandwidth_out = internet_max_bandwidth_out

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.epninstance_type is not None:
            result['EPNInstanceType'] = self.epninstance_type
        if self.epninstance_name is not None:
            result['EPNInstanceName'] = self.epninstance_name
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.networking_model is not None:
            result['NetworkingModel'] = self.networking_model
        if self.internet_max_bandwidth_out is not None:
            result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EPNInstanceType') is not None:
            self.epninstance_type = m.get('EPNInstanceType')
        if m.get('EPNInstanceName') is not None:
            self.epninstance_name = m.get('EPNInstanceName')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('NetworkingModel') is not None:
            self.networking_model = m.get('NetworkingModel')
        if m.get('InternetMaxBandwidthOut') is not None:
            self.internet_max_bandwidth_out = m.get('InternetMaxBandwidthOut')
        return self


class CreateEPInstanceResponseBody(TeaModel):
    def __init__(
        self,
        epninstance_id: str = None,
        request_id: str = None,
    ):
        self.epninstance_id = epninstance_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.epninstance_id is not None:
            result['EPNInstanceId'] = self.epninstance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EPNInstanceId') is not None:
            self.epninstance_id = m.get('EPNInstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateEPInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateEPInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateEPInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEpnInstanceRequest(TeaModel):
    def __init__(
        self,
        epninstance_type: str = None,
        epninstance_name: str = None,
        internet_charge_type: str = None,
        networking_model: str = None,
        internet_max_bandwidth_out: int = None,
    ):
        self.epninstance_type = epninstance_type
        self.epninstance_name = epninstance_name
        self.internet_charge_type = internet_charge_type
        self.networking_model = networking_model
        self.internet_max_bandwidth_out = internet_max_bandwidth_out

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.epninstance_type is not None:
            result['EPNInstanceType'] = self.epninstance_type
        if self.epninstance_name is not None:
            result['EPNInstanceName'] = self.epninstance_name
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.networking_model is not None:
            result['NetworkingModel'] = self.networking_model
        if self.internet_max_bandwidth_out is not None:
            result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EPNInstanceType') is not None:
            self.epninstance_type = m.get('EPNInstanceType')
        if m.get('EPNInstanceName') is not None:
            self.epninstance_name = m.get('EPNInstanceName')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('NetworkingModel') is not None:
            self.networking_model = m.get('NetworkingModel')
        if m.get('InternetMaxBandwidthOut') is not None:
            self.internet_max_bandwidth_out = m.get('InternetMaxBandwidthOut')
        return self


class CreateEpnInstanceResponseBody(TeaModel):
    def __init__(
        self,
        epninstance_id: str = None,
        request_id: str = None,
    ):
        self.epninstance_id = epninstance_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.epninstance_id is not None:
            result['EPNInstanceId'] = self.epninstance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EPNInstanceId') is not None:
            self.epninstance_id = m.get('EPNInstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateEpnInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateEpnInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateEpnInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateImageRequest(TeaModel):
    def __init__(
        self,
        product: str = None,
        version: str = None,
        instance_id: str = None,
        image_name: str = None,
        delete_after_image_upload: str = None,
    ):
        self.product = product
        self.version = version
        self.instance_id = instance_id
        self.image_name = image_name
        self.delete_after_image_upload = delete_after_image_upload

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.product is not None:
            result['product'] = self.product
        if self.version is not None:
            result['Version'] = self.version
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.delete_after_image_upload is not None:
            result['DeleteAfterImageUpload'] = self.delete_after_image_upload
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('product') is not None:
            self.product = m.get('product')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('DeleteAfterImageUpload') is not None:
            self.delete_after_image_upload = m.get('DeleteAfterImageUpload')
        return self


class CreateImageResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        request_id: str = None,
    ):
        self.code = code
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateImageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateKeyPairRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
        key_pair_name: str = None,
    ):
        self.version = version
        self.key_pair_name = key_pair_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        return self


class CreateKeyPairResponseBody(TeaModel):
    def __init__(
        self,
        key_pair_finger_print: str = None,
        key_pair_id: str = None,
        key_pair_name: str = None,
        private_key_body: str = None,
        request_id: str = None,
    ):
        self.key_pair_finger_print = key_pair_finger_print
        self.key_pair_id = key_pair_id
        self.key_pair_name = key_pair_name
        self.private_key_body = private_key_body
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key_pair_finger_print is not None:
            result['KeyPairFingerPrint'] = self.key_pair_finger_print
        if self.key_pair_id is not None:
            result['KeyPairId'] = self.key_pair_id
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.private_key_body is not None:
            result['PrivateKeyBody'] = self.private_key_body
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyPairFingerPrint') is not None:
            self.key_pair_finger_print = m.get('KeyPairFingerPrint')
        if m.get('KeyPairId') is not None:
            self.key_pair_id = m.get('KeyPairId')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('PrivateKeyBody') is not None:
            self.private_key_body = m.get('PrivateKeyBody')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateKeyPairResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateKeyPairResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateKeyPairResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSecurityGroupRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
        security_group_name: str = None,
    ):
        self.version = version
        self.security_group_name = security_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.security_group_name is not None:
            result['SecurityGroupName'] = self.security_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('SecurityGroupName') is not None:
            self.security_group_name = m.get('SecurityGroupName')
        return self


class CreateSecurityGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        security_group_id: str = None,
    ):
        self.request_id = request_id
        self.security_group_id = security_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        return self


class CreateSecurityGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSecurityGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateSecurityGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVmAndSaveStockRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        tenant: str = None,
        workload_uuid: str = None,
        group_uuid: str = None,
        resource_attribute: str = None,
    ):
        self.ali_uid = ali_uid
        self.tenant = tenant
        self.workload_uuid = workload_uuid
        self.group_uuid = group_uuid
        self.resource_attribute = resource_attribute

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.tenant is not None:
            result['Tenant'] = self.tenant
        if self.workload_uuid is not None:
            result['WorkloadUuid'] = self.workload_uuid
        if self.group_uuid is not None:
            result['GroupUuid'] = self.group_uuid
        if self.resource_attribute is not None:
            result['ResourceAttribute'] = self.resource_attribute
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('Tenant') is not None:
            self.tenant = m.get('Tenant')
        if m.get('WorkloadUuid') is not None:
            self.workload_uuid = m.get('WorkloadUuid')
        if m.get('GroupUuid') is not None:
            self.group_uuid = m.get('GroupUuid')
        if m.get('ResourceAttribute') is not None:
            self.resource_attribute = m.get('ResourceAttribute')
        return self


class CreateVmAndSaveStockResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: int = None,
        msg: str = None,
        desc: str = None,
        data: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.code = code
        self.msg = msg
        self.desc = desc
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class CreateVmAndSaveStockResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateVmAndSaveStockResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateVmAndSaveStockResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVSwitchRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
        ens_region_id: str = None,
        cidr_block: str = None,
        v_switch_name: str = None,
    ):
        self.version = version
        self.ens_region_id = ens_region_id
        self.cidr_block = cidr_block
        self.v_switch_name = v_switch_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block
        if self.v_switch_name is not None:
            result['VSwitchName'] = self.v_switch_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')
        if m.get('VSwitchName') is not None:
            self.v_switch_name = m.get('VSwitchName')
        return self


class CreateVSwitchResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        v_switch_id: str = None,
    ):
        self.request_id = request_id
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class CreateVSwitchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateVSwitchResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateVSwitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteApplicationRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        timeout: int = None,
    ):
        self.app_id = app_id
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        return self


class DeleteApplicationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteApplicationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEpnInstanceRequest(TeaModel):
    def __init__(
        self,
        epninstance_id: str = None,
    ):
        self.epninstance_id = epninstance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.epninstance_id is not None:
            result['EPNInstanceId'] = self.epninstance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EPNInstanceId') is not None:
            self.epninstance_id = m.get('EPNInstanceId')
        return self


class DeleteEpnInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteEpnInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteEpnInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteEpnInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteKeyPairsRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
        key_pair_name: str = None,
    ):
        self.version = version
        self.key_pair_name = key_pair_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        return self


class DeleteKeyPairsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteKeyPairsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteKeyPairsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteKeyPairsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSecurityGroupRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
        security_group_id: str = None,
    ):
        self.version = version
        self.security_group_id = security_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        return self


class DeleteSecurityGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteSecurityGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteSecurityGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteSecurityGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVmRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        workload_uuid: str = None,
    ):
        self.ali_uid = ali_uid
        self.workload_uuid = workload_uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.workload_uuid is not None:
            result['WorkloadUuid'] = self.workload_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('WorkloadUuid') is not None:
            self.workload_uuid = m.get('WorkloadUuid')
        return self


class DeleteVmResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        desc: str = None,
        data: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.msg = msg
        self.desc = desc
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteVmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteVmResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteVmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVSwitchRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
        v_switch_id: str = None,
    ):
        self.version = version
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class DeleteVSwitchResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteVSwitchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteVSwitchResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteVSwitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApplicationRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_versions: str = None,
        level: str = None,
        out_detail_stat_params: str = None,
    ):
        self.app_id = app_id
        self.app_versions = app_versions
        self.level = level
        self.out_detail_stat_params = out_detail_stat_params

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_versions is not None:
            result['AppVersions'] = self.app_versions
        if self.level is not None:
            result['Level'] = self.level
        if self.out_detail_stat_params is not None:
            result['OutDetailStatParams'] = self.out_detail_stat_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersions') is not None:
            self.app_versions = m.get('AppVersions')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('OutDetailStatParams') is not None:
            self.out_detail_stat_params = m.get('OutDetailStatParams')
        return self


class DescribeApplicationResponseBody(TeaModel):
    def __init__(
        self,
        application: str = None,
        request_id: str = None,
    ):
        self.application = application
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.application is not None:
            result['Application'] = self.application
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Application') is not None:
            self.application = m.get('Application')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeApplicationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApplicationResourceSummaryRequest(TeaModel):
    def __init__(
        self,
        level: str = None,
        resource_type: str = None,
    ):
        self.level = level
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.level is not None:
            result['Level'] = self.level
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class DescribeApplicationResourceSummaryResponseBody(TeaModel):
    def __init__(
        self,
        application_resource: str = None,
        request_id: str = None,
    ):
        self.application_resource = application_resource
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.application_resource is not None:
            result['ApplicationResource'] = self.application_resource
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationResource') is not None:
            self.application_resource = m.get('ApplicationResource')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeApplicationResourceSummaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeApplicationResourceSummaryResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeApplicationResourceSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAvailableResourceRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
    ):
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeAvailableResourceResponseBodyImagesImage(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        image_name: str = None,
    ):
        self.image_id = image_id
        self.image_name = image_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        return self


class DescribeAvailableResourceResponseBodyImages(TeaModel):
    def __init__(
        self,
        image: List[DescribeAvailableResourceResponseBodyImagesImage] = None,
    ):
        self.image = image

    def validate(self):
        if self.image:
            for k in self.image:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Image'] = []
        if self.image is not None:
            for k in self.image:
                result['Image'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.image = []
        if m.get('Image') is not None:
            for k in m.get('Image'):
                temp_model = DescribeAvailableResourceResponseBodyImagesImage()
                self.image.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceResponseBodySupportResourcesSupportResource(TeaModel):
    def __init__(
        self,
        data_disk_size: str = None,
        ens_region_id: str = None,
        instance_spec: str = None,
        support_resources_count: str = None,
        system_disk_size: str = None,
    ):
        self.data_disk_size = data_disk_size
        self.ens_region_id = ens_region_id
        self.instance_spec = instance_spec
        self.support_resources_count = support_resources_count
        self.system_disk_size = system_disk_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec
        if self.support_resources_count is not None:
            result['SupportResourcesCount'] = self.support_resources_count
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')
        if m.get('SupportResourcesCount') is not None:
            self.support_resources_count = m.get('SupportResourcesCount')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        return self


class DescribeAvailableResourceResponseBodySupportResources(TeaModel):
    def __init__(
        self,
        support_resource: List[DescribeAvailableResourceResponseBodySupportResourcesSupportResource] = None,
    ):
        self.support_resource = support_resource

    def validate(self):
        if self.support_resource:
            for k in self.support_resource:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['SupportResource'] = []
        if self.support_resource is not None:
            for k in self.support_resource:
                result['SupportResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.support_resource = []
        if m.get('SupportResource') is not None:
            for k in m.get('SupportResource'):
                temp_model = DescribeAvailableResourceResponseBodySupportResourcesSupportResource()
                self.support_resource.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        images: DescribeAvailableResourceResponseBodyImages = None,
        request_id: str = None,
        support_resources: DescribeAvailableResourceResponseBodySupportResources = None,
    ):
        self.code = code
        self.images = images
        self.request_id = request_id
        self.support_resources = support_resources

    def validate(self):
        if self.images:
            self.images.validate()
        if self.support_resources:
            self.support_resources.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.images is not None:
            result['Images'] = self.images.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.support_resources is not None:
            result['SupportResources'] = self.support_resources.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Images') is not None:
            temp_model = DescribeAvailableResourceResponseBodyImages()
            self.images = temp_model.from_map(m['Images'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SupportResources') is not None:
            temp_model = DescribeAvailableResourceResponseBodySupportResources()
            self.support_resources = temp_model.from_map(m['SupportResources'])
        return self


class DescribeAvailableResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAvailableResourceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAvailableResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBandwitdhByInternetChargeTypeRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
        start_time: str = None,
        end_time: str = None,
        isp: str = None,
        ens_region_id: str = None,
    ):
        self.version = version
        self.start_time = start_time
        self.end_time = end_time
        self.isp = isp
        self.ens_region_id = ens_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        return self


class DescribeBandwitdhByInternetChargeTypeResponseBody(TeaModel):
    def __init__(
        self,
        bandwidth_value: int = None,
        internet_charge_type: str = None,
        request_id: str = None,
        time_stamp: str = None,
    ):
        self.bandwidth_value = bandwidth_value
        self.internet_charge_type = internet_charge_type
        self.request_id = request_id
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.bandwidth_value is not None:
            result['BandwidthValue'] = self.bandwidth_value
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthValue') is not None:
            self.bandwidth_value = m.get('BandwidthValue')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeBandwitdhByInternetChargeTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeBandwitdhByInternetChargeTypeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeBandwitdhByInternetChargeTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBandWithdChargeTypeRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
    ):
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeBandWithdChargeTypeResponseBody(TeaModel):
    def __init__(
        self,
        band_with_type_info: str = None,
        charge_contract_type: str = None,
        charge_cycle_info: str = None,
        code: int = None,
        request_id: str = None,
    ):
        self.band_with_type_info = band_with_type_info
        self.charge_contract_type = charge_contract_type
        self.charge_cycle_info = charge_cycle_info
        self.code = code
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.band_with_type_info is not None:
            result['BandWithTypeInfo'] = self.band_with_type_info
        if self.charge_contract_type is not None:
            result['ChargeContractType'] = self.charge_contract_type
        if self.charge_cycle_info is not None:
            result['ChargeCycleInfo'] = self.charge_cycle_info
        if self.code is not None:
            result['Code'] = self.code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandWithTypeInfo') is not None:
            self.band_with_type_info = m.get('BandWithTypeInfo')
        if m.get('ChargeContractType') is not None:
            self.charge_contract_type = m.get('ChargeContractType')
        if m.get('ChargeCycleInfo') is not None:
            self.charge_cycle_info = m.get('ChargeCycleInfo')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeBandWithdChargeTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeBandWithdChargeTypeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeBandWithdChargeTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCreatePrePaidInstanceResultRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
        instance_id: str = None,
    ):
        self.version = version
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeCreatePrePaidInstanceResultResponseBodyInstanceCreateResult(TeaModel):
    def __init__(
        self,
        instance_create_status: str = None,
        instance_id: str = None,
    ):
        self.instance_create_status = instance_create_status
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_create_status is not None:
            result['InstanceCreateStatus'] = self.instance_create_status
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceCreateStatus') is not None:
            self.instance_create_status = m.get('InstanceCreateStatus')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeCreatePrePaidInstanceResultResponseBody(TeaModel):
    def __init__(
        self,
        instance_create_result: DescribeCreatePrePaidInstanceResultResponseBodyInstanceCreateResult = None,
        request_id: str = None,
    ):
        self.instance_create_result = instance_create_result
        self.request_id = request_id

    def validate(self):
        if self.instance_create_result:
            self.instance_create_result.validate()

    def to_map(self):
        result = dict()
        if self.instance_create_result is not None:
            result['InstanceCreateResult'] = self.instance_create_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceCreateResult') is not None:
            temp_model = DescribeCreatePrePaidInstanceResultResponseBodyInstanceCreateResult()
            self.instance_create_result = temp_model.from_map(m['InstanceCreateResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCreatePrePaidInstanceResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCreatePrePaidInstanceResultResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCreatePrePaidInstanceResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDataDistResultRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        data_names: str = None,
        data_versions: str = None,
        instance_ids: str = None,
        min_date: str = None,
        max_date: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.app_id = app_id
        self.data_names = data_names
        self.data_versions = data_versions
        self.instance_ids = instance_ids
        self.min_date = min_date
        self.max_date = max_date
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.data_names is not None:
            result['DataNames'] = self.data_names
        if self.data_versions is not None:
            result['DataVersions'] = self.data_versions
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.min_date is not None:
            result['MinDate'] = self.min_date
        if self.max_date is not None:
            result['MaxDate'] = self.max_date
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('DataNames') is not None:
            self.data_names = m.get('DataNames')
        if m.get('DataVersions') is not None:
            self.data_versions = m.get('DataVersions')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('MinDate') is not None:
            self.min_date = m.get('MinDate')
        if m.get('MaxDate') is not None:
            self.max_date = m.get('MaxDate')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeDataDistResultResponseBodyDistResultsDistResultStatusStatsStatusStatInstancesInstance(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        start_time: str = None,
        status_descrip: str = None,
        update_time: str = None,
    ):
        self.instance_id = instance_id
        self.start_time = start_time
        self.status_descrip = status_descrip
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status_descrip is not None:
            result['StatusDescrip'] = self.status_descrip
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StatusDescrip') is not None:
            self.status_descrip = m.get('StatusDescrip')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeDataDistResultResponseBodyDistResultsDistResultStatusStatsStatusStatInstances(TeaModel):
    def __init__(
        self,
        instance: List[DescribeDataDistResultResponseBodyDistResultsDistResultStatusStatsStatusStatInstancesInstance] = None,
    ):
        self.instance = instance

    def validate(self):
        if self.instance:
            for k in self.instance:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Instance'] = []
        if self.instance is not None:
            for k in self.instance:
                result['Instance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance = []
        if m.get('Instance') is not None:
            for k in m.get('Instance'):
                temp_model = DescribeDataDistResultResponseBodyDistResultsDistResultStatusStatsStatusStatInstancesInstance()
                self.instance.append(temp_model.from_map(k))
        return self


class DescribeDataDistResultResponseBodyDistResultsDistResultStatusStatsStatusStat(TeaModel):
    def __init__(
        self,
        instance_count: str = None,
        instances: DescribeDataDistResultResponseBodyDistResultsDistResultStatusStatsStatusStatInstances = None,
        status: str = None,
    ):
        self.instance_count = instance_count
        self.instances = instances
        self.status = status

    def validate(self):
        if self.instances:
            self.instances.validate()

    def to_map(self):
        result = dict()
        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count
        if self.instances is not None:
            result['Instances'] = self.instances.to_map()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')
        if m.get('Instances') is not None:
            temp_model = DescribeDataDistResultResponseBodyDistResultsDistResultStatusStatsStatusStatInstances()
            self.instances = temp_model.from_map(m['Instances'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDataDistResultResponseBodyDistResultsDistResultStatusStats(TeaModel):
    def __init__(
        self,
        status_stat: List[DescribeDataDistResultResponseBodyDistResultsDistResultStatusStatsStatusStat] = None,
    ):
        self.status_stat = status_stat

    def validate(self):
        if self.status_stat:
            for k in self.status_stat:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['StatusStat'] = []
        if self.status_stat is not None:
            for k in self.status_stat:
                result['StatusStat'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.status_stat = []
        if m.get('StatusStat') is not None:
            for k in m.get('StatusStat'):
                temp_model = DescribeDataDistResultResponseBodyDistResultsDistResultStatusStatsStatusStat()
                self.status_stat.append(temp_model.from_map(k))
        return self


class DescribeDataDistResultResponseBodyDistResultsDistResult(TeaModel):
    def __init__(
        self,
        name: str = None,
        status_stats: DescribeDataDistResultResponseBodyDistResultsDistResultStatusStats = None,
        version: str = None,
    ):
        self.name = name
        self.status_stats = status_stats
        self.version = version

    def validate(self):
        if self.status_stats:
            self.status_stats.validate()

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.status_stats is not None:
            result['StatusStats'] = self.status_stats.to_map()
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('StatusStats') is not None:
            temp_model = DescribeDataDistResultResponseBodyDistResultsDistResultStatusStats()
            self.status_stats = temp_model.from_map(m['StatusStats'])
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeDataDistResultResponseBodyDistResults(TeaModel):
    def __init__(
        self,
        dist_result: List[DescribeDataDistResultResponseBodyDistResultsDistResult] = None,
    ):
        self.dist_result = dist_result

    def validate(self):
        if self.dist_result:
            for k in self.dist_result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['DistResult'] = []
        if self.dist_result is not None:
            for k in self.dist_result:
                result['DistResult'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dist_result = []
        if m.get('DistResult') is not None:
            for k in m.get('DistResult'):
                temp_model = DescribeDataDistResultResponseBodyDistResultsDistResult()
                self.dist_result.append(temp_model.from_map(k))
        return self


class DescribeDataDistResultResponseBody(TeaModel):
    def __init__(
        self,
        dist_results: DescribeDataDistResultResponseBodyDistResults = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.dist_results = dist_results
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.dist_results:
            self.dist_results.validate()

    def to_map(self):
        result = dict()
        if self.dist_results is not None:
            result['DistResults'] = self.dist_results.to_map()
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
        if m.get('DistResults') is not None:
            temp_model = DescribeDataDistResultResponseBodyDistResults()
            self.dist_results = temp_model.from_map(m['DistResults'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDataDistResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDataDistResultResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDataDistResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDataPushResultRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        data_names: str = None,
        data_versions: str = None,
        min_date: str = None,
        max_date: str = None,
        page_number: int = None,
        page_size: int = None,
        region_ids: str = None,
    ):
        self.app_id = app_id
        self.data_names = data_names
        self.data_versions = data_versions
        self.min_date = min_date
        self.max_date = max_date
        self.page_number = page_number
        self.page_size = page_size
        self.region_ids = region_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.data_names is not None:
            result['DataNames'] = self.data_names
        if self.data_versions is not None:
            result['DataVersions'] = self.data_versions
        if self.min_date is not None:
            result['MinDate'] = self.min_date
        if self.max_date is not None:
            result['MaxDate'] = self.max_date
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('DataNames') is not None:
            self.data_names = m.get('DataNames')
        if m.get('DataVersions') is not None:
            self.data_versions = m.get('DataVersions')
        if m.get('MinDate') is not None:
            self.min_date = m.get('MinDate')
        if m.get('MaxDate') is not None:
            self.max_date = m.get('MaxDate')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionIds') is not None:
            self.region_ids = m.get('RegionIds')
        return self


class DescribeDataPushResultResponseBodyPushResultsPushResultStatusStatSStatusStatRegionIdsRegionId(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        start_time: str = None,
        status_descrip: str = None,
        update_time: str = None,
    ):
        self.region_id = region_id
        self.start_time = start_time
        self.status_descrip = status_descrip
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status_descrip is not None:
            result['StatusDescrip'] = self.status_descrip
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StatusDescrip') is not None:
            self.status_descrip = m.get('StatusDescrip')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeDataPushResultResponseBodyPushResultsPushResultStatusStatSStatusStatRegionIds(TeaModel):
    def __init__(
        self,
        region_id: List[DescribeDataPushResultResponseBodyPushResultsPushResultStatusStatSStatusStatRegionIdsRegionId] = None,
    ):
        self.region_id = region_id

    def validate(self):
        if self.region_id:
            for k in self.region_id:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['RegionId'] = []
        if self.region_id is not None:
            for k in self.region_id:
                result['RegionId'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region_id = []
        if m.get('RegionId') is not None:
            for k in m.get('RegionId'):
                temp_model = DescribeDataPushResultResponseBodyPushResultsPushResultStatusStatSStatusStatRegionIdsRegionId()
                self.region_id.append(temp_model.from_map(k))
        return self


class DescribeDataPushResultResponseBodyPushResultsPushResultStatusStatSStatusStat(TeaModel):
    def __init__(
        self,
        region_id_count: int = None,
        region_ids: DescribeDataPushResultResponseBodyPushResultsPushResultStatusStatSStatusStatRegionIds = None,
        status: str = None,
    ):
        self.region_id_count = region_id_count
        self.region_ids = region_ids
        self.status = status

    def validate(self):
        if self.region_ids:
            self.region_ids.validate()

    def to_map(self):
        result = dict()
        if self.region_id_count is not None:
            result['RegionIdCount'] = self.region_id_count
        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids.to_map()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionIdCount') is not None:
            self.region_id_count = m.get('RegionIdCount')
        if m.get('RegionIds') is not None:
            temp_model = DescribeDataPushResultResponseBodyPushResultsPushResultStatusStatSStatusStatRegionIds()
            self.region_ids = temp_model.from_map(m['RegionIds'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDataPushResultResponseBodyPushResultsPushResultStatusStatS(TeaModel):
    def __init__(
        self,
        status_stat: List[DescribeDataPushResultResponseBodyPushResultsPushResultStatusStatSStatusStat] = None,
    ):
        self.status_stat = status_stat

    def validate(self):
        if self.status_stat:
            for k in self.status_stat:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['StatusStat'] = []
        if self.status_stat is not None:
            for k in self.status_stat:
                result['StatusStat'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.status_stat = []
        if m.get('StatusStat') is not None:
            for k in m.get('StatusStat'):
                temp_model = DescribeDataPushResultResponseBodyPushResultsPushResultStatusStatSStatusStat()
                self.status_stat.append(temp_model.from_map(k))
        return self


class DescribeDataPushResultResponseBodyPushResultsPushResult(TeaModel):
    def __init__(
        self,
        name: str = None,
        status_stat_s: DescribeDataPushResultResponseBodyPushResultsPushResultStatusStatS = None,
        version: str = None,
    ):
        self.name = name
        self.status_stat_s = status_stat_s
        self.version = version

    def validate(self):
        if self.status_stat_s:
            self.status_stat_s.validate()

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.status_stat_s is not None:
            result['StatusStatS'] = self.status_stat_s.to_map()
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('StatusStatS') is not None:
            temp_model = DescribeDataPushResultResponseBodyPushResultsPushResultStatusStatS()
            self.status_stat_s = temp_model.from_map(m['StatusStatS'])
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeDataPushResultResponseBodyPushResults(TeaModel):
    def __init__(
        self,
        push_result: List[DescribeDataPushResultResponseBodyPushResultsPushResult] = None,
    ):
        self.push_result = push_result

    def validate(self):
        if self.push_result:
            for k in self.push_result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['PushResult'] = []
        if self.push_result is not None:
            for k in self.push_result:
                result['PushResult'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.push_result = []
        if m.get('PushResult') is not None:
            for k in m.get('PushResult'):
                temp_model = DescribeDataPushResultResponseBodyPushResultsPushResult()
                self.push_result.append(temp_model.from_map(k))
        return self


class DescribeDataPushResultResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        push_results: DescribeDataPushResultResponseBodyPushResults = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.push_results = push_results
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.push_results:
            self.push_results.validate()

    def to_map(self):
        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.push_results is not None:
            result['PushResults'] = self.push_results.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PushResults') is not None:
            temp_model = DescribeDataPushResultResponseBodyPushResults()
            self.push_results = temp_model.from_map(m['PushResults'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDataPushResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDataPushResultResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDataPushResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEipAddressesRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
        ens_region_id: str = None,
        eips: str = None,
    ):
        self.version = version
        self.ens_region_id = ens_region_id
        self.eips = eips

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.eips is not None:
            result['Eips'] = self.eips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('Eips') is not None:
            self.eips = m.get('Eips')
        return self


class DescribeEipAddressesResponseBodyEipAddressesEipAddress(TeaModel):
    def __init__(
        self,
        eip: str = None,
        instance_id_internet_ip: str = None,
    ):
        self.eip = eip
        self.instance_id_internet_ip = instance_id_internet_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.eip is not None:
            result['Eip'] = self.eip
        if self.instance_id_internet_ip is not None:
            result['InstanceIdInternetIp'] = self.instance_id_internet_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Eip') is not None:
            self.eip = m.get('Eip')
        if m.get('InstanceIdInternetIp') is not None:
            self.instance_id_internet_ip = m.get('InstanceIdInternetIp')
        return self


class DescribeEipAddressesResponseBodyEipAddresses(TeaModel):
    def __init__(
        self,
        eip_address: List[DescribeEipAddressesResponseBodyEipAddressesEipAddress] = None,
    ):
        self.eip_address = eip_address

    def validate(self):
        if self.eip_address:
            for k in self.eip_address:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['EipAddress'] = []
        if self.eip_address is not None:
            for k in self.eip_address:
                result['EipAddress'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.eip_address = []
        if m.get('EipAddress') is not None:
            for k in m.get('EipAddress'):
                temp_model = DescribeEipAddressesResponseBodyEipAddressesEipAddress()
                self.eip_address.append(temp_model.from_map(k))
        return self


class DescribeEipAddressesResponseBody(TeaModel):
    def __init__(
        self,
        eip_addresses: DescribeEipAddressesResponseBodyEipAddresses = None,
        request_id: str = None,
    ):
        self.eip_addresses = eip_addresses
        self.request_id = request_id

    def validate(self):
        if self.eip_addresses:
            self.eip_addresses.validate()

    def to_map(self):
        result = dict()
        if self.eip_addresses is not None:
            result['EipAddresses'] = self.eip_addresses.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EipAddresses') is not None:
            temp_model = DescribeEipAddressesResponseBodyEipAddresses()
            self.eip_addresses = temp_model.from_map(m['EipAddresses'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeEipAddressesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeEipAddressesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeEipAddressesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEnsNetDistrictRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
        net_level_code: str = None,
        net_district_code: str = None,
    ):
        self.version = version
        self.net_level_code = net_level_code
        self.net_district_code = net_district_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.net_level_code is not None:
            result['NetLevelCode'] = self.net_level_code
        if self.net_district_code is not None:
            result['NetDistrictCode'] = self.net_district_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('NetLevelCode') is not None:
            self.net_level_code = m.get('NetLevelCode')
        if m.get('NetDistrictCode') is not None:
            self.net_district_code = m.get('NetDistrictCode')
        return self


class DescribeEnsNetDistrictResponseBodyEnsNetDistrictsEnsNetDistrict(TeaModel):
    def __init__(
        self,
        ens_region_id_count: str = None,
        net_district_code: str = None,
        net_district_en_name: str = None,
        net_district_father_code: str = None,
        net_district_level: str = None,
        net_district_name: str = None,
    ):
        self.ens_region_id_count = ens_region_id_count
        self.net_district_code = net_district_code
        self.net_district_en_name = net_district_en_name
        self.net_district_father_code = net_district_father_code
        self.net_district_level = net_district_level
        self.net_district_name = net_district_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ens_region_id_count is not None:
            result['EnsRegionIdCount'] = self.ens_region_id_count
        if self.net_district_code is not None:
            result['NetDistrictCode'] = self.net_district_code
        if self.net_district_en_name is not None:
            result['NetDistrictEnName'] = self.net_district_en_name
        if self.net_district_father_code is not None:
            result['NetDistrictFatherCode'] = self.net_district_father_code
        if self.net_district_level is not None:
            result['NetDistrictLevel'] = self.net_district_level
        if self.net_district_name is not None:
            result['NetDistrictName'] = self.net_district_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnsRegionIdCount') is not None:
            self.ens_region_id_count = m.get('EnsRegionIdCount')
        if m.get('NetDistrictCode') is not None:
            self.net_district_code = m.get('NetDistrictCode')
        if m.get('NetDistrictEnName') is not None:
            self.net_district_en_name = m.get('NetDistrictEnName')
        if m.get('NetDistrictFatherCode') is not None:
            self.net_district_father_code = m.get('NetDistrictFatherCode')
        if m.get('NetDistrictLevel') is not None:
            self.net_district_level = m.get('NetDistrictLevel')
        if m.get('NetDistrictName') is not None:
            self.net_district_name = m.get('NetDistrictName')
        return self


class DescribeEnsNetDistrictResponseBodyEnsNetDistricts(TeaModel):
    def __init__(
        self,
        ens_net_district: List[DescribeEnsNetDistrictResponseBodyEnsNetDistrictsEnsNetDistrict] = None,
    ):
        self.ens_net_district = ens_net_district

    def validate(self):
        if self.ens_net_district:
            for k in self.ens_net_district:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['EnsNetDistrict'] = []
        if self.ens_net_district is not None:
            for k in self.ens_net_district:
                result['EnsNetDistrict'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ens_net_district = []
        if m.get('EnsNetDistrict') is not None:
            for k in m.get('EnsNetDistrict'):
                temp_model = DescribeEnsNetDistrictResponseBodyEnsNetDistrictsEnsNetDistrict()
                self.ens_net_district.append(temp_model.from_map(k))
        return self


class DescribeEnsNetDistrictResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        ens_net_districts: DescribeEnsNetDistrictResponseBodyEnsNetDistricts = None,
        request_id: str = None,
    ):
        self.code = code
        self.ens_net_districts = ens_net_districts
        self.request_id = request_id

    def validate(self):
        if self.ens_net_districts:
            self.ens_net_districts.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.ens_net_districts is not None:
            result['EnsNetDistricts'] = self.ens_net_districts.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('EnsNetDistricts') is not None:
            temp_model = DescribeEnsNetDistrictResponseBodyEnsNetDistricts()
            self.ens_net_districts = temp_model.from_map(m['EnsNetDistricts'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeEnsNetDistrictResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeEnsNetDistrictResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeEnsNetDistrictResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEnsNetLevelRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
    ):
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeEnsNetLevelResponseBodyEnsNetLevelsEnsNetLevel(TeaModel):
    def __init__(
        self,
        ens_net_level_code: str = None,
    ):
        self.ens_net_level_code = ens_net_level_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ens_net_level_code is not None:
            result['EnsNetLevelCode'] = self.ens_net_level_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnsNetLevelCode') is not None:
            self.ens_net_level_code = m.get('EnsNetLevelCode')
        return self


class DescribeEnsNetLevelResponseBodyEnsNetLevels(TeaModel):
    def __init__(
        self,
        ens_net_level: List[DescribeEnsNetLevelResponseBodyEnsNetLevelsEnsNetLevel] = None,
    ):
        self.ens_net_level = ens_net_level

    def validate(self):
        if self.ens_net_level:
            for k in self.ens_net_level:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['EnsNetLevel'] = []
        if self.ens_net_level is not None:
            for k in self.ens_net_level:
                result['EnsNetLevel'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ens_net_level = []
        if m.get('EnsNetLevel') is not None:
            for k in m.get('EnsNetLevel'):
                temp_model = DescribeEnsNetLevelResponseBodyEnsNetLevelsEnsNetLevel()
                self.ens_net_level.append(temp_model.from_map(k))
        return self


class DescribeEnsNetLevelResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        ens_net_levels: DescribeEnsNetLevelResponseBodyEnsNetLevels = None,
        request_id: str = None,
    ):
        self.code = code
        self.ens_net_levels = ens_net_levels
        self.request_id = request_id

    def validate(self):
        if self.ens_net_levels:
            self.ens_net_levels.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.ens_net_levels is not None:
            result['EnsNetLevels'] = self.ens_net_levels.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('EnsNetLevels') is not None:
            temp_model = DescribeEnsNetLevelResponseBodyEnsNetLevels()
            self.ens_net_levels = temp_model.from_map(m['EnsNetLevels'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeEnsNetLevelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeEnsNetLevelResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeEnsNetLevelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEnsNetSaleDistrictRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
        net_level_code: str = None,
        net_district_code: str = None,
    ):
        self.version = version
        self.net_level_code = net_level_code
        self.net_district_code = net_district_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.net_level_code is not None:
            result['NetLevelCode'] = self.net_level_code
        if self.net_district_code is not None:
            result['NetDistrictCode'] = self.net_district_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('NetLevelCode') is not None:
            self.net_level_code = m.get('NetLevelCode')
        if m.get('NetDistrictCode') is not None:
            self.net_district_code = m.get('NetDistrictCode')
        return self


class DescribeEnsNetSaleDistrictResponseBodyEnsNetDistrictsEnsNetDistrict(TeaModel):
    def __init__(
        self,
        ens_region_id_count: str = None,
        instance_count: str = None,
        net_district_code: str = None,
        net_district_en_name: str = None,
        net_district_father_code: str = None,
        net_district_level: str = None,
        net_district_name: str = None,
    ):
        self.ens_region_id_count = ens_region_id_count
        self.instance_count = instance_count
        self.net_district_code = net_district_code
        self.net_district_en_name = net_district_en_name
        self.net_district_father_code = net_district_father_code
        self.net_district_level = net_district_level
        self.net_district_name = net_district_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ens_region_id_count is not None:
            result['EnsRegionIdCount'] = self.ens_region_id_count
        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count
        if self.net_district_code is not None:
            result['NetDistrictCode'] = self.net_district_code
        if self.net_district_en_name is not None:
            result['NetDistrictEnName'] = self.net_district_en_name
        if self.net_district_father_code is not None:
            result['NetDistrictFatherCode'] = self.net_district_father_code
        if self.net_district_level is not None:
            result['NetDistrictLevel'] = self.net_district_level
        if self.net_district_name is not None:
            result['NetDistrictName'] = self.net_district_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnsRegionIdCount') is not None:
            self.ens_region_id_count = m.get('EnsRegionIdCount')
        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')
        if m.get('NetDistrictCode') is not None:
            self.net_district_code = m.get('NetDistrictCode')
        if m.get('NetDistrictEnName') is not None:
            self.net_district_en_name = m.get('NetDistrictEnName')
        if m.get('NetDistrictFatherCode') is not None:
            self.net_district_father_code = m.get('NetDistrictFatherCode')
        if m.get('NetDistrictLevel') is not None:
            self.net_district_level = m.get('NetDistrictLevel')
        if m.get('NetDistrictName') is not None:
            self.net_district_name = m.get('NetDistrictName')
        return self


class DescribeEnsNetSaleDistrictResponseBodyEnsNetDistricts(TeaModel):
    def __init__(
        self,
        ens_net_district: List[DescribeEnsNetSaleDistrictResponseBodyEnsNetDistrictsEnsNetDistrict] = None,
    ):
        self.ens_net_district = ens_net_district

    def validate(self):
        if self.ens_net_district:
            for k in self.ens_net_district:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['EnsNetDistrict'] = []
        if self.ens_net_district is not None:
            for k in self.ens_net_district:
                result['EnsNetDistrict'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ens_net_district = []
        if m.get('EnsNetDistrict') is not None:
            for k in m.get('EnsNetDistrict'):
                temp_model = DescribeEnsNetSaleDistrictResponseBodyEnsNetDistrictsEnsNetDistrict()
                self.ens_net_district.append(temp_model.from_map(k))
        return self


class DescribeEnsNetSaleDistrictResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        ens_net_districts: DescribeEnsNetSaleDistrictResponseBodyEnsNetDistricts = None,
        request_id: str = None,
    ):
        self.code = code
        self.ens_net_districts = ens_net_districts
        self.request_id = request_id

    def validate(self):
        if self.ens_net_districts:
            self.ens_net_districts.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.ens_net_districts is not None:
            result['EnsNetDistricts'] = self.ens_net_districts.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('EnsNetDistricts') is not None:
            temp_model = DescribeEnsNetSaleDistrictResponseBodyEnsNetDistricts()
            self.ens_net_districts = temp_model.from_map(m['EnsNetDistricts'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeEnsNetSaleDistrictResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeEnsNetSaleDistrictResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeEnsNetSaleDistrictResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEnsRegionIdIpv6InfoRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
        ens_region_id: str = None,
    ):
        self.version = version
        self.ens_region_id = ens_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        return self


class DescribeEnsRegionIdIpv6InfoResponseBodySupportIpv6Info(TeaModel):
    def __init__(
        self,
        ens_region_id: str = None,
        support_ipv_6: bool = None,
    ):
        self.ens_region_id = ens_region_id
        self.support_ipv_6 = support_ipv_6

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.support_ipv_6 is not None:
            result['SupportIpv6'] = self.support_ipv_6
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('SupportIpv6') is not None:
            self.support_ipv_6 = m.get('SupportIpv6')
        return self


class DescribeEnsRegionIdIpv6InfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        support_ipv_6info: DescribeEnsRegionIdIpv6InfoResponseBodySupportIpv6Info = None,
    ):
        self.request_id = request_id
        self.support_ipv_6info = support_ipv_6info

    def validate(self):
        if self.support_ipv_6info:
            self.support_ipv_6info.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.support_ipv_6info is not None:
            result['SupportIpv6Info'] = self.support_ipv_6info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SupportIpv6Info') is not None:
            temp_model = DescribeEnsRegionIdIpv6InfoResponseBodySupportIpv6Info()
            self.support_ipv_6info = temp_model.from_map(m['SupportIpv6Info'])
        return self


class DescribeEnsRegionIdIpv6InfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeEnsRegionIdIpv6InfoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeEnsRegionIdIpv6InfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEnsRegionIdResourceRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
        start_time: str = None,
        end_time: str = None,
        order_by_params: str = None,
        page_number: int = None,
        page_size: str = None,
        isp: str = None,
    ):
        self.version = version
        self.start_time = start_time
        self.end_time = end_time
        self.order_by_params = order_by_params
        self.page_number = page_number
        self.page_size = page_size
        self.isp = isp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.order_by_params is not None:
            result['OrderByParams'] = self.order_by_params
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.isp is not None:
            result['Isp'] = self.isp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OrderByParams') is not None:
            self.order_by_params = m.get('OrderByParams')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        return self


class DescribeEnsRegionIdResourceResponseBodyEnsRegionIdResourcesEnsRegionIdResource(TeaModel):
    def __init__(
        self,
        area: str = None,
        area_code: str = None,
        biz_date: str = None,
        ens_region_id: str = None,
        ens_region_id_name: str = None,
        instance_count: int = None,
        internet_bandwidth: int = None,
        isp: str = None,
        vcpu: int = None,
    ):
        self.area = area
        self.area_code = area_code
        self.biz_date = biz_date
        self.ens_region_id = ens_region_id
        self.ens_region_id_name = ens_region_id_name
        self.instance_count = instance_count
        self.internet_bandwidth = internet_bandwidth
        self.isp = isp
        self.vcpu = vcpu

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.area is not None:
            result['Area'] = self.area
        if self.area_code is not None:
            result['AreaCode'] = self.area_code
        if self.biz_date is not None:
            result['BizDate'] = self.biz_date
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.ens_region_id_name is not None:
            result['EnsRegionIdName'] = self.ens_region_id_name
        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count
        if self.internet_bandwidth is not None:
            result['InternetBandwidth'] = self.internet_bandwidth
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.vcpu is not None:
            result['VCpu'] = self.vcpu
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')
        if m.get('AreaCode') is not None:
            self.area_code = m.get('AreaCode')
        if m.get('BizDate') is not None:
            self.biz_date = m.get('BizDate')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('EnsRegionIdName') is not None:
            self.ens_region_id_name = m.get('EnsRegionIdName')
        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')
        if m.get('InternetBandwidth') is not None:
            self.internet_bandwidth = m.get('InternetBandwidth')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('VCpu') is not None:
            self.vcpu = m.get('VCpu')
        return self


class DescribeEnsRegionIdResourceResponseBodyEnsRegionIdResources(TeaModel):
    def __init__(
        self,
        ens_region_id_resource: List[DescribeEnsRegionIdResourceResponseBodyEnsRegionIdResourcesEnsRegionIdResource] = None,
    ):
        self.ens_region_id_resource = ens_region_id_resource

    def validate(self):
        if self.ens_region_id_resource:
            for k in self.ens_region_id_resource:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['EnsRegionIdResource'] = []
        if self.ens_region_id_resource is not None:
            for k in self.ens_region_id_resource:
                result['EnsRegionIdResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ens_region_id_resource = []
        if m.get('EnsRegionIdResource') is not None:
            for k in m.get('EnsRegionIdResource'):
                temp_model = DescribeEnsRegionIdResourceResponseBodyEnsRegionIdResourcesEnsRegionIdResource()
                self.ens_region_id_resource.append(temp_model.from_map(k))
        return self


class DescribeEnsRegionIdResourceResponseBody(TeaModel):
    def __init__(
        self,
        ens_region_id_resources: DescribeEnsRegionIdResourceResponseBodyEnsRegionIdResources = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.ens_region_id_resources = ens_region_id_resources
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.ens_region_id_resources:
            self.ens_region_id_resources.validate()

    def to_map(self):
        result = dict()
        if self.ens_region_id_resources is not None:
            result['EnsRegionIdResources'] = self.ens_region_id_resources.to_map()
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
        if m.get('EnsRegionIdResources') is not None:
            temp_model = DescribeEnsRegionIdResourceResponseBodyEnsRegionIdResources()
            self.ens_region_id_resources = temp_model.from_map(m['EnsRegionIdResources'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeEnsRegionIdResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeEnsRegionIdResourceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeEnsRegionIdResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEnsRegionsRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
        ens_region_id: str = None,
    ):
        self.version = version
        self.ens_region_id = ens_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        return self


class DescribeEnsRegionsResponseBodyEnsRegionsEnsRegions(TeaModel):
    def __init__(
        self,
        area: str = None,
        en_name: str = None,
        ens_region_id: str = None,
        name: str = None,
        province: str = None,
    ):
        self.area = area
        self.en_name = en_name
        self.ens_region_id = ens_region_id
        self.name = name
        self.province = province

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.area is not None:
            result['Area'] = self.area
        if self.en_name is not None:
            result['EnName'] = self.en_name
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.name is not None:
            result['Name'] = self.name
        if self.province is not None:
            result['Province'] = self.province
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')
        if m.get('EnName') is not None:
            self.en_name = m.get('EnName')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        return self


class DescribeEnsRegionsResponseBodyEnsRegions(TeaModel):
    def __init__(
        self,
        ens_regions: List[DescribeEnsRegionsResponseBodyEnsRegionsEnsRegions] = None,
    ):
        self.ens_regions = ens_regions

    def validate(self):
        if self.ens_regions:
            for k in self.ens_regions:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['EnsRegions'] = []
        if self.ens_regions is not None:
            for k in self.ens_regions:
                result['EnsRegions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ens_regions = []
        if m.get('EnsRegions') is not None:
            for k in m.get('EnsRegions'):
                temp_model = DescribeEnsRegionsResponseBodyEnsRegionsEnsRegions()
                self.ens_regions.append(temp_model.from_map(k))
        return self


class DescribeEnsRegionsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        ens_regions: DescribeEnsRegionsResponseBodyEnsRegions = None,
        request_id: str = None,
    ):
        self.code = code
        self.ens_regions = ens_regions
        self.request_id = request_id

    def validate(self):
        if self.ens_regions:
            self.ens_regions.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.ens_regions is not None:
            result['EnsRegions'] = self.ens_regions.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('EnsRegions') is not None:
            temp_model = DescribeEnsRegionsResponseBodyEnsRegions()
            self.ens_regions = temp_model.from_map(m['EnsRegions'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeEnsRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeEnsRegionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeEnsRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEpnBandWidthDataRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
        ens_region_id: str = None,
        instance_id: str = None,
        start_time: str = None,
        end_time: str = None,
        period: str = None,
        isp: str = None,
        networking_model: str = None,
        epninstance_id: str = None,
    ):
        self.version = version
        self.ens_region_id = ens_region_id
        self.instance_id = instance_id
        self.start_time = start_time
        self.end_time = end_time
        self.period = period
        self.isp = isp
        self.networking_model = networking_model
        self.epninstance_id = epninstance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.period is not None:
            result['Period'] = self.period
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.networking_model is not None:
            result['NetworkingModel'] = self.networking_model
        if self.epninstance_id is not None:
            result['EPNInstanceId'] = self.epninstance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('NetworkingModel') is not None:
            self.networking_model = m.get('NetworkingModel')
        if m.get('EPNInstanceId') is not None:
            self.epninstance_id = m.get('EPNInstanceId')
        return self


class DescribeEpnBandWidthDataResponseBodyMonitorDataBandWidthMonitorData(TeaModel):
    def __init__(
        self,
        down_band_width: int = None,
        internet_rx: int = None,
        internet_tx: int = None,
        time_stamp: str = None,
        up_band_width: int = None,
    ):
        self.down_band_width = down_band_width
        self.internet_rx = internet_rx
        self.internet_tx = internet_tx
        self.time_stamp = time_stamp
        self.up_band_width = up_band_width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.down_band_width is not None:
            result['DownBandWidth'] = self.down_band_width
        if self.internet_rx is not None:
            result['InternetRX'] = self.internet_rx
        if self.internet_tx is not None:
            result['InternetTX'] = self.internet_tx
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.up_band_width is not None:
            result['UpBandWidth'] = self.up_band_width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownBandWidth') is not None:
            self.down_band_width = m.get('DownBandWidth')
        if m.get('InternetRX') is not None:
            self.internet_rx = m.get('InternetRX')
        if m.get('InternetTX') is not None:
            self.internet_tx = m.get('InternetTX')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('UpBandWidth') is not None:
            self.up_band_width = m.get('UpBandWidth')
        return self


class DescribeEpnBandWidthDataResponseBodyMonitorData(TeaModel):
    def __init__(
        self,
        band_width_monitor_data: List[DescribeEpnBandWidthDataResponseBodyMonitorDataBandWidthMonitorData] = None,
        max_down_band_width: int = None,
        max_up_band_width: int = None,
    ):
        self.band_width_monitor_data = band_width_monitor_data
        self.max_down_band_width = max_down_band_width
        self.max_up_band_width = max_up_band_width

    def validate(self):
        if self.band_width_monitor_data:
            for k in self.band_width_monitor_data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['BandWidthMonitorData'] = []
        if self.band_width_monitor_data is not None:
            for k in self.band_width_monitor_data:
                result['BandWidthMonitorData'].append(k.to_map() if k else None)
        if self.max_down_band_width is not None:
            result['MaxDownBandWidth'] = self.max_down_band_width
        if self.max_up_band_width is not None:
            result['MaxUpBandWidth'] = self.max_up_band_width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.band_width_monitor_data = []
        if m.get('BandWidthMonitorData') is not None:
            for k in m.get('BandWidthMonitorData'):
                temp_model = DescribeEpnBandWidthDataResponseBodyMonitorDataBandWidthMonitorData()
                self.band_width_monitor_data.append(temp_model.from_map(k))
        if m.get('MaxDownBandWidth') is not None:
            self.max_down_band_width = m.get('MaxDownBandWidth')
        if m.get('MaxUpBandWidth') is not None:
            self.max_up_band_width = m.get('MaxUpBandWidth')
        return self


class DescribeEpnBandWidthDataResponseBody(TeaModel):
    def __init__(
        self,
        monitor_data: DescribeEpnBandWidthDataResponseBodyMonitorData = None,
        request_id: str = None,
    ):
        self.monitor_data = monitor_data
        self.request_id = request_id

    def validate(self):
        if self.monitor_data:
            self.monitor_data.validate()

    def to_map(self):
        result = dict()
        if self.monitor_data is not None:
            result['MonitorData'] = self.monitor_data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MonitorData') is not None:
            temp_model = DescribeEpnBandWidthDataResponseBodyMonitorData()
            self.monitor_data = temp_model.from_map(m['MonitorData'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeEpnBandWidthDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeEpnBandWidthDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeEpnBandWidthDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEpnBandwitdhByInternetChargeTypeRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
        start_time: str = None,
        end_time: str = None,
        isp: str = None,
        ens_region_id: str = None,
        networking_model: str = None,
    ):
        self.version = version
        self.start_time = start_time
        self.end_time = end_time
        self.isp = isp
        self.ens_region_id = ens_region_id
        self.networking_model = networking_model

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.networking_model is not None:
            result['NetworkingModel'] = self.networking_model
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('NetworkingModel') is not None:
            self.networking_model = m.get('NetworkingModel')
        return self


class DescribeEpnBandwitdhByInternetChargeTypeResponseBody(TeaModel):
    def __init__(
        self,
        bandwidth_value: int = None,
        internet_charge_type: str = None,
        request_id: str = None,
        time_stamp: str = None,
    ):
        self.bandwidth_value = bandwidth_value
        self.internet_charge_type = internet_charge_type
        self.request_id = request_id
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.bandwidth_value is not None:
            result['BandwidthValue'] = self.bandwidth_value
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthValue') is not None:
            self.bandwidth_value = m.get('BandwidthValue')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeEpnBandwitdhByInternetChargeTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeEpnBandwitdhByInternetChargeTypeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeEpnBandwitdhByInternetChargeTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEpnInstanceAttributeRequest(TeaModel):
    def __init__(
        self,
        epninstance_id: str = None,
    ):
        self.epninstance_id = epninstance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.epninstance_id is not None:
            result['EPNInstanceId'] = self.epninstance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EPNInstanceId') is not None:
            self.epninstance_id = m.get('EPNInstanceId')
        return self


class DescribeEpnInstanceAttributeResponseBodyConfVersions(TeaModel):
    def __init__(
        self,
        conf_version: str = None,
        ens_region_id: str = None,
    ):
        self.conf_version = conf_version
        self.ens_region_id = ens_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.conf_version is not None:
            result['ConfVersion'] = self.conf_version
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfVersion') is not None:
            self.conf_version = m.get('ConfVersion')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        return self


class DescribeEpnInstanceAttributeResponseBodyInstances(TeaModel):
    def __init__(
        self,
        ens_region_id: str = None,
        instance_id: str = None,
        instance_name: str = None,
        isp: str = None,
        private_ip_address: str = None,
        public_ip_address: str = None,
        status: str = None,
    ):
        self.ens_region_id = ens_region_id
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.isp = isp
        self.private_ip_address = private_ip_address
        self.public_ip_address = public_ip_address
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        if self.public_ip_address is not None:
            result['PublicIpAddress'] = self.public_ip_address
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        if m.get('PublicIpAddress') is not None:
            self.public_ip_address = m.get('PublicIpAddress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeEpnInstanceAttributeResponseBodyVSwitches(TeaModel):
    def __init__(
        self,
        cidr_block: str = None,
        ens_region_id: str = None,
        v_switch_id: str = None,
        v_switch_name: str = None,
    ):
        self.cidr_block = cidr_block
        self.ens_region_id = ens_region_id
        self.v_switch_id = v_switch_id
        self.v_switch_name = v_switch_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.v_switch_name is not None:
            result['VSwitchName'] = self.v_switch_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VSwitchName') is not None:
            self.v_switch_name = m.get('VSwitchName')
        return self


class DescribeEpnInstanceAttributeResponseBody(TeaModel):
    def __init__(
        self,
        conf_versions: List[DescribeEpnInstanceAttributeResponseBodyConfVersions] = None,
        epninstance_id: str = None,
        epninstance_name: str = None,
        instances: List[DescribeEpnInstanceAttributeResponseBodyInstances] = None,
        networking_model: str = None,
        request_id: str = None,
        v_switches: List[DescribeEpnInstanceAttributeResponseBodyVSwitches] = None,
    ):
        self.conf_versions = conf_versions
        self.epninstance_id = epninstance_id
        self.epninstance_name = epninstance_name
        self.instances = instances
        self.networking_model = networking_model
        self.request_id = request_id
        self.v_switches = v_switches

    def validate(self):
        if self.conf_versions:
            for k in self.conf_versions:
                if k:
                    k.validate()
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()
        if self.v_switches:
            for k in self.v_switches:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ConfVersions'] = []
        if self.conf_versions is not None:
            for k in self.conf_versions:
                result['ConfVersions'].append(k.to_map() if k else None)
        if self.epninstance_id is not None:
            result['EPNInstanceId'] = self.epninstance_id
        if self.epninstance_name is not None:
            result['EPNInstanceName'] = self.epninstance_name
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.networking_model is not None:
            result['NetworkingModel'] = self.networking_model
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['VSwitches'] = []
        if self.v_switches is not None:
            for k in self.v_switches:
                result['VSwitches'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conf_versions = []
        if m.get('ConfVersions') is not None:
            for k in m.get('ConfVersions'):
                temp_model = DescribeEpnInstanceAttributeResponseBodyConfVersions()
                self.conf_versions.append(temp_model.from_map(k))
        if m.get('EPNInstanceId') is not None:
            self.epninstance_id = m.get('EPNInstanceId')
        if m.get('EPNInstanceName') is not None:
            self.epninstance_name = m.get('EPNInstanceName')
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = DescribeEpnInstanceAttributeResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('NetworkingModel') is not None:
            self.networking_model = m.get('NetworkingModel')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.v_switches = []
        if m.get('VSwitches') is not None:
            for k in m.get('VSwitches'):
                temp_model = DescribeEpnInstanceAttributeResponseBodyVSwitches()
                self.v_switches.append(temp_model.from_map(k))
        return self


class DescribeEpnInstanceAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeEpnInstanceAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeEpnInstanceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEpnInstancesRequest(TeaModel):
    def __init__(
        self,
        epninstance_id: str = None,
        epninstance_name: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.epninstance_id = epninstance_id
        self.epninstance_name = epninstance_name
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.epninstance_id is not None:
            result['EPNInstanceId'] = self.epninstance_id
        if self.epninstance_name is not None:
            result['EPNInstanceName'] = self.epninstance_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EPNInstanceId') is not None:
            self.epninstance_id = m.get('EPNInstanceId')
        if m.get('EPNInstanceName') is not None:
            self.epninstance_name = m.get('EPNInstanceName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeEpnInstancesResponseBodyEPNInstancesEPNInstance(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        epninstance_id: str = None,
        epninstance_name: str = None,
        epninstance_type: str = None,
        end_time: str = None,
        internet_max_bandwidth_out: int = None,
        modify_time: str = None,
        networking_model: str = None,
        start_time: str = None,
        status: str = None,
    ):
        self.creation_time = creation_time
        self.epninstance_id = epninstance_id
        self.epninstance_name = epninstance_name
        self.epninstance_type = epninstance_type
        self.end_time = end_time
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        self.modify_time = modify_time
        self.networking_model = networking_model
        self.start_time = start_time
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.epninstance_id is not None:
            result['EPNInstanceId'] = self.epninstance_id
        if self.epninstance_name is not None:
            result['EPNInstanceName'] = self.epninstance_name
        if self.epninstance_type is not None:
            result['EPNInstanceType'] = self.epninstance_type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.internet_max_bandwidth_out is not None:
            result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.networking_model is not None:
            result['NetworkingModel'] = self.networking_model
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('EPNInstanceId') is not None:
            self.epninstance_id = m.get('EPNInstanceId')
        if m.get('EPNInstanceName') is not None:
            self.epninstance_name = m.get('EPNInstanceName')
        if m.get('EPNInstanceType') is not None:
            self.epninstance_type = m.get('EPNInstanceType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InternetMaxBandwidthOut') is not None:
            self.internet_max_bandwidth_out = m.get('InternetMaxBandwidthOut')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('NetworkingModel') is not None:
            self.networking_model = m.get('NetworkingModel')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeEpnInstancesResponseBodyEPNInstances(TeaModel):
    def __init__(
        self,
        epninstance: List[DescribeEpnInstancesResponseBodyEPNInstancesEPNInstance] = None,
    ):
        self.epninstance = epninstance

    def validate(self):
        if self.epninstance:
            for k in self.epninstance:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['EPNInstance'] = []
        if self.epninstance is not None:
            for k in self.epninstance:
                result['EPNInstance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.epninstance = []
        if m.get('EPNInstance') is not None:
            for k in m.get('EPNInstance'):
                temp_model = DescribeEpnInstancesResponseBodyEPNInstancesEPNInstance()
                self.epninstance.append(temp_model.from_map(k))
        return self


class DescribeEpnInstancesResponseBody(TeaModel):
    def __init__(
        self,
        epninstances: DescribeEpnInstancesResponseBodyEPNInstances = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.epninstances = epninstances
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.epninstances:
            self.epninstances.validate()

    def to_map(self):
        result = dict()
        if self.epninstances is not None:
            result['EPNInstances'] = self.epninstances.to_map()
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
        if m.get('EPNInstances') is not None:
            temp_model = DescribeEpnInstancesResponseBodyEPNInstances()
            self.epninstances = temp_model.from_map(m['EPNInstances'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeEpnInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeEpnInstancesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeEpnInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEpnMeasurementDataRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
        start_date: str = None,
        end_date: str = None,
    ):
        self.version = version
        self.start_date = start_date
        self.end_date = end_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class DescribeEpnMeasurementDataResponseBodyMeasurementDatasMeasurementDataBandWidthFeeDatasBandWidthFeeData(TeaModel):
    def __init__(
        self,
        cost_code: str = None,
        cost_name: str = None,
        cost_type: str = None,
        cost_val: int = None,
        isp_line: str = None,
    ):
        self.cost_code = cost_code
        self.cost_name = cost_name
        self.cost_type = cost_type
        self.cost_val = cost_val
        self.isp_line = isp_line

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cost_code is not None:
            result['CostCode'] = self.cost_code
        if self.cost_name is not None:
            result['CostName'] = self.cost_name
        if self.cost_type is not None:
            result['CostType'] = self.cost_type
        if self.cost_val is not None:
            result['CostVal'] = self.cost_val
        if self.isp_line is not None:
            result['IspLine'] = self.isp_line
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostCode') is not None:
            self.cost_code = m.get('CostCode')
        if m.get('CostName') is not None:
            self.cost_name = m.get('CostName')
        if m.get('CostType') is not None:
            self.cost_type = m.get('CostType')
        if m.get('CostVal') is not None:
            self.cost_val = m.get('CostVal')
        if m.get('IspLine') is not None:
            self.isp_line = m.get('IspLine')
        return self


class DescribeEpnMeasurementDataResponseBodyMeasurementDatasMeasurementDataBandWidthFeeDatas(TeaModel):
    def __init__(
        self,
        band_width_fee_data: List[DescribeEpnMeasurementDataResponseBodyMeasurementDatasMeasurementDataBandWidthFeeDatasBandWidthFeeData] = None,
    ):
        self.band_width_fee_data = band_width_fee_data

    def validate(self):
        if self.band_width_fee_data:
            for k in self.band_width_fee_data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['BandWidthFeeData'] = []
        if self.band_width_fee_data is not None:
            for k in self.band_width_fee_data:
                result['BandWidthFeeData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.band_width_fee_data = []
        if m.get('BandWidthFeeData') is not None:
            for k in m.get('BandWidthFeeData'):
                temp_model = DescribeEpnMeasurementDataResponseBodyMeasurementDatasMeasurementDataBandWidthFeeDatasBandWidthFeeData()
                self.band_width_fee_data.append(temp_model.from_map(k))
        return self


class DescribeEpnMeasurementDataResponseBodyMeasurementDatasMeasurementData(TeaModel):
    def __init__(
        self,
        band_width_fee_datas: DescribeEpnMeasurementDataResponseBodyMeasurementDatasMeasurementDataBandWidthFeeDatas = None,
        charge_model: str = None,
        cost_cycle: str = None,
        cost_end_time: str = None,
        cost_start_time: str = None,
    ):
        self.band_width_fee_datas = band_width_fee_datas
        self.charge_model = charge_model
        self.cost_cycle = cost_cycle
        self.cost_end_time = cost_end_time
        self.cost_start_time = cost_start_time

    def validate(self):
        if self.band_width_fee_datas:
            self.band_width_fee_datas.validate()

    def to_map(self):
        result = dict()
        if self.band_width_fee_datas is not None:
            result['BandWidthFeeDatas'] = self.band_width_fee_datas.to_map()
        if self.charge_model is not None:
            result['ChargeModel'] = self.charge_model
        if self.cost_cycle is not None:
            result['CostCycle'] = self.cost_cycle
        if self.cost_end_time is not None:
            result['CostEndTime'] = self.cost_end_time
        if self.cost_start_time is not None:
            result['CostStartTime'] = self.cost_start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandWidthFeeDatas') is not None:
            temp_model = DescribeEpnMeasurementDataResponseBodyMeasurementDatasMeasurementDataBandWidthFeeDatas()
            self.band_width_fee_datas = temp_model.from_map(m['BandWidthFeeDatas'])
        if m.get('ChargeModel') is not None:
            self.charge_model = m.get('ChargeModel')
        if m.get('CostCycle') is not None:
            self.cost_cycle = m.get('CostCycle')
        if m.get('CostEndTime') is not None:
            self.cost_end_time = m.get('CostEndTime')
        if m.get('CostStartTime') is not None:
            self.cost_start_time = m.get('CostStartTime')
        return self


class DescribeEpnMeasurementDataResponseBodyMeasurementDatas(TeaModel):
    def __init__(
        self,
        measurement_data: List[DescribeEpnMeasurementDataResponseBodyMeasurementDatasMeasurementData] = None,
    ):
        self.measurement_data = measurement_data

    def validate(self):
        if self.measurement_data:
            for k in self.measurement_data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['MeasurementData'] = []
        if self.measurement_data is not None:
            for k in self.measurement_data:
                result['MeasurementData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.measurement_data = []
        if m.get('MeasurementData') is not None:
            for k in m.get('MeasurementData'):
                temp_model = DescribeEpnMeasurementDataResponseBodyMeasurementDatasMeasurementData()
                self.measurement_data.append(temp_model.from_map(k))
        return self


class DescribeEpnMeasurementDataResponseBody(TeaModel):
    def __init__(
        self,
        measurement_datas: DescribeEpnMeasurementDataResponseBodyMeasurementDatas = None,
        request_id: str = None,
    ):
        self.measurement_datas = measurement_datas
        self.request_id = request_id

    def validate(self):
        if self.measurement_datas:
            self.measurement_datas.validate()

    def to_map(self):
        result = dict()
        if self.measurement_datas is not None:
            result['MeasurementDatas'] = self.measurement_datas.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MeasurementDatas') is not None:
            temp_model = DescribeEpnMeasurementDataResponseBodyMeasurementDatas()
            self.measurement_datas = temp_model.from_map(m['MeasurementDatas'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeEpnMeasurementDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeEpnMeasurementDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeEpnMeasurementDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeExportImageInfoRequest(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        image_name: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.image_id = image_id
        self.image_name = image_name
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeExportImageInfoResponseBodyImagesImage(TeaModel):
    def __init__(
        self,
        architecture: str = None,
        creation_time: str = None,
        exported_image_url: str = None,
        image_export_status: str = None,
        image_id: str = None,
        image_name: str = None,
        image_owner_alias: str = None,
        platform: str = None,
    ):
        self.architecture = architecture
        self.creation_time = creation_time
        self.exported_image_url = exported_image_url
        self.image_export_status = image_export_status
        self.image_id = image_id
        self.image_name = image_name
        self.image_owner_alias = image_owner_alias
        self.platform = platform

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.architecture is not None:
            result['Architecture'] = self.architecture
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.exported_image_url is not None:
            result['ExportedImageURL'] = self.exported_image_url
        if self.image_export_status is not None:
            result['ImageExportStatus'] = self.image_export_status
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.image_owner_alias is not None:
            result['ImageOwnerAlias'] = self.image_owner_alias
        if self.platform is not None:
            result['Platform'] = self.platform
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('ExportedImageURL') is not None:
            self.exported_image_url = m.get('ExportedImageURL')
        if m.get('ImageExportStatus') is not None:
            self.image_export_status = m.get('ImageExportStatus')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('ImageOwnerAlias') is not None:
            self.image_owner_alias = m.get('ImageOwnerAlias')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        return self


class DescribeExportImageInfoResponseBodyImages(TeaModel):
    def __init__(
        self,
        image: List[DescribeExportImageInfoResponseBodyImagesImage] = None,
    ):
        self.image = image

    def validate(self):
        if self.image:
            for k in self.image:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Image'] = []
        if self.image is not None:
            for k in self.image:
                result['Image'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.image = []
        if m.get('Image') is not None:
            for k in m.get('Image'):
                temp_model = DescribeExportImageInfoResponseBodyImagesImage()
                self.image.append(temp_model.from_map(k))
        return self


class DescribeExportImageInfoResponseBody(TeaModel):
    def __init__(
        self,
        images: DescribeExportImageInfoResponseBodyImages = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.images = images
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.images:
            self.images.validate()

    def to_map(self):
        result = dict()
        if self.images is not None:
            result['Images'] = self.images.to_map()
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
        if m.get('Images') is not None:
            temp_model = DescribeExportImageInfoResponseBodyImages()
            self.images = temp_model.from_map(m['Images'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeExportImageInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeExportImageInfoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeExportImageInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeExportImageStatusRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
        image_id: str = None,
    ):
        self.version = version
        self.image_id = image_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        return self


class DescribeExportImageStatusResponseBody(TeaModel):
    def __init__(
        self,
        image_export_status: str = None,
        request_id: str = None,
    ):
        self.image_export_status = image_export_status
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_export_status is not None:
            result['ImageExportStatus'] = self.image_export_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageExportStatus') is not None:
            self.image_export_status = m.get('ImageExportStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeExportImageStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeExportImageStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeExportImageStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeImageInfosRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
        os_type: str = None,
    ):
        self.version = version
        self.os_type = os_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.os_type is not None:
            result['OsType'] = self.os_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        return self


class DescribeImageInfosResponseBodyImagesImage(TeaModel):
    def __init__(
        self,
        description: str = None,
        image_id: str = None,
        image_size: str = None,
        image_version: str = None,
        osname: str = None,
        ostype: str = None,
    ):
        self.description = description
        self.image_id = image_id
        self.image_size = image_size
        self.image_version = image_version
        self.osname = osname
        self.ostype = ostype

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_size is not None:
            result['ImageSize'] = self.image_size
        if self.image_version is not None:
            result['ImageVersion'] = self.image_version
        if self.osname is not None:
            result['OSName'] = self.osname
        if self.ostype is not None:
            result['OSType'] = self.ostype
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageSize') is not None:
            self.image_size = m.get('ImageSize')
        if m.get('ImageVersion') is not None:
            self.image_version = m.get('ImageVersion')
        if m.get('OSName') is not None:
            self.osname = m.get('OSName')
        if m.get('OSType') is not None:
            self.ostype = m.get('OSType')
        return self


class DescribeImageInfosResponseBodyImages(TeaModel):
    def __init__(
        self,
        image: List[DescribeImageInfosResponseBodyImagesImage] = None,
    ):
        self.image = image

    def validate(self):
        if self.image:
            for k in self.image:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Image'] = []
        if self.image is not None:
            for k in self.image:
                result['Image'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.image = []
        if m.get('Image') is not None:
            for k in m.get('Image'):
                temp_model = DescribeImageInfosResponseBodyImagesImage()
                self.image.append(temp_model.from_map(k))
        return self


class DescribeImageInfosResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        images: DescribeImageInfosResponseBodyImages = None,
        request_id: str = None,
    ):
        self.code = code
        self.images = images
        self.request_id = request_id

    def validate(self):
        if self.images:
            self.images.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.images is not None:
            result['Images'] = self.images.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Images') is not None:
            temp_model = DescribeImageInfosResponseBodyImages()
            self.images = temp_model.from_map(m['Images'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeImageInfosResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeImageInfosResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeImageInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeImagesRequest(TeaModel):
    def __init__(
        self,
        product: str = None,
        version: str = None,
        ens_region_id: str = None,
        image_id: str = None,
        status: str = None,
        image_name: str = None,
        page_number: str = None,
        page_size: str = None,
    ):
        self.product = product
        self.version = version
        self.ens_region_id = ens_region_id
        self.image_id = image_id
        self.status = status
        self.image_name = image_name
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.product is not None:
            result['product'] = self.product
        if self.version is not None:
            result['Version'] = self.version
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.status is not None:
            result['Status'] = self.status
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('product') is not None:
            self.product = m.get('product')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeImagesResponseBodyImagesImage(TeaModel):
    def __init__(
        self,
        architecture: str = None,
        creation_time: str = None,
        image_id: str = None,
        image_name: str = None,
        image_owner_alias: str = None,
        image_size: str = None,
        platform: str = None,
    ):
        self.architecture = architecture
        self.creation_time = creation_time
        self.image_id = image_id
        self.image_name = image_name
        self.image_owner_alias = image_owner_alias
        self.image_size = image_size
        self.platform = platform

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.architecture is not None:
            result['Architecture'] = self.architecture
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.image_owner_alias is not None:
            result['ImageOwnerAlias'] = self.image_owner_alias
        if self.image_size is not None:
            result['ImageSize'] = self.image_size
        if self.platform is not None:
            result['Platform'] = self.platform
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('ImageOwnerAlias') is not None:
            self.image_owner_alias = m.get('ImageOwnerAlias')
        if m.get('ImageSize') is not None:
            self.image_size = m.get('ImageSize')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        return self


class DescribeImagesResponseBodyImages(TeaModel):
    def __init__(
        self,
        image: List[DescribeImagesResponseBodyImagesImage] = None,
    ):
        self.image = image

    def validate(self):
        if self.image:
            for k in self.image:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Image'] = []
        if self.image is not None:
            for k in self.image:
                result['Image'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.image = []
        if m.get('Image') is not None:
            for k in m.get('Image'):
                temp_model = DescribeImagesResponseBodyImagesImage()
                self.image.append(temp_model.from_map(k))
        return self


class DescribeImagesResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        images: DescribeImagesResponseBodyImages = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.code = code
        self.images = images
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.images:
            self.images.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.images is not None:
            result['Images'] = self.images.to_map()
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Images') is not None:
            temp_model = DescribeImagesResponseBodyImages()
            self.images = temp_model.from_map(m['Images'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeImagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeImagesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeImagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceAutoRenewAttributeRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
        instance_ids: str = None,
        owner_id: int = None,
    ):
        self.version = version
        self.instance_ids = instance_ids
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeInstanceAutoRenewAttributeResponseBodyInstanceRenewAttributesInstanceRenewAttribute(TeaModel):
    def __init__(
        self,
        auto_renewal: bool = None,
        duration: str = None,
        instance_id: str = None,
    ):
        self.auto_renewal = auto_renewal
        self.duration = duration
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.auto_renewal is not None:
            result['AutoRenewal'] = self.auto_renewal
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenewal') is not None:
            self.auto_renewal = m.get('AutoRenewal')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeInstanceAutoRenewAttributeResponseBodyInstanceRenewAttributes(TeaModel):
    def __init__(
        self,
        instance_renew_attribute: List[DescribeInstanceAutoRenewAttributeResponseBodyInstanceRenewAttributesInstanceRenewAttribute] = None,
    ):
        self.instance_renew_attribute = instance_renew_attribute

    def validate(self):
        if self.instance_renew_attribute:
            for k in self.instance_renew_attribute:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['InstanceRenewAttribute'] = []
        if self.instance_renew_attribute is not None:
            for k in self.instance_renew_attribute:
                result['InstanceRenewAttribute'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_renew_attribute = []
        if m.get('InstanceRenewAttribute') is not None:
            for k in m.get('InstanceRenewAttribute'):
                temp_model = DescribeInstanceAutoRenewAttributeResponseBodyInstanceRenewAttributesInstanceRenewAttribute()
                self.instance_renew_attribute.append(temp_model.from_map(k))
        return self


class DescribeInstanceAutoRenewAttributeResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        instance_renew_attributes: DescribeInstanceAutoRenewAttributeResponseBodyInstanceRenewAttributes = None,
        request_id: str = None,
    ):
        self.code = code
        self.instance_renew_attributes = instance_renew_attributes
        self.request_id = request_id

    def validate(self):
        if self.instance_renew_attributes:
            self.instance_renew_attributes.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.instance_renew_attributes is not None:
            result['InstanceRenewAttributes'] = self.instance_renew_attributes.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('InstanceRenewAttributes') is not None:
            temp_model = DescribeInstanceAutoRenewAttributeResponseBodyInstanceRenewAttributes()
            self.instance_renew_attributes = temp_model.from_map(m['InstanceRenewAttributes'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInstanceAutoRenewAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeInstanceAutoRenewAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeInstanceAutoRenewAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceMonitorDataRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
        instance_id: str = None,
        start_time: str = None,
        end_time: str = None,
        period: str = None,
    ):
        self.version = version
        self.instance_id = instance_id
        self.start_time = start_time
        self.end_time = end_time
        self.period = period

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.period is not None:
            result['Period'] = self.period
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        return self


class DescribeInstanceMonitorDataResponseBodyMonitorDataInstanceMonitorData(TeaModel):
    def __init__(
        self,
        cpu: str = None,
        instance_id: str = None,
        memory: str = None,
    ):
        self.cpu = cpu
        self.instance_id = instance_id
        self.memory = memory

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cpu is not None:
            result['CPU'] = self.cpu
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.memory is not None:
            result['Memory'] = self.memory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CPU') is not None:
            self.cpu = m.get('CPU')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class DescribeInstanceMonitorDataResponseBodyMonitorData(TeaModel):
    def __init__(
        self,
        instance_monitor_data: List[DescribeInstanceMonitorDataResponseBodyMonitorDataInstanceMonitorData] = None,
    ):
        self.instance_monitor_data = instance_monitor_data

    def validate(self):
        if self.instance_monitor_data:
            for k in self.instance_monitor_data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['InstanceMonitorData'] = []
        if self.instance_monitor_data is not None:
            for k in self.instance_monitor_data:
                result['InstanceMonitorData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_monitor_data = []
        if m.get('InstanceMonitorData') is not None:
            for k in m.get('InstanceMonitorData'):
                temp_model = DescribeInstanceMonitorDataResponseBodyMonitorDataInstanceMonitorData()
                self.instance_monitor_data.append(temp_model.from_map(k))
        return self


class DescribeInstanceMonitorDataResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        monitor_data: DescribeInstanceMonitorDataResponseBodyMonitorData = None,
        request_id: str = None,
    ):
        self.code = code
        self.monitor_data = monitor_data
        self.request_id = request_id

    def validate(self):
        if self.monitor_data:
            self.monitor_data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.monitor_data is not None:
            result['MonitorData'] = self.monitor_data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('MonitorData') is not None:
            temp_model = DescribeInstanceMonitorDataResponseBodyMonitorData()
            self.monitor_data = temp_model.from_map(m['MonitorData'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInstanceMonitorDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeInstanceMonitorDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeInstanceMonitorDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceSpecRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
    ):
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeInstanceSpecResponseBodyInstanceSpecsInstanceSpec(TeaModel):
    def __init__(
        self,
        core: str = None,
        display_name: str = None,
        instance_type: str = None,
        memory: str = None,
    ):
        self.core = core
        self.display_name = display_name
        self.instance_type = instance_type
        self.memory = memory

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.core is not None:
            result['Core'] = self.core
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.memory is not None:
            result['Memory'] = self.memory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Core') is not None:
            self.core = m.get('Core')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class DescribeInstanceSpecResponseBodyInstanceSpecs(TeaModel):
    def __init__(
        self,
        instance_spec: List[DescribeInstanceSpecResponseBodyInstanceSpecsInstanceSpec] = None,
    ):
        self.instance_spec = instance_spec

    def validate(self):
        if self.instance_spec:
            for k in self.instance_spec:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['InstanceSpec'] = []
        if self.instance_spec is not None:
            for k in self.instance_spec:
                result['InstanceSpec'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_spec = []
        if m.get('InstanceSpec') is not None:
            for k in m.get('InstanceSpec'):
                temp_model = DescribeInstanceSpecResponseBodyInstanceSpecsInstanceSpec()
                self.instance_spec.append(temp_model.from_map(k))
        return self


class DescribeInstanceSpecResponseBody(TeaModel):
    def __init__(
        self,
        bandwidth_limit: int = None,
        code: int = None,
        data_disk_max_size: int = None,
        data_disk_min_size: int = None,
        instance_specs: DescribeInstanceSpecResponseBodyInstanceSpecs = None,
        request_id: str = None,
        system_disk_max_size: int = None,
    ):
        self.bandwidth_limit = bandwidth_limit
        self.code = code
        self.data_disk_max_size = data_disk_max_size
        self.data_disk_min_size = data_disk_min_size
        self.instance_specs = instance_specs
        self.request_id = request_id
        self.system_disk_max_size = system_disk_max_size

    def validate(self):
        if self.instance_specs:
            self.instance_specs.validate()

    def to_map(self):
        result = dict()
        if self.bandwidth_limit is not None:
            result['BandwidthLimit'] = self.bandwidth_limit
        if self.code is not None:
            result['Code'] = self.code
        if self.data_disk_max_size is not None:
            result['DataDiskMaxSize'] = self.data_disk_max_size
        if self.data_disk_min_size is not None:
            result['DataDiskMinSize'] = self.data_disk_min_size
        if self.instance_specs is not None:
            result['InstanceSpecs'] = self.instance_specs.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.system_disk_max_size is not None:
            result['SystemDiskMaxSize'] = self.system_disk_max_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthLimit') is not None:
            self.bandwidth_limit = m.get('BandwidthLimit')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DataDiskMaxSize') is not None:
            self.data_disk_max_size = m.get('DataDiskMaxSize')
        if m.get('DataDiskMinSize') is not None:
            self.data_disk_min_size = m.get('DataDiskMinSize')
        if m.get('InstanceSpecs') is not None:
            temp_model = DescribeInstanceSpecResponseBodyInstanceSpecs()
            self.instance_specs = temp_model.from_map(m['InstanceSpecs'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SystemDiskMaxSize') is not None:
            self.system_disk_max_size = m.get('SystemDiskMaxSize')
        return self


class DescribeInstanceSpecResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeInstanceSpecResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeInstanceSpecResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceTypesRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
    ):
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeInstanceTypesResponseBodyInstanceTypesInstanceType(TeaModel):
    def __init__(
        self,
        cpu_core_count: int = None,
        instance_type_id: str = None,
        instance_type_name: str = None,
        memory_size: int = None,
    ):
        self.cpu_core_count = cpu_core_count
        self.instance_type_id = instance_type_id
        self.instance_type_name = instance_type_name
        self.memory_size = memory_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cpu_core_count is not None:
            result['CpuCoreCount'] = self.cpu_core_count
        if self.instance_type_id is not None:
            result['InstanceTypeId'] = self.instance_type_id
        if self.instance_type_name is not None:
            result['InstanceTypeName'] = self.instance_type_name
        if self.memory_size is not None:
            result['MemorySize'] = self.memory_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuCoreCount') is not None:
            self.cpu_core_count = m.get('CpuCoreCount')
        if m.get('InstanceTypeId') is not None:
            self.instance_type_id = m.get('InstanceTypeId')
        if m.get('InstanceTypeName') is not None:
            self.instance_type_name = m.get('InstanceTypeName')
        if m.get('MemorySize') is not None:
            self.memory_size = m.get('MemorySize')
        return self


class DescribeInstanceTypesResponseBodyInstanceTypes(TeaModel):
    def __init__(
        self,
        instance_type: List[DescribeInstanceTypesResponseBodyInstanceTypesInstanceType] = None,
    ):
        self.instance_type = instance_type

    def validate(self):
        if self.instance_type:
            for k in self.instance_type:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['InstanceType'] = []
        if self.instance_type is not None:
            for k in self.instance_type:
                result['InstanceType'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_type = []
        if m.get('InstanceType') is not None:
            for k in m.get('InstanceType'):
                temp_model = DescribeInstanceTypesResponseBodyInstanceTypesInstanceType()
                self.instance_type.append(temp_model.from_map(k))
        return self


class DescribeInstanceTypesResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        instance_types: DescribeInstanceTypesResponseBodyInstanceTypes = None,
        request_id: str = None,
    ):
        self.code = code
        self.instance_types = instance_types
        self.request_id = request_id

    def validate(self):
        if self.instance_types:
            self.instance_types.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.instance_types is not None:
            result['InstanceTypes'] = self.instance_types.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('InstanceTypes') is not None:
            temp_model = DescribeInstanceTypesResponseBodyInstanceTypes()
            self.instance_types = temp_model.from_map(m['InstanceTypes'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInstanceTypesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeInstanceTypesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeInstanceTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceVncUrlRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # 实例ID。
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeInstanceVncUrlResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        vnc_url: str = None,
    ):
        # 请求ID。
        self.request_id = request_id
        # 管理终端Url。
        self.vnc_url = vnc_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.vnc_url is not None:
            result['VncUrl'] = self.vnc_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VncUrl') is not None:
            self.vnc_url = m.get('VncUrl')
        return self


class DescribeInstanceVncUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeInstanceVncUrlResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeInstanceVncUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeKeyPairsRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
        key_pair_name: str = None,
        page_number: str = None,
        page_size: str = None,
    ):
        self.version = version
        self.key_pair_name = key_pair_name
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeKeyPairsResponseBodyKeyPairsKeyPair(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        key_pair_finger_print: str = None,
        key_pair_name: str = None,
    ):
        self.creation_time = creation_time
        self.key_pair_finger_print = key_pair_finger_print
        self.key_pair_name = key_pair_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.key_pair_finger_print is not None:
            result['KeyPairFingerPrint'] = self.key_pair_finger_print
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('KeyPairFingerPrint') is not None:
            self.key_pair_finger_print = m.get('KeyPairFingerPrint')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        return self


class DescribeKeyPairsResponseBodyKeyPairs(TeaModel):
    def __init__(
        self,
        key_pair: List[DescribeKeyPairsResponseBodyKeyPairsKeyPair] = None,
    ):
        self.key_pair = key_pair

    def validate(self):
        if self.key_pair:
            for k in self.key_pair:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['KeyPair'] = []
        if self.key_pair is not None:
            for k in self.key_pair:
                result['KeyPair'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.key_pair = []
        if m.get('KeyPair') is not None:
            for k in m.get('KeyPair'):
                temp_model = DescribeKeyPairsResponseBodyKeyPairsKeyPair()
                self.key_pair.append(temp_model.from_map(k))
        return self


class DescribeKeyPairsResponseBody(TeaModel):
    def __init__(
        self,
        key_pairs: DescribeKeyPairsResponseBodyKeyPairs = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.key_pairs = key_pairs
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.key_pairs:
            self.key_pairs.validate()

    def to_map(self):
        result = dict()
        if self.key_pairs is not None:
            result['KeyPairs'] = self.key_pairs.to_map()
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
        if m.get('KeyPairs') is not None:
            temp_model = DescribeKeyPairsResponseBodyKeyPairs()
            self.key_pairs = temp_model.from_map(m['KeyPairs'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeKeyPairsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeKeyPairsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeKeyPairsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMeasurementDataRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
        start_date: str = None,
        end_date: str = None,
    ):
        self.version = version
        self.start_date = start_date
        self.end_date = end_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class DescribeMeasurementDataResponseBodyMeasurementDatasMeasurementDataBandWidthFeeDatasBandWidthFeeData(TeaModel):
    def __init__(
        self,
        cost_code: str = None,
        cost_name: str = None,
        cost_val: int = None,
    ):
        self.cost_code = cost_code
        self.cost_name = cost_name
        self.cost_val = cost_val

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cost_code is not None:
            result['CostCode'] = self.cost_code
        if self.cost_name is not None:
            result['CostName'] = self.cost_name
        if self.cost_val is not None:
            result['CostVal'] = self.cost_val
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostCode') is not None:
            self.cost_code = m.get('CostCode')
        if m.get('CostName') is not None:
            self.cost_name = m.get('CostName')
        if m.get('CostVal') is not None:
            self.cost_val = m.get('CostVal')
        return self


class DescribeMeasurementDataResponseBodyMeasurementDatasMeasurementDataBandWidthFeeDatas(TeaModel):
    def __init__(
        self,
        band_width_fee_data: List[DescribeMeasurementDataResponseBodyMeasurementDatasMeasurementDataBandWidthFeeDatasBandWidthFeeData] = None,
    ):
        self.band_width_fee_data = band_width_fee_data

    def validate(self):
        if self.band_width_fee_data:
            for k in self.band_width_fee_data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['BandWidthFeeData'] = []
        if self.band_width_fee_data is not None:
            for k in self.band_width_fee_data:
                result['BandWidthFeeData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.band_width_fee_data = []
        if m.get('BandWidthFeeData') is not None:
            for k in m.get('BandWidthFeeData'):
                temp_model = DescribeMeasurementDataResponseBodyMeasurementDatasMeasurementDataBandWidthFeeDatasBandWidthFeeData()
                self.band_width_fee_data.append(temp_model.from_map(k))
        return self


class DescribeMeasurementDataResponseBodyMeasurementDatasMeasurementDataResourceFeeData(TeaModel):
    def __init__(
        self,
        memory: int = None,
        storage: int = None,
        vcpu: int = None,
    ):
        self.memory = memory
        self.storage = storage
        self.vcpu = vcpu

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.storage is not None:
            result['Storage'] = self.storage
        if self.vcpu is not None:
            result['Vcpu'] = self.vcpu
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Storage') is not None:
            self.storage = m.get('Storage')
        if m.get('Vcpu') is not None:
            self.vcpu = m.get('Vcpu')
        return self


class DescribeMeasurementDataResponseBodyMeasurementDatasMeasurementDataResourceFeeDataDetailsResourceFeeDataDetail(TeaModel):
    def __init__(
        self,
        cost_code: str = None,
        cost_name: str = None,
        cost_val: int = None,
        resource_type: str = None,
    ):
        self.cost_code = cost_code
        self.cost_name = cost_name
        self.cost_val = cost_val
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cost_code is not None:
            result['CostCode'] = self.cost_code
        if self.cost_name is not None:
            result['CostName'] = self.cost_name
        if self.cost_val is not None:
            result['CostVal'] = self.cost_val
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostCode') is not None:
            self.cost_code = m.get('CostCode')
        if m.get('CostName') is not None:
            self.cost_name = m.get('CostName')
        if m.get('CostVal') is not None:
            self.cost_val = m.get('CostVal')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class DescribeMeasurementDataResponseBodyMeasurementDatasMeasurementDataResourceFeeDataDetails(TeaModel):
    def __init__(
        self,
        resource_fee_data_detail: List[DescribeMeasurementDataResponseBodyMeasurementDatasMeasurementDataResourceFeeDataDetailsResourceFeeDataDetail] = None,
    ):
        self.resource_fee_data_detail = resource_fee_data_detail

    def validate(self):
        if self.resource_fee_data_detail:
            for k in self.resource_fee_data_detail:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ResourceFeeDataDetail'] = []
        if self.resource_fee_data_detail is not None:
            for k in self.resource_fee_data_detail:
                result['ResourceFeeDataDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource_fee_data_detail = []
        if m.get('ResourceFeeDataDetail') is not None:
            for k in m.get('ResourceFeeDataDetail'):
                temp_model = DescribeMeasurementDataResponseBodyMeasurementDatasMeasurementDataResourceFeeDataDetailsResourceFeeDataDetail()
                self.resource_fee_data_detail.append(temp_model.from_map(k))
        return self


class DescribeMeasurementDataResponseBodyMeasurementDatasMeasurementData(TeaModel):
    def __init__(
        self,
        band_width_fee_datas: DescribeMeasurementDataResponseBodyMeasurementDatasMeasurementDataBandWidthFeeDatas = None,
        charge_model: str = None,
        cost_cycle: str = None,
        cost_end_time: str = None,
        cost_start_time: str = None,
        resource_fee_data: DescribeMeasurementDataResponseBodyMeasurementDatasMeasurementDataResourceFeeData = None,
        resource_fee_data_details: DescribeMeasurementDataResponseBodyMeasurementDatasMeasurementDataResourceFeeDataDetails = None,
    ):
        self.band_width_fee_datas = band_width_fee_datas
        self.charge_model = charge_model
        self.cost_cycle = cost_cycle
        self.cost_end_time = cost_end_time
        self.cost_start_time = cost_start_time
        self.resource_fee_data = resource_fee_data
        self.resource_fee_data_details = resource_fee_data_details

    def validate(self):
        if self.band_width_fee_datas:
            self.band_width_fee_datas.validate()
        if self.resource_fee_data:
            self.resource_fee_data.validate()
        if self.resource_fee_data_details:
            self.resource_fee_data_details.validate()

    def to_map(self):
        result = dict()
        if self.band_width_fee_datas is not None:
            result['BandWidthFeeDatas'] = self.band_width_fee_datas.to_map()
        if self.charge_model is not None:
            result['ChargeModel'] = self.charge_model
        if self.cost_cycle is not None:
            result['CostCycle'] = self.cost_cycle
        if self.cost_end_time is not None:
            result['CostEndTime'] = self.cost_end_time
        if self.cost_start_time is not None:
            result['CostStartTime'] = self.cost_start_time
        if self.resource_fee_data is not None:
            result['ResourceFeeData'] = self.resource_fee_data.to_map()
        if self.resource_fee_data_details is not None:
            result['ResourceFeeDataDetails'] = self.resource_fee_data_details.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandWidthFeeDatas') is not None:
            temp_model = DescribeMeasurementDataResponseBodyMeasurementDatasMeasurementDataBandWidthFeeDatas()
            self.band_width_fee_datas = temp_model.from_map(m['BandWidthFeeDatas'])
        if m.get('ChargeModel') is not None:
            self.charge_model = m.get('ChargeModel')
        if m.get('CostCycle') is not None:
            self.cost_cycle = m.get('CostCycle')
        if m.get('CostEndTime') is not None:
            self.cost_end_time = m.get('CostEndTime')
        if m.get('CostStartTime') is not None:
            self.cost_start_time = m.get('CostStartTime')
        if m.get('ResourceFeeData') is not None:
            temp_model = DescribeMeasurementDataResponseBodyMeasurementDatasMeasurementDataResourceFeeData()
            self.resource_fee_data = temp_model.from_map(m['ResourceFeeData'])
        if m.get('ResourceFeeDataDetails') is not None:
            temp_model = DescribeMeasurementDataResponseBodyMeasurementDatasMeasurementDataResourceFeeDataDetails()
            self.resource_fee_data_details = temp_model.from_map(m['ResourceFeeDataDetails'])
        return self


class DescribeMeasurementDataResponseBodyMeasurementDatas(TeaModel):
    def __init__(
        self,
        measurement_data: List[DescribeMeasurementDataResponseBodyMeasurementDatasMeasurementData] = None,
    ):
        self.measurement_data = measurement_data

    def validate(self):
        if self.measurement_data:
            for k in self.measurement_data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['MeasurementData'] = []
        if self.measurement_data is not None:
            for k in self.measurement_data:
                result['MeasurementData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.measurement_data = []
        if m.get('MeasurementData') is not None:
            for k in m.get('MeasurementData'):
                temp_model = DescribeMeasurementDataResponseBodyMeasurementDatasMeasurementData()
                self.measurement_data.append(temp_model.from_map(k))
        return self


class DescribeMeasurementDataResponseBody(TeaModel):
    def __init__(
        self,
        measurement_datas: DescribeMeasurementDataResponseBodyMeasurementDatas = None,
        request_id: str = None,
    ):
        self.measurement_datas = measurement_datas
        self.request_id = request_id

    def validate(self):
        if self.measurement_datas:
            self.measurement_datas.validate()

    def to_map(self):
        result = dict()
        if self.measurement_datas is not None:
            result['MeasurementDatas'] = self.measurement_datas.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MeasurementDatas') is not None:
            temp_model = DescribeMeasurementDataResponseBodyMeasurementDatas()
            self.measurement_datas = temp_model.from_map(m['MeasurementDatas'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeMeasurementDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeMeasurementDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeMeasurementDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNetworkInterfacesRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        v_switch_id: str = None,
        ens_region_id: str = None,
        primary_ip_address: str = None,
        page_number: str = None,
        page_size: str = None,
    ):
        self.instance_id = instance_id
        self.v_switch_id = v_switch_id
        self.ens_region_id = ens_region_id
        self.primary_ip_address = primary_ip_address
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.primary_ip_address is not None:
            result['PrimaryIpAddress'] = self.primary_ip_address
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('PrimaryIpAddress') is not None:
            self.primary_ip_address = m.get('PrimaryIpAddress')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSet(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        ens_region_id: str = None,
        instance_id: str = None,
        mac_address: str = None,
        network_interface_id: str = None,
        primary_ip: str = None,
        primary_ip_type: str = None,
        status: str = None,
        v_switch_id: str = None,
    ):
        self.creation_time = creation_time
        self.ens_region_id = ens_region_id
        self.instance_id = instance_id
        self.mac_address = mac_address
        self.network_interface_id = network_interface_id
        self.primary_ip = primary_ip
        self.primary_ip_type = primary_ip_type
        self.status = status
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mac_address is not None:
            result['MacAddress'] = self.mac_address
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id
        if self.primary_ip is not None:
            result['PrimaryIp'] = self.primary_ip
        if self.primary_ip_type is not None:
            result['PrimaryIpType'] = self.primary_ip_type
        if self.status is not None:
            result['Status'] = self.status
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MacAddress') is not None:
            self.mac_address = m.get('MacAddress')
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')
        if m.get('PrimaryIp') is not None:
            self.primary_ip = m.get('PrimaryIp')
        if m.get('PrimaryIpType') is not None:
            self.primary_ip_type = m.get('PrimaryIpType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class DescribeNetworkInterfacesResponseBodyNetworkInterfaceSets(TeaModel):
    def __init__(
        self,
        network_interface_set: List[DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSet] = None,
    ):
        self.network_interface_set = network_interface_set

    def validate(self):
        if self.network_interface_set:
            for k in self.network_interface_set:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['NetworkInterfaceSet'] = []
        if self.network_interface_set is not None:
            for k in self.network_interface_set:
                result['NetworkInterfaceSet'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.network_interface_set = []
        if m.get('NetworkInterfaceSet') is not None:
            for k in m.get('NetworkInterfaceSet'):
                temp_model = DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSet()
                self.network_interface_set.append(temp_model.from_map(k))
        return self


class DescribeNetworkInterfacesResponseBody(TeaModel):
    def __init__(
        self,
        network_interface_sets: DescribeNetworkInterfacesResponseBodyNetworkInterfaceSets = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.network_interface_sets = network_interface_sets
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.network_interface_sets:
            self.network_interface_sets.validate()

    def to_map(self):
        result = dict()
        if self.network_interface_sets is not None:
            result['NetworkInterfaceSets'] = self.network_interface_sets.to_map()
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
        if m.get('NetworkInterfaceSets') is not None:
            temp_model = DescribeNetworkInterfacesResponseBodyNetworkInterfaceSets()
            self.network_interface_sets = temp_model.from_map(m['NetworkInterfaceSets'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeNetworkInterfacesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeNetworkInterfacesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeNetworkInterfacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePrePaidInstanceStockRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
        ens_region_id: str = None,
        system_disk_size: int = None,
        data_disk_size: int = None,
        instance_spec: str = None,
    ):
        self.version = version
        self.ens_region_id = ens_region_id
        self.system_disk_size = system_disk_size
        self.data_disk_size = data_disk_size
        self.instance_spec = instance_spec

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size
        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')
        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')
        return self


class DescribePrePaidInstanceStockResponseBody(TeaModel):
    def __init__(
        self,
        avaliable_count: int = None,
        cores: int = None,
        data_disk_size: int = None,
        ens_region_id: str = None,
        instance_spec: str = None,
        memory: int = None,
        request_id: str = None,
        system_disk_size: int = None,
    ):
        self.avaliable_count = avaliable_count
        self.cores = cores
        self.data_disk_size = data_disk_size
        self.ens_region_id = ens_region_id
        self.instance_spec = instance_spec
        self.memory = memory
        self.request_id = request_id
        self.system_disk_size = system_disk_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.avaliable_count is not None:
            result['AvaliableCount'] = self.avaliable_count
        if self.cores is not None:
            result['Cores'] = self.cores
        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvaliableCount') is not None:
            self.avaliable_count = m.get('AvaliableCount')
        if m.get('Cores') is not None:
            self.cores = m.get('Cores')
        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        return self


class DescribePrePaidInstanceStockResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePrePaidInstanceStockResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribePrePaidInstanceStockResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePriceRequestSystemDisk(TeaModel):
    def __init__(
        self,
        size: int = None,
    ):
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class DescribePriceRequestDataDisk(TeaModel):
    def __init__(
        self,
        size: int = None,
    ):
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class DescribePriceRequest(TeaModel):
    def __init__(
        self,
        system_disk: DescribePriceRequestSystemDisk = None,
        data_disk: List[DescribePriceRequestDataDisk] = None,
        version: str = None,
        instance_type: str = None,
        ens_region_id: str = None,
        period: int = None,
        quantity: int = None,
        internet_charge_type: str = None,
    ):
        self.system_disk = system_disk
        self.data_disk = data_disk
        self.version = version
        self.instance_type = instance_type
        self.ens_region_id = ens_region_id
        self.period = period
        self.quantity = quantity
        self.internet_charge_type = internet_charge_type

    def validate(self):
        if self.system_disk:
            self.system_disk.validate()
        if self.data_disk:
            for k in self.data_disk:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()
        result['DataDisk'] = []
        if self.data_disk is not None:
            for k in self.data_disk:
                result['DataDisk'].append(k.to_map() if k else None)
        if self.version is not None:
            result['Version'] = self.version
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.period is not None:
            result['Period'] = self.period
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SystemDisk') is not None:
            temp_model = DescribePriceRequestSystemDisk()
            self.system_disk = temp_model.from_map(m['SystemDisk'])
        self.data_disk = []
        if m.get('DataDisk') is not None:
            for k in m.get('DataDisk'):
                temp_model = DescribePriceRequestDataDisk()
                self.data_disk.append(temp_model.from_map(k))
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        return self


class DescribePriceResponseBodyPriceInfoPrice(TeaModel):
    def __init__(
        self,
        currency: str = None,
        discount_price: float = None,
        original_price: float = None,
        trade_price: float = None,
    ):
        self.currency = currency
        self.discount_price = discount_price
        self.original_price = original_price
        self.trade_price = trade_price

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class DescribePriceResponseBodyPriceInfo(TeaModel):
    def __init__(
        self,
        price: DescribePriceResponseBodyPriceInfoPrice = None,
    ):
        self.price = price

    def validate(self):
        if self.price:
            self.price.validate()

    def to_map(self):
        result = dict()
        if self.price is not None:
            result['Price'] = self.price.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Price') is not None:
            temp_model = DescribePriceResponseBodyPriceInfoPrice()
            self.price = temp_model.from_map(m['Price'])
        return self


class DescribePriceResponseBody(TeaModel):
    def __init__(
        self,
        price_info: DescribePriceResponseBodyPriceInfo = None,
        request_id: str = None,
    ):
        self.price_info = price_info
        self.request_id = request_id

    def validate(self):
        if self.price_info:
            self.price_info.validate()

    def to_map(self):
        result = dict()
        if self.price_info is not None:
            result['PriceInfo'] = self.price_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PriceInfo') is not None:
            temp_model = DescribePriceResponseBodyPriceInfo()
            self.price_info = temp_model.from_map(m['PriceInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePriceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePriceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribePriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSecurityGroupAttributeRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
        security_group_id: str = None,
    ):
        self.version = version
        self.security_group_id = security_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        return self


class DescribeSecurityGroupAttributeResponseBodyPermissionsPermission(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        dest_cidr_ip: str = None,
        direction: str = None,
        ip_protocol: str = None,
        policy: str = None,
        port_range: str = None,
        priority: int = None,
        source_cidr_ip: str = None,
        source_port_range: str = None,
    ):
        self.creation_time = creation_time
        self.dest_cidr_ip = dest_cidr_ip
        self.direction = direction
        self.ip_protocol = ip_protocol
        self.policy = policy
        self.port_range = port_range
        self.priority = priority
        self.source_cidr_ip = source_cidr_ip
        self.source_port_range = source_port_range

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.dest_cidr_ip is not None:
            result['DestCidrIp'] = self.dest_cidr_ip
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.port_range is not None:
            result['PortRange'] = self.port_range
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.source_cidr_ip is not None:
            result['SourceCidrIp'] = self.source_cidr_ip
        if self.source_port_range is not None:
            result['SourcePortRange'] = self.source_port_range
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('DestCidrIp') is not None:
            self.dest_cidr_ip = m.get('DestCidrIp')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('SourceCidrIp') is not None:
            self.source_cidr_ip = m.get('SourceCidrIp')
        if m.get('SourcePortRange') is not None:
            self.source_port_range = m.get('SourcePortRange')
        return self


class DescribeSecurityGroupAttributeResponseBodyPermissions(TeaModel):
    def __init__(
        self,
        permission: List[DescribeSecurityGroupAttributeResponseBodyPermissionsPermission] = None,
    ):
        self.permission = permission

    def validate(self):
        if self.permission:
            for k in self.permission:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Permission'] = []
        if self.permission is not None:
            for k in self.permission:
                result['Permission'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.permission = []
        if m.get('Permission') is not None:
            for k in m.get('Permission'):
                temp_model = DescribeSecurityGroupAttributeResponseBodyPermissionsPermission()
                self.permission.append(temp_model.from_map(k))
        return self


class DescribeSecurityGroupAttributeResponseBody(TeaModel):
    def __init__(
        self,
        permissions: DescribeSecurityGroupAttributeResponseBodyPermissions = None,
        request_id: str = None,
        security_group_id: str = None,
    ):
        self.permissions = permissions
        self.request_id = request_id
        self.security_group_id = security_group_id

    def validate(self):
        if self.permissions:
            self.permissions.validate()

    def to_map(self):
        result = dict()
        if self.permissions is not None:
            result['Permissions'] = self.permissions.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Permissions') is not None:
            temp_model = DescribeSecurityGroupAttributeResponseBodyPermissions()
            self.permissions = temp_model.from_map(m['Permissions'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        return self


class DescribeSecurityGroupAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSecurityGroupAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSecurityGroupAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSecurityGroupsRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
        security_group_id: str = None,
        page_number: int = None,
        page_size: int = None,
        security_group_name: str = None,
    ):
        self.version = version
        self.security_group_id = security_group_id
        self.page_number = page_number
        self.page_size = page_size
        self.security_group_name = security_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.security_group_name is not None:
            result['SecurityGroupName'] = self.security_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecurityGroupName') is not None:
            self.security_group_name = m.get('SecurityGroupName')
        return self


class DescribeSecurityGroupsResponseBodySecurityGroupsSecurityGroup(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        security_group_id: str = None,
        security_group_name: str = None,
    ):
        self.creation_time = creation_time
        self.security_group_id = security_group_id
        self.security_group_name = security_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.security_group_name is not None:
            result['SecurityGroupName'] = self.security_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('SecurityGroupName') is not None:
            self.security_group_name = m.get('SecurityGroupName')
        return self


class DescribeSecurityGroupsResponseBodySecurityGroups(TeaModel):
    def __init__(
        self,
        security_group: List[DescribeSecurityGroupsResponseBodySecurityGroupsSecurityGroup] = None,
    ):
        self.security_group = security_group

    def validate(self):
        if self.security_group:
            for k in self.security_group:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['SecurityGroup'] = []
        if self.security_group is not None:
            for k in self.security_group:
                result['SecurityGroup'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.security_group = []
        if m.get('SecurityGroup') is not None:
            for k in m.get('SecurityGroup'):
                temp_model = DescribeSecurityGroupsResponseBodySecurityGroupsSecurityGroup()
                self.security_group.append(temp_model.from_map(k))
        return self


class DescribeSecurityGroupsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        security_groups: DescribeSecurityGroupsResponseBodySecurityGroups = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.security_groups = security_groups
        self.total_count = total_count

    def validate(self):
        if self.security_groups:
            self.security_groups.validate()

    def to_map(self):
        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.security_groups is not None:
            result['SecurityGroups'] = self.security_groups.to_map()
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
        if m.get('SecurityGroups') is not None:
            temp_model = DescribeSecurityGroupsResponseBodySecurityGroups()
            self.security_groups = temp_model.from_map(m['SecurityGroups'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeSecurityGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSecurityGroupsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSecurityGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServcieScheduleRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        uuid: str = None,
        pod_config_name: str = None,
    ):
        self.app_id = app_id
        self.uuid = uuid
        self.pod_config_name = pod_config_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.pod_config_name is not None:
            result['PodConfigName'] = self.pod_config_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('PodConfigName') is not None:
            self.pod_config_name = m.get('PodConfigName')
        return self


class DescribeServcieScheduleResponseBodyPodAbstractInfoContainerStatusesContainerStatus(TeaModel):
    def __init__(
        self,
        container_id: str = None,
        name: str = None,
    ):
        self.container_id = container_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.container_id is not None:
            result['ContainerId'] = self.container_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerId') is not None:
            self.container_id = m.get('ContainerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeServcieScheduleResponseBodyPodAbstractInfoContainerStatuses(TeaModel):
    def __init__(
        self,
        container_status: List[DescribeServcieScheduleResponseBodyPodAbstractInfoContainerStatusesContainerStatus] = None,
    ):
        self.container_status = container_status

    def validate(self):
        if self.container_status:
            for k in self.container_status:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ContainerStatus'] = []
        if self.container_status is not None:
            for k in self.container_status:
                result['ContainerStatus'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.container_status = []
        if m.get('ContainerStatus') is not None:
            for k in m.get('ContainerStatus'):
                temp_model = DescribeServcieScheduleResponseBodyPodAbstractInfoContainerStatusesContainerStatus()
                self.container_status.append(temp_model.from_map(k))
        return self


class DescribeServcieScheduleResponseBodyPodAbstractInfo(TeaModel):
    def __init__(
        self,
        container_service: bool = None,
        container_statuses: DescribeServcieScheduleResponseBodyPodAbstractInfoContainerStatuses = None,
        name: bool = None,
        namespace: bool = None,
        resource_scope: bool = None,
        status: bool = None,
    ):
        self.container_service = container_service
        self.container_statuses = container_statuses
        self.name = name
        self.namespace = namespace
        self.resource_scope = resource_scope
        self.status = status

    def validate(self):
        if self.container_statuses:
            self.container_statuses.validate()

    def to_map(self):
        result = dict()
        if self.container_service is not None:
            result['ContainerService'] = self.container_service
        if self.container_statuses is not None:
            result['ContainerStatuses'] = self.container_statuses.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.resource_scope is not None:
            result['ResourceScope'] = self.resource_scope
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerService') is not None:
            self.container_service = m.get('ContainerService')
        if m.get('ContainerStatuses') is not None:
            temp_model = DescribeServcieScheduleResponseBodyPodAbstractInfoContainerStatuses()
            self.container_statuses = temp_model.from_map(m['ContainerStatuses'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ResourceScope') is not None:
            self.resource_scope = m.get('ResourceScope')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeServcieScheduleResponseBody(TeaModel):
    def __init__(
        self,
        index: int = None,
        instance_id: str = None,
        instance_ip: str = None,
        instance_port: int = None,
        pod_abstract_info: DescribeServcieScheduleResponseBodyPodAbstractInfo = None,
        request_id: str = None,
        request_repeated: bool = None,
        tcp_ports: str = None,
    ):
        self.index = index
        self.instance_id = instance_id
        self.instance_ip = instance_ip
        self.instance_port = instance_port
        self.pod_abstract_info = pod_abstract_info
        self.request_id = request_id
        self.request_repeated = request_repeated
        self.tcp_ports = tcp_ports

    def validate(self):
        if self.pod_abstract_info:
            self.pod_abstract_info.validate()

    def to_map(self):
        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_ip is not None:
            result['InstanceIp'] = self.instance_ip
        if self.instance_port is not None:
            result['InstancePort'] = self.instance_port
        if self.pod_abstract_info is not None:
            result['PodAbstractInfo'] = self.pod_abstract_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.request_repeated is not None:
            result['RequestRepeated'] = self.request_repeated
        if self.tcp_ports is not None:
            result['TcpPorts'] = self.tcp_ports
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceIp') is not None:
            self.instance_ip = m.get('InstanceIp')
        if m.get('InstancePort') is not None:
            self.instance_port = m.get('InstancePort')
        if m.get('PodAbstractInfo') is not None:
            temp_model = DescribeServcieScheduleResponseBodyPodAbstractInfo()
            self.pod_abstract_info = temp_model.from_map(m['PodAbstractInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RequestRepeated') is not None:
            self.request_repeated = m.get('RequestRepeated')
        if m.get('TcpPorts') is not None:
            self.tcp_ports = m.get('TcpPorts')
        return self


class DescribeServcieScheduleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeServcieScheduleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeServcieScheduleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserBandWidthDataRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
        ens_region_id: str = None,
        instance_id: str = None,
        start_time: str = None,
        end_time: str = None,
        period: str = None,
        isp: str = None,
    ):
        self.version = version
        self.ens_region_id = ens_region_id
        self.instance_id = instance_id
        self.start_time = start_time
        self.end_time = end_time
        self.period = period
        self.isp = isp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.period is not None:
            result['Period'] = self.period
        if self.isp is not None:
            result['Isp'] = self.isp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        return self


class DescribeUserBandWidthDataResponseBodyMonitorDataBandWidthMonitorData(TeaModel):
    def __init__(
        self,
        down_band_width: int = None,
        internet_rx: int = None,
        internet_tx: int = None,
        time_stamp: str = None,
        up_band_width: int = None,
    ):
        self.down_band_width = down_band_width
        self.internet_rx = internet_rx
        self.internet_tx = internet_tx
        self.time_stamp = time_stamp
        self.up_band_width = up_band_width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.down_band_width is not None:
            result['DownBandWidth'] = self.down_band_width
        if self.internet_rx is not None:
            result['InternetRX'] = self.internet_rx
        if self.internet_tx is not None:
            result['InternetTX'] = self.internet_tx
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.up_band_width is not None:
            result['UpBandWidth'] = self.up_band_width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownBandWidth') is not None:
            self.down_band_width = m.get('DownBandWidth')
        if m.get('InternetRX') is not None:
            self.internet_rx = m.get('InternetRX')
        if m.get('InternetTX') is not None:
            self.internet_tx = m.get('InternetTX')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('UpBandWidth') is not None:
            self.up_band_width = m.get('UpBandWidth')
        return self


class DescribeUserBandWidthDataResponseBodyMonitorData(TeaModel):
    def __init__(
        self,
        band_width_monitor_data: List[DescribeUserBandWidthDataResponseBodyMonitorDataBandWidthMonitorData] = None,
        max_down_band_width: str = None,
        max_up_band_width: str = None,
    ):
        self.band_width_monitor_data = band_width_monitor_data
        self.max_down_band_width = max_down_band_width
        self.max_up_band_width = max_up_band_width

    def validate(self):
        if self.band_width_monitor_data:
            for k in self.band_width_monitor_data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['BandWidthMonitorData'] = []
        if self.band_width_monitor_data is not None:
            for k in self.band_width_monitor_data:
                result['BandWidthMonitorData'].append(k.to_map() if k else None)
        if self.max_down_band_width is not None:
            result['MaxDownBandWidth'] = self.max_down_band_width
        if self.max_up_band_width is not None:
            result['MaxUpBandWidth'] = self.max_up_band_width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.band_width_monitor_data = []
        if m.get('BandWidthMonitorData') is not None:
            for k in m.get('BandWidthMonitorData'):
                temp_model = DescribeUserBandWidthDataResponseBodyMonitorDataBandWidthMonitorData()
                self.band_width_monitor_data.append(temp_model.from_map(k))
        if m.get('MaxDownBandWidth') is not None:
            self.max_down_band_width = m.get('MaxDownBandWidth')
        if m.get('MaxUpBandWidth') is not None:
            self.max_up_band_width = m.get('MaxUpBandWidth')
        return self


class DescribeUserBandWidthDataResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        monitor_data: DescribeUserBandWidthDataResponseBodyMonitorData = None,
        request_id: str = None,
    ):
        self.code = code
        self.monitor_data = monitor_data
        self.request_id = request_id

    def validate(self):
        if self.monitor_data:
            self.monitor_data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.monitor_data is not None:
            result['MonitorData'] = self.monitor_data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('MonitorData') is not None:
            temp_model = DescribeUserBandWidthDataResponseBodyMonitorData()
            self.monitor_data = temp_model.from_map(m['MonitorData'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeUserBandWidthDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeUserBandWidthDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeUserBandWidthDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVSwitchesRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
        ens_region_id: str = None,
        v_switch_id: str = None,
        v_switch_name: str = None,
        page_number: int = None,
        page_size: int = None,
        order_by_params: str = None,
    ):
        self.version = version
        self.ens_region_id = ens_region_id
        self.v_switch_id = v_switch_id
        self.v_switch_name = v_switch_name
        self.page_number = page_number
        self.page_size = page_size
        self.order_by_params = order_by_params

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.v_switch_name is not None:
            result['VSwitchName'] = self.v_switch_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.order_by_params is not None:
            result['OrderByParams'] = self.order_by_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VSwitchName') is not None:
            self.v_switch_name = m.get('VSwitchName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('OrderByParams') is not None:
            self.order_by_params = m.get('OrderByParams')
        return self


class DescribeVSwitchesResponseBodyVSwitchesVSwitch(TeaModel):
    def __init__(
        self,
        cidr_block: str = None,
        created_time: str = None,
        ens_region_id: str = None,
        free_ip_count: int = None,
        status: str = None,
        v_switch_id: str = None,
        v_switch_name: str = None,
    ):
        self.cidr_block = cidr_block
        self.created_time = created_time
        self.ens_region_id = ens_region_id
        self.free_ip_count = free_ip_count
        self.status = status
        self.v_switch_id = v_switch_id
        self.v_switch_name = v_switch_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.free_ip_count is not None:
            result['FreeIpCount'] = self.free_ip_count
        if self.status is not None:
            result['Status'] = self.status
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.v_switch_name is not None:
            result['VSwitchName'] = self.v_switch_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('FreeIpCount') is not None:
            self.free_ip_count = m.get('FreeIpCount')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VSwitchName') is not None:
            self.v_switch_name = m.get('VSwitchName')
        return self


class DescribeVSwitchesResponseBodyVSwitches(TeaModel):
    def __init__(
        self,
        v_switch: List[DescribeVSwitchesResponseBodyVSwitchesVSwitch] = None,
    ):
        self.v_switch = v_switch

    def validate(self):
        if self.v_switch:
            for k in self.v_switch:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['VSwitch'] = []
        if self.v_switch is not None:
            for k in self.v_switch:
                result['VSwitch'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.v_switch = []
        if m.get('VSwitch') is not None:
            for k in m.get('VSwitch'):
                temp_model = DescribeVSwitchesResponseBodyVSwitchesVSwitch()
                self.v_switch.append(temp_model.from_map(k))
        return self


class DescribeVSwitchesResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        v_switches: DescribeVSwitchesResponseBodyVSwitches = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.v_switches = v_switches

    def validate(self):
        if self.v_switches:
            self.v_switches.validate()

    def to_map(self):
        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.v_switches is not None:
            result['VSwitches'] = self.v_switches.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('VSwitches') is not None:
            temp_model = DescribeVSwitchesResponseBodyVSwitches()
            self.v_switches = temp_model.from_map(m['VSwitches'])
        return self


class DescribeVSwitchesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVSwitchesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeVSwitchesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportBillDetailDataRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
        start_date: str = None,
        end_date: str = None,
    ):
        self.version = version
        self.start_date = start_date
        self.end_date = end_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class ExportBillDetailDataResponseBody(TeaModel):
    def __init__(
        self,
        file_path: str = None,
        request_id: str = None,
    ):
        self.file_path = file_path
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ExportBillDetailDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ExportBillDetailDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ExportBillDetailDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportImageRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
        image_id: str = None,
        ossbucket: str = None,
        ossregion_id: str = None,
        ossprefix: str = None,
        role_name: str = None,
    ):
        self.version = version
        self.image_id = image_id
        self.ossbucket = ossbucket
        self.ossregion_id = ossregion_id
        self.ossprefix = ossprefix
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.ossbucket is not None:
            result['OSSBucket'] = self.ossbucket
        if self.ossregion_id is not None:
            result['OSSRegionId'] = self.ossregion_id
        if self.ossprefix is not None:
            result['OSSPrefix'] = self.ossprefix
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('OSSBucket') is not None:
            self.ossbucket = m.get('OSSBucket')
        if m.get('OSSRegionId') is not None:
            self.ossregion_id = m.get('OSSRegionId')
        if m.get('OSSPrefix') is not None:
            self.ossprefix = m.get('OSSPrefix')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class ExportImageResponseBody(TeaModel):
    def __init__(
        self,
        exported_image_url: str = None,
        request_id: str = None,
    ):
        self.exported_image_url = exported_image_url
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.exported_image_url is not None:
            result['ExportedImageURL'] = self.exported_image_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExportedImageURL') is not None:
            self.exported_image_url = m.get('ExportedImageURL')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ExportImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ExportImageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ExportImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportMeasurementDataRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
        start_date: str = None,
        end_date: str = None,
    ):
        self.version = version
        self.start_date = start_date
        self.end_date = end_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class ExportMeasurementDataResponseBody(TeaModel):
    def __init__(
        self,
        file_path: str = None,
        request_id: str = None,
    ):
        self.file_path = file_path
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ExportMeasurementDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ExportMeasurementDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ExportMeasurementDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVmListRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        group_uuid: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.ali_uid = ali_uid
        self.group_uuid = group_uuid
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.group_uuid is not None:
            result['GroupUuid'] = self.group_uuid
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('GroupUuid') is not None:
            self.group_uuid = m.get('GroupUuid')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class GetVmListResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        request_id: str = None,
        msg: str = None,
        data: str = None,
        desc: str = None,
    ):
        # 业务状态码
        self.code = code
        # Id of the request
        self.request_id = request_id
        # 返回信息
        self.msg = msg
        # 业务数据
        self.data = data
        self.desc = desc

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.data is not None:
            result['Data'] = self.data
        if self.desc is not None:
            result['Desc'] = self.desc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        return self


class GetVmListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetVmListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetVmListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportKeyPairRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
        key_pair_name: str = None,
        public_key_body: str = None,
    ):
        self.version = version
        self.key_pair_name = key_pair_name
        self.public_key_body = public_key_body

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.public_key_body is not None:
            result['PublicKeyBody'] = self.public_key_body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('PublicKeyBody') is not None:
            self.public_key_body = m.get('PublicKeyBody')
        return self


class ImportKeyPairResponseBody(TeaModel):
    def __init__(
        self,
        key_pair_finger_print: str = None,
        key_pair_name: str = None,
        request_id: str = None,
    ):
        self.key_pair_finger_print = key_pair_finger_print
        self.key_pair_name = key_pair_name
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key_pair_finger_print is not None:
            result['KeyPairFingerPrint'] = self.key_pair_finger_print
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyPairFingerPrint') is not None:
            self.key_pair_finger_print = m.get('KeyPairFingerPrint')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ImportKeyPairResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ImportKeyPairResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ImportKeyPairResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class JoinPublicIpsToEpnInstanceRequest(TeaModel):
    def __init__(
        self,
        epninstance_id: str = None,
        instance_infos: str = None,
    ):
        self.epninstance_id = epninstance_id
        self.instance_infos = instance_infos

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.epninstance_id is not None:
            result['EPNInstanceId'] = self.epninstance_id
        if self.instance_infos is not None:
            result['InstanceInfos'] = self.instance_infos
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EPNInstanceId') is not None:
            self.epninstance_id = m.get('EPNInstanceId')
        if m.get('InstanceInfos') is not None:
            self.instance_infos = m.get('InstanceInfos')
        return self


class JoinPublicIpsToEpnInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class JoinPublicIpsToEpnInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: JoinPublicIpsToEpnInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = JoinPublicIpsToEpnInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class JoinSecurityGroupRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
        security_group_id: str = None,
        instance_id: str = None,
    ):
        self.version = version
        self.security_group_id = security_group_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class JoinSecurityGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class JoinSecurityGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: JoinSecurityGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = JoinSecurityGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class JoinVSwitchesToEpnInstanceRequest(TeaModel):
    def __init__(
        self,
        epninstance_id: str = None,
        v_switches_info: str = None,
    ):
        self.epninstance_id = epninstance_id
        self.v_switches_info = v_switches_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.epninstance_id is not None:
            result['EPNInstanceId'] = self.epninstance_id
        if self.v_switches_info is not None:
            result['VSwitchesInfo'] = self.v_switches_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EPNInstanceId') is not None:
            self.epninstance_id = m.get('EPNInstanceId')
        if m.get('VSwitchesInfo') is not None:
            self.v_switches_info = m.get('VSwitchesInfo')
        return self


class JoinVSwitchesToEpnInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class JoinVSwitchesToEpnInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: JoinVSwitchesToEpnInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = JoinVSwitchesToEpnInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LeaveSecurityGroupRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
        security_group_id: str = None,
        instance_id: str = None,
    ):
        self.version = version
        self.security_group_id = security_group_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class LeaveSecurityGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class LeaveSecurityGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: LeaveSecurityGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = LeaveSecurityGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListApplicationsRequest(TeaModel):
    def __init__(
        self,
        cluster_names: str = None,
        app_versions: str = None,
        level: str = None,
        out_app_info_params: str = None,
        page_number: int = None,
        page_size: int = None,
        min_date: str = None,
        max_date: str = None,
    ):
        self.cluster_names = cluster_names
        self.app_versions = app_versions
        self.level = level
        self.out_app_info_params = out_app_info_params
        self.page_number = page_number
        self.page_size = page_size
        self.min_date = min_date
        self.max_date = max_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_names is not None:
            result['ClusterNames'] = self.cluster_names
        if self.app_versions is not None:
            result['AppVersions'] = self.app_versions
        if self.level is not None:
            result['Level'] = self.level
        if self.out_app_info_params is not None:
            result['OutAppInfoParams'] = self.out_app_info_params
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.min_date is not None:
            result['MinDate'] = self.min_date
        if self.max_date is not None:
            result['MaxDate'] = self.max_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterNames') is not None:
            self.cluster_names = m.get('ClusterNames')
        if m.get('AppVersions') is not None:
            self.app_versions = m.get('AppVersions')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('OutAppInfoParams') is not None:
            self.out_app_info_params = m.get('OutAppInfoParams')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('MinDate') is not None:
            self.min_date = m.get('MinDate')
        if m.get('MaxDate') is not None:
            self.max_date = m.get('MaxDate')
        return self


class ListApplicationsResponseBodyApplicationsApplicationAppListApp(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_info: str = None,
    ):
        self.app_id = app_id
        self.app_info = app_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_info is not None:
            result['AppInfo'] = self.app_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppInfo') is not None:
            self.app_info = m.get('AppInfo')
        return self


class ListApplicationsResponseBodyApplicationsApplicationAppList(TeaModel):
    def __init__(
        self,
        app: List[ListApplicationsResponseBodyApplicationsApplicationAppListApp] = None,
    ):
        self.app = app

    def validate(self):
        if self.app:
            for k in self.app:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['App'] = []
        if self.app is not None:
            for k in self.app:
                result['App'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app = []
        if m.get('App') is not None:
            for k in m.get('App'):
                temp_model = ListApplicationsResponseBodyApplicationsApplicationAppListApp()
                self.app.append(temp_model.from_map(k))
        return self


class ListApplicationsResponseBodyApplicationsApplication(TeaModel):
    def __init__(
        self,
        app_list: ListApplicationsResponseBodyApplicationsApplicationAppList = None,
        cluster_name: str = None,
    ):
        self.app_list = app_list
        self.cluster_name = cluster_name

    def validate(self):
        if self.app_list:
            self.app_list.validate()

    def to_map(self):
        result = dict()
        if self.app_list is not None:
            result['AppList'] = self.app_list.to_map()
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppList') is not None:
            temp_model = ListApplicationsResponseBodyApplicationsApplicationAppList()
            self.app_list = temp_model.from_map(m['AppList'])
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        return self


class ListApplicationsResponseBodyApplications(TeaModel):
    def __init__(
        self,
        application: List[ListApplicationsResponseBodyApplicationsApplication] = None,
    ):
        self.application = application

    def validate(self):
        if self.application:
            for k in self.application:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Application'] = []
        if self.application is not None:
            for k in self.application:
                result['Application'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.application = []
        if m.get('Application') is not None:
            for k in m.get('Application'):
                temp_model = ListApplicationsResponseBodyApplicationsApplication()
                self.application.append(temp_model.from_map(k))
        return self


class ListApplicationsResponseBody(TeaModel):
    def __init__(
        self,
        applications: ListApplicationsResponseBodyApplications = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.applications = applications
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.applications:
            self.applications.validate()

    def to_map(self):
        result = dict()
        if self.applications is not None:
            result['Applications'] = self.applications.to_map()
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
        if m.get('Applications') is not None:
            temp_model = ListApplicationsResponseBodyApplications()
            self.applications = temp_model.from_map(m['Applications'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListApplicationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListApplicationsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListApplicationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyEpnInstanceRequest(TeaModel):
    def __init__(
        self,
        epninstance_id: str = None,
        epninstance_name: str = None,
        networking_model: str = None,
        internet_max_bandwidth_out: int = None,
    ):
        self.epninstance_id = epninstance_id
        self.epninstance_name = epninstance_name
        self.networking_model = networking_model
        self.internet_max_bandwidth_out = internet_max_bandwidth_out

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.epninstance_id is not None:
            result['EPNInstanceId'] = self.epninstance_id
        if self.epninstance_name is not None:
            result['EPNInstanceName'] = self.epninstance_name
        if self.networking_model is not None:
            result['NetworkingModel'] = self.networking_model
        if self.internet_max_bandwidth_out is not None:
            result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EPNInstanceId') is not None:
            self.epninstance_id = m.get('EPNInstanceId')
        if m.get('EPNInstanceName') is not None:
            self.epninstance_name = m.get('EPNInstanceName')
        if m.get('NetworkingModel') is not None:
            self.networking_model = m.get('NetworkingModel')
        if m.get('InternetMaxBandwidthOut') is not None:
            self.internet_max_bandwidth_out = m.get('InternetMaxBandwidthOut')
        return self


class ModifyEpnInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyEpnInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyEpnInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyEpnInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyImageAttributeRequest(TeaModel):
    def __init__(
        self,
        product: str = None,
        version: str = None,
        image_id: str = None,
        image_name: str = None,
    ):
        self.product = product
        self.version = version
        self.image_id = image_id
        self.image_name = image_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.product is not None:
            result['product'] = self.product
        if self.version is not None:
            result['Version'] = self.version
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('product') is not None:
            self.product = m.get('product')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        return self


class ModifyImageAttributeResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        request_id: str = None,
    ):
        self.code = code
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyImageAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyImageAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyImageAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyImageSharePermissionRequest(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        add_accounts: str = None,
        remove_accounts: str = None,
    ):
        self.image_id = image_id
        self.add_accounts = add_accounts
        self.remove_accounts = remove_accounts

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.add_accounts is not None:
            result['AddAccounts'] = self.add_accounts
        if self.remove_accounts is not None:
            result['RemoveAccounts'] = self.remove_accounts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('AddAccounts') is not None:
            self.add_accounts = m.get('AddAccounts')
        if m.get('RemoveAccounts') is not None:
            self.remove_accounts = m.get('RemoveAccounts')
        return self


class ModifyImageSharePermissionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyImageSharePermissionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyImageSharePermissionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyImageSharePermissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceAttributeRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
        instance_id: str = None,
        password: str = None,
        instance_name: str = None,
    ):
        self.version = version
        self.instance_id = instance_id
        self.password = password
        self.instance_name = instance_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.password is not None:
            result['Password'] = self.password
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        return self


class ModifyInstanceAttributeResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        request_id: str = None,
    ):
        self.code = code
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyInstanceAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyInstanceAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyInstanceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PreCreateEnsServiceRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
        ens_service_name: str = None,
        image_id: str = None,
        instance_spec: str = None,
        system_disk_size: str = None,
        data_disk_size: str = None,
        bandwidth_type: str = None,
        instance_bandwithd_limit: str = None,
        password: str = None,
        key_pair_name: str = None,
        user_data: str = None,
        net_level: str = None,
        scheduling_strategy: str = None,
        scheduling_price_strategy: str = None,
        buy_resources_detail: str = None,
    ):
        self.version = version
        self.ens_service_name = ens_service_name
        self.image_id = image_id
        self.instance_spec = instance_spec
        self.system_disk_size = system_disk_size
        self.data_disk_size = data_disk_size
        self.bandwidth_type = bandwidth_type
        self.instance_bandwithd_limit = instance_bandwithd_limit
        self.password = password
        self.key_pair_name = key_pair_name
        self.user_data = user_data
        self.net_level = net_level
        self.scheduling_strategy = scheduling_strategy
        self.scheduling_price_strategy = scheduling_price_strategy
        self.buy_resources_detail = buy_resources_detail

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.ens_service_name is not None:
            result['EnsServiceName'] = self.ens_service_name
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size
        if self.bandwidth_type is not None:
            result['BandwidthType'] = self.bandwidth_type
        if self.instance_bandwithd_limit is not None:
            result['InstanceBandwithdLimit'] = self.instance_bandwithd_limit
        if self.password is not None:
            result['Password'] = self.password
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.net_level is not None:
            result['NetLevel'] = self.net_level
        if self.scheduling_strategy is not None:
            result['SchedulingStrategy'] = self.scheduling_strategy
        if self.scheduling_price_strategy is not None:
            result['SchedulingPriceStrategy'] = self.scheduling_price_strategy
        if self.buy_resources_detail is not None:
            result['BuyResourcesDetail'] = self.buy_resources_detail
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('EnsServiceName') is not None:
            self.ens_service_name = m.get('EnsServiceName')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')
        if m.get('BandwidthType') is not None:
            self.bandwidth_type = m.get('BandwidthType')
        if m.get('InstanceBandwithdLimit') is not None:
            self.instance_bandwithd_limit = m.get('InstanceBandwithdLimit')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('NetLevel') is not None:
            self.net_level = m.get('NetLevel')
        if m.get('SchedulingStrategy') is not None:
            self.scheduling_strategy = m.get('SchedulingStrategy')
        if m.get('SchedulingPriceStrategy') is not None:
            self.scheduling_price_strategy = m.get('SchedulingPriceStrategy')
        if m.get('BuyResourcesDetail') is not None:
            self.buy_resources_detail = m.get('BuyResourcesDetail')
        return self


class PreCreateEnsServiceResponseBody(TeaModel):
    def __init__(
        self,
        buy_resources_detail: str = None,
        code: int = None,
        ens_service_id: str = None,
        net_level: str = None,
        request_id: str = None,
    ):
        self.buy_resources_detail = buy_resources_detail
        self.code = code
        self.ens_service_id = ens_service_id
        self.net_level = net_level
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.buy_resources_detail is not None:
            result['BuyResourcesDetail'] = self.buy_resources_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.ens_service_id is not None:
            result['EnsServiceId'] = self.ens_service_id
        if self.net_level is not None:
            result['NetLevel'] = self.net_level
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuyResourcesDetail') is not None:
            self.buy_resources_detail = m.get('BuyResourcesDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('EnsServiceId') is not None:
            self.ens_service_id = m.get('EnsServiceId')
        if m.get('NetLevel') is not None:
            self.net_level = m.get('NetLevel')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PreCreateEnsServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PreCreateEnsServiceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = PreCreateEnsServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushApplicationDataRequest(TeaModel):
    def __init__(
        self,
        data: str = None,
        app_id: str = None,
        timeout: int = None,
        push_strategy: str = None,
    ):
        self.data = data
        self.app_id = app_id
        self.timeout = timeout
        self.push_strategy = push_strategy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.push_strategy is not None:
            result['PushStrategy'] = self.push_strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('PushStrategy') is not None:
            self.push_strategy = m.get('PushStrategy')
        return self


class PushApplicationDataResponseBodyPushResultsPushResult(TeaModel):
    def __init__(
        self,
        name: str = None,
        result_code: int = None,
        result_descrip: str = None,
        version: str = None,
    ):
        self.name = name
        self.result_code = result_code
        self.result_descrip = result_descrip
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_descrip is not None:
            result['ResultDescrip'] = self.result_descrip
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultDescrip') is not None:
            self.result_descrip = m.get('ResultDescrip')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class PushApplicationDataResponseBodyPushResults(TeaModel):
    def __init__(
        self,
        push_result: List[PushApplicationDataResponseBodyPushResultsPushResult] = None,
    ):
        self.push_result = push_result

    def validate(self):
        if self.push_result:
            for k in self.push_result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['PushResult'] = []
        if self.push_result is not None:
            for k in self.push_result:
                result['PushResult'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.push_result = []
        if m.get('PushResult') is not None:
            for k in m.get('PushResult'):
                temp_model = PushApplicationDataResponseBodyPushResultsPushResult()
                self.push_result.append(temp_model.from_map(k))
        return self


class PushApplicationDataResponseBody(TeaModel):
    def __init__(
        self,
        push_results: PushApplicationDataResponseBodyPushResults = None,
        request_id: str = None,
    ):
        self.push_results = push_results
        self.request_id = request_id

    def validate(self):
        if self.push_results:
            self.push_results.validate()

    def to_map(self):
        result = dict()
        if self.push_results is not None:
            result['PushResults'] = self.push_results.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PushResults') is not None:
            temp_model = PushApplicationDataResponseBodyPushResults()
            self.push_results = temp_model.from_map(m['PushResults'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PushApplicationDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PushApplicationDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = PushApplicationDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RebootInstanceRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
        instance_id: str = None,
        force_stop: str = None,
    ):
        self.version = version
        self.instance_id = instance_id
        self.force_stop = force_stop

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.force_stop is not None:
            result['ForceStop'] = self.force_stop
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ForceStop') is not None:
            self.force_stop = m.get('ForceStop')
        return self


class RebootInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        request_id: str = None,
    ):
        self.code = code
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RebootInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RebootInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RebootInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReInitDiskRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
        disk_id: str = None,
        image_id: str = None,
    ):
        self.version = version
        self.disk_id = disk_id
        self.image_id = image_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        return self


class ReInitDiskResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        request_id: str = None,
    ):
        self.code = code
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReInitDiskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ReInitDiskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ReInitDiskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseEipAddressRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
        ens_region_id: str = None,
        eips: str = None,
    ):
        self.version = version
        self.ens_region_id = ens_region_id
        self.eips = eips

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.eips is not None:
            result['Eips'] = self.eips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('Eips') is not None:
            self.eips = m.get('Eips')
        return self


class ReleaseEipAddressResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReleaseEipAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ReleaseEipAddressResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ReleaseEipAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleasePostPaidInstanceRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
        instance_id: str = None,
    ):
        self.version = version
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ReleasePostPaidInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReleasePostPaidInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ReleasePostPaidInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ReleasePostPaidInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleasePrePaidInstanceRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
        instance_id: str = None,
    ):
        self.version = version
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ReleasePrePaidInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReleasePrePaidInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ReleasePrePaidInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ReleasePrePaidInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemovePublicIpsFromEpnInstanceRequest(TeaModel):
    def __init__(
        self,
        epninstance_id: str = None,
        instance_infos: str = None,
    ):
        self.epninstance_id = epninstance_id
        self.instance_infos = instance_infos

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.epninstance_id is not None:
            result['EPNInstanceId'] = self.epninstance_id
        if self.instance_infos is not None:
            result['InstanceInfos'] = self.instance_infos
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EPNInstanceId') is not None:
            self.epninstance_id = m.get('EPNInstanceId')
        if m.get('InstanceInfos') is not None:
            self.instance_infos = m.get('InstanceInfos')
        return self


class RemovePublicIpsFromEpnInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemovePublicIpsFromEpnInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemovePublicIpsFromEpnInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RemovePublicIpsFromEpnInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveVSwitchesFromEpnInstanceRequest(TeaModel):
    def __init__(
        self,
        epninstance_id: str = None,
        v_switches_info: str = None,
    ):
        self.epninstance_id = epninstance_id
        self.v_switches_info = v_switches_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.epninstance_id is not None:
            result['EPNInstanceId'] = self.epninstance_id
        if self.v_switches_info is not None:
            result['VSwitchesInfo'] = self.v_switches_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EPNInstanceId') is not None:
            self.epninstance_id = m.get('EPNInstanceId')
        if m.get('VSwitchesInfo') is not None:
            self.v_switches_info = m.get('VSwitchesInfo')
        return self


class RemoveVSwitchesFromEpnInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveVSwitchesFromEpnInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveVSwitchesFromEpnInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RemoveVSwitchesFromEpnInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RescaleApplicationRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        rescale_type: str = None,
        rescale_level: str = None,
        resource_selector: str = None,
        to_app_version: str = None,
        timeout: int = None,
    ):
        self.app_id = app_id
        self.rescale_type = rescale_type
        self.rescale_level = rescale_level
        self.resource_selector = resource_selector
        self.to_app_version = to_app_version
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.rescale_type is not None:
            result['RescaleType'] = self.rescale_type
        if self.rescale_level is not None:
            result['RescaleLevel'] = self.rescale_level
        if self.resource_selector is not None:
            result['ResourceSelector'] = self.resource_selector
        if self.to_app_version is not None:
            result['ToAppVersion'] = self.to_app_version
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RescaleType') is not None:
            self.rescale_type = m.get('RescaleType')
        if m.get('RescaleLevel') is not None:
            self.rescale_level = m.get('RescaleLevel')
        if m.get('ResourceSelector') is not None:
            self.resource_selector = m.get('ResourceSelector')
        if m.get('ToAppVersion') is not None:
            self.to_app_version = m.get('ToAppVersion')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        return self


class RescaleApplicationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RescaleApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RescaleApplicationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RescaleApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RevokeSecurityGroupRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
        ip_protocol: str = None,
        port_range: str = None,
        security_group_id: str = None,
        policy: str = None,
        priority: int = None,
        source_cidr_ip: str = None,
        source_port_range: str = None,
    ):
        self.version = version
        self.ip_protocol = ip_protocol
        self.port_range = port_range
        self.security_group_id = security_group_id
        self.policy = policy
        self.priority = priority
        self.source_cidr_ip = source_cidr_ip
        self.source_port_range = source_port_range

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol
        if self.port_range is not None:
            result['PortRange'] = self.port_range
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.source_cidr_ip is not None:
            result['SourceCidrIp'] = self.source_cidr_ip
        if self.source_port_range is not None:
            result['SourcePortRange'] = self.source_port_range
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')
        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('SourceCidrIp') is not None:
            self.source_cidr_ip = m.get('SourceCidrIp')
        if m.get('SourcePortRange') is not None:
            self.source_port_range = m.get('SourcePortRange')
        return self


class RevokeSecurityGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RevokeSecurityGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RevokeSecurityGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RevokeSecurityGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RevokeSecurityGroupEgressRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
        ip_protocol: str = None,
        port_range: str = None,
        security_group_id: str = None,
        policy: str = None,
        priority: int = None,
        dest_cidr_ip: str = None,
        source_port_range: str = None,
    ):
        self.version = version
        self.ip_protocol = ip_protocol
        self.port_range = port_range
        self.security_group_id = security_group_id
        self.policy = policy
        self.priority = priority
        self.dest_cidr_ip = dest_cidr_ip
        self.source_port_range = source_port_range

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol
        if self.port_range is not None:
            result['PortRange'] = self.port_range
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.dest_cidr_ip is not None:
            result['DestCidrIp'] = self.dest_cidr_ip
        if self.source_port_range is not None:
            result['SourcePortRange'] = self.source_port_range
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')
        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('DestCidrIp') is not None:
            self.dest_cidr_ip = m.get('DestCidrIp')
        if m.get('SourcePortRange') is not None:
            self.source_port_range = m.get('SourcePortRange')
        return self


class RevokeSecurityGroupEgressResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RevokeSecurityGroupEgressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RevokeSecurityGroupEgressResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RevokeSecurityGroupEgressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RollbackApplicationRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        from_app_version: str = None,
        to_app_version: str = None,
        timeout: int = None,
    ):
        self.app_id = app_id
        self.from_app_version = from_app_version
        self.to_app_version = to_app_version
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.from_app_version is not None:
            result['FromAppVersion'] = self.from_app_version
        if self.to_app_version is not None:
            result['ToAppVersion'] = self.to_app_version
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('FromAppVersion') is not None:
            self.from_app_version = m.get('FromAppVersion')
        if m.get('ToAppVersion') is not None:
            self.to_app_version = m.get('ToAppVersion')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        return self


class RollbackApplicationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RollbackApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RollbackApplicationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RollbackApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunServiceScheduleRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        uuid: str = None,
        client_ip: str = None,
        service_action: str = None,
        pod_config_name: str = None,
        pre_locked_timeout: int = None,
        directorys: str = None,
        service_commands: str = None,
        schedule_strategy: str = None,
    ):
        self.app_id = app_id
        self.uuid = uuid
        self.client_ip = client_ip
        self.service_action = service_action
        self.pod_config_name = pod_config_name
        self.pre_locked_timeout = pre_locked_timeout
        self.directorys = directorys
        self.service_commands = service_commands
        self.schedule_strategy = schedule_strategy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.service_action is not None:
            result['ServiceAction'] = self.service_action
        if self.pod_config_name is not None:
            result['PodConfigName'] = self.pod_config_name
        if self.pre_locked_timeout is not None:
            result['PreLockedTimeout'] = self.pre_locked_timeout
        if self.directorys is not None:
            result['Directorys'] = self.directorys
        if self.service_commands is not None:
            result['ServiceCommands'] = self.service_commands
        if self.schedule_strategy is not None:
            result['ScheduleStrategy'] = self.schedule_strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('ServiceAction') is not None:
            self.service_action = m.get('ServiceAction')
        if m.get('PodConfigName') is not None:
            self.pod_config_name = m.get('PodConfigName')
        if m.get('PreLockedTimeout') is not None:
            self.pre_locked_timeout = m.get('PreLockedTimeout')
        if m.get('Directorys') is not None:
            self.directorys = m.get('Directorys')
        if m.get('ServiceCommands') is not None:
            self.service_commands = m.get('ServiceCommands')
        if m.get('ScheduleStrategy') is not None:
            self.schedule_strategy = m.get('ScheduleStrategy')
        return self


class RunServiceScheduleResponseBodyCommandResultsCommandResult(TeaModel):
    def __init__(
        self,
        command: str = None,
        container_name: str = None,
        result_msg: str = None,
    ):
        self.command = command
        self.container_name = container_name
        self.result_msg = result_msg

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.command is not None:
            result['Command'] = self.command
        if self.container_name is not None:
            result['ContainerName'] = self.container_name
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('ContainerName') is not None:
            self.container_name = m.get('ContainerName')
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        return self


class RunServiceScheduleResponseBodyCommandResults(TeaModel):
    def __init__(
        self,
        command_result: List[RunServiceScheduleResponseBodyCommandResultsCommandResult] = None,
    ):
        self.command_result = command_result

    def validate(self):
        if self.command_result:
            for k in self.command_result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['CommandResult'] = []
        if self.command_result is not None:
            for k in self.command_result:
                result['CommandResult'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.command_result = []
        if m.get('CommandResult') is not None:
            for k in m.get('CommandResult'):
                temp_model = RunServiceScheduleResponseBodyCommandResultsCommandResult()
                self.command_result.append(temp_model.from_map(k))
        return self


class RunServiceScheduleResponseBody(TeaModel):
    def __init__(
        self,
        command_results: RunServiceScheduleResponseBodyCommandResults = None,
        index: int = None,
        instance_id: str = None,
        instance_ip: str = None,
        instance_port: int = None,
        request_id: str = None,
        request_repeated: str = None,
        tcp_ports: bool = None,
    ):
        self.command_results = command_results
        self.index = index
        self.instance_id = instance_id
        self.instance_ip = instance_ip
        self.instance_port = instance_port
        self.request_id = request_id
        self.request_repeated = request_repeated
        self.tcp_ports = tcp_ports

    def validate(self):
        if self.command_results:
            self.command_results.validate()

    def to_map(self):
        result = dict()
        if self.command_results is not None:
            result['CommandResults'] = self.command_results.to_map()
        if self.index is not None:
            result['Index'] = self.index
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_ip is not None:
            result['InstanceIp'] = self.instance_ip
        if self.instance_port is not None:
            result['InstancePort'] = self.instance_port
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.request_repeated is not None:
            result['RequestRepeated'] = self.request_repeated
        if self.tcp_ports is not None:
            result['TcpPorts'] = self.tcp_ports
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandResults') is not None:
            temp_model = RunServiceScheduleResponseBodyCommandResults()
            self.command_results = temp_model.from_map(m['CommandResults'])
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceIp') is not None:
            self.instance_ip = m.get('InstanceIp')
        if m.get('InstancePort') is not None:
            self.instance_port = m.get('InstancePort')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RequestRepeated') is not None:
            self.request_repeated = m.get('RequestRepeated')
        if m.get('TcpPorts') is not None:
            self.tcp_ports = m.get('TcpPorts')
        return self


class RunServiceScheduleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RunServiceScheduleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RunServiceScheduleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SchedulePodRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        group_uuid: str = None,
        workload_uuid: str = None,
        tenant: str = None,
        regions: str = None,
        area_codes: str = None,
        isps: str = None,
        requirements: str = None,
        labels: str = None,
        resource_attribute: str = None,
    ):
        self.ali_uid = ali_uid
        self.group_uuid = group_uuid
        self.workload_uuid = workload_uuid
        self.tenant = tenant
        self.regions = regions
        self.area_codes = area_codes
        self.isps = isps
        self.requirements = requirements
        self.labels = labels
        self.resource_attribute = resource_attribute

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.group_uuid is not None:
            result['GroupUuid'] = self.group_uuid
        if self.workload_uuid is not None:
            result['WorkloadUuid'] = self.workload_uuid
        if self.tenant is not None:
            result['Tenant'] = self.tenant
        if self.regions is not None:
            result['Regions'] = self.regions
        if self.area_codes is not None:
            result['AreaCodes'] = self.area_codes
        if self.isps is not None:
            result['Isps'] = self.isps
        if self.requirements is not None:
            result['Requirements'] = self.requirements
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.resource_attribute is not None:
            result['ResourceAttribute'] = self.resource_attribute
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('GroupUuid') is not None:
            self.group_uuid = m.get('GroupUuid')
        if m.get('WorkloadUuid') is not None:
            self.workload_uuid = m.get('WorkloadUuid')
        if m.get('Tenant') is not None:
            self.tenant = m.get('Tenant')
        if m.get('Regions') is not None:
            self.regions = m.get('Regions')
        if m.get('AreaCodes') is not None:
            self.area_codes = m.get('AreaCodes')
        if m.get('Isps') is not None:
            self.isps = m.get('Isps')
        if m.get('Requirements') is not None:
            self.requirements = m.get('Requirements')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('ResourceAttribute') is not None:
            self.resource_attribute = m.get('ResourceAttribute')
        return self


class SchedulePodResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: int = None,
        msg: str = None,
        desc: str = None,
        data: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.code = code
        self.msg = msg
        self.desc = desc
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class SchedulePodResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SchedulePodResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SchedulePodResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartEpnInstanceRequest(TeaModel):
    def __init__(
        self,
        epninstance_id: str = None,
    ):
        self.epninstance_id = epninstance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.epninstance_id is not None:
            result['EPNInstanceId'] = self.epninstance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EPNInstanceId') is not None:
            self.epninstance_id = m.get('EPNInstanceId')
        return self


class StartEpnInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartEpnInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartEpnInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StartEpnInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartInstanceRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
        instance_id: str = None,
    ):
        self.version = version
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class StartInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        request_id: str = None,
    ):
        self.code = code
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StartInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopEpnInstanceRequest(TeaModel):
    def __init__(
        self,
        epninstance_id: str = None,
    ):
        self.epninstance_id = epninstance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.epninstance_id is not None:
            result['EPNInstanceId'] = self.epninstance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EPNInstanceId') is not None:
            self.epninstance_id = m.get('EPNInstanceId')
        return self


class StopEpnInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopEpnInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopEpnInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StopEpnInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopInstanceRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
        instance_id: str = None,
        force_stop: str = None,
    ):
        self.version = version
        self.instance_id = instance_id
        self.force_stop = force_stop

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.force_stop is not None:
            result['ForceStop'] = self.force_stop
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ForceStop') is not None:
            self.force_stop = m.get('ForceStop')
        return self


class StopInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        request_id: str = None,
    ):
        self.code = code
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StopInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnassociateEipAddressRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
        ens_region_id: str = None,
        eip: str = None,
        instance_id_internet_ip: str = None,
    ):
        self.version = version
        self.ens_region_id = ens_region_id
        self.eip = eip
        self.instance_id_internet_ip = instance_id_internet_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.eip is not None:
            result['Eip'] = self.eip
        if self.instance_id_internet_ip is not None:
            result['InstanceIdInternetIp'] = self.instance_id_internet_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('Eip') is not None:
            self.eip = m.get('Eip')
        if m.get('InstanceIdInternetIp') is not None:
            self.instance_id_internet_ip = m.get('InstanceIdInternetIp')
        return self


class UnassociateEipAddressResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UnassociateEipAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UnassociateEipAddressResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UnassociateEipAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeApplicationRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        template: str = None,
        timeout: int = None,
    ):
        self.app_id = app_id
        self.template = template
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.template is not None:
            result['Template'] = self.template
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        return self


class UpgradeApplicationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpgradeApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpgradeApplicationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpgradeApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


