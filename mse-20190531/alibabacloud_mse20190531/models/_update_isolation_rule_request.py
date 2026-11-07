# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateIsolationRuleRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        app_id: str = None,
        app_name: str = None,
        enable: bool = None,
        limit_app: str = None,
        namespace: str = None,
        rule_id: int = None,
        threshold: float = None,
    ):
        # The language in which the response is displayed. Valid values: zh (default): Chinese. en: English.
        self.accept_language = accept_language
        # The ID of the application.
        self.app_id = app_id
        # The name of the application.
        # 
        # This parameter is required.
        self.app_name = app_name
        # Specifies whether the rule is enabled.
        self.enable = enable
        # The source application of the request.
        self.limit_app = limit_app
        # The microservice namespace to which the application belongs.
        # 
        # This parameter is required.
        self.namespace = namespace
        # The ID of the rule.
        # 
        # This parameter is required.
        self.rule_id = rule_id
        # The concurrency threshold of the isolation rule.
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

        if self.limit_app is not None:
            result['LimitApp'] = self.limit_app

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

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

        if m.get('LimitApp') is not None:
            self.limit_app = m.get('LimitApp')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        return self

