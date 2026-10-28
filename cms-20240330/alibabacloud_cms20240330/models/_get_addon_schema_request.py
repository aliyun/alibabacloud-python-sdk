# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAddonSchemaRequest(DaraModel):
    def __init__(
        self,
        aliyun_lang: str = None,
        api_version: str = None,
        environment_type: str = None,
        version: str = None,
    ):
        # The language environment. Default value: zh. Valid values: zh, en.
        self.aliyun_lang = aliyun_lang
        # The add-on catalog version. Valid values: v1, v2.
        self.api_version = api_version
        # The environment type. Valid values: CS (container), ECS.
        self.environment_type = environment_type
        # The component version.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_lang is not None:
            result['aliyunLang'] = self.aliyun_lang

        if self.api_version is not None:
            result['apiVersion'] = self.api_version

        if self.environment_type is not None:
            result['environmentType'] = self.environment_type

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliyunLang') is not None:
            self.aliyun_lang = m.get('aliyunLang')

        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')

        if m.get('environmentType') is not None:
            self.environment_type = m.get('environmentType')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

