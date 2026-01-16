# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class CreateCollectorRequest(DaraModel):
    def __init__(
        self,
        collector_paths: List[str] = None,
        configs: List[main_models.CreateCollectorRequestConfigs] = None,
        dry_run: bool = None,
        extend_configs: List[Dict[str, Any]] = None,
        name: str = None,
        res_type: str = None,
        res_version: str = None,
        vpc_id: str = None,
        client_token: str = None,
    ):
        self.collector_paths = collector_paths
        # This parameter is required.
        self.configs = configs
        # This parameter is required.
        self.dry_run = dry_run
        # This parameter is required.
        self.extend_configs = extend_configs
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.res_type = res_type
        # This parameter is required.
        self.res_version = res_version
        # This parameter is required.
        self.vpc_id = vpc_id
        # The ID of the created crawer.
        self.client_token = client_token

    def validate(self):
        if self.configs:
            for v1 in self.configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.collector_paths is not None:
            result['collectorPaths'] = self.collector_paths

        result['configs'] = []
        if self.configs is not None:
            for k1 in self.configs:
                result['configs'].append(k1.to_map() if k1 else None)

        if self.dry_run is not None:
            result['dryRun'] = self.dry_run

        if self.extend_configs is not None:
            result['extendConfigs'] = self.extend_configs

        if self.name is not None:
            result['name'] = self.name

        if self.res_type is not None:
            result['resType'] = self.res_type

        if self.res_version is not None:
            result['resVersion'] = self.res_version

        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('collectorPaths') is not None:
            self.collector_paths = m.get('collectorPaths')

        self.configs = []
        if m.get('configs') is not None:
            for k1 in m.get('configs'):
                temp_model = main_models.CreateCollectorRequestConfigs()
                self.configs.append(temp_model.from_map(k1))

        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')

        if m.get('extendConfigs') is not None:
            self.extend_configs = m.get('extendConfigs')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('resType') is not None:
            self.res_type = m.get('resType')

        if m.get('resVersion') is not None:
            self.res_version = m.get('resVersion')

        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

class CreateCollectorRequestConfigs(DaraModel):
    def __init__(
        self,
        content: str = None,
        file_name: str = None,
    ):
        # This parameter is required.
        self.content = content
        # This parameter is required.
        self.file_name = file_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.file_name is not None:
            result['fileName'] = self.file_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        return self

