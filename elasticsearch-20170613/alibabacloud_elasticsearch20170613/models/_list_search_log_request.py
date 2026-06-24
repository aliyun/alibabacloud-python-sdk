# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSearchLogRequest(DaraModel):
    def __init__(
        self,
        begin_time: int = None,
        end_time: int = None,
        page: int = None,
        query: str = None,
        size: int = None,
        type: str = None,
    ):
        # The start timestamp of the log, in milliseconds. The value must be within the last 7 days. If this parameter is not specified, all logs within the [current time - 7 days, endTime\\] range are queried.
        self.begin_time = begin_time
        # The end timestamp of the log, in milliseconds. The value must be within the last 7 days. Specify this parameter. If this parameter is not specified, an empty result is returned.
        self.end_time = end_time
        # The page number of the plug-in list. Minimum value: 1. Default value: 1.
        self.page = page
        # The keyword to query.
        # 
        # This parameter is required.
        self.query = query
        # The number of entries per page for a paged query. Default value: 20. Minimum value: 1. Maximum value: 50.
        self.size = size
        # The log type. Valid values:
        # - INSTANCELOG: primary log.
        # - SEARCHSLOW: searching slow log.
        # - INDEXINGSLOW: indexing slow log.
        # - JVMLOG: GC log.
        # - ES_SEARCH_ACCESS_LOG: Elasticsearch access log.
        # - AUDIT: audit log.
        # 
        # For limits on viewing logs, see [Query logs](https://help.aliyun.com/document_detail/72026.html).
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_time is not None:
            result['beginTime'] = self.begin_time

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.page is not None:
            result['page'] = self.page

        if self.query is not None:
            result['query'] = self.query

        if self.size is not None:
            result['size'] = self.size

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('beginTime') is not None:
            self.begin_time = m.get('beginTime')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('size') is not None:
            self.size = m.get('size')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

