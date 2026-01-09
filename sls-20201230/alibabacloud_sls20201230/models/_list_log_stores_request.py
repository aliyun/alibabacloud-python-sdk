# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListLogStoresRequest(DaraModel):
    def __init__(
        self,
        logstore_name: str = None,
        mode: str = None,
        offset: int = None,
        size: int = None,
        telemetry_type: str = None,
    ):
        # The name of the Logstore. Fuzzy match is supported. For example, if you enter test, Logstores whose name contains test are returned.
        self.logstore_name = logstore_name
        # The type of the Logstore. Valid values: standard and query.
        # 
        # *   **standard**: Standard Logstore. This type of Logstore supports the log analysis feature and is suitable for scenarios such as real-time monitoring and interactive analysis. You can also use this type of Logstore to build a comprehensive observability system.
        # *   **query**: Query Logstore. This type of Logstore supports high-performance queries. The index traffic fee of a Query Logstore is approximately half that of a Standard Logstore. Query Logstores do not support SQL analysis. Query Logstores are suitable for scenarios in which the volume of data is large, the log retention period is long, or log analysis is not required. Log retention periods of weeks or months are considered long.
        self.mode = mode
        # The line from which the query starts. Default value: 0.
        self.offset = offset
        # The number of entries per page. Maximum value: 500. Default value: 200.
        self.size = size
        # The type of the data that you want to query. Valid values:
        # 
        # *   None: logs
        # *   Metrics: metrics
        self.telemetry_type = telemetry_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.logstore_name is not None:
            result['logstoreName'] = self.logstore_name

        if self.mode is not None:
            result['mode'] = self.mode

        if self.offset is not None:
            result['offset'] = self.offset

        if self.size is not None:
            result['size'] = self.size

        if self.telemetry_type is not None:
            result['telemetryType'] = self.telemetry_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logstoreName') is not None:
            self.logstore_name = m.get('logstoreName')

        if m.get('mode') is not None:
            self.mode = m.get('mode')

        if m.get('offset') is not None:
            self.offset = m.get('offset')

        if m.get('size') is not None:
            self.size = m.get('size')

        if m.get('telemetryType') is not None:
            self.telemetry_type = m.get('telemetryType')

        return self

