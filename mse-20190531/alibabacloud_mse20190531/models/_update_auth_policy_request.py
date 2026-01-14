# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAuthPolicyRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        app_id: str = None,
        auth_rule: str = None,
        enable: str = None,
        id: str = None,
        k_8s_namespace: str = None,
        name: str = None,
        protocol: str = None,
        region: str = None,
        source: str = None,
    ):
        # The language of the response. Valid values: zh-CN and en-US. Default value: zh-CN. The value zh-CN indicates Chinese, and the value en-US indicates English.
        self.accept_language = accept_language
        # The application ID.
        self.app_id = app_id
        # The content of the service authentication rule.
        self.auth_rule = auth_rule
        # Specifies whether to enable the rule.
        self.enable = enable
        # The rule ID.
        # 
        # This parameter is required.
        self.id = id
        # The ID of the ACK cluster namespace.
        self.k_8s_namespace = k_8s_namespace
        # The name of the rule.
        self.name = name
        # The protocol type. Valid values:
        # 
        # *   **SPRING_CLOUD**
        # *   **DUBBO**
        # *   **istio**
        self.protocol = protocol
        # The region ID.
        self.region = region
        # The source for application access.
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.auth_rule is not None:
            result['AuthRule'] = self.auth_rule

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.id is not None:
            result['Id'] = self.id

        if self.k_8s_namespace is not None:
            result['K8sNamespace'] = self.k_8s_namespace

        if self.name is not None:
            result['Name'] = self.name

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.region is not None:
            result['Region'] = self.region

        if self.source is not None:
            result['Source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AuthRule') is not None:
            self.auth_rule = m.get('AuthRule')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('K8sNamespace') is not None:
            self.k_8s_namespace = m.get('K8sNamespace')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        return self

