# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_epg20260715 import models as main_models
from darabonba.model import DaraModel

class CreateEgressProxyGatewayRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        dry_run: bool = None,
        egress_proxy_configuration_id: str = None,
        egress_proxy_gateway_name: str = None,
        listener_properties: List[main_models.CreateEgressProxyGatewayRequestListenerProperties] = None,
        resource_group_id: str = None,
        tag: List[main_models.CreateEgressProxyGatewayRequestTag] = None,
        tls_intercept_properties: main_models.CreateEgressProxyGatewayRequestTlsInterceptProperties = None,
        vpc_id: str = None,
        zone_mappings: List[main_models.CreateEgressProxyGatewayRequestZoneMappings] = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > Note If you do not specify this parameter, the system automatically uses the RequestId of the API request as the client token. The RequestId of each API request is unique.
        self.client_token = client_token
        # The description of the egress proxy gateway instance.
        # 
        # The description must be 2 to 256 characters in length, and can contain Chinese characters, letters, digits, commas (,), periods (.), semicolons (;), forward slashes (/), at signs (@), underscores (_), and hyphens (-).
        self.description = description
        # Specifies whether to only precheck the request. Valid values:
        # 
        # - **true**: prechecks the request without creating the egress proxy gateway instance. The system checks whether required parameters are specified, the request format, and service limits. If the request fails the precheck, the corresponding error is returned. If the request passes the precheck, the DryRunOperation error code is returned.
        # 
        # - **false** (default): sends the request. If the request passes the precheck, the HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The ID of the egress proxy configuration that is associated with the egress proxy gateway instance.
        # 
        # This parameter is required.
        self.egress_proxy_configuration_id = egress_proxy_configuration_id
        # The name of the egress proxy gateway instance.
        # 
        # The name must be 2 to 128 characters in length, and must start with a letter or a Chinese character. It can contain Chinese characters, letters, digits, periods (.), underscores (_), and hyphens (-).
        # 
        # This parameter is required.
        self.egress_proxy_gateway_name = egress_proxy_gateway_name
        # The listener configurations of the egress proxy gateway instance.
        # 
        # Listeners in the same gateway instance cannot use the same port.
        # 
        # This parameter is required.
        self.listener_properties = listener_properties
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The tags.
        self.tag = tag
        # The TLS interception configuration of the egress proxy gateway instance.
        self.tls_intercept_properties = tls_intercept_properties
        # The ID of the virtual private cloud (VPC) to which the egress proxy gateway instance belongs.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id
        # The zone and vSwitch mappings of the egress proxy gateway instance.
        # 
        # If the current region supports two or more zones, add at least two zones to improve availability.
        # 
        # This parameter is required.
        self.zone_mappings = zone_mappings

    def validate(self):
        if self.listener_properties:
            for v1 in self.listener_properties:
                 if v1:
                    v1.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()
        if self.tls_intercept_properties:
            self.tls_intercept_properties.validate()
        if self.zone_mappings:
            for v1 in self.zone_mappings:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.egress_proxy_configuration_id is not None:
            result['EgressProxyConfigurationId'] = self.egress_proxy_configuration_id

        if self.egress_proxy_gateway_name is not None:
            result['EgressProxyGatewayName'] = self.egress_proxy_gateway_name

        result['ListenerProperties'] = []
        if self.listener_properties is not None:
            for k1 in self.listener_properties:
                result['ListenerProperties'].append(k1.to_map() if k1 else None)

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.tls_intercept_properties is not None:
            result['TlsInterceptProperties'] = self.tls_intercept_properties.to_map()

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        result['ZoneMappings'] = []
        if self.zone_mappings is not None:
            for k1 in self.zone_mappings:
                result['ZoneMappings'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EgressProxyConfigurationId') is not None:
            self.egress_proxy_configuration_id = m.get('EgressProxyConfigurationId')

        if m.get('EgressProxyGatewayName') is not None:
            self.egress_proxy_gateway_name = m.get('EgressProxyGatewayName')

        self.listener_properties = []
        if m.get('ListenerProperties') is not None:
            for k1 in m.get('ListenerProperties'):
                temp_model = main_models.CreateEgressProxyGatewayRequestListenerProperties()
                self.listener_properties.append(temp_model.from_map(k1))

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateEgressProxyGatewayRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TlsInterceptProperties') is not None:
            temp_model = main_models.CreateEgressProxyGatewayRequestTlsInterceptProperties()
            self.tls_intercept_properties = temp_model.from_map(m.get('TlsInterceptProperties'))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        self.zone_mappings = []
        if m.get('ZoneMappings') is not None:
            for k1 in m.get('ZoneMappings'):
                temp_model = main_models.CreateEgressProxyGatewayRequestZoneMappings()
                self.zone_mappings.append(temp_model.from_map(k1))

        return self

class CreateEgressProxyGatewayRequestZoneMappings(DaraModel):
    def __init__(
        self,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # The ID of the vSwitch that corresponds to the zone.
        # 
        # The vSwitch must belong to the specified VPC and match the zone specified by ZoneId.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # The zone ID.
        # 
        # You can call the DescribeZones operation to query information about zones in a region.
        # 
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class CreateEgressProxyGatewayRequestTlsInterceptProperties(DaraModel):
    def __init__(
        self,
        private_ca_certificate_id: str = None,
        tls_intercept_mode: str = None,
    ):
        # The ID of the private CA certificate.
        # 
        # - This parameter is required when **TlsInterceptMode** is set to **enable**.
        # - Do not specify this parameter when **TlsInterceptMode** is set to **disable**.
        self.private_ca_certificate_id = private_ca_certificate_id
        # Specifies whether to enable TLS interception. Valid values:
        # 
        # - **enable**: enables TLS interception.
        # 
        # - **disable**: disables TLS interception.
        # 
        # This parameter is required.
        self.tls_intercept_mode = tls_intercept_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.private_ca_certificate_id is not None:
            result['PrivateCaCertificateId'] = self.private_ca_certificate_id

        if self.tls_intercept_mode is not None:
            result['TlsInterceptMode'] = self.tls_intercept_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrivateCaCertificateId') is not None:
            self.private_ca_certificate_id = m.get('PrivateCaCertificateId')

        if m.get('TlsInterceptMode') is not None:
            self.tls_intercept_mode = m.get('TlsInterceptMode')

        return self

class CreateEgressProxyGatewayRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. The key can be up to 128 characters in length. It cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
        self.key = key
        # The tag value. The value can be up to 256 characters in length, and cannot contain `http://` or `https://`.
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

class CreateEgressProxyGatewayRequestListenerProperties(DaraModel):
    def __init__(
        self,
        port: int = None,
        protocol: str = None,
    ):
        # The listener port.
        # 
        # Valid values: **1** to **65535**.
        # 
        # This parameter is required.
        self.port = port
        # The protocol type of the listener. Valid values:
        # 
        # - **HTTP**: HTTP.
        # 
        # - **HTTPS**: HTTPS.
        # 
        # This parameter is required.
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.port is not None:
            result['Port'] = self.port

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        return self

