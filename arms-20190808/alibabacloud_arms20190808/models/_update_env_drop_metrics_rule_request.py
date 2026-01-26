# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateEnvDropMetricsRuleRequest(DaraModel):
    def __init__(
        self,
        aliyun_lang: str = None,
        drop_metrics: str = None,
        environment_id: str = None,
        region_id: str = None,
    ):
        # The language. Valid values:
        # 
        # *   zh (default)
        # *   en
        self.aliyun_lang = aliyun_lang
        # The metric to be discarded. Separate multiple metrics with line feeds.
        # 
        # This parameter is required.
        self.drop_metrics = drop_metrics
        # The environment ID.
        # 
        # This parameter is required.
        self.environment_id = environment_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_lang is not None:
            result['AliyunLang'] = self.aliyun_lang

        if self.drop_metrics is not None:
            result['DropMetrics'] = self.drop_metrics

        if self.environment_id is not None:
            result['EnvironmentId'] = self.environment_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunLang') is not None:
            self.aliyun_lang = m.get('AliyunLang')

        if m.get('DropMetrics') is not None:
            self.drop_metrics = m.get('DropMetrics')

        if m.get('EnvironmentId') is not None:
            self.environment_id = m.get('EnvironmentId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

