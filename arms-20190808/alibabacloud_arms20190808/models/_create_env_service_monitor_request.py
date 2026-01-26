# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateEnvServiceMonitorRequest(DaraModel):
    def __init__(
        self,
        aliyun_lang: str = None,
        config_yaml: str = None,
        dry_run: bool = None,
        environment_id: str = None,
        region_id: str = None,
    ):
        # The language. Valid values:
        # 
        # *   zh (default): Chinese
        # *   en: English
        self.aliyun_lang = aliyun_lang
        # The YAML configuration file of the ServiceMonitor.
        # 
        # This parameter is required.
        self.config_yaml = config_yaml
        # Specifies whether to perform only a dry run, without performing the actual request. The system checks whether the format is valid and whether targets are matched.
        self.dry_run = dry_run
        # The ID of the environment instance.
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

        if self.config_yaml is not None:
            result['ConfigYaml'] = self.config_yaml

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.environment_id is not None:
            result['EnvironmentId'] = self.environment_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunLang') is not None:
            self.aliyun_lang = m.get('AliyunLang')

        if m.get('ConfigYaml') is not None:
            self.config_yaml = m.get('ConfigYaml')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EnvironmentId') is not None:
            self.environment_id = m.get('EnvironmentId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

