# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddAuthPolicyRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        app_id: str = None,
        auth_rule: str = None,
        auth_type: int = None,
        enable: str = None,
        k_8s_namespace: str = None,
        name: str = None,
        namespace: str = None,
        protocol: str = None,
        region: str = None,
        source: str = None,
    ):
        # The language of the response. Valid values: zh-CN (Chinese, default) and en-US (English).
        self.accept_language = accept_language
        # The ID of the application.
        self.app_id = app_id
        # The content of the service authentication rule.
        # 
        # This parameter is required.
        self.auth_rule = auth_rule
        # The type of the rule. Valid values:
        # 
        # - 0: application dimension.
        # - 1: namespace dimension.
        self.auth_type = auth_type
        # Specifies whether the authentication rule is enabled. Valid values:
        # 
        # - `true`: Enabled.
        # - `false`: Disabled.
        # 
        # This parameter is required.
        self.enable = enable
        # The ID of the namespace in the Kubernetes cluster.
        self.k_8s_namespace = k_8s_namespace
        # The name of the rule.
        # 
        # This parameter is required.
        self.name = name
        # The MSE namespace to which the application belongs.
        self.namespace = namespace
        # The protocol type. Valid values:
        # 
        # - **SPRING_CLOUD**
        # - **DUBBO**
        # - **istio**
        # 
        # This parameter is required.
        self.protocol = protocol
        # The region.
        # 
        # This parameter is required.
        self.region = region
        # The source. Valid values: edasmsc.
        # 
        # This parameter is required.
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

        if self.auth_type is not None:
            result['AuthType'] = self.auth_type

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.k_8s_namespace is not None:
            result['K8sNamespace'] = self.k_8s_namespace

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

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

        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('K8sNamespace') is not None:
            self.k_8s_namespace = m.get('K8sNamespace')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        return self

