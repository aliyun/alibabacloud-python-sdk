# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BindSentinelBlockFallbackDefinitionRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        app_name: str = None,
        fallback_id: int = None,
        namespace: str = None,
        resource: str = None,
        target_type: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        # The name of the application.
        # 
        # This parameter is required.
        self.app_name = app_name
        # Behavior ID. 0:the default behavior.
        # 
        # This parameter is required.
        self.fallback_id = fallback_id
        # The microservice namespace.
        # 
        # This parameter is required.
        self.namespace = namespace
        # Interface Name: The resource to which the rule applies. It must match the interface name in the console\\"s interface details.
        # 
        # This parameter is required.
        self.resource = resource
        # Target rule type.
        # 
        # This parameter is required.
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.fallback_id is not None:
            result['FallbackId'] = self.fallback_id

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.resource is not None:
            result['Resource'] = self.resource

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('FallbackId') is not None:
            self.fallback_id = m.get('FallbackId')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('Resource') is not None:
            self.resource = m.get('Resource')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

