# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetLogsV2Request(DaraModel):
    def __init__(
        self,
        forward: bool = None,
        from_: int = None,
        highlight: bool = None,
        is_accurate: bool = None,
        line: int = None,
        offset: int = None,
        power_sql: bool = None,
        query: str = None,
        reverse: bool = None,
        session: str = None,
        to: int = None,
        topic: str = None,
    ):
        # For a scan or phrase query, specifies whether to page forward or backward.
        self.forward = forward
        # The start of the time range to query. The value is the log time that was specified when the log was written.
        # 
        # The time range is a left-closed right-open interval. This means the range includes the start time but not the end time. If the from and to values are the same, the interval is invalid and an error is returned. The value is a UNIX timestamp that represents the number of seconds since 00:00:00 UTC on January 1, 1970.
        # 
        # This parameter is required.
        self.from_ = from_
        # Specifies whether to highlight the results.
        self.highlight = highlight
        # Specifies whether to enable nanosecond-level sorting.
        self.is_accurate = is_accurate
        # The maximum number of logs to return. This parameter is valid only if the query parameter contains a query statement. The value must be an integer from 0 to 100. The default value is 100.
        self.line = line
        # The line number from which to start the query. This parameter is valid only if the query parameter contains a query statement. The default value is 0.
        self.offset = offset
        # Specifies whether to enable enhanced SQL. The default value is false.
        self.power_sql = power_sql
        # The query statement or analytic statement. For more information, see [Query overview](https://help.aliyun.com/document_detail/43772.html) and [Analysis overview](https://help.aliyun.com/document_detail/53608.html).
        # 
        # To use the Exclusive SQL feature, add set session parallel_sql=true; to the analytic statement in the query parameter. Example: \\* | set session parallel_sql=true; select count(\\*) as pv.
        # 
        # Note: If the query parameter contains an analytic statement (SQL statement), the line and offset parameters are invalid. Set them to 0. Use the LIMIT clause in the SQL statement for paging. For more information, see Paginate query and analysis results.
        self.query = query
        # Specifies whether to return logs in descending order of their timestamps. The precision is at the minute level.
        # 
        # true: Returns logs in descending order of their timestamps. false (default): Returns logs in ascending order of their timestamps. Note: If the query parameter contains a query statement, the reverse parameter is valid and specifies the sorting order. If the query parameter contains a query and analysis statement, the reverse parameter is invalid. The sorting order is specified by the ORDER BY clause in the analytic statement. If ORDER BY is asc (default), logs are sorted in ascending order. If ORDER BY is desc, logs are sorted in descending order.
        self.reverse = reverse
        # The query parameter.
        self.session = session
        # The end of the time range to query. The value is the log time that was specified when the log was written.
        # 
        # The time range is a left-closed right-open interval. This means the range includes the start time but not the end time. If the from and to values are the same, the interval is invalid and an error is returned. The value is a UNIX timestamp that represents the number of seconds since 00:00:00 UTC on January 1, 1970.
        # 
        # This parameter is required.
        self.to = to
        # The log topic. The default value is double quotation marks ("").
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.forward is not None:
            result['forward'] = self.forward

        if self.from_ is not None:
            result['from'] = self.from_

        if self.highlight is not None:
            result['highlight'] = self.highlight

        if self.is_accurate is not None:
            result['isAccurate'] = self.is_accurate

        if self.line is not None:
            result['line'] = self.line

        if self.offset is not None:
            result['offset'] = self.offset

        if self.power_sql is not None:
            result['powerSql'] = self.power_sql

        if self.query is not None:
            result['query'] = self.query

        if self.reverse is not None:
            result['reverse'] = self.reverse

        if self.session is not None:
            result['session'] = self.session

        if self.to is not None:
            result['to'] = self.to

        if self.topic is not None:
            result['topic'] = self.topic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('forward') is not None:
            self.forward = m.get('forward')

        if m.get('from') is not None:
            self.from_ = m.get('from')

        if m.get('highlight') is not None:
            self.highlight = m.get('highlight')

        if m.get('isAccurate') is not None:
            self.is_accurate = m.get('isAccurate')

        if m.get('line') is not None:
            self.line = m.get('line')

        if m.get('offset') is not None:
            self.offset = m.get('offset')

        if m.get('powerSql') is not None:
            self.power_sql = m.get('powerSql')

        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('reverse') is not None:
            self.reverse = m.get('reverse')

        if m.get('session') is not None:
            self.session = m.get('session')

        if m.get('to') is not None:
            self.to = m.get('to')

        if m.get('topic') is not None:
            self.topic = m.get('topic')

        return self

