# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class ImportServicesRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        fc_alias: str = None,
        fc_service_name: str = None,
        fc_version: str = None,
        gateway_unique_id: str = None,
        service_list: List[main_models.ImportServicesRequestServiceList] = None,
        source_id: int = None,
        source_type: str = None,
        tls_setting: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        self.fc_alias = fc_alias
        self.fc_service_name = fc_service_name
        self.fc_version = fc_version
        # The unique ID of the gateway.
        self.gateway_unique_id = gateway_unique_id
        # The information about services.
        self.service_list = service_list
        self.source_id = source_id
        # The service source. Valid values:
        # 
        # *   MSE: MSE Nacos instance
        # *   K8s: ACK cluster
        # *   VIP: fixed address
        # *   DNS: DNS domain
        self.source_type = source_type
        # The Transport Layer Security (TLS) settings. Valid values:
        # 
        # *   mode: TLS mode
        # *   certId: certificate ID
        # *   caCertId: CA certificate ID
        # *   caCertContent: CA certificate public key
        # *   sni: service name identification
        self.tls_setting = tls_setting

    def validate(self):
        if self.service_list:
            for v1 in self.service_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.fc_alias is not None:
            result['FcAlias'] = self.fc_alias

        if self.fc_service_name is not None:
            result['FcServiceName'] = self.fc_service_name

        if self.fc_version is not None:
            result['FcVersion'] = self.fc_version

        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id

        result['ServiceList'] = []
        if self.service_list is not None:
            for k1 in self.service_list:
                result['ServiceList'].append(k1.to_map() if k1 else None)

        if self.source_id is not None:
            result['SourceId'] = self.source_id

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.tls_setting is not None:
            result['TlsSetting'] = self.tls_setting

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('FcAlias') is not None:
            self.fc_alias = m.get('FcAlias')

        if m.get('FcServiceName') is not None:
            self.fc_service_name = m.get('FcServiceName')

        if m.get('FcVersion') is not None:
            self.fc_version = m.get('FcVersion')

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        self.service_list = []
        if m.get('ServiceList') is not None:
            for k1 in m.get('ServiceList'):
                temp_model = main_models.ImportServicesRequestServiceList()
                self.service_list.append(temp_model.from_map(k1))

        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('TlsSetting') is not None:
            self.tls_setting = m.get('TlsSetting')

        return self

class ImportServicesRequestServiceList(DaraModel):
    def __init__(
        self,
        dns_server_list: List[str] = None,
        group_name: str = None,
        ips: List[str] = None,
        name: str = None,
        namespace: str = None,
        sae_app_id: str = None,
        service_port: int = None,
        service_protocol: str = None,
    ):
        self.dns_server_list = dns_server_list
        # The group.
        self.group_name = group_name
        # The IP addresses of the service.
        self.ips = ips
        # The name of the service.
        self.name = name
        # The namespace.
        self.namespace = namespace
        self.sae_app_id = sae_app_id
        # The port of the service.
        self.service_port = service_port
        # The protocol of the service.
        self.service_protocol = service_protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dns_server_list is not None:
            result['DnsServerList'] = self.dns_server_list

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.ips is not None:
            result['Ips'] = self.ips

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.sae_app_id is not None:
            result['SaeAppId'] = self.sae_app_id

        if self.service_port is not None:
            result['ServicePort'] = self.service_port

        if self.service_protocol is not None:
            result['ServiceProtocol'] = self.service_protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DnsServerList') is not None:
            self.dns_server_list = m.get('DnsServerList')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('Ips') is not None:
            self.ips = m.get('Ips')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('SaeAppId') is not None:
            self.sae_app_id = m.get('SaeAppId')

        if m.get('ServicePort') is not None:
            self.service_port = m.get('ServicePort')

        if m.get('ServiceProtocol') is not None:
            self.service_protocol = m.get('ServiceProtocol')

        return self

