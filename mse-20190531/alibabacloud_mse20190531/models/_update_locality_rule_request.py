# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateLocalityRuleRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        app_id: str = None,
        app_name: str = None,
        enable: bool = None,
        namespace: str = None,
        region: str = None,
        rules: str = None,
        source: str = None,
        threshold: float = None,
    ):
        self.accept_language = accept_language
        self.app_id = app_id
        self.app_name = app_name
        # This parameter is required.
        self.enable = enable
        self.namespace = namespace
        # This parameter is required.
        self.region = region
        self.rules = rules
        self.source = source
        self.threshold = threshold

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

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.region is not None:
            result['Region'] = self.region

        if self.rules is not None:
            result['Rules'] = self.rules

        if self.source is not None:
            result['Source'] = self.source

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Rules') is not None:
            self.rules = m.get('Rules')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        return self

