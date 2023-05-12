# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class AddResolverEndpointRequestIpConfig(TeaModel):
    def __init__(
        self,
        az_id: str = None,
        cidr_block: str = None,
        ip: str = None,
        v_switch_id: str = None,
    ):
        self.az_id = az_id
        self.cidr_block = cidr_block
        self.ip = ip
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.az_id is not None:
            result['AzId'] = self.az_id
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AzId') is not None:
            self.az_id = m.get('AzId')
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class AddResolverEndpointRequest(TeaModel):
    def __init__(
        self,
        ip_config: List[AddResolverEndpointRequestIpConfig] = None,
        lang: str = None,
        name: str = None,
        security_group_id: str = None,
        vpc_id: str = None,
        vpc_region_id: str = None,
    ):
        self.ip_config = ip_config
        self.lang = lang
        self.name = name
        self.security_group_id = security_group_id
        self.vpc_id = vpc_id
        self.vpc_region_id = vpc_region_id

    def validate(self):
        if self.ip_config:
            for k in self.ip_config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['IpConfig'] = []
        if self.ip_config is not None:
            for k in self.ip_config:
                result['IpConfig'].append(k.to_map() if k else None)
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.name is not None:
            result['Name'] = self.name
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_region_id is not None:
            result['VpcRegionId'] = self.vpc_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ip_config = []
        if m.get('IpConfig') is not None:
            for k in m.get('IpConfig'):
                temp_model = AddResolverEndpointRequestIpConfig()
                self.ip_config.append(temp_model.from_map(k))
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcRegionId') is not None:
            self.vpc_region_id = m.get('VpcRegionId')
        return self


class AddResolverEndpointResponseBody(TeaModel):
    def __init__(
        self,
        endpoint_id: str = None,
        request_id: str = None,
    ):
        self.endpoint_id = endpoint_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddResolverEndpointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddResolverEndpointResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = AddResolverEndpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddResolverRuleRequestForwardIp(TeaModel):
    def __init__(
        self,
        ip: str = None,
        port: int = None,
    ):
        self.ip = ip
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class AddResolverRuleRequest(TeaModel):
    def __init__(
        self,
        endpoint_id: str = None,
        forward_ip: List[AddResolverRuleRequestForwardIp] = None,
        lang: str = None,
        name: str = None,
        type: str = None,
        zone_name: str = None,
    ):
        self.endpoint_id = endpoint_id
        self.forward_ip = forward_ip
        self.lang = lang
        self.name = name
        self.type = type
        self.zone_name = zone_name

    def validate(self):
        if self.forward_ip:
            for k in self.forward_ip:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        result['ForwardIp'] = []
        if self.forward_ip is not None:
            for k in self.forward_ip:
                result['ForwardIp'].append(k.to_map() if k else None)
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.zone_name is not None:
            result['ZoneName'] = self.zone_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        self.forward_ip = []
        if m.get('ForwardIp') is not None:
            for k in m.get('ForwardIp'):
                temp_model = AddResolverRuleRequestForwardIp()
                self.forward_ip.append(temp_model.from_map(k))
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('ZoneName') is not None:
            self.zone_name = m.get('ZoneName')
        return self


class AddResolverRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        rule_id: str = None,
    ):
        self.request_id = request_id
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class AddResolverRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddResolverRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = AddResolverRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddUserVpcAuthorizationRequest(TeaModel):
    def __init__(
        self,
        auth_channel: str = None,
        auth_code: str = None,
        auth_type: str = None,
        authorized_user_id: int = None,
    ):
        self.auth_channel = auth_channel
        self.auth_code = auth_code
        self.auth_type = auth_type
        self.authorized_user_id = authorized_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_channel is not None:
            result['AuthChannel'] = self.auth_channel
        if self.auth_code is not None:
            result['AuthCode'] = self.auth_code
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        if self.authorized_user_id is not None:
            result['AuthorizedUserId'] = self.authorized_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthChannel') is not None:
            self.auth_channel = m.get('AuthChannel')
        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('AuthorizedUserId') is not None:
            self.authorized_user_id = m.get('AuthorizedUserId')
        return self


class AddUserVpcAuthorizationResponseBody(TeaModel):
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


class AddUserVpcAuthorizationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddUserVpcAuthorizationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = AddUserVpcAuthorizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddZoneRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        proxy_pattern: str = None,
        resource_group_id: str = None,
        zone_name: str = None,
        zone_tag: str = None,
        zone_type: str = None,
    ):
        self.lang = lang
        self.proxy_pattern = proxy_pattern
        self.resource_group_id = resource_group_id
        self.zone_name = zone_name
        self.zone_tag = zone_tag
        self.zone_type = zone_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.proxy_pattern is not None:
            result['ProxyPattern'] = self.proxy_pattern
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.zone_name is not None:
            result['ZoneName'] = self.zone_name
        if self.zone_tag is not None:
            result['ZoneTag'] = self.zone_tag
        if self.zone_type is not None:
            result['ZoneType'] = self.zone_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ProxyPattern') is not None:
            self.proxy_pattern = m.get('ProxyPattern')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ZoneName') is not None:
            self.zone_name = m.get('ZoneName')
        if m.get('ZoneTag') is not None:
            self.zone_tag = m.get('ZoneTag')
        if m.get('ZoneType') is not None:
            self.zone_type = m.get('ZoneType')
        return self


class AddZoneResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        zone_id: str = None,
        zone_name: str = None,
    ):
        self.request_id = request_id
        self.success = success
        # zone ID。
        self.zone_id = zone_id
        self.zone_name = zone_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.zone_name is not None:
            result['ZoneName'] = self.zone_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ZoneName') is not None:
            self.zone_name = m.get('ZoneName')
        return self


class AddZoneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddZoneResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = AddZoneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddZoneRecordRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        priority: int = None,
        remark: str = None,
        rr: str = None,
        ttl: int = None,
        type: str = None,
        user_client_ip: str = None,
        value: str = None,
        zone_id: str = None,
    ):
        self.lang = lang
        self.priority = priority
        self.remark = remark
        self.rr = rr
        self.ttl = ttl
        self.type = type
        self.user_client_ip = user_client_ip
        self.value = value
        # Zone ID。
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.rr is not None:
            result['Rr'] = self.rr
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        if self.type is not None:
            result['Type'] = self.type
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        if self.value is not None:
            result['Value'] = self.value
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Rr') is not None:
            self.rr = m.get('Rr')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class AddZoneRecordResponseBody(TeaModel):
    def __init__(
        self,
        record_id: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.record_id = record_id
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddZoneRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddZoneRecordResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = AddZoneRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindResolverRuleVpcRequestVpc(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        vpc_id: str = None,
        vpc_type: str = None,
    ):
        self.region_id = region_id
        # vpcID
        self.vpc_id = vpc_id
        self.vpc_type = vpc_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_type is not None:
            result['VpcType'] = self.vpc_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcType') is not None:
            self.vpc_type = m.get('VpcType')
        return self


class BindResolverRuleVpcRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        rule_id: str = None,
        vpc: List[BindResolverRuleVpcRequestVpc] = None,
    ):
        self.lang = lang
        self.rule_id = rule_id
        self.vpc = vpc

    def validate(self):
        if self.vpc:
            for k in self.vpc:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        result['Vpc'] = []
        if self.vpc is not None:
            for k in self.vpc:
                result['Vpc'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        self.vpc = []
        if m.get('Vpc') is not None:
            for k in m.get('Vpc'):
                temp_model = BindResolverRuleVpcRequestVpc()
                self.vpc.append(temp_model.from_map(k))
        return self


class BindResolverRuleVpcResponseBody(TeaModel):
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


class BindResolverRuleVpcResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BindResolverRuleVpcResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = BindResolverRuleVpcResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindZoneVpcRequestVpcs(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        vpc_id: str = None,
        vpc_type: str = None,
    ):
        self.region_id = region_id
        self.vpc_id = vpc_id
        self.vpc_type = vpc_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_type is not None:
            result['VpcType'] = self.vpc_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcType') is not None:
            self.vpc_type = m.get('VpcType')
        return self


class BindZoneVpcRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        user_client_ip: str = None,
        vpcs: List[BindZoneVpcRequestVpcs] = None,
        zone_id: str = None,
    ):
        self.lang = lang
        self.user_client_ip = user_client_ip
        self.vpcs = vpcs
        self.zone_id = zone_id

    def validate(self):
        if self.vpcs:
            for k in self.vpcs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        result['Vpcs'] = []
        if self.vpcs is not None:
            for k in self.vpcs:
                result['Vpcs'].append(k.to_map() if k else None)
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        self.vpcs = []
        if m.get('Vpcs') is not None:
            for k in m.get('Vpcs'):
                temp_model = BindZoneVpcRequestVpcs()
                self.vpcs.append(temp_model.from_map(k))
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class BindZoneVpcResponseBody(TeaModel):
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


class BindZoneVpcResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BindZoneVpcResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = BindZoneVpcResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckZoneNameRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        user_client_ip: str = None,
        zone_name: str = None,
    ):
        self.lang = lang
        self.user_client_ip = user_client_ip
        self.zone_name = zone_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        if self.zone_name is not None:
            result['ZoneName'] = self.zone_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        if m.get('ZoneName') is not None:
            self.zone_name = m.get('ZoneName')
        return self


class CheckZoneNameResponseBody(TeaModel):
    def __init__(
        self,
        check: bool = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.check = check
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check is not None:
            result['Check'] = self.check
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Check') is not None:
            self.check = m.get('Check')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckZoneNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckZoneNameResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CheckZoneNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteResolverEndpointRequest(TeaModel):
    def __init__(
        self,
        endpoint_id: str = None,
        lang: str = None,
    ):
        self.endpoint_id = endpoint_id
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DeleteResolverEndpointResponseBody(TeaModel):
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


class DeleteResolverEndpointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteResolverEndpointResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteResolverEndpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteResolverRuleRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        rule_id: str = None,
    ):
        self.lang = lang
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DeleteResolverRuleResponseBody(TeaModel):
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


class DeleteResolverRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteResolverRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteResolverRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserVpcAuthorizationRequest(TeaModel):
    def __init__(
        self,
        auth_type: str = None,
        authorized_user_id: int = None,
    ):
        self.auth_type = auth_type
        self.authorized_user_id = authorized_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        if self.authorized_user_id is not None:
            result['AuthorizedUserId'] = self.authorized_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('AuthorizedUserId') is not None:
            self.authorized_user_id = m.get('AuthorizedUserId')
        return self


class DeleteUserVpcAuthorizationResponseBody(TeaModel):
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


class DeleteUserVpcAuthorizationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteUserVpcAuthorizationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteUserVpcAuthorizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteZoneRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        user_client_ip: str = None,
        zone_id: str = None,
    ):
        self.lang = lang
        self.user_client_ip = user_client_ip
        # zone ID
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DeleteZoneResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        zone_id: str = None,
    ):
        self.request_id = request_id
        # zone ID
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DeleteZoneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteZoneResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteZoneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteZoneRecordRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        record_id: int = None,
        user_client_ip: str = None,
    ):
        self.lang = lang
        self.record_id = record_id
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class DeleteZoneRecordResponseBody(TeaModel):
    def __init__(
        self,
        record_id: int = None,
        request_id: str = None,
    ):
        self.record_id = record_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteZoneRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteZoneRecordResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteZoneRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeChangeLogsRequest(TeaModel):
    def __init__(
        self,
        end_timestamp: int = None,
        entity_type: str = None,
        keyword: str = None,
        lang: str = None,
        page_number: int = None,
        page_size: int = None,
        start_timestamp: int = None,
        user_client_ip: str = None,
        zone_id: str = None,
    ):
        self.end_timestamp = end_timestamp
        self.entity_type = entity_type
        self.keyword = keyword
        self.lang = lang
        self.page_number = page_number
        self.page_size = page_size
        self.start_timestamp = start_timestamp
        self.user_client_ip = user_client_ip
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeChangeLogsResponseBodyChangeLogsChangeLog(TeaModel):
    def __init__(
        self,
        content: str = None,
        entity_id: str = None,
        entity_name: str = None,
        id: int = None,
        oper_action: str = None,
        oper_ip: str = None,
        oper_object: str = None,
        oper_time: str = None,
        oper_timestamp: int = None,
    ):
        self.content = content
        self.entity_id = entity_id
        self.entity_name = entity_name
        self.id = id
        self.oper_action = oper_action
        self.oper_ip = oper_ip
        self.oper_object = oper_object
        self.oper_time = oper_time
        self.oper_timestamp = oper_timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        if self.id is not None:
            result['Id'] = self.id
        if self.oper_action is not None:
            result['OperAction'] = self.oper_action
        if self.oper_ip is not None:
            result['OperIp'] = self.oper_ip
        if self.oper_object is not None:
            result['OperObject'] = self.oper_object
        if self.oper_time is not None:
            result['OperTime'] = self.oper_time
        if self.oper_timestamp is not None:
            result['OperTimestamp'] = self.oper_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OperAction') is not None:
            self.oper_action = m.get('OperAction')
        if m.get('OperIp') is not None:
            self.oper_ip = m.get('OperIp')
        if m.get('OperObject') is not None:
            self.oper_object = m.get('OperObject')
        if m.get('OperTime') is not None:
            self.oper_time = m.get('OperTime')
        if m.get('OperTimestamp') is not None:
            self.oper_timestamp = m.get('OperTimestamp')
        return self


class DescribeChangeLogsResponseBodyChangeLogs(TeaModel):
    def __init__(
        self,
        change_log: List[DescribeChangeLogsResponseBodyChangeLogsChangeLog] = None,
    ):
        self.change_log = change_log

    def validate(self):
        if self.change_log:
            for k in self.change_log:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ChangeLog'] = []
        if self.change_log is not None:
            for k in self.change_log:
                result['ChangeLog'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.change_log = []
        if m.get('ChangeLog') is not None:
            for k in m.get('ChangeLog'):
                temp_model = DescribeChangeLogsResponseBodyChangeLogsChangeLog()
                self.change_log.append(temp_model.from_map(k))
        return self


class DescribeChangeLogsResponseBody(TeaModel):
    def __init__(
        self,
        change_logs: DescribeChangeLogsResponseBodyChangeLogs = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_items: int = None,
        total_pages: int = None,
    ):
        self.change_logs = change_logs
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_items = total_items
        self.total_pages = total_pages

    def validate(self):
        if self.change_logs:
            self.change_logs.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_logs is not None:
            result['ChangeLogs'] = self.change_logs.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_items is not None:
            result['TotalItems'] = self.total_items
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeLogs') is not None:
            temp_model = DescribeChangeLogsResponseBodyChangeLogs()
            self.change_logs = temp_model.from_map(m['ChangeLogs'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItems') is not None:
            self.total_items = m.get('TotalItems')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        return self


class DescribeChangeLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeChangeLogsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeChangeLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        authorized_user_id: int = None,
        lang: str = None,
        user_client_ip: str = None,
        vpc_type: str = None,
    ):
        self.accept_language = accept_language
        self.authorized_user_id = authorized_user_id
        self.lang = lang
        self.user_client_ip = user_client_ip
        self.vpc_type = vpc_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.authorized_user_id is not None:
            result['AuthorizedUserId'] = self.authorized_user_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        if self.vpc_type is not None:
            result['VpcType'] = self.vpc_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('AuthorizedUserId') is not None:
            self.authorized_user_id = m.get('AuthorizedUserId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        if m.get('VpcType') is not None:
            self.vpc_type = m.get('VpcType')
        return self


class DescribeRegionsResponseBodyRegionsRegion(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        region_endpoint: str = None,
        region_id: str = None,
        region_name: str = None,
    ):
        self.local_name = local_name
        self.region_endpoint = region_endpoint
        self.region_id = region_id
        self.region_name = region_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        region: List[DescribeRegionsResponseBodyRegionsRegion] = None,
    ):
        self.region = region

    def validate(self):
        if self.region:
            for k in self.region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Region'] = []
        if self.region is not None:
            for k in self.region:
                result['Region'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region = []
        if m.get('Region') is not None:
            for k in m.get('Region'):
                temp_model = DescribeRegionsResponseBodyRegionsRegion()
                self.region.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        regions: DescribeRegionsResponseBodyRegions = None,
        request_id: str = None,
    ):
        self.regions = regions
        self.request_id = request_id

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Regions') is not None:
            temp_model = DescribeRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRegionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRequestGraphRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_type: str = None,
        end_timestamp: int = None,
        lang: str = None,
        start_timestamp: int = None,
        user_client_ip: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        self.biz_id = biz_id
        self.biz_type = biz_type
        self.end_timestamp = end_timestamp
        self.lang = lang
        self.start_timestamp = start_timestamp
        self.user_client_ip = user_client_ip
        # VPC ID
        self.vpc_id = vpc_id
        # zone ID
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeRequestGraphResponseBodyRequestDetailsZoneRequestTop(TeaModel):
    def __init__(
        self,
        request_count: int = None,
        time: str = None,
        timestamp: int = None,
    ):
        self.request_count = request_count
        self.time = time
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_count is not None:
            result['RequestCount'] = self.request_count
        if self.time is not None:
            result['Time'] = self.time
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestCount') is not None:
            self.request_count = m.get('RequestCount')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class DescribeRequestGraphResponseBodyRequestDetails(TeaModel):
    def __init__(
        self,
        zone_request_top: List[DescribeRequestGraphResponseBodyRequestDetailsZoneRequestTop] = None,
    ):
        self.zone_request_top = zone_request_top

    def validate(self):
        if self.zone_request_top:
            for k in self.zone_request_top:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ZoneRequestTop'] = []
        if self.zone_request_top is not None:
            for k in self.zone_request_top:
                result['ZoneRequestTop'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.zone_request_top = []
        if m.get('ZoneRequestTop') is not None:
            for k in m.get('ZoneRequestTop'):
                temp_model = DescribeRequestGraphResponseBodyRequestDetailsZoneRequestTop()
                self.zone_request_top.append(temp_model.from_map(k))
        return self


class DescribeRequestGraphResponseBody(TeaModel):
    def __init__(
        self,
        request_details: DescribeRequestGraphResponseBodyRequestDetails = None,
        request_id: str = None,
    ):
        self.request_details = request_details
        self.request_id = request_id

    def validate(self):
        if self.request_details:
            self.request_details.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_details is not None:
            result['RequestDetails'] = self.request_details.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestDetails') is not None:
            temp_model = DescribeRequestGraphResponseBodyRequestDetails()
            self.request_details = temp_model.from_map(m['RequestDetails'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRequestGraphResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRequestGraphResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeRequestGraphResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeResolverAvailableZonesRequest(TeaModel):
    def __init__(
        self,
        az_id: str = None,
        lang: str = None,
        resolver_region_id: str = None,
    ):
        self.az_id = az_id
        self.lang = lang
        self.resolver_region_id = resolver_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.az_id is not None:
            result['AzId'] = self.az_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resolver_region_id is not None:
            result['ResolverRegionId'] = self.resolver_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AzId') is not None:
            self.az_id = m.get('AzId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResolverRegionId') is not None:
            self.resolver_region_id = m.get('ResolverRegionId')
        return self


class DescribeResolverAvailableZonesResponseBodyAvailableZones(TeaModel):
    def __init__(
        self,
        az_id: str = None,
        status: str = None,
    ):
        self.az_id = az_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.az_id is not None:
            result['AzId'] = self.az_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AzId') is not None:
            self.az_id = m.get('AzId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeResolverAvailableZonesResponseBody(TeaModel):
    def __init__(
        self,
        available_zones: List[DescribeResolverAvailableZonesResponseBodyAvailableZones] = None,
        request_id: str = None,
    ):
        self.available_zones = available_zones
        self.request_id = request_id

    def validate(self):
        if self.available_zones:
            for k in self.available_zones:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AvailableZones'] = []
        if self.available_zones is not None:
            for k in self.available_zones:
                result['AvailableZones'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.available_zones = []
        if m.get('AvailableZones') is not None:
            for k in m.get('AvailableZones'):
                temp_model = DescribeResolverAvailableZonesResponseBodyAvailableZones()
                self.available_zones.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeResolverAvailableZonesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeResolverAvailableZonesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeResolverAvailableZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeResolverEndpointRequest(TeaModel):
    def __init__(
        self,
        endpoint_id: str = None,
        lang: str = None,
    ):
        self.endpoint_id = endpoint_id
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeResolverEndpointResponseBodyIpConfigs(TeaModel):
    def __init__(
        self,
        az_id: str = None,
        cidr_block: str = None,
        ip: str = None,
        v_switch_id: str = None,
    ):
        self.az_id = az_id
        self.cidr_block = cidr_block
        self.ip = ip
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.az_id is not None:
            result['AzId'] = self.az_id
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AzId') is not None:
            self.az_id = m.get('AzId')
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class DescribeResolverEndpointResponseBody(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        create_timestamp: int = None,
        id: str = None,
        ip_configs: List[DescribeResolverEndpointResponseBodyIpConfigs] = None,
        name: str = None,
        request_id: str = None,
        security_group_id: str = None,
        status: str = None,
        update_time: str = None,
        update_timestamp: int = None,
        vpc_id: str = None,
        vpc_name: str = None,
        vpc_region_id: str = None,
        vpc_region_name: str = None,
    ):
        self.create_time = create_time
        self.create_timestamp = create_timestamp
        self.id = id
        self.ip_configs = ip_configs
        self.name = name
        self.request_id = request_id
        self.security_group_id = security_group_id
        self.status = status
        self.update_time = update_time
        self.update_timestamp = update_timestamp
        self.vpc_id = vpc_id
        self.vpc_name = vpc_name
        self.vpc_region_id = vpc_region_id
        self.vpc_region_name = vpc_region_name

    def validate(self):
        if self.ip_configs:
            for k in self.ip_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        if self.id is not None:
            result['Id'] = self.id
        result['IpConfigs'] = []
        if self.ip_configs is not None:
            for k in self.ip_configs:
                result['IpConfigs'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.update_timestamp is not None:
            result['UpdateTimestamp'] = self.update_timestamp
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name
        if self.vpc_region_id is not None:
            result['VpcRegionId'] = self.vpc_region_id
        if self.vpc_region_name is not None:
            result['VpcRegionName'] = self.vpc_region_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        self.ip_configs = []
        if m.get('IpConfigs') is not None:
            for k in m.get('IpConfigs'):
                temp_model = DescribeResolverEndpointResponseBodyIpConfigs()
                self.ip_configs.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')
        if m.get('VpcRegionId') is not None:
            self.vpc_region_id = m.get('VpcRegionId')
        if m.get('VpcRegionName') is not None:
            self.vpc_region_name = m.get('VpcRegionName')
        return self


class DescribeResolverEndpointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeResolverEndpointResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeResolverEndpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeResolverEndpointsRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        lang: str = None,
        page_number: int = None,
        page_size: int = None,
        status: str = None,
    ):
        self.keyword = keyword
        self.lang = lang
        self.page_number = page_number
        self.page_size = page_size
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeResolverEndpointsResponseBodyEndpointsIpConfigs(TeaModel):
    def __init__(
        self,
        az_id: str = None,
        cidr_block: str = None,
        ip: str = None,
        v_switch_id: str = None,
    ):
        self.az_id = az_id
        self.cidr_block = cidr_block
        self.ip = ip
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.az_id is not None:
            result['AzId'] = self.az_id
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AzId') is not None:
            self.az_id = m.get('AzId')
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class DescribeResolverEndpointsResponseBodyEndpoints(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        create_timestamp: int = None,
        id: str = None,
        ip_configs: List[DescribeResolverEndpointsResponseBodyEndpointsIpConfigs] = None,
        name: str = None,
        security_group_id: str = None,
        status: str = None,
        update_time: str = None,
        update_timestamp: int = None,
        vpc_id: str = None,
        vpc_name: str = None,
        vpc_region_id: str = None,
        vpc_region_name: str = None,
    ):
        self.create_time = create_time
        self.create_timestamp = create_timestamp
        self.id = id
        self.ip_configs = ip_configs
        self.name = name
        self.security_group_id = security_group_id
        self.status = status
        self.update_time = update_time
        self.update_timestamp = update_timestamp
        self.vpc_id = vpc_id
        self.vpc_name = vpc_name
        self.vpc_region_id = vpc_region_id
        self.vpc_region_name = vpc_region_name

    def validate(self):
        if self.ip_configs:
            for k in self.ip_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        if self.id is not None:
            result['Id'] = self.id
        result['IpConfigs'] = []
        if self.ip_configs is not None:
            for k in self.ip_configs:
                result['IpConfigs'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.update_timestamp is not None:
            result['UpdateTimestamp'] = self.update_timestamp
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name
        if self.vpc_region_id is not None:
            result['VpcRegionId'] = self.vpc_region_id
        if self.vpc_region_name is not None:
            result['VpcRegionName'] = self.vpc_region_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        self.ip_configs = []
        if m.get('IpConfigs') is not None:
            for k in m.get('IpConfigs'):
                temp_model = DescribeResolverEndpointsResponseBodyEndpointsIpConfigs()
                self.ip_configs.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')
        if m.get('VpcRegionId') is not None:
            self.vpc_region_id = m.get('VpcRegionId')
        if m.get('VpcRegionName') is not None:
            self.vpc_region_name = m.get('VpcRegionName')
        return self


class DescribeResolverEndpointsResponseBody(TeaModel):
    def __init__(
        self,
        endpoints: List[DescribeResolverEndpointsResponseBodyEndpoints] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_items: int = None,
        total_pages: int = None,
    ):
        self.endpoints = endpoints
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_items = total_items
        self.total_pages = total_pages

    def validate(self):
        if self.endpoints:
            for k in self.endpoints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Endpoints'] = []
        if self.endpoints is not None:
            for k in self.endpoints:
                result['Endpoints'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_items is not None:
            result['TotalItems'] = self.total_items
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.endpoints = []
        if m.get('Endpoints') is not None:
            for k in m.get('Endpoints'):
                temp_model = DescribeResolverEndpointsResponseBodyEndpoints()
                self.endpoints.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItems') is not None:
            self.total_items = m.get('TotalItems')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        return self


class DescribeResolverEndpointsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeResolverEndpointsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeResolverEndpointsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeResolverRuleRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        rule_id: str = None,
    ):
        self.lang = lang
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DescribeResolverRuleResponseBodyBindVpcs(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        region_name: str = None,
        vpc_id: str = None,
        vpc_name: str = None,
        vpc_type: str = None,
    ):
        self.region_id = region_id
        self.region_name = region_name
        # Vpc ID
        self.vpc_id = vpc_id
        self.vpc_name = vpc_name
        self.vpc_type = vpc_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name
        if self.vpc_type is not None:
            result['VpcType'] = self.vpc_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')
        if m.get('VpcType') is not None:
            self.vpc_type = m.get('VpcType')
        return self


class DescribeResolverRuleResponseBodyForwardIps(TeaModel):
    def __init__(
        self,
        ip: str = None,
        port: int = None,
    ):
        self.ip = ip
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class DescribeResolverRuleResponseBody(TeaModel):
    def __init__(
        self,
        bind_vpcs: List[DescribeResolverRuleResponseBodyBindVpcs] = None,
        create_time: str = None,
        create_timestamp: int = None,
        endpoint_id: str = None,
        endpoint_name: str = None,
        forward_ips: List[DescribeResolverRuleResponseBodyForwardIps] = None,
        id: str = None,
        name: str = None,
        request_id: str = None,
        type: str = None,
        update_time: str = None,
        update_timestamp: int = None,
        zone_name: str = None,
    ):
        self.bind_vpcs = bind_vpcs
        self.create_time = create_time
        self.create_timestamp = create_timestamp
        self.endpoint_id = endpoint_id
        self.endpoint_name = endpoint_name
        self.forward_ips = forward_ips
        self.id = id
        self.name = name
        self.request_id = request_id
        self.type = type
        self.update_time = update_time
        self.update_timestamp = update_timestamp
        self.zone_name = zone_name

    def validate(self):
        if self.bind_vpcs:
            for k in self.bind_vpcs:
                if k:
                    k.validate()
        if self.forward_ips:
            for k in self.forward_ips:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BindVpcs'] = []
        if self.bind_vpcs is not None:
            for k in self.bind_vpcs:
                result['BindVpcs'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.endpoint_name is not None:
            result['EndpointName'] = self.endpoint_name
        result['ForwardIps'] = []
        if self.forward_ips is not None:
            for k in self.forward_ips:
                result['ForwardIps'].append(k.to_map() if k else None)
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.update_timestamp is not None:
            result['UpdateTimestamp'] = self.update_timestamp
        if self.zone_name is not None:
            result['ZoneName'] = self.zone_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bind_vpcs = []
        if m.get('BindVpcs') is not None:
            for k in m.get('BindVpcs'):
                temp_model = DescribeResolverRuleResponseBodyBindVpcs()
                self.bind_vpcs.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('EndpointName') is not None:
            self.endpoint_name = m.get('EndpointName')
        self.forward_ips = []
        if m.get('ForwardIps') is not None:
            for k in m.get('ForwardIps'):
                temp_model = DescribeResolverRuleResponseBodyForwardIps()
                self.forward_ips.append(temp_model.from_map(k))
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')
        if m.get('ZoneName') is not None:
            self.zone_name = m.get('ZoneName')
        return self


class DescribeResolverRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeResolverRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeResolverRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeResolverRulesRequest(TeaModel):
    def __init__(
        self,
        endpoint_id: str = None,
        keyword: str = None,
        lang: str = None,
        need_detail_attributes: bool = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.endpoint_id = endpoint_id
        self.keyword = keyword
        self.lang = lang
        self.need_detail_attributes = need_detail_attributes
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.need_detail_attributes is not None:
            result['NeedDetailAttributes'] = self.need_detail_attributes
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('NeedDetailAttributes') is not None:
            self.need_detail_attributes = m.get('NeedDetailAttributes')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeResolverRulesResponseBodyRulesBindVpcs(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        region_name: str = None,
        vpc_id: str = None,
        vpc_name: str = None,
        vpc_type: str = None,
    ):
        self.region_id = region_id
        self.region_name = region_name
        # VPC ID
        self.vpc_id = vpc_id
        self.vpc_name = vpc_name
        self.vpc_type = vpc_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name
        if self.vpc_type is not None:
            result['VpcType'] = self.vpc_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')
        if m.get('VpcType') is not None:
            self.vpc_type = m.get('VpcType')
        return self


class DescribeResolverRulesResponseBodyRulesForwardIps(TeaModel):
    def __init__(
        self,
        ip: str = None,
        port: int = None,
    ):
        self.ip = ip
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class DescribeResolverRulesResponseBodyRules(TeaModel):
    def __init__(
        self,
        bind_vpcs: List[DescribeResolverRulesResponseBodyRulesBindVpcs] = None,
        create_time: str = None,
        create_timestamp: int = None,
        endpoint_id: str = None,
        endpoint_name: str = None,
        forward_ips: List[DescribeResolverRulesResponseBodyRulesForwardIps] = None,
        id: str = None,
        name: str = None,
        type: str = None,
        update_time: str = None,
        update_timestamp: int = None,
        zone_name: str = None,
    ):
        self.bind_vpcs = bind_vpcs
        self.create_time = create_time
        self.create_timestamp = create_timestamp
        self.endpoint_id = endpoint_id
        self.endpoint_name = endpoint_name
        self.forward_ips = forward_ips
        self.id = id
        self.name = name
        self.type = type
        self.update_time = update_time
        self.update_timestamp = update_timestamp
        self.zone_name = zone_name

    def validate(self):
        if self.bind_vpcs:
            for k in self.bind_vpcs:
                if k:
                    k.validate()
        if self.forward_ips:
            for k in self.forward_ips:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BindVpcs'] = []
        if self.bind_vpcs is not None:
            for k in self.bind_vpcs:
                result['BindVpcs'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.endpoint_name is not None:
            result['EndpointName'] = self.endpoint_name
        result['ForwardIps'] = []
        if self.forward_ips is not None:
            for k in self.forward_ips:
                result['ForwardIps'].append(k.to_map() if k else None)
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.update_timestamp is not None:
            result['UpdateTimestamp'] = self.update_timestamp
        if self.zone_name is not None:
            result['ZoneName'] = self.zone_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bind_vpcs = []
        if m.get('BindVpcs') is not None:
            for k in m.get('BindVpcs'):
                temp_model = DescribeResolverRulesResponseBodyRulesBindVpcs()
                self.bind_vpcs.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('EndpointName') is not None:
            self.endpoint_name = m.get('EndpointName')
        self.forward_ips = []
        if m.get('ForwardIps') is not None:
            for k in m.get('ForwardIps'):
                temp_model = DescribeResolverRulesResponseBodyRulesForwardIps()
                self.forward_ips.append(temp_model.from_map(k))
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')
        if m.get('ZoneName') is not None:
            self.zone_name = m.get('ZoneName')
        return self


class DescribeResolverRulesResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        rules: List[DescribeResolverRulesResponseBodyRules] = None,
        total_items: int = None,
        total_pages: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.rules = rules
        self.total_items = total_items
        self.total_pages = total_pages

    def validate(self):
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        if self.total_items is not None:
            result['TotalItems'] = self.total_items
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = DescribeResolverRulesResponseBodyRules()
                self.rules.append(temp_model.from_map(k))
        if m.get('TotalItems') is not None:
            self.total_items = m.get('TotalItems')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        return self


class DescribeResolverRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeResolverRulesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeResolverRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeStatisticSummaryRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        user_client_ip: str = None,
    ):
        self.lang = lang
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class DescribeStatisticSummaryResponseBodyVpcRequestTopsVpcRequestTop(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        region_name: str = None,
        request_count: int = None,
        tunnel_id: str = None,
        vpc_id: str = None,
        vpc_type: str = None,
    ):
        self.region_id = region_id
        self.region_name = region_name
        self.request_count = request_count
        self.tunnel_id = tunnel_id
        # VPC ID
        self.vpc_id = vpc_id
        self.vpc_type = vpc_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.request_count is not None:
            result['RequestCount'] = self.request_count
        if self.tunnel_id is not None:
            result['TunnelId'] = self.tunnel_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_type is not None:
            result['VpcType'] = self.vpc_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('RequestCount') is not None:
            self.request_count = m.get('RequestCount')
        if m.get('TunnelId') is not None:
            self.tunnel_id = m.get('TunnelId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcType') is not None:
            self.vpc_type = m.get('VpcType')
        return self


class DescribeStatisticSummaryResponseBodyVpcRequestTops(TeaModel):
    def __init__(
        self,
        vpc_request_top: List[DescribeStatisticSummaryResponseBodyVpcRequestTopsVpcRequestTop] = None,
    ):
        self.vpc_request_top = vpc_request_top

    def validate(self):
        if self.vpc_request_top:
            for k in self.vpc_request_top:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['VpcRequestTop'] = []
        if self.vpc_request_top is not None:
            for k in self.vpc_request_top:
                result['VpcRequestTop'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.vpc_request_top = []
        if m.get('VpcRequestTop') is not None:
            for k in m.get('VpcRequestTop'):
                temp_model = DescribeStatisticSummaryResponseBodyVpcRequestTopsVpcRequestTop()
                self.vpc_request_top.append(temp_model.from_map(k))
        return self


class DescribeStatisticSummaryResponseBodyZoneRequestTopsZoneRequestTop(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        request_count: int = None,
        zone_name: str = None,
    ):
        self.biz_type = biz_type
        self.request_count = request_count
        self.zone_name = zone_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.request_count is not None:
            result['RequestCount'] = self.request_count
        if self.zone_name is not None:
            result['ZoneName'] = self.zone_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('RequestCount') is not None:
            self.request_count = m.get('RequestCount')
        if m.get('ZoneName') is not None:
            self.zone_name = m.get('ZoneName')
        return self


class DescribeStatisticSummaryResponseBodyZoneRequestTops(TeaModel):
    def __init__(
        self,
        zone_request_top: List[DescribeStatisticSummaryResponseBodyZoneRequestTopsZoneRequestTop] = None,
    ):
        self.zone_request_top = zone_request_top

    def validate(self):
        if self.zone_request_top:
            for k in self.zone_request_top:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ZoneRequestTop'] = []
        if self.zone_request_top is not None:
            for k in self.zone_request_top:
                result['ZoneRequestTop'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.zone_request_top = []
        if m.get('ZoneRequestTop') is not None:
            for k in m.get('ZoneRequestTop'):
                temp_model = DescribeStatisticSummaryResponseBodyZoneRequestTopsZoneRequestTop()
                self.zone_request_top.append(temp_model.from_map(k))
        return self


class DescribeStatisticSummaryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        vpc_request_tops: DescribeStatisticSummaryResponseBodyVpcRequestTops = None,
        zone_request_tops: DescribeStatisticSummaryResponseBodyZoneRequestTops = None,
    ):
        self.request_id = request_id
        self.total_count = total_count
        self.vpc_request_tops = vpc_request_tops
        self.zone_request_tops = zone_request_tops

    def validate(self):
        if self.vpc_request_tops:
            self.vpc_request_tops.validate()
        if self.zone_request_tops:
            self.zone_request_tops.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.vpc_request_tops is not None:
            result['VpcRequestTops'] = self.vpc_request_tops.to_map()
        if self.zone_request_tops is not None:
            result['ZoneRequestTops'] = self.zone_request_tops.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('VpcRequestTops') is not None:
            temp_model = DescribeStatisticSummaryResponseBodyVpcRequestTops()
            self.vpc_request_tops = temp_model.from_map(m['VpcRequestTops'])
        if m.get('ZoneRequestTops') is not None:
            temp_model = DescribeStatisticSummaryResponseBodyZoneRequestTops()
            self.zone_request_tops = temp_model.from_map(m['ZoneRequestTops'])
        return self


class DescribeStatisticSummaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeStatisticSummaryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeStatisticSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSyncEcsHostTaskRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        zone_id: str = None,
    ):
        self.lang = lang
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeSyncEcsHostTaskResponseBodyEcsRegionsEcsRegionRegionIds(TeaModel):
    def __init__(
        self,
        region_id: List[str] = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeSyncEcsHostTaskResponseBodyEcsRegionsEcsRegion(TeaModel):
    def __init__(
        self,
        region_ids: DescribeSyncEcsHostTaskResponseBodyEcsRegionsEcsRegionRegionIds = None,
        user_id: int = None,
    ):
        self.region_ids = region_ids
        self.user_id = user_id

    def validate(self):
        if self.region_ids:
            self.region_ids.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids.to_map()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionIds') is not None:
            temp_model = DescribeSyncEcsHostTaskResponseBodyEcsRegionsEcsRegionRegionIds()
            self.region_ids = temp_model.from_map(m['RegionIds'])
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeSyncEcsHostTaskResponseBodyEcsRegions(TeaModel):
    def __init__(
        self,
        ecs_region: List[DescribeSyncEcsHostTaskResponseBodyEcsRegionsEcsRegion] = None,
    ):
        self.ecs_region = ecs_region

    def validate(self):
        if self.ecs_region:
            for k in self.ecs_region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EcsRegion'] = []
        if self.ecs_region is not None:
            for k in self.ecs_region:
                result['EcsRegion'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ecs_region = []
        if m.get('EcsRegion') is not None:
            for k in m.get('EcsRegion'):
                temp_model = DescribeSyncEcsHostTaskResponseBodyEcsRegionsEcsRegion()
                self.ecs_region.append(temp_model.from_map(k))
        return self


class DescribeSyncEcsHostTaskResponseBodyRegions(TeaModel):
    def __init__(
        self,
        region_id: List[str] = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeSyncEcsHostTaskResponseBody(TeaModel):
    def __init__(
        self,
        ecs_regions: DescribeSyncEcsHostTaskResponseBodyEcsRegions = None,
        regions: DescribeSyncEcsHostTaskResponseBodyRegions = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
        zone_id: str = None,
    ):
        self.ecs_regions = ecs_regions
        self.regions = regions
        self.request_id = request_id
        self.status = status
        self.success = success
        self.zone_id = zone_id

    def validate(self):
        if self.ecs_regions:
            self.ecs_regions.validate()
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ecs_regions is not None:
            result['EcsRegions'] = self.ecs_regions.to_map()
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EcsRegions') is not None:
            temp_model = DescribeSyncEcsHostTaskResponseBodyEcsRegions()
            self.ecs_regions = temp_model.from_map(m['EcsRegions'])
        if m.get('Regions') is not None:
            temp_model = DescribeSyncEcsHostTaskResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeSyncEcsHostTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSyncEcsHostTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeSyncEcsHostTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTagsRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_type: str = None,
    ):
        self.lang = lang
        self.page_number = page_number
        self.page_size = page_size
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class DescribeTagsResponseBodyTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        values: List[str] = None,
    ):
        self.key = key
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class DescribeTagsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        tags: List[DescribeTagsResponseBodyTags] = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.tags = tags
        self.total_count = total_count

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
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
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
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeTagsResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTagsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserVpcAuthorizationsRequest(TeaModel):
    def __init__(
        self,
        auth_type: str = None,
        authorized_user_id: int = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.auth_type = auth_type
        self.authorized_user_id = authorized_user_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        if self.authorized_user_id is not None:
            result['AuthorizedUserId'] = self.authorized_user_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('AuthorizedUserId') is not None:
            self.authorized_user_id = m.get('AuthorizedUserId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeUserVpcAuthorizationsResponseBodyUsers(TeaModel):
    def __init__(
        self,
        auth_type: str = None,
        authorized_aliyun_id: str = None,
        authorized_user_id: int = None,
    ):
        self.auth_type = auth_type
        self.authorized_aliyun_id = authorized_aliyun_id
        self.authorized_user_id = authorized_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        if self.authorized_aliyun_id is not None:
            result['AuthorizedAliyunId'] = self.authorized_aliyun_id
        if self.authorized_user_id is not None:
            result['AuthorizedUserId'] = self.authorized_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('AuthorizedAliyunId') is not None:
            self.authorized_aliyun_id = m.get('AuthorizedAliyunId')
        if m.get('AuthorizedUserId') is not None:
            self.authorized_user_id = m.get('AuthorizedUserId')
        return self


class DescribeUserVpcAuthorizationsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_items: int = None,
        total_pages: int = None,
        users: List[DescribeUserVpcAuthorizationsResponseBodyUsers] = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_items = total_items
        self.total_pages = total_pages
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
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_items is not None:
            result['TotalItems'] = self.total_items
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        result['Users'] = []
        if self.users is not None:
            for k in self.users:
                result['Users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItems') is not None:
            self.total_items = m.get('TotalItems')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        self.users = []
        if m.get('Users') is not None:
            for k in m.get('Users'):
                temp_model = DescribeUserVpcAuthorizationsResponseBodyUsers()
                self.users.append(temp_model.from_map(k))
        return self


class DescribeUserVpcAuthorizationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeUserVpcAuthorizationsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeUserVpcAuthorizationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeZoneInfoRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        zone_id: str = None,
    ):
        self.lang = lang
        # Zone ID。
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeZoneInfoResponseBodyBindVpcsVpc(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        region_name: str = None,
        vpc_id: str = None,
        vpc_name: str = None,
        vpc_type: str = None,
        vpc_user_id: int = None,
    ):
        self.region_id = region_id
        self.region_name = region_name
        # Vpc ID。
        self.vpc_id = vpc_id
        self.vpc_name = vpc_name
        self.vpc_type = vpc_type
        self.vpc_user_id = vpc_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name
        if self.vpc_type is not None:
            result['VpcType'] = self.vpc_type
        if self.vpc_user_id is not None:
            result['VpcUserId'] = self.vpc_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')
        if m.get('VpcType') is not None:
            self.vpc_type = m.get('VpcType')
        if m.get('VpcUserId') is not None:
            self.vpc_user_id = m.get('VpcUserId')
        return self


class DescribeZoneInfoResponseBodyBindVpcs(TeaModel):
    def __init__(
        self,
        vpc: List[DescribeZoneInfoResponseBodyBindVpcsVpc] = None,
    ):
        self.vpc = vpc

    def validate(self):
        if self.vpc:
            for k in self.vpc:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Vpc'] = []
        if self.vpc is not None:
            for k in self.vpc:
                result['Vpc'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.vpc = []
        if m.get('Vpc') is not None:
            for k in m.get('Vpc'):
                temp_model = DescribeZoneInfoResponseBodyBindVpcsVpc()
                self.vpc.append(temp_model.from_map(k))
        return self


class DescribeZoneInfoResponseBody(TeaModel):
    def __init__(
        self,
        bind_vpcs: DescribeZoneInfoResponseBodyBindVpcs = None,
        create_time: str = None,
        create_timestamp: int = None,
        is_ptr: bool = None,
        proxy_pattern: str = None,
        record_count: int = None,
        remark: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        slave_dns: bool = None,
        update_time: str = None,
        update_timestamp: int = None,
        zone_id: str = None,
        zone_name: str = None,
        zone_tag: str = None,
        zone_type: str = None,
    ):
        self.bind_vpcs = bind_vpcs
        self.create_time = create_time
        self.create_timestamp = create_timestamp
        self.is_ptr = is_ptr
        self.proxy_pattern = proxy_pattern
        self.record_count = record_count
        self.remark = remark
        self.request_id = request_id
        self.resource_group_id = resource_group_id
        self.slave_dns = slave_dns
        self.update_time = update_time
        self.update_timestamp = update_timestamp
        # Zone ID。
        self.zone_id = zone_id
        self.zone_name = zone_name
        self.zone_tag = zone_tag
        self.zone_type = zone_type

    def validate(self):
        if self.bind_vpcs:
            self.bind_vpcs.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bind_vpcs is not None:
            result['BindVpcs'] = self.bind_vpcs.to_map()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        if self.is_ptr is not None:
            result['IsPtr'] = self.is_ptr
        if self.proxy_pattern is not None:
            result['ProxyPattern'] = self.proxy_pattern
        if self.record_count is not None:
            result['RecordCount'] = self.record_count
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.slave_dns is not None:
            result['SlaveDns'] = self.slave_dns
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.update_timestamp is not None:
            result['UpdateTimestamp'] = self.update_timestamp
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.zone_name is not None:
            result['ZoneName'] = self.zone_name
        if self.zone_tag is not None:
            result['ZoneTag'] = self.zone_tag
        if self.zone_type is not None:
            result['ZoneType'] = self.zone_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindVpcs') is not None:
            temp_model = DescribeZoneInfoResponseBodyBindVpcs()
            self.bind_vpcs = temp_model.from_map(m['BindVpcs'])
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        if m.get('IsPtr') is not None:
            self.is_ptr = m.get('IsPtr')
        if m.get('ProxyPattern') is not None:
            self.proxy_pattern = m.get('ProxyPattern')
        if m.get('RecordCount') is not None:
            self.record_count = m.get('RecordCount')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SlaveDns') is not None:
            self.slave_dns = m.get('SlaveDns')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ZoneName') is not None:
            self.zone_name = m.get('ZoneName')
        if m.get('ZoneTag') is not None:
            self.zone_tag = m.get('ZoneTag')
        if m.get('ZoneType') is not None:
            self.zone_type = m.get('ZoneType')
        return self


class DescribeZoneInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeZoneInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeZoneInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeZoneRecordsRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        lang: str = None,
        page_number: int = None,
        page_size: int = None,
        search_mode: str = None,
        tag: str = None,
        user_client_ip: str = None,
        zone_id: str = None,
    ):
        self.keyword = keyword
        self.lang = lang
        self.page_number = page_number
        self.page_size = page_size
        self.search_mode = search_mode
        self.tag = tag
        self.user_client_ip = user_client_ip
        # Zone ID。
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_mode is not None:
            result['SearchMode'] = self.search_mode
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchMode') is not None:
            self.search_mode = m.get('SearchMode')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeZoneRecordsResponseBodyRecordsRecord(TeaModel):
    def __init__(
        self,
        priority: int = None,
        record_id: int = None,
        remark: str = None,
        rr: str = None,
        status: str = None,
        ttl: int = None,
        type: str = None,
        value: str = None,
    ):
        self.priority = priority
        self.record_id = record_id
        self.remark = remark
        self.rr = rr
        self.status = status
        self.ttl = ttl
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.rr is not None:
            result['Rr'] = self.rr
        if self.status is not None:
            result['Status'] = self.status
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Rr') is not None:
            self.rr = m.get('Rr')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeZoneRecordsResponseBodyRecords(TeaModel):
    def __init__(
        self,
        record: List[DescribeZoneRecordsResponseBodyRecordsRecord] = None,
    ):
        self.record = record

    def validate(self):
        if self.record:
            for k in self.record:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Record'] = []
        if self.record is not None:
            for k in self.record:
                result['Record'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.record = []
        if m.get('Record') is not None:
            for k in m.get('Record'):
                temp_model = DescribeZoneRecordsResponseBodyRecordsRecord()
                self.record.append(temp_model.from_map(k))
        return self


class DescribeZoneRecordsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        records: DescribeZoneRecordsResponseBodyRecords = None,
        request_id: str = None,
        total_items: int = None,
        total_pages: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.records = records
        self.request_id = request_id
        self.total_items = total_items
        self.total_pages = total_pages

    def validate(self):
        if self.records:
            self.records.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.records is not None:
            result['Records'] = self.records.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_items is not None:
            result['TotalItems'] = self.total_items
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Records') is not None:
            temp_model = DescribeZoneRecordsResponseBodyRecords()
            self.records = temp_model.from_map(m['Records'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItems') is not None:
            self.total_items = m.get('TotalItems')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        return self


class DescribeZoneRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeZoneRecordsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeZoneRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeZoneVpcTreeRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        user_client_ip: str = None,
    ):
        self.lang = lang
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class DescribeZoneVpcTreeResponseBodyZonesZoneVpcsVpc(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        region_name: str = None,
        vpc_id: str = None,
        vpc_name: str = None,
        vpc_type: str = None,
    ):
        # region Id
        self.region_id = region_id
        self.region_name = region_name
        # vpc id
        self.vpc_id = vpc_id
        self.vpc_name = vpc_name
        self.vpc_type = vpc_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name
        if self.vpc_type is not None:
            result['VpcType'] = self.vpc_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')
        if m.get('VpcType') is not None:
            self.vpc_type = m.get('VpcType')
        return self


class DescribeZoneVpcTreeResponseBodyZonesZoneVpcs(TeaModel):
    def __init__(
        self,
        vpc: List[DescribeZoneVpcTreeResponseBodyZonesZoneVpcsVpc] = None,
    ):
        self.vpc = vpc

    def validate(self):
        if self.vpc:
            for k in self.vpc:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Vpc'] = []
        if self.vpc is not None:
            for k in self.vpc:
                result['Vpc'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.vpc = []
        if m.get('Vpc') is not None:
            for k in m.get('Vpc'):
                temp_model = DescribeZoneVpcTreeResponseBodyZonesZoneVpcsVpc()
                self.vpc.append(temp_model.from_map(k))
        return self


class DescribeZoneVpcTreeResponseBodyZonesZone(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        create_timestamp: int = None,
        is_ptr: bool = None,
        record_count: int = None,
        remark: str = None,
        update_time: str = None,
        update_timestamp: int = None,
        vpcs: DescribeZoneVpcTreeResponseBodyZonesZoneVpcs = None,
        zone_id: str = None,
        zone_name: str = None,
        zone_tag: str = None,
        zone_type: str = None,
    ):
        self.create_time = create_time
        self.create_timestamp = create_timestamp
        self.is_ptr = is_ptr
        self.record_count = record_count
        self.remark = remark
        self.update_time = update_time
        self.update_timestamp = update_timestamp
        self.vpcs = vpcs
        # Zone id
        self.zone_id = zone_id
        self.zone_name = zone_name
        self.zone_tag = zone_tag
        self.zone_type = zone_type

    def validate(self):
        if self.vpcs:
            self.vpcs.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        if self.is_ptr is not None:
            result['IsPtr'] = self.is_ptr
        if self.record_count is not None:
            result['RecordCount'] = self.record_count
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.update_timestamp is not None:
            result['UpdateTimestamp'] = self.update_timestamp
        if self.vpcs is not None:
            result['Vpcs'] = self.vpcs.to_map()
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.zone_name is not None:
            result['ZoneName'] = self.zone_name
        if self.zone_tag is not None:
            result['ZoneTag'] = self.zone_tag
        if self.zone_type is not None:
            result['ZoneType'] = self.zone_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        if m.get('IsPtr') is not None:
            self.is_ptr = m.get('IsPtr')
        if m.get('RecordCount') is not None:
            self.record_count = m.get('RecordCount')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')
        if m.get('Vpcs') is not None:
            temp_model = DescribeZoneVpcTreeResponseBodyZonesZoneVpcs()
            self.vpcs = temp_model.from_map(m['Vpcs'])
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ZoneName') is not None:
            self.zone_name = m.get('ZoneName')
        if m.get('ZoneTag') is not None:
            self.zone_tag = m.get('ZoneTag')
        if m.get('ZoneType') is not None:
            self.zone_type = m.get('ZoneType')
        return self


class DescribeZoneVpcTreeResponseBodyZones(TeaModel):
    def __init__(
        self,
        zone: List[DescribeZoneVpcTreeResponseBodyZonesZone] = None,
    ):
        self.zone = zone

    def validate(self):
        if self.zone:
            for k in self.zone:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Zone'] = []
        if self.zone is not None:
            for k in self.zone:
                result['Zone'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.zone = []
        if m.get('Zone') is not None:
            for k in m.get('Zone'):
                temp_model = DescribeZoneVpcTreeResponseBodyZonesZone()
                self.zone.append(temp_model.from_map(k))
        return self


class DescribeZoneVpcTreeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        zones: DescribeZoneVpcTreeResponseBodyZones = None,
    ):
        self.request_id = request_id
        self.zones = zones

    def validate(self):
        if self.zones:
            self.zones.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.zones is not None:
            result['Zones'] = self.zones.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Zones') is not None:
            temp_model = DescribeZoneVpcTreeResponseBodyZones()
            self.zones = temp_model.from_map(m['Zones'])
        return self


class DescribeZoneVpcTreeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeZoneVpcTreeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeZoneVpcTreeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeZonesRequestResourceTag(TeaModel):
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


class DescribeZonesRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        lang: str = None,
        page_number: int = None,
        page_size: int = None,
        query_region_id: str = None,
        query_vpc_id: str = None,
        resource_group_id: str = None,
        resource_tag: List[DescribeZonesRequestResourceTag] = None,
        search_mode: str = None,
        zone_tag: List[str] = None,
        zone_type: str = None,
    ):
        self.keyword = keyword
        self.lang = lang
        self.page_number = page_number
        self.page_size = page_size
        self.query_region_id = query_region_id
        # VPC ID。
        self.query_vpc_id = query_vpc_id
        self.resource_group_id = resource_group_id
        self.resource_tag = resource_tag
        self.search_mode = search_mode
        self.zone_tag = zone_tag
        self.zone_type = zone_type

    def validate(self):
        if self.resource_tag:
            for k in self.resource_tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_region_id is not None:
            result['QueryRegionId'] = self.query_region_id
        if self.query_vpc_id is not None:
            result['QueryVpcId'] = self.query_vpc_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['ResourceTag'] = []
        if self.resource_tag is not None:
            for k in self.resource_tag:
                result['ResourceTag'].append(k.to_map() if k else None)
        if self.search_mode is not None:
            result['SearchMode'] = self.search_mode
        if self.zone_tag is not None:
            result['ZoneTag'] = self.zone_tag
        if self.zone_type is not None:
            result['ZoneType'] = self.zone_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryRegionId') is not None:
            self.query_region_id = m.get('QueryRegionId')
        if m.get('QueryVpcId') is not None:
            self.query_vpc_id = m.get('QueryVpcId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.resource_tag = []
        if m.get('ResourceTag') is not None:
            for k in m.get('ResourceTag'):
                temp_model = DescribeZonesRequestResourceTag()
                self.resource_tag.append(temp_model.from_map(k))
        if m.get('SearchMode') is not None:
            self.search_mode = m.get('SearchMode')
        if m.get('ZoneTag') is not None:
            self.zone_tag = m.get('ZoneTag')
        if m.get('ZoneType') is not None:
            self.zone_type = m.get('ZoneType')
        return self


class DescribeZonesResponseBodyZonesZoneResourceTagsResourceTag(TeaModel):
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


class DescribeZonesResponseBodyZonesZoneResourceTags(TeaModel):
    def __init__(
        self,
        resource_tag: List[DescribeZonesResponseBodyZonesZoneResourceTagsResourceTag] = None,
    ):
        self.resource_tag = resource_tag

    def validate(self):
        if self.resource_tag:
            for k in self.resource_tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ResourceTag'] = []
        if self.resource_tag is not None:
            for k in self.resource_tag:
                result['ResourceTag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource_tag = []
        if m.get('ResourceTag') is not None:
            for k in m.get('ResourceTag'):
                temp_model = DescribeZonesResponseBodyZonesZoneResourceTagsResourceTag()
                self.resource_tag.append(temp_model.from_map(k))
        return self


class DescribeZonesResponseBodyZonesZone(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        create_timestamp: int = None,
        is_ptr: bool = None,
        proxy_pattern: str = None,
        record_count: int = None,
        remark: str = None,
        resource_group_id: str = None,
        resource_tags: DescribeZonesResponseBodyZonesZoneResourceTags = None,
        update_time: str = None,
        update_timestamp: int = None,
        zone_id: str = None,
        zone_name: str = None,
        zone_tag: str = None,
        zone_type: str = None,
    ):
        self.create_time = create_time
        self.create_timestamp = create_timestamp
        self.is_ptr = is_ptr
        self.proxy_pattern = proxy_pattern
        self.record_count = record_count
        self.remark = remark
        self.resource_group_id = resource_group_id
        self.resource_tags = resource_tags
        self.update_time = update_time
        self.update_timestamp = update_timestamp
        # zone ID。
        self.zone_id = zone_id
        self.zone_name = zone_name
        self.zone_tag = zone_tag
        self.zone_type = zone_type

    def validate(self):
        if self.resource_tags:
            self.resource_tags.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        if self.is_ptr is not None:
            result['IsPtr'] = self.is_ptr
        if self.proxy_pattern is not None:
            result['ProxyPattern'] = self.proxy_pattern
        if self.record_count is not None:
            result['RecordCount'] = self.record_count
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_tags is not None:
            result['ResourceTags'] = self.resource_tags.to_map()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.update_timestamp is not None:
            result['UpdateTimestamp'] = self.update_timestamp
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.zone_name is not None:
            result['ZoneName'] = self.zone_name
        if self.zone_tag is not None:
            result['ZoneTag'] = self.zone_tag
        if self.zone_type is not None:
            result['ZoneType'] = self.zone_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        if m.get('IsPtr') is not None:
            self.is_ptr = m.get('IsPtr')
        if m.get('ProxyPattern') is not None:
            self.proxy_pattern = m.get('ProxyPattern')
        if m.get('RecordCount') is not None:
            self.record_count = m.get('RecordCount')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceTags') is not None:
            temp_model = DescribeZonesResponseBodyZonesZoneResourceTags()
            self.resource_tags = temp_model.from_map(m['ResourceTags'])
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ZoneName') is not None:
            self.zone_name = m.get('ZoneName')
        if m.get('ZoneTag') is not None:
            self.zone_tag = m.get('ZoneTag')
        if m.get('ZoneType') is not None:
            self.zone_type = m.get('ZoneType')
        return self


class DescribeZonesResponseBodyZones(TeaModel):
    def __init__(
        self,
        zone: List[DescribeZonesResponseBodyZonesZone] = None,
    ):
        self.zone = zone

    def validate(self):
        if self.zone:
            for k in self.zone:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Zone'] = []
        if self.zone is not None:
            for k in self.zone:
                result['Zone'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.zone = []
        if m.get('Zone') is not None:
            for k in m.get('Zone'):
                temp_model = DescribeZonesResponseBodyZonesZone()
                self.zone.append(temp_model.from_map(k))
        return self


class DescribeZonesResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_items: int = None,
        total_pages: int = None,
        zones: DescribeZonesResponseBodyZones = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_items = total_items
        self.total_pages = total_pages
        self.zones = zones

    def validate(self):
        if self.zones:
            self.zones.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_items is not None:
            result['TotalItems'] = self.total_items
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        if self.zones is not None:
            result['Zones'] = self.zones.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItems') is not None:
            self.total_items = m.get('TotalItems')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        if m.get('Zones') is not None:
            temp_model = DescribeZonesResponseBodyZones()
            self.zones = temp_model.from_map(m['Zones'])
        return self


class DescribeZonesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeZonesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
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


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        next_token: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        size: int = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        self.lang = lang
        self.next_token = next_token
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.size = size
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
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.size is not None:
            result['Size'] = self.size
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_resources: List[ListTagResourcesResponseBodyTagResources] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['TagResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tag_resources = []
        if m.get('TagResources') is not None:
            for k in m.get('TagResources'):
                temp_model = ListTagResourcesResponseBodyTagResources()
                self.tag_resources.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveResourceGroupRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        new_resource_group_id: str = None,
        resource_id: str = None,
    ):
        self.lang = lang
        self.new_resource_group_id = new_resource_group_id
        # Zone Id。
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.new_resource_group_id is not None:
            result['NewResourceGroupId'] = self.new_resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('NewResourceGroupId') is not None:
            self.new_resource_group_id = m.get('NewResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


class MoveResourceGroupResponseBody(TeaModel):
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


class MoveResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MoveResourceGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = MoveResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetProxyPatternRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        proxy_pattern: str = None,
        user_client_ip: str = None,
        zone_id: str = None,
    ):
        self.lang = lang
        self.proxy_pattern = proxy_pattern
        self.user_client_ip = user_client_ip
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.proxy_pattern is not None:
            result['ProxyPattern'] = self.proxy_pattern
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ProxyPattern') is not None:
            self.proxy_pattern = m.get('ProxyPattern')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class SetProxyPatternResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        zone_id: str = None,
    ):
        self.request_id = request_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class SetProxyPatternResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetProxyPatternResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = SetProxyPatternResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetZoneRecordStatusRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        record_id: int = None,
        status: str = None,
        user_client_ip: str = None,
    ):
        self.lang = lang
        self.record_id = record_id
        self.status = status
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.status is not None:
            result['Status'] = self.status
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SetZoneRecordStatusResponseBody(TeaModel):
    def __init__(
        self,
        record_id: int = None,
        request_id: str = None,
        status: str = None,
    ):
        self.record_id = record_id
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class SetZoneRecordStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetZoneRecordStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = SetZoneRecordStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
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


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        over_write: bool = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        self.lang = lang
        self.over_write = over_write
        self.resource_id = resource_id
        self.resource_type = resource_type
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
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.over_write is not None:
            result['OverWrite'] = self.over_write
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('OverWrite') is not None:
            self.over_write = m.get('OverWrite')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
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


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        lang: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag_key: List[str] = None,
    ):
        self.all = all
        self.lang = lang
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
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


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UntagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRecordRemarkRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        record_id: int = None,
        remark: str = None,
    ):
        self.lang = lang
        self.record_id = record_id
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class UpdateRecordRemarkResponseBody(TeaModel):
    def __init__(
        self,
        record_id: int = None,
        request_id: str = None,
    ):
        self.record_id = record_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateRecordRemarkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateRecordRemarkResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UpdateRecordRemarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateResolverEndpointRequestIpConfig(TeaModel):
    def __init__(
        self,
        az_id: str = None,
        cidr_block: str = None,
        ip: str = None,
        v_switch_id: str = None,
    ):
        self.az_id = az_id
        self.cidr_block = cidr_block
        self.ip = ip
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.az_id is not None:
            result['AzId'] = self.az_id
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AzId') is not None:
            self.az_id = m.get('AzId')
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class UpdateResolverEndpointRequest(TeaModel):
    def __init__(
        self,
        endpoint_id: str = None,
        ip_config: List[UpdateResolverEndpointRequestIpConfig] = None,
        lang: str = None,
        name: str = None,
    ):
        self.endpoint_id = endpoint_id
        self.ip_config = ip_config
        self.lang = lang
        self.name = name

    def validate(self):
        if self.ip_config:
            for k in self.ip_config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        result['IpConfig'] = []
        if self.ip_config is not None:
            for k in self.ip_config:
                result['IpConfig'].append(k.to_map() if k else None)
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        self.ip_config = []
        if m.get('IpConfig') is not None:
            for k in m.get('IpConfig'):
                temp_model = UpdateResolverEndpointRequestIpConfig()
                self.ip_config.append(temp_model.from_map(k))
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateResolverEndpointResponseBody(TeaModel):
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


class UpdateResolverEndpointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateResolverEndpointResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UpdateResolverEndpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateResolverRuleRequestForwardIp(TeaModel):
    def __init__(
        self,
        ip: str = None,
        port: int = None,
    ):
        self.ip = ip
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class UpdateResolverRuleRequest(TeaModel):
    def __init__(
        self,
        forward_ip: List[UpdateResolverRuleRequestForwardIp] = None,
        lang: str = None,
        name: str = None,
        rule_id: str = None,
    ):
        self.forward_ip = forward_ip
        self.lang = lang
        self.name = name
        self.rule_id = rule_id

    def validate(self):
        if self.forward_ip:
            for k in self.forward_ip:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ForwardIp'] = []
        if self.forward_ip is not None:
            for k in self.forward_ip:
                result['ForwardIp'].append(k.to_map() if k else None)
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.name is not None:
            result['Name'] = self.name
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.forward_ip = []
        if m.get('ForwardIp') is not None:
            for k in m.get('ForwardIp'):
                temp_model = UpdateResolverRuleRequestForwardIp()
                self.forward_ip.append(temp_model.from_map(k))
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class UpdateResolverRuleResponseBody(TeaModel):
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


class UpdateResolverRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateResolverRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UpdateResolverRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSyncEcsHostTaskRequestRegion(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        user_id: int = None,
    ):
        self.region_id = region_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class UpdateSyncEcsHostTaskRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        region: List[UpdateSyncEcsHostTaskRequestRegion] = None,
        status: str = None,
        zone_id: str = None,
    ):
        self.lang = lang
        self.region = region
        self.status = status
        self.zone_id = zone_id

    def validate(self):
        if self.region:
            for k in self.region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        result['Region'] = []
        if self.region is not None:
            for k in self.region:
                result['Region'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        self.region = []
        if m.get('Region') is not None:
            for k in m.get('Region'):
                temp_model = UpdateSyncEcsHostTaskRequestRegion()
                self.region.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class UpdateSyncEcsHostTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateSyncEcsHostTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateSyncEcsHostTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UpdateSyncEcsHostTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateZoneRecordRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        priority: int = None,
        record_id: int = None,
        rr: str = None,
        ttl: int = None,
        type: str = None,
        user_client_ip: str = None,
        value: str = None,
    ):
        self.lang = lang
        self.priority = priority
        self.record_id = record_id
        self.rr = rr
        self.ttl = ttl
        self.type = type
        self.user_client_ip = user_client_ip
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.rr is not None:
            result['Rr'] = self.rr
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        if self.type is not None:
            result['Type'] = self.type
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('Rr') is not None:
            self.rr = m.get('Rr')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateZoneRecordResponseBody(TeaModel):
    def __init__(
        self,
        record_id: int = None,
        request_id: str = None,
    ):
        self.record_id = record_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateZoneRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateZoneRecordResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UpdateZoneRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateZoneRemarkRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        remark: str = None,
        user_client_ip: str = None,
        zone_id: str = None,
    ):
        self.lang = lang
        self.remark = remark
        self.user_client_ip = user_client_ip
        # Zone ID。
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class UpdateZoneRemarkResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        zone_id: str = None,
    ):
        self.request_id = request_id
        # Zone ID。
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class UpdateZoneRemarkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateZoneRemarkResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UpdateZoneRemarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


