# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class LogConfig(DaraModel):
    def __init__(
        self,
        enable_instance_metrics: bool = None,
        enable_request_metrics: bool = None,
        log_begin_rule: str = None,
        logstore: str = None,
        project: str = None,
        push_to_user_sls: bool = None,
    ):
        self.enable_instance_metrics = enable_instance_metrics
        self.enable_request_metrics = enable_request_metrics
        self.log_begin_rule = log_begin_rule
        self.logstore = logstore
        self.project = project
        self.push_to_user_sls = push_to_user_sls

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_instance_metrics is not None:
            result['enableInstanceMetrics'] = self.enable_instance_metrics

        if self.enable_request_metrics is not None:
            result['enableRequestMetrics'] = self.enable_request_metrics

        if self.log_begin_rule is not None:
            result['logBeginRule'] = self.log_begin_rule

        if self.logstore is not None:
            result['logstore'] = self.logstore

        if self.project is not None:
            result['project'] = self.project

        if self.push_to_user_sls is not None:
            result['pushToUserSLS'] = self.push_to_user_sls

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enableInstanceMetrics') is not None:
            self.enable_instance_metrics = m.get('enableInstanceMetrics')

        if m.get('enableRequestMetrics') is not None:
            self.enable_request_metrics = m.get('enableRequestMetrics')

        if m.get('logBeginRule') is not None:
            self.log_begin_rule = m.get('logBeginRule')

        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')

        if m.get('project') is not None:
            self.project = m.get('project')

        if m.get('pushToUserSLS') is not None:
            self.push_to_user_sls = m.get('pushToUserSLS')

        return self

