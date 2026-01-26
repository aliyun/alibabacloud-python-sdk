# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpgradeEnvironmentFeatureRequest(DaraModel):
    def __init__(
        self,
        aliyun_lang: str = None,
        environment_id: str = None,
        feature_name: str = None,
        feature_version: str = None,
        region_id: str = None,
        values: str = None,
    ):
        # The language. Valid values: zh and en. Default value: zh.
        self.aliyun_lang = aliyun_lang
        # The environment ID.
        # 
        # This parameter is required.
        self.environment_id = environment_id
        # The feature name. Valid values: app-agent-pilot, metric-agent, ebpf-agent, and service-check.
        # 
        # This parameter is required.
        self.feature_name = feature_name
        # The version of the feature.
        self.feature_version = feature_version
        # The region ID.
        self.region_id = region_id
        # Specifies whether to enable service discovery. For PodAnnotation, set the value to run or mini. For PodMonitor and ServiceMonitor, set the value to true or false.
        self.values = values

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

        if self.feature_version is not None:
            result['FeatureVersion'] = self.feature_version

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunLang') is not None:
            self.aliyun_lang = m.get('AliyunLang')

        if m.get('EnvironmentId') is not None:
            self.environment_id = m.get('EnvironmentId')

        if m.get('FeatureName') is not None:
            self.feature_name = m.get('FeatureName')

        if m.get('FeatureVersion') is not None:
            self.feature_version = m.get('FeatureVersion')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

