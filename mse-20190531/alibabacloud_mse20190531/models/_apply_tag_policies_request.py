# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class ApplyTagPoliciesRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        app_id: str = None,
        app_name: str = None,
        enable: bool = None,
        namespace: str = None,
        namespace_id: str = None,
        region: str = None,
        rules: Dict[str, main_models.RulesValue] = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        # The ID of the application.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The name of the application.
        self.app_name = app_name
        # Specifies whether to enable the routing rule.
        self.enable = enable
        # The Microservices Engine (MSE) namespace to which the application belongs.
        self.namespace = namespace
        # Optional. The ID of the namespace.
        self.namespace_id = namespace_id
        # The region ID.
        self.region = region
        # The details of the routing rule.
        self.rules = rules

    def validate(self):
        if self.rules:
            for v1 in self.rules.values():
                 if v1:
                    v1.validate()

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

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.region is not None:
            result['Region'] = self.region

        result['Rules'] = {}
        if self.rules is not None:
            for k1, v1 in self.rules.items():
                result['Rules'][k1] = v1.to_map() if v1 else None

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

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        self.rules = {}
        if m.get('Rules') is not None:
            for k1, v1 in m.get('Rules').items():
                temp_model = main_models.RulesValue()
                self.rules[k1] = temp_model.from_map(v1)

        return self

