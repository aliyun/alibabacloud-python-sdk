# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class UpdateServiceSourceRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        address: str = None,
        gateway_id: int = None,
        gateway_unique_id: str = None,
        id: int = None,
        ingress_options_request: main_models.UpdateServiceSourceRequestIngressOptionsRequest = None,
        name: str = None,
        path_list: List[str] = None,
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
        self.ingress_options_request = ingress_options_request
        # The name.
        self.name = name
        # An array of service root paths.
        self.path_list = path_list
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
        if self.ingress_options_request:
            self.ingress_options_request.validate()

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

        if self.ingress_options_request is not None:
            result['IngressOptionsRequest'] = self.ingress_options_request.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.path_list is not None:
            result['PathList'] = self.path_list

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
            temp_model = main_models.UpdateServiceSourceRequestIngressOptionsRequest()
            self.ingress_options_request = temp_model.from_map(m.get('IngressOptionsRequest'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PathList') is not None:
            self.path_list = m.get('PathList')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class UpdateServiceSourceRequestIngressOptionsRequest(DaraModel):
    def __init__(
        self,
        enable_ingress: bool = None,
        enable_status: bool = None,
        ingress_class: str = None,
        watch_namespace: str = None,
    ):
        # Specifies whether to enable Ingress.
        self.enable_ingress = enable_ingress
        # Specifies whether to update the Ingress status.
        self.enable_status = enable_status
        # Specifies whether to monitor Ingress classes.
        self.ingress_class = ingress_class
        # The namespace whose resources you want to monitor.
        self.watch_namespace = watch_namespace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_ingress is not None:
            result['EnableIngress'] = self.enable_ingress

        if self.enable_status is not None:
            result['EnableStatus'] = self.enable_status

        if self.ingress_class is not None:
            result['IngressClass'] = self.ingress_class

        if self.watch_namespace is not None:
            result['WatchNamespace'] = self.watch_namespace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableIngress') is not None:
            self.enable_ingress = m.get('EnableIngress')

        if m.get('EnableStatus') is not None:
            self.enable_status = m.get('EnableStatus')

        if m.get('IngressClass') is not None:
            self.ingress_class = m.get('IngressClass')

        if m.get('WatchNamespace') is not None:
            self.watch_namespace = m.get('WatchNamespace')

        return self

