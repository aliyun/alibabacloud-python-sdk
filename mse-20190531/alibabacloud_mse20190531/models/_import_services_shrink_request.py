# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImportServicesShrinkRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        fc_alias: str = None,
        fc_service_name: str = None,
        fc_version: str = None,
        gateway_unique_id: str = None,
        service_list_shrink: str = None,
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
        self.service_list_shrink = service_list_shrink
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
        pass

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

        if self.service_list_shrink is not None:
            result['ServiceList'] = self.service_list_shrink

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

        if m.get('ServiceList') is not None:
            self.service_list_shrink = m.get('ServiceList')

        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('TlsSetting') is not None:
            self.tls_setting = m.get('TlsSetting')

        return self

