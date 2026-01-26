# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAddonMetricsRequest(DaraModel):
    def __init__(
        self,
        addon_version: str = None,
        aliyun_lang: str = None,
        environment_type: str = None,
        name: str = None,
        region_id: str = None,
    ):
        # The version of the component.
        self.addon_version = addon_version
        # The language. Valid values: zh and en. Default value: zh.
        self.aliyun_lang = aliyun_lang
        # The environment.
        self.environment_type = environment_type
        # The name of the component.
        # 
        # This parameter is required.
        self.name = name
        # The ID of the region.
        self.region_id = region_id

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

        if self.environment_type is not None:
            result['EnvironmentType'] = self.environment_type

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddonVersion') is not None:
            self.addon_version = m.get('AddonVersion')

        if m.get('AliyunLang') is not None:
            self.aliyun_lang = m.get('AliyunLang')

        if m.get('EnvironmentType') is not None:
            self.environment_type = m.get('EnvironmentType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

