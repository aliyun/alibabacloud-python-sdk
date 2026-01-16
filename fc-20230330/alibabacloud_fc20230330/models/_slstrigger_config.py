# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_fc20230330 import models as main_models
from darabonba.model import DaraModel

class SLSTriggerConfig(DaraModel):
    def __init__(
        self,
        enable: bool = None,
        function_parameter: Dict[str, str] = None,
        job_config: main_models.JobConfig = None,
        log_config: main_models.SLSTriggerLogConfig = None,
        source_config: main_models.SourceConfig = None,
    ):
        self.enable = enable
        self.function_parameter = function_parameter
        self.job_config = job_config
        self.log_config = log_config
        self.source_config = source_config

    def validate(self):
        if self.job_config:
            self.job_config.validate()
        if self.log_config:
            self.log_config.validate()
        if self.source_config:
            self.source_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['enable'] = self.enable

        if self.function_parameter is not None:
            result['functionParameter'] = self.function_parameter

        if self.job_config is not None:
            result['jobConfig'] = self.job_config.to_map()

        if self.log_config is not None:
            result['logConfig'] = self.log_config.to_map()

        if self.source_config is not None:
            result['sourceConfig'] = self.source_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('functionParameter') is not None:
            self.function_parameter = m.get('functionParameter')

        if m.get('jobConfig') is not None:
            temp_model = main_models.JobConfig()
            self.job_config = temp_model.from_map(m.get('jobConfig'))

        if m.get('logConfig') is not None:
            temp_model = main_models.SLSTriggerLogConfig()
            self.log_config = temp_model.from_map(m.get('logConfig'))

        if m.get('sourceConfig') is not None:
            temp_model = main_models.SourceConfig()
            self.source_config = temp_model.from_map(m.get('sourceConfig'))

        return self

