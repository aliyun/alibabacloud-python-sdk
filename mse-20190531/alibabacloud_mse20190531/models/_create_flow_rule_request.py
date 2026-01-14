# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateFlowRuleRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        app_id: str = None,
        app_name: str = None,
        control_behavior: int = None,
        enable: bool = None,
        limit_app: str = None,
        max_queueing_time_ms: int = None,
        namespace: str = None,
        region_id: str = None,
        resource: str = None,
        resource_type: int = None,
        threshold: int = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        # The application ID.
        self.app_id = app_id
        # The application name.
        # 
        # This parameter is required.
        self.app_name = app_name
        # The throttling effect.
        # 
        # Valid values:
        # 
        # *   0: fast failure
        # *   2: in queue
        self.control_behavior = control_behavior
        # Specifies whether to enable the rule.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # This parameter is required.
        self.enable = enable
        self.limit_app = limit_app
        # The timeout period. Unit: milliseconds. This value is required if the ControlBehavior parameter is set to 2.
        self.max_queueing_time_ms = max_queueing_time_ms
        # The namespace.
        # 
        # This parameter is required.
        self.namespace = namespace
        # The region in which the instance resides.
        self.region_id = region_id
        # The name of the API resource.
        # 
        # This parameter is required.
        self.resource = resource
        self.resource_type = resource_type
        # The throttling threshold.
        # 
        # This parameter is required.
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

        if self.control_behavior is not None:
            result['ControlBehavior'] = self.control_behavior

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.limit_app is not None:
            result['LimitApp'] = self.limit_app

        if self.max_queueing_time_ms is not None:
            result['MaxQueueingTimeMs'] = self.max_queueing_time_ms

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource is not None:
            result['Resource'] = self.resource

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

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

        if m.get('ControlBehavior') is not None:
            self.control_behavior = m.get('ControlBehavior')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('LimitApp') is not None:
            self.limit_app = m.get('LimitApp')

        if m.get('MaxQueueingTimeMs') is not None:
            self.max_queueing_time_ms = m.get('MaxQueueingTimeMs')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Resource') is not None:
            self.resource = m.get('Resource')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        return self

