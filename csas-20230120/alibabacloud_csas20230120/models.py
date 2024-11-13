# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class AttachApplication2ConnectorRequest(TeaModel):
    def __init__(
        self,
        application_ids: List[str] = None,
        connector_id: str = None,
    ):
        # This parameter is required.
        self.application_ids = application_ids
        # ConnectorID。
        # 
        # This parameter is required.
        self.connector_id = connector_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_ids is not None:
            result['ApplicationIds'] = self.application_ids
        if self.connector_id is not None:
            result['ConnectorId'] = self.connector_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationIds') is not None:
            self.application_ids = m.get('ApplicationIds')
        if m.get('ConnectorId') is not None:
            self.connector_id = m.get('ConnectorId')
        return self


class AttachApplication2ConnectorShrinkRequest(TeaModel):
    def __init__(
        self,
        application_ids_shrink: str = None,
        connector_id: str = None,
    ):
        # This parameter is required.
        self.application_ids_shrink = application_ids_shrink
        # ConnectorID。
        # 
        # This parameter is required.
        self.connector_id = connector_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_ids_shrink is not None:
            result['ApplicationIds'] = self.application_ids_shrink
        if self.connector_id is not None:
            result['ConnectorId'] = self.connector_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationIds') is not None:
            self.application_ids_shrink = m.get('ApplicationIds')
        if m.get('ConnectorId') is not None:
            self.connector_id = m.get('ConnectorId')
        return self


class AttachApplication2ConnectorResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AttachApplication2ConnectorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AttachApplication2ConnectorResponseBody = None,
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
            temp_model = AttachApplication2ConnectorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateClientUserRequest(TeaModel):
    def __init__(
        self,
        department_id: str = None,
        description: str = None,
        email: str = None,
        idp_config_id: str = None,
        mobile_number: str = None,
        password: str = None,
        username: str = None,
    ):
        self.department_id = department_id
        self.description = description
        # This parameter is required.
        self.email = email
        # This parameter is required.
        self.idp_config_id = idp_config_id
        self.mobile_number = mobile_number
        self.password = password
        # This parameter is required.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.department_id is not None:
            result['DepartmentId'] = self.department_id
        if self.description is not None:
            result['Description'] = self.description
        if self.email is not None:
            result['Email'] = self.email
        if self.idp_config_id is not None:
            result['IdpConfigId'] = self.idp_config_id
        if self.mobile_number is not None:
            result['MobileNumber'] = self.mobile_number
        if self.password is not None:
            result['Password'] = self.password
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('IdpConfigId') is not None:
            self.idp_config_id = m.get('IdpConfigId')
        if m.get('MobileNumber') is not None:
            self.mobile_number = m.get('MobileNumber')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class CreateClientUserResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateClientUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateClientUserResponseBody = None,
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
            temp_model = CreateClientUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDynamicRouteRequest(TeaModel):
    def __init__(
        self,
        application_ids: List[str] = None,
        application_type: str = None,
        description: str = None,
        dynamic_route_type: str = None,
        name: str = None,
        next_hop: str = None,
        priority: int = None,
        region_ids: List[str] = None,
        status: str = None,
        tag_ids: List[str] = None,
    ):
        self.application_ids = application_ids
        # This parameter is required.
        self.application_type = application_type
        self.description = description
        # This parameter is required.
        self.dynamic_route_type = dynamic_route_type
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.next_hop = next_hop
        # This parameter is required.
        self.priority = priority
        # This parameter is required.
        self.region_ids = region_ids
        # This parameter is required.
        self.status = status
        self.tag_ids = tag_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_ids is not None:
            result['ApplicationIds'] = self.application_ids
        if self.application_type is not None:
            result['ApplicationType'] = self.application_type
        if self.description is not None:
            result['Description'] = self.description
        if self.dynamic_route_type is not None:
            result['DynamicRouteType'] = self.dynamic_route_type
        if self.name is not None:
            result['Name'] = self.name
        if self.next_hop is not None:
            result['NextHop'] = self.next_hop
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids
        if self.status is not None:
            result['Status'] = self.status
        if self.tag_ids is not None:
            result['TagIds'] = self.tag_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationIds') is not None:
            self.application_ids = m.get('ApplicationIds')
        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DynamicRouteType') is not None:
            self.dynamic_route_type = m.get('DynamicRouteType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NextHop') is not None:
            self.next_hop = m.get('NextHop')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('RegionIds') is not None:
            self.region_ids = m.get('RegionIds')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TagIds') is not None:
            self.tag_ids = m.get('TagIds')
        return self


class CreateDynamicRouteResponseBody(TeaModel):
    def __init__(
        self,
        dynamic_route_id: str = None,
        request_id: str = None,
    ):
        self.dynamic_route_id = dynamic_route_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dynamic_route_id is not None:
            result['DynamicRouteId'] = self.dynamic_route_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DynamicRouteId') is not None:
            self.dynamic_route_id = m.get('DynamicRouteId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDynamicRouteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDynamicRouteResponseBody = None,
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
            temp_model = CreateDynamicRouteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIdpDepartmentRequest(TeaModel):
    def __init__(
        self,
        department_name: str = None,
        idp_config_id: str = None,
    ):
        # This parameter is required.
        self.department_name = department_name
        # This parameter is required.
        self.idp_config_id = idp_config_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.department_name is not None:
            result['DepartmentName'] = self.department_name
        if self.idp_config_id is not None:
            result['IdpConfigId'] = self.idp_config_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DepartmentName') is not None:
            self.department_name = m.get('DepartmentName')
        if m.get('IdpConfigId') is not None:
            self.idp_config_id = m.get('IdpConfigId')
        return self


class CreateIdpDepartmentResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateIdpDepartmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateIdpDepartmentResponseBody = None,
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
            temp_model = CreateIdpDepartmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePrivateAccessApplicationRequestPortRanges(TeaModel):
    def __init__(
        self,
        begin: int = None,
        end: int = None,
    ):
        # This parameter is required.
        self.begin = begin
        # This parameter is required.
        self.end = end

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.end is not None:
            result['End'] = self.end
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('End') is not None:
            self.end = m.get('End')
        return self


class CreatePrivateAccessApplicationRequest(TeaModel):
    def __init__(
        self,
        addresses: List[str] = None,
        browser_access_status: str = None,
        description: str = None,
        l_7proxy_domain_automatic_prefix: str = None,
        l_7proxy_domain_custom: str = None,
        name: str = None,
        port_ranges: List[CreatePrivateAccessApplicationRequestPortRanges] = None,
        protocol: str = None,
        status: str = None,
        tag_ids: List[str] = None,
    ):
        # This parameter is required.
        self.addresses = addresses
        self.browser_access_status = browser_access_status
        self.description = description
        self.l_7proxy_domain_automatic_prefix = l_7proxy_domain_automatic_prefix
        self.l_7proxy_domain_custom = l_7proxy_domain_custom
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.port_ranges = port_ranges
        # This parameter is required.
        self.protocol = protocol
        # This parameter is required.
        self.status = status
        self.tag_ids = tag_ids

    def validate(self):
        if self.port_ranges:
            for k in self.port_ranges:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.addresses is not None:
            result['Addresses'] = self.addresses
        if self.browser_access_status is not None:
            result['BrowserAccessStatus'] = self.browser_access_status
        if self.description is not None:
            result['Description'] = self.description
        if self.l_7proxy_domain_automatic_prefix is not None:
            result['L7ProxyDomainAutomaticPrefix'] = self.l_7proxy_domain_automatic_prefix
        if self.l_7proxy_domain_custom is not None:
            result['L7ProxyDomainCustom'] = self.l_7proxy_domain_custom
        if self.name is not None:
            result['Name'] = self.name
        result['PortRanges'] = []
        if self.port_ranges is not None:
            for k in self.port_ranges:
                result['PortRanges'].append(k.to_map() if k else None)
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.status is not None:
            result['Status'] = self.status
        if self.tag_ids is not None:
            result['TagIds'] = self.tag_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Addresses') is not None:
            self.addresses = m.get('Addresses')
        if m.get('BrowserAccessStatus') is not None:
            self.browser_access_status = m.get('BrowserAccessStatus')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('L7ProxyDomainAutomaticPrefix') is not None:
            self.l_7proxy_domain_automatic_prefix = m.get('L7ProxyDomainAutomaticPrefix')
        if m.get('L7ProxyDomainCustom') is not None:
            self.l_7proxy_domain_custom = m.get('L7ProxyDomainCustom')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.port_ranges = []
        if m.get('PortRanges') is not None:
            for k in m.get('PortRanges'):
                temp_model = CreatePrivateAccessApplicationRequestPortRanges()
                self.port_ranges.append(temp_model.from_map(k))
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TagIds') is not None:
            self.tag_ids = m.get('TagIds')
        return self


class CreatePrivateAccessApplicationResponseBody(TeaModel):
    def __init__(
        self,
        application_id: str = None,
        request_id: str = None,
    ):
        self.application_id = application_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreatePrivateAccessApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatePrivateAccessApplicationResponseBody = None,
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
            temp_model = CreatePrivateAccessApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePrivateAccessPolicyRequestCustomUserAttributes(TeaModel):
    def __init__(
        self,
        idp_id: int = None,
        relation: str = None,
        user_group_type: str = None,
        value: str = None,
    ):
        self.idp_id = idp_id
        self.relation = relation
        self.user_group_type = user_group_type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.idp_id is not None:
            result['IdpId'] = self.idp_id
        if self.relation is not None:
            result['Relation'] = self.relation
        if self.user_group_type is not None:
            result['UserGroupType'] = self.user_group_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdpId') is not None:
            self.idp_id = m.get('IdpId')
        if m.get('Relation') is not None:
            self.relation = m.get('Relation')
        if m.get('UserGroupType') is not None:
            self.user_group_type = m.get('UserGroupType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreatePrivateAccessPolicyRequest(TeaModel):
    def __init__(
        self,
        application_ids: List[str] = None,
        application_type: str = None,
        custom_user_attributes: List[CreatePrivateAccessPolicyRequestCustomUserAttributes] = None,
        description: str = None,
        device_attribute_action: str = None,
        device_attribute_id: str = None,
        name: str = None,
        policy_action: str = None,
        priority: int = None,
        status: str = None,
        tag_ids: List[str] = None,
        user_group_ids: List[str] = None,
        user_group_mode: str = None,
    ):
        self.application_ids = application_ids
        # This parameter is required.
        self.application_type = application_type
        self.custom_user_attributes = custom_user_attributes
        self.description = description
        self.device_attribute_action = device_attribute_action
        self.device_attribute_id = device_attribute_id
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.policy_action = policy_action
        # This parameter is required.
        self.priority = priority
        # This parameter is required.
        self.status = status
        # 内网访问标签ID集合。最多可输入100个内网访问标签ID。当**ApplicationType**为**Tag时**，必填。和**ApplicationIds**互斥。
        self.tag_ids = tag_ids
        self.user_group_ids = user_group_ids
        # 内网访问策略的用户组类型。取值：
        # - **Normal**：普通用户组。
        # - **Custom**：自定义用户组。
        # 
        # This parameter is required.
        self.user_group_mode = user_group_mode

    def validate(self):
        if self.custom_user_attributes:
            for k in self.custom_user_attributes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_ids is not None:
            result['ApplicationIds'] = self.application_ids
        if self.application_type is not None:
            result['ApplicationType'] = self.application_type
        result['CustomUserAttributes'] = []
        if self.custom_user_attributes is not None:
            for k in self.custom_user_attributes:
                result['CustomUserAttributes'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.device_attribute_action is not None:
            result['DeviceAttributeAction'] = self.device_attribute_action
        if self.device_attribute_id is not None:
            result['DeviceAttributeId'] = self.device_attribute_id
        if self.name is not None:
            result['Name'] = self.name
        if self.policy_action is not None:
            result['PolicyAction'] = self.policy_action
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.status is not None:
            result['Status'] = self.status
        if self.tag_ids is not None:
            result['TagIds'] = self.tag_ids
        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids
        if self.user_group_mode is not None:
            result['UserGroupMode'] = self.user_group_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationIds') is not None:
            self.application_ids = m.get('ApplicationIds')
        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')
        self.custom_user_attributes = []
        if m.get('CustomUserAttributes') is not None:
            for k in m.get('CustomUserAttributes'):
                temp_model = CreatePrivateAccessPolicyRequestCustomUserAttributes()
                self.custom_user_attributes.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DeviceAttributeAction') is not None:
            self.device_attribute_action = m.get('DeviceAttributeAction')
        if m.get('DeviceAttributeId') is not None:
            self.device_attribute_id = m.get('DeviceAttributeId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PolicyAction') is not None:
            self.policy_action = m.get('PolicyAction')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TagIds') is not None:
            self.tag_ids = m.get('TagIds')
        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')
        if m.get('UserGroupMode') is not None:
            self.user_group_mode = m.get('UserGroupMode')
        return self


class CreatePrivateAccessPolicyResponseBody(TeaModel):
    def __init__(
        self,
        policy_id: str = None,
        request_id: str = None,
    ):
        self.policy_id = policy_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreatePrivateAccessPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatePrivateAccessPolicyResponseBody = None,
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
            temp_model = CreatePrivateAccessPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePrivateAccessTagRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
    ):
        self.description = description
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreatePrivateAccessTagResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tag_id: str = None,
    ):
        self.request_id = request_id
        self.tag_id = tag_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        return self


class CreatePrivateAccessTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatePrivateAccessTagResponseBody = None,
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
            temp_model = CreatePrivateAccessTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRegistrationPolicyRequestCompanyLimitCount(TeaModel):
    def __init__(
        self,
        all: int = None,
        mobile: int = None,
        pc: int = None,
    ):
        self.all = all
        self.mobile = mobile
        self.pc = pc

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.pc is not None:
            result['PC'] = self.pc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('PC') is not None:
            self.pc = m.get('PC')
        return self


class CreateRegistrationPolicyRequestPersonalLimitCount(TeaModel):
    def __init__(
        self,
        all: int = None,
        mobile: int = None,
        pc: int = None,
    ):
        self.all = all
        self.mobile = mobile
        self.pc = pc

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.pc is not None:
            result['PC'] = self.pc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('PC') is not None:
            self.pc = m.get('PC')
        return self


class CreateRegistrationPolicyRequest(TeaModel):
    def __init__(
        self,
        company_limit_count: CreateRegistrationPolicyRequestCompanyLimitCount = None,
        company_limit_type: str = None,
        description: str = None,
        match_mode: str = None,
        name: str = None,
        personal_limit_count: CreateRegistrationPolicyRequestPersonalLimitCount = None,
        personal_limit_type: str = None,
        priority: int = None,
        status: str = None,
        user_group_ids: List[str] = None,
        whitelist: List[str] = None,
    ):
        self.company_limit_count = company_limit_count
        # This parameter is required.
        self.company_limit_type = company_limit_type
        self.description = description
        # This parameter is required.
        self.match_mode = match_mode
        # This parameter is required.
        self.name = name
        self.personal_limit_count = personal_limit_count
        # This parameter is required.
        self.personal_limit_type = personal_limit_type
        self.priority = priority
        # This parameter is required.
        self.status = status
        self.user_group_ids = user_group_ids
        self.whitelist = whitelist

    def validate(self):
        if self.company_limit_count:
            self.company_limit_count.validate()
        if self.personal_limit_count:
            self.personal_limit_count.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.company_limit_count is not None:
            result['CompanyLimitCount'] = self.company_limit_count.to_map()
        if self.company_limit_type is not None:
            result['CompanyLimitType'] = self.company_limit_type
        if self.description is not None:
            result['Description'] = self.description
        if self.match_mode is not None:
            result['MatchMode'] = self.match_mode
        if self.name is not None:
            result['Name'] = self.name
        if self.personal_limit_count is not None:
            result['PersonalLimitCount'] = self.personal_limit_count.to_map()
        if self.personal_limit_type is not None:
            result['PersonalLimitType'] = self.personal_limit_type
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.status is not None:
            result['Status'] = self.status
        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids
        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompanyLimitCount') is not None:
            temp_model = CreateRegistrationPolicyRequestCompanyLimitCount()
            self.company_limit_count = temp_model.from_map(m['CompanyLimitCount'])
        if m.get('CompanyLimitType') is not None:
            self.company_limit_type = m.get('CompanyLimitType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('MatchMode') is not None:
            self.match_mode = m.get('MatchMode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PersonalLimitCount') is not None:
            temp_model = CreateRegistrationPolicyRequestPersonalLimitCount()
            self.personal_limit_count = temp_model.from_map(m['PersonalLimitCount'])
        if m.get('PersonalLimitType') is not None:
            self.personal_limit_type = m.get('PersonalLimitType')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')
        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')
        return self


class CreateRegistrationPolicyShrinkRequest(TeaModel):
    def __init__(
        self,
        company_limit_count_shrink: str = None,
        company_limit_type: str = None,
        description: str = None,
        match_mode: str = None,
        name: str = None,
        personal_limit_count_shrink: str = None,
        personal_limit_type: str = None,
        priority: int = None,
        status: str = None,
        user_group_ids: List[str] = None,
        whitelist: List[str] = None,
    ):
        self.company_limit_count_shrink = company_limit_count_shrink
        # This parameter is required.
        self.company_limit_type = company_limit_type
        self.description = description
        # This parameter is required.
        self.match_mode = match_mode
        # This parameter is required.
        self.name = name
        self.personal_limit_count_shrink = personal_limit_count_shrink
        # This parameter is required.
        self.personal_limit_type = personal_limit_type
        self.priority = priority
        # This parameter is required.
        self.status = status
        self.user_group_ids = user_group_ids
        self.whitelist = whitelist

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.company_limit_count_shrink is not None:
            result['CompanyLimitCount'] = self.company_limit_count_shrink
        if self.company_limit_type is not None:
            result['CompanyLimitType'] = self.company_limit_type
        if self.description is not None:
            result['Description'] = self.description
        if self.match_mode is not None:
            result['MatchMode'] = self.match_mode
        if self.name is not None:
            result['Name'] = self.name
        if self.personal_limit_count_shrink is not None:
            result['PersonalLimitCount'] = self.personal_limit_count_shrink
        if self.personal_limit_type is not None:
            result['PersonalLimitType'] = self.personal_limit_type
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.status is not None:
            result['Status'] = self.status
        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids
        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompanyLimitCount') is not None:
            self.company_limit_count_shrink = m.get('CompanyLimitCount')
        if m.get('CompanyLimitType') is not None:
            self.company_limit_type = m.get('CompanyLimitType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('MatchMode') is not None:
            self.match_mode = m.get('MatchMode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PersonalLimitCount') is not None:
            self.personal_limit_count_shrink = m.get('PersonalLimitCount')
        if m.get('PersonalLimitType') is not None:
            self.personal_limit_type = m.get('PersonalLimitType')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')
        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')
        return self


class CreateRegistrationPolicyResponseBodyPolicyLimitDetailLimitCount(TeaModel):
    def __init__(
        self,
        all: int = None,
        mobile: int = None,
        pc: int = None,
    ):
        self.all = all
        self.mobile = mobile
        self.pc = pc

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.pc is not None:
            result['PC'] = self.pc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('PC') is not None:
            self.pc = m.get('PC')
        return self


class CreateRegistrationPolicyResponseBodyPolicyLimitDetail(TeaModel):
    def __init__(
        self,
        device_belong: str = None,
        limit_count: CreateRegistrationPolicyResponseBodyPolicyLimitDetailLimitCount = None,
        limit_type: str = None,
    ):
        self.device_belong = device_belong
        self.limit_count = limit_count
        self.limit_type = limit_type

    def validate(self):
        if self.limit_count:
            self.limit_count.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_belong is not None:
            result['DeviceBelong'] = self.device_belong
        if self.limit_count is not None:
            result['LimitCount'] = self.limit_count.to_map()
        if self.limit_type is not None:
            result['LimitType'] = self.limit_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceBelong') is not None:
            self.device_belong = m.get('DeviceBelong')
        if m.get('LimitCount') is not None:
            temp_model = CreateRegistrationPolicyResponseBodyPolicyLimitDetailLimitCount()
            self.limit_count = temp_model.from_map(m['LimitCount'])
        if m.get('LimitType') is not None:
            self.limit_type = m.get('LimitType')
        return self


class CreateRegistrationPolicyResponseBodyPolicy(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        limit_detail: List[CreateRegistrationPolicyResponseBodyPolicyLimitDetail] = None,
        match_mode: str = None,
        name: str = None,
        policy_id: str = None,
        priority: str = None,
        status: str = None,
        user_group_ids: List[str] = None,
        whitelist: List[str] = None,
    ):
        self.create_time = create_time
        self.description = description
        self.limit_detail = limit_detail
        self.match_mode = match_mode
        self.name = name
        self.policy_id = policy_id
        self.priority = priority
        self.status = status
        self.user_group_ids = user_group_ids
        self.whitelist = whitelist

    def validate(self):
        if self.limit_detail:
            for k in self.limit_detail:
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
        result['LimitDetail'] = []
        if self.limit_detail is not None:
            for k in self.limit_detail:
                result['LimitDetail'].append(k.to_map() if k else None)
        if self.match_mode is not None:
            result['MatchMode'] = self.match_mode
        if self.name is not None:
            result['Name'] = self.name
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.status is not None:
            result['Status'] = self.status
        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids
        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.limit_detail = []
        if m.get('LimitDetail') is not None:
            for k in m.get('LimitDetail'):
                temp_model = CreateRegistrationPolicyResponseBodyPolicyLimitDetail()
                self.limit_detail.append(temp_model.from_map(k))
        if m.get('MatchMode') is not None:
            self.match_mode = m.get('MatchMode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')
        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')
        return self


class CreateRegistrationPolicyResponseBody(TeaModel):
    def __init__(
        self,
        policy: CreateRegistrationPolicyResponseBodyPolicy = None,
        request_id: str = None,
    ):
        self.policy = policy
        self.request_id = request_id

    def validate(self):
        if self.policy:
            self.policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Policy') is not None:
            temp_model = CreateRegistrationPolicyResponseBodyPolicy()
            self.policy = temp_model.from_map(m['Policy'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateRegistrationPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateRegistrationPolicyResponseBody = None,
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
            temp_model = CreateRegistrationPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUserGroupRequestAttributes(TeaModel):
    def __init__(
        self,
        idp_id: int = None,
        relation: str = None,
        user_group_type: str = None,
        value: str = None,
    ):
        self.idp_id = idp_id
        # This parameter is required.
        self.relation = relation
        # This parameter is required.
        self.user_group_type = user_group_type
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.idp_id is not None:
            result['IdpId'] = self.idp_id
        if self.relation is not None:
            result['Relation'] = self.relation
        if self.user_group_type is not None:
            result['UserGroupType'] = self.user_group_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdpId') is not None:
            self.idp_id = m.get('IdpId')
        if m.get('Relation') is not None:
            self.relation = m.get('Relation')
        if m.get('UserGroupType') is not None:
            self.user_group_type = m.get('UserGroupType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateUserGroupRequest(TeaModel):
    def __init__(
        self,
        attributes: List[CreateUserGroupRequestAttributes] = None,
        description: str = None,
        name: str = None,
    ):
        # This parameter is required.
        self.attributes = attributes
        self.description = description
        # This parameter is required.
        self.name = name

    def validate(self):
        if self.attributes:
            for k in self.attributes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Attributes'] = []
        if self.attributes is not None:
            for k in self.attributes:
                result['Attributes'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attributes = []
        if m.get('Attributes') is not None:
            for k in m.get('Attributes'):
                temp_model = CreateUserGroupRequestAttributes()
                self.attributes.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateUserGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        user_group_id: str = None,
    ):
        self.request_id = request_id
        self.user_group_id = user_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class CreateUserGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateUserGroupResponseBody = None,
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
            temp_model = CreateUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateWmBaseImageRequest(TeaModel):
    def __init__(
        self,
        height: int = None,
        opacity: int = None,
        scale: int = None,
        width: int = None,
        wm_info_bytes_b64: str = None,
        wm_info_size: int = None,
        wm_info_uint: str = None,
        wm_type: str = None,
    ):
        # This parameter is required.
        self.height = height
        # This parameter is required.
        self.opacity = opacity
        # This parameter is required.
        self.scale = scale
        # This parameter is required.
        self.width = width
        self.wm_info_bytes_b64 = wm_info_bytes_b64
        self.wm_info_size = wm_info_size
        self.wm_info_uint = wm_info_uint
        # This parameter is required.
        self.wm_type = wm_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['Height'] = self.height
        if self.opacity is not None:
            result['Opacity'] = self.opacity
        if self.scale is not None:
            result['Scale'] = self.scale
        if self.width is not None:
            result['Width'] = self.width
        if self.wm_info_bytes_b64 is not None:
            result['WmInfoBytesB64'] = self.wm_info_bytes_b64
        if self.wm_info_size is not None:
            result['WmInfoSize'] = self.wm_info_size
        if self.wm_info_uint is not None:
            result['WmInfoUint'] = self.wm_info_uint
        if self.wm_type is not None:
            result['WmType'] = self.wm_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Opacity') is not None:
            self.opacity = m.get('Opacity')
        if m.get('Scale') is not None:
            self.scale = m.get('Scale')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('WmInfoBytesB64') is not None:
            self.wm_info_bytes_b64 = m.get('WmInfoBytesB64')
        if m.get('WmInfoSize') is not None:
            self.wm_info_size = m.get('WmInfoSize')
        if m.get('WmInfoUint') is not None:
            self.wm_info_uint = m.get('WmInfoUint')
        if m.get('WmType') is not None:
            self.wm_type = m.get('WmType')
        return self


class CreateWmBaseImageResponseBodyData(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        image_url: str = None,
        image_url_exp: int = None,
    ):
        self.image_id = image_id
        self.image_url = image_url
        self.image_url_exp = image_url_exp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.image_url_exp is not None:
            result['ImageUrlExp'] = self.image_url_exp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('ImageUrlExp') is not None:
            self.image_url_exp = m.get('ImageUrlExp')
        return self


class CreateWmBaseImageResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateWmBaseImageResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateWmBaseImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateWmBaseImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateWmBaseImageResponseBody = None,
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
            temp_model = CreateWmBaseImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateWmEmbedTaskRequestCsvControl(TeaModel):
    def __init__(
        self,
        embed_column: int = None,
        embed_precision: int = None,
        method: str = None,
    ):
        self.embed_column = embed_column
        self.embed_precision = embed_precision
        self.method = method

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.embed_column is not None:
            result['EmbedColumn'] = self.embed_column
        if self.embed_precision is not None:
            result['EmbedPrecision'] = self.embed_precision
        if self.method is not None:
            result['Method'] = self.method
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EmbedColumn') is not None:
            self.embed_column = m.get('EmbedColumn')
        if m.get('EmbedPrecision') is not None:
            self.embed_precision = m.get('EmbedPrecision')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        return self


class CreateWmEmbedTaskRequestDocumentControlBackgroundControlBgInvisibleControl(TeaModel):
    def __init__(
        self,
        opacity: int = None,
    ):
        self.opacity = opacity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.opacity is not None:
            result['Opacity'] = self.opacity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Opacity') is not None:
            self.opacity = m.get('Opacity')
        return self


class CreateWmEmbedTaskRequestDocumentControlBackgroundControlBgVisibleControl(TeaModel):
    def __init__(
        self,
        angle: int = None,
        font_color: str = None,
        font_size: int = None,
        horizontal_number: int = None,
        mode: str = None,
        opacity: int = None,
        pos_x: str = None,
        pos_y: str = None,
        vertical_number: int = None,
        visible_text: str = None,
    ):
        self.angle = angle
        self.font_color = font_color
        self.font_size = font_size
        self.horizontal_number = horizontal_number
        self.mode = mode
        self.opacity = opacity
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vertical_number = vertical_number
        self.visible_text = visible_text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.angle is not None:
            result['Angle'] = self.angle
        if self.font_color is not None:
            result['FontColor'] = self.font_color
        if self.font_size is not None:
            result['FontSize'] = self.font_size
        if self.horizontal_number is not None:
            result['HorizontalNumber'] = self.horizontal_number
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.opacity is not None:
            result['Opacity'] = self.opacity
        if self.pos_x is not None:
            result['PosX'] = self.pos_x
        if self.pos_y is not None:
            result['PosY'] = self.pos_y
        if self.vertical_number is not None:
            result['VerticalNumber'] = self.vertical_number
        if self.visible_text is not None:
            result['VisibleText'] = self.visible_text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Angle') is not None:
            self.angle = m.get('Angle')
        if m.get('FontColor') is not None:
            self.font_color = m.get('FontColor')
        if m.get('FontSize') is not None:
            self.font_size = m.get('FontSize')
        if m.get('HorizontalNumber') is not None:
            self.horizontal_number = m.get('HorizontalNumber')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Opacity') is not None:
            self.opacity = m.get('Opacity')
        if m.get('PosX') is not None:
            self.pos_x = m.get('PosX')
        if m.get('PosY') is not None:
            self.pos_y = m.get('PosY')
        if m.get('VerticalNumber') is not None:
            self.vertical_number = m.get('VerticalNumber')
        if m.get('VisibleText') is not None:
            self.visible_text = m.get('VisibleText')
        return self


class CreateWmEmbedTaskRequestDocumentControlBackgroundControl(TeaModel):
    def __init__(
        self,
        bg_add_invisible: bool = None,
        bg_add_visible: bool = None,
        bg_invisible_control: CreateWmEmbedTaskRequestDocumentControlBackgroundControlBgInvisibleControl = None,
        bg_visible_control: CreateWmEmbedTaskRequestDocumentControlBackgroundControlBgVisibleControl = None,
    ):
        self.bg_add_invisible = bg_add_invisible
        self.bg_add_visible = bg_add_visible
        self.bg_invisible_control = bg_invisible_control
        self.bg_visible_control = bg_visible_control

    def validate(self):
        if self.bg_invisible_control:
            self.bg_invisible_control.validate()
        if self.bg_visible_control:
            self.bg_visible_control.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bg_add_invisible is not None:
            result['BgAddInvisible'] = self.bg_add_invisible
        if self.bg_add_visible is not None:
            result['BgAddVisible'] = self.bg_add_visible
        if self.bg_invisible_control is not None:
            result['BgInvisibleControl'] = self.bg_invisible_control.to_map()
        if self.bg_visible_control is not None:
            result['BgVisibleControl'] = self.bg_visible_control.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BgAddInvisible') is not None:
            self.bg_add_invisible = m.get('BgAddInvisible')
        if m.get('BgAddVisible') is not None:
            self.bg_add_visible = m.get('BgAddVisible')
        if m.get('BgInvisibleControl') is not None:
            temp_model = CreateWmEmbedTaskRequestDocumentControlBackgroundControlBgInvisibleControl()
            self.bg_invisible_control = temp_model.from_map(m['BgInvisibleControl'])
        if m.get('BgVisibleControl') is not None:
            temp_model = CreateWmEmbedTaskRequestDocumentControlBackgroundControlBgVisibleControl()
            self.bg_visible_control = temp_model.from_map(m['BgVisibleControl'])
        return self


class CreateWmEmbedTaskRequestDocumentControl(TeaModel):
    def __init__(
        self,
        background_control: CreateWmEmbedTaskRequestDocumentControlBackgroundControl = None,
        invisible_anti_all_copy: bool = None,
        invisible_anti_text_copy: bool = None,
    ):
        self.background_control = background_control
        self.invisible_anti_all_copy = invisible_anti_all_copy
        self.invisible_anti_text_copy = invisible_anti_text_copy

    def validate(self):
        if self.background_control:
            self.background_control.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.background_control is not None:
            result['BackgroundControl'] = self.background_control.to_map()
        if self.invisible_anti_all_copy is not None:
            result['InvisibleAntiAllCopy'] = self.invisible_anti_all_copy
        if self.invisible_anti_text_copy is not None:
            result['InvisibleAntiTextCopy'] = self.invisible_anti_text_copy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackgroundControl') is not None:
            temp_model = CreateWmEmbedTaskRequestDocumentControlBackgroundControl()
            self.background_control = temp_model.from_map(m['BackgroundControl'])
        if m.get('InvisibleAntiAllCopy') is not None:
            self.invisible_anti_all_copy = m.get('InvisibleAntiAllCopy')
        if m.get('InvisibleAntiTextCopy') is not None:
            self.invisible_anti_text_copy = m.get('InvisibleAntiTextCopy')
        return self


class CreateWmEmbedTaskRequest(TeaModel):
    def __init__(
        self,
        csv_control: CreateWmEmbedTaskRequestCsvControl = None,
        document_control: CreateWmEmbedTaskRequestDocumentControl = None,
        file_url: str = None,
        filename: str = None,
        image_embed_jpeg_quality: int = None,
        image_embed_level: int = None,
        video_bitrate: str = None,
        video_is_long: bool = None,
        wm_info_bytes_b64: str = None,
        wm_info_size: int = None,
        wm_info_uint: str = None,
        wm_type: str = None,
    ):
        self.csv_control = csv_control
        self.document_control = document_control
        # This parameter is required.
        self.file_url = file_url
        # This parameter is required.
        self.filename = filename
        self.image_embed_jpeg_quality = image_embed_jpeg_quality
        self.image_embed_level = image_embed_level
        self.video_bitrate = video_bitrate
        self.video_is_long = video_is_long
        self.wm_info_bytes_b64 = wm_info_bytes_b64
        self.wm_info_size = wm_info_size
        self.wm_info_uint = wm_info_uint
        # This parameter is required.
        self.wm_type = wm_type

    def validate(self):
        if self.csv_control:
            self.csv_control.validate()
        if self.document_control:
            self.document_control.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.csv_control is not None:
            result['CsvControl'] = self.csv_control.to_map()
        if self.document_control is not None:
            result['DocumentControl'] = self.document_control.to_map()
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.filename is not None:
            result['Filename'] = self.filename
        if self.image_embed_jpeg_quality is not None:
            result['ImageEmbedJpegQuality'] = self.image_embed_jpeg_quality
        if self.image_embed_level is not None:
            result['ImageEmbedLevel'] = self.image_embed_level
        if self.video_bitrate is not None:
            result['VideoBitrate'] = self.video_bitrate
        if self.video_is_long is not None:
            result['VideoIsLong'] = self.video_is_long
        if self.wm_info_bytes_b64 is not None:
            result['WmInfoBytesB64'] = self.wm_info_bytes_b64
        if self.wm_info_size is not None:
            result['WmInfoSize'] = self.wm_info_size
        if self.wm_info_uint is not None:
            result['WmInfoUint'] = self.wm_info_uint
        if self.wm_type is not None:
            result['WmType'] = self.wm_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CsvControl') is not None:
            temp_model = CreateWmEmbedTaskRequestCsvControl()
            self.csv_control = temp_model.from_map(m['CsvControl'])
        if m.get('DocumentControl') is not None:
            temp_model = CreateWmEmbedTaskRequestDocumentControl()
            self.document_control = temp_model.from_map(m['DocumentControl'])
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('Filename') is not None:
            self.filename = m.get('Filename')
        if m.get('ImageEmbedJpegQuality') is not None:
            self.image_embed_jpeg_quality = m.get('ImageEmbedJpegQuality')
        if m.get('ImageEmbedLevel') is not None:
            self.image_embed_level = m.get('ImageEmbedLevel')
        if m.get('VideoBitrate') is not None:
            self.video_bitrate = m.get('VideoBitrate')
        if m.get('VideoIsLong') is not None:
            self.video_is_long = m.get('VideoIsLong')
        if m.get('WmInfoBytesB64') is not None:
            self.wm_info_bytes_b64 = m.get('WmInfoBytesB64')
        if m.get('WmInfoSize') is not None:
            self.wm_info_size = m.get('WmInfoSize')
        if m.get('WmInfoUint') is not None:
            self.wm_info_uint = m.get('WmInfoUint')
        if m.get('WmType') is not None:
            self.wm_type = m.get('WmType')
        return self


class CreateWmEmbedTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        csv_control_shrink: str = None,
        document_control_shrink: str = None,
        file_url: str = None,
        filename: str = None,
        image_embed_jpeg_quality: int = None,
        image_embed_level: int = None,
        video_bitrate: str = None,
        video_is_long: bool = None,
        wm_info_bytes_b64: str = None,
        wm_info_size: int = None,
        wm_info_uint: str = None,
        wm_type: str = None,
    ):
        self.csv_control_shrink = csv_control_shrink
        self.document_control_shrink = document_control_shrink
        # This parameter is required.
        self.file_url = file_url
        # This parameter is required.
        self.filename = filename
        self.image_embed_jpeg_quality = image_embed_jpeg_quality
        self.image_embed_level = image_embed_level
        self.video_bitrate = video_bitrate
        self.video_is_long = video_is_long
        self.wm_info_bytes_b64 = wm_info_bytes_b64
        self.wm_info_size = wm_info_size
        self.wm_info_uint = wm_info_uint
        # This parameter is required.
        self.wm_type = wm_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.csv_control_shrink is not None:
            result['CsvControl'] = self.csv_control_shrink
        if self.document_control_shrink is not None:
            result['DocumentControl'] = self.document_control_shrink
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.filename is not None:
            result['Filename'] = self.filename
        if self.image_embed_jpeg_quality is not None:
            result['ImageEmbedJpegQuality'] = self.image_embed_jpeg_quality
        if self.image_embed_level is not None:
            result['ImageEmbedLevel'] = self.image_embed_level
        if self.video_bitrate is not None:
            result['VideoBitrate'] = self.video_bitrate
        if self.video_is_long is not None:
            result['VideoIsLong'] = self.video_is_long
        if self.wm_info_bytes_b64 is not None:
            result['WmInfoBytesB64'] = self.wm_info_bytes_b64
        if self.wm_info_size is not None:
            result['WmInfoSize'] = self.wm_info_size
        if self.wm_info_uint is not None:
            result['WmInfoUint'] = self.wm_info_uint
        if self.wm_type is not None:
            result['WmType'] = self.wm_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CsvControl') is not None:
            self.csv_control_shrink = m.get('CsvControl')
        if m.get('DocumentControl') is not None:
            self.document_control_shrink = m.get('DocumentControl')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('Filename') is not None:
            self.filename = m.get('Filename')
        if m.get('ImageEmbedJpegQuality') is not None:
            self.image_embed_jpeg_quality = m.get('ImageEmbedJpegQuality')
        if m.get('ImageEmbedLevel') is not None:
            self.image_embed_level = m.get('ImageEmbedLevel')
        if m.get('VideoBitrate') is not None:
            self.video_bitrate = m.get('VideoBitrate')
        if m.get('VideoIsLong') is not None:
            self.video_is_long = m.get('VideoIsLong')
        if m.get('WmInfoBytesB64') is not None:
            self.wm_info_bytes_b64 = m.get('WmInfoBytesB64')
        if m.get('WmInfoSize') is not None:
            self.wm_info_size = m.get('WmInfoSize')
        if m.get('WmInfoUint') is not None:
            self.wm_info_uint = m.get('WmInfoUint')
        if m.get('WmType') is not None:
            self.wm_type = m.get('WmType')
        return self


class CreateWmEmbedTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateWmEmbedTaskResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateWmEmbedTaskResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateWmEmbedTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateWmEmbedTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateWmEmbedTaskResponseBody = None,
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
            temp_model = CreateWmEmbedTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateWmExtractTaskRequestCsvControl(TeaModel):
    def __init__(
        self,
        embed_column: int = None,
        embed_precision: int = None,
        method: str = None,
    ):
        self.embed_column = embed_column
        self.embed_precision = embed_precision
        self.method = method

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.embed_column is not None:
            result['EmbedColumn'] = self.embed_column
        if self.embed_precision is not None:
            result['EmbedPrecision'] = self.embed_precision
        if self.method is not None:
            result['Method'] = self.method
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EmbedColumn') is not None:
            self.embed_column = m.get('EmbedColumn')
        if m.get('EmbedPrecision') is not None:
            self.embed_precision = m.get('EmbedPrecision')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        return self


class CreateWmExtractTaskRequest(TeaModel):
    def __init__(
        self,
        csv_control: CreateWmExtractTaskRequestCsvControl = None,
        document_is_capture: bool = None,
        file_url: str = None,
        filename: str = None,
        video_is_long: bool = None,
        video_speed: str = None,
        wm_info_size: int = None,
        wm_type: str = None,
    ):
        self.csv_control = csv_control
        self.document_is_capture = document_is_capture
        # This parameter is required.
        self.file_url = file_url
        # This parameter is required.
        self.filename = filename
        self.video_is_long = video_is_long
        self.video_speed = video_speed
        self.wm_info_size = wm_info_size
        # This parameter is required.
        self.wm_type = wm_type

    def validate(self):
        if self.csv_control:
            self.csv_control.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.csv_control is not None:
            result['CsvControl'] = self.csv_control.to_map()
        if self.document_is_capture is not None:
            result['DocumentIsCapture'] = self.document_is_capture
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.filename is not None:
            result['Filename'] = self.filename
        if self.video_is_long is not None:
            result['VideoIsLong'] = self.video_is_long
        if self.video_speed is not None:
            result['VideoSpeed'] = self.video_speed
        if self.wm_info_size is not None:
            result['WmInfoSize'] = self.wm_info_size
        if self.wm_type is not None:
            result['WmType'] = self.wm_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CsvControl') is not None:
            temp_model = CreateWmExtractTaskRequestCsvControl()
            self.csv_control = temp_model.from_map(m['CsvControl'])
        if m.get('DocumentIsCapture') is not None:
            self.document_is_capture = m.get('DocumentIsCapture')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('Filename') is not None:
            self.filename = m.get('Filename')
        if m.get('VideoIsLong') is not None:
            self.video_is_long = m.get('VideoIsLong')
        if m.get('VideoSpeed') is not None:
            self.video_speed = m.get('VideoSpeed')
        if m.get('WmInfoSize') is not None:
            self.wm_info_size = m.get('WmInfoSize')
        if m.get('WmType') is not None:
            self.wm_type = m.get('WmType')
        return self


class CreateWmExtractTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        csv_control_shrink: str = None,
        document_is_capture: bool = None,
        file_url: str = None,
        filename: str = None,
        video_is_long: bool = None,
        video_speed: str = None,
        wm_info_size: int = None,
        wm_type: str = None,
    ):
        self.csv_control_shrink = csv_control_shrink
        self.document_is_capture = document_is_capture
        # This parameter is required.
        self.file_url = file_url
        # This parameter is required.
        self.filename = filename
        self.video_is_long = video_is_long
        self.video_speed = video_speed
        self.wm_info_size = wm_info_size
        # This parameter is required.
        self.wm_type = wm_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.csv_control_shrink is not None:
            result['CsvControl'] = self.csv_control_shrink
        if self.document_is_capture is not None:
            result['DocumentIsCapture'] = self.document_is_capture
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.filename is not None:
            result['Filename'] = self.filename
        if self.video_is_long is not None:
            result['VideoIsLong'] = self.video_is_long
        if self.video_speed is not None:
            result['VideoSpeed'] = self.video_speed
        if self.wm_info_size is not None:
            result['WmInfoSize'] = self.wm_info_size
        if self.wm_type is not None:
            result['WmType'] = self.wm_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CsvControl') is not None:
            self.csv_control_shrink = m.get('CsvControl')
        if m.get('DocumentIsCapture') is not None:
            self.document_is_capture = m.get('DocumentIsCapture')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('Filename') is not None:
            self.filename = m.get('Filename')
        if m.get('VideoIsLong') is not None:
            self.video_is_long = m.get('VideoIsLong')
        if m.get('VideoSpeed') is not None:
            self.video_speed = m.get('VideoSpeed')
        if m.get('WmInfoSize') is not None:
            self.wm_info_size = m.get('WmInfoSize')
        if m.get('WmType') is not None:
            self.wm_type = m.get('WmType')
        return self


class CreateWmExtractTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateWmExtractTaskResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateWmExtractTaskResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateWmExtractTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateWmExtractTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateWmExtractTaskResponseBody = None,
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
            temp_model = CreateWmExtractTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateWmInfoMappingRequest(TeaModel):
    def __init__(
        self,
        wm_info_bytes_b64: str = None,
        wm_info_size: int = None,
        wm_type: str = None,
    ):
        # This parameter is required.
        self.wm_info_bytes_b64 = wm_info_bytes_b64
        self.wm_info_size = wm_info_size
        # This parameter is required.
        self.wm_type = wm_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.wm_info_bytes_b64 is not None:
            result['WmInfoBytesB64'] = self.wm_info_bytes_b64
        if self.wm_info_size is not None:
            result['WmInfoSize'] = self.wm_info_size
        if self.wm_type is not None:
            result['WmType'] = self.wm_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WmInfoBytesB64') is not None:
            self.wm_info_bytes_b64 = m.get('WmInfoBytesB64')
        if m.get('WmInfoSize') is not None:
            self.wm_info_size = m.get('WmInfoSize')
        if m.get('WmType') is not None:
            self.wm_type = m.get('WmType')
        return self


class CreateWmInfoMappingResponseBodyData(TeaModel):
    def __init__(
        self,
        wm_info_uint: int = None,
    ):
        self.wm_info_uint = wm_info_uint

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.wm_info_uint is not None:
            result['WmInfoUint'] = self.wm_info_uint
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WmInfoUint') is not None:
            self.wm_info_uint = m.get('WmInfoUint')
        return self


class CreateWmInfoMappingResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateWmInfoMappingResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateWmInfoMappingResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateWmInfoMappingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateWmInfoMappingResponseBody = None,
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
            temp_model = CreateWmInfoMappingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteClientUserRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteClientUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteClientUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteClientUserResponseBody = None,
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
            temp_model = DeleteClientUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDynamicRouteRequest(TeaModel):
    def __init__(
        self,
        dynamic_route_id: str = None,
    ):
        # This parameter is required.
        self.dynamic_route_id = dynamic_route_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dynamic_route_id is not None:
            result['DynamicRouteId'] = self.dynamic_route_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DynamicRouteId') is not None:
            self.dynamic_route_id = m.get('DynamicRouteId')
        return self


class DeleteDynamicRouteResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDynamicRouteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDynamicRouteResponseBody = None,
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
            temp_model = DeleteDynamicRouteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIdpDepartmentRequest(TeaModel):
    def __init__(
        self,
        department_id: str = None,
        idp_config_id: str = None,
    ):
        # This parameter is required.
        self.department_id = department_id
        # This parameter is required.
        self.idp_config_id = idp_config_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.department_id is not None:
            result['DepartmentId'] = self.department_id
        if self.idp_config_id is not None:
            result['IdpConfigId'] = self.idp_config_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')
        if m.get('IdpConfigId') is not None:
            self.idp_config_id = m.get('IdpConfigId')
        return self


class DeleteIdpDepartmentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteIdpDepartmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteIdpDepartmentResponseBody = None,
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
            temp_model = DeleteIdpDepartmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePrivateAccessApplicationRequest(TeaModel):
    def __init__(
        self,
        application_id: str = None,
    ):
        # This parameter is required.
        self.application_id = application_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        return self


class DeletePrivateAccessApplicationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeletePrivateAccessApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeletePrivateAccessApplicationResponseBody = None,
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
            temp_model = DeletePrivateAccessApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePrivateAccessPolicyRequest(TeaModel):
    def __init__(
        self,
        policy_id: str = None,
    ):
        # This parameter is required.
        self.policy_id = policy_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        return self


class DeletePrivateAccessPolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeletePrivateAccessPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeletePrivateAccessPolicyResponseBody = None,
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
            temp_model = DeletePrivateAccessPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePrivateAccessTagRequest(TeaModel):
    def __init__(
        self,
        tag_id: str = None,
    ):
        # This parameter is required.
        self.tag_id = tag_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        return self


class DeletePrivateAccessTagResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeletePrivateAccessTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeletePrivateAccessTagResponseBody = None,
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
            temp_model = DeletePrivateAccessTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRegistrationPoliciesRequest(TeaModel):
    def __init__(
        self,
        policy_ids: List[str] = None,
    ):
        # This parameter is required.
        self.policy_ids = policy_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')
        return self


class DeleteRegistrationPoliciesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteRegistrationPoliciesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteRegistrationPoliciesResponseBody = None,
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
            temp_model = DeleteRegistrationPoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserDevicesRequest(TeaModel):
    def __init__(
        self,
        device_tags: List[str] = None,
    ):
        self.device_tags = device_tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_tags is not None:
            result['DeviceTags'] = self.device_tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceTags') is not None:
            self.device_tags = m.get('DeviceTags')
        return self


class DeleteUserDevicesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteUserDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteUserDevicesResponseBody = None,
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
            temp_model = DeleteUserDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserGroupRequest(TeaModel):
    def __init__(
        self,
        user_group_id: str = None,
    ):
        # This parameter is required.
        self.user_group_id = user_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class DeleteUserGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteUserGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteUserGroupResponseBody = None,
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
            temp_model = DeleteUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachApplication2ConnectorRequest(TeaModel):
    def __init__(
        self,
        application_ids: List[str] = None,
        connector_id: str = None,
    ):
        # This parameter is required.
        self.application_ids = application_ids
        # ConnectorID。
        # 
        # This parameter is required.
        self.connector_id = connector_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_ids is not None:
            result['ApplicationIds'] = self.application_ids
        if self.connector_id is not None:
            result['ConnectorId'] = self.connector_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationIds') is not None:
            self.application_ids = m.get('ApplicationIds')
        if m.get('ConnectorId') is not None:
            self.connector_id = m.get('ConnectorId')
        return self


class DetachApplication2ConnectorShrinkRequest(TeaModel):
    def __init__(
        self,
        application_ids_shrink: str = None,
        connector_id: str = None,
    ):
        # This parameter is required.
        self.application_ids_shrink = application_ids_shrink
        # ConnectorID。
        # 
        # This parameter is required.
        self.connector_id = connector_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_ids_shrink is not None:
            result['ApplicationIds'] = self.application_ids_shrink
        if self.connector_id is not None:
            result['ConnectorId'] = self.connector_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationIds') is not None:
            self.application_ids_shrink = m.get('ApplicationIds')
        if m.get('ConnectorId') is not None:
            self.connector_id = m.get('ConnectorId')
        return self


class DetachApplication2ConnectorResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetachApplication2ConnectorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetachApplication2ConnectorResponseBody = None,
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
            temp_model = DetachApplication2ConnectorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportUserDevicesRequest(TeaModel):
    def __init__(
        self,
        app_statuses: List[str] = None,
        department: str = None,
        device_belong: str = None,
        device_statuses: List[str] = None,
        device_tags: List[str] = None,
        device_types: List[str] = None,
        dlp_statuses: List[str] = None,
        hostname: str = None,
        ia_statuses: List[str] = None,
        mac: str = None,
        nac_statuses: List[str] = None,
        pa_statuses: List[str] = None,
        sase_user_id: str = None,
        sharing_status: bool = None,
        username: str = None,
    ):
        self.app_statuses = app_statuses
        self.department = department
        self.device_belong = device_belong
        self.device_statuses = device_statuses
        self.device_tags = device_tags
        self.device_types = device_types
        self.dlp_statuses = dlp_statuses
        self.hostname = hostname
        self.ia_statuses = ia_statuses
        self.mac = mac
        self.nac_statuses = nac_statuses
        self.pa_statuses = pa_statuses
        self.sase_user_id = sase_user_id
        self.sharing_status = sharing_status
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_statuses is not None:
            result['AppStatuses'] = self.app_statuses
        if self.department is not None:
            result['Department'] = self.department
        if self.device_belong is not None:
            result['DeviceBelong'] = self.device_belong
        if self.device_statuses is not None:
            result['DeviceStatuses'] = self.device_statuses
        if self.device_tags is not None:
            result['DeviceTags'] = self.device_tags
        if self.device_types is not None:
            result['DeviceTypes'] = self.device_types
        if self.dlp_statuses is not None:
            result['DlpStatuses'] = self.dlp_statuses
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.ia_statuses is not None:
            result['IaStatuses'] = self.ia_statuses
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.nac_statuses is not None:
            result['NacStatuses'] = self.nac_statuses
        if self.pa_statuses is not None:
            result['PaStatuses'] = self.pa_statuses
        if self.sase_user_id is not None:
            result['SaseUserId'] = self.sase_user_id
        if self.sharing_status is not None:
            result['SharingStatus'] = self.sharing_status
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppStatuses') is not None:
            self.app_statuses = m.get('AppStatuses')
        if m.get('Department') is not None:
            self.department = m.get('Department')
        if m.get('DeviceBelong') is not None:
            self.device_belong = m.get('DeviceBelong')
        if m.get('DeviceStatuses') is not None:
            self.device_statuses = m.get('DeviceStatuses')
        if m.get('DeviceTags') is not None:
            self.device_tags = m.get('DeviceTags')
        if m.get('DeviceTypes') is not None:
            self.device_types = m.get('DeviceTypes')
        if m.get('DlpStatuses') is not None:
            self.dlp_statuses = m.get('DlpStatuses')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('IaStatuses') is not None:
            self.ia_statuses = m.get('IaStatuses')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('NacStatuses') is not None:
            self.nac_statuses = m.get('NacStatuses')
        if m.get('PaStatuses') is not None:
            self.pa_statuses = m.get('PaStatuses')
        if m.get('SaseUserId') is not None:
            self.sase_user_id = m.get('SaseUserId')
        if m.get('SharingStatus') is not None:
            self.sharing_status = m.get('SharingStatus')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class ExportUserDevicesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        signed_url: str = None,
    ):
        self.request_id = request_id
        self.signed_url = signed_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.signed_url is not None:
            result['SignedUrl'] = self.signed_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SignedUrl') is not None:
            self.signed_url = m.get('SignedUrl')
        return self


class ExportUserDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExportUserDevicesResponseBody = None,
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
            temp_model = ExportUserDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetActiveIdpConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        description: str = None,
        id: str = None,
        name: str = None,
        type: str = None,
    ):
        self.description = description
        self.id = id
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetActiveIdpConfigResponseBody(TeaModel):
    def __init__(
        self,
        data: GetActiveIdpConfigResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetActiveIdpConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetActiveIdpConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetActiveIdpConfigResponseBody = None,
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
            temp_model = GetActiveIdpConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetClientUserRequest(TeaModel):
    def __init__(
        self,
        idp_config_id: str = None,
        username: str = None,
    ):
        # This parameter is required.
        self.idp_config_id = idp_config_id
        # This parameter is required.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.idp_config_id is not None:
            result['IdpConfigId'] = self.idp_config_id
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdpConfigId') is not None:
            self.idp_config_id = m.get('IdpConfigId')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class GetClientUserResponseBodyDataDepartment(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetClientUserResponseBodyData(TeaModel):
    def __init__(
        self,
        department: GetClientUserResponseBodyDataDepartment = None,
        department_id: str = None,
        description: str = None,
        email: str = None,
        id: str = None,
        idp_config_id: str = None,
        mobile_number: str = None,
        status: str = None,
        user_id: str = None,
        username: str = None,
    ):
        self.department = department
        self.department_id = department_id
        self.description = description
        self.email = email
        self.id = id
        self.idp_config_id = idp_config_id
        self.mobile_number = mobile_number
        self.status = status
        self.user_id = user_id
        self.username = username

    def validate(self):
        if self.department:
            self.department.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.department is not None:
            result['Department'] = self.department.to_map()
        if self.department_id is not None:
            result['DepartmentId'] = self.department_id
        if self.description is not None:
            result['Description'] = self.description
        if self.email is not None:
            result['Email'] = self.email
        if self.id is not None:
            result['Id'] = self.id
        if self.idp_config_id is not None:
            result['IdpConfigId'] = self.idp_config_id
        if self.mobile_number is not None:
            result['MobileNumber'] = self.mobile_number
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Department') is not None:
            temp_model = GetClientUserResponseBodyDataDepartment()
            self.department = temp_model.from_map(m['Department'])
        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdpConfigId') is not None:
            self.idp_config_id = m.get('IdpConfigId')
        if m.get('MobileNumber') is not None:
            self.mobile_number = m.get('MobileNumber')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class GetClientUserResponseBody(TeaModel):
    def __init__(
        self,
        data: GetClientUserResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetClientUserResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetClientUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetClientUserResponseBody = None,
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
            temp_model = GetClientUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDynamicRouteRequest(TeaModel):
    def __init__(
        self,
        dynamic_route_id: str = None,
    ):
        # This parameter is required.
        self.dynamic_route_id = dynamic_route_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dynamic_route_id is not None:
            result['DynamicRouteId'] = self.dynamic_route_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DynamicRouteId') is not None:
            self.dynamic_route_id = m.get('DynamicRouteId')
        return self


class GetDynamicRouteResponseBodyDynamicRoute(TeaModel):
    def __init__(
        self,
        application_ids: List[str] = None,
        application_type: str = None,
        create_time: str = None,
        description: str = None,
        dynamic_route_id: str = None,
        dynamic_route_type: str = None,
        name: str = None,
        next_hop: str = None,
        priority: int = None,
        region_ids: List[str] = None,
        status: str = None,
        tag_ids: List[str] = None,
    ):
        self.application_ids = application_ids
        self.application_type = application_type
        self.create_time = create_time
        self.description = description
        self.dynamic_route_id = dynamic_route_id
        self.dynamic_route_type = dynamic_route_type
        self.name = name
        self.next_hop = next_hop
        self.priority = priority
        self.region_ids = region_ids
        self.status = status
        self.tag_ids = tag_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_ids is not None:
            result['ApplicationIds'] = self.application_ids
        if self.application_type is not None:
            result['ApplicationType'] = self.application_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.dynamic_route_id is not None:
            result['DynamicRouteId'] = self.dynamic_route_id
        if self.dynamic_route_type is not None:
            result['DynamicRouteType'] = self.dynamic_route_type
        if self.name is not None:
            result['Name'] = self.name
        if self.next_hop is not None:
            result['NextHop'] = self.next_hop
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids
        if self.status is not None:
            result['Status'] = self.status
        if self.tag_ids is not None:
            result['TagIds'] = self.tag_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationIds') is not None:
            self.application_ids = m.get('ApplicationIds')
        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DynamicRouteId') is not None:
            self.dynamic_route_id = m.get('DynamicRouteId')
        if m.get('DynamicRouteType') is not None:
            self.dynamic_route_type = m.get('DynamicRouteType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NextHop') is not None:
            self.next_hop = m.get('NextHop')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('RegionIds') is not None:
            self.region_ids = m.get('RegionIds')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TagIds') is not None:
            self.tag_ids = m.get('TagIds')
        return self


class GetDynamicRouteResponseBody(TeaModel):
    def __init__(
        self,
        dynamic_route: GetDynamicRouteResponseBodyDynamicRoute = None,
        request_id: str = None,
    ):
        self.dynamic_route = dynamic_route
        self.request_id = request_id

    def validate(self):
        if self.dynamic_route:
            self.dynamic_route.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dynamic_route is not None:
            result['DynamicRoute'] = self.dynamic_route.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DynamicRoute') is not None:
            temp_model = GetDynamicRouteResponseBodyDynamicRoute()
            self.dynamic_route = temp_model.from_map(m['DynamicRoute'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDynamicRouteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDynamicRouteResponseBody = None,
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
            temp_model = GetDynamicRouteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetIdpConfigRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetIdpConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        access_key_secret: str = None,
        description: str = None,
        get_group_url: str = None,
        id: str = None,
        idp_metadata: str = None,
        mfa_config_type: str = None,
        mobile_login_type: str = None,
        mobile_mfa_config_type: str = None,
        multi_idp_info: str = None,
        name: str = None,
        pc_login_type: str = None,
        status: str = None,
        type: str = None,
        update_time: str = None,
        verify_aes_key: str = None,
        verify_token: str = None,
        verify_url: str = None,
    ):
        # AccessKey ID
        self.access_key = access_key
        # AccessKey Secret
        self.access_key_secret = access_key_secret
        self.description = description
        self.get_group_url = get_group_url
        self.id = id
        self.idp_metadata = idp_metadata
        self.mfa_config_type = mfa_config_type
        self.mobile_login_type = mobile_login_type
        self.mobile_mfa_config_type = mobile_mfa_config_type
        self.multi_idp_info = multi_idp_info
        self.name = name
        self.pc_login_type = pc_login_type
        self.status = status
        self.type = type
        self.update_time = update_time
        self.verify_aes_key = verify_aes_key
        self.verify_token = verify_token
        self.verify_url = verify_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret
        if self.description is not None:
            result['Description'] = self.description
        if self.get_group_url is not None:
            result['GetGroupUrl'] = self.get_group_url
        if self.id is not None:
            result['Id'] = self.id
        if self.idp_metadata is not None:
            result['IdpMetadata'] = self.idp_metadata
        if self.mfa_config_type is not None:
            result['MfaConfigType'] = self.mfa_config_type
        if self.mobile_login_type is not None:
            result['MobileLoginType'] = self.mobile_login_type
        if self.mobile_mfa_config_type is not None:
            result['MobileMfaConfigType'] = self.mobile_mfa_config_type
        if self.multi_idp_info is not None:
            result['MultiIdpInfo'] = self.multi_idp_info
        if self.name is not None:
            result['Name'] = self.name
        if self.pc_login_type is not None:
            result['PcLoginType'] = self.pc_login_type
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.verify_aes_key is not None:
            result['VerifyAesKey'] = self.verify_aes_key
        if self.verify_token is not None:
            result['VerifyToken'] = self.verify_token
        if self.verify_url is not None:
            result['VerifyUrl'] = self.verify_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GetGroupUrl') is not None:
            self.get_group_url = m.get('GetGroupUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdpMetadata') is not None:
            self.idp_metadata = m.get('IdpMetadata')
        if m.get('MfaConfigType') is not None:
            self.mfa_config_type = m.get('MfaConfigType')
        if m.get('MobileLoginType') is not None:
            self.mobile_login_type = m.get('MobileLoginType')
        if m.get('MobileMfaConfigType') is not None:
            self.mobile_mfa_config_type = m.get('MobileMfaConfigType')
        if m.get('MultiIdpInfo') is not None:
            self.multi_idp_info = m.get('MultiIdpInfo')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PcLoginType') is not None:
            self.pc_login_type = m.get('PcLoginType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('VerifyAesKey') is not None:
            self.verify_aes_key = m.get('VerifyAesKey')
        if m.get('VerifyToken') is not None:
            self.verify_token = m.get('VerifyToken')
        if m.get('VerifyUrl') is not None:
            self.verify_url = m.get('VerifyUrl')
        return self


class GetIdpConfigResponseBody(TeaModel):
    def __init__(
        self,
        data: GetIdpConfigResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetIdpConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetIdpConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetIdpConfigResponseBody = None,
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
            temp_model = GetIdpConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPrivateAccessApplicationRequest(TeaModel):
    def __init__(
        self,
        application_id: str = None,
    ):
        # This parameter is required.
        self.application_id = application_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        return self


class GetPrivateAccessApplicationResponseBodyApplicationPortRanges(TeaModel):
    def __init__(
        self,
        begin: int = None,
        end: int = None,
    ):
        self.begin = begin
        self.end = end

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.end is not None:
            result['End'] = self.end
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('End') is not None:
            self.end = m.get('End')
        return self


class GetPrivateAccessApplicationResponseBodyApplication(TeaModel):
    def __init__(
        self,
        addresses: List[str] = None,
        application_id: str = None,
        browser_access_status: str = None,
        connector_ids: List[str] = None,
        create_time: str = None,
        description: str = None,
        l_7proxy_domain_automatic: str = None,
        l_7proxy_domain_custom: str = None,
        name: str = None,
        policy_ids: List[str] = None,
        port_ranges: List[GetPrivateAccessApplicationResponseBodyApplicationPortRanges] = None,
        protocol: str = None,
        status: str = None,
        tag_ids: List[str] = None,
    ):
        self.addresses = addresses
        self.application_id = application_id
        self.browser_access_status = browser_access_status
        self.connector_ids = connector_ids
        self.create_time = create_time
        self.description = description
        self.l_7proxy_domain_automatic = l_7proxy_domain_automatic
        self.l_7proxy_domain_custom = l_7proxy_domain_custom
        self.name = name
        self.policy_ids = policy_ids
        self.port_ranges = port_ranges
        self.protocol = protocol
        self.status = status
        self.tag_ids = tag_ids

    def validate(self):
        if self.port_ranges:
            for k in self.port_ranges:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.addresses is not None:
            result['Addresses'] = self.addresses
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.browser_access_status is not None:
            result['BrowserAccessStatus'] = self.browser_access_status
        if self.connector_ids is not None:
            result['ConnectorIds'] = self.connector_ids
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.l_7proxy_domain_automatic is not None:
            result['L7ProxyDomainAutomatic'] = self.l_7proxy_domain_automatic
        if self.l_7proxy_domain_custom is not None:
            result['L7ProxyDomainCustom'] = self.l_7proxy_domain_custom
        if self.name is not None:
            result['Name'] = self.name
        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids
        result['PortRanges'] = []
        if self.port_ranges is not None:
            for k in self.port_ranges:
                result['PortRanges'].append(k.to_map() if k else None)
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.status is not None:
            result['Status'] = self.status
        if self.tag_ids is not None:
            result['TagIds'] = self.tag_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Addresses') is not None:
            self.addresses = m.get('Addresses')
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('BrowserAccessStatus') is not None:
            self.browser_access_status = m.get('BrowserAccessStatus')
        if m.get('ConnectorIds') is not None:
            self.connector_ids = m.get('ConnectorIds')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('L7ProxyDomainAutomatic') is not None:
            self.l_7proxy_domain_automatic = m.get('L7ProxyDomainAutomatic')
        if m.get('L7ProxyDomainCustom') is not None:
            self.l_7proxy_domain_custom = m.get('L7ProxyDomainCustom')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')
        self.port_ranges = []
        if m.get('PortRanges') is not None:
            for k in m.get('PortRanges'):
                temp_model = GetPrivateAccessApplicationResponseBodyApplicationPortRanges()
                self.port_ranges.append(temp_model.from_map(k))
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TagIds') is not None:
            self.tag_ids = m.get('TagIds')
        return self


class GetPrivateAccessApplicationResponseBody(TeaModel):
    def __init__(
        self,
        application: GetPrivateAccessApplicationResponseBodyApplication = None,
        request_id: str = None,
    ):
        self.application = application
        self.request_id = request_id

    def validate(self):
        if self.application:
            self.application.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application is not None:
            result['Application'] = self.application.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Application') is not None:
            temp_model = GetPrivateAccessApplicationResponseBodyApplication()
            self.application = temp_model.from_map(m['Application'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPrivateAccessApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPrivateAccessApplicationResponseBody = None,
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
            temp_model = GetPrivateAccessApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPrivateAccessPolicyRequest(TeaModel):
    def __init__(
        self,
        policy_id: str = None,
    ):
        # This parameter is required.
        self.policy_id = policy_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        return self


class GetPrivateAccessPolicyResponseBodyPolicyCustomUserAttributes(TeaModel):
    def __init__(
        self,
        idp_id: int = None,
        relation: str = None,
        user_group_type: str = None,
        value: str = None,
    ):
        self.idp_id = idp_id
        self.relation = relation
        self.user_group_type = user_group_type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.idp_id is not None:
            result['IdpId'] = self.idp_id
        if self.relation is not None:
            result['Relation'] = self.relation
        if self.user_group_type is not None:
            result['UserGroupType'] = self.user_group_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdpId') is not None:
            self.idp_id = m.get('IdpId')
        if m.get('Relation') is not None:
            self.relation = m.get('Relation')
        if m.get('UserGroupType') is not None:
            self.user_group_type = m.get('UserGroupType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetPrivateAccessPolicyResponseBodyPolicy(TeaModel):
    def __init__(
        self,
        application_ids: List[str] = None,
        application_type: str = None,
        create_time: str = None,
        custom_user_attributes: List[GetPrivateAccessPolicyResponseBodyPolicyCustomUserAttributes] = None,
        description: str = None,
        device_attribute_action: str = None,
        device_attribute_id: str = None,
        name: str = None,
        policy_action: str = None,
        policy_id: str = None,
        priority: int = None,
        status: str = None,
        tag_ids: List[str] = None,
        user_group_ids: List[str] = None,
        user_group_mode: str = None,
    ):
        self.application_ids = application_ids
        self.application_type = application_type
        self.create_time = create_time
        self.custom_user_attributes = custom_user_attributes
        self.description = description
        self.device_attribute_action = device_attribute_action
        self.device_attribute_id = device_attribute_id
        self.name = name
        self.policy_action = policy_action
        self.policy_id = policy_id
        self.priority = priority
        self.status = status
        self.tag_ids = tag_ids
        self.user_group_ids = user_group_ids
        self.user_group_mode = user_group_mode

    def validate(self):
        if self.custom_user_attributes:
            for k in self.custom_user_attributes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_ids is not None:
            result['ApplicationIds'] = self.application_ids
        if self.application_type is not None:
            result['ApplicationType'] = self.application_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        result['CustomUserAttributes'] = []
        if self.custom_user_attributes is not None:
            for k in self.custom_user_attributes:
                result['CustomUserAttributes'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.device_attribute_action is not None:
            result['DeviceAttributeAction'] = self.device_attribute_action
        if self.device_attribute_id is not None:
            result['DeviceAttributeId'] = self.device_attribute_id
        if self.name is not None:
            result['Name'] = self.name
        if self.policy_action is not None:
            result['PolicyAction'] = self.policy_action
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.status is not None:
            result['Status'] = self.status
        if self.tag_ids is not None:
            result['TagIds'] = self.tag_ids
        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids
        if self.user_group_mode is not None:
            result['UserGroupMode'] = self.user_group_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationIds') is not None:
            self.application_ids = m.get('ApplicationIds')
        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        self.custom_user_attributes = []
        if m.get('CustomUserAttributes') is not None:
            for k in m.get('CustomUserAttributes'):
                temp_model = GetPrivateAccessPolicyResponseBodyPolicyCustomUserAttributes()
                self.custom_user_attributes.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DeviceAttributeAction') is not None:
            self.device_attribute_action = m.get('DeviceAttributeAction')
        if m.get('DeviceAttributeId') is not None:
            self.device_attribute_id = m.get('DeviceAttributeId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PolicyAction') is not None:
            self.policy_action = m.get('PolicyAction')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TagIds') is not None:
            self.tag_ids = m.get('TagIds')
        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')
        if m.get('UserGroupMode') is not None:
            self.user_group_mode = m.get('UserGroupMode')
        return self


class GetPrivateAccessPolicyResponseBody(TeaModel):
    def __init__(
        self,
        policy: GetPrivateAccessPolicyResponseBodyPolicy = None,
        request_id: str = None,
    ):
        self.policy = policy
        self.request_id = request_id

    def validate(self):
        if self.policy:
            self.policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Policy') is not None:
            temp_model = GetPrivateAccessPolicyResponseBodyPolicy()
            self.policy = temp_model.from_map(m['Policy'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPrivateAccessPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPrivateAccessPolicyResponseBody = None,
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
            temp_model = GetPrivateAccessPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRegistrationPolicyRequest(TeaModel):
    def __init__(
        self,
        policy_id: str = None,
    ):
        # This parameter is required.
        self.policy_id = policy_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        return self


class GetRegistrationPolicyResponseBodyLimitDetailLimitCount(TeaModel):
    def __init__(
        self,
        all: int = None,
        mobile: int = None,
        pc: int = None,
    ):
        self.all = all
        self.mobile = mobile
        self.pc = pc

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.pc is not None:
            result['PC'] = self.pc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('PC') is not None:
            self.pc = m.get('PC')
        return self


class GetRegistrationPolicyResponseBodyLimitDetail(TeaModel):
    def __init__(
        self,
        device_belong: str = None,
        limit_count: GetRegistrationPolicyResponseBodyLimitDetailLimitCount = None,
        limit_type: str = None,
    ):
        self.device_belong = device_belong
        self.limit_count = limit_count
        self.limit_type = limit_type

    def validate(self):
        if self.limit_count:
            self.limit_count.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_belong is not None:
            result['DeviceBelong'] = self.device_belong
        if self.limit_count is not None:
            result['LimitCount'] = self.limit_count.to_map()
        if self.limit_type is not None:
            result['LimitType'] = self.limit_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceBelong') is not None:
            self.device_belong = m.get('DeviceBelong')
        if m.get('LimitCount') is not None:
            temp_model = GetRegistrationPolicyResponseBodyLimitDetailLimitCount()
            self.limit_count = temp_model.from_map(m['LimitCount'])
        if m.get('LimitType') is not None:
            self.limit_type = m.get('LimitType')
        return self


class GetRegistrationPolicyResponseBody(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        limit_detail: List[GetRegistrationPolicyResponseBodyLimitDetail] = None,
        match_mode: str = None,
        name: str = None,
        policy_id: str = None,
        priority: int = None,
        request_id: str = None,
        status: str = None,
        user_group_ids: List[str] = None,
        whitelist: List[str] = None,
    ):
        self.create_time = create_time
        self.description = description
        self.limit_detail = limit_detail
        self.match_mode = match_mode
        self.name = name
        self.policy_id = policy_id
        self.priority = priority
        self.request_id = request_id
        self.status = status
        self.user_group_ids = user_group_ids
        self.whitelist = whitelist

    def validate(self):
        if self.limit_detail:
            for k in self.limit_detail:
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
        result['LimitDetail'] = []
        if self.limit_detail is not None:
            for k in self.limit_detail:
                result['LimitDetail'].append(k.to_map() if k else None)
        if self.match_mode is not None:
            result['MatchMode'] = self.match_mode
        if self.name is not None:
            result['Name'] = self.name
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids
        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.limit_detail = []
        if m.get('LimitDetail') is not None:
            for k in m.get('LimitDetail'):
                temp_model = GetRegistrationPolicyResponseBodyLimitDetail()
                self.limit_detail.append(temp_model.from_map(k))
        if m.get('MatchMode') is not None:
            self.match_mode = m.get('MatchMode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')
        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')
        return self


class GetRegistrationPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRegistrationPolicyResponseBody = None,
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
            temp_model = GetRegistrationPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserDeviceRequest(TeaModel):
    def __init__(
        self,
        device_tag: str = None,
    ):
        # This parameter is required.
        self.device_tag = device_tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_tag is not None:
            result['DeviceTag'] = self.device_tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceTag') is not None:
            self.device_tag = m.get('DeviceTag')
        return self


class GetUserDeviceResponseBodyDeviceHistoryUsers(TeaModel):
    def __init__(
        self,
        sase_user_id: str = None,
        username: str = None,
    ):
        self.sase_user_id = sase_user_id
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sase_user_id is not None:
            result['SaseUserId'] = self.sase_user_id
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SaseUserId') is not None:
            self.sase_user_id = m.get('SaseUserId')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class GetUserDeviceResponseBodyDevice(TeaModel):
    def __init__(
        self,
        app_status: str = None,
        app_version: str = None,
        cpu: str = None,
        create_time: str = None,
        department: str = None,
        device_belong: str = None,
        device_model: str = None,
        device_status: str = None,
        device_tag: str = None,
        device_type: str = None,
        device_version: str = None,
        disk: str = None,
        dlp_status: str = None,
        history_users: List[GetUserDeviceResponseBodyDeviceHistoryUsers] = None,
        hostname: str = None,
        ia_status: str = None,
        inner_ip: str = None,
        mac: str = None,
        memory: str = None,
        nac_status: str = None,
        pa_status: str = None,
        sase_user_id: str = None,
        sharing_status: bool = None,
        src_ip: str = None,
        update_time: str = None,
        username: str = None,
    ):
        self.app_status = app_status
        self.app_version = app_version
        self.cpu = cpu
        self.create_time = create_time
        self.department = department
        self.device_belong = device_belong
        self.device_model = device_model
        self.device_status = device_status
        self.device_tag = device_tag
        self.device_type = device_type
        self.device_version = device_version
        self.disk = disk
        self.dlp_status = dlp_status
        self.history_users = history_users
        self.hostname = hostname
        self.ia_status = ia_status
        self.inner_ip = inner_ip
        self.mac = mac
        self.memory = memory
        self.nac_status = nac_status
        self.pa_status = pa_status
        self.sase_user_id = sase_user_id
        self.sharing_status = sharing_status
        self.src_ip = src_ip
        self.update_time = update_time
        self.username = username

    def validate(self):
        if self.history_users:
            for k in self.history_users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_status is not None:
            result['AppStatus'] = self.app_status
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.cpu is not None:
            result['CPU'] = self.cpu
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.department is not None:
            result['Department'] = self.department
        if self.device_belong is not None:
            result['DeviceBelong'] = self.device_belong
        if self.device_model is not None:
            result['DeviceModel'] = self.device_model
        if self.device_status is not None:
            result['DeviceStatus'] = self.device_status
        if self.device_tag is not None:
            result['DeviceTag'] = self.device_tag
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.device_version is not None:
            result['DeviceVersion'] = self.device_version
        if self.disk is not None:
            result['Disk'] = self.disk
        if self.dlp_status is not None:
            result['DlpStatus'] = self.dlp_status
        result['HistoryUsers'] = []
        if self.history_users is not None:
            for k in self.history_users:
                result['HistoryUsers'].append(k.to_map() if k else None)
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.ia_status is not None:
            result['IaStatus'] = self.ia_status
        if self.inner_ip is not None:
            result['InnerIP'] = self.inner_ip
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.nac_status is not None:
            result['NacStatus'] = self.nac_status
        if self.pa_status is not None:
            result['PaStatus'] = self.pa_status
        if self.sase_user_id is not None:
            result['SaseUserId'] = self.sase_user_id
        if self.sharing_status is not None:
            result['SharingStatus'] = self.sharing_status
        if self.src_ip is not None:
            result['SrcIP'] = self.src_ip
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppStatus') is not None:
            self.app_status = m.get('AppStatus')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('CPU') is not None:
            self.cpu = m.get('CPU')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Department') is not None:
            self.department = m.get('Department')
        if m.get('DeviceBelong') is not None:
            self.device_belong = m.get('DeviceBelong')
        if m.get('DeviceModel') is not None:
            self.device_model = m.get('DeviceModel')
        if m.get('DeviceStatus') is not None:
            self.device_status = m.get('DeviceStatus')
        if m.get('DeviceTag') is not None:
            self.device_tag = m.get('DeviceTag')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('DeviceVersion') is not None:
            self.device_version = m.get('DeviceVersion')
        if m.get('Disk') is not None:
            self.disk = m.get('Disk')
        if m.get('DlpStatus') is not None:
            self.dlp_status = m.get('DlpStatus')
        self.history_users = []
        if m.get('HistoryUsers') is not None:
            for k in m.get('HistoryUsers'):
                temp_model = GetUserDeviceResponseBodyDeviceHistoryUsers()
                self.history_users.append(temp_model.from_map(k))
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('IaStatus') is not None:
            self.ia_status = m.get('IaStatus')
        if m.get('InnerIP') is not None:
            self.inner_ip = m.get('InnerIP')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('NacStatus') is not None:
            self.nac_status = m.get('NacStatus')
        if m.get('PaStatus') is not None:
            self.pa_status = m.get('PaStatus')
        if m.get('SaseUserId') is not None:
            self.sase_user_id = m.get('SaseUserId')
        if m.get('SharingStatus') is not None:
            self.sharing_status = m.get('SharingStatus')
        if m.get('SrcIP') is not None:
            self.src_ip = m.get('SrcIP')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class GetUserDeviceResponseBody(TeaModel):
    def __init__(
        self,
        device: GetUserDeviceResponseBodyDevice = None,
        request_id: str = None,
    ):
        self.device = device
        self.request_id = request_id

    def validate(self):
        if self.device:
            self.device.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device is not None:
            result['Device'] = self.device.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Device') is not None:
            temp_model = GetUserDeviceResponseBodyDevice()
            self.device = temp_model.from_map(m['Device'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetUserDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserDeviceResponseBody = None,
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
            temp_model = GetUserDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserGroupRequest(TeaModel):
    def __init__(
        self,
        user_group_id: str = None,
    ):
        # This parameter is required.
        self.user_group_id = user_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class GetUserGroupResponseBodyUserGroupAttributes(TeaModel):
    def __init__(
        self,
        idp_id: int = None,
        relation: str = None,
        user_group_type: str = None,
        value: str = None,
    ):
        self.idp_id = idp_id
        self.relation = relation
        self.user_group_type = user_group_type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.idp_id is not None:
            result['IdpId'] = self.idp_id
        if self.relation is not None:
            result['Relation'] = self.relation
        if self.user_group_type is not None:
            result['UserGroupType'] = self.user_group_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdpId') is not None:
            self.idp_id = m.get('IdpId')
        if m.get('Relation') is not None:
            self.relation = m.get('Relation')
        if m.get('UserGroupType') is not None:
            self.user_group_type = m.get('UserGroupType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetUserGroupResponseBodyUserGroup(TeaModel):
    def __init__(
        self,
        attributes: List[GetUserGroupResponseBodyUserGroupAttributes] = None,
        create_time: str = None,
        description: str = None,
        name: str = None,
        user_group_id: str = None,
    ):
        self.attributes = attributes
        self.create_time = create_time
        self.description = description
        self.name = name
        self.user_group_id = user_group_id

    def validate(self):
        if self.attributes:
            for k in self.attributes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Attributes'] = []
        if self.attributes is not None:
            for k in self.attributes:
                result['Attributes'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attributes = []
        if m.get('Attributes') is not None:
            for k in m.get('Attributes'):
                temp_model = GetUserGroupResponseBodyUserGroupAttributes()
                self.attributes.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class GetUserGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        user_group: GetUserGroupResponseBodyUserGroup = None,
    ):
        self.request_id = request_id
        self.user_group = user_group

    def validate(self):
        if self.user_group:
            self.user_group.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_group is not None:
            result['UserGroup'] = self.user_group.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserGroup') is not None:
            temp_model = GetUserGroupResponseBodyUserGroup()
            self.user_group = temp_model.from_map(m['UserGroup'])
        return self


class GetUserGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserGroupResponseBody = None,
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
            temp_model = GetUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWmEmbedTaskRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetWmEmbedTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        file_url: str = None,
        file_url_exp: str = None,
        filename: str = None,
        out_file_hash_md_5: str = None,
        out_file_size: int = None,
        task_id: str = None,
        task_status: str = None,
    ):
        self.file_url = file_url
        self.file_url_exp = file_url_exp
        self.filename = filename
        self.out_file_hash_md_5 = out_file_hash_md_5
        self.out_file_size = out_file_size
        self.task_id = task_id
        self.task_status = task_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.file_url_exp is not None:
            result['FileUrlExp'] = self.file_url_exp
        if self.filename is not None:
            result['Filename'] = self.filename
        if self.out_file_hash_md_5 is not None:
            result['OutFileHashMd5'] = self.out_file_hash_md_5
        if self.out_file_size is not None:
            result['OutFileSize'] = self.out_file_size
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('FileUrlExp') is not None:
            self.file_url_exp = m.get('FileUrlExp')
        if m.get('Filename') is not None:
            self.filename = m.get('Filename')
        if m.get('OutFileHashMd5') is not None:
            self.out_file_hash_md_5 = m.get('OutFileHashMd5')
        if m.get('OutFileSize') is not None:
            self.out_file_size = m.get('OutFileSize')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        return self


class GetWmEmbedTaskResponseBody(TeaModel):
    def __init__(
        self,
        data: GetWmEmbedTaskResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetWmEmbedTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetWmEmbedTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetWmEmbedTaskResponseBody = None,
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
            temp_model = GetWmEmbedTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWmExtractTaskRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetWmExtractTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        filename: str = None,
        status: str = None,
        task_id: str = None,
        wm_info_bytes_b64: str = None,
        wm_info_size: int = None,
        wm_info_uint: int = None,
        wm_type: str = None,
    ):
        self.create_time = create_time
        self.filename = filename
        self.status = status
        self.task_id = task_id
        self.wm_info_bytes_b64 = wm_info_bytes_b64
        self.wm_info_size = wm_info_size
        self.wm_info_uint = wm_info_uint
        self.wm_type = wm_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.filename is not None:
            result['Filename'] = self.filename
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.wm_info_bytes_b64 is not None:
            result['WmInfoBytesB64'] = self.wm_info_bytes_b64
        if self.wm_info_size is not None:
            result['WmInfoSize'] = self.wm_info_size
        if self.wm_info_uint is not None:
            result['WmInfoUint'] = self.wm_info_uint
        if self.wm_type is not None:
            result['WmType'] = self.wm_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Filename') is not None:
            self.filename = m.get('Filename')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('WmInfoBytesB64') is not None:
            self.wm_info_bytes_b64 = m.get('WmInfoBytesB64')
        if m.get('WmInfoSize') is not None:
            self.wm_info_size = m.get('WmInfoSize')
        if m.get('WmInfoUint') is not None:
            self.wm_info_uint = m.get('WmInfoUint')
        if m.get('WmType') is not None:
            self.wm_type = m.get('WmType')
        return self


class GetWmExtractTaskResponseBody(TeaModel):
    def __init__(
        self,
        data: GetWmExtractTaskResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetWmExtractTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetWmExtractTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetWmExtractTaskResponseBody = None,
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
            temp_model = GetWmExtractTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListApplicationsForPrivateAccessPolicyRequest(TeaModel):
    def __init__(
        self,
        policy_ids: List[str] = None,
    ):
        # This parameter is required.
        self.policy_ids = policy_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')
        return self


class ListApplicationsForPrivateAccessPolicyResponseBodyPolicesApplicationsPortRanges(TeaModel):
    def __init__(
        self,
        begin: int = None,
        end: int = None,
    ):
        self.begin = begin
        self.end = end

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.end is not None:
            result['End'] = self.end
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('End') is not None:
            self.end = m.get('End')
        return self


class ListApplicationsForPrivateAccessPolicyResponseBodyPolicesApplications(TeaModel):
    def __init__(
        self,
        addresses: List[str] = None,
        application_id: str = None,
        create_time: str = None,
        description: str = None,
        name: str = None,
        port_ranges: List[ListApplicationsForPrivateAccessPolicyResponseBodyPolicesApplicationsPortRanges] = None,
        protocol: str = None,
        status: str = None,
    ):
        self.addresses = addresses
        self.application_id = application_id
        self.create_time = create_time
        self.description = description
        self.name = name
        self.port_ranges = port_ranges
        self.protocol = protocol
        self.status = status

    def validate(self):
        if self.port_ranges:
            for k in self.port_ranges:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.addresses is not None:
            result['Addresses'] = self.addresses
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        result['PortRanges'] = []
        if self.port_ranges is not None:
            for k in self.port_ranges:
                result['PortRanges'].append(k.to_map() if k else None)
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Addresses') is not None:
            self.addresses = m.get('Addresses')
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.port_ranges = []
        if m.get('PortRanges') is not None:
            for k in m.get('PortRanges'):
                temp_model = ListApplicationsForPrivateAccessPolicyResponseBodyPolicesApplicationsPortRanges()
                self.port_ranges.append(temp_model.from_map(k))
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListApplicationsForPrivateAccessPolicyResponseBodyPolices(TeaModel):
    def __init__(
        self,
        applications: List[ListApplicationsForPrivateAccessPolicyResponseBodyPolicesApplications] = None,
        policy_id: str = None,
    ):
        self.applications = applications
        self.policy_id = policy_id

    def validate(self):
        if self.applications:
            for k in self.applications:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Applications'] = []
        if self.applications is not None:
            for k in self.applications:
                result['Applications'].append(k.to_map() if k else None)
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.applications = []
        if m.get('Applications') is not None:
            for k in m.get('Applications'):
                temp_model = ListApplicationsForPrivateAccessPolicyResponseBodyPolicesApplications()
                self.applications.append(temp_model.from_map(k))
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        return self


class ListApplicationsForPrivateAccessPolicyResponseBody(TeaModel):
    def __init__(
        self,
        polices: List[ListApplicationsForPrivateAccessPolicyResponseBodyPolices] = None,
        request_id: str = None,
    ):
        self.polices = polices
        self.request_id = request_id

    def validate(self):
        if self.polices:
            for k in self.polices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Polices'] = []
        if self.polices is not None:
            for k in self.polices:
                result['Polices'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.polices = []
        if m.get('Polices') is not None:
            for k in m.get('Polices'):
                temp_model = ListApplicationsForPrivateAccessPolicyResponseBodyPolices()
                self.polices.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListApplicationsForPrivateAccessPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListApplicationsForPrivateAccessPolicyResponseBody = None,
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
            temp_model = ListApplicationsForPrivateAccessPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListApplicationsForPrivateAccessTagRequest(TeaModel):
    def __init__(
        self,
        tag_ids: List[str] = None,
    ):
        # This parameter is required.
        self.tag_ids = tag_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_ids is not None:
            result['TagIds'] = self.tag_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagIds') is not None:
            self.tag_ids = m.get('TagIds')
        return self


class ListApplicationsForPrivateAccessTagResponseBodyTagsApplicationsPortRanges(TeaModel):
    def __init__(
        self,
        begin: int = None,
        end: int = None,
    ):
        self.begin = begin
        self.end = end

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.end is not None:
            result['End'] = self.end
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('End') is not None:
            self.end = m.get('End')
        return self


class ListApplicationsForPrivateAccessTagResponseBodyTagsApplications(TeaModel):
    def __init__(
        self,
        addresses: List[str] = None,
        application_id: str = None,
        create_time: str = None,
        description: str = None,
        name: str = None,
        port_ranges: List[ListApplicationsForPrivateAccessTagResponseBodyTagsApplicationsPortRanges] = None,
        protocol: str = None,
        status: str = None,
    ):
        self.addresses = addresses
        self.application_id = application_id
        # 内网访问应用创建时间。
        self.create_time = create_time
        self.description = description
        self.name = name
        self.port_ranges = port_ranges
        self.protocol = protocol
        self.status = status

    def validate(self):
        if self.port_ranges:
            for k in self.port_ranges:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.addresses is not None:
            result['Addresses'] = self.addresses
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        result['PortRanges'] = []
        if self.port_ranges is not None:
            for k in self.port_ranges:
                result['PortRanges'].append(k.to_map() if k else None)
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Addresses') is not None:
            self.addresses = m.get('Addresses')
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.port_ranges = []
        if m.get('PortRanges') is not None:
            for k in m.get('PortRanges'):
                temp_model = ListApplicationsForPrivateAccessTagResponseBodyTagsApplicationsPortRanges()
                self.port_ranges.append(temp_model.from_map(k))
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListApplicationsForPrivateAccessTagResponseBodyTags(TeaModel):
    def __init__(
        self,
        applications: List[ListApplicationsForPrivateAccessTagResponseBodyTagsApplications] = None,
        tag_id: str = None,
    ):
        self.applications = applications
        self.tag_id = tag_id

    def validate(self):
        if self.applications:
            for k in self.applications:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Applications'] = []
        if self.applications is not None:
            for k in self.applications:
                result['Applications'].append(k.to_map() if k else None)
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.applications = []
        if m.get('Applications') is not None:
            for k in m.get('Applications'):
                temp_model = ListApplicationsForPrivateAccessTagResponseBodyTagsApplications()
                self.applications.append(temp_model.from_map(k))
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        return self


class ListApplicationsForPrivateAccessTagResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tags: List[ListApplicationsForPrivateAccessTagResponseBodyTags] = None,
    ):
        self.request_id = request_id
        self.tags = tags

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListApplicationsForPrivateAccessTagResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListApplicationsForPrivateAccessTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListApplicationsForPrivateAccessTagResponseBody = None,
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
            temp_model = ListApplicationsForPrivateAccessTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClientUsersRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        department_id: str = None,
        email: str = None,
        idp_config_id: str = None,
        mobile_number: str = None,
        page_size: int = None,
        status: str = None,
        username: str = None,
    ):
        self.current_page = current_page
        self.department_id = department_id
        self.email = email
        # This parameter is required.
        self.idp_config_id = idp_config_id
        self.mobile_number = mobile_number
        self.page_size = page_size
        self.status = status
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.department_id is not None:
            result['DepartmentId'] = self.department_id
        if self.email is not None:
            result['Email'] = self.email
        if self.idp_config_id is not None:
            result['IdpConfigId'] = self.idp_config_id
        if self.mobile_number is not None:
            result['MobileNumber'] = self.mobile_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('IdpConfigId') is not None:
            self.idp_config_id = m.get('IdpConfigId')
        if m.get('MobileNumber') is not None:
            self.mobile_number = m.get('MobileNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class ListClientUsersResponseBodyDataDataListDepartment(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListClientUsersResponseBodyDataDataList(TeaModel):
    def __init__(
        self,
        department: ListClientUsersResponseBodyDataDataListDepartment = None,
        department_id: str = None,
        description: str = None,
        email: str = None,
        id: str = None,
        idp_config_id: str = None,
        mobile_number: str = None,
        status: str = None,
        user_id: str = None,
        username: str = None,
    ):
        self.department = department
        self.department_id = department_id
        self.description = description
        self.email = email
        self.id = id
        self.idp_config_id = idp_config_id
        self.mobile_number = mobile_number
        self.status = status
        self.user_id = user_id
        self.username = username

    def validate(self):
        if self.department:
            self.department.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.department is not None:
            result['Department'] = self.department.to_map()
        if self.department_id is not None:
            result['DepartmentId'] = self.department_id
        if self.description is not None:
            result['Description'] = self.description
        if self.email is not None:
            result['Email'] = self.email
        if self.id is not None:
            result['Id'] = self.id
        if self.idp_config_id is not None:
            result['IdpConfigId'] = self.idp_config_id
        if self.mobile_number is not None:
            result['MobileNumber'] = self.mobile_number
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Department') is not None:
            temp_model = ListClientUsersResponseBodyDataDataListDepartment()
            self.department = temp_model.from_map(m['Department'])
        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdpConfigId') is not None:
            self.idp_config_id = m.get('IdpConfigId')
        if m.get('MobileNumber') is not None:
            self.mobile_number = m.get('MobileNumber')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class ListClientUsersResponseBodyData(TeaModel):
    def __init__(
        self,
        data_list: List[ListClientUsersResponseBodyDataDataList] = None,
        total_num: int = None,
    ):
        self.data_list = data_list
        self.total_num = total_num

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['DataList'].append(k.to_map() if k else None)
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = ListClientUsersResponseBodyDataDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class ListClientUsersResponseBody(TeaModel):
    def __init__(
        self,
        data: ListClientUsersResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListClientUsersResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListClientUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListClientUsersResponseBody = None,
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
            temp_model = ListClientUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConnectorsRequest(TeaModel):
    def __init__(
        self,
        connector_ids: List[str] = None,
        current_page: int = None,
        name: str = None,
        page_size: int = None,
        status: str = None,
        switch_status: str = None,
    ):
        self.connector_ids = connector_ids
        # This parameter is required.
        self.current_page = current_page
        self.name = name
        # This parameter is required.
        self.page_size = page_size
        self.status = status
        self.switch_status = switch_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connector_ids is not None:
            result['ConnectorIds'] = self.connector_ids
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.name is not None:
            result['Name'] = self.name
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        if self.switch_status is not None:
            result['SwitchStatus'] = self.switch_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectorIds') is not None:
            self.connector_ids = m.get('ConnectorIds')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SwitchStatus') is not None:
            self.switch_status = m.get('SwitchStatus')
        return self


class ListConnectorsResponseBodyConnectorsApplications(TeaModel):
    def __init__(
        self,
        application_id: str = None,
        application_name: str = None,
    ):
        self.application_id = application_id
        self.application_name = application_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        return self


class ListConnectorsResponseBodyConnectorsConnectorClients(TeaModel):
    def __init__(
        self,
        connection_status: str = None,
        dev_tag: str = None,
        hostname: str = None,
        public_ip: str = None,
    ):
        self.connection_status = connection_status
        self.dev_tag = dev_tag
        self.hostname = hostname
        self.public_ip = public_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_status is not None:
            result['ConnectionStatus'] = self.connection_status
        if self.dev_tag is not None:
            result['DevTag'] = self.dev_tag
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.public_ip is not None:
            result['PublicIp'] = self.public_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionStatus') is not None:
            self.connection_status = m.get('ConnectionStatus')
        if m.get('DevTag') is not None:
            self.dev_tag = m.get('DevTag')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('PublicIp') is not None:
            self.public_ip = m.get('PublicIp')
        return self


class ListConnectorsResponseBodyConnectorsUpgradeTime(TeaModel):
    def __init__(
        self,
        end: str = None,
        start: str = None,
    ):
        self.end = end
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['End'] = self.end
        if self.start is not None:
            result['Start'] = self.start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        return self


class ListConnectorsResponseBodyConnectors(TeaModel):
    def __init__(
        self,
        applications: List[ListConnectorsResponseBodyConnectorsApplications] = None,
        connector_clients: List[ListConnectorsResponseBodyConnectorsConnectorClients] = None,
        connector_id: str = None,
        create_time: str = None,
        name: str = None,
        region_id: str = None,
        status: str = None,
        switch_status: str = None,
        upgrade_time: ListConnectorsResponseBodyConnectorsUpgradeTime = None,
    ):
        self.applications = applications
        self.connector_clients = connector_clients
        # ConnectorID。
        self.connector_id = connector_id
        self.create_time = create_time
        self.name = name
        self.region_id = region_id
        self.status = status
        self.switch_status = switch_status
        self.upgrade_time = upgrade_time

    def validate(self):
        if self.applications:
            for k in self.applications:
                if k:
                    k.validate()
        if self.connector_clients:
            for k in self.connector_clients:
                if k:
                    k.validate()
        if self.upgrade_time:
            self.upgrade_time.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Applications'] = []
        if self.applications is not None:
            for k in self.applications:
                result['Applications'].append(k.to_map() if k else None)
        result['ConnectorClients'] = []
        if self.connector_clients is not None:
            for k in self.connector_clients:
                result['ConnectorClients'].append(k.to_map() if k else None)
        if self.connector_id is not None:
            result['ConnectorId'] = self.connector_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.switch_status is not None:
            result['SwitchStatus'] = self.switch_status
        if self.upgrade_time is not None:
            result['UpgradeTime'] = self.upgrade_time.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.applications = []
        if m.get('Applications') is not None:
            for k in m.get('Applications'):
                temp_model = ListConnectorsResponseBodyConnectorsApplications()
                self.applications.append(temp_model.from_map(k))
        self.connector_clients = []
        if m.get('ConnectorClients') is not None:
            for k in m.get('ConnectorClients'):
                temp_model = ListConnectorsResponseBodyConnectorsConnectorClients()
                self.connector_clients.append(temp_model.from_map(k))
        if m.get('ConnectorId') is not None:
            self.connector_id = m.get('ConnectorId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SwitchStatus') is not None:
            self.switch_status = m.get('SwitchStatus')
        if m.get('UpgradeTime') is not None:
            temp_model = ListConnectorsResponseBodyConnectorsUpgradeTime()
            self.upgrade_time = temp_model.from_map(m['UpgradeTime'])
        return self


class ListConnectorsResponseBody(TeaModel):
    def __init__(
        self,
        connectors: List[ListConnectorsResponseBodyConnectors] = None,
        request_id: str = None,
        total_num: int = None,
    ):
        self.connectors = connectors
        self.request_id = request_id
        self.total_num = total_num

    def validate(self):
        if self.connectors:
            for k in self.connectors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Connectors'] = []
        if self.connectors is not None:
            for k in self.connectors:
                result['Connectors'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.connectors = []
        if m.get('Connectors') is not None:
            for k in m.get('Connectors'):
                temp_model = ListConnectorsResponseBodyConnectors()
                self.connectors.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class ListConnectorsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListConnectorsResponseBody = None,
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
            temp_model = ListConnectorsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDynamicRouteRegionsResponseBody(TeaModel):
    def __init__(
        self,
        regions: List[str] = None,
        request_id: str = None,
        total_num: int = None,
    ):
        self.regions = regions
        self.request_id = request_id
        self.total_num = total_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.regions is not None:
            result['Regions'] = self.regions
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Regions') is not None:
            self.regions = m.get('Regions')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class ListDynamicRouteRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDynamicRouteRegionsResponseBody = None,
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
            temp_model = ListDynamicRouteRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDynamicRoutesRequest(TeaModel):
    def __init__(
        self,
        application_id: str = None,
        current_page: int = None,
        dynamic_route_ids: List[str] = None,
        name: str = None,
        next_hop: str = None,
        page_size: int = None,
        region_ids: List[str] = None,
        status: str = None,
        tag_id: str = None,
    ):
        self.application_id = application_id
        # This parameter is required.
        self.current_page = current_page
        self.dynamic_route_ids = dynamic_route_ids
        self.name = name
        self.next_hop = next_hop
        # This parameter is required.
        self.page_size = page_size
        self.region_ids = region_ids
        self.status = status
        self.tag_id = tag_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.dynamic_route_ids is not None:
            result['DynamicRouteIds'] = self.dynamic_route_ids
        if self.name is not None:
            result['Name'] = self.name
        if self.next_hop is not None:
            result['NextHop'] = self.next_hop
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids
        if self.status is not None:
            result['Status'] = self.status
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DynamicRouteIds') is not None:
            self.dynamic_route_ids = m.get('DynamicRouteIds')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NextHop') is not None:
            self.next_hop = m.get('NextHop')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionIds') is not None:
            self.region_ids = m.get('RegionIds')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        return self


class ListDynamicRoutesResponseBodyDynamicRoutes(TeaModel):
    def __init__(
        self,
        application_ids: List[str] = None,
        application_type: str = None,
        create_time: str = None,
        description: str = None,
        dynamic_route_id: str = None,
        dynamic_route_type: str = None,
        name: str = None,
        next_hop: str = None,
        priority: int = None,
        region_ids: List[str] = None,
        status: str = None,
        tag_ids: List[str] = None,
    ):
        self.application_ids = application_ids
        self.application_type = application_type
        self.create_time = create_time
        self.description = description
        self.dynamic_route_id = dynamic_route_id
        self.dynamic_route_type = dynamic_route_type
        self.name = name
        self.next_hop = next_hop
        self.priority = priority
        self.region_ids = region_ids
        self.status = status
        self.tag_ids = tag_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_ids is not None:
            result['ApplicationIds'] = self.application_ids
        if self.application_type is not None:
            result['ApplicationType'] = self.application_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.dynamic_route_id is not None:
            result['DynamicRouteId'] = self.dynamic_route_id
        if self.dynamic_route_type is not None:
            result['DynamicRouteType'] = self.dynamic_route_type
        if self.name is not None:
            result['Name'] = self.name
        if self.next_hop is not None:
            result['NextHop'] = self.next_hop
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids
        if self.status is not None:
            result['Status'] = self.status
        if self.tag_ids is not None:
            result['TagIds'] = self.tag_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationIds') is not None:
            self.application_ids = m.get('ApplicationIds')
        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DynamicRouteId') is not None:
            self.dynamic_route_id = m.get('DynamicRouteId')
        if m.get('DynamicRouteType') is not None:
            self.dynamic_route_type = m.get('DynamicRouteType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NextHop') is not None:
            self.next_hop = m.get('NextHop')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('RegionIds') is not None:
            self.region_ids = m.get('RegionIds')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TagIds') is not None:
            self.tag_ids = m.get('TagIds')
        return self


class ListDynamicRoutesResponseBody(TeaModel):
    def __init__(
        self,
        dynamic_routes: List[ListDynamicRoutesResponseBodyDynamicRoutes] = None,
        request_id: str = None,
        total_num: int = None,
    ):
        self.dynamic_routes = dynamic_routes
        self.request_id = request_id
        self.total_num = total_num

    def validate(self):
        if self.dynamic_routes:
            for k in self.dynamic_routes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DynamicRoutes'] = []
        if self.dynamic_routes is not None:
            for k in self.dynamic_routes:
                result['DynamicRoutes'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dynamic_routes = []
        if m.get('DynamicRoutes') is not None:
            for k in m.get('DynamicRoutes'):
                temp_model = ListDynamicRoutesResponseBodyDynamicRoutes()
                self.dynamic_routes.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class ListDynamicRoutesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDynamicRoutesResponseBody = None,
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
            temp_model = ListDynamicRoutesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListExcessiveDeviceRegistrationApplicationsRequest(TeaModel):
    def __init__(
        self,
        application_ids: List[str] = None,
        current_page: int = None,
        department: str = None,
        device_tag: str = None,
        hostname: str = None,
        mac: str = None,
        page_size: int = None,
        sase_user_id: str = None,
        statuses: List[str] = None,
        username: str = None,
    ):
        self.application_ids = application_ids
        # This parameter is required.
        self.current_page = current_page
        self.department = department
        self.device_tag = device_tag
        self.hostname = hostname
        self.mac = mac
        # This parameter is required.
        self.page_size = page_size
        self.sase_user_id = sase_user_id
        self.statuses = statuses
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_ids is not None:
            result['ApplicationIds'] = self.application_ids
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.department is not None:
            result['Department'] = self.department
        if self.device_tag is not None:
            result['DeviceTag'] = self.device_tag
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sase_user_id is not None:
            result['SaseUserId'] = self.sase_user_id
        if self.statuses is not None:
            result['Statuses'] = self.statuses
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationIds') is not None:
            self.application_ids = m.get('ApplicationIds')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Department') is not None:
            self.department = m.get('Department')
        if m.get('DeviceTag') is not None:
            self.device_tag = m.get('DeviceTag')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SaseUserId') is not None:
            self.sase_user_id = m.get('SaseUserId')
        if m.get('Statuses') is not None:
            self.statuses = m.get('Statuses')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class ListExcessiveDeviceRegistrationApplicationsResponseBodyApplications(TeaModel):
    def __init__(
        self,
        application_id: str = None,
        create_time: str = None,
        department: str = None,
        description: str = None,
        device_tag: str = None,
        device_type: str = None,
        hostname: str = None,
        is_used: bool = None,
        mac: str = None,
        sase_user_id: str = None,
        status: str = None,
        username: str = None,
    ):
        self.application_id = application_id
        self.create_time = create_time
        self.department = department
        self.description = description
        self.device_tag = device_tag
        self.device_type = device_type
        self.hostname = hostname
        self.is_used = is_used
        self.mac = mac
        self.sase_user_id = sase_user_id
        self.status = status
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.department is not None:
            result['Department'] = self.department
        if self.description is not None:
            result['Description'] = self.description
        if self.device_tag is not None:
            result['DeviceTag'] = self.device_tag
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.is_used is not None:
            result['IsUsed'] = self.is_used
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.sase_user_id is not None:
            result['SaseUserId'] = self.sase_user_id
        if self.status is not None:
            result['Status'] = self.status
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Department') is not None:
            self.department = m.get('Department')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DeviceTag') is not None:
            self.device_tag = m.get('DeviceTag')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('IsUsed') is not None:
            self.is_used = m.get('IsUsed')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('SaseUserId') is not None:
            self.sase_user_id = m.get('SaseUserId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class ListExcessiveDeviceRegistrationApplicationsResponseBody(TeaModel):
    def __init__(
        self,
        applications: List[ListExcessiveDeviceRegistrationApplicationsResponseBodyApplications] = None,
        request_id: str = None,
        total_num: int = None,
    ):
        self.applications = applications
        self.request_id = request_id
        self.total_num = total_num

    def validate(self):
        if self.applications:
            for k in self.applications:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Applications'] = []
        if self.applications is not None:
            for k in self.applications:
                result['Applications'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.applications = []
        if m.get('Applications') is not None:
            for k in m.get('Applications'):
                temp_model = ListExcessiveDeviceRegistrationApplicationsResponseBodyApplications()
                self.applications.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class ListExcessiveDeviceRegistrationApplicationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListExcessiveDeviceRegistrationApplicationsResponseBody = None,
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
            temp_model = ListExcessiveDeviceRegistrationApplicationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIdpConfigsRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        include: str = None,
        page_size: int = None,
    ):
        self.current_page = current_page
        self.include = include
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.include is not None:
            result['Include'] = self.include
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Include') is not None:
            self.include = m.get('Include')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListIdpConfigsResponseBodyDataDataList(TeaModel):
    def __init__(
        self,
        description: str = None,
        id: str = None,
        mfa: str = None,
        mobile_login_type: str = None,
        mobile_mfa_config_type: str = None,
        multi_idp_info: str = None,
        name: str = None,
        pc_login_type: str = None,
        status: str = None,
        type: str = None,
        update_time: str = None,
    ):
        self.description = description
        self.id = id
        self.mfa = mfa
        self.mobile_login_type = mobile_login_type
        self.mobile_mfa_config_type = mobile_mfa_config_type
        self.multi_idp_info = multi_idp_info
        self.name = name
        self.pc_login_type = pc_login_type
        self.status = status
        self.type = type
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.mfa is not None:
            result['Mfa'] = self.mfa
        if self.mobile_login_type is not None:
            result['MobileLoginType'] = self.mobile_login_type
        if self.mobile_mfa_config_type is not None:
            result['MobileMfaConfigType'] = self.mobile_mfa_config_type
        if self.multi_idp_info is not None:
            result['MultiIdpInfo'] = self.multi_idp_info
        if self.name is not None:
            result['Name'] = self.name
        if self.pc_login_type is not None:
            result['PcLoginType'] = self.pc_login_type
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Mfa') is not None:
            self.mfa = m.get('Mfa')
        if m.get('MobileLoginType') is not None:
            self.mobile_login_type = m.get('MobileLoginType')
        if m.get('MobileMfaConfigType') is not None:
            self.mobile_mfa_config_type = m.get('MobileMfaConfigType')
        if m.get('MultiIdpInfo') is not None:
            self.multi_idp_info = m.get('MultiIdpInfo')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PcLoginType') is not None:
            self.pc_login_type = m.get('PcLoginType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListIdpConfigsResponseBodyData(TeaModel):
    def __init__(
        self,
        data_list: List[ListIdpConfigsResponseBodyDataDataList] = None,
        total_num: int = None,
    ):
        self.data_list = data_list
        self.total_num = total_num

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['DataList'].append(k.to_map() if k else None)
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = ListIdpConfigsResponseBodyDataDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class ListIdpConfigsResponseBody(TeaModel):
    def __init__(
        self,
        data: ListIdpConfigsResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListIdpConfigsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListIdpConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListIdpConfigsResponseBody = None,
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
            temp_model = ListIdpConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIdpDepartmentsRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        idp_config_id: str = None,
        page_size: int = None,
    ):
        self.current_page = current_page
        # This parameter is required.
        self.idp_config_id = idp_config_id
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.idp_config_id is not None:
            result['IdpConfigId'] = self.idp_config_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('IdpConfigId') is not None:
            self.idp_config_id = m.get('IdpConfigId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListIdpDepartmentsResponseBodyDataDataList(TeaModel):
    def __init__(
        self,
        id: str = None,
        idp_config_id: str = None,
        name: str = None,
    ):
        self.id = id
        self.idp_config_id = idp_config_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.idp_config_id is not None:
            result['IdpConfigId'] = self.idp_config_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdpConfigId') is not None:
            self.idp_config_id = m.get('IdpConfigId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListIdpDepartmentsResponseBodyData(TeaModel):
    def __init__(
        self,
        data_list: List[ListIdpDepartmentsResponseBodyDataDataList] = None,
        total_num: int = None,
    ):
        self.data_list = data_list
        self.total_num = total_num

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['DataList'].append(k.to_map() if k else None)
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = ListIdpDepartmentsResponseBodyDataDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class ListIdpDepartmentsResponseBody(TeaModel):
    def __init__(
        self,
        data: ListIdpDepartmentsResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListIdpDepartmentsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListIdpDepartmentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListIdpDepartmentsResponseBody = None,
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
            temp_model = ListIdpDepartmentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNacUserCertRequest(TeaModel):
    def __init__(
        self,
        current_page: str = None,
        department: str = None,
        device_type: str = None,
        end_time: int = None,
        page_size: str = None,
        start_time: int = None,
        status: str = None,
        username: str = None,
    ):
        self.current_page = current_page
        self.department = department
        self.device_type = device_type
        self.end_time = end_time
        self.page_size = page_size
        self.start_time = start_time
        self.status = status
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.department is not None:
            result['Department'] = self.department
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Department') is not None:
            self.department = m.get('Department')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class ListNacUserCertResponseBodyDataList(TeaModel):
    def __init__(
        self,
        aliuid: str = None,
        department: str = None,
        dev_tag: str = None,
        device_type: str = None,
        expired_time: str = None,
        hostname: str = None,
        mac: str = None,
        status: str = None,
        user_id: str = None,
        username: str = None,
    ):
        self.aliuid = aliuid
        self.department = department
        self.dev_tag = dev_tag
        self.device_type = device_type
        self.expired_time = expired_time
        self.hostname = hostname
        self.mac = mac
        self.status = status
        self.user_id = user_id
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid
        if self.department is not None:
            result['Department'] = self.department
        if self.dev_tag is not None:
            result['DevTag'] = self.dev_tag
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')
        if m.get('Department') is not None:
            self.department = m.get('Department')
        if m.get('DevTag') is not None:
            self.dev_tag = m.get('DevTag')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class ListNacUserCertResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data_list: List[ListNacUserCertResponseBodyDataList] = None,
        message: str = None,
        request_id: str = None,
        total_num: int = None,
    ):
        self.code = code
        self.data_list = data_list
        self.message = message
        self.request_id = request_id
        self.total_num = total_num

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['DataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['DataList'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = ListNacUserCertResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class ListNacUserCertResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListNacUserCertResponseBody = None,
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
            temp_model = ListNacUserCertResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPolicesForPrivateAccessApplicationRequest(TeaModel):
    def __init__(
        self,
        application_ids: List[str] = None,
    ):
        # This parameter is required.
        self.application_ids = application_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_ids is not None:
            result['ApplicationIds'] = self.application_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationIds') is not None:
            self.application_ids = m.get('ApplicationIds')
        return self


class ListPolicesForPrivateAccessApplicationResponseBodyApplicationsPoliciesCustomUserAttributes(TeaModel):
    def __init__(
        self,
        idp_id: int = None,
        relation: str = None,
        user_group_type: str = None,
        value: str = None,
    ):
        self.idp_id = idp_id
        self.relation = relation
        self.user_group_type = user_group_type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.idp_id is not None:
            result['IdpId'] = self.idp_id
        if self.relation is not None:
            result['Relation'] = self.relation
        if self.user_group_type is not None:
            result['UserGroupType'] = self.user_group_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdpId') is not None:
            self.idp_id = m.get('IdpId')
        if m.get('Relation') is not None:
            self.relation = m.get('Relation')
        if m.get('UserGroupType') is not None:
            self.user_group_type = m.get('UserGroupType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListPolicesForPrivateAccessApplicationResponseBodyApplicationsPolicies(TeaModel):
    def __init__(
        self,
        application_type: str = None,
        create_time: str = None,
        custom_user_attributes: List[ListPolicesForPrivateAccessApplicationResponseBodyApplicationsPoliciesCustomUserAttributes] = None,
        description: str = None,
        name: str = None,
        policy_action: str = None,
        policy_id: str = None,
        priority: int = None,
        status: str = None,
        user_group_type: str = None,
    ):
        self.application_type = application_type
        self.create_time = create_time
        self.custom_user_attributes = custom_user_attributes
        self.description = description
        self.name = name
        self.policy_action = policy_action
        self.policy_id = policy_id
        self.priority = priority
        self.status = status
        self.user_group_type = user_group_type

    def validate(self):
        if self.custom_user_attributes:
            for k in self.custom_user_attributes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_type is not None:
            result['ApplicationType'] = self.application_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        result['CustomUserAttributes'] = []
        if self.custom_user_attributes is not None:
            for k in self.custom_user_attributes:
                result['CustomUserAttributes'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.policy_action is not None:
            result['PolicyAction'] = self.policy_action
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.status is not None:
            result['Status'] = self.status
        if self.user_group_type is not None:
            result['UserGroupType'] = self.user_group_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        self.custom_user_attributes = []
        if m.get('CustomUserAttributes') is not None:
            for k in m.get('CustomUserAttributes'):
                temp_model = ListPolicesForPrivateAccessApplicationResponseBodyApplicationsPoliciesCustomUserAttributes()
                self.custom_user_attributes.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PolicyAction') is not None:
            self.policy_action = m.get('PolicyAction')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserGroupType') is not None:
            self.user_group_type = m.get('UserGroupType')
        return self


class ListPolicesForPrivateAccessApplicationResponseBodyApplications(TeaModel):
    def __init__(
        self,
        application_id: str = None,
        policies: List[ListPolicesForPrivateAccessApplicationResponseBodyApplicationsPolicies] = None,
    ):
        self.application_id = application_id
        self.policies = policies

    def validate(self):
        if self.policies:
            for k in self.policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        result['Policies'] = []
        if self.policies is not None:
            for k in self.policies:
                result['Policies'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        self.policies = []
        if m.get('Policies') is not None:
            for k in m.get('Policies'):
                temp_model = ListPolicesForPrivateAccessApplicationResponseBodyApplicationsPolicies()
                self.policies.append(temp_model.from_map(k))
        return self


class ListPolicesForPrivateAccessApplicationResponseBody(TeaModel):
    def __init__(
        self,
        applications: List[ListPolicesForPrivateAccessApplicationResponseBodyApplications] = None,
        request_id: str = None,
    ):
        self.applications = applications
        self.request_id = request_id

    def validate(self):
        if self.applications:
            for k in self.applications:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Applications'] = []
        if self.applications is not None:
            for k in self.applications:
                result['Applications'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.applications = []
        if m.get('Applications') is not None:
            for k in m.get('Applications'):
                temp_model = ListPolicesForPrivateAccessApplicationResponseBodyApplications()
                self.applications.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListPolicesForPrivateAccessApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPolicesForPrivateAccessApplicationResponseBody = None,
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
            temp_model = ListPolicesForPrivateAccessApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPolicesForPrivateAccessTagRequest(TeaModel):
    def __init__(
        self,
        tag_ids: List[str] = None,
    ):
        # This parameter is required.
        self.tag_ids = tag_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_ids is not None:
            result['TagIds'] = self.tag_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagIds') is not None:
            self.tag_ids = m.get('TagIds')
        return self


class ListPolicesForPrivateAccessTagResponseBodyTagsPolicesCustomUserAttributes(TeaModel):
    def __init__(
        self,
        idp_id: int = None,
        relation: str = None,
        user_group_type: str = None,
        value: str = None,
    ):
        # 用户组的身份源ID。当自定义用户组类型为**department**时，存在该值。
        self.idp_id = idp_id
        # 用户组的关系。取值：
        # - **Equal**：等于。
        # - **Unequal**：不等于。
        self.relation = relation
        # 用户组的类型。取值：
        # - **username**：用户名。
        # - **department**：部门。
        # - **email**：邮箱。
        # - **telephone**：手机。
        self.user_group_type = user_group_type
        # 用户组属性的值。
        # - 当用户组类型为**username**时，表示用户名的值。长度为1~128个字符，支持中文和大小写英文字母，可包含数字、半角句号（.）、下划线（_）和短划线（-）。
        # - 当用户组类型为**department**时，表示部门的值。如：OU=部门1,OU=SASE钉钉。
        # - 当用户组类型为**email**时，表示邮箱的值。如：username@example.com。
        # - 当用户组类型为**telephone**时，表示手机的值。如：13900001234。
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.idp_id is not None:
            result['IdpId'] = self.idp_id
        if self.relation is not None:
            result['Relation'] = self.relation
        if self.user_group_type is not None:
            result['UserGroupType'] = self.user_group_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdpId') is not None:
            self.idp_id = m.get('IdpId')
        if m.get('Relation') is not None:
            self.relation = m.get('Relation')
        if m.get('UserGroupType') is not None:
            self.user_group_type = m.get('UserGroupType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListPolicesForPrivateAccessTagResponseBodyTagsPolices(TeaModel):
    def __init__(
        self,
        application_type: str = None,
        create_time: str = None,
        custom_user_attributes: List[ListPolicesForPrivateAccessTagResponseBodyTagsPolicesCustomUserAttributes] = None,
        description: str = None,
        name: str = None,
        policy_action: str = None,
        policy_id: str = None,
        priority: int = None,
        status: str = None,
        user_group_type: str = None,
    ):
        self.application_type = application_type
        # 内网访问策略创建时间。
        self.create_time = create_time
        # 自定义用户组属性集合。多个自定义用户组属性之间是或的关系，按照合集生效。
        self.custom_user_attributes = custom_user_attributes
        self.description = description
        self.name = name
        self.policy_action = policy_action
        self.policy_id = policy_id
        self.priority = priority
        self.status = status
        self.user_group_type = user_group_type

    def validate(self):
        if self.custom_user_attributes:
            for k in self.custom_user_attributes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_type is not None:
            result['ApplicationType'] = self.application_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        result['CustomUserAttributes'] = []
        if self.custom_user_attributes is not None:
            for k in self.custom_user_attributes:
                result['CustomUserAttributes'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.policy_action is not None:
            result['PolicyAction'] = self.policy_action
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.status is not None:
            result['Status'] = self.status
        if self.user_group_type is not None:
            result['UserGroupType'] = self.user_group_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        self.custom_user_attributes = []
        if m.get('CustomUserAttributes') is not None:
            for k in m.get('CustomUserAttributes'):
                temp_model = ListPolicesForPrivateAccessTagResponseBodyTagsPolicesCustomUserAttributes()
                self.custom_user_attributes.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PolicyAction') is not None:
            self.policy_action = m.get('PolicyAction')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserGroupType') is not None:
            self.user_group_type = m.get('UserGroupType')
        return self


class ListPolicesForPrivateAccessTagResponseBodyTags(TeaModel):
    def __init__(
        self,
        polices: List[ListPolicesForPrivateAccessTagResponseBodyTagsPolices] = None,
        tag_id: str = None,
    ):
        self.polices = polices
        self.tag_id = tag_id

    def validate(self):
        if self.polices:
            for k in self.polices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Polices'] = []
        if self.polices is not None:
            for k in self.polices:
                result['Polices'].append(k.to_map() if k else None)
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.polices = []
        if m.get('Polices') is not None:
            for k in m.get('Polices'):
                temp_model = ListPolicesForPrivateAccessTagResponseBodyTagsPolices()
                self.polices.append(temp_model.from_map(k))
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        return self


class ListPolicesForPrivateAccessTagResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tags: List[ListPolicesForPrivateAccessTagResponseBodyTags] = None,
    ):
        self.request_id = request_id
        self.tags = tags

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListPolicesForPrivateAccessTagResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListPolicesForPrivateAccessTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPolicesForPrivateAccessTagResponseBody = None,
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
            temp_model = ListPolicesForPrivateAccessTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPolicesForUserGroupRequest(TeaModel):
    def __init__(
        self,
        user_group_ids: List[str] = None,
    ):
        # This parameter is required.
        self.user_group_ids = user_group_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')
        return self


class ListPolicesForUserGroupResponseBodyUserGroupsPolices(TeaModel):
    def __init__(
        self,
        name: str = None,
        policy_id: str = None,
        policy_type: str = None,
    ):
        self.name = name
        self.policy_id = policy_id
        self.policy_type = policy_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        return self


class ListPolicesForUserGroupResponseBodyUserGroups(TeaModel):
    def __init__(
        self,
        polices: List[ListPolicesForUserGroupResponseBodyUserGroupsPolices] = None,
        user_group_id: str = None,
    ):
        self.polices = polices
        self.user_group_id = user_group_id

    def validate(self):
        if self.polices:
            for k in self.polices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Polices'] = []
        if self.polices is not None:
            for k in self.polices:
                result['Polices'].append(k.to_map() if k else None)
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.polices = []
        if m.get('Polices') is not None:
            for k in m.get('Polices'):
                temp_model = ListPolicesForUserGroupResponseBodyUserGroupsPolices()
                self.polices.append(temp_model.from_map(k))
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class ListPolicesForUserGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        user_groups: List[ListPolicesForUserGroupResponseBodyUserGroups] = None,
    ):
        self.request_id = request_id
        self.user_groups = user_groups

    def validate(self):
        if self.user_groups:
            for k in self.user_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['UserGroups'] = []
        if self.user_groups is not None:
            for k in self.user_groups:
                result['UserGroups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.user_groups = []
        if m.get('UserGroups') is not None:
            for k in m.get('UserGroups'):
                temp_model = ListPolicesForUserGroupResponseBodyUserGroups()
                self.user_groups.append(temp_model.from_map(k))
        return self


class ListPolicesForUserGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPolicesForUserGroupResponseBody = None,
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
            temp_model = ListPolicesForUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPopTrafficStatisticsRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        region: str = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.region = region
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.region is not None:
            result['Region'] = self.region
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListPopTrafficStatisticsResponseBodyTrafficDataDatapoints(TeaModel):
    def __init__(
        self,
        average: float = None,
        date_time: str = None,
    ):
        self.average = average
        self.date_time = date_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.average is not None:
            result['Average'] = self.average
        if self.date_time is not None:
            result['DateTime'] = self.date_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Average') is not None:
            self.average = m.get('Average')
        if m.get('DateTime') is not None:
            self.date_time = m.get('DateTime')
        return self


class ListPopTrafficStatisticsResponseBodyTrafficData(TeaModel):
    def __init__(
        self,
        datapoints: List[ListPopTrafficStatisticsResponseBodyTrafficDataDatapoints] = None,
        metric_name: str = None,
    ):
        self.datapoints = datapoints
        self.metric_name = metric_name

    def validate(self):
        if self.datapoints:
            for k in self.datapoints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Datapoints'] = []
        if self.datapoints is not None:
            for k in self.datapoints:
                result['Datapoints'].append(k.to_map() if k else None)
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.datapoints = []
        if m.get('Datapoints') is not None:
            for k in m.get('Datapoints'):
                temp_model = ListPopTrafficStatisticsResponseBodyTrafficDataDatapoints()
                self.datapoints.append(temp_model.from_map(k))
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        return self


class ListPopTrafficStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        traffic_data: List[ListPopTrafficStatisticsResponseBodyTrafficData] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.traffic_data = traffic_data

    def validate(self):
        if self.traffic_data:
            for k in self.traffic_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TrafficData'] = []
        if self.traffic_data is not None:
            for k in self.traffic_data:
                result['TrafficData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.traffic_data = []
        if m.get('TrafficData') is not None:
            for k in m.get('TrafficData'):
                temp_model = ListPopTrafficStatisticsResponseBodyTrafficData()
                self.traffic_data.append(temp_model.from_map(k))
        return self


class ListPopTrafficStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPopTrafficStatisticsResponseBody = None,
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
            temp_model = ListPopTrafficStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPrivateAccessApplicationsRequest(TeaModel):
    def __init__(
        self,
        access_modes: str = None,
        address: str = None,
        application_ids: List[str] = None,
        connector_id: str = None,
        current_page: int = None,
        name: str = None,
        page_size: int = None,
        policy_id: str = None,
        status: str = None,
        tag_id: str = None,
    ):
        self.access_modes = access_modes
        self.address = address
        self.application_ids = application_ids
        self.connector_id = connector_id
        # This parameter is required.
        self.current_page = current_page
        self.name = name
        # This parameter is required.
        self.page_size = page_size
        self.policy_id = policy_id
        self.status = status
        self.tag_id = tag_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_modes is not None:
            result['AccessModes'] = self.access_modes
        if self.address is not None:
            result['Address'] = self.address
        if self.application_ids is not None:
            result['ApplicationIds'] = self.application_ids
        if self.connector_id is not None:
            result['ConnectorId'] = self.connector_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.name is not None:
            result['Name'] = self.name
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.status is not None:
            result['Status'] = self.status
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessModes') is not None:
            self.access_modes = m.get('AccessModes')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('ApplicationIds') is not None:
            self.application_ids = m.get('ApplicationIds')
        if m.get('ConnectorId') is not None:
            self.connector_id = m.get('ConnectorId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        return self


class ListPrivateAccessApplicationsResponseBodyApplicationsPortRanges(TeaModel):
    def __init__(
        self,
        begin: int = None,
        end: int = None,
    ):
        self.begin = begin
        self.end = end

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.end is not None:
            result['End'] = self.end
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('End') is not None:
            self.end = m.get('End')
        return self


class ListPrivateAccessApplicationsResponseBodyApplications(TeaModel):
    def __init__(
        self,
        addresses: List[str] = None,
        application_id: str = None,
        browser_access_status: str = None,
        connector_ids: List[str] = None,
        create_time: str = None,
        description: str = None,
        l_7proxy_domain_automatic: str = None,
        l_7proxy_domain_custom: str = None,
        name: str = None,
        policy_ids: List[str] = None,
        port_ranges: List[ListPrivateAccessApplicationsResponseBodyApplicationsPortRanges] = None,
        protocol: str = None,
        status: str = None,
        tag_ids: List[str] = None,
    ):
        self.addresses = addresses
        self.application_id = application_id
        self.browser_access_status = browser_access_status
        self.connector_ids = connector_ids
        self.create_time = create_time
        self.description = description
        self.l_7proxy_domain_automatic = l_7proxy_domain_automatic
        self.l_7proxy_domain_custom = l_7proxy_domain_custom
        self.name = name
        self.policy_ids = policy_ids
        self.port_ranges = port_ranges
        self.protocol = protocol
        self.status = status
        self.tag_ids = tag_ids

    def validate(self):
        if self.port_ranges:
            for k in self.port_ranges:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.addresses is not None:
            result['Addresses'] = self.addresses
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.browser_access_status is not None:
            result['BrowserAccessStatus'] = self.browser_access_status
        if self.connector_ids is not None:
            result['ConnectorIds'] = self.connector_ids
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.l_7proxy_domain_automatic is not None:
            result['L7ProxyDomainAutomatic'] = self.l_7proxy_domain_automatic
        if self.l_7proxy_domain_custom is not None:
            result['L7ProxyDomainCustom'] = self.l_7proxy_domain_custom
        if self.name is not None:
            result['Name'] = self.name
        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids
        result['PortRanges'] = []
        if self.port_ranges is not None:
            for k in self.port_ranges:
                result['PortRanges'].append(k.to_map() if k else None)
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.status is not None:
            result['Status'] = self.status
        if self.tag_ids is not None:
            result['TagIds'] = self.tag_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Addresses') is not None:
            self.addresses = m.get('Addresses')
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('BrowserAccessStatus') is not None:
            self.browser_access_status = m.get('BrowserAccessStatus')
        if m.get('ConnectorIds') is not None:
            self.connector_ids = m.get('ConnectorIds')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('L7ProxyDomainAutomatic') is not None:
            self.l_7proxy_domain_automatic = m.get('L7ProxyDomainAutomatic')
        if m.get('L7ProxyDomainCustom') is not None:
            self.l_7proxy_domain_custom = m.get('L7ProxyDomainCustom')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')
        self.port_ranges = []
        if m.get('PortRanges') is not None:
            for k in m.get('PortRanges'):
                temp_model = ListPrivateAccessApplicationsResponseBodyApplicationsPortRanges()
                self.port_ranges.append(temp_model.from_map(k))
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TagIds') is not None:
            self.tag_ids = m.get('TagIds')
        return self


class ListPrivateAccessApplicationsResponseBody(TeaModel):
    def __init__(
        self,
        applications: List[ListPrivateAccessApplicationsResponseBodyApplications] = None,
        request_id: str = None,
        total_num: int = None,
    ):
        self.applications = applications
        self.request_id = request_id
        self.total_num = total_num

    def validate(self):
        if self.applications:
            for k in self.applications:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Applications'] = []
        if self.applications is not None:
            for k in self.applications:
                result['Applications'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.applications = []
        if m.get('Applications') is not None:
            for k in m.get('Applications'):
                temp_model = ListPrivateAccessApplicationsResponseBodyApplications()
                self.applications.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class ListPrivateAccessApplicationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPrivateAccessApplicationsResponseBody = None,
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
            temp_model = ListPrivateAccessApplicationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPrivateAccessApplicationsForDynamicRouteRequest(TeaModel):
    def __init__(
        self,
        dynamic_route_ids: List[str] = None,
    ):
        # This parameter is required.
        self.dynamic_route_ids = dynamic_route_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dynamic_route_ids is not None:
            result['DynamicRouteIds'] = self.dynamic_route_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DynamicRouteIds') is not None:
            self.dynamic_route_ids = m.get('DynamicRouteIds')
        return self


class ListPrivateAccessApplicationsForDynamicRouteResponseBodyDynamicRoutesApplicationsPortRanges(TeaModel):
    def __init__(
        self,
        begin: int = None,
        end: int = None,
    ):
        self.begin = begin
        self.end = end

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.end is not None:
            result['End'] = self.end
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('End') is not None:
            self.end = m.get('End')
        return self


class ListPrivateAccessApplicationsForDynamicRouteResponseBodyDynamicRoutesApplications(TeaModel):
    def __init__(
        self,
        addresses: List[str] = None,
        application_id: str = None,
        create_time: str = None,
        description: str = None,
        name: str = None,
        port_ranges: List[ListPrivateAccessApplicationsForDynamicRouteResponseBodyDynamicRoutesApplicationsPortRanges] = None,
        protocol: str = None,
        status: str = None,
    ):
        self.addresses = addresses
        self.application_id = application_id
        self.create_time = create_time
        self.description = description
        self.name = name
        self.port_ranges = port_ranges
        self.protocol = protocol
        self.status = status

    def validate(self):
        if self.port_ranges:
            for k in self.port_ranges:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.addresses is not None:
            result['Addresses'] = self.addresses
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        result['PortRanges'] = []
        if self.port_ranges is not None:
            for k in self.port_ranges:
                result['PortRanges'].append(k.to_map() if k else None)
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Addresses') is not None:
            self.addresses = m.get('Addresses')
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.port_ranges = []
        if m.get('PortRanges') is not None:
            for k in m.get('PortRanges'):
                temp_model = ListPrivateAccessApplicationsForDynamicRouteResponseBodyDynamicRoutesApplicationsPortRanges()
                self.port_ranges.append(temp_model.from_map(k))
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListPrivateAccessApplicationsForDynamicRouteResponseBodyDynamicRoutes(TeaModel):
    def __init__(
        self,
        applications: List[ListPrivateAccessApplicationsForDynamicRouteResponseBodyDynamicRoutesApplications] = None,
        dynamic_route_id: str = None,
    ):
        self.applications = applications
        self.dynamic_route_id = dynamic_route_id

    def validate(self):
        if self.applications:
            for k in self.applications:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Applications'] = []
        if self.applications is not None:
            for k in self.applications:
                result['Applications'].append(k.to_map() if k else None)
        if self.dynamic_route_id is not None:
            result['DynamicRouteId'] = self.dynamic_route_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.applications = []
        if m.get('Applications') is not None:
            for k in m.get('Applications'):
                temp_model = ListPrivateAccessApplicationsForDynamicRouteResponseBodyDynamicRoutesApplications()
                self.applications.append(temp_model.from_map(k))
        if m.get('DynamicRouteId') is not None:
            self.dynamic_route_id = m.get('DynamicRouteId')
        return self


class ListPrivateAccessApplicationsForDynamicRouteResponseBody(TeaModel):
    def __init__(
        self,
        dynamic_routes: List[ListPrivateAccessApplicationsForDynamicRouteResponseBodyDynamicRoutes] = None,
        request_id: str = None,
    ):
        self.dynamic_routes = dynamic_routes
        self.request_id = request_id

    def validate(self):
        if self.dynamic_routes:
            for k in self.dynamic_routes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DynamicRoutes'] = []
        if self.dynamic_routes is not None:
            for k in self.dynamic_routes:
                result['DynamicRoutes'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dynamic_routes = []
        if m.get('DynamicRoutes') is not None:
            for k in m.get('DynamicRoutes'):
                temp_model = ListPrivateAccessApplicationsForDynamicRouteResponseBodyDynamicRoutes()
                self.dynamic_routes.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListPrivateAccessApplicationsForDynamicRouteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPrivateAccessApplicationsForDynamicRouteResponseBody = None,
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
            temp_model = ListPrivateAccessApplicationsForDynamicRouteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPrivateAccessPolicesRequest(TeaModel):
    def __init__(
        self,
        application_id: str = None,
        application_name: str = None,
        current_page: int = None,
        name: str = None,
        page_size: int = None,
        policy_action: str = None,
        policy_ids: List[str] = None,
        status: str = None,
        tag_id: str = None,
        tag_name: str = None,
        user_group_id: str = None,
    ):
        self.application_id = application_id
        self.application_name = application_name
        # This parameter is required.
        self.current_page = current_page
        self.name = name
        # This parameter is required.
        self.page_size = page_size
        self.policy_action = policy_action
        self.policy_ids = policy_ids
        self.status = status
        self.tag_id = tag_id
        self.tag_name = tag_name
        # 用户组ID。取值来源：
        # - [ListUserGroups](~~ListUserGroups~~)：批量查询用户组。
        # - [CreateUserGroup](~~CreateUserGroup~~)：创建用户组。
        self.user_group_id = user_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.name is not None:
            result['Name'] = self.name
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.policy_action is not None:
            result['PolicyAction'] = self.policy_action
        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids
        if self.status is not None:
            result['Status'] = self.status
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PolicyAction') is not None:
            self.policy_action = m.get('PolicyAction')
        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class ListPrivateAccessPolicesResponseBodyPolicesCustomUserAttributes(TeaModel):
    def __init__(
        self,
        idp_id: int = None,
        relation: str = None,
        user_group_type: str = None,
        value: str = None,
    ):
        self.idp_id = idp_id
        self.relation = relation
        self.user_group_type = user_group_type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.idp_id is not None:
            result['IdpId'] = self.idp_id
        if self.relation is not None:
            result['Relation'] = self.relation
        if self.user_group_type is not None:
            result['UserGroupType'] = self.user_group_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdpId') is not None:
            self.idp_id = m.get('IdpId')
        if m.get('Relation') is not None:
            self.relation = m.get('Relation')
        if m.get('UserGroupType') is not None:
            self.user_group_type = m.get('UserGroupType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListPrivateAccessPolicesResponseBodyPolices(TeaModel):
    def __init__(
        self,
        application_ids: List[str] = None,
        application_type: str = None,
        create_time: str = None,
        custom_user_attributes: List[ListPrivateAccessPolicesResponseBodyPolicesCustomUserAttributes] = None,
        description: str = None,
        device_attribute_action: str = None,
        device_attribute_id: str = None,
        name: str = None,
        policy_action: str = None,
        policy_id: str = None,
        priority: int = None,
        status: str = None,
        tag_ids: List[str] = None,
        user_group_ids: List[str] = None,
        user_group_mode: str = None,
    ):
        self.application_ids = application_ids
        self.application_type = application_type
        self.create_time = create_time
        self.custom_user_attributes = custom_user_attributes
        self.description = description
        self.device_attribute_action = device_attribute_action
        self.device_attribute_id = device_attribute_id
        self.name = name
        self.policy_action = policy_action
        self.policy_id = policy_id
        self.priority = priority
        self.status = status
        self.tag_ids = tag_ids
        self.user_group_ids = user_group_ids
        self.user_group_mode = user_group_mode

    def validate(self):
        if self.custom_user_attributes:
            for k in self.custom_user_attributes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_ids is not None:
            result['ApplicationIds'] = self.application_ids
        if self.application_type is not None:
            result['ApplicationType'] = self.application_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        result['CustomUserAttributes'] = []
        if self.custom_user_attributes is not None:
            for k in self.custom_user_attributes:
                result['CustomUserAttributes'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.device_attribute_action is not None:
            result['DeviceAttributeAction'] = self.device_attribute_action
        if self.device_attribute_id is not None:
            result['DeviceAttributeId'] = self.device_attribute_id
        if self.name is not None:
            result['Name'] = self.name
        if self.policy_action is not None:
            result['PolicyAction'] = self.policy_action
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.status is not None:
            result['Status'] = self.status
        if self.tag_ids is not None:
            result['TagIds'] = self.tag_ids
        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids
        if self.user_group_mode is not None:
            result['UserGroupMode'] = self.user_group_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationIds') is not None:
            self.application_ids = m.get('ApplicationIds')
        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        self.custom_user_attributes = []
        if m.get('CustomUserAttributes') is not None:
            for k in m.get('CustomUserAttributes'):
                temp_model = ListPrivateAccessPolicesResponseBodyPolicesCustomUserAttributes()
                self.custom_user_attributes.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DeviceAttributeAction') is not None:
            self.device_attribute_action = m.get('DeviceAttributeAction')
        if m.get('DeviceAttributeId') is not None:
            self.device_attribute_id = m.get('DeviceAttributeId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PolicyAction') is not None:
            self.policy_action = m.get('PolicyAction')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TagIds') is not None:
            self.tag_ids = m.get('TagIds')
        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')
        if m.get('UserGroupMode') is not None:
            self.user_group_mode = m.get('UserGroupMode')
        return self


class ListPrivateAccessPolicesResponseBody(TeaModel):
    def __init__(
        self,
        polices: List[ListPrivateAccessPolicesResponseBodyPolices] = None,
        request_id: str = None,
        total_num: int = None,
    ):
        self.polices = polices
        self.request_id = request_id
        self.total_num = total_num

    def validate(self):
        if self.polices:
            for k in self.polices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Polices'] = []
        if self.polices is not None:
            for k in self.polices:
                result['Polices'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.polices = []
        if m.get('Polices') is not None:
            for k in m.get('Polices'):
                temp_model = ListPrivateAccessPolicesResponseBodyPolices()
                self.polices.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class ListPrivateAccessPolicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPrivateAccessPolicesResponseBody = None,
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
            temp_model = ListPrivateAccessPolicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPrivateAccessTagsRequest(TeaModel):
    def __init__(
        self,
        application_id: str = None,
        current_page: int = None,
        name: str = None,
        page_size: int = None,
        policy_id: str = None,
        simple_mode: bool = None,
        tag_ids: List[str] = None,
    ):
        # The ID of the internal access application. You can obtain the application ID by calling the following operations:
        # 
        # *   [ListPrivateAccessApplications](~~ListPrivateAccessApplications~~): queries all internal access applications.
        # *   [CreatePrivateAccessApplication](~~CreatePrivateAccessApplication~~): creates an internal access application.
        self.application_id = application_id
        # The page number. Valid values: 1 to 10000.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The name of the internal access tag. The name must be 1 to 128 characters in length and can contain letters, digits, periods (.), underscores (_), and hyphens (-).
        self.name = name
        # The number of entries per page. Valid values: 1 to 1000.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The ID of the internal access policy. You can obtain the policy ID by calling the following operations:
        # 
        # *   [ListPrivateAccessPolices](~~ListPrivateAccessPolices~~): queries all internal access policies.
        # *   [CreatePrivateAccessPolicy](~~CreatePrivateAccessPolicy~~): creates an internal access policy.
        self.policy_id = policy_id
        # Specifies whether to enable the simple query mode. A value of true specifies that policy IDs are not queried.
        self.simple_mode = simple_mode
        # The IDs of internal access tags. You can specify up to 100 tag IDs.
        self.tag_ids = tag_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.name is not None:
            result['Name'] = self.name
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.simple_mode is not None:
            result['SimpleMode'] = self.simple_mode
        if self.tag_ids is not None:
            result['TagIds'] = self.tag_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('SimpleMode') is not None:
            self.simple_mode = m.get('SimpleMode')
        if m.get('TagIds') is not None:
            self.tag_ids = m.get('TagIds')
        return self


class ListPrivateAccessTagsResponseBodyTags(TeaModel):
    def __init__(
        self,
        application_ids: List[str] = None,
        create_time: str = None,
        description: str = None,
        name: str = None,
        policy_ids: List[str] = None,
        tag_id: str = None,
        tag_type: str = None,
    ):
        # The IDs of the internal access applications.
        self.application_ids = application_ids
        # The time when the internal access tag was created.
        self.create_time = create_time
        # The description of the internal access tag.
        self.description = description
        # The name of the internal access tag.
        self.name = name
        # The IDs of the internal access policies.
        self.policy_ids = policy_ids
        # The ID of the internal access tag.
        self.tag_id = tag_id
        # The type of the internal access tag. Valid values:
        # 
        # *   **Default**\
        # *   **Custom**\
        self.tag_type = tag_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_ids is not None:
            result['ApplicationIds'] = self.application_ids
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        if self.tag_type is not None:
            result['TagType'] = self.tag_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationIds') is not None:
            self.application_ids = m.get('ApplicationIds')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        if m.get('TagType') is not None:
            self.tag_type = m.get('TagType')
        return self


class ListPrivateAccessTagsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tags: List[ListPrivateAccessTagsResponseBodyTags] = None,
        total_num: int = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The internal access tags.
        self.tags = tags
        # The total number of internal access tags.
        self.total_num = total_num

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListPrivateAccessTagsResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class ListPrivateAccessTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPrivateAccessTagsResponseBody = None,
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
            temp_model = ListPrivateAccessTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPrivateAccessTagsForDynamicRouteRequest(TeaModel):
    def __init__(
        self,
        dynamic_route_ids: List[str] = None,
    ):
        # This parameter is required.
        self.dynamic_route_ids = dynamic_route_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dynamic_route_ids is not None:
            result['DynamicRouteIds'] = self.dynamic_route_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DynamicRouteIds') is not None:
            self.dynamic_route_ids = m.get('DynamicRouteIds')
        return self


class ListPrivateAccessTagsForDynamicRouteResponseBodyDynamicRoutesTags(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        name: str = None,
        tag_id: str = None,
        tag_type: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.name = name
        self.tag_id = tag_id
        self.tag_type = tag_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        if self.tag_type is not None:
            result['TagType'] = self.tag_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        if m.get('TagType') is not None:
            self.tag_type = m.get('TagType')
        return self


class ListPrivateAccessTagsForDynamicRouteResponseBodyDynamicRoutes(TeaModel):
    def __init__(
        self,
        dynamic_route_id: str = None,
        tags: List[ListPrivateAccessTagsForDynamicRouteResponseBodyDynamicRoutesTags] = None,
    ):
        self.dynamic_route_id = dynamic_route_id
        self.tags = tags

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
        if self.dynamic_route_id is not None:
            result['DynamicRouteId'] = self.dynamic_route_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DynamicRouteId') is not None:
            self.dynamic_route_id = m.get('DynamicRouteId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListPrivateAccessTagsForDynamicRouteResponseBodyDynamicRoutesTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListPrivateAccessTagsForDynamicRouteResponseBody(TeaModel):
    def __init__(
        self,
        dynamic_routes: List[ListPrivateAccessTagsForDynamicRouteResponseBodyDynamicRoutes] = None,
        request_id: str = None,
    ):
        self.dynamic_routes = dynamic_routes
        self.request_id = request_id

    def validate(self):
        if self.dynamic_routes:
            for k in self.dynamic_routes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DynamicRoutes'] = []
        if self.dynamic_routes is not None:
            for k in self.dynamic_routes:
                result['DynamicRoutes'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dynamic_routes = []
        if m.get('DynamicRoutes') is not None:
            for k in m.get('DynamicRoutes'):
                temp_model = ListPrivateAccessTagsForDynamicRouteResponseBodyDynamicRoutes()
                self.dynamic_routes.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListPrivateAccessTagsForDynamicRouteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPrivateAccessTagsForDynamicRouteResponseBody = None,
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
            temp_model = ListPrivateAccessTagsForDynamicRouteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRegistrationPoliciesRequest(TeaModel):
    def __init__(
        self,
        company_limit_type: str = None,
        current_page: int = None,
        match_mode: str = None,
        name: str = None,
        page_size: int = None,
        personal_limit_type: str = None,
        policy_ids: List[str] = None,
        status: str = None,
        user_group_id: str = None,
    ):
        self.company_limit_type = company_limit_type
        # This parameter is required.
        self.current_page = current_page
        self.match_mode = match_mode
        self.name = name
        # This parameter is required.
        self.page_size = page_size
        self.personal_limit_type = personal_limit_type
        self.policy_ids = policy_ids
        self.status = status
        self.user_group_id = user_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.company_limit_type is not None:
            result['CompanyLimitType'] = self.company_limit_type
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.match_mode is not None:
            result['MatchMode'] = self.match_mode
        if self.name is not None:
            result['Name'] = self.name
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.personal_limit_type is not None:
            result['PersonalLimitType'] = self.personal_limit_type
        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids
        if self.status is not None:
            result['Status'] = self.status
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompanyLimitType') is not None:
            self.company_limit_type = m.get('CompanyLimitType')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('MatchMode') is not None:
            self.match_mode = m.get('MatchMode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PersonalLimitType') is not None:
            self.personal_limit_type = m.get('PersonalLimitType')
        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class ListRegistrationPoliciesResponseBodyPoliciesLimitDetailLimitCount(TeaModel):
    def __init__(
        self,
        all: int = None,
        mobile: int = None,
        pc: int = None,
    ):
        self.all = all
        self.mobile = mobile
        self.pc = pc

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.pc is not None:
            result['PC'] = self.pc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('PC') is not None:
            self.pc = m.get('PC')
        return self


class ListRegistrationPoliciesResponseBodyPoliciesLimitDetail(TeaModel):
    def __init__(
        self,
        device_belong: str = None,
        limit_count: ListRegistrationPoliciesResponseBodyPoliciesLimitDetailLimitCount = None,
        limit_type: str = None,
    ):
        self.device_belong = device_belong
        self.limit_count = limit_count
        self.limit_type = limit_type

    def validate(self):
        if self.limit_count:
            self.limit_count.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_belong is not None:
            result['DeviceBelong'] = self.device_belong
        if self.limit_count is not None:
            result['LimitCount'] = self.limit_count.to_map()
        if self.limit_type is not None:
            result['LimitType'] = self.limit_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceBelong') is not None:
            self.device_belong = m.get('DeviceBelong')
        if m.get('LimitCount') is not None:
            temp_model = ListRegistrationPoliciesResponseBodyPoliciesLimitDetailLimitCount()
            self.limit_count = temp_model.from_map(m['LimitCount'])
        if m.get('LimitType') is not None:
            self.limit_type = m.get('LimitType')
        return self


class ListRegistrationPoliciesResponseBodyPolicies(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        limit_detail: List[ListRegistrationPoliciesResponseBodyPoliciesLimitDetail] = None,
        match_mode: str = None,
        name: str = None,
        policy_id: str = None,
        priority: int = None,
        status: str = None,
        user_group_ids: List[str] = None,
        whitelist: List[str] = None,
    ):
        self.create_time = create_time
        self.description = description
        self.limit_detail = limit_detail
        self.match_mode = match_mode
        self.name = name
        self.policy_id = policy_id
        self.priority = priority
        self.status = status
        self.user_group_ids = user_group_ids
        self.whitelist = whitelist

    def validate(self):
        if self.limit_detail:
            for k in self.limit_detail:
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
        result['LimitDetail'] = []
        if self.limit_detail is not None:
            for k in self.limit_detail:
                result['LimitDetail'].append(k.to_map() if k else None)
        if self.match_mode is not None:
            result['MatchMode'] = self.match_mode
        if self.name is not None:
            result['Name'] = self.name
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.status is not None:
            result['Status'] = self.status
        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids
        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.limit_detail = []
        if m.get('LimitDetail') is not None:
            for k in m.get('LimitDetail'):
                temp_model = ListRegistrationPoliciesResponseBodyPoliciesLimitDetail()
                self.limit_detail.append(temp_model.from_map(k))
        if m.get('MatchMode') is not None:
            self.match_mode = m.get('MatchMode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')
        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')
        return self


class ListRegistrationPoliciesResponseBody(TeaModel):
    def __init__(
        self,
        policies: List[ListRegistrationPoliciesResponseBodyPolicies] = None,
        request_id: str = None,
        total_num: str = None,
    ):
        self.policies = policies
        self.request_id = request_id
        self.total_num = total_num

    def validate(self):
        if self.policies:
            for k in self.policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Policies'] = []
        if self.policies is not None:
            for k in self.policies:
                result['Policies'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.policies = []
        if m.get('Policies') is not None:
            for k in m.get('Policies'):
                temp_model = ListRegistrationPoliciesResponseBodyPolicies()
                self.policies.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class ListRegistrationPoliciesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRegistrationPoliciesResponseBody = None,
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
            temp_model = ListRegistrationPoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRegistrationPoliciesForUserGroupRequest(TeaModel):
    def __init__(
        self,
        user_group_ids: List[str] = None,
    ):
        # This parameter is required.
        self.user_group_ids = user_group_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')
        return self


class ListRegistrationPoliciesForUserGroupResponseBodyUserGroupsPoliciesLimitDetailLimitCount(TeaModel):
    def __init__(
        self,
        all: str = None,
        mobile: str = None,
        pc: str = None,
    ):
        self.all = all
        self.mobile = mobile
        self.pc = pc

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.pc is not None:
            result['PC'] = self.pc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('PC') is not None:
            self.pc = m.get('PC')
        return self


class ListRegistrationPoliciesForUserGroupResponseBodyUserGroupsPoliciesLimitDetail(TeaModel):
    def __init__(
        self,
        device_belong: str = None,
        limit_count: ListRegistrationPoliciesForUserGroupResponseBodyUserGroupsPoliciesLimitDetailLimitCount = None,
        limit_type: str = None,
    ):
        self.device_belong = device_belong
        self.limit_count = limit_count
        self.limit_type = limit_type

    def validate(self):
        if self.limit_count:
            self.limit_count.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_belong is not None:
            result['DeviceBelong'] = self.device_belong
        if self.limit_count is not None:
            result['LimitCount'] = self.limit_count.to_map()
        if self.limit_type is not None:
            result['LimitType'] = self.limit_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceBelong') is not None:
            self.device_belong = m.get('DeviceBelong')
        if m.get('LimitCount') is not None:
            temp_model = ListRegistrationPoliciesForUserGroupResponseBodyUserGroupsPoliciesLimitDetailLimitCount()
            self.limit_count = temp_model.from_map(m['LimitCount'])
        if m.get('LimitType') is not None:
            self.limit_type = m.get('LimitType')
        return self


class ListRegistrationPoliciesForUserGroupResponseBodyUserGroupsPolicies(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        limit_detail: List[ListRegistrationPoliciesForUserGroupResponseBodyUserGroupsPoliciesLimitDetail] = None,
        match_mode: str = None,
        name: str = None,
        policy_id: str = None,
        priority: int = None,
        status: str = None,
        whitelist: List[str] = None,
    ):
        self.create_time = create_time
        self.description = description
        self.limit_detail = limit_detail
        self.match_mode = match_mode
        self.name = name
        self.policy_id = policy_id
        self.priority = priority
        self.status = status
        self.whitelist = whitelist

    def validate(self):
        if self.limit_detail:
            for k in self.limit_detail:
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
        result['LimitDetail'] = []
        if self.limit_detail is not None:
            for k in self.limit_detail:
                result['LimitDetail'].append(k.to_map() if k else None)
        if self.match_mode is not None:
            result['MatchMode'] = self.match_mode
        if self.name is not None:
            result['Name'] = self.name
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.status is not None:
            result['Status'] = self.status
        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.limit_detail = []
        if m.get('LimitDetail') is not None:
            for k in m.get('LimitDetail'):
                temp_model = ListRegistrationPoliciesForUserGroupResponseBodyUserGroupsPoliciesLimitDetail()
                self.limit_detail.append(temp_model.from_map(k))
        if m.get('MatchMode') is not None:
            self.match_mode = m.get('MatchMode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')
        return self


class ListRegistrationPoliciesForUserGroupResponseBodyUserGroups(TeaModel):
    def __init__(
        self,
        policies: List[ListRegistrationPoliciesForUserGroupResponseBodyUserGroupsPolicies] = None,
        user_group_id: str = None,
    ):
        self.policies = policies
        self.user_group_id = user_group_id

    def validate(self):
        if self.policies:
            for k in self.policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Policies'] = []
        if self.policies is not None:
            for k in self.policies:
                result['Policies'].append(k.to_map() if k else None)
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.policies = []
        if m.get('Policies') is not None:
            for k in m.get('Policies'):
                temp_model = ListRegistrationPoliciesForUserGroupResponseBodyUserGroupsPolicies()
                self.policies.append(temp_model.from_map(k))
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class ListRegistrationPoliciesForUserGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        user_groups: List[ListRegistrationPoliciesForUserGroupResponseBodyUserGroups] = None,
    ):
        self.request_id = request_id
        self.user_groups = user_groups

    def validate(self):
        if self.user_groups:
            for k in self.user_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['UserGroups'] = []
        if self.user_groups is not None:
            for k in self.user_groups:
                result['UserGroups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.user_groups = []
        if m.get('UserGroups') is not None:
            for k in m.get('UserGroups'):
                temp_model = ListRegistrationPoliciesForUserGroupResponseBodyUserGroups()
                self.user_groups.append(temp_model.from_map(k))
        return self


class ListRegistrationPoliciesForUserGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRegistrationPoliciesForUserGroupResponseBody = None,
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
            temp_model = ListRegistrationPoliciesForUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSoftwareForUserDeviceRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        device_tag: str = None,
        page_size: int = None,
    ):
        # This parameter is required.
        self.current_page = current_page
        # This parameter is required.
        self.device_tag = device_tag
        # This parameter is required.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.device_tag is not None:
            result['DeviceTag'] = self.device_tag
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DeviceTag') is not None:
            self.device_tag = m.get('DeviceTag')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListSoftwareForUserDeviceResponseBodySoftware(TeaModel):
    def __init__(
        self,
        inc: str = None,
        install_time: str = None,
        name: str = None,
        versions: List[str] = None,
    ):
        self.inc = inc
        self.install_time = install_time
        self.name = name
        self.versions = versions

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.inc is not None:
            result['Inc'] = self.inc
        if self.install_time is not None:
            result['InstallTime'] = self.install_time
        if self.name is not None:
            result['Name'] = self.name
        if self.versions is not None:
            result['Versions'] = self.versions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Inc') is not None:
            self.inc = m.get('Inc')
        if m.get('InstallTime') is not None:
            self.install_time = m.get('InstallTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Versions') is not None:
            self.versions = m.get('Versions')
        return self


class ListSoftwareForUserDeviceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        software: List[ListSoftwareForUserDeviceResponseBodySoftware] = None,
        total_num: int = None,
    ):
        self.request_id = request_id
        self.software = software
        self.total_num = total_num

    def validate(self):
        if self.software:
            for k in self.software:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Software'] = []
        if self.software is not None:
            for k in self.software:
                result['Software'].append(k.to_map() if k else None)
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.software = []
        if m.get('Software') is not None:
            for k in m.get('Software'):
                temp_model = ListSoftwareForUserDeviceResponseBodySoftware()
                self.software.append(temp_model.from_map(k))
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class ListSoftwareForUserDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSoftwareForUserDeviceResponseBody = None,
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
            temp_model = ListSoftwareForUserDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagsForPrivateAccessApplicationRequest(TeaModel):
    def __init__(
        self,
        application_ids: List[str] = None,
    ):
        # This parameter is required.
        self.application_ids = application_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_ids is not None:
            result['ApplicationIds'] = self.application_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationIds') is not None:
            self.application_ids = m.get('ApplicationIds')
        return self


class ListTagsForPrivateAccessApplicationResponseBodyApplicationsTags(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        name: str = None,
        tag_id: str = None,
        tag_type: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.name = name
        self.tag_id = tag_id
        self.tag_type = tag_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        if self.tag_type is not None:
            result['TagType'] = self.tag_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        if m.get('TagType') is not None:
            self.tag_type = m.get('TagType')
        return self


class ListTagsForPrivateAccessApplicationResponseBodyApplications(TeaModel):
    def __init__(
        self,
        application_id: str = None,
        tags: List[ListTagsForPrivateAccessApplicationResponseBodyApplicationsTags] = None,
    ):
        self.application_id = application_id
        self.tags = tags

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
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListTagsForPrivateAccessApplicationResponseBodyApplicationsTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListTagsForPrivateAccessApplicationResponseBody(TeaModel):
    def __init__(
        self,
        applications: List[ListTagsForPrivateAccessApplicationResponseBodyApplications] = None,
        request_id: str = None,
    ):
        self.applications = applications
        self.request_id = request_id

    def validate(self):
        if self.applications:
            for k in self.applications:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Applications'] = []
        if self.applications is not None:
            for k in self.applications:
                result['Applications'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.applications = []
        if m.get('Applications') is not None:
            for k in m.get('Applications'):
                temp_model = ListTagsForPrivateAccessApplicationResponseBodyApplications()
                self.applications.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListTagsForPrivateAccessApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagsForPrivateAccessApplicationResponseBody = None,
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
            temp_model = ListTagsForPrivateAccessApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagsForPrivateAccessPolicyRequest(TeaModel):
    def __init__(
        self,
        policy_ids: List[str] = None,
    ):
        # This parameter is required.
        self.policy_ids = policy_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')
        return self


class ListTagsForPrivateAccessPolicyResponseBodyPolicesTags(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        name: str = None,
        tag_id: str = None,
        tag_type: str = None,
    ):
        # 内网访问标签创建时间。
        self.create_time = create_time
        self.description = description
        self.name = name
        self.tag_id = tag_id
        self.tag_type = tag_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        if self.tag_type is not None:
            result['TagType'] = self.tag_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        if m.get('TagType') is not None:
            self.tag_type = m.get('TagType')
        return self


class ListTagsForPrivateAccessPolicyResponseBodyPolices(TeaModel):
    def __init__(
        self,
        policy_id: str = None,
        tags: List[ListTagsForPrivateAccessPolicyResponseBodyPolicesTags] = None,
    ):
        self.policy_id = policy_id
        self.tags = tags

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
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListTagsForPrivateAccessPolicyResponseBodyPolicesTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListTagsForPrivateAccessPolicyResponseBody(TeaModel):
    def __init__(
        self,
        polices: List[ListTagsForPrivateAccessPolicyResponseBodyPolices] = None,
        request_id: str = None,
    ):
        self.polices = polices
        self.request_id = request_id

    def validate(self):
        if self.polices:
            for k in self.polices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Polices'] = []
        if self.polices is not None:
            for k in self.polices:
                result['Polices'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.polices = []
        if m.get('Polices') is not None:
            for k in m.get('Polices'):
                temp_model = ListTagsForPrivateAccessPolicyResponseBodyPolices()
                self.polices.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListTagsForPrivateAccessPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagsForPrivateAccessPolicyResponseBody = None,
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
            temp_model = ListTagsForPrivateAccessPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserApplicationsRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        name: str = None,
        page_size: int = None,
        sase_user_id: str = None,
    ):
        # This parameter is required.
        self.current_page = current_page
        self.name = name
        # This parameter is required.
        self.page_size = page_size
        # This parameter is required.
        self.sase_user_id = sase_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.name is not None:
            result['Name'] = self.name
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sase_user_id is not None:
            result['SaseUserId'] = self.sase_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SaseUserId') is not None:
            self.sase_user_id = m.get('SaseUserId')
        return self


class ListUserApplicationsResponseBodyApplicationsPortRanges(TeaModel):
    def __init__(
        self,
        begin: str = None,
        end: str = None,
    ):
        self.begin = begin
        self.end = end

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.end is not None:
            result['End'] = self.end
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('End') is not None:
            self.end = m.get('End')
        return self


class ListUserApplicationsResponseBodyApplications(TeaModel):
    def __init__(
        self,
        action: str = None,
        addresses: List[str] = None,
        application_id: str = None,
        name: str = None,
        port_ranges: List[ListUserApplicationsResponseBodyApplicationsPortRanges] = None,
        protocol: str = None,
    ):
        self.action = action
        self.addresses = addresses
        self.application_id = application_id
        self.name = name
        self.port_ranges = port_ranges
        self.protocol = protocol

    def validate(self):
        if self.port_ranges:
            for k in self.port_ranges:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.addresses is not None:
            result['Addresses'] = self.addresses
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.name is not None:
            result['Name'] = self.name
        result['PortRanges'] = []
        if self.port_ranges is not None:
            for k in self.port_ranges:
                result['PortRanges'].append(k.to_map() if k else None)
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Addresses') is not None:
            self.addresses = m.get('Addresses')
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.port_ranges = []
        if m.get('PortRanges') is not None:
            for k in m.get('PortRanges'):
                temp_model = ListUserApplicationsResponseBodyApplicationsPortRanges()
                self.port_ranges.append(temp_model.from_map(k))
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        return self


class ListUserApplicationsResponseBody(TeaModel):
    def __init__(
        self,
        applications: List[ListUserApplicationsResponseBodyApplications] = None,
        request_id: str = None,
        total_num: int = None,
    ):
        self.applications = applications
        # Id of the request
        self.request_id = request_id
        self.total_num = total_num

    def validate(self):
        if self.applications:
            for k in self.applications:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Applications'] = []
        if self.applications is not None:
            for k in self.applications:
                result['Applications'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.applications = []
        if m.get('Applications') is not None:
            for k in m.get('Applications'):
                temp_model = ListUserApplicationsResponseBodyApplications()
                self.applications.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class ListUserApplicationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUserApplicationsResponseBody = None,
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
            temp_model = ListUserApplicationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserDevicesRequest(TeaModel):
    def __init__(
        self,
        app_statuses: List[str] = None,
        current_page: int = None,
        department: str = None,
        device_belong: str = None,
        device_statuses: List[str] = None,
        device_tags: List[str] = None,
        device_types: List[str] = None,
        dlp_statuses: List[str] = None,
        hostname: str = None,
        ia_statuses: List[str] = None,
        inner_ip: str = None,
        mac: str = None,
        nac_statuses: List[str] = None,
        pa_statuses: List[str] = None,
        page_size: int = None,
        sase_user_id: str = None,
        sharing_status: bool = None,
        sort_by: str = None,
        username: str = None,
    ):
        self.app_statuses = app_statuses
        # This parameter is required.
        self.current_page = current_page
        self.department = department
        self.device_belong = device_belong
        self.device_statuses = device_statuses
        self.device_tags = device_tags
        self.device_types = device_types
        self.dlp_statuses = dlp_statuses
        self.hostname = hostname
        self.ia_statuses = ia_statuses
        self.inner_ip = inner_ip
        self.mac = mac
        self.nac_statuses = nac_statuses
        self.pa_statuses = pa_statuses
        # This parameter is required.
        self.page_size = page_size
        self.sase_user_id = sase_user_id
        self.sharing_status = sharing_status
        self.sort_by = sort_by
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_statuses is not None:
            result['AppStatuses'] = self.app_statuses
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.department is not None:
            result['Department'] = self.department
        if self.device_belong is not None:
            result['DeviceBelong'] = self.device_belong
        if self.device_statuses is not None:
            result['DeviceStatuses'] = self.device_statuses
        if self.device_tags is not None:
            result['DeviceTags'] = self.device_tags
        if self.device_types is not None:
            result['DeviceTypes'] = self.device_types
        if self.dlp_statuses is not None:
            result['DlpStatuses'] = self.dlp_statuses
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.ia_statuses is not None:
            result['IaStatuses'] = self.ia_statuses
        if self.inner_ip is not None:
            result['InnerIp'] = self.inner_ip
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.nac_statuses is not None:
            result['NacStatuses'] = self.nac_statuses
        if self.pa_statuses is not None:
            result['PaStatuses'] = self.pa_statuses
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sase_user_id is not None:
            result['SaseUserId'] = self.sase_user_id
        if self.sharing_status is not None:
            result['SharingStatus'] = self.sharing_status
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppStatuses') is not None:
            self.app_statuses = m.get('AppStatuses')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Department') is not None:
            self.department = m.get('Department')
        if m.get('DeviceBelong') is not None:
            self.device_belong = m.get('DeviceBelong')
        if m.get('DeviceStatuses') is not None:
            self.device_statuses = m.get('DeviceStatuses')
        if m.get('DeviceTags') is not None:
            self.device_tags = m.get('DeviceTags')
        if m.get('DeviceTypes') is not None:
            self.device_types = m.get('DeviceTypes')
        if m.get('DlpStatuses') is not None:
            self.dlp_statuses = m.get('DlpStatuses')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('IaStatuses') is not None:
            self.ia_statuses = m.get('IaStatuses')
        if m.get('InnerIp') is not None:
            self.inner_ip = m.get('InnerIp')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('NacStatuses') is not None:
            self.nac_statuses = m.get('NacStatuses')
        if m.get('PaStatuses') is not None:
            self.pa_statuses = m.get('PaStatuses')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SaseUserId') is not None:
            self.sase_user_id = m.get('SaseUserId')
        if m.get('SharingStatus') is not None:
            self.sharing_status = m.get('SharingStatus')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class ListUserDevicesResponseBodyDevices(TeaModel):
    def __init__(
        self,
        app_status: str = None,
        app_version: str = None,
        cpu: str = None,
        create_time: str = None,
        department: str = None,
        device_belong: str = None,
        device_model: str = None,
        device_status: str = None,
        device_tag: str = None,
        device_type: str = None,
        device_version: str = None,
        disk: str = None,
        dlp_status: str = None,
        hostname: str = None,
        ia_status: str = None,
        inner_ip: str = None,
        mac: str = None,
        memory: str = None,
        nac_status: str = None,
        pa_status: str = None,
        sase_user_id: str = None,
        sharing_status: bool = None,
        src_ip: str = None,
        update_time: str = None,
        username: str = None,
    ):
        self.app_status = app_status
        self.app_version = app_version
        self.cpu = cpu
        self.create_time = create_time
        self.department = department
        self.device_belong = device_belong
        self.device_model = device_model
        self.device_status = device_status
        self.device_tag = device_tag
        self.device_type = device_type
        self.device_version = device_version
        self.disk = disk
        self.dlp_status = dlp_status
        self.hostname = hostname
        self.ia_status = ia_status
        self.inner_ip = inner_ip
        self.mac = mac
        self.memory = memory
        self.nac_status = nac_status
        self.pa_status = pa_status
        self.sase_user_id = sase_user_id
        self.sharing_status = sharing_status
        self.src_ip = src_ip
        self.update_time = update_time
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_status is not None:
            result['AppStatus'] = self.app_status
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.cpu is not None:
            result['CPU'] = self.cpu
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.department is not None:
            result['Department'] = self.department
        if self.device_belong is not None:
            result['DeviceBelong'] = self.device_belong
        if self.device_model is not None:
            result['DeviceModel'] = self.device_model
        if self.device_status is not None:
            result['DeviceStatus'] = self.device_status
        if self.device_tag is not None:
            result['DeviceTag'] = self.device_tag
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.device_version is not None:
            result['DeviceVersion'] = self.device_version
        if self.disk is not None:
            result['Disk'] = self.disk
        if self.dlp_status is not None:
            result['DlpStatus'] = self.dlp_status
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.ia_status is not None:
            result['IaStatus'] = self.ia_status
        if self.inner_ip is not None:
            result['InnerIP'] = self.inner_ip
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.nac_status is not None:
            result['NacStatus'] = self.nac_status
        if self.pa_status is not None:
            result['PaStatus'] = self.pa_status
        if self.sase_user_id is not None:
            result['SaseUserId'] = self.sase_user_id
        if self.sharing_status is not None:
            result['SharingStatus'] = self.sharing_status
        if self.src_ip is not None:
            result['SrcIP'] = self.src_ip
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppStatus') is not None:
            self.app_status = m.get('AppStatus')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('CPU') is not None:
            self.cpu = m.get('CPU')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Department') is not None:
            self.department = m.get('Department')
        if m.get('DeviceBelong') is not None:
            self.device_belong = m.get('DeviceBelong')
        if m.get('DeviceModel') is not None:
            self.device_model = m.get('DeviceModel')
        if m.get('DeviceStatus') is not None:
            self.device_status = m.get('DeviceStatus')
        if m.get('DeviceTag') is not None:
            self.device_tag = m.get('DeviceTag')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('DeviceVersion') is not None:
            self.device_version = m.get('DeviceVersion')
        if m.get('Disk') is not None:
            self.disk = m.get('Disk')
        if m.get('DlpStatus') is not None:
            self.dlp_status = m.get('DlpStatus')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('IaStatus') is not None:
            self.ia_status = m.get('IaStatus')
        if m.get('InnerIP') is not None:
            self.inner_ip = m.get('InnerIP')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('NacStatus') is not None:
            self.nac_status = m.get('NacStatus')
        if m.get('PaStatus') is not None:
            self.pa_status = m.get('PaStatus')
        if m.get('SaseUserId') is not None:
            self.sase_user_id = m.get('SaseUserId')
        if m.get('SharingStatus') is not None:
            self.sharing_status = m.get('SharingStatus')
        if m.get('SrcIP') is not None:
            self.src_ip = m.get('SrcIP')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class ListUserDevicesResponseBody(TeaModel):
    def __init__(
        self,
        devices: List[ListUserDevicesResponseBodyDevices] = None,
        request_id: str = None,
        total_num: int = None,
    ):
        self.devices = devices
        self.request_id = request_id
        self.total_num = total_num

    def validate(self):
        if self.devices:
            for k in self.devices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Devices'] = []
        if self.devices is not None:
            for k in self.devices:
                result['Devices'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.devices = []
        if m.get('Devices') is not None:
            for k in m.get('Devices'):
                temp_model = ListUserDevicesResponseBodyDevices()
                self.devices.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class ListUserDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUserDevicesResponseBody = None,
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
            temp_model = ListUserDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserGroupsRequest(TeaModel):
    def __init__(
        self,
        attribute_value: str = None,
        current_page: int = None,
        name: str = None,
        papolicy_id: str = None,
        page_size: int = None,
        user_group_ids: List[str] = None,
    ):
        self.attribute_value = attribute_value
        # This parameter is required.
        self.current_page = current_page
        # 用户组名称。长度为1~128个字符，支持中文和大小写英文字母，可包含数字、半角句号（.）、下划线（_）和短划线（-）。
        self.name = name
        self.papolicy_id = papolicy_id
        # This parameter is required.
        self.page_size = page_size
        self.user_group_ids = user_group_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attribute_value is not None:
            result['AttributeValue'] = self.attribute_value
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.name is not None:
            result['Name'] = self.name
        if self.papolicy_id is not None:
            result['PAPolicyId'] = self.papolicy_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttributeValue') is not None:
            self.attribute_value = m.get('AttributeValue')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PAPolicyId') is not None:
            self.papolicy_id = m.get('PAPolicyId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')
        return self


class ListUserGroupsResponseBodyUserGroupsAttributes(TeaModel):
    def __init__(
        self,
        idp_id: int = None,
        relation: str = None,
        user_group_type: str = None,
        value: str = None,
    ):
        self.idp_id = idp_id
        self.relation = relation
        self.user_group_type = user_group_type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.idp_id is not None:
            result['IdpId'] = self.idp_id
        if self.relation is not None:
            result['Relation'] = self.relation
        if self.user_group_type is not None:
            result['UserGroupType'] = self.user_group_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdpId') is not None:
            self.idp_id = m.get('IdpId')
        if m.get('Relation') is not None:
            self.relation = m.get('Relation')
        if m.get('UserGroupType') is not None:
            self.user_group_type = m.get('UserGroupType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListUserGroupsResponseBodyUserGroups(TeaModel):
    def __init__(
        self,
        attributes: List[ListUserGroupsResponseBodyUserGroupsAttributes] = None,
        create_time: str = None,
        description: str = None,
        name: str = None,
        user_group_id: str = None,
    ):
        self.attributes = attributes
        self.create_time = create_time
        self.description = description
        self.name = name
        self.user_group_id = user_group_id

    def validate(self):
        if self.attributes:
            for k in self.attributes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Attributes'] = []
        if self.attributes is not None:
            for k in self.attributes:
                result['Attributes'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attributes = []
        if m.get('Attributes') is not None:
            for k in m.get('Attributes'):
                temp_model = ListUserGroupsResponseBodyUserGroupsAttributes()
                self.attributes.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class ListUserGroupsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_num: int = None,
        user_groups: List[ListUserGroupsResponseBodyUserGroups] = None,
    ):
        self.request_id = request_id
        self.total_num = total_num
        self.user_groups = user_groups

    def validate(self):
        if self.user_groups:
            for k in self.user_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        result['UserGroups'] = []
        if self.user_groups is not None:
            for k in self.user_groups:
                result['UserGroups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        self.user_groups = []
        if m.get('UserGroups') is not None:
            for k in m.get('UserGroups'):
                temp_model = ListUserGroupsResponseBodyUserGroups()
                self.user_groups.append(temp_model.from_map(k))
        return self


class ListUserGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUserGroupsResponseBody = None,
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
            temp_model = ListUserGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserGroupsForPrivateAccessPolicyRequest(TeaModel):
    def __init__(
        self,
        policy_ids: List[str] = None,
    ):
        # This parameter is required.
        self.policy_ids = policy_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')
        return self


class ListUserGroupsForPrivateAccessPolicyResponseBodyPolicesUserGroupsAttributes(TeaModel):
    def __init__(
        self,
        idp_id: int = None,
        relation: str = None,
        user_group_type: str = None,
        value: str = None,
    ):
        self.idp_id = idp_id
        self.relation = relation
        self.user_group_type = user_group_type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.idp_id is not None:
            result['IdpId'] = self.idp_id
        if self.relation is not None:
            result['Relation'] = self.relation
        if self.user_group_type is not None:
            result['UserGroupType'] = self.user_group_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdpId') is not None:
            self.idp_id = m.get('IdpId')
        if m.get('Relation') is not None:
            self.relation = m.get('Relation')
        if m.get('UserGroupType') is not None:
            self.user_group_type = m.get('UserGroupType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListUserGroupsForPrivateAccessPolicyResponseBodyPolicesUserGroups(TeaModel):
    def __init__(
        self,
        attributes: List[ListUserGroupsForPrivateAccessPolicyResponseBodyPolicesUserGroupsAttributes] = None,
        create_time: str = None,
        description: str = None,
        name: str = None,
        user_group_id: str = None,
    ):
        self.attributes = attributes
        # 用户组创建时间。
        self.create_time = create_time
        self.description = description
        self.name = name
        self.user_group_id = user_group_id

    def validate(self):
        if self.attributes:
            for k in self.attributes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Attributes'] = []
        if self.attributes is not None:
            for k in self.attributes:
                result['Attributes'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attributes = []
        if m.get('Attributes') is not None:
            for k in m.get('Attributes'):
                temp_model = ListUserGroupsForPrivateAccessPolicyResponseBodyPolicesUserGroupsAttributes()
                self.attributes.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class ListUserGroupsForPrivateAccessPolicyResponseBodyPolices(TeaModel):
    def __init__(
        self,
        policy_id: str = None,
        user_groups: List[ListUserGroupsForPrivateAccessPolicyResponseBodyPolicesUserGroups] = None,
    ):
        self.policy_id = policy_id
        self.user_groups = user_groups

    def validate(self):
        if self.user_groups:
            for k in self.user_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        result['UserGroups'] = []
        if self.user_groups is not None:
            for k in self.user_groups:
                result['UserGroups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        self.user_groups = []
        if m.get('UserGroups') is not None:
            for k in m.get('UserGroups'):
                temp_model = ListUserGroupsForPrivateAccessPolicyResponseBodyPolicesUserGroups()
                self.user_groups.append(temp_model.from_map(k))
        return self


class ListUserGroupsForPrivateAccessPolicyResponseBody(TeaModel):
    def __init__(
        self,
        polices: List[ListUserGroupsForPrivateAccessPolicyResponseBodyPolices] = None,
        request_id: str = None,
    ):
        self.polices = polices
        self.request_id = request_id

    def validate(self):
        if self.polices:
            for k in self.polices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Polices'] = []
        if self.polices is not None:
            for k in self.polices:
                result['Polices'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.polices = []
        if m.get('Polices') is not None:
            for k in m.get('Polices'):
                temp_model = ListUserGroupsForPrivateAccessPolicyResponseBodyPolices()
                self.polices.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListUserGroupsForPrivateAccessPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUserGroupsForPrivateAccessPolicyResponseBody = None,
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
            temp_model = ListUserGroupsForPrivateAccessPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserGroupsForRegistrationPolicyRequest(TeaModel):
    def __init__(
        self,
        policy_ids: List[str] = None,
    ):
        # This parameter is required.
        self.policy_ids = policy_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')
        return self


class ListUserGroupsForRegistrationPolicyResponseBodyPoliciesUserGroupsAttributes(TeaModel):
    def __init__(
        self,
        idp_id: int = None,
        relation: str = None,
        user_group_type: str = None,
        value: str = None,
    ):
        self.idp_id = idp_id
        self.relation = relation
        self.user_group_type = user_group_type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.idp_id is not None:
            result['IdpId'] = self.idp_id
        if self.relation is not None:
            result['Relation'] = self.relation
        if self.user_group_type is not None:
            result['UserGroupType'] = self.user_group_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdpId') is not None:
            self.idp_id = m.get('IdpId')
        if m.get('Relation') is not None:
            self.relation = m.get('Relation')
        if m.get('UserGroupType') is not None:
            self.user_group_type = m.get('UserGroupType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListUserGroupsForRegistrationPolicyResponseBodyPoliciesUserGroups(TeaModel):
    def __init__(
        self,
        attributes: List[ListUserGroupsForRegistrationPolicyResponseBodyPoliciesUserGroupsAttributes] = None,
        create_time: str = None,
        description: str = None,
        name: str = None,
        user_group_id: str = None,
    ):
        self.attributes = attributes
        self.create_time = create_time
        self.description = description
        self.name = name
        self.user_group_id = user_group_id

    def validate(self):
        if self.attributes:
            for k in self.attributes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Attributes'] = []
        if self.attributes is not None:
            for k in self.attributes:
                result['Attributes'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attributes = []
        if m.get('Attributes') is not None:
            for k in m.get('Attributes'):
                temp_model = ListUserGroupsForRegistrationPolicyResponseBodyPoliciesUserGroupsAttributes()
                self.attributes.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class ListUserGroupsForRegistrationPolicyResponseBodyPolicies(TeaModel):
    def __init__(
        self,
        policy_id: str = None,
        user_groups: List[ListUserGroupsForRegistrationPolicyResponseBodyPoliciesUserGroups] = None,
    ):
        self.policy_id = policy_id
        self.user_groups = user_groups

    def validate(self):
        if self.user_groups:
            for k in self.user_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        result['UserGroups'] = []
        if self.user_groups is not None:
            for k in self.user_groups:
                result['UserGroups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        self.user_groups = []
        if m.get('UserGroups') is not None:
            for k in m.get('UserGroups'):
                temp_model = ListUserGroupsForRegistrationPolicyResponseBodyPoliciesUserGroups()
                self.user_groups.append(temp_model.from_map(k))
        return self


class ListUserGroupsForRegistrationPolicyResponseBody(TeaModel):
    def __init__(
        self,
        policies: List[ListUserGroupsForRegistrationPolicyResponseBodyPolicies] = None,
        request_id: str = None,
    ):
        self.policies = policies
        self.request_id = request_id

    def validate(self):
        if self.policies:
            for k in self.policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Policies'] = []
        if self.policies is not None:
            for k in self.policies:
                result['Policies'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.policies = []
        if m.get('Policies') is not None:
            for k in m.get('Policies'):
                temp_model = ListUserGroupsForRegistrationPolicyResponseBodyPolicies()
                self.policies.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListUserGroupsForRegistrationPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUserGroupsForRegistrationPolicyResponseBody = None,
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
            temp_model = ListUserGroupsForRegistrationPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserPrivateAccessPoliciesRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        name: str = None,
        page_size: int = None,
        sase_user_id: str = None,
    ):
        # This parameter is required.
        self.current_page = current_page
        self.name = name
        # This parameter is required.
        self.page_size = page_size
        # This parameter is required.
        self.sase_user_id = sase_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.name is not None:
            result['Name'] = self.name
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sase_user_id is not None:
            result['SaseUserId'] = self.sase_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SaseUserId') is not None:
            self.sase_user_id = m.get('SaseUserId')
        return self


class ListUserPrivateAccessPoliciesResponseBodyPolicesCustomUserAttributes(TeaModel):
    def __init__(
        self,
        idp_id: int = None,
        relation: str = None,
        user_group_type: str = None,
        value: str = None,
    ):
        self.idp_id = idp_id
        self.relation = relation
        self.user_group_type = user_group_type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.idp_id is not None:
            result['IdpId'] = self.idp_id
        if self.relation is not None:
            result['Relation'] = self.relation
        if self.user_group_type is not None:
            result['UserGroupType'] = self.user_group_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdpId') is not None:
            self.idp_id = m.get('IdpId')
        if m.get('Relation') is not None:
            self.relation = m.get('Relation')
        if m.get('UserGroupType') is not None:
            self.user_group_type = m.get('UserGroupType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListUserPrivateAccessPoliciesResponseBodyPolices(TeaModel):
    def __init__(
        self,
        custom_user_attributes: List[ListUserPrivateAccessPoliciesResponseBodyPolicesCustomUserAttributes] = None,
        device_attribute_name: str = None,
        matched_user_group: str = None,
        name: str = None,
        policy_action: str = None,
        policy_id: str = None,
        priority: int = None,
        user_group_mode: str = None,
    ):
        self.custom_user_attributes = custom_user_attributes
        self.device_attribute_name = device_attribute_name
        self.matched_user_group = matched_user_group
        self.name = name
        self.policy_action = policy_action
        self.policy_id = policy_id
        self.priority = priority
        self.user_group_mode = user_group_mode

    def validate(self):
        if self.custom_user_attributes:
            for k in self.custom_user_attributes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CustomUserAttributes'] = []
        if self.custom_user_attributes is not None:
            for k in self.custom_user_attributes:
                result['CustomUserAttributes'].append(k.to_map() if k else None)
        if self.device_attribute_name is not None:
            result['DeviceAttributeName'] = self.device_attribute_name
        if self.matched_user_group is not None:
            result['MatchedUserGroup'] = self.matched_user_group
        if self.name is not None:
            result['Name'] = self.name
        if self.policy_action is not None:
            result['PolicyAction'] = self.policy_action
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.user_group_mode is not None:
            result['UserGroupMode'] = self.user_group_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_user_attributes = []
        if m.get('CustomUserAttributes') is not None:
            for k in m.get('CustomUserAttributes'):
                temp_model = ListUserPrivateAccessPoliciesResponseBodyPolicesCustomUserAttributes()
                self.custom_user_attributes.append(temp_model.from_map(k))
        if m.get('DeviceAttributeName') is not None:
            self.device_attribute_name = m.get('DeviceAttributeName')
        if m.get('MatchedUserGroup') is not None:
            self.matched_user_group = m.get('MatchedUserGroup')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PolicyAction') is not None:
            self.policy_action = m.get('PolicyAction')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('UserGroupMode') is not None:
            self.user_group_mode = m.get('UserGroupMode')
        return self


class ListUserPrivateAccessPoliciesResponseBody(TeaModel):
    def __init__(
        self,
        polices: List[ListUserPrivateAccessPoliciesResponseBodyPolices] = None,
        request_id: str = None,
        total_num: int = None,
    ):
        self.polices = polices
        # Id of the request
        self.request_id = request_id
        self.total_num = total_num

    def validate(self):
        if self.polices:
            for k in self.polices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Polices'] = []
        if self.polices is not None:
            for k in self.polices:
                result['Polices'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.polices = []
        if m.get('Polices') is not None:
            for k in m.get('Polices'):
                temp_model = ListUserPrivateAccessPoliciesResponseBodyPolices()
                self.polices.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class ListUserPrivateAccessPoliciesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUserPrivateAccessPoliciesResponseBody = None,
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
            temp_model = ListUserPrivateAccessPoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUsersRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        department: str = None,
        fuzzy_username: str = None,
        page_size: int = None,
        precise_username: str = None,
        sase_user_ids: List[str] = None,
        status: str = None,
    ):
        # This parameter is required.
        self.current_page = current_page
        self.department = department
        self.fuzzy_username = fuzzy_username
        # This parameter is required.
        self.page_size = page_size
        self.precise_username = precise_username
        self.sase_user_ids = sase_user_ids
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.department is not None:
            result['Department'] = self.department
        if self.fuzzy_username is not None:
            result['FuzzyUsername'] = self.fuzzy_username
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.precise_username is not None:
            result['PreciseUsername'] = self.precise_username
        if self.sase_user_ids is not None:
            result['SaseUserIds'] = self.sase_user_ids
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Department') is not None:
            self.department = m.get('Department')
        if m.get('FuzzyUsername') is not None:
            self.fuzzy_username = m.get('FuzzyUsername')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PreciseUsername') is not None:
            self.precise_username = m.get('PreciseUsername')
        if m.get('SaseUserIds') is not None:
            self.sase_user_ids = m.get('SaseUserIds')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListUsersResponseBodyUsers(TeaModel):
    def __init__(
        self,
        department: str = None,
        email: str = None,
        idp_name: str = None,
        phone: str = None,
        sase_user_id: str = None,
        status: str = None,
        username: str = None,
    ):
        self.department = department
        self.email = email
        self.idp_name = idp_name
        self.phone = phone
        self.sase_user_id = sase_user_id
        self.status = status
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.department is not None:
            result['Department'] = self.department
        if self.email is not None:
            result['Email'] = self.email
        if self.idp_name is not None:
            result['IdpName'] = self.idp_name
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.sase_user_id is not None:
            result['SaseUserId'] = self.sase_user_id
        if self.status is not None:
            result['Status'] = self.status
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Department') is not None:
            self.department = m.get('Department')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('IdpName') is not None:
            self.idp_name = m.get('IdpName')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('SaseUserId') is not None:
            self.sase_user_id = m.get('SaseUserId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class ListUsersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_num: str = None,
        users: List[ListUsersResponseBodyUsers] = None,
    ):
        self.request_id = request_id
        self.total_num = total_num
        self.users = users

    def validate(self):
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        result['Users'] = []
        if self.users is not None:
            for k in self.users:
                result['Users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        self.users = []
        if m.get('Users') is not None:
            for k in m.get('Users'):
                temp_model = ListUsersResponseBodyUsers()
                self.users.append(temp_model.from_map(k))
        return self


class ListUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUsersResponseBody = None,
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
            temp_model = ListUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LookupWmInfoMappingRequest(TeaModel):
    def __init__(
        self,
        wm_info_size: int = None,
        wm_info_uint: str = None,
        wm_type: str = None,
    ):
        self.wm_info_size = wm_info_size
        # This parameter is required.
        self.wm_info_uint = wm_info_uint
        # This parameter is required.
        self.wm_type = wm_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.wm_info_size is not None:
            result['WmInfoSize'] = self.wm_info_size
        if self.wm_info_uint is not None:
            result['WmInfoUint'] = self.wm_info_uint
        if self.wm_type is not None:
            result['WmType'] = self.wm_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WmInfoSize') is not None:
            self.wm_info_size = m.get('WmInfoSize')
        if m.get('WmInfoUint') is not None:
            self.wm_info_uint = m.get('WmInfoUint')
        if m.get('WmType') is not None:
            self.wm_type = m.get('WmType')
        return self


class LookupWmInfoMappingResponseBodyData(TeaModel):
    def __init__(
        self,
        wm_info_bytes_b64: str = None,
    ):
        self.wm_info_bytes_b64 = wm_info_bytes_b64

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.wm_info_bytes_b64 is not None:
            result['WmInfoBytesB64'] = self.wm_info_bytes_b64
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WmInfoBytesB64') is not None:
            self.wm_info_bytes_b64 = m.get('WmInfoBytesB64')
        return self


class LookupWmInfoMappingResponseBody(TeaModel):
    def __init__(
        self,
        data: LookupWmInfoMappingResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = LookupWmInfoMappingResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class LookupWmInfoMappingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: LookupWmInfoMappingResponseBody = None,
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
            temp_model = LookupWmInfoMappingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RevokeUserSessionRequest(TeaModel):
    def __init__(
        self,
        external_ids: str = None,
        idp_id: str = None,
    ):
        # This parameter is required.
        self.external_ids = external_ids
        # This parameter is required.
        self.idp_id = idp_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.external_ids is not None:
            result['ExternalIds'] = self.external_ids
        if self.idp_id is not None:
            result['IdpId'] = self.idp_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternalIds') is not None:
            self.external_ids = m.get('ExternalIds')
        if m.get('IdpId') is not None:
            self.idp_id = m.get('IdpId')
        return self


class RevokeUserSessionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RevokeUserSessionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RevokeUserSessionResponseBody = None,
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
            temp_model = RevokeUserSessionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateClientUserRequest(TeaModel):
    def __init__(
        self,
        department_id: str = None,
        description: str = None,
        email: str = None,
        id: str = None,
        mobile_number: str = None,
    ):
        self.department_id = department_id
        self.description = description
        self.email = email
        # This parameter is required.
        self.id = id
        self.mobile_number = mobile_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.department_id is not None:
            result['DepartmentId'] = self.department_id
        if self.description is not None:
            result['Description'] = self.description
        if self.email is not None:
            result['Email'] = self.email
        if self.id is not None:
            result['Id'] = self.id
        if self.mobile_number is not None:
            result['MobileNumber'] = self.mobile_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MobileNumber') is not None:
            self.mobile_number = m.get('MobileNumber')
        return self


class UpdateClientUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateClientUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateClientUserResponseBody = None,
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
            temp_model = UpdateClientUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateClientUserPasswordRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        password: str = None,
        username: str = None,
    ):
        self.id = id
        self.password = password
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.password is not None:
            result['Password'] = self.password
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class UpdateClientUserPasswordResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateClientUserPasswordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateClientUserPasswordResponseBody = None,
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
            temp_model = UpdateClientUserPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateClientUserStatusRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        status: str = None,
    ):
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateClientUserStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateClientUserStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateClientUserStatusResponseBody = None,
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
            temp_model = UpdateClientUserStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDynamicRouteRequest(TeaModel):
    def __init__(
        self,
        application_ids: List[str] = None,
        application_type: str = None,
        description: str = None,
        dynamic_route_id: str = None,
        dynamic_route_type: str = None,
        modify_type: str = None,
        name: str = None,
        next_hop: str = None,
        priority: int = None,
        region_ids: List[str] = None,
        status: str = None,
        tag_ids: List[str] = None,
    ):
        self.application_ids = application_ids
        self.application_type = application_type
        self.description = description
        # This parameter is required.
        self.dynamic_route_id = dynamic_route_id
        self.dynamic_route_type = dynamic_route_type
        self.modify_type = modify_type
        self.name = name
        self.next_hop = next_hop
        self.priority = priority
        self.region_ids = region_ids
        self.status = status
        self.tag_ids = tag_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_ids is not None:
            result['ApplicationIds'] = self.application_ids
        if self.application_type is not None:
            result['ApplicationType'] = self.application_type
        if self.description is not None:
            result['Description'] = self.description
        if self.dynamic_route_id is not None:
            result['DynamicRouteId'] = self.dynamic_route_id
        if self.dynamic_route_type is not None:
            result['DynamicRouteType'] = self.dynamic_route_type
        if self.modify_type is not None:
            result['ModifyType'] = self.modify_type
        if self.name is not None:
            result['Name'] = self.name
        if self.next_hop is not None:
            result['NextHop'] = self.next_hop
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids
        if self.status is not None:
            result['Status'] = self.status
        if self.tag_ids is not None:
            result['TagIds'] = self.tag_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationIds') is not None:
            self.application_ids = m.get('ApplicationIds')
        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DynamicRouteId') is not None:
            self.dynamic_route_id = m.get('DynamicRouteId')
        if m.get('DynamicRouteType') is not None:
            self.dynamic_route_type = m.get('DynamicRouteType')
        if m.get('ModifyType') is not None:
            self.modify_type = m.get('ModifyType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NextHop') is not None:
            self.next_hop = m.get('NextHop')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('RegionIds') is not None:
            self.region_ids = m.get('RegionIds')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TagIds') is not None:
            self.tag_ids = m.get('TagIds')
        return self


class UpdateDynamicRouteResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateDynamicRouteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDynamicRouteResponseBody = None,
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
            temp_model = UpdateDynamicRouteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateExcessiveDeviceRegistrationApplicationsStatusRequest(TeaModel):
    def __init__(
        self,
        application_ids: List[str] = None,
        status: str = None,
    ):
        # This parameter is required.
        self.application_ids = application_ids
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_ids is not None:
            result['ApplicationIds'] = self.application_ids
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationIds') is not None:
            self.application_ids = m.get('ApplicationIds')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateExcessiveDeviceRegistrationApplicationsStatusResponseBodyApplications(TeaModel):
    def __init__(
        self,
        application_id: str = None,
        create_time: str = None,
        department: str = None,
        description: str = None,
        device_tag: str = None,
        device_type: str = None,
        hostname: str = None,
        is_used: bool = None,
        mac: str = None,
        sase_user_id: str = None,
        status: str = None,
        username: str = None,
    ):
        self.application_id = application_id
        self.create_time = create_time
        self.department = department
        self.description = description
        self.device_tag = device_tag
        self.device_type = device_type
        self.hostname = hostname
        self.is_used = is_used
        self.mac = mac
        self.sase_user_id = sase_user_id
        self.status = status
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.department is not None:
            result['Department'] = self.department
        if self.description is not None:
            result['Description'] = self.description
        if self.device_tag is not None:
            result['DeviceTag'] = self.device_tag
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.is_used is not None:
            result['IsUsed'] = self.is_used
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.sase_user_id is not None:
            result['SaseUserId'] = self.sase_user_id
        if self.status is not None:
            result['Status'] = self.status
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Department') is not None:
            self.department = m.get('Department')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DeviceTag') is not None:
            self.device_tag = m.get('DeviceTag')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('IsUsed') is not None:
            self.is_used = m.get('IsUsed')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('SaseUserId') is not None:
            self.sase_user_id = m.get('SaseUserId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class UpdateExcessiveDeviceRegistrationApplicationsStatusResponseBody(TeaModel):
    def __init__(
        self,
        applications: List[UpdateExcessiveDeviceRegistrationApplicationsStatusResponseBodyApplications] = None,
        request_id: str = None,
    ):
        self.applications = applications
        self.request_id = request_id

    def validate(self):
        if self.applications:
            for k in self.applications:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Applications'] = []
        if self.applications is not None:
            for k in self.applications:
                result['Applications'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.applications = []
        if m.get('Applications') is not None:
            for k in m.get('Applications'):
                temp_model = UpdateExcessiveDeviceRegistrationApplicationsStatusResponseBodyApplications()
                self.applications.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateExcessiveDeviceRegistrationApplicationsStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateExcessiveDeviceRegistrationApplicationsStatusResponseBody = None,
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
            temp_model = UpdateExcessiveDeviceRegistrationApplicationsStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateIdpDepartmentRequest(TeaModel):
    def __init__(
        self,
        department_id: str = None,
        department_name: str = None,
        idp_config_id: str = None,
    ):
        # This parameter is required.
        self.department_id = department_id
        # This parameter is required.
        self.department_name = department_name
        # This parameter is required.
        self.idp_config_id = idp_config_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.department_id is not None:
            result['DepartmentId'] = self.department_id
        if self.department_name is not None:
            result['DepartmentName'] = self.department_name
        if self.idp_config_id is not None:
            result['IdpConfigId'] = self.idp_config_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')
        if m.get('DepartmentName') is not None:
            self.department_name = m.get('DepartmentName')
        if m.get('IdpConfigId') is not None:
            self.idp_config_id = m.get('IdpConfigId')
        return self


class UpdateIdpDepartmentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateIdpDepartmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateIdpDepartmentResponseBody = None,
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
            temp_model = UpdateIdpDepartmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateNacUserCertStatusRequestIdList(TeaModel):
    def __init__(
        self,
        dev_tag: str = None,
        user_id: str = None,
    ):
        self.dev_tag = dev_tag
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dev_tag is not None:
            result['DevTag'] = self.dev_tag
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DevTag') is not None:
            self.dev_tag = m.get('DevTag')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class UpdateNacUserCertStatusRequest(TeaModel):
    def __init__(
        self,
        id_list: List[UpdateNacUserCertStatusRequestIdList] = None,
        status: str = None,
    ):
        self.id_list = id_list
        self.status = status

    def validate(self):
        if self.id_list:
            for k in self.id_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['IdList'] = []
        if self.id_list is not None:
            for k in self.id_list:
                result['IdList'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.id_list = []
        if m.get('IdList') is not None:
            for k in m.get('IdList'):
                temp_model = UpdateNacUserCertStatusRequestIdList()
                self.id_list.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateNacUserCertStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateNacUserCertStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateNacUserCertStatusResponseBody = None,
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
            temp_model = UpdateNacUserCertStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePrivateAccessApplicationRequestPortRanges(TeaModel):
    def __init__(
        self,
        begin: int = None,
        end: int = None,
    ):
        self.begin = begin
        self.end = end

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.end is not None:
            result['End'] = self.end
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('End') is not None:
            self.end = m.get('End')
        return self


class UpdatePrivateAccessApplicationRequest(TeaModel):
    def __init__(
        self,
        addresses: List[str] = None,
        application_id: str = None,
        description: str = None,
        l_7proxy_domain_automatic_prefix: str = None,
        l_7proxy_domain_custom: str = None,
        l_7proxy_domain_private: str = None,
        modify_type: str = None,
        port_ranges: List[UpdatePrivateAccessApplicationRequestPortRanges] = None,
        protocol: str = None,
        status: str = None,
        tag_ids: List[str] = None,
    ):
        self.addresses = addresses
        # This parameter is required.
        self.application_id = application_id
        self.description = description
        self.l_7proxy_domain_automatic_prefix = l_7proxy_domain_automatic_prefix
        self.l_7proxy_domain_custom = l_7proxy_domain_custom
        self.l_7proxy_domain_private = l_7proxy_domain_private
        self.modify_type = modify_type
        self.port_ranges = port_ranges
        self.protocol = protocol
        self.status = status
        self.tag_ids = tag_ids

    def validate(self):
        if self.port_ranges:
            for k in self.port_ranges:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.addresses is not None:
            result['Addresses'] = self.addresses
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.description is not None:
            result['Description'] = self.description
        if self.l_7proxy_domain_automatic_prefix is not None:
            result['L7ProxyDomainAutomaticPrefix'] = self.l_7proxy_domain_automatic_prefix
        if self.l_7proxy_domain_custom is not None:
            result['L7ProxyDomainCustom'] = self.l_7proxy_domain_custom
        if self.l_7proxy_domain_private is not None:
            result['L7ProxyDomainPrivate'] = self.l_7proxy_domain_private
        if self.modify_type is not None:
            result['ModifyType'] = self.modify_type
        result['PortRanges'] = []
        if self.port_ranges is not None:
            for k in self.port_ranges:
                result['PortRanges'].append(k.to_map() if k else None)
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.status is not None:
            result['Status'] = self.status
        if self.tag_ids is not None:
            result['TagIds'] = self.tag_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Addresses') is not None:
            self.addresses = m.get('Addresses')
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('L7ProxyDomainAutomaticPrefix') is not None:
            self.l_7proxy_domain_automatic_prefix = m.get('L7ProxyDomainAutomaticPrefix')
        if m.get('L7ProxyDomainCustom') is not None:
            self.l_7proxy_domain_custom = m.get('L7ProxyDomainCustom')
        if m.get('L7ProxyDomainPrivate') is not None:
            self.l_7proxy_domain_private = m.get('L7ProxyDomainPrivate')
        if m.get('ModifyType') is not None:
            self.modify_type = m.get('ModifyType')
        self.port_ranges = []
        if m.get('PortRanges') is not None:
            for k in m.get('PortRanges'):
                temp_model = UpdatePrivateAccessApplicationRequestPortRanges()
                self.port_ranges.append(temp_model.from_map(k))
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TagIds') is not None:
            self.tag_ids = m.get('TagIds')
        return self


class UpdatePrivateAccessApplicationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdatePrivateAccessApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdatePrivateAccessApplicationResponseBody = None,
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
            temp_model = UpdatePrivateAccessApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePrivateAccessPolicyRequestCustomUserAttributes(TeaModel):
    def __init__(
        self,
        idp_id: int = None,
        relation: str = None,
        user_group_type: str = None,
        value: str = None,
    ):
        self.idp_id = idp_id
        # This parameter is required.
        self.relation = relation
        # This parameter is required.
        self.user_group_type = user_group_type
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.idp_id is not None:
            result['IdpId'] = self.idp_id
        if self.relation is not None:
            result['Relation'] = self.relation
        if self.user_group_type is not None:
            result['UserGroupType'] = self.user_group_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdpId') is not None:
            self.idp_id = m.get('IdpId')
        if m.get('Relation') is not None:
            self.relation = m.get('Relation')
        if m.get('UserGroupType') is not None:
            self.user_group_type = m.get('UserGroupType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdatePrivateAccessPolicyRequest(TeaModel):
    def __init__(
        self,
        application_ids: List[str] = None,
        application_type: str = None,
        custom_user_attributes: List[UpdatePrivateAccessPolicyRequestCustomUserAttributes] = None,
        description: str = None,
        device_attribute_action: str = None,
        device_attribute_id: str = None,
        modify_type: str = None,
        policy_action: str = None,
        policy_id: str = None,
        priority: int = None,
        status: str = None,
        tag_ids: List[str] = None,
        user_group_ids: List[str] = None,
        user_group_mode: str = None,
    ):
        self.application_ids = application_ids
        self.application_type = application_type
        self.custom_user_attributes = custom_user_attributes
        self.description = description
        self.device_attribute_action = device_attribute_action
        self.device_attribute_id = device_attribute_id
        self.modify_type = modify_type
        self.policy_action = policy_action
        # This parameter is required.
        self.policy_id = policy_id
        self.priority = priority
        self.status = status
        # 内网访问标签ID集合。一条策略最多支持100个内网访问标签ID。
        self.tag_ids = tag_ids
        self.user_group_ids = user_group_ids
        # 内网访问策略的用户组类型。取值：
        # - **Normal**：普通用户组。
        # - **Custom**：自定义用户组。
        self.user_group_mode = user_group_mode

    def validate(self):
        if self.custom_user_attributes:
            for k in self.custom_user_attributes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_ids is not None:
            result['ApplicationIds'] = self.application_ids
        if self.application_type is not None:
            result['ApplicationType'] = self.application_type
        result['CustomUserAttributes'] = []
        if self.custom_user_attributes is not None:
            for k in self.custom_user_attributes:
                result['CustomUserAttributes'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.device_attribute_action is not None:
            result['DeviceAttributeAction'] = self.device_attribute_action
        if self.device_attribute_id is not None:
            result['DeviceAttributeId'] = self.device_attribute_id
        if self.modify_type is not None:
            result['ModifyType'] = self.modify_type
        if self.policy_action is not None:
            result['PolicyAction'] = self.policy_action
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.status is not None:
            result['Status'] = self.status
        if self.tag_ids is not None:
            result['TagIds'] = self.tag_ids
        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids
        if self.user_group_mode is not None:
            result['UserGroupMode'] = self.user_group_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationIds') is not None:
            self.application_ids = m.get('ApplicationIds')
        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')
        self.custom_user_attributes = []
        if m.get('CustomUserAttributes') is not None:
            for k in m.get('CustomUserAttributes'):
                temp_model = UpdatePrivateAccessPolicyRequestCustomUserAttributes()
                self.custom_user_attributes.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DeviceAttributeAction') is not None:
            self.device_attribute_action = m.get('DeviceAttributeAction')
        if m.get('DeviceAttributeId') is not None:
            self.device_attribute_id = m.get('DeviceAttributeId')
        if m.get('ModifyType') is not None:
            self.modify_type = m.get('ModifyType')
        if m.get('PolicyAction') is not None:
            self.policy_action = m.get('PolicyAction')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TagIds') is not None:
            self.tag_ids = m.get('TagIds')
        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')
        if m.get('UserGroupMode') is not None:
            self.user_group_mode = m.get('UserGroupMode')
        return self


class UpdatePrivateAccessPolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdatePrivateAccessPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdatePrivateAccessPolicyResponseBody = None,
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
            temp_model = UpdatePrivateAccessPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRegistrationPolicyRequestCompanyLimitCount(TeaModel):
    def __init__(
        self,
        all: int = None,
        mobile: int = None,
        pc: int = None,
    ):
        self.all = all
        self.mobile = mobile
        self.pc = pc

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.pc is not None:
            result['PC'] = self.pc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('PC') is not None:
            self.pc = m.get('PC')
        return self


class UpdateRegistrationPolicyRequestPersonalLimitCount(TeaModel):
    def __init__(
        self,
        all: int = None,
        mobile: int = None,
        pc: int = None,
    ):
        self.all = all
        self.mobile = mobile
        self.pc = pc

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.pc is not None:
            result['PC'] = self.pc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('PC') is not None:
            self.pc = m.get('PC')
        return self


class UpdateRegistrationPolicyRequest(TeaModel):
    def __init__(
        self,
        company_limit_count: UpdateRegistrationPolicyRequestCompanyLimitCount = None,
        company_limit_type: str = None,
        description: str = None,
        match_mode: str = None,
        name: str = None,
        personal_limit_count: UpdateRegistrationPolicyRequestPersonalLimitCount = None,
        personal_limit_type: str = None,
        policy_id: str = None,
        priority: int = None,
        status: str = None,
        user_group_ids: List[str] = None,
        whitelist: List[str] = None,
    ):
        self.company_limit_count = company_limit_count
        self.company_limit_type = company_limit_type
        self.description = description
        self.match_mode = match_mode
        self.name = name
        self.personal_limit_count = personal_limit_count
        self.personal_limit_type = personal_limit_type
        # This parameter is required.
        self.policy_id = policy_id
        self.priority = priority
        self.status = status
        self.user_group_ids = user_group_ids
        self.whitelist = whitelist

    def validate(self):
        if self.company_limit_count:
            self.company_limit_count.validate()
        if self.personal_limit_count:
            self.personal_limit_count.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.company_limit_count is not None:
            result['CompanyLimitCount'] = self.company_limit_count.to_map()
        if self.company_limit_type is not None:
            result['CompanyLimitType'] = self.company_limit_type
        if self.description is not None:
            result['Description'] = self.description
        if self.match_mode is not None:
            result['MatchMode'] = self.match_mode
        if self.name is not None:
            result['Name'] = self.name
        if self.personal_limit_count is not None:
            result['PersonalLimitCount'] = self.personal_limit_count.to_map()
        if self.personal_limit_type is not None:
            result['PersonalLimitType'] = self.personal_limit_type
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.status is not None:
            result['Status'] = self.status
        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids
        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompanyLimitCount') is not None:
            temp_model = UpdateRegistrationPolicyRequestCompanyLimitCount()
            self.company_limit_count = temp_model.from_map(m['CompanyLimitCount'])
        if m.get('CompanyLimitType') is not None:
            self.company_limit_type = m.get('CompanyLimitType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('MatchMode') is not None:
            self.match_mode = m.get('MatchMode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PersonalLimitCount') is not None:
            temp_model = UpdateRegistrationPolicyRequestPersonalLimitCount()
            self.personal_limit_count = temp_model.from_map(m['PersonalLimitCount'])
        if m.get('PersonalLimitType') is not None:
            self.personal_limit_type = m.get('PersonalLimitType')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')
        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')
        return self


class UpdateRegistrationPolicyShrinkRequest(TeaModel):
    def __init__(
        self,
        company_limit_count_shrink: str = None,
        company_limit_type: str = None,
        description: str = None,
        match_mode: str = None,
        name: str = None,
        personal_limit_count_shrink: str = None,
        personal_limit_type: str = None,
        policy_id: str = None,
        priority: int = None,
        status: str = None,
        user_group_ids: List[str] = None,
        whitelist: List[str] = None,
    ):
        self.company_limit_count_shrink = company_limit_count_shrink
        self.company_limit_type = company_limit_type
        self.description = description
        self.match_mode = match_mode
        self.name = name
        self.personal_limit_count_shrink = personal_limit_count_shrink
        self.personal_limit_type = personal_limit_type
        # This parameter is required.
        self.policy_id = policy_id
        self.priority = priority
        self.status = status
        self.user_group_ids = user_group_ids
        self.whitelist = whitelist

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.company_limit_count_shrink is not None:
            result['CompanyLimitCount'] = self.company_limit_count_shrink
        if self.company_limit_type is not None:
            result['CompanyLimitType'] = self.company_limit_type
        if self.description is not None:
            result['Description'] = self.description
        if self.match_mode is not None:
            result['MatchMode'] = self.match_mode
        if self.name is not None:
            result['Name'] = self.name
        if self.personal_limit_count_shrink is not None:
            result['PersonalLimitCount'] = self.personal_limit_count_shrink
        if self.personal_limit_type is not None:
            result['PersonalLimitType'] = self.personal_limit_type
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.status is not None:
            result['Status'] = self.status
        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids
        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompanyLimitCount') is not None:
            self.company_limit_count_shrink = m.get('CompanyLimitCount')
        if m.get('CompanyLimitType') is not None:
            self.company_limit_type = m.get('CompanyLimitType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('MatchMode') is not None:
            self.match_mode = m.get('MatchMode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PersonalLimitCount') is not None:
            self.personal_limit_count_shrink = m.get('PersonalLimitCount')
        if m.get('PersonalLimitType') is not None:
            self.personal_limit_type = m.get('PersonalLimitType')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')
        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')
        return self


class UpdateRegistrationPolicyResponseBodyPolicyLimitDetailLimitCount(TeaModel):
    def __init__(
        self,
        all: int = None,
        mobile: int = None,
        pc: int = None,
    ):
        self.all = all
        self.mobile = mobile
        self.pc = pc

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.pc is not None:
            result['PC'] = self.pc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('PC') is not None:
            self.pc = m.get('PC')
        return self


class UpdateRegistrationPolicyResponseBodyPolicyLimitDetail(TeaModel):
    def __init__(
        self,
        device_belong: str = None,
        limit_count: UpdateRegistrationPolicyResponseBodyPolicyLimitDetailLimitCount = None,
        limit_type: str = None,
    ):
        self.device_belong = device_belong
        self.limit_count = limit_count
        self.limit_type = limit_type

    def validate(self):
        if self.limit_count:
            self.limit_count.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_belong is not None:
            result['DeviceBelong'] = self.device_belong
        if self.limit_count is not None:
            result['LimitCount'] = self.limit_count.to_map()
        if self.limit_type is not None:
            result['LimitType'] = self.limit_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceBelong') is not None:
            self.device_belong = m.get('DeviceBelong')
        if m.get('LimitCount') is not None:
            temp_model = UpdateRegistrationPolicyResponseBodyPolicyLimitDetailLimitCount()
            self.limit_count = temp_model.from_map(m['LimitCount'])
        if m.get('LimitType') is not None:
            self.limit_type = m.get('LimitType')
        return self


class UpdateRegistrationPolicyResponseBodyPolicy(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        limit_detail: List[UpdateRegistrationPolicyResponseBodyPolicyLimitDetail] = None,
        match_mode: str = None,
        name: str = None,
        policy_id: str = None,
        priority: str = None,
        status: str = None,
        user_group_ids: List[str] = None,
        whitelist: List[str] = None,
    ):
        self.create_time = create_time
        self.description = description
        self.limit_detail = limit_detail
        self.match_mode = match_mode
        self.name = name
        self.policy_id = policy_id
        self.priority = priority
        self.status = status
        self.user_group_ids = user_group_ids
        self.whitelist = whitelist

    def validate(self):
        if self.limit_detail:
            for k in self.limit_detail:
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
        result['LimitDetail'] = []
        if self.limit_detail is not None:
            for k in self.limit_detail:
                result['LimitDetail'].append(k.to_map() if k else None)
        if self.match_mode is not None:
            result['MatchMode'] = self.match_mode
        if self.name is not None:
            result['Name'] = self.name
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.status is not None:
            result['Status'] = self.status
        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids
        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.limit_detail = []
        if m.get('LimitDetail') is not None:
            for k in m.get('LimitDetail'):
                temp_model = UpdateRegistrationPolicyResponseBodyPolicyLimitDetail()
                self.limit_detail.append(temp_model.from_map(k))
        if m.get('MatchMode') is not None:
            self.match_mode = m.get('MatchMode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')
        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')
        return self


class UpdateRegistrationPolicyResponseBody(TeaModel):
    def __init__(
        self,
        policy: UpdateRegistrationPolicyResponseBodyPolicy = None,
        request_id: str = None,
    ):
        self.policy = policy
        self.request_id = request_id

    def validate(self):
        if self.policy:
            self.policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Policy') is not None:
            temp_model = UpdateRegistrationPolicyResponseBodyPolicy()
            self.policy = temp_model.from_map(m['Policy'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateRegistrationPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateRegistrationPolicyResponseBody = None,
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
            temp_model = UpdateRegistrationPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserDevicesSharingStatusRequest(TeaModel):
    def __init__(
        self,
        device_tags: List[str] = None,
        sharing_status: bool = None,
    ):
        # This parameter is required.
        self.device_tags = device_tags
        # This parameter is required.
        self.sharing_status = sharing_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_tags is not None:
            result['DeviceTags'] = self.device_tags
        if self.sharing_status is not None:
            result['SharingStatus'] = self.sharing_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceTags') is not None:
            self.device_tags = m.get('DeviceTags')
        if m.get('SharingStatus') is not None:
            self.sharing_status = m.get('SharingStatus')
        return self


class UpdateUserDevicesSharingStatusResponseBodyDevices(TeaModel):
    def __init__(
        self,
        app_status: str = None,
        app_version: str = None,
        cpu: str = None,
        create_time: str = None,
        department: str = None,
        device_belong: str = None,
        device_model: str = None,
        device_status: str = None,
        device_tag: str = None,
        device_type: str = None,
        device_version: str = None,
        disk: str = None,
        dlp_status: str = None,
        hostname: str = None,
        ia_status: str = None,
        inner_ip: str = None,
        mac: str = None,
        memory: str = None,
        nac_status: str = None,
        pa_status: str = None,
        sase_user_id: str = None,
        sharing_status: bool = None,
        src_ip: str = None,
        update_time: str = None,
        username: str = None,
    ):
        self.app_status = app_status
        self.app_version = app_version
        self.cpu = cpu
        self.create_time = create_time
        self.department = department
        self.device_belong = device_belong
        self.device_model = device_model
        self.device_status = device_status
        self.device_tag = device_tag
        self.device_type = device_type
        self.device_version = device_version
        self.disk = disk
        self.dlp_status = dlp_status
        self.hostname = hostname
        self.ia_status = ia_status
        self.inner_ip = inner_ip
        self.mac = mac
        self.memory = memory
        self.nac_status = nac_status
        self.pa_status = pa_status
        self.sase_user_id = sase_user_id
        self.sharing_status = sharing_status
        self.src_ip = src_ip
        self.update_time = update_time
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_status is not None:
            result['AppStatus'] = self.app_status
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.cpu is not None:
            result['CPU'] = self.cpu
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.department is not None:
            result['Department'] = self.department
        if self.device_belong is not None:
            result['DeviceBelong'] = self.device_belong
        if self.device_model is not None:
            result['DeviceModel'] = self.device_model
        if self.device_status is not None:
            result['DeviceStatus'] = self.device_status
        if self.device_tag is not None:
            result['DeviceTag'] = self.device_tag
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.device_version is not None:
            result['DeviceVersion'] = self.device_version
        if self.disk is not None:
            result['Disk'] = self.disk
        if self.dlp_status is not None:
            result['DlpStatus'] = self.dlp_status
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.ia_status is not None:
            result['IaStatus'] = self.ia_status
        if self.inner_ip is not None:
            result['InnerIP'] = self.inner_ip
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.nac_status is not None:
            result['NacStatus'] = self.nac_status
        if self.pa_status is not None:
            result['PaStatus'] = self.pa_status
        if self.sase_user_id is not None:
            result['SaseUserId'] = self.sase_user_id
        if self.sharing_status is not None:
            result['SharingStatus'] = self.sharing_status
        if self.src_ip is not None:
            result['SrcIP'] = self.src_ip
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppStatus') is not None:
            self.app_status = m.get('AppStatus')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('CPU') is not None:
            self.cpu = m.get('CPU')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Department') is not None:
            self.department = m.get('Department')
        if m.get('DeviceBelong') is not None:
            self.device_belong = m.get('DeviceBelong')
        if m.get('DeviceModel') is not None:
            self.device_model = m.get('DeviceModel')
        if m.get('DeviceStatus') is not None:
            self.device_status = m.get('DeviceStatus')
        if m.get('DeviceTag') is not None:
            self.device_tag = m.get('DeviceTag')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('DeviceVersion') is not None:
            self.device_version = m.get('DeviceVersion')
        if m.get('Disk') is not None:
            self.disk = m.get('Disk')
        if m.get('DlpStatus') is not None:
            self.dlp_status = m.get('DlpStatus')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('IaStatus') is not None:
            self.ia_status = m.get('IaStatus')
        if m.get('InnerIP') is not None:
            self.inner_ip = m.get('InnerIP')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('NacStatus') is not None:
            self.nac_status = m.get('NacStatus')
        if m.get('PaStatus') is not None:
            self.pa_status = m.get('PaStatus')
        if m.get('SaseUserId') is not None:
            self.sase_user_id = m.get('SaseUserId')
        if m.get('SharingStatus') is not None:
            self.sharing_status = m.get('SharingStatus')
        if m.get('SrcIP') is not None:
            self.src_ip = m.get('SrcIP')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class UpdateUserDevicesSharingStatusResponseBody(TeaModel):
    def __init__(
        self,
        devices: List[UpdateUserDevicesSharingStatusResponseBodyDevices] = None,
        request_id: str = None,
    ):
        self.devices = devices
        self.request_id = request_id

    def validate(self):
        if self.devices:
            for k in self.devices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Devices'] = []
        if self.devices is not None:
            for k in self.devices:
                result['Devices'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.devices = []
        if m.get('Devices') is not None:
            for k in m.get('Devices'):
                temp_model = UpdateUserDevicesSharingStatusResponseBodyDevices()
                self.devices.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateUserDevicesSharingStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateUserDevicesSharingStatusResponseBody = None,
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
            temp_model = UpdateUserDevicesSharingStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserDevicesStatusRequest(TeaModel):
    def __init__(
        self,
        device_action: str = None,
        device_tags: List[str] = None,
    ):
        # This parameter is required.
        self.device_action = device_action
        # This parameter is required.
        self.device_tags = device_tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_action is not None:
            result['DeviceAction'] = self.device_action
        if self.device_tags is not None:
            result['DeviceTags'] = self.device_tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceAction') is not None:
            self.device_action = m.get('DeviceAction')
        if m.get('DeviceTags') is not None:
            self.device_tags = m.get('DeviceTags')
        return self


class UpdateUserDevicesStatusResponseBodyDevices(TeaModel):
    def __init__(
        self,
        app_status: str = None,
        app_version: str = None,
        cpu: str = None,
        create_time: str = None,
        department: str = None,
        device_belong: str = None,
        device_model: str = None,
        device_status: str = None,
        device_tag: str = None,
        device_type: str = None,
        device_version: str = None,
        disk: str = None,
        dlp_status: str = None,
        hostname: str = None,
        ia_status: str = None,
        inner_ip: str = None,
        mac: str = None,
        memory: str = None,
        nac_status: str = None,
        pa_status: str = None,
        sase_user_id: str = None,
        sharing_status: bool = None,
        src_ip: str = None,
        update_time: str = None,
        username: str = None,
    ):
        self.app_status = app_status
        self.app_version = app_version
        self.cpu = cpu
        self.create_time = create_time
        self.department = department
        self.device_belong = device_belong
        self.device_model = device_model
        self.device_status = device_status
        self.device_tag = device_tag
        self.device_type = device_type
        self.device_version = device_version
        self.disk = disk
        self.dlp_status = dlp_status
        self.hostname = hostname
        self.ia_status = ia_status
        self.inner_ip = inner_ip
        self.mac = mac
        self.memory = memory
        self.nac_status = nac_status
        self.pa_status = pa_status
        self.sase_user_id = sase_user_id
        self.sharing_status = sharing_status
        self.src_ip = src_ip
        self.update_time = update_time
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_status is not None:
            result['AppStatus'] = self.app_status
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.cpu is not None:
            result['CPU'] = self.cpu
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.department is not None:
            result['Department'] = self.department
        if self.device_belong is not None:
            result['DeviceBelong'] = self.device_belong
        if self.device_model is not None:
            result['DeviceModel'] = self.device_model
        if self.device_status is not None:
            result['DeviceStatus'] = self.device_status
        if self.device_tag is not None:
            result['DeviceTag'] = self.device_tag
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.device_version is not None:
            result['DeviceVersion'] = self.device_version
        if self.disk is not None:
            result['Disk'] = self.disk
        if self.dlp_status is not None:
            result['DlpStatus'] = self.dlp_status
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.ia_status is not None:
            result['IaStatus'] = self.ia_status
        if self.inner_ip is not None:
            result['InnerIP'] = self.inner_ip
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.nac_status is not None:
            result['NacStatus'] = self.nac_status
        if self.pa_status is not None:
            result['PaStatus'] = self.pa_status
        if self.sase_user_id is not None:
            result['SaseUserId'] = self.sase_user_id
        if self.sharing_status is not None:
            result['SharingStatus'] = self.sharing_status
        if self.src_ip is not None:
            result['SrcIP'] = self.src_ip
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppStatus') is not None:
            self.app_status = m.get('AppStatus')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('CPU') is not None:
            self.cpu = m.get('CPU')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Department') is not None:
            self.department = m.get('Department')
        if m.get('DeviceBelong') is not None:
            self.device_belong = m.get('DeviceBelong')
        if m.get('DeviceModel') is not None:
            self.device_model = m.get('DeviceModel')
        if m.get('DeviceStatus') is not None:
            self.device_status = m.get('DeviceStatus')
        if m.get('DeviceTag') is not None:
            self.device_tag = m.get('DeviceTag')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('DeviceVersion') is not None:
            self.device_version = m.get('DeviceVersion')
        if m.get('Disk') is not None:
            self.disk = m.get('Disk')
        if m.get('DlpStatus') is not None:
            self.dlp_status = m.get('DlpStatus')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('IaStatus') is not None:
            self.ia_status = m.get('IaStatus')
        if m.get('InnerIP') is not None:
            self.inner_ip = m.get('InnerIP')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('NacStatus') is not None:
            self.nac_status = m.get('NacStatus')
        if m.get('PaStatus') is not None:
            self.pa_status = m.get('PaStatus')
        if m.get('SaseUserId') is not None:
            self.sase_user_id = m.get('SaseUserId')
        if m.get('SharingStatus') is not None:
            self.sharing_status = m.get('SharingStatus')
        if m.get('SrcIP') is not None:
            self.src_ip = m.get('SrcIP')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class UpdateUserDevicesStatusResponseBody(TeaModel):
    def __init__(
        self,
        devices: List[UpdateUserDevicesStatusResponseBodyDevices] = None,
        request_id: str = None,
    ):
        self.devices = devices
        self.request_id = request_id

    def validate(self):
        if self.devices:
            for k in self.devices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Devices'] = []
        if self.devices is not None:
            for k in self.devices:
                result['Devices'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.devices = []
        if m.get('Devices') is not None:
            for k in m.get('Devices'):
                temp_model = UpdateUserDevicesStatusResponseBodyDevices()
                self.devices.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateUserDevicesStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateUserDevicesStatusResponseBody = None,
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
            temp_model = UpdateUserDevicesStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserGroupRequestAttributes(TeaModel):
    def __init__(
        self,
        idp_id: int = None,
        relation: str = None,
        user_group_type: str = None,
        value: str = None,
    ):
        self.idp_id = idp_id
        # This parameter is required.
        self.relation = relation
        # This parameter is required.
        self.user_group_type = user_group_type
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.idp_id is not None:
            result['IdpId'] = self.idp_id
        if self.relation is not None:
            result['Relation'] = self.relation
        if self.user_group_type is not None:
            result['UserGroupType'] = self.user_group_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdpId') is not None:
            self.idp_id = m.get('IdpId')
        if m.get('Relation') is not None:
            self.relation = m.get('Relation')
        if m.get('UserGroupType') is not None:
            self.user_group_type = m.get('UserGroupType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateUserGroupRequest(TeaModel):
    def __init__(
        self,
        attributes: List[UpdateUserGroupRequestAttributes] = None,
        description: str = None,
        modify_type: str = None,
        user_group_id: str = None,
    ):
        self.attributes = attributes
        self.description = description
        self.modify_type = modify_type
        # This parameter is required.
        self.user_group_id = user_group_id

    def validate(self):
        if self.attributes:
            for k in self.attributes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Attributes'] = []
        if self.attributes is not None:
            for k in self.attributes:
                result['Attributes'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.modify_type is not None:
            result['ModifyType'] = self.modify_type
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attributes = []
        if m.get('Attributes') is not None:
            for k in m.get('Attributes'):
                temp_model = UpdateUserGroupRequestAttributes()
                self.attributes.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModifyType') is not None:
            self.modify_type = m.get('ModifyType')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class UpdateUserGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateUserGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateUserGroupResponseBody = None,
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
            temp_model = UpdateUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUsersStatusRequest(TeaModel):
    def __init__(
        self,
        sase_user_ids: List[str] = None,
        status: str = None,
    ):
        # This parameter is required.
        self.sase_user_ids = sase_user_ids
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sase_user_ids is not None:
            result['SaseUserIds'] = self.sase_user_ids
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SaseUserIds') is not None:
            self.sase_user_ids = m.get('SaseUserIds')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateUsersStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateUsersStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateUsersStatusResponseBody = None,
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
            temp_model = UpdateUsersStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


