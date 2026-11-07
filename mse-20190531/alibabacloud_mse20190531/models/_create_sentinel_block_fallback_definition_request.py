# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSentinelBlockFallbackDefinitionRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        app_id: str = None,
        app_name: str = None,
        fallback_behavior: str = None,
        language: str = None,
        name: str = None,
        namespace: str = None,
        region_id: str = None,
        resource_classification: int = None,
        scenario: str = None,
        source: str = None,
    ):
        # The language in which you want to display the results. Valid values: zh and en. zh is the default value, which indicates Chinese. en indicates English.
        self.accept_language = accept_language
        # The application ID, which can be omitted.
        self.app_id = app_id
        # The application name.
        self.app_name = app_name
        # The behavior details.
        self.fallback_behavior = fallback_behavior
        # The programming language, such as Java or Go.
        self.language = language
        # The behavior name.
        self.name = name
        # The name of the Microservices Engine (MSE) namespace.
        self.namespace = namespace
        # The region.
        self.region_id = region_id
        # The target resource type.
        self.resource_classification = resource_classification
        # The scenario, uniformly fill in default.
        self.scenario = scenario
        # Redundant parameter, currently ignored.
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

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.fallback_behavior is not None:
            result['FallbackBehavior'] = self.fallback_behavior

        if self.language is not None:
            result['Language'] = self.language

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_classification is not None:
            result['ResourceClassification'] = self.resource_classification

        if self.scenario is not None:
            result['Scenario'] = self.scenario

        if self.source is not None:
            result['Source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('FallbackBehavior') is not None:
            self.fallback_behavior = m.get('FallbackBehavior')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceClassification') is not None:
            self.resource_classification = m.get('ResourceClassification')

        if m.get('Scenario') is not None:
            self.scenario = m.get('Scenario')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        return self

