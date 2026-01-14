# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddServiceSourceShrinkRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        address: str = None,
        gateway_unique_id: str = None,
        group_list_shrink: str = None,
        ingress_options_request_shrink: str = None,
        name: str = None,
        path_list_shrink: str = None,
        source: str = None,
        to_authorize_security_groups_shrink: str = None,
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
        self.group_list_shrink = group_list_shrink
        # The list of service groups.
        self.ingress_options_request_shrink = ingress_options_request_shrink
        # The namespace whose resources you want to monitor.
        self.name = name
        # The HTTP status code returned.
        self.path_list_shrink = path_list_shrink
        # The service source.
        # 
        # *   K8s: ACK cluster
        # *   NACOS: MSE Nacos instance
        self.source = source
        # The list of security groups to be authorized. You can specify security groups to allow backend services to access data sources that you create.
        self.to_authorize_security_groups_shrink = to_authorize_security_groups_shrink
        # The type of the service source.
        # 
        # *   K8s: Container Service for Kubernetes (ACK) cluster
        # *   NACOS: Nacos instance
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

        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id

        if self.group_list_shrink is not None:
            result['GroupList'] = self.group_list_shrink

        if self.ingress_options_request_shrink is not None:
            result['IngressOptionsRequest'] = self.ingress_options_request_shrink

        if self.name is not None:
            result['Name'] = self.name

        if self.path_list_shrink is not None:
            result['PathList'] = self.path_list_shrink

        if self.source is not None:
            result['Source'] = self.source

        if self.to_authorize_security_groups_shrink is not None:
            result['ToAuthorizeSecurityGroups'] = self.to_authorize_security_groups_shrink

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
            self.group_list_shrink = m.get('GroupList')

        if m.get('IngressOptionsRequest') is not None:
            self.ingress_options_request_shrink = m.get('IngressOptionsRequest')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PathList') is not None:
            self.path_list_shrink = m.get('PathList')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('ToAuthorizeSecurityGroups') is not None:
            self.to_authorize_security_groups_shrink = m.get('ToAuthorizeSecurityGroups')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

