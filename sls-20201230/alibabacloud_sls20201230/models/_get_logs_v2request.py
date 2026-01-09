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
        line: int = None,
        offset: int = None,
        power_sql: bool = None,
        query: str = None,
        reverse: bool = None,
        session: str = None,
        to: int = None,
        topic: str = None,
    ):
        # Specifies whether to page forward or backward for the scan-based query or phrase search.
        self.forward = forward
        # The beginning of the time range to query. The value is the log time that is specified when log data is written.
        # 
        # The time range that is specified in this operation is a left-closed, right-open interval. The interval includes the start time specified by the from parameter, but does not include the end time specified by the to parameter. If you specify the same value for the from and to parameters, the interval is invalid, and an error message is returned. The value is a timestamp that follows the UNIX time format. It is the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # This parameter is required.
        self.from_ = from_
        # Specifies whether to highlight the returned result.
        self.highlight = highlight
        # The maximum number of logs to return for the request. This parameter takes effect only when the query parameter is set to a search statement. Valid values: 0 to 100. Default value: 100.
        self.line = line
        # The line from which the query starts. This parameter takes effect only when the query parameter is set to a search statement. Default value: 0.
        self.offset = offset
        # Specifies whether to enable the SQL enhancement feature. By default, the feature is disabled.
        self.power_sql = power_sql
        # The search statement or query statement. For more information, see the "Log search overview" and "Log analysis overview" topics.
        # 
        # If you add set session parallel_sql=true; to the analytic statement in the query parameter, Dedicated SQL is used. Example: \\* | set session parallel_sql=true; select count(\\*) as pv.
        # 
        # Note: If you specify an analytic statement in the query parameter, the line and offset parameters do not take effect in this operation. In this case, we recommend that you set the line and offset parameters to 0 and use the LIMIT clause to specify the number of logs to return on each page. For more information, see the "Perform paged queries" topic.
        self.query = query
        # Specifies whether to return logs in reverse chronological order of log timestamps. The log timestamps are accurate to minutes. Valid values:
        # 
        # true: Logs are returned in reverse chronological order of log timestamps. false (default): Logs are returned in chronological order of log timestamps. Note: The reverse parameter takes effect only when the query parameter is set to a search statement. The reverse parameter specifies the method used to sort returned logs. If the query parameter is set to a query statement, the reverse parameter does not take effect. The method used to sort returned logs is specified by the ORDER BY clause in the analytic statement. If you use the keyword asc in the ORDER BY clause, the logs are sorted in chronological order. If you use the keyword desc in the ORDER BY clause, the logs are sorted in reverse chronological order. By default, asc is used in the ORDER BY clause.
        self.reverse = reverse
        # The parameter that is used to query data.
        self.session = session
        # The end of the time range to query. The value is the log time that is specified when log data is written.
        # 
        # The time range that is specified in this operation is a left-closed, right-open interval. The interval includes the start time specified by the from parameter, but does not include the end time specified by the to parameter. If you specify the same value for the from and to parameters, the interval is invalid, and an error message is returned. The value is a timestamp that follows the UNIX time format. It is the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # This parameter is required.
        self.to = to
        # The topic of the logs. Default value: double quotation marks ("").
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

