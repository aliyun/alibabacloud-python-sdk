# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSentinelBlockFallbackDefinitionsShrinkRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        app_name: str = None,
        classification_set_shrink: str = None,
        namespace: str = None,
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
        # Behavior Classification Set.
        self.classification_set_shrink = classification_set_shrink
        # The name of the Microservices namespace.
        # 
        # This parameter is required.
        self.namespace = namespace

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

        if self.classification_set_shrink is not None:
            result['ClassificationSet'] = self.classification_set_shrink

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ClassificationSet') is not None:
            self.classification_set_shrink = m.get('ClassificationSet')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        return self

