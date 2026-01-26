# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InstallEnvironmentFeatureRequest(DaraModel):
    def __init__(
        self,
        aliyun_lang: str = None,
        config: str = None,
        environment_id: str = None,
        feature_name: str = None,
        feature_version: str = None,
        region: str = None,
        region_id: str = None,
    ):
        # The language. Valid values: zh and en. Default value: zh.
        self.aliyun_lang = aliyun_lang
        # The metadata of the feature.
        self.config = config
        # The environment ID.
        # 
        # This parameter is required.
        self.environment_id = environment_id
        # The name of the feature.
        # 
        # Valid values:
        # 
        # *   app-agent-pilot
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   metric-agent
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # This parameter is required.
        self.feature_name = feature_name
        # The version of the feature.
        # 
        # This parameter is required.
        self.feature_version = feature_version
        # The region ID of the feature.
        self.region = region
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

        if self.config is not None:
            result['Config'] = self.config

        if self.environment_id is not None:
            result['EnvironmentId'] = self.environment_id

        if self.feature_name is not None:
            result['FeatureName'] = self.feature_name

        if self.feature_version is not None:
            result['FeatureVersion'] = self.feature_version

        if self.region is not None:
            result['Region'] = self.region

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunLang') is not None:
            self.aliyun_lang = m.get('AliyunLang')

        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('EnvironmentId') is not None:
            self.environment_id = m.get('EnvironmentId')

        if m.get('FeatureName') is not None:
            self.feature_name = m.get('FeatureName')

        if m.get('FeatureVersion') is not None:
            self.feature_version = m.get('FeatureVersion')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

