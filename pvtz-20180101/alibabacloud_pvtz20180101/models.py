# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class AddCustomLineRequest(TeaModel):
    def __init__(
        self,
        dns_category: str = None,
        ipv_4s: List[str] = None,
        lang: str = None,
        name: str = None,
        share_scope: str = None,
    ):
        # This parameter is not available. You can ignore it.
        self.dns_category = dns_category
        # The IPv4 CIDR blocks.
        # 
        # This parameter is required.
        self.ipv_4s = ipv_4s
        # The language.
        self.lang = lang
        # The name of the custom line.
        # 
        # This parameter is required.
        self.name = name
        # This parameter is not available. You can ignore it.
        self.share_scope = share_scope

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dns_category is not None:
            result['DnsCategory'] = self.dns_category
        if self.ipv_4s is not None:
            result['Ipv4s'] = self.ipv_4s
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.name is not None:
            result['Name'] = self.name
        if self.share_scope is not None:
            result['ShareScope'] = self.share_scope
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DnsCategory') is not None:
            self.dns_category = m.get('DnsCategory')
        if m.get('Ipv4s') is not None:
            self.ipv_4s = m.get('Ipv4s')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ShareScope') is not None:
            self.share_scope = m.get('ShareScope')
        return self


class AddCustomLineResponseBody(TeaModel):
    def __init__(
        self,
        line_id: str = None,
        name: str = None,
        request_id: str = None,
    ):
        # The unique ID of the custom line.
        self.line_id = line_id
        # The name of the custom line.
        self.name = name
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.line_id is not None:
            result['LineId'] = self.line_id
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LineId') is not None:
            self.line_id = m.get('LineId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddCustomLineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddCustomLineResponseBody = None,
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
            temp_model = AddCustomLineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddResolverEndpointRequestIpConfig(TeaModel):
    def __init__(
        self,
        az_id: str = None,
        cidr_block: str = None,
        ip: str = None,
        v_switch_id: str = None,
    ):
        # The ID of the zone to which the vSwitch belongs.
        # 
        # This parameter is required.
        self.az_id = az_id
        # The IPv4 CIDR block of the vSwitch.
        # 
        # This parameter is required.
        self.cidr_block = cidr_block
        # The source IP address of outbound traffic. The IP address must be within the specified CIDR block. If you leave this parameter empty, the system automatically allocates an IP address.
        self.ip = ip
        # The vSwitch ID.
        # 
        # This parameter is required.
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
        # The source IP addresses of outbound traffic. You must add two to six source IP addresses.
        # 
        # >  You must add at least two source IP addresses for outbound traffic to ensure high availability. We recommend that you add two IP addresses that reside in different zones. You can add up to six source IP addresses.
        # 
        # This parameter is required.
        self.ip_config = ip_config
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        # 
        # Default value: en.
        self.lang = lang
        # The endpoint name. The name can be up to 20 characters in length. If the upper limit is exceeded, an error message is returned.
        # 
        # This parameter is required.
        self.name = name
        # The ID of the security group. The security group rules are applied to the outbound VPC.
        # 
        # >  After you create the outbound endpoint, you cannot change the value of SecurityGroupId. This prevents the forwarding of DNS requests from being interrupted due to misoperations.
        # 
        # This parameter is required.
        self.security_group_id = security_group_id
        # The outbound VPC ID. All outbound Domain Name System (DNS) requests of the resolver are forwarded by this VPC.
        # 
        # >  After you create the outbound endpoint, you cannot change the value of VpcId. This prevents the forwarding of DNS requests from being interrupted due to misoperations.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id
        # The region ID of the outbound virtual private cloud (VPC).
        # 
        # This parameter is required.
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
        # The endpoint ID.
        self.endpoint_id = endpoint_id
        # The request ID.
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


class AddResolverRuleRequestEdgeDnsClusters(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
    ):
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class AddResolverRuleRequestForwardIp(TeaModel):
    def __init__(
        self,
        ip: str = None,
        port: int = None,
    ):
        # The IP address of the destination server.
        # 
        # >  The following CIDR blocks are reserved by the system: 100.100.2.136 to 100.100.2.138 and 100.100.2.116 to 100.100.2.118. You cannot specify the IP addresses within these CIDR blocks for the external DNS servers.
        # 
        # This parameter is required.
        self.ip = ip
        # The port of the destination server.
        # 
        # This parameter is required.
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


class AddResolverRuleRequestVpcs(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        vpc_id: str = None,
        vpc_type: str = None,
        vpc_user_id: int = None,
    ):
        self.region_id = region_id
        self.vpc_id = vpc_id
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
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_type is not None:
            result['VpcType'] = self.vpc_type
        if self.vpc_user_id is not None:
            result['VpcUserId'] = self.vpc_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcType') is not None:
            self.vpc_type = m.get('VpcType')
        if m.get('VpcUserId') is not None:
            self.vpc_user_id = m.get('VpcUserId')
        return self


class AddResolverRuleRequest(TeaModel):
    def __init__(
        self,
        edge_dns_clusters: List[AddResolverRuleRequestEdgeDnsClusters] = None,
        endpoint_id: str = None,
        forward_ip: List[AddResolverRuleRequestForwardIp] = None,
        lang: str = None,
        name: str = None,
        type: str = None,
        vpcs: List[AddResolverRuleRequestVpcs] = None,
        zone_name: str = None,
    ):
        self.edge_dns_clusters = edge_dns_clusters
        # The outbound endpoint ID. The outbound endpoint is used to forward the DNS requests to the specified destination IP addresses.
        self.endpoint_id = endpoint_id
        # The IP addresses and ports of the external DNS servers. Enter the IP addresses and ports of the destination servers to which the DNS requests are forwarded. You can enter up to **six** IP addresses and ports. Both private and public IP addresses are supported.
        # 
        # >  If you specify public IP addresses as the IP addresses of the external DNS servers and Elastic Compute Service (ECS) instances in the outbound VPC are not assigned public IP addresses, you need to activate NAT Gateway for the VPC and create and manage SNAT entries on a NAT gateway.
        # 
        # This parameter is required.
        self.forward_ip = forward_ip
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        # 
        # Default value: en.
        self.lang = lang
        # The name of the forwarding rule. You can name the rule based on your business requirements.
        # 
        # This parameter is required.
        self.name = name
        # The type of the forwarding rule. The parameter value can only be OUTBOUND, which indicates that DNS requests are forwarded to one or more external IP addresses.
        # 
        # >  You cannot change the value of Type after you create the forwarding rule.
        self.type = type
        self.vpcs = vpcs
        # The zone for which you want to forward DNS requests.
        # 
        # >  You cannot change the value of ZoneName after you create the forwarding rule.
        # 
        # This parameter is required.
        self.zone_name = zone_name

    def validate(self):
        if self.edge_dns_clusters:
            for k in self.edge_dns_clusters:
                if k:
                    k.validate()
        if self.forward_ip:
            for k in self.forward_ip:
                if k:
                    k.validate()
        if self.vpcs:
            for k in self.vpcs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EdgeDnsClusters'] = []
        if self.edge_dns_clusters is not None:
            for k in self.edge_dns_clusters:
                result['EdgeDnsClusters'].append(k.to_map() if k else None)
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
        result['Vpcs'] = []
        if self.vpcs is not None:
            for k in self.vpcs:
                result['Vpcs'].append(k.to_map() if k else None)
        if self.zone_name is not None:
            result['ZoneName'] = self.zone_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.edge_dns_clusters = []
        if m.get('EdgeDnsClusters') is not None:
            for k in m.get('EdgeDnsClusters'):
                temp_model = AddResolverRuleRequestEdgeDnsClusters()
                self.edge_dns_clusters.append(temp_model.from_map(k))
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
        self.vpcs = []
        if m.get('Vpcs') is not None:
            for k in m.get('Vpcs'):
                temp_model = AddResolverRuleRequestVpcs()
                self.vpcs.append(temp_model.from_map(k))
        if m.get('ZoneName') is not None:
            self.zone_name = m.get('ZoneName')
        return self


class AddResolverRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        rule_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The ID of the forwarding rule.
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
        # The authorization channel. Valid values:
        # 
        # *   AUTH_CODE: A verification code is used for authorization.
        # *   RESOURCE_DIRECTORY: A resource directory is used for authorization.
        # 
        # Default value: AUTH_CODE.
        self.auth_channel = auth_channel
        # The verification code.
        # 
        # > 
        # 
        # *   The specified authentication code is used if the value of AuthChannel is left empty or is set to AUTH_CODE.
        # 
        # *   In other cases, a random 6-digit number is used. Example: 123456.
        self.auth_code = auth_code
        # The authorization scope. Valid values:
        # 
        # *   NORMAL: general authorization
        # *   CLOUD_PRODUCT: cloud service-related authorization
        self.auth_type = auth_type
        # The ID of the Alibaba Cloud account to which the permissions on the resources are granted.
        # 
        # >  You can set an effective scope across accounts only by using an Alibaba Cloud account instead of a RAM user. You can set an effective scope across accounts registered on the same site. For example, you can perform the operation across accounts that are both registered on the Alibaba Cloud China site or Alibaba Cloud international site. You cannot set an effective scope across accounts registered on different sites. For example, you cannot perform the operation across accounts that are separately registered on the Alibaba Cloud China site and Alibaba Cloud international site.
        # 
        # This parameter is required.
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
        # The request ID.
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
        client_token: str = None,
        dns_group: str = None,
        lang: str = None,
        proxy_pattern: str = None,
        resource_group_id: str = None,
        zone_name: str = None,
        zone_tag: str = None,
        zone_type: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The logical location type of the built-in authoritative module in which the zone is added. Valid values:
        # 
        # *   **NORMAL_ZONE**: the regular module. DNS results are stored in the cache module and DNS requests are sent to the regular module if the DNS requests do not match the DNS records in the cache module. DNS record updates take effect based on the time to live (TTL) value. The regular module does not support DNS resolution over user-defined lines or based on weight values.
        # *   **FAST_ZONE**: the acceleration module. It directly responds to DNS requests with the lowest latency and updates DNS records in real time. The acceleration module supports DNS resolution over user-defined lines or based on weight values.
        # 
        # Default value: **NORMAL_ZONE**.
        # 
        # >  The DNS results returned by the built-in authoritative acceleration module are not stored in the cache module because the built-in authoritative acceleration module is located before the cache module. As a result, you are charged more for DNS requests.
        self.dns_group = dns_group
        # The language of the response. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        # 
        # Default value: **en**.
        self.lang = lang
        # Specifies whether to enable the recursive resolution proxy for subdomain names. Valid values:
        # 
        # *   **ZONE**: disables the recursive resolution proxy for subdomain names. In this case, NXDOMAIN is returned if the queried subdomain name does not exist in the zone.
        # *   **RECORD**: enables the recursive resolution proxy for subdomain names. In this case, if the queried subdomain name does not exist in the zone, DNS requests are recursively forwarded to the forward module and then to the recursion module until DNS results are returned.
        # 
        # Default value: **ZONE**.
        self.proxy_pattern = proxy_pattern
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The name of the zone to be added.
        self.zone_name = zone_name
        # This parameter is not available. You can ignore it.
        self.zone_tag = zone_tag
        # This parameter is not available. You can ignore it.
        self.zone_type = zone_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dns_group is not None:
            result['DnsGroup'] = self.dns_group
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
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DnsGroup') is not None:
            self.dns_group = m.get('DnsGroup')
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
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success
        # The zone ID. This ID uniquely identifies the zone.
        self.zone_id = zone_id
        # The name of the zone.
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
        client_token: str = None,
        lang: str = None,
        line: str = None,
        priority: int = None,
        remark: str = None,
        rr: str = None,
        ttl: int = None,
        type: str = None,
        user_client_ip: str = None,
        value: str = None,
        weight: int = None,
        zone_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        # 
        # Default value: en.
        self.lang = lang
        # The DNS request source. Valid values:
        # 
        # *   default: the default resolution line. The default line is equivalent to a global line. We recommend that you configure a default line to ensure that a DNS record can be returned if no intelligent line is matched.
        # *   Alibaba Cloud lines: indicate that DNS requests are originated from Alibaba Cloud, including Alibaba Cloud public cloud, Alibaba Finance Cloud, and Alibaba Gov Cloud.
        # *   Custom lines: You can configure custom lines so that Private DNS can return specific IP addresses for DNS requests that are originated from a specific CIDR block.
        # 
        # > 
        # 
        # *   Only built-in authoritative acceleration zones support custom lines.
        # 
        # *   Set Line to default if you want to choose the default line. Set Line to a specific line code if you want to choose an Alibaba Cloud line or a custom line. Example: aliyun_r_cn-beijing-a.
        self.line = line
        # The priority of the mail exchanger (MX) record. Valid values: **1 to 99**. A smaller value indicates a higher priority.
        self.priority = priority
        # The description of the DNS record.
        self.remark = remark
        # The hostname. The hostname is the prefix of the subdomain name for the zone. Example: www, @, \\* (used for wildcard DNS resolution), and mail (used for specifying the mail server that receives emails).
        # 
        # For example, if you want to resolve the domain name @.exmaple.com, you must set Rr to @ instead of leaving Rr empty.
        # 
        # This parameter is required.
        self.rr = rr
        # The time to live (TTL) period. Valid values: 5, 30, 60, 3600, 43200, and 86400. Unit: seconds. Default value: 60.
        self.ttl = ttl
        # The type of the DNS record. Valid values:
        # 
        # *   **A**: An A record maps a domain name to an IPv4 address in the dotted decimal notation format.
        # *   **AAAA**: An AAAA record maps a domain name to an IPv6 address.
        # *   **CNAME**: A canonical name (CNAME) record maps a domain name to another domain name.
        # *   **TXT**: A text (TXT) record usually serves as a Sender Policy Framework (SPF) record to prevent email spam. The record value of the TXT record can be up to 255 characters in length.
        # *   **MX**: A mail exchanger (MX) record maps a domain name to the domain name of a mail server.
        # *   **PTR**: A pointer (PTR) record maps an IP address to a domain name.
        # *   **SRV**: A service (SRV) record specifies a server that hosts a specific service. Enter a record value in the format of Priority Weight Port Destination domain name. Separate these items with spaces.
        # 
        # >  Before you add a PTR record, you must configure a reverse lookup zone. For more information, see [Add PTR records](https://help.aliyun.com/document_detail/2592976.html).
        # 
        # This parameter is required.
        self.type = type
        # The IP address of the client.
        self.user_client_ip = user_client_ip
        # The record value. You need to enter the record value based on the DNS record type.
        # 
        # This parameter is required.
        self.value = value
        # The weight value of the address. You can set a different weight value for each address. This way, addresses are returned based on the weight values for DNS requests. A weight value must be an integer that ranges from 1 to 100. Default value: 1.
        self.weight = weight
        # The zone ID. This ID uniquely identifies the zone.
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.line is not None:
            result['Line'] = self.line
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
        if self.weight is not None:
            result['Weight'] = self.weight
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Line') is not None:
            self.line = m.get('Line')
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
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
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
        # The ID of the DNS record.
        self.record_id = record_id
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
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
        # The region ID of the outbound VPC.
        self.region_id = region_id
        # The VPC ID.
        self.vpc_id = vpc_id
        # The VPC type. Valid values:
        # 
        # *   STANDARD: standard VPC
        # *   EDS: Elastic Desktop Service (EDS) workspace VPC
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
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        # 
        # Default value: en.
        self.lang = lang
        # The ID of the forwarding rule.
        # 
        # This parameter is required.
        self.rule_id = rule_id
        # The VPCs that you want to associate with the forwarding rule.
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
        # The request ID.
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
        # The region ID of the VPC.
        self.region_id = region_id
        # The VPC ID. If the zone is already associated with VPCs and you do not specify this parameter, the associated VPCs are disassociated from the zone.
        self.vpc_id = vpc_id
        # The VPC type. Valid values:
        # 
        # *   **STANDARD**: standard VPC
        # *   **EDS**: Elastic Desktop Service (EDS) workspace VPC
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
        client_token: str = None,
        lang: str = None,
        user_client_ip: str = None,
        vpcs: List[BindZoneVpcRequestVpcs] = None,
        zone_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        # 
        # Default value: en.
        self.lang = lang
        # The IP address of the client.
        self.user_client_ip = user_client_ip
        # The VPCs.
        # 
        # >  If Vpcs is left empty, all VPCs that are associated with the zone are disassociated from the zone.
        self.vpcs = vpcs
        # The zone ID. This ID uniquely identifies the zone.
        # 
        # This parameter is required.
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
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
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
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
        # The request ID.
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


class ChangeZoneDnsGroupRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dns_group: str = None,
        zone_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see How to ensure idempotence.
        self.client_token = client_token
        # The logical location of the built-in authoritative module in which the zone is added. Valid values:
        # 
        # *   Normal zone: regular module
        # *   Fast Zone: acceleration module
        # 
        # This parameter is required.
        self.dns_group = dns_group
        # The global ID of the zone.
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dns_group is not None:
            result['DnsGroup'] = self.dns_group
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DnsGroup') is not None:
            self.dns_group = m.get('DnsGroup')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ChangeZoneDnsGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        zone_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The global ID of the zone.
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


class ChangeZoneDnsGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChangeZoneDnsGroupResponseBody = None,
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
            temp_model = ChangeZoneDnsGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckZoneNameRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        user_client_ip: str = None,
        zone_name: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        # 
        # Default value: en.
        self.lang = lang
        # The IP address of the client.
        self.user_client_ip = user_client_ip
        # The name of the zone. This parameter is required.
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
        # Indicates whether the zone name can be added. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.check = check
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
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


class DeleteCustomLineRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        line_id: str = None,
    ):
        # The language.
        self.lang = lang
        # The unique ID of the custom line.
        # 
        # This parameter is required.
        self.line_id = line_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.line_id is not None:
            result['LineId'] = self.line_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('LineId') is not None:
            self.line_id = m.get('LineId')
        return self


class DeleteCustomLineResponseBody(TeaModel):
    def __init__(
        self,
        line_id: str = None,
        request_id: str = None,
    ):
        # The unique ID of the custom line.
        self.line_id = line_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.line_id is not None:
            result['LineId'] = self.line_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LineId') is not None:
            self.line_id = m.get('LineId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteCustomLineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCustomLineResponseBody = None,
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
            temp_model = DeleteCustomLineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteResolverEndpointRequest(TeaModel):
    def __init__(
        self,
        endpoint_id: str = None,
        lang: str = None,
    ):
        # The endpoint ID. This ID uniquely identifies the endpoint.
        # 
        # This parameter is required.
        self.endpoint_id = endpoint_id
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        # 
        # Default value: en.
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
        # The request ID.
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
        # The language.
        self.lang = lang
        # The forwarding rule ID.
        # 
        # This parameter is required.
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
        # The request ID.
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
        # The authorization scope. Valid values:
        # 
        # *   NORMAL: general authorization
        # *   NORMAL: cloud service-related authorization
        # 
        # Default value: NORMAL.
        self.auth_type = auth_type
        # The ID of the Alibaba Cloud account.
        # 
        # This parameter is required.
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
        # The request ID.
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
        client_token: str = None,
        lang: str = None,
        user_client_ip: str = None,
        zone_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        # 
        # Default value: en.
        self.lang = lang
        # The IP address of the client.
        self.user_client_ip = user_client_ip
        # The zone ID. This ID uniquely identifies the zone.
        # 
        # >  If you want to delete a built-in authoritative zone whose effective scope is configured, you must disassociate the zone from the effective scope first.
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
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
        # The request ID.
        self.request_id = request_id
        # The zone ID. This ID uniquely identifies the zone.
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
        client_token: str = None,
        lang: str = None,
        record_id: int = None,
        user_client_ip: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        # 
        # Default value: en.
        self.lang = lang
        # The ID of the DNS record.
        # 
        # This parameter is required.
        self.record_id = record_id
        # The IP address of the client.
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
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
        # The ID of the DNS record.
        self.record_id = record_id
        # The request ID.
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
        # The end of the time range to query. Set the time to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.end_timestamp = end_timestamp
        # The type of operation logs. Valid values:
        # 
        # *   **PV_ZONE**: the logs that record the operations on built-in authoritative zones
        # *   **PV_RECORD**: the logs that record the operations on DNS records
        # *   **RESOLVER_RULE**: the logs that record the operations on forwarding rules
        # *   **CUSTOM_LINE**: the logs that record the operations on user-defined lines
        # *   **RESOLVER_ENDPOINT**: the logs that record the operations on outbound endpoints
        # *   **INBOUND_ENDPOINT**: the logs that record the operations on inbound endpoints
        # *   **CACHE_RESERVE_DOMAIN**: the logs that record the operations on cache retention domain names
        # 
        # >  If you set EntityType to other values, all types of logs are queried.
        self.entity_type = entity_type
        # The keyword of the operation or the operation content. Fuzzy search is supported. The value is not case-sensitive.
        self.keyword = keyword
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        # 
        # Default value: en.
        self.lang = lang
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.page_size = page_size
        # The beginning of the time range to query. Set the time to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.start_timestamp = start_timestamp
        # The IP address of the client.
        self.user_client_ip = user_client_ip
        # The zone ID. Valid values:
        # 
        # *   If you set ZoneId to a zone ID, the logs that record the operations on the DNS records of the specified zone are queried.\\
        # 
        # *   If you leave ZoneId empty, the logs that record the operations on all zones and the DNS records of these zones that belong to the current Alibaba Cloud account are queried.
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
        creator_id: str = None,
        creator_sub_type: str = None,
        creator_type: str = None,
        creator_user_id: str = None,
        entity_id: str = None,
        entity_name: str = None,
        id: int = None,
        oper_action: str = None,
        oper_ip: str = None,
        oper_object: str = None,
        oper_time: str = None,
        oper_timestamp: int = None,
    ):
        # The operation content.
        self.content = content
        # The operator ID.
        self.creator_id = creator_id
        # The subtype of the operator. Valid values:
        # 
        # *   CUSTOMER: Alibaba Cloud account
        # *   SUB: RAM user
        # *   STS: assumed role that obtains the Security Token Service (STS) token of a RAM role
        # *   OTHER: other types
        self.creator_sub_type = creator_sub_type
        # The operator type. No value or **USER** is returned for this parameter.
        self.creator_type = creator_type
        # The operator ID.
        self.creator_user_id = creator_user_id
        # The unique ID of the zone, user-defined line, forwarding rule, outbound endpoint, or inbound endpoint.
        self.entity_id = entity_id
        # The name of the object on which the operation was performed, such as the domain name, user-defined line, cache retention domain name, forwarding rule, outbound endpoint, or inbound endpoint.
        self.entity_name = entity_name
        # The ID of the operation log.
        self.id = id
        # The specific operation performed on the object, such as adding, deleting, modifying, or associating the object.
        self.oper_action = oper_action
        # The public IP address of the operator terminal. If the IP address of the operator terminal is a private IP address, the value of this parameter is the public IP address to which the private IP address is mapped after network address translation (NAT).
        self.oper_ip = oper_ip
        # The type of the object on which the operation was performed. Valid values:
        # 
        # *   **PV_ZONE**: the built-in authoritative zone
        # *   **PV_RECORD**: the DNS record
        # *   **RESOLVER_RULE**: the forwarding rule
        # *   **CUSTOM_LINE**: the user-defined line
        # *   **RESOLVER_ENDPOINT**: the outbound endpoint
        # *   **INBOUND_ENDPOINT**: the inbound endpoint
        # *   **CACHE_RESERVE_DOMAIN**: the cache retention domain name
        self.oper_object = oper_object
        # The time when the operation is performed. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.oper_time = oper_time
        # The time when the operation was performed. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
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
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.creator_sub_type is not None:
            result['CreatorSubType'] = self.creator_sub_type
        if self.creator_type is not None:
            result['CreatorType'] = self.creator_type
        if self.creator_user_id is not None:
            result['CreatorUserId'] = self.creator_user_id
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
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('CreatorSubType') is not None:
            self.creator_sub_type = m.get('CreatorSubType')
        if m.get('CreatorType') is not None:
            self.creator_type = m.get('CreatorType')
        if m.get('CreatorUserId') is not None:
            self.creator_user_id = m.get('CreatorUserId')
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
        # The operation logs.
        self.change_logs = change_logs
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_items = total_items
        # The total number of pages returned.
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


class DescribeCustomLineInfoRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        line_id: str = None,
    ):
        # The language of the response.
        self.lang = lang
        # The unique ID of the custom line.
        # 
        # This parameter is required.
        self.line_id = line_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.line_id is not None:
            result['LineId'] = self.line_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('LineId') is not None:
            self.line_id = m.get('LineId')
        return self


class DescribeCustomLineInfoResponseBody(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        create_timestamp: int = None,
        creator: str = None,
        creator_sub_type: str = None,
        creator_type: str = None,
        dnscategory: str = None,
        ipv_4s: List[str] = None,
        line_id: str = None,
        name: str = None,
        request_id: str = None,
        update_time: str = None,
        update_timestamp: int = None,
    ):
        # The time when the custom line was created. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        # The time when the custom line was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_timestamp = create_timestamp
        # The creator of the custom line.
        self.creator = creator
        # The type of the creator. Valid values:
        # 
        # *   CUSTOM: Alibaba Cloud account
        # *   SUB: RAM user
        # *   STS: assumed role that obtains the Security Token Service (STS) token of a RAM role
        # *   OTHER: other roles
        self.creator_sub_type = creator_sub_type
        # The role of the creator. Valid values:
        # 
        # *   USER: user
        # *   SYSTEM: system
        self.creator_type = creator_type
        self.dnscategory = dnscategory
        # The IPv4 CIDR blocks.
        self.ipv_4s = ipv_4s
        # The unique ID of the custom line.
        self.line_id = line_id
        # The name of the custom line.
        self.name = name
        # The request ID.
        self.request_id = request_id
        # The time when the custom line was updated. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.update_time = update_time
        # The time when the custom line was updated. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.update_timestamp = update_timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.creator_sub_type is not None:
            result['CreatorSubType'] = self.creator_sub_type
        if self.creator_type is not None:
            result['CreatorType'] = self.creator_type
        if self.dnscategory is not None:
            result['Dnscategory'] = self.dnscategory
        if self.ipv_4s is not None:
            result['Ipv4s'] = self.ipv_4s
        if self.line_id is not None:
            result['LineId'] = self.line_id
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.update_timestamp is not None:
            result['UpdateTimestamp'] = self.update_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('CreatorSubType') is not None:
            self.creator_sub_type = m.get('CreatorSubType')
        if m.get('CreatorType') is not None:
            self.creator_type = m.get('CreatorType')
        if m.get('Dnscategory') is not None:
            self.dnscategory = m.get('Dnscategory')
        if m.get('Ipv4s') is not None:
            self.ipv_4s = m.get('Ipv4s')
        if m.get('LineId') is not None:
            self.line_id = m.get('LineId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')
        return self


class DescribeCustomLineInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCustomLineInfoResponseBody = None,
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
            temp_model = DescribeCustomLineInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCustomLinesRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The language.
        self.lang = lang
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: **1 to 100**. Default value: **10**.
        self.page_size = page_size

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeCustomLinesResponseBodyCustomLinesCustomLineIpv4s(TeaModel):
    def __init__(
        self,
        ipv_4: List[str] = None,
    ):
        self.ipv_4 = ipv_4

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ipv_4 is not None:
            result['Ipv4'] = self.ipv_4
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ipv4') is not None:
            self.ipv_4 = m.get('Ipv4')
        return self


class DescribeCustomLinesResponseBodyCustomLinesCustomLine(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        create_timestamp: int = None,
        creator: str = None,
        creator_sub_type: str = None,
        creator_type: str = None,
        dns_category: str = None,
        ipv_4s: DescribeCustomLinesResponseBodyCustomLinesCustomLineIpv4s = None,
        line_id: str = None,
        name: str = None,
        update_time: str = None,
        update_timestamp: int = None,
    ):
        # The time when the custom line was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        # The time when the custom line was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_timestamp = create_timestamp
        # The creator of the custom line.
        self.creator = creator
        # The type of the creator for the custom line. Valid values:
        # 
        # *   CUSTOM: Alibaba Cloud account
        # *   SUB: RAM user
        # *   STS: assumed role that obtains the Security Token Service (STS) token of a RAM role
        # *   OTHER: other roles
        self.creator_sub_type = creator_sub_type
        # The role of the creator for the custom line. Valid values:
        # 
        # *   USER: user
        # *   SYSTEM: system
        self.creator_type = creator_type
        self.dns_category = dns_category
        # The IPv4 CIDR blocks.
        self.ipv_4s = ipv_4s
        # The unique ID of the custom line.
        self.line_id = line_id
        # The name of the custom line.
        self.name = name
        # The time when the custom line was updated. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.update_time = update_time
        # The time when the custom line was updated. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.update_timestamp = update_timestamp

    def validate(self):
        if self.ipv_4s:
            self.ipv_4s.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.creator_sub_type is not None:
            result['CreatorSubType'] = self.creator_sub_type
        if self.creator_type is not None:
            result['CreatorType'] = self.creator_type
        if self.dns_category is not None:
            result['DnsCategory'] = self.dns_category
        if self.ipv_4s is not None:
            result['Ipv4s'] = self.ipv_4s.to_map()
        if self.line_id is not None:
            result['LineId'] = self.line_id
        if self.name is not None:
            result['Name'] = self.name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.update_timestamp is not None:
            result['UpdateTimestamp'] = self.update_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('CreatorSubType') is not None:
            self.creator_sub_type = m.get('CreatorSubType')
        if m.get('CreatorType') is not None:
            self.creator_type = m.get('CreatorType')
        if m.get('DnsCategory') is not None:
            self.dns_category = m.get('DnsCategory')
        if m.get('Ipv4s') is not None:
            temp_model = DescribeCustomLinesResponseBodyCustomLinesCustomLineIpv4s()
            self.ipv_4s = temp_model.from_map(m['Ipv4s'])
        if m.get('LineId') is not None:
            self.line_id = m.get('LineId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')
        return self


class DescribeCustomLinesResponseBodyCustomLines(TeaModel):
    def __init__(
        self,
        custom_line: List[DescribeCustomLinesResponseBodyCustomLinesCustomLine] = None,
    ):
        self.custom_line = custom_line

    def validate(self):
        if self.custom_line:
            for k in self.custom_line:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CustomLine'] = []
        if self.custom_line is not None:
            for k in self.custom_line:
                result['CustomLine'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_line = []
        if m.get('CustomLine') is not None:
            for k in m.get('CustomLine'):
                temp_model = DescribeCustomLinesResponseBodyCustomLinesCustomLine()
                self.custom_line.append(temp_model.from_map(k))
        return self


class DescribeCustomLinesResponseBody(TeaModel):
    def __init__(
        self,
        custom_lines: DescribeCustomLinesResponseBodyCustomLines = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_items: int = None,
        total_pages: int = None,
    ):
        # The custom lines.
        self.custom_lines = custom_lines
        # The page number. Pages start from page **1**. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Valid values: **1 to 100**. Default value: **10**.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_items = total_items
        # The total number of returned pages.
        self.total_pages = total_pages

    def validate(self):
        if self.custom_lines:
            self.custom_lines.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_lines is not None:
            result['CustomLines'] = self.custom_lines.to_map()
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
        if m.get('CustomLines') is not None:
            temp_model = DescribeCustomLinesResponseBodyCustomLines()
            self.custom_lines = temp_model.from_map(m['CustomLines'])
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


class DescribeCustomLinesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCustomLinesResponseBody = None,
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
            temp_model = DescribeCustomLinesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        authorized_user_id: int = None,
        lang: str = None,
        scene: str = None,
        user_client_ip: str = None,
        vpc_type: str = None,
    ):
        # The supported language. Valid values:
        # 
        # *   zh-CN: Chinese
        # *   en-US: English
        # 
        # Default value: en-US.
        # 
        # >  AcceptLanguage has a higher priority than Lang.
        self.accept_language = accept_language
        # The ID of the Alibaba Cloud account to which the permissions on the resources are granted.
        self.authorized_user_id = authorized_user_id
        # The language of the response. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        # 
        # Default value: **en**.
        # 
        # >  Lang has a lower priority than AcceptLanguage.
        self.lang = lang
        # The scenario. Valid values:
        # 
        # *   AUTH: the built-in authoritative module
        # *   FWD: the forward module
        # *   RA: the traffic analysis module
        self.scene = scene
        # The IP address of the client.
        self.user_client_ip = user_client_ip
        # The VPC type. Valid values:
        # 
        # *   STANDARD: standard VPC
        # *   EDS: Elastic Desktop Service (EDS) workspace VPC
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
        if self.scene is not None:
            result['Scene'] = self.scene
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
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
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
        # The display name of the region, which varies based on the current language.
        self.local_name = local_name
        # The endpoint of the service in the region.
        self.region_endpoint = region_endpoint
        # The region ID.
        self.region_id = region_id
        # The region name.
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
        # The regions.
        self.regions = regions
        # The request ID.
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
        # The business ID. BizId is specified together with BizType.
        # 
        # *   If you set BizType to AUTH_ZONE, set BizId to a zone ID.
        # *   If you set BizType to RESOLVER_RULE, set BizId to the ID of a forwarding rule.
        self.biz_id = biz_id
        # The business type. Valid values:
        # 
        # *   AUTH_ZONE: authoritative zone
        # *   RESOLVER_RULE: forwarding rule
        self.biz_type = biz_type
        # The end of the time range to query. Set the time to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # This parameter is required.
        self.end_timestamp = end_timestamp
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        # 
        # Default value: en.
        self.lang = lang
        # The beginning of the time range to query. Set the time to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # This parameter is required.
        self.start_timestamp = start_timestamp
        # The IP address of the client.
        self.user_client_ip = user_client_ip
        # The ID of the virtual private cloud (VPC).
        self.vpc_id = vpc_id
        # The zone ID.
        # 
        # >  To query the number of DNS requests for a zone, you can specify ZoneId or BizType and BizId.
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
        # The number of DNS requests.
        self.request_count = request_count
        # The time when the data was collected. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.time = time
        # The time when the data was collected. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
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
        # The details of the DNS requests.
        self.request_details = request_details
        # The request ID.
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
        # The zone ID.
        self.az_id = az_id
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        # 
        # Default value: en.
        self.lang = lang
        # The region ID.
        # 
        # This parameter is required.
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
        # The zone ID.
        self.az_id = az_id
        # The state of resources in the zone. Valid values:
        # 
        # *   NORMAL: The resources are in the normal state.
        # *   SOLD_OUT: The resources are sold out.
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
        # The queried zones.
        self.available_zones = available_zones
        # The request ID.
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
        # The endpoint ID. This ID uniquely identifies the endpoint.
        # 
        # This parameter is required.
        self.endpoint_id = endpoint_id
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        # 
        # Default value: en.
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
        # The ID of the zone to which the vSwitch belongs.
        self.az_id = az_id
        # The IPv4 CIDR block of the vSwitch.
        self.cidr_block = cidr_block
        # The source IP address of outbound traffic. The IP address must be within the specified CIDR block. If this parameter is left empty, the system automatically allocates an IP address.
        self.ip = ip
        # The vSwitch ID.
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
        # The time when the endpoint was created.
        self.create_time = create_time
        # The time when the endpoint was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_timestamp = create_timestamp
        # The endpoint ID. This ID uniquely identifies the endpoint.
        self.id = id
        # The configurations of the source IP addresses for outbound traffic.
        self.ip_configs = ip_configs
        # The name of the endpoint.
        self.name = name
        # The request ID.
        self.request_id = request_id
        # The ID of the security group. The security group rules are applied to the outbound virtual private cloud (VPC).
        self.security_group_id = security_group_id
        # The state of the endpoint. Valid values:
        # 
        # *   SUCCESS: The endpoint works as expected.
        # *   INIT: The endpoint is being created.
        # *   FAILED: The endpoint failed to be created.
        # *   CHANGE_INIT: The endpoint is being modified.
        # *   CHANGE_FAILED: The endpoint failed to be modified.
        # *   EXCEPTION: The endpoint encountered an exception.
        self.status = status
        # The time when the endpoint was updated.
        self.update_time = update_time
        # The time when the endpoint was updated. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.update_timestamp = update_timestamp
        # The ID of the outbound VPC. All outbound Domain Name System (DNS) requests of the resolver are forwarded by this VPC.
        self.vpc_id = vpc_id
        # The name of the outbound VPC.
        self.vpc_name = vpc_name
        # The region ID of the outbound VPC.
        self.vpc_region_id = vpc_region_id
        # The name of the region where the outbound VPC resides.
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
        vpc_region_id: str = None,
    ):
        # The keyword of the endpoint name, which is used for fuzzy searches.
        self.keyword = keyword
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        # 
        # Default value: en.
        self.lang = lang
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.page_size = page_size
        # The state of the endpoint that you want to query. Valid values:
        # 
        # *   SUCCESS: The endpoint works as expected.
        # *   INIT: The endpoint is being created.
        # *   FAILED: The endpoint failed to be created.
        # *   CHANGE_INIT: The endpoint is being modified.
        # *   CHANGE_FAILED: The endpoint failed to be modified.
        # *   EXCEPTION: The endpoint encountered an exception.
        # 
        # >  If you do not specify this parameter, endpoints in all states are returned.
        self.status = status
        # The region ID of the outbound virtual private cloud (VPC).
        self.vpc_region_id = vpc_region_id

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
        if self.vpc_region_id is not None:
            result['VpcRegionId'] = self.vpc_region_id
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
        if m.get('VpcRegionId') is not None:
            self.vpc_region_id = m.get('VpcRegionId')
        return self


class DescribeResolverEndpointsResponseBodyEndpointsIpConfigs(TeaModel):
    def __init__(
        self,
        az_id: str = None,
        cidr_block: str = None,
        ip: str = None,
        v_switch_id: str = None,
    ):
        # The ID of the zone to which the vSwitch belongs.
        self.az_id = az_id
        # The IPv4 CIDR block of the vSwitch.
        self.cidr_block = cidr_block
        # The source IP address of outbound traffic. The IP address must be within the specified CIDR block.
        self.ip = ip
        # The vSwitch ID.
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
        # The time when the endpoint was created.
        self.create_time = create_time
        # The time when the endpoint was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_timestamp = create_timestamp
        # The endpoint ID.
        self.id = id
        # The source IP addresses of outbound traffic.
        self.ip_configs = ip_configs
        # The name of the endpoint.
        self.name = name
        # The ID of the security group.
        self.security_group_id = security_group_id
        # The state of the endpoint that you queried. Valid values:
        # 
        # *   SUCCESS: The endpoint works as expected.
        # *   INIT: The endpoint is being created.
        # *   FAILED: The endpoint failed to be created.
        # *   CHANGE_INIT: The endpoint is being modified.
        # *   CHANGE_FAILED: The endpoint failed to be modified.
        # *   EXCEPTION: The endpoint encountered an exception.
        self.status = status
        # The time when the endpoint was updated.
        self.update_time = update_time
        # The time when the endpoint was updated. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.update_timestamp = update_timestamp
        # The ID of the outbound VPC. All outbound Domain Name System (DNS) requests of the resolver are forwarded by this VPC.
        self.vpc_id = vpc_id
        # The name of the outbound VPC.
        self.vpc_name = vpc_name
        # The region ID of the outbound VPC.
        self.vpc_region_id = vpc_region_id
        # The name of the region where the VPC resides.
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
        # The endpoints.
        self.endpoints = endpoints
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of endpoints.
        self.total_items = total_items
        # The total number of pages returned.
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
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        # 
        # Default value: en.
        self.lang = lang
        # The ID of the forwarding rule.
        # 
        # This parameter is required.
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


class DescribeResolverRuleResponseBodyBindEdgeDnsClusters(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        cluster_user_id: int = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.cluster_user_id = cluster_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.cluster_user_id is not None:
            result['ClusterUserId'] = self.cluster_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ClusterUserId') is not None:
            self.cluster_user_id = m.get('ClusterUserId')
        return self


class DescribeResolverRuleResponseBodyBindVpcs(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        region_name: str = None,
        vpc_id: str = None,
        vpc_name: str = None,
        vpc_type: str = None,
        vpc_user_id: str = None,
    ):
        # The region ID.
        self.region_id = region_id
        # The region name.
        self.region_name = region_name
        # The VPC ID.
        self.vpc_id = vpc_id
        # The VPC name.
        self.vpc_name = vpc_name
        # The VPC type. Valid values:
        # 
        # *   STANDARD: standard VPC
        # *   EDS: Elastic Desktop Service (EDS) workspace VPC
        self.vpc_type = vpc_type
        # The ID of the user to which the VPC belongs.
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


class DescribeResolverRuleResponseBodyForwardIps(TeaModel):
    def __init__(
        self,
        ip: str = None,
        port: int = None,
    ):
        # The destination IP address.
        self.ip = ip
        # The port number.
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
        bind_edge_dns_clusters: List[DescribeResolverRuleResponseBodyBindEdgeDnsClusters] = None,
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
        self.bind_edge_dns_clusters = bind_edge_dns_clusters
        # The virtual private clouds (VPCs) that are associated with the forwarding rule.
        self.bind_vpcs = bind_vpcs
        # The time when the forwarding rule was created.
        self.create_time = create_time
        # The time when the forwarding rule was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_timestamp = create_timestamp
        # The endpoint ID.
        self.endpoint_id = endpoint_id
        # The endpoint name.
        self.endpoint_name = endpoint_name
        # The destination IP addresses.
        self.forward_ips = forward_ips
        # The ID of the forwarding rule.
        self.id = id
        # The name of the forwarding rule.
        self.name = name
        # The request ID.
        self.request_id = request_id
        # The type of the forwarding rule. Valid value:
        # 
        # OUTBOUND: outbound forwarding rule. This type of rule forwards Domain Name System (DNS) requests to one or more external IP addresses.
        self.type = type
        # The time when the forwarding rule was updated.
        self.update_time = update_time
        # The time when the forwarding rule was updated. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.update_timestamp = update_timestamp
        # The name of the forward zone.
        self.zone_name = zone_name

    def validate(self):
        if self.bind_edge_dns_clusters:
            for k in self.bind_edge_dns_clusters:
                if k:
                    k.validate()
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
        result['BindEdgeDnsClusters'] = []
        if self.bind_edge_dns_clusters is not None:
            for k in self.bind_edge_dns_clusters:
                result['BindEdgeDnsClusters'].append(k.to_map() if k else None)
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
        self.bind_edge_dns_clusters = []
        if m.get('BindEdgeDnsClusters') is not None:
            for k in m.get('BindEdgeDnsClusters'):
                temp_model = DescribeResolverRuleResponseBodyBindEdgeDnsClusters()
                self.bind_edge_dns_clusters.append(temp_model.from_map(k))
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
        # The outbound endpoint ID.
        self.endpoint_id = endpoint_id
        # The keyword of the forwarding rule name. Fuzzy search is supported. The value is not case-sensitive.
        self.keyword = keyword
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        # 
        # Default value: en.
        self.lang = lang
        # Specifies whether to return virtual private clouds (VPCs) associated with the forwarding rule. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.need_detail_attributes = need_detail_attributes
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 100. Default value: 20.
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


class DescribeResolverRulesResponseBodyRulesBindEdgeDnsClusters(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        cluster_user_id: int = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.cluster_user_id = cluster_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.cluster_user_id is not None:
            result['ClusterUserId'] = self.cluster_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ClusterUserId') is not None:
            self.cluster_user_id = m.get('ClusterUserId')
        return self


class DescribeResolverRulesResponseBodyRulesBindVpcs(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        region_name: str = None,
        vpc_id: str = None,
        vpc_name: str = None,
        vpc_type: str = None,
        vpc_user_id: str = None,
    ):
        # The region ID of the VPC.
        self.region_id = region_id
        # The name of the region to which the VPC belongs.
        self.region_name = region_name
        # The VPC ID. This ID uniquely identifies the VPC.
        self.vpc_id = vpc_id
        # The VPC name.
        self.vpc_name = vpc_name
        # The VPC type. Valid values:
        # 
        # *   STANDARD: standard VPC
        # *   EDS: Elastic Desktop Service (EDS) workspace VPC
        self.vpc_type = vpc_type
        # The user ID to which the VPC belongs.
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


class DescribeResolverRulesResponseBodyRulesForwardIps(TeaModel):
    def __init__(
        self,
        ip: str = None,
        port: int = None,
    ):
        # The IP address of the destination server.
        self.ip = ip
        # The port of the destination server.
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
        bind_edge_dns_clusters: List[DescribeResolverRulesResponseBodyRulesBindEdgeDnsClusters] = None,
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
        self.bind_edge_dns_clusters = bind_edge_dns_clusters
        # The VPCs associated with the forwarding rule.
        self.bind_vpcs = bind_vpcs
        # The time when the forwarding was created. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC.
        self.create_time = create_time
        # The time when the forwarding rule was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_timestamp = create_timestamp
        # The endpoint ID.
        self.endpoint_id = endpoint_id
        # The endpoint name.
        self.endpoint_name = endpoint_name
        # The IP addresses and ports of the external DNS servers. Enter the IP addresses and ports of the destination servers to which the DNS requests are forwarded.
        self.forward_ips = forward_ips
        # The ID of the forwarding rule.
        self.id = id
        # The name of the forwarding rule.
        self.name = name
        # The type of the forwarding rule.
        # 
        # The parameter value can only be OUTBOUND, which indicates that Domain Name System (DNS) requests are forwarded to one or more external IP addresses.
        self.type = type
        # The time when the forwarding rule was last modified. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC.
        self.update_time = update_time
        # The time when the forwarding rule was updated. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.update_timestamp = update_timestamp
        # The zone for which you want to forward DNS requests.
        self.zone_name = zone_name

    def validate(self):
        if self.bind_edge_dns_clusters:
            for k in self.bind_edge_dns_clusters:
                if k:
                    k.validate()
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
        result['BindEdgeDnsClusters'] = []
        if self.bind_edge_dns_clusters is not None:
            for k in self.bind_edge_dns_clusters:
                result['BindEdgeDnsClusters'].append(k.to_map() if k else None)
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
        self.bind_edge_dns_clusters = []
        if m.get('BindEdgeDnsClusters') is not None:
            for k in m.get('BindEdgeDnsClusters'):
                temp_model = DescribeResolverRulesResponseBodyRulesBindEdgeDnsClusters()
                self.bind_edge_dns_clusters.append(temp_model.from_map(k))
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
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The forwarding rules.
        self.rules = rules
        # The total number of entries returned.
        self.total_items = total_items
        # The total number of returned pages.
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
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        # 
        # Default value: en.
        self.lang = lang
        # The IP address of the client.
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
        # The region ID.
        self.region_id = region_id
        # The name of the region.
        self.region_name = region_name
        # The number of DNS requests on the previous day.
        self.request_count = request_count
        # The tunnel ID.
        self.tunnel_id = tunnel_id
        # The VPC ID.
        self.vpc_id = vpc_id
        # The VPC type. Valid values:
        # 
        # *   STANDARD: standard VPC
        # *   EDS: Elastic Desktop Service (EDS) workspace VPC
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
        # The business type. Valid values:
        # 
        # *   AUTH_ZONE: authoritative zone
        # *   RESOLVER_RULE: forwarding rule
        # *   INBOUND: inbound endpoint
        self.biz_type = biz_type
        # The number of DNS requests on the previous day.
        self.request_count = request_count
        # The zone name.
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
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count
        # The top three VPCs with the largest number of DNS requests.
        self.vpc_request_tops = vpc_request_tops
        # The top three zones with the largest number of DNS requests.
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
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        # 
        # Default value: en.
        self.lang = lang
        # The zone ID. This ID uniquely identifies the zone.
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
        # The synchronized region IDs.
        self.region_ids = region_ids
        # The user ID to which the region belongs. This parameter is used in cross-account synchronization scenarios.
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
        # The synchronized regions where the ECS instances are deployed.
        self.ecs_regions = ecs_regions
        # The synchronized region IDs of the ECS instances.
        self.regions = regions
        # The request ID.
        self.request_id = request_id
        # Indicates whether hostname automatic synchronization is enabled. Valid values:
        # 
        # *   ON: Hostname automatic synchronization is enabled. After this feature is enabled, the system automatically reads the hostnames of the Elastic Compute Service (ECS) instances in the specified regions and updates Domain Name System (DNS) records at an interval of 1 minute.
        # *   OFF: Hostname automatic synchronization is disabled.
        self.status = status
        # Indicates whether the task was successful. Valid values:
        # 
        # *   True
        # *   False
        self.success = success
        # The zone ID. This ID uniquely identifies the zone.
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
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        # 
        # Default value: en.
        self.lang = lang
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Maximum number: 1. Default value: 20.
        self.page_size = page_size
        # The resource type. Valid value: ZONE.
        # 
        # This parameter is required.
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
        # The key of tag N added to the resource.
        self.key = key
        # The values of tags added to the resources.
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
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The tags added to the resources.
        self.tags = tags
        # The total number of entries returned.
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


class DescribeUserServiceStatusRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        # 
        # Default value: en.
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeUserServiceStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        status: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # Current user\\"s service status:
        # 
        # *  **CLOSED**: Not activated
        # *  **OPENED**: Activated
        # *  **IN_DEBT**: Overdue payment
        # *  **IN_DEBT_OVER_DUE**: Payment overdue
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeUserServiceStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeUserServiceStatusResponseBody = None,
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
            temp_model = DescribeUserServiceStatusResponseBody()
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
        # The authorization scope. Valid values:
        # 
        # *   NORMAL: general authorization
        # *   CLOUD_PRODUCT: cloud service-related authorization
        self.auth_type = auth_type
        # The ID of the Alibaba Cloud account to which the permissions on the resources are granted.
        self.authorized_user_id = authorized_user_id
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 100. Default value: 20.
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
        create_time: str = None,
        create_timestamp: int = None,
    ):
        # The authorization scope. Valid values:
        # 
        # *   NORMAL: general authorization
        # *   CLOUD_PRODUCT: cloud service-related authorization
        self.auth_type = auth_type
        # The name of the Alibaba Cloud account to which the permissions on the resources are granted.
        self.authorized_aliyun_id = authorized_aliyun_id
        # The ID of the Alibaba Cloud account to which the permissions on the resources are granted.
        self.authorized_user_id = authorized_user_id
        # The time when the authorization was performed. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        # The time when the authorization was performed. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_timestamp = create_timestamp

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
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('AuthorizedAliyunId') is not None:
            self.authorized_aliyun_id = m.get('AuthorizedAliyunId')
        if m.get('AuthorizedUserId') is not None:
            self.authorized_user_id = m.get('AuthorizedUserId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
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
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_items = total_items
        # The total number of returned pages.
        self.total_pages = total_pages
        # The Alibaba Cloud accounts to which the permissions on the resources are granted.
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
        # The language of the response. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English.
        # 
        # Default value: **en**.
        self.lang = lang
        # The zone ID. This ID uniquely identifies the zone.
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


class DescribeZoneInfoResponseBodyBindEdgeDnsClustersEdgeDnsCluster(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        cluster_user_id: int = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.cluster_user_id = cluster_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.cluster_user_id is not None:
            result['ClusterUserId'] = self.cluster_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ClusterUserId') is not None:
            self.cluster_user_id = m.get('ClusterUserId')
        return self


class DescribeZoneInfoResponseBodyBindEdgeDnsClusters(TeaModel):
    def __init__(
        self,
        edge_dns_cluster: List[DescribeZoneInfoResponseBodyBindEdgeDnsClustersEdgeDnsCluster] = None,
    ):
        self.edge_dns_cluster = edge_dns_cluster

    def validate(self):
        if self.edge_dns_cluster:
            for k in self.edge_dns_cluster:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EdgeDnsCluster'] = []
        if self.edge_dns_cluster is not None:
            for k in self.edge_dns_cluster:
                result['EdgeDnsCluster'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.edge_dns_cluster = []
        if m.get('EdgeDnsCluster') is not None:
            for k in m.get('EdgeDnsCluster'):
                temp_model = DescribeZoneInfoResponseBodyBindEdgeDnsClustersEdgeDnsCluster()
                self.edge_dns_cluster.append(temp_model.from_map(k))
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
        # The region ID of the VPC.
        self.region_id = region_id
        # The name of the region where the VPC resides.
        self.region_name = region_name
        # The VPC ID. This ID uniquely identifies the VPC.
        self.vpc_id = vpc_id
        # The VPC name.
        self.vpc_name = vpc_name
        # The VPC type. Valid values:
        # 
        # *   STANDARD: standard VPC
        # *   EDS: Elastic Desktop Service (EDS) workspace VPC
        self.vpc_type = vpc_type
        # The user ID to which the VPC belongs. If null is returned, the VPC belongs to the current user.
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
        bind_edge_dns_clusters: DescribeZoneInfoResponseBodyBindEdgeDnsClusters = None,
        bind_vpcs: DescribeZoneInfoResponseBodyBindVpcs = None,
        create_time: str = None,
        create_timestamp: int = None,
        creator: str = None,
        creator_type: str = None,
        dns_group: str = None,
        dns_group_changing: bool = None,
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
        self.bind_edge_dns_clusters = bind_edge_dns_clusters
        # The VPCs associated with the zone.
        self.bind_vpcs = bind_vpcs
        # The time when the zone was created. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        # The time when the zone was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_timestamp = create_timestamp
        # The creator of the zone.
        self.creator = creator
        # The type of the creator.
        self.creator_type = creator_type
        # The logical location type of the built-in authoritative module in which the zone is added. Valid values:
        # 
        # *   **NORMAL_ZONE**: regular module
        # *   **FAST_ZONE**: acceleration module
        self.dns_group = dns_group
        # Indicates whether the zone is being removed to another logical location. Valid values:
        # 
        # *   true
        # *   false
        self.dns_group_changing = dns_group_changing
        # Indicates whether the zone is a reverse lookup zone. Valid values:
        # 
        # *   true
        # *   false
        self.is_ptr = is_ptr
        # Indicates whether the recursive resolution proxy for subdomain names is enabled. Valid values:
        # 
        # *   ZONE: The recursive resolution proxy for subdomain names is disabled. In this case, NXDOMAIN is returned if the queried domain name does not exist in the zone.
        # *   RECORD: The recursive resolution proxy for subdomain names is enabled. In this case, if the queried domain name does not exist in the zone, DNS requests are recursively forwarded to the forward module and then to the recursion module until DNS results are returned.
        self.proxy_pattern = proxy_pattern
        # The total number of DNS records added in the zone.
        self.record_count = record_count
        # The description of the zone.
        self.remark = remark
        # The request ID.
        self.request_id = request_id
        # The ID of the resource group to which the zone belongs.
        self.resource_group_id = resource_group_id
        # Indicates whether the secondary Domain Name System (DNS) feature is enabled for the zone. Valid values:
        # 
        # *   **true**: The secondary DNS feature is enabled.
        # *   **false**: The secondary DNS feature is disabled.
        self.slave_dns = slave_dns
        # The time when the zone was last updated. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.update_time = update_time
        # The time when the zone was last updated. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.update_timestamp = update_timestamp
        # The zone ID. This ID uniquely identifies the zone.
        self.zone_id = zone_id
        # The zone name.
        self.zone_name = zone_name
        # The tag added to the zone.
        self.zone_tag = zone_tag
        # The zone type. Valid values:
        # 
        # *   **AUTH_ZONE**: authoritative zone
        # *   **CLOUD_PRODUCT_ZONE**: authoritative zone for cloud services
        self.zone_type = zone_type

    def validate(self):
        if self.bind_edge_dns_clusters:
            self.bind_edge_dns_clusters.validate()
        if self.bind_vpcs:
            self.bind_vpcs.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bind_edge_dns_clusters is not None:
            result['BindEdgeDnsClusters'] = self.bind_edge_dns_clusters.to_map()
        if self.bind_vpcs is not None:
            result['BindVpcs'] = self.bind_vpcs.to_map()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.creator_type is not None:
            result['CreatorType'] = self.creator_type
        if self.dns_group is not None:
            result['DnsGroup'] = self.dns_group
        if self.dns_group_changing is not None:
            result['DnsGroupChanging'] = self.dns_group_changing
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
        if m.get('BindEdgeDnsClusters') is not None:
            temp_model = DescribeZoneInfoResponseBodyBindEdgeDnsClusters()
            self.bind_edge_dns_clusters = temp_model.from_map(m['BindEdgeDnsClusters'])
        if m.get('BindVpcs') is not None:
            temp_model = DescribeZoneInfoResponseBodyBindVpcs()
            self.bind_vpcs = temp_model.from_map(m['BindVpcs'])
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('CreatorType') is not None:
            self.creator_type = m.get('CreatorType')
        if m.get('DnsGroup') is not None:
            self.dns_group = m.get('DnsGroup')
        if m.get('DnsGroupChanging') is not None:
            self.dns_group_changing = m.get('DnsGroupChanging')
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


class DescribeZoneRecordRequest(TeaModel):
    def __init__(
        self,
        record_id: int = None,
    ):
        # The ID of the DNS record.
        # 
        # This parameter is required.
        self.record_id = record_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        return self


class DescribeZoneRecordResponseBody(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        create_timestamp: int = None,
        line: str = None,
        priority: int = None,
        record_id: int = None,
        remark: str = None,
        request_id: str = None,
        rr: str = None,
        status: str = None,
        ttl: int = None,
        type: str = None,
        update_time: str = None,
        update_timestamp: int = None,
        value: str = None,
        weight: int = None,
        zone_id: str = None,
    ):
        # The time when the DNS record was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        # The time when the DNS record was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_timestamp = create_timestamp
        # The resolution line.
        self.line = line
        # The priority of the mail exchanger (MX) record.
        self.priority = priority
        # The ID of the DNS record.
        self.record_id = record_id
        # The description of the DNS record.
        self.remark = remark
        # The request ID.
        self.request_id = request_id
        # The hostname.
        self.rr = rr
        # The state of the DNS record. Valid values:
        # 
        # *   **ENABLE**: The DNS record is enabled.
        # *   **DISABLE**: The DNS record is disabled.
        self.status = status
        # The time to live (TTL) of the DNS record.
        self.ttl = ttl
        # The type of the DNS record.
        self.type = type
        # The time when the DNS record was updated. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.update_time = update_time
        # The time when the DNS record was updated. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.update_timestamp = update_timestamp
        # The record value.
        self.value = value
        # The weight value of the DNS record.
        self.weight = weight
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        if self.line is not None:
            result['Line'] = self.line
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rr is not None:
            result['Rr'] = self.rr
        if self.status is not None:
            result['Status'] = self.status
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.update_timestamp is not None:
            result['UpdateTimestamp'] = self.update_timestamp
        if self.value is not None:
            result['Value'] = self.value
        if self.weight is not None:
            result['Weight'] = self.weight
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        if m.get('Line') is not None:
            self.line = m.get('Line')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Rr') is not None:
            self.rr = m.get('Rr')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeZoneRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeZoneRecordResponseBody = None,
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
            temp_model = DescribeZoneRecordResponseBody()
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
        # The keyword of the hostname. The value is not case-sensitive. You can set SearchMode to LIKE or EXACT. The default value of SearchMode is EXACT.
        self.keyword = keyword
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        # 
        # Default value: en.
        self.lang = lang
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.page_size = page_size
        # The search mode. Valid values:
        # 
        # *   **LIKE**: fuzzy search
        # *   **EXACT** (default): exact search
        # 
        # The value of Keyword is the search scope.
        self.search_mode = search_mode
        # The tag added to the DNS record. Valid values:
        # 
        # *   ecs: If you set Tag to ecs, the DNS records added to the hostnames of Elastic Compute Service (ECS) instances in the zone are queried.
        # *   If Tag is left empty, the DNS records in the zone are queried.
        self.tag = tag
        # The IP address of the client.
        self.user_client_ip = user_client_ip
        # The zone ID. This ID uniquely identifies the zone.
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
        create_time: str = None,
        create_timestamp: int = None,
        line: str = None,
        priority: int = None,
        record_id: int = None,
        remark: str = None,
        rr: str = None,
        status: str = None,
        ttl: int = None,
        type: str = None,
        update_time: str = None,
        update_timestamp: int = None,
        value: str = None,
        weight: int = None,
        zone_id: str = None,
    ):
        # The time when the DNS record was created. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        # The time when the DNS record was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_timestamp = create_timestamp
        # The resolution line.
        self.line = line
        # The priority of the mail exchanger (MX) record.
        self.priority = priority
        # The ID of the DNS record.
        self.record_id = record_id
        # The description of the DNS record.
        self.remark = remark
        # The hostname.
        self.rr = rr
        # The state of the DNS record. Valid values:
        # 
        # *   ENABLE: The DNS record is enabled.
        # *   DISABLE: The DNS record is disabled.
        self.status = status
        # The time to live (TTL) period.
        self.ttl = ttl
        # The type of the DNS record. Valid values:
        # 
        # *   **A**: An A record points a domain name to an IPv4 address.
        # *   **AAAA**: An AAAA record points a domain name to an IPv6 address.
        # *   **CNAME**: A canonical name (CNAME) record points a domain name to another domain name.
        # *   **TXT**: A text (TXT) record usually serves as a Sender Policy Framework (SPF) record to prevent email spam. The record value of the TXT record can be up to 255 characters in length.
        # *   **MX**: A mail exchanger (MX) record points a domain name to a mail server address.
        # *   **PTR**: A pointer (PTR) points an IP address to a domain name.
        # *   **SRV**: A service (SRV) record specifies a server that hosts a specific service.
        self.type = type
        # The time when the DNS record was updated. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.update_time = update_time
        # The time when the DNS record was updated. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.update_timestamp = update_timestamp
        # The record value.
        self.value = value
        # The weight value of the address. You can set a different weight value for each address. This way, addresses are returned based on the weight values for DNS requests. A weight value must be an integer that ranges from 1 to 100.
        self.weight = weight
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        if self.line is not None:
            result['Line'] = self.line
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
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.update_timestamp is not None:
            result['UpdateTimestamp'] = self.update_timestamp
        if self.value is not None:
            result['Value'] = self.value
        if self.weight is not None:
            result['Weight'] = self.weight
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        if m.get('Line') is not None:
            self.line = m.get('Line')
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
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
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
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The DNS records.
        self.records = records
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_items = total_items
        # The total number of pages returned.
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
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        # 
        # Default value: en.
        self.lang = lang
        # The IP address of the client.
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
        # The region ID of the VPC.
        self.region_id = region_id
        # The name of the region to which the VPC belongs.
        self.region_name = region_name
        # The VPC ID. The unique ID of the VPC.
        self.vpc_id = vpc_id
        # The VPC name.
        self.vpc_name = vpc_name
        # The VPC type. Valid values:
        # 
        # *   STANDARD: standard VPC
        # *   EDS: Elastic Desktop Service (EDS) workspace VPC
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
        creator: str = None,
        creator_type: str = None,
        dns_group: str = None,
        dns_group_changing: bool = None,
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
        # The time when the zone was created. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        # The time when the zone was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_timestamp = create_timestamp
        # The creator of the zone.
        self.creator = creator
        # The operator type.
        self.creator_type = creator_type
        # The logical location of the built-in authoritative module in which the zone is added. Valid values:
        # 
        # *   NORMAL_ZONE: regular module
        # *   FAST_ZONE: acceleration module
        self.dns_group = dns_group
        # Indicates whether the zone is being removed to another logical location. Valid values:
        # 
        # *   true
        # *   false
        self.dns_group_changing = dns_group_changing
        # Indicates whether the zone is a reverse lookup zone. Valid values:
        # 
        # *   true
        # *   false
        self.is_ptr = is_ptr
        # The number of Domain Name System (DNS) records added for the zone.
        self.record_count = record_count
        # The description of the zone.
        self.remark = remark
        # The time when the zone was last modified. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.update_time = update_time
        # The time when the zone was last modified. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.update_timestamp = update_timestamp
        # The VPCs associated with the zone.
        self.vpcs = vpcs
        # The zone ID. This ID uniquely identifies the zone.
        self.zone_id = zone_id
        # The zone name.
        self.zone_name = zone_name
        # The type of the cloud service.
        # 
        # 
        # **Valid values:**\
        # 
        # *   If ZoneType is set to AUTH_ZONE, no value is returned for this parameter.
        # 
        # *   If ZoneType is set to CLOUD_PRODUCT_ZONE, the type of the cloud service is returned.
        self.zone_tag = zone_tag
        # The zone type. Valid values:
        # 
        # *   AUTH_ZONE: authoritative zone
        # *   CLOUD_PRODUCT_ZONE: authoritative zone for cloud services
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
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.creator_type is not None:
            result['CreatorType'] = self.creator_type
        if self.dns_group is not None:
            result['DnsGroup'] = self.dns_group
        if self.dns_group_changing is not None:
            result['DnsGroupChanging'] = self.dns_group_changing
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
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('CreatorType') is not None:
            self.creator_type = m.get('CreatorType')
        if m.get('DnsGroup') is not None:
            self.dns_group = m.get('DnsGroup')
        if m.get('DnsGroupChanging') is not None:
            self.dns_group_changing = m.get('DnsGroupChanging')
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
        # The request ID.
        self.request_id = request_id
        # The zones.
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
        # The key of tag N added to the zone.
        self.key = key
        # The value of tag N added to the zone.
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
        # The keyword of the zone name. The value is not case-sensitive. You can set SearchMode to LIKE or EXACT. The default value of SearchMode is LIKE.
        self.keyword = keyword
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        # 
        # Default value: en.
        self.lang = lang
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: **1 to 100**. Default value: **20**.
        self.page_size = page_size
        # The region ID of the virtual private cloud (VPC) associated with the zone.
        self.query_region_id = query_region_id
        # The ID of the VPC associated with the zone.
        self.query_vpc_id = query_vpc_id
        # The ID of the resource group to which the zone belongs.
        self.resource_group_id = resource_group_id
        # The tags added to the zone.
        self.resource_tag = resource_tag
        # The search mode. The value of Keyword is the search scope. Valid values:
        # 
        # *   **LIKE** (default): fuzzy search
        # *   **EXACT**: exact search
        # 
        # Default value: **LIKE**.
        self.search_mode = search_mode
        # The types of cloud services.
        self.zone_tag = zone_tag
        # The zone type. Valid values:
        # 
        # *   **AUTH_ZONE**: authoritative zone
        # *   **CLOUD_PRODUCT_ZONE**: authoritative zone for cloud services
        # 
        # Default value: **AUTH_ZONE**.
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
        # The key of tag N added to the zone.
        self.key = key
        # The value of tag N added to the zone.
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
        creator: str = None,
        creator_sub_type: str = None,
        dns_group: str = None,
        dns_group_changing: bool = None,
        is_ptr: bool = None,
        proxy_pattern: str = None,
        record_count: int = None,
        remark: str = None,
        resource_group_id: str = None,
        resource_tags: DescribeZonesResponseBodyZonesZoneResourceTags = None,
        slave_dns_status: str = None,
        update_time: str = None,
        update_timestamp: int = None,
        zone_id: str = None,
        zone_name: str = None,
        zone_tag: str = None,
        zone_type: str = None,
    ):
        # The time when the zone was created. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        # The time when the zone was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_timestamp = create_timestamp
        # The creator of the zone.
        self.creator = creator
        # The account type. Valid values:
        # 
        # *   **CUSTOMER**: Alibaba Cloud account
        # *   **SUB**: RAM user
        # *   **STS**: assumed role that obtains the Security Token Service (STS) token of a RAM role
        # *   **OTHER**: other types
        self.creator_sub_type = creator_sub_type
        # The logical location type of the built-in authoritative module in which the zone is added. Valid values:
        # 
        # *   **NORMAL_ZONE**: regular module
        # *   **FAST_ZONE**: acceleration module
        self.dns_group = dns_group
        # Indicates whether the zone is being removed to another logical location. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.dns_group_changing = dns_group_changing
        # Indicates whether the zone is a reverse lookup zone. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.is_ptr = is_ptr
        # Indicates whether the recursive resolution proxy for subdomain names is enabled. Valid values:
        # 
        # *   **ZONE**: The recursive resolution proxy for subdomain names is disabled. In this case, NXDOMAIN is returned if the queried domain name does not exist in the zone.
        # *   **RECORD**: The recursive resolution proxy for subdomain names is enabled. In this case, if the queried domain name does not exist in the zone, DNS requests are recursively forwarded to the forward module and then to the recursion module until DNS results are returned.
        self.proxy_pattern = proxy_pattern
        # The number of Domain Name System (DNS) records added in the zone.
        self.record_count = record_count
        # The description of the zone.
        self.remark = remark
        # The ID of the resource group to which the zone belongs.
        self.resource_group_id = resource_group_id
        # The tags added to the zone.
        self.resource_tags = resource_tags
        self.slave_dns_status = slave_dns_status
        # The time when the zone was last modified. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.update_time = update_time
        # The time when the DNS record was updated. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since 00:00:00 UTC on January 1, 1970.
        self.update_timestamp = update_timestamp
        # The zone ID. This ID uniquely identifies the zone.
        self.zone_id = zone_id
        # The name of the zone.
        self.zone_name = zone_name
        # The type of the cloud service. Valid values:
        # 
        # *   If ZoneType is set to AUTH_ZONE, no value is returned for this parameter.
        # *   If ZoneType is set to CLOUD_PRODUCT_ZONE, the type of the cloud service is returned.
        self.zone_tag = zone_tag
        # The zone type. Valid values:
        # 
        # *   **AUTH_ZONE**: authoritative zone
        # *   **CLOUD_PRODUCT_ZONE**: authoritative zone for cloud services
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
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.creator_sub_type is not None:
            result['CreatorSubType'] = self.creator_sub_type
        if self.dns_group is not None:
            result['DnsGroup'] = self.dns_group
        if self.dns_group_changing is not None:
            result['DnsGroupChanging'] = self.dns_group_changing
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
        if self.slave_dns_status is not None:
            result['SlaveDnsStatus'] = self.slave_dns_status
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
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('CreatorSubType') is not None:
            self.creator_sub_type = m.get('CreatorSubType')
        if m.get('DnsGroup') is not None:
            self.dns_group = m.get('DnsGroup')
        if m.get('DnsGroupChanging') is not None:
            self.dns_group_changing = m.get('DnsGroupChanging')
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
        if m.get('SlaveDnsStatus') is not None:
            self.slave_dns_status = m.get('SlaveDnsStatus')
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
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_items = total_items
        # The total number of returned pages.
        self.total_pages = total_pages
        # The zones.
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
        # The key of tag N added to the resource.
        self.key = key
        # The value of tag N added to the resource.
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
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        # 
        # Default value: en.
        self.lang = lang
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        # The resource IDs, which are zone IDs. You can specify up to 50 zone IDs.
        self.resource_id = resource_id
        # The resource type. Valid value: ZONE.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The number of entries per page. Maximum value: 200. Default value: 20.
        self.size = size
        # The tags added to the resources.
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
        # The resource ID, which is a zone ID.
        self.resource_id = resource_id
        # The resource type.
        self.resource_type = resource_type
        # The key of tag N added to the resource.
        self.tag_key = tag_key
        # The value of tag N added to the resource.
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
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The tags added to the resources.
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
        client_token: str = None,
        lang: str = None,
        new_resource_group_id: str = None,
        resource_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        # 
        # Default value: en.
        self.lang = lang
        # The ID of the new resource group.
        # 
        # This parameter is required.
        self.new_resource_group_id = new_resource_group_id
        # The zone ID. This ID uniquely identifies the zone.
        # 
        # This parameter is required.
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.new_resource_group_id is not None:
            result['NewResourceGroupId'] = self.new_resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
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
        # The request ID.
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


class SearchCustomLinesRequest(TeaModel):
    def __init__(
        self,
        create_timestamp_end: int = None,
        create_timestamp_start: int = None,
        creator: List[str] = None,
        ipv_4: str = None,
        lang: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        update_timestamp_end: int = None,
        update_timestamp_start: int = None,
    ):
        # The end of the time range during which the custom lines are created to query. Set the time to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_timestamp_end = create_timestamp_end
        # The beginning of the time range during which the custom lines are created to query. Set the time to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_timestamp_start = create_timestamp_start
        # The IDs of the creators for the custom lines.
        self.creator = creator
        # The IPv4 address.
        self.ipv_4 = ipv_4
        # The language.
        self.lang = lang
        # The name of the custom line.
        self.name = name
        # The page number. Pages start from page **1**. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Valid values: **1 to 100**. Default value: **10**.
        self.page_size = page_size
        # The end of the time range during which the custom lines are updated to query. Set the time to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.update_timestamp_end = update_timestamp_end
        # The beginning of the time range during which the custom lines are updated to query. Set the time to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.update_timestamp_start = update_timestamp_start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_timestamp_end is not None:
            result['CreateTimestampEnd'] = self.create_timestamp_end
        if self.create_timestamp_start is not None:
            result['CreateTimestampStart'] = self.create_timestamp_start
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.ipv_4 is not None:
            result['Ipv4'] = self.ipv_4
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.update_timestamp_end is not None:
            result['UpdateTimestampEnd'] = self.update_timestamp_end
        if self.update_timestamp_start is not None:
            result['UpdateTimestampStart'] = self.update_timestamp_start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTimestampEnd') is not None:
            self.create_timestamp_end = m.get('CreateTimestampEnd')
        if m.get('CreateTimestampStart') is not None:
            self.create_timestamp_start = m.get('CreateTimestampStart')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('Ipv4') is not None:
            self.ipv_4 = m.get('Ipv4')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('UpdateTimestampEnd') is not None:
            self.update_timestamp_end = m.get('UpdateTimestampEnd')
        if m.get('UpdateTimestampStart') is not None:
            self.update_timestamp_start = m.get('UpdateTimestampStart')
        return self


class SearchCustomLinesResponseBodyCustomLinesCustomLineIpv4s(TeaModel):
    def __init__(
        self,
        ipv_4: List[str] = None,
    ):
        self.ipv_4 = ipv_4

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ipv_4 is not None:
            result['Ipv4'] = self.ipv_4
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ipv4') is not None:
            self.ipv_4 = m.get('Ipv4')
        return self


class SearchCustomLinesResponseBodyCustomLinesCustomLine(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        create_timestamp: int = None,
        creator: str = None,
        creator_sub_type: str = None,
        creator_type: str = None,
        dns_category: str = None,
        ipv_4s: SearchCustomLinesResponseBodyCustomLinesCustomLineIpv4s = None,
        line_id: str = None,
        name: str = None,
        update_time: str = None,
        update_timestamp: int = None,
    ):
        # The time when the custom line was created.
        self.create_time = create_time
        # The time when the custom line was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_timestamp = create_timestamp
        # The ID of the creator for the custom line.
        self.creator = creator
        # The creator type. Valid values:
        # 
        # *   CUSTOM: Alibaba Cloud account
        # *   SUB: RAM user
        # *   STS: assumed role that obtains the Security Token Service (STS) token of a RAM role
        # *   OTHER: other types
        self.creator_sub_type = creator_sub_type
        # The role of the creator for the custom line. Valid values:
        # 
        # *   USER: user
        # *   SYSTEM: system
        self.creator_type = creator_type
        self.dns_category = dns_category
        # The IPv4 CIDR blocks.
        self.ipv_4s = ipv_4s
        # The unique ID of the custom line.
        self.line_id = line_id
        # The name of the custom line.
        self.name = name
        # The time when the custom line was updated.
        self.update_time = update_time
        # The time when the custom line was updated. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.update_timestamp = update_timestamp

    def validate(self):
        if self.ipv_4s:
            self.ipv_4s.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.creator_sub_type is not None:
            result['CreatorSubType'] = self.creator_sub_type
        if self.creator_type is not None:
            result['CreatorType'] = self.creator_type
        if self.dns_category is not None:
            result['DnsCategory'] = self.dns_category
        if self.ipv_4s is not None:
            result['Ipv4s'] = self.ipv_4s.to_map()
        if self.line_id is not None:
            result['LineId'] = self.line_id
        if self.name is not None:
            result['Name'] = self.name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.update_timestamp is not None:
            result['UpdateTimestamp'] = self.update_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('CreatorSubType') is not None:
            self.creator_sub_type = m.get('CreatorSubType')
        if m.get('CreatorType') is not None:
            self.creator_type = m.get('CreatorType')
        if m.get('DnsCategory') is not None:
            self.dns_category = m.get('DnsCategory')
        if m.get('Ipv4s') is not None:
            temp_model = SearchCustomLinesResponseBodyCustomLinesCustomLineIpv4s()
            self.ipv_4s = temp_model.from_map(m['Ipv4s'])
        if m.get('LineId') is not None:
            self.line_id = m.get('LineId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')
        return self


class SearchCustomLinesResponseBodyCustomLines(TeaModel):
    def __init__(
        self,
        custom_line: List[SearchCustomLinesResponseBodyCustomLinesCustomLine] = None,
    ):
        self.custom_line = custom_line

    def validate(self):
        if self.custom_line:
            for k in self.custom_line:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CustomLine'] = []
        if self.custom_line is not None:
            for k in self.custom_line:
                result['CustomLine'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_line = []
        if m.get('CustomLine') is not None:
            for k in m.get('CustomLine'):
                temp_model = SearchCustomLinesResponseBodyCustomLinesCustomLine()
                self.custom_line.append(temp_model.from_map(k))
        return self


class SearchCustomLinesResponseBody(TeaModel):
    def __init__(
        self,
        custom_lines: SearchCustomLinesResponseBodyCustomLines = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_items: int = None,
        total_pages: int = None,
    ):
        # The custom lines.
        self.custom_lines = custom_lines
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: **1 to 100**. Default value: **10**.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_items = total_items
        # The total number of returned pages.
        self.total_pages = total_pages

    def validate(self):
        if self.custom_lines:
            self.custom_lines.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_lines is not None:
            result['CustomLines'] = self.custom_lines.to_map()
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
        if m.get('CustomLines') is not None:
            temp_model = SearchCustomLinesResponseBodyCustomLines()
            self.custom_lines = temp_model.from_map(m['CustomLines'])
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


class SearchCustomLinesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchCustomLinesResponseBody = None,
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
            temp_model = SearchCustomLinesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetProxyPatternRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        lang: str = None,
        proxy_pattern: str = None,
        user_client_ip: str = None,
        zone_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        # 
        # Default value: en.
        self.lang = lang
        # Specifies whether to enable the recursive resolution proxy for subdomain names. Valid values:
        # 
        # *   **ZONE**: disables the recursive resolution proxy for subdomain names. In this case, NXDOMAIN is returned if the queried subdomain name does not exist in the zone.
        # *   **RECORD**: enables the recursive resolution proxy for subdomain names. In this case, if the queried domain name does not exist in the zone, Domain Name System (DNS) requests are recursively forwarded to the forward module and then to the recursion module until DNS results are returned.
        # 
        # This parameter is required.
        self.proxy_pattern = proxy_pattern
        # The IP address of the client.
        self.user_client_ip = user_client_ip
        # The zone ID. This ID uniquely identifies the zone.
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
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
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
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
        # The request ID.
        self.request_id = request_id
        # The global ID of the zone.
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
        client_token: str = None,
        lang: str = None,
        record_id: int = None,
        status: str = None,
        user_client_ip: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        # 
        # Default value: en.
        self.lang = lang
        # The ID of the DNS record.
        # 
        # This parameter is required.
        self.record_id = record_id
        # The state of the DNS record. Valid values:
        # 
        # *   ENABLE: enables the DNS record.
        # *   DISABLE: suspends the DNS record.
        # 
        # This parameter is required.
        self.status = status
        # The IP address of the client.
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
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
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
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
        # The ID of the DNS record.
        self.record_id = record_id
        # The request ID.
        self.request_id = request_id
        # The state of the DNS record. Valid values:
        # 
        # *   ENABLE: The DNS record is enabled.
        # *   DISABLE: The DNS record is disabled.
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
        # The key of tag N to add to the resources.
        self.key = key
        # The value of tag N to add to the resources.
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
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        # 
        # Default value: en.
        self.lang = lang
        # Specifies whether to replace the original tags added to the resources. Valid values:
        # 
        # *   True: replaces the original tags.
        # *   False (default): appends the specified one or more tags to the original tags. If a new tag has the same key but a different value from an original tag, the new tag replaces the original tag.
        self.over_write = over_write
        # The resource IDs, which are zone IDs. You can specify up to 50 zone IDs.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The resource type. Valid value: ZONE.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tags to add to the resources.
        # 
        # This parameter is required.
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
        # The request ID.
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
        # Specifies whether to remove all tags of the specified zones. Valid values:
        # 
        # *   true: removes all tags of the specified zones.
        # *   false: removes only the tags with the specified tag keys.
        # 
        # Default value: false.
        self.all = all
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        # 
        # Default value: en.
        self.lang = lang
        # The resource IDs, which are zone IDs. You can specify up to 50 zone IDs.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The resource type. The value of ResourceType can only be ZONE.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The keys of tags that you want to remove. You can specify up to 20 tag keys.
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
        # The request ID.
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


class UpdateCustomLineRequest(TeaModel):
    def __init__(
        self,
        dns_category: str = None,
        ipv_4s: List[str] = None,
        lang: str = None,
        line_id: str = None,
        name: str = None,
    ):
        self.dns_category = dns_category
        # The IPv4 CIDR blocks.
        # 
        # This parameter is required.
        self.ipv_4s = ipv_4s
        # The language.
        self.lang = lang
        # The unique ID of the custom line.
        # 
        # This parameter is required.
        self.line_id = line_id
        # The name of the custom line.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dns_category is not None:
            result['DnsCategory'] = self.dns_category
        if self.ipv_4s is not None:
            result['Ipv4s'] = self.ipv_4s
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.line_id is not None:
            result['LineId'] = self.line_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DnsCategory') is not None:
            self.dns_category = m.get('DnsCategory')
        if m.get('Ipv4s') is not None:
            self.ipv_4s = m.get('Ipv4s')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('LineId') is not None:
            self.line_id = m.get('LineId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateCustomLineResponseBody(TeaModel):
    def __init__(
        self,
        line_id: str = None,
        request_id: str = None,
    ):
        # The unique ID of the custom line.
        self.line_id = line_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.line_id is not None:
            result['LineId'] = self.line_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LineId') is not None:
            self.line_id = m.get('LineId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateCustomLineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateCustomLineResponseBody = None,
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
            temp_model = UpdateCustomLineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRecordRemarkRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        lang: str = None,
        record_id: int = None,
        remark: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        # 
        # Default value: en.
        self.lang = lang
        # The ID of the DNS record.
        # 
        # This parameter is required.
        self.record_id = record_id
        # The description of the DNS record.
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
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
        # The ID of the DNS record.
        self.record_id = record_id
        # The request ID.
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
        # The ID of the zone to which the vSwitch belongs.
        self.az_id = az_id
        # The IPv4 CIDR block of the vSwitch.
        self.cidr_block = cidr_block
        # The source IP address of outbound traffic. The IP address must be within the specified CIDR block. If you leave this parameter empty, the system automatically allocates an IP address.
        self.ip = ip
        # The vSwitch ID.
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
        # The endpoint ID.
        # 
        # This parameter is required.
        self.endpoint_id = endpoint_id
        # The source IP addresses of outbound traffic. You can add two to six IP addresses.
        # 
        # >  You must add at least two source IP addresses for outbound traffic to ensure high availability. We recommend that you add two IP addresses that reside in different zones. You can add up to six source IP addresses.
        self.ip_config = ip_config
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        # 
        # Default value: en.
        self.lang = lang
        # The endpoint name.
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
        # The request ID.
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
        # The IP address of the destination server.
        # 
        # >  You cannot specify the following IP addresses as the IP addresses of the external DNS servers because the IP addresses are reserved by the system: 100.100.2.136 to 100.100.2.138, and 100.100.2.116 to 100.100.2.118.
        self.ip = ip
        # The port of the destination server.
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
        endpoint_id: str = None,
        forward_ip: List[UpdateResolverRuleRequestForwardIp] = None,
        lang: str = None,
        name: str = None,
        rule_id: str = None,
    ):
        # The endpoint ID.
        self.endpoint_id = endpoint_id
        # The IP addresses and ports of the external Domain Name System (DNS) servers. Enter the IP addresses and ports of the destination servers to which the DNS requests are forwarded. You can enter up to six IP addresses and ports. Both private and public IP addresses are supported.
        # 
        # >  If you specify public IP addresses as the IP addresses of the external DNS servers and Elastic Compute Service (ECS) instances in the outbound virtual private cloud (VPC) are not assigned public IP addresses, you need to activate NAT Gateway for the VPC and create and manage SNAT entries on a NAT gateway.
        self.forward_ip = forward_ip
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        # 
        # Default value: en.
        self.lang = lang
        # The name of the forwarding rule.
        self.name = name
        # The ID of the forwarding rule.
        # 
        # This parameter is required.
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
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
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
        # The request ID.
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
        # The region ID.
        self.region_id = region_id
        # The user ID to which the region belongs. This parameter is used in cross-account synchronization scenarios.
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
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        # 
        # Default value: en.
        self.lang = lang
        # The regions to be synchronized.
        # 
        # This parameter is required.
        self.region = region
        # The state of the hostname synchronization task. Valid values:
        # 
        # *   ON: The task is started.
        # *   OFF: The task is ended.
        # 
        # This parameter is required.
        self.status = status
        # The zone ID. This ID uniquely identifies the zone.
        # 
        # This parameter is required.
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
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
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
        client_token: str = None,
        lang: str = None,
        line: str = None,
        priority: int = None,
        record_id: int = None,
        rr: str = None,
        ttl: int = None,
        type: str = None,
        user_client_ip: str = None,
        value: str = None,
        weight: int = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        # 
        # Default value: en.
        self.lang = lang
        # The resolution line. Default value: default.
        self.line = line
        # The priority of the MX record. You can set priorities for different email servers. Valid values: 1 to 99. A smaller value indicates a higher priority.
        # 
        # >  This parameter is required if the type of the DNS record is MX.
        self.priority = priority
        # The ID of the DNS record. You can call the DescribeZoneRecords operation to query a list of DNS records.
        # 
        # This parameter is required.
        self.record_id = record_id
        # The hostname. The hostname is the prefix of the subdomain name for zone. Example: www, @, \\* (used for wildcard DNS resolution), and mail (used for specifying the mail server that receives emails).
        # 
        # For example, if you want to resolve the domain name @.exmaple.com, you must set Rr to @ instead of leaving Rr empty.
        # 
        # This parameter is required.
        self.rr = rr
        # The TTL period. Valid values: 5, 30, 60, 3600, 43200, and 86400. Unit: seconds.
        self.ttl = ttl
        # The type of the DNS record. Valid values:
        # 
        # *   **A**: An A record maps a domain name to an IPv4 address in the dotted decimal notation format.
        # *   **AAAA**: An AAAA record maps a domain name to an IPv6 address.
        # *   **CNAME**: A canonical name (CNAME) record maps a domain name to another domain name.
        # *   **TXT**: A text (TXT) record usually serves as a Sender Policy Framework (SPF) record to prevent email spam. The record value of the TXT record can be up to 255 characters in length.
        # *   **MX**: A mail exchanger (MX) record maps a domain name to the domain name of a mail server.
        # *   **PTR**: A pointer (PTR) record maps an IP address to a domain name.
        # *   **SRV**: A service (SRV) record specifies a server that hosts a specific service. Enter a record value in the format of Priority Weight Port Destination domain name. Separate these items with spaces.
        # 
        # >  Before you add a PTR record, you must configure a reverse lookup zone. For more information, see [Add PTR records](https://help.aliyun.com/document_detail/2592976.html).
        # 
        # This parameter is required.
        self.type = type
        # The IP address of the client.
        self.user_client_ip = user_client_ip
        # The record value. You need to enter the record value based on the DNS record type.
        # 
        # This parameter is required.
        self.value = value
        # The weight value of the address. You can set a different weight value for each address. This way, addresses are returned based on the weight values for DNS requests. A weight value must be an integer that ranges from 1 to 100.
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.line is not None:
            result['Line'] = self.line
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
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Line') is not None:
            self.line = m.get('Line')
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
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class UpdateZoneRecordResponseBody(TeaModel):
    def __init__(
        self,
        record_id: int = None,
        request_id: str = None,
    ):
        # The ID of the DNS record.
        self.record_id = record_id
        # The request ID.
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
        client_token: str = None,
        lang: str = None,
        remark: str = None,
        user_client_ip: str = None,
        zone_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        # 
        # Default value: en.
        self.lang = lang
        # The new description. If you leave Remark empty, the zone has no description.
        self.remark = remark
        # The IP address of the client.
        self.user_client_ip = user_client_ip
        # The zone ID. This ID uniquely identifies the zone.
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
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
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
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
        # The request ID.
        self.request_id = request_id
        # The zone ID. This ID uniquely identifies the zone.
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


