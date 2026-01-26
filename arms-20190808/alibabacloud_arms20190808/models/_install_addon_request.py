# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InstallAddonRequest(DaraModel):
    def __init__(
        self,
        addon_version: str = None,
        aliyun_lang: str = None,
        dry_run: bool = None,
        environment_id: str = None,
        name: str = None,
        region_id: str = None,
        release_name: str = None,
        values: str = None,
    ):
        # The version of the add-on.
        # 
        # This parameter is required.
        self.addon_version = addon_version
        # The language. Valid values: zh and en. Default value: zh.
        self.aliyun_lang = aliyun_lang
        # Specifies whether to perform only a dry run, without performing the actual request. Default value: false.
        self.dry_run = dry_run
        # The environment ID.
        # 
        # This parameter is required.
        self.environment_id = environment_id
        # The name of the add-on.
        # 
        # This parameter is required.
        self.name = name
        # The region ID.
        self.region_id = region_id
        # The name of the add-on after it is installed. If you do not specify this parameter, a default rule name is generated.
        self.release_name = release_name
        # The metadata.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addon_version is not None:
            result['AddonVersion'] = self.addon_version

        if self.aliyun_lang is not None:
            result['AliyunLang'] = self.aliyun_lang

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.environment_id is not None:
            result['EnvironmentId'] = self.environment_id

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.release_name is not None:
            result['ReleaseName'] = self.release_name

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddonVersion') is not None:
            self.addon_version = m.get('AddonVersion')

        if m.get('AliyunLang') is not None:
            self.aliyun_lang = m.get('AliyunLang')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EnvironmentId') is not None:
            self.environment_id = m.get('EnvironmentId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReleaseName') is not None:
            self.release_name = m.get('ReleaseName')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

