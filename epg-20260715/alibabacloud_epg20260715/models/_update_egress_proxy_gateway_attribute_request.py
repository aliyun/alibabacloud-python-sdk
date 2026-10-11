# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_epg20260715 import models as main_models
from darabonba.model import DaraModel

class UpdateEgressProxyGatewayAttributeRequest(DaraModel):
    def __init__(
        self,
        add_listener_properties: List[main_models.UpdateEgressProxyGatewayAttributeRequestAddListenerProperties] = None,
        client_token: str = None,
        default_egress_proxy_ip_pool_id: str = None,
        description: str = None,
        dry_run: bool = None,
        egress_proxy_gateway_id: str = None,
        egress_proxy_gateway_name: str = None,
        remove_listener_properties: List[main_models.UpdateEgressProxyGatewayAttributeRequestRemoveListenerProperties] = None,
        tls_intercept_properties: main_models.UpdateEgressProxyGatewayAttributeRequestTlsInterceptProperties = None,
    ):
        self.add_listener_properties = add_listener_properties
        self.client_token = client_token
        self.default_egress_proxy_ip_pool_id = default_egress_proxy_ip_pool_id
        self.description = description
        self.dry_run = dry_run
        # This parameter is required.
        self.egress_proxy_gateway_id = egress_proxy_gateway_id
        self.egress_proxy_gateway_name = egress_proxy_gateway_name
        self.remove_listener_properties = remove_listener_properties
        self.tls_intercept_properties = tls_intercept_properties

    def validate(self):
        if self.add_listener_properties:
            for v1 in self.add_listener_properties:
                 if v1:
                    v1.validate()
        if self.remove_listener_properties:
            for v1 in self.remove_listener_properties:
                 if v1:
                    v1.validate()
        if self.tls_intercept_properties:
            self.tls_intercept_properties.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AddListenerProperties'] = []
        if self.add_listener_properties is not None:
            for k1 in self.add_listener_properties:
                result['AddListenerProperties'].append(k1.to_map() if k1 else None)

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.default_egress_proxy_ip_pool_id is not None:
            result['DefaultEgressProxyIpPoolId'] = self.default_egress_proxy_ip_pool_id

        if self.description is not None:
            result['Description'] = self.description

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.egress_proxy_gateway_id is not None:
            result['EgressProxyGatewayId'] = self.egress_proxy_gateway_id

        if self.egress_proxy_gateway_name is not None:
            result['EgressProxyGatewayName'] = self.egress_proxy_gateway_name

        result['RemoveListenerProperties'] = []
        if self.remove_listener_properties is not None:
            for k1 in self.remove_listener_properties:
                result['RemoveListenerProperties'].append(k1.to_map() if k1 else None)

        if self.tls_intercept_properties is not None:
            result['TlsInterceptProperties'] = self.tls_intercept_properties.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.add_listener_properties = []
        if m.get('AddListenerProperties') is not None:
            for k1 in m.get('AddListenerProperties'):
                temp_model = main_models.UpdateEgressProxyGatewayAttributeRequestAddListenerProperties()
                self.add_listener_properties.append(temp_model.from_map(k1))

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DefaultEgressProxyIpPoolId') is not None:
            self.default_egress_proxy_ip_pool_id = m.get('DefaultEgressProxyIpPoolId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EgressProxyGatewayId') is not None:
            self.egress_proxy_gateway_id = m.get('EgressProxyGatewayId')

        if m.get('EgressProxyGatewayName') is not None:
            self.egress_proxy_gateway_name = m.get('EgressProxyGatewayName')

        self.remove_listener_properties = []
        if m.get('RemoveListenerProperties') is not None:
            for k1 in m.get('RemoveListenerProperties'):
                temp_model = main_models.UpdateEgressProxyGatewayAttributeRequestRemoveListenerProperties()
                self.remove_listener_properties.append(temp_model.from_map(k1))

        if m.get('TlsInterceptProperties') is not None:
            temp_model = main_models.UpdateEgressProxyGatewayAttributeRequestTlsInterceptProperties()
            self.tls_intercept_properties = temp_model.from_map(m.get('TlsInterceptProperties'))

        return self

class UpdateEgressProxyGatewayAttributeRequestTlsInterceptProperties(DaraModel):
    def __init__(
        self,
        private_ca_certificate_id: str = None,
        tls_intercept_mode: str = None,
    ):
        self.private_ca_certificate_id = private_ca_certificate_id
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

class UpdateEgressProxyGatewayAttributeRequestRemoveListenerProperties(DaraModel):
    def __init__(
        self,
        port: int = None,
        protocol: str = None,
    ):
        # This parameter is required.
        self.port = port
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

class UpdateEgressProxyGatewayAttributeRequestAddListenerProperties(DaraModel):
    def __init__(
        self,
        port: int = None,
        protocol: str = None,
    ):
        # This parameter is required.
        self.port = port
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

