# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateServiceSourceShrinkRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        address: str = None,
        gateway_id: int = None,
        gateway_unique_id: str = None,
        id: int = None,
        ingress_options_request_shrink: str = None,
        name: str = None,
        path_list_shrink: str = None,
        source: str = None,
        type: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese.
        # *   en: English.
        self.accept_language = accept_language
        # The address.
        self.address = address
        # The ID of the gateway.
        self.gateway_id = gateway_id
        # The unique ID of the gateway.
        self.gateway_unique_id = gateway_unique_id
        # The ID of the service source.
        self.id = id
        # The configurations of Ingress resources.
        self.ingress_options_request_shrink = ingress_options_request_shrink
        # The name.
        self.name = name
        # An array of service root paths.
        self.path_list_shrink = path_list_shrink
        # The service source. Valid values:
        # 
        # *   K8s: ACK cluster.
        # *   MSE: Nacos instance.
        self.source = source
        # The type of the service source. Valid values:
        # 
        # *   K8s: ACK cluster.
        # *   NACOS: Nacos instance.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.address is not None:
            result['Address'] = self.address

        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id

        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id

        if self.id is not None:
            result['Id'] = self.id

        if self.ingress_options_request_shrink is not None:
            result['IngressOptionsRequest'] = self.ingress_options_request_shrink

        if self.name is not None:
            result['Name'] = self.name

        if self.path_list_shrink is not None:
            result['PathList'] = self.path_list_shrink

        if self.source is not None:
            result['Source'] = self.source

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IngressOptionsRequest') is not None:
            self.ingress_options_request_shrink = m.get('IngressOptionsRequest')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PathList') is not None:
            self.path_list_shrink = m.get('PathList')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

