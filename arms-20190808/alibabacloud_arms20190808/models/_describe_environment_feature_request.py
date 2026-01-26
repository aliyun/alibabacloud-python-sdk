# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeEnvironmentFeatureRequest(DaraModel):
    def __init__(
        self,
        aliyun_lang: str = None,
        environment_id: str = None,
        feature_name: str = None,
        region_id: str = None,
    ):
        # The language. Valid values: en and zh.
        self.aliyun_lang = aliyun_lang
        # The environment ID.
        # 
        # This parameter is required.
        self.environment_id = environment_id
        # The name of the feature.
        # 
        # Valid values:
        # 
        # *   app-agent-pilot: App Pilot agent
        # *   arms-cmonitor: ARMS CMonitor agent
        # *   metric-agent: Prometheus agent
        # 
        # This parameter is required.
        self.feature_name = feature_name
        # The region ID.
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

        if self.environment_id is not None:
            result['EnvironmentId'] = self.environment_id

        if self.feature_name is not None:
            result['FeatureName'] = self.feature_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunLang') is not None:
            self.aliyun_lang = m.get('AliyunLang')

        if m.get('EnvironmentId') is not None:
            self.environment_id = m.get('EnvironmentId')

        if m.get('FeatureName') is not None:
            self.feature_name = m.get('FeatureName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

