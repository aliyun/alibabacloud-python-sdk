# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class UpgradeEngineVersionRequest(DaraModel):
    def __init__(
        self,
        plugins: List[main_models.UpgradeEngineVersionRequestPlugins] = None,
        type: str = None,
        version: str = None,
        client_token: str = None,
        dry_run: bool = None,
        update_strategy: str = None,
    ):
        self.plugins = plugins
        self.type = type
        self.version = version
        # The moderation results.
        self.client_token = client_token
        # The monitoring type. Valid values:
        # 
        # *   checkClusterHealth: Cluster Health Status
        # *   checkConfigCompatible: Configuration Compatibility Status
        # *   checkClusterResource: resource space status
        # *   checkClusterSnapshot: Whether a snapshot exists
        self.dry_run = dry_run
        self.update_strategy = update_strategy

    def validate(self):
        if self.plugins:
            for v1 in self.plugins:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['plugins'] = []
        if self.plugins is not None:
            for k1 in self.plugins:
                result['plugins'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['type'] = self.type

        if self.version is not None:
            result['version'] = self.version

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        if self.dry_run is not None:
            result['dryRun'] = self.dry_run

        if self.update_strategy is not None:
            result['updateStrategy'] = self.update_strategy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.plugins = []
        if m.get('plugins') is not None:
            for k1 in m.get('plugins'):
                temp_model = main_models.UpgradeEngineVersionRequestPlugins()
                self.plugins.append(temp_model.from_map(k1))

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('version') is not None:
            self.version = m.get('version')

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')

        if m.get('updateStrategy') is not None:
            self.update_strategy = m.get('updateStrategy')

        return self

class UpgradeEngineVersionRequestPlugins(DaraModel):
    def __init__(
        self,
        enable: str = None,
        file_version: str = None,
        name: str = None,
        version: str = None,
    ):
        self.enable = enable
        self.file_version = file_version
        self.name = name
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['enable'] = self.enable

        if self.file_version is not None:
            result['fileVersion'] = self.file_version

        if self.name is not None:
            result['name'] = self.name

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('fileVersion') is not None:
            self.file_version = m.get('fileVersion')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

