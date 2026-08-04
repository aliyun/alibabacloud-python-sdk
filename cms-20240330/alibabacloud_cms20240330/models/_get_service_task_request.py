# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetServiceTaskRequest(DaraModel):
    def __init__(
        self,
        type: str = None,
    ):
        # The task type. This parameter is required. Valid values:
        # 
        # - heapdump: heap dump.
        # - LiveDebug Probe: live_debug_log_probe, live_debug_snapshot_probe, live_debug_metric_probe, live_debug_span_probe, live_debug_span_tag_probe.
        # - LiveDebug Command: live_debug_inspect_object, live_debug_search_type, live_debug_search_method, live_debug_decompile, live_debug_get_thread_info, live_debug_get_runtime_info, live_debug_get_memory_info, live_debug_evaluate_expression, live_debug_modify_logger_level.
        # - LiveDebug code hot replacement: live_debug_code_replace.
        # 
        # The value must be the same as the type specified during task creation.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')

        return self

