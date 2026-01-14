# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyLosslessRuleRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        aligned: bool = None,
        app_id: str = None,
        app_name: str = None,
        delay_time: int = None,
        enable: bool = None,
        func_type: int = None,
        loss_less_detail: bool = None,
        namespace: str = None,
        notice: bool = None,
        region_id: str = None,
        related: bool = None,
        warmup_time: int = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        # Specifies whether to align the lifecycle of the application in the Kubernetes cluster with that of the microservice.
        # 
        # This parameter is required.
        self.aligned = aligned
        # The ID of the application.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The name of the application.
        self.app_name = app_name
        # The registration latency.
        # 
        # This parameter is required.
        self.delay_time = delay_time
        # Specifies whether to enable the alert rule. Valid values:
        # 
        # *   `true`: enables the rule.
        # *   `false`: disables the rule.
        # 
        # This parameter is required.
        self.enable = enable
        # The slope of the prefetching curve.
        # 
        # This parameter is required.
        self.func_type = func_type
        # Specifies whether to display online and offline processing details.
        self.loss_less_detail = loss_less_detail
        # The microservice namespace to which the rule applies.
        self.namespace = namespace
        # Specifies whether to enable notification.
        self.notice = notice
        # The ID of the region.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Specifies whether to associate with service prefetching.
        # 
        # This parameter is required.
        self.related = related
        # The prefetching duration.
        # 
        # This parameter is required.
        self.warmup_time = warmup_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.aligned is not None:
            result['Aligned'] = self.aligned

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.delay_time is not None:
            result['DelayTime'] = self.delay_time

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.func_type is not None:
            result['FuncType'] = self.func_type

        if self.loss_less_detail is not None:
            result['LossLessDetail'] = self.loss_less_detail

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.notice is not None:
            result['Notice'] = self.notice

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.related is not None:
            result['Related'] = self.related

        if self.warmup_time is not None:
            result['WarmupTime'] = self.warmup_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('Aligned') is not None:
            self.aligned = m.get('Aligned')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DelayTime') is not None:
            self.delay_time = m.get('DelayTime')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('FuncType') is not None:
            self.func_type = m.get('FuncType')

        if m.get('LossLessDetail') is not None:
            self.loss_less_detail = m.get('LossLessDetail')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('Notice') is not None:
            self.notice = m.get('Notice')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Related') is not None:
            self.related = m.get('Related')

        if m.get('WarmupTime') is not None:
            self.warmup_time = m.get('WarmupTime')

        return self

