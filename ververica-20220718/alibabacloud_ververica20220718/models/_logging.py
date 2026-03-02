# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class Logging(DaraModel):
    def __init__(
        self,
        log_4j_2configuration_template: str = None,
        log_4j_loggers: List[main_models.Log4jLogger] = None,
        log_reserve_policy: main_models.LogReservePolicy = None,
        logging_profile: str = None,
    ):
        # Custom log templates.
        self.log_4j_2configuration_template = log_4j_2configuration_template
        # The Log4j configuration.
        self.log_4j_loggers = log_4j_loggers
        # The log retention policy.
        self.log_reserve_policy = log_reserve_policy
        # The type of the system log template.
        # 
        # *   default: The default template is used.
        # *   oss: Logs are delivered to Object Storage Service (OSS).
        self.logging_profile = logging_profile

    def validate(self):
        if self.log_4j_loggers:
            for v1 in self.log_4j_loggers:
                 if v1:
                    v1.validate()
        if self.log_reserve_policy:
            self.log_reserve_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log_4j_2configuration_template is not None:
            result['log4j2ConfigurationTemplate'] = self.log_4j_2configuration_template

        result['log4jLoggers'] = []
        if self.log_4j_loggers is not None:
            for k1 in self.log_4j_loggers:
                result['log4jLoggers'].append(k1.to_map() if k1 else None)

        if self.log_reserve_policy is not None:
            result['logReservePolicy'] = self.log_reserve_policy.to_map()

        if self.logging_profile is not None:
            result['loggingProfile'] = self.logging_profile

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('log4j2ConfigurationTemplate') is not None:
            self.log_4j_2configuration_template = m.get('log4j2ConfigurationTemplate')

        self.log_4j_loggers = []
        if m.get('log4jLoggers') is not None:
            for k1 in m.get('log4jLoggers'):
                temp_model = main_models.Log4jLogger()
                self.log_4j_loggers.append(temp_model.from_map(k1))

        if m.get('logReservePolicy') is not None:
            temp_model = main_models.LogReservePolicy()
            self.log_reserve_policy = temp_model.from_map(m.get('logReservePolicy'))

        if m.get('loggingProfile') is not None:
            self.logging_profile = m.get('loggingProfile')

        return self

