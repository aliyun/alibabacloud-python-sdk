# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_epg20260715 import models as main_models
from darabonba.model import DaraModel

class GetEgressProxyGatewayAttributeResponseBody(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        default_egress_proxy_ip_pool_id: str = None,
        description: str = None,
        dns_name: str = None,
        egress_proxy_configuration_id: str = None,
        egress_proxy_gateway_id: str = None,
        egress_proxy_gateway_name: str = None,
        listener_properties: List[main_models.GetEgressProxyGatewayAttributeResponseBodyListenerProperties] = None,
        request_id: str = None,
        resource_group_id: str = None,
        status: str = None,
        tags: List[main_models.GetEgressProxyGatewayAttributeResponseBodyTags] = None,
        tls_intercept_properties: main_models.GetEgressProxyGatewayAttributeResponseBodyTlsInterceptProperties = None,
        vpc_id: str = None,
        zone_mappings: List[main_models.GetEgressProxyGatewayAttributeResponseBodyZoneMappings] = None,
    ):
        # The time when the egress proxy gateway was created. The time is displayed in UTC and follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format.
        self.create_time = create_time
        # The ID of the default egress IP pool.
        self.default_egress_proxy_ip_pool_id = default_egress_proxy_ip_pool_id
        # The description of the egress proxy gateway instance. The description must be 2 to 256 characters in length and can contain Chinese characters and English letters. It can also contain digits, commas (,), periods (.), semicolons (;), forward slashes (/), at signs (@), underscores (_), and hyphens (-).
        self.description = description
        # The DNS domain name.
        self.dns_name = dns_name
        # The ID of the associated egress proxy configuration.
        self.egress_proxy_configuration_id = egress_proxy_configuration_id
        # The ID of the egress proxy gateway instance.
        self.egress_proxy_gateway_id = egress_proxy_gateway_id
        # The name of the egress proxy gateway. The name must be 2 to 128 characters in length and can contain English letters and Chinese characters. It must start with a letter or a Chinese character and can contain digits, periods (.), underscores (_), and hyphens (-).
        self.egress_proxy_gateway_name = egress_proxy_gateway_name
        # The list of listener properties.
        self.listener_properties = listener_properties
        # The request ID.
        self.request_id = request_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The instance status of the egress proxy gateway. Valid values:
        # 
        # - **Provisioning**: The instance is being created.
        # - **Active**: The instance is running.
        # - **Configuring**: The instance is being reconfigured.
        # - **Inactive**: The instance is stopped.
        self.status = status
        # The list of tags.
        self.tags = tags
        # The TLS interception properties.
        self.tls_intercept_properties = tls_intercept_properties
        # The ID of the virtual private cloud (VPC).
        self.vpc_id = vpc_id
        # The list of zone and vSwitch mappings. If the current region supports two or more zones, at least two zones must be returned.
        self.zone_mappings = zone_mappings

    def validate(self):
        if self.listener_properties:
            for v1 in self.listener_properties:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
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
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.default_egress_proxy_ip_pool_id is not None:
            result['DefaultEgressProxyIpPoolId'] = self.default_egress_proxy_ip_pool_id

        if self.description is not None:
            result['Description'] = self.description

        if self.dns_name is not None:
            result['DnsName'] = self.dns_name

        if self.egress_proxy_configuration_id is not None:
            result['EgressProxyConfigurationId'] = self.egress_proxy_configuration_id

        if self.egress_proxy_gateway_id is not None:
            result['EgressProxyGatewayId'] = self.egress_proxy_gateway_id

        if self.egress_proxy_gateway_name is not None:
            result['EgressProxyGatewayName'] = self.egress_proxy_gateway_name

        result['ListenerProperties'] = []
        if self.listener_properties is not None:
            for k1 in self.listener_properties:
                result['ListenerProperties'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

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
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DefaultEgressProxyIpPoolId') is not None:
            self.default_egress_proxy_ip_pool_id = m.get('DefaultEgressProxyIpPoolId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DnsName') is not None:
            self.dns_name = m.get('DnsName')

        if m.get('EgressProxyConfigurationId') is not None:
            self.egress_proxy_configuration_id = m.get('EgressProxyConfigurationId')

        if m.get('EgressProxyGatewayId') is not None:
            self.egress_proxy_gateway_id = m.get('EgressProxyGatewayId')

        if m.get('EgressProxyGatewayName') is not None:
            self.egress_proxy_gateway_name = m.get('EgressProxyGatewayName')

        self.listener_properties = []
        if m.get('ListenerProperties') is not None:
            for k1 in m.get('ListenerProperties'):
                temp_model = main_models.GetEgressProxyGatewayAttributeResponseBodyListenerProperties()
                self.listener_properties.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetEgressProxyGatewayAttributeResponseBodyTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TlsInterceptProperties') is not None:
            temp_model = main_models.GetEgressProxyGatewayAttributeResponseBodyTlsInterceptProperties()
            self.tls_intercept_properties = temp_model.from_map(m.get('TlsInterceptProperties'))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        self.zone_mappings = []
        if m.get('ZoneMappings') is not None:
            for k1 in m.get('ZoneMappings'):
                temp_model = main_models.GetEgressProxyGatewayAttributeResponseBodyZoneMappings()
                self.zone_mappings.append(temp_model.from_map(k1))

        return self

class GetEgressProxyGatewayAttributeResponseBodyZoneMappings(DaraModel):
    def __init__(
        self,
        status: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # The zone status. Valid values:
        # 
        # - **Provisioning**: The zone is being created.
        # - **Available**: The zone is available.
        # - **Configuring**: The zone is being reconfigured.
        self.status = status
        # The ID of the vSwitch that corresponds to the zone.
        self.v_switch_id = v_switch_id
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['Status'] = self.status

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class GetEgressProxyGatewayAttributeResponseBodyTlsInterceptProperties(DaraModel):
    def __init__(
        self,
        private_ca_certificate_id: str = None,
        tls_intercept_mode: str = None,
    ):
        # The ID of the private CA certificate.
        self.private_ca_certificate_id = private_ca_certificate_id
        # The TLS Block Mode. Valid values:
        # 
        # - **enable**: Enables the TLS Block Mode.
        # - **disable**: Disables the TLS Block Mode.
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

class GetEgressProxyGatewayAttributeResponseBodyTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. The key can be up to 128 characters in length. It cannot start with aliyun or acs: and cannot contain http:// or https://.
        self.key = key
        # The tag value. The value can be up to 256 characters in length and cannot contain http:// or https://.
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

class GetEgressProxyGatewayAttributeResponseBodyListenerProperties(DaraModel):
    def __init__(
        self,
        port: int = None,
        protocol: str = None,
    ):
        # The listener port. Valid values: 1 to 65535.
        self.port = port
        # The listener protocol. Valid values:
        # 
        # - **HTTP**
        # - **HTTPS**
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

