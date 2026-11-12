# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateServiceTaskRequest(DaraModel):
    def __init__(
        self,
        ip: str = None,
        task_config: str = None,
        type: str = None,
    ):
        # The IP address of the target instance. This parameter is optional. If not specified, some tasks can be matched by instance scope (such as instanceIds). This parameter is usually required for heap dump scenarios.
        # 
        # This parameter is required.
        self.ip = ip
        # The task configuration. The value is a JSON string with a maximum length of 65,536 characters. This parameter is required for LiveDebug tasks. Use a flat JSON structure and pass a single command or probe object directly. Do not wrap it in a commands or probes array. Probe example (dynamic log): {"probeType":"LOG","language":"java","target":{"typeName":"com.example.UserService","methodName":"getUser","location":"exit","instanceIds":["*"]},"action":{"type":"LOG","template":"userId=${args[0]}","templateSegments":[{"type":"TEXT","value":"userId="},{"type":"EXPRESSION","value":"args[0]"}]},"ttl":"1h","captureCount":100}. Command example (OGNL): {"commandType":"EVALUATE_EXPRESSION","language":"java","params":{"expression":"@java.lang.System@getProperty(\\"java.home\\")"},"instanceIds":["*"]}. Note: The top level of a Command type must contain instanceIds. For a Probe, place instanceIds inside target. For a METRIC probe, the valid values for action.metricType are COUNTER, GAUGE, HISTOGRAM, and SUMMARY. The Java agent supports only COUNTER and GAUGE.
        self.task_config = task_config
        # The task type. This parameter is required. Valid values: heapdump (heap dump); LiveDebug Probe: live_debug_log_probe, live_debug_snapshot_probe, live_debug_metric_probe, live_debug_span_probe, and live_debug_span_tag_probe; LiveDebug Command: live_debug_inspect_object, live_debug_search_type, live_debug_search_method, live_debug_decompile, live_debug_get_thread_info, live_debug_get_runtime_info, live_debug_get_memory_info, live_debug_evaluate_expression, and live_debug_modify_logger_level; LiveDebug hot code replacement: live_debug_code_replace.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip is not None:
            result['ip'] = self.ip

        if self.task_config is not None:
            result['taskConfig'] = self.task_config

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')

        if m.get('taskConfig') is not None:
            self.task_config = m.get('taskConfig')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

