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
        # Specifies whether to page forward or backward for scan or phrase queries.
        self.forward = forward
        # The start time of the query. This time refers to the log time specified when log data is written.
        # 
        # The time range defined by the from and to request parameters follows the left-closed, right-open principle. The time range includes the start time but excludes the end time. If the values of from and to are the same, the time range is invalid and the function returns an error.
        # The value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # This parameter is required.
        self.from_ = from_
        # Specifies whether to enable highlighting.
        self.highlight = highlight
        # Specifies whether to enable nanosecond-precision ordering.
        self.is_accurate = is_accurate
        # The maximum number of logs to return in the request. This parameter is valid only when the query parameter is a query statement (not an analytic statement). Minimum value: 0. Maximum value: 100. Default value: 100.
        self.line = line
        # The start row of the query. This parameter is valid only when the query parameter is a query statement (not an analytic statement). The value starts from 0. Default value: 0.
        self.offset = offset
        # Specifies whether to enable Dedicated SQL. Disabled by default.
        self.power_sql = power_sql
        # The query statement or analytic statement. For more information, see [Query overview](https://help.aliyun.com/document_detail/43772.html) and [Analysis overview](https://help.aliyun.com/document_detail/53608.html).
        # 
        # Add set session parallel_sql=true; to the analytic statement in the query parameter to use Dedicated SQL. Example: * | set session parallel_sql=true; select count(*) as pv.
        # 
        # Note: When the query parameter contains an analytic statement (SQL statement), the line and offset parameters of this API are invalid. Set them to 0. Use the LIMIT syntax in the SQL statement for pagination. For more information, see Display query and analysis results by page.
        self.query = query
        # Specifies whether to return logs in descending order of log timestamps, accurate to the minute level. This parameter is valid only when the query parameter is a query statement (not an analytic statement).
        # 
        # - true: Returns logs in descending order of log timestamps.
        # - false (default): Returns logs in ascending order of log timestamps.
        # 
        # To sort results in an analytic statement, use the ORDER BY syntax. If ORDER BY is set to asc (default), the results are sorted in ascending order. If ORDER BY is set to desc, the results are sorted in descending order.
        self.reverse = reverse
        # The query parameter.
        self.session = session
        # The end time of the query. This time refers to the log time specified when log data is written.
        # 
        # The time range defined by the from and to request parameters follows the left-closed, right-open principle. The time range includes the start time but excludes the end time. If the values of from and to are the same, the time range is invalid and the function returns an error.
        # The value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # This parameter is required.
        self.to = to
        # The topic. Default value: empty string.
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

