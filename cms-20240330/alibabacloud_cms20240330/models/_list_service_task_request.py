# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListServiceTaskRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        search_condition: str = None,
        type: str = None,
    ):
        # The maximum number of entries per page. Valid values: 0 to 100. Default value: 100.
        self.max_results = max_results
        # The pagination token. Pass the nextToken value from the previous response as-is. This parameter is not required for the first request. The server returns an encrypted hexadecimal string (internal format: {md5}#{dbId}) with a maximum length of 128 characters.
        self.next_token = next_token
        # The search condition. A JSON string with a maximum length of 1024 characters. For heapdump, this can be used to filter by IP address or other conditions. Example for pprof: {"ip":"10.0.0.1","start":1711843200000,"end":1711846800000,"profileType":1}.
        self.search_condition = search_condition
        # The task type. Valid values: heapdump (heap dump). LiveDebug Probe: live_debug_log_probe, live_debug_snapshot_probe, live_debug_metric_probe, live_debug_span_probe, live_debug_span_tag_probe. LiveDebug Command: live_debug_inspect_object, live_debug_search_type, live_debug_search_method, live_debug_decompile, live_debug_get_thread_info, live_debug_get_runtime_info, live_debug_get_memory_info, live_debug_evaluate_expression, live_debug_modify_logger_level. LiveDebug hot code replacement: live_debug_code_replace. The list operation additionally supports pprof.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.search_condition is not None:
            result['searchCondition'] = self.search_condition

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('searchCondition') is not None:
            self.search_condition = m.get('searchCondition')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

