# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class LogConfig(DaraModel):
    def __init__(
        self,
        enable_instance_metrics: bool = None,
        enable_llm_metrics: bool = None,
        enable_request_metrics: bool = None,
        log_begin_rule: str = None,
        logstore: str = None,
        project: str = None,
    ):
        # Specifies whether to enable instance-level metrics. When this feature is enabled, you can view core metrics for each instance, such as CPU usage, memory usage, network conditions, and the number of requests. The default value is \\`false\\`, which disables instance-level metrics. Set the value to \\`true\\` to enable them.
        self.enable_instance_metrics = enable_instance_metrics
        self.enable_llm_metrics = enable_llm_metrics
        # Specifies whether to enable request-level metrics. When this feature is enabled, you can view the time and memory consumed by each function invocation in the service. The default value is \\`true\\`, which enables request-level metrics. Set the value to \\`false\\` to disable them.
        self.enable_request_metrics = enable_request_metrics
        # The rule for matching the first line of a log entry.
        self.log_begin_rule = log_begin_rule
        # The name of the Logstore in Simple Log Service.
        self.logstore = logstore
        # The name of the Project in Simple Log Service.
        self.project = project

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_instance_metrics is not None:
            result['enableInstanceMetrics'] = self.enable_instance_metrics

        if self.enable_llm_metrics is not None:
            result['enableLlmMetrics'] = self.enable_llm_metrics

        if self.enable_request_metrics is not None:
            result['enableRequestMetrics'] = self.enable_request_metrics

        if self.log_begin_rule is not None:
            result['logBeginRule'] = self.log_begin_rule

        if self.logstore is not None:
            result['logstore'] = self.logstore

        if self.project is not None:
            result['project'] = self.project

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enableInstanceMetrics') is not None:
            self.enable_instance_metrics = m.get('enableInstanceMetrics')

        if m.get('enableLlmMetrics') is not None:
            self.enable_llm_metrics = m.get('enableLlmMetrics')

        if m.get('enableRequestMetrics') is not None:
            self.enable_request_metrics = m.get('enableRequestMetrics')

        if m.get('logBeginRule') is not None:
            self.log_begin_rule = m.get('logBeginRule')

        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')

        if m.get('project') is not None:
            self.project = m.get('project')

        return self

