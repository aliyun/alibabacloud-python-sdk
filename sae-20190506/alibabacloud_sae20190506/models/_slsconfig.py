# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class SLSConfig(DaraModel):
    def __init__(
        self,
        collect_configs: List[main_models.SLSConfigCollectConfigs] = None,
    ):
        self.collect_configs = collect_configs

    def validate(self):
        if self.collect_configs:
            for v1 in self.collect_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['collectConfigs'] = []
        if self.collect_configs is not None:
            for k1 in self.collect_configs:
                result['collectConfigs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.collect_configs = []
        if m.get('collectConfigs') is not None:
            for k1 in m.get('collectConfigs'):
                temp_model = main_models.SLSConfigCollectConfigs()
                self.collect_configs.append(temp_model.from_map(k1))

        return self

class SLSConfigCollectConfigs(DaraModel):
    def __init__(
        self,
        log_path: str = None,
        log_type: str = None,
        logstore_name: str = None,
        logtail_name: str = None,
        project_name: str = None,
    ):
        self.log_path = log_path
        self.log_type = log_type
        self.logstore_name = logstore_name
        self.logtail_name = logtail_name
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log_path is not None:
            result['logPath'] = self.log_path

        if self.log_type is not None:
            result['logType'] = self.log_type

        if self.logstore_name is not None:
            result['logstoreName'] = self.logstore_name

        if self.logtail_name is not None:
            result['logtailName'] = self.logtail_name

        if self.project_name is not None:
            result['projectName'] = self.project_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logPath') is not None:
            self.log_path = m.get('logPath')

        if m.get('logType') is not None:
            self.log_type = m.get('logType')

        if m.get('logstoreName') is not None:
            self.logstore_name = m.get('logstoreName')

        if m.get('logtailName') is not None:
            self.logtail_name = m.get('logtailName')

        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')

        return self

