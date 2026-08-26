# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PrometheusInstanceStoreConfig(DaraModel):
    def __init__(
        self,
        parallel_count_per_host: int = None,
        parallel_enable: bool = None,
        parallel_mode: str = None,
        query_cache_enable: bool = None,
        total_parallel_count: int = None,
    ):
        # The concurrency per host. If this parameter is not specified, the default value is 2. Valid values: 1 to 8.
        self.parallel_count_per_host = parallel_count_per_host
        # Specifies whether to enable parallel query. If this parameter is not specified, the value is considered as false.
        self.parallel_enable = parallel_enable
        # The parallel query mode. Valid values:
        # 
        # - auto
        # - static
        # 
        # If this parameter is not specified, the default value is auto.
        self.parallel_mode = parallel_mode
        # Specifies whether to enable query cache. If this parameter is not specified, the value is considered as false.
        self.query_cache_enable = query_cache_enable
        # The global concurrency. If this parameter is not specified, the default value is 8. Valid values: 2 to 64.
        self.total_parallel_count = total_parallel_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.parallel_count_per_host is not None:
            result['parallelCountPerHost'] = self.parallel_count_per_host

        if self.parallel_enable is not None:
            result['parallelEnable'] = self.parallel_enable

        if self.parallel_mode is not None:
            result['parallelMode'] = self.parallel_mode

        if self.query_cache_enable is not None:
            result['queryCacheEnable'] = self.query_cache_enable

        if self.total_parallel_count is not None:
            result['totalParallelCount'] = self.total_parallel_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('parallelCountPerHost') is not None:
            self.parallel_count_per_host = m.get('parallelCountPerHost')

        if m.get('parallelEnable') is not None:
            self.parallel_enable = m.get('parallelEnable')

        if m.get('parallelMode') is not None:
            self.parallel_mode = m.get('parallelMode')

        if m.get('queryCacheEnable') is not None:
            self.query_cache_enable = m.get('queryCacheEnable')

        if m.get('totalParallelCount') is not None:
            self.total_parallel_count = m.get('totalParallelCount')

        return self

