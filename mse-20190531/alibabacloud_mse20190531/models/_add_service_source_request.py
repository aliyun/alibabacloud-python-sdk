# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class AddServiceSourceRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        address: str = None,
        gateway_unique_id: str = None,
        group_list: List[str] = None,
        ingress_options_request: main_models.AddServiceSourceRequestIngressOptionsRequest = None,
        name: str = None,
        path_list: List[str] = None,
        source: str = None,
        to_authorize_security_groups: List[main_models.AddServiceSourceRequestToAuthorizeSecurityGroups] = None,
        type: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh-CN (default): Chinese
        # *   en-US: English
        # *   ja: Japanese
        self.accept_language = accept_language
        # Specifies whether to monitor Ingress classes.
        self.address = address
        # Specifies whether to update the Ingress status.
        self.gateway_unique_id = gateway_unique_id
        # The data structure.
        self.group_list = group_list
        # The list of service groups.
        self.ingress_options_request = ingress_options_request
        # The namespace whose resources you want to monitor.
        self.name = name
        # The HTTP status code returned.
        self.path_list = path_list
        # The service source.
        # 
        # *   K8s: ACK cluster
        # *   NACOS: MSE Nacos instance
        self.source = source
        # The list of security groups to be authorized. You can specify security groups to allow backend services to access data sources that you create.
        self.to_authorize_security_groups = to_authorize_security_groups
        # The type of the service source.
        # 
        # *   K8s: Container Service for Kubernetes (ACK) cluster
        # *   NACOS: Nacos instance
        self.type = type

    def validate(self):
        if self.ingress_options_request:
            self.ingress_options_request.validate()
        if self.to_authorize_security_groups:
            for v1 in self.to_authorize_security_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.address is not None:
            result['Address'] = self.address

        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id

        if self.group_list is not None:
            result['GroupList'] = self.group_list

        if self.ingress_options_request is not None:
            result['IngressOptionsRequest'] = self.ingress_options_request.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.path_list is not None:
            result['PathList'] = self.path_list

        if self.source is not None:
            result['Source'] = self.source

        result['ToAuthorizeSecurityGroups'] = []
        if self.to_authorize_security_groups is not None:
            for k1 in self.to_authorize_security_groups:
                result['ToAuthorizeSecurityGroups'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('GroupList') is not None:
            self.group_list = m.get('GroupList')

        if m.get('IngressOptionsRequest') is not None:
            temp_model = main_models.AddServiceSourceRequestIngressOptionsRequest()
            self.ingress_options_request = temp_model.from_map(m.get('IngressOptionsRequest'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PathList') is not None:
            self.path_list = m.get('PathList')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        self.to_authorize_security_groups = []
        if m.get('ToAuthorizeSecurityGroups') is not None:
            for k1 in m.get('ToAuthorizeSecurityGroups'):
                temp_model = main_models.AddServiceSourceRequestToAuthorizeSecurityGroups()
                self.to_authorize_security_groups.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class AddServiceSourceRequestToAuthorizeSecurityGroups(DaraModel):
    def __init__(
        self,
        description: str = None,
        port_range: str = None,
        security_group_id: str = None,
    ):
        # The description of the authorization record.
        self.description = description
        # The authorized port range of the security group. You can select multiple port ranges. Separate each port range with a comma (,).
        self.port_range = port_range
        # The ID of the security group.
        self.security_group_id = security_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.port_range is not None:
            result['PortRange'] = self.port_range

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        return self

class AddServiceSourceRequestIngressOptionsRequest(DaraModel):
    def __init__(
        self,
        enable_ingress: bool = None,
        enable_status: bool = None,
        ingress_class: str = None,
        watch_namespace: str = None,
    ):
        # The group to which the service belongs.
        self.enable_ingress = enable_ingress
        # The language of the response. Valid values:
        # 
        # *   zh-CN: Chinese. This is the default value.
        # *   en-US: English.
        # *   ja: Japanese.
        self.enable_status = enable_status
        # An array of service root paths.
        self.ingress_class = ingress_class
        # The root path of the service.
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

