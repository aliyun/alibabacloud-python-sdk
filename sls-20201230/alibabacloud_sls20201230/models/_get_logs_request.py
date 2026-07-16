# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetLogsRequest(DaraModel):
    def __init__(
        self,
        from_: int = None,
        line: int = None,
        offset: int = None,
        power_sql: bool = None,
        query: str = None,
        reverse: bool = None,
        to: int = None,
        topic: str = None,
    ):
        # The start of the query time range, based on the log time specified when the log data was written.
        # 
        # - The **from** and **to** parameters define a left-closed, right-open interval [from, to). If **from** equals **to**, the interval is invalid and the system returns an error.
        # 
        # - Value: a UNIX timestamp representing the number of seconds elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # > To avoid missing data, align the query time to the minute level. If a time range is specified in the analytic statement, that time range takes precedence.
        # 
        # To specify a time in seconds within an analytic statement, use the [from_unixtime function](https://help.aliyun.com/document_detail/63451.html) or the [to_unixtime function](https://help.aliyun.com/document_detail/63451.html) to convert the time format. Examples:
        # 
        # - `* | SELECT * FROM log WHERE from_unixtime(__time__) > from_unixtime(1664186624) AND from_unixtime(__time__) < now()`
        # 
        # - `* | SELECT * FROM log WHERE __time__ > to_unixtime(date_parse(\\"2022-10-19 15:46:05\\", \\"%Y-%m-%d %H:%i:%s\\")) AND __time__ < to_unixtime(now())`
        # 
        # This parameter is required.
        self.from_ = from_
        # Valid only when the query parameter is a search statement. Maximum number of logs to return. Valid values: 0 to 100. Default value: 100. See [Page through query and analysis results](https://help.aliyun.com/document_detail/89994.html).
        self.line = line
        # Valid only when the query parameter is a search statement. The starting row for the query. Default value: 0. See [Page through query and analysis results](https://help.aliyun.com/document_detail/89994.html).
        self.offset = offset
        # Whether to enable the Exclusive SQL feature. See [Enable the Exclusive SQL feature](https://help.aliyun.com/document_detail/223777.html).
        # 
        # - true: Enable Exclusive SQL.
        # 
        # - false (default): Use standard SQL.
        # 
        # Alternatively, add `set session parallel_sql=true;` to the analytic statement in the **query** parameter to enable Exclusive SQL.
        self.power_sql = power_sql
        # The search statement or analytic statement. See [Query overview](https://help.aliyun.com/document_detail/43772.html) and [Analysis overview](https://help.aliyun.com/document_detail/53608.html). To enable the Exclusive SQL feature, add `set session parallel_sql=true;` to the analytic statement. Example: `* | set session parallel_sql=true; select count(*) as pv`. For common query and analysis issues, see [Common errors that occur when you query and analyze logs](https://help.aliyun.com/document_detail/61628.html).
        # 
        # > When the query parameter contains an analytic statement (SQL statement), the `line` and `offset` parameters are ignored. Set both to 0 and use the LIMIT clause in the SQL statement for pagination. See [Page through query and analysis results](https://help.aliyun.com/document_detail/89994.html).
        self.query = query
        # Whether to return logs in descending order of timestamp, with minute-level precision.
        # 
        # - true: Descending order (newest first).
        # 
        # - false (default): Ascending order (oldest first).
        # 
        # >Notice: 
        # 
        # - When the query parameter is a search statement, the reverse parameter controls the sort order.
        # 
        # - When the query parameter includes an analytic statement, the reverse parameter is ignored. Use the ORDER BY clause in the SQL statement instead. ORDER BY defaults to ascending (asc). Specify desc for descending order.
        self.reverse = reverse
        # The end of the query time range, based on the log time specified when the log data was written.
        # 
        # - The **from** and **to** parameters define a left-closed, right-open interval [from, to). If **from** equals **to**, the interval is invalid and the system returns an error.
        # 
        # - Value: a UNIX timestamp representing the number of seconds elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # > To avoid missing data, align the query time to the minute level. If a time range is specified in the analytic statement, that time range takes precedence.
        # 
        # To specify a time in seconds within an analytic statement, use the [from_unixtime function](https://help.aliyun.com/document_detail/63451.html) or the [to_unixtime function](https://help.aliyun.com/document_detail/63451.html) to convert the time format. Examples:
        # 
        # - `* | SELECT * FROM log WHERE from_unixtime(__time__) > from_unixtime(1664186624) AND from_unixtime(__time__) < now()`
        # 
        # - `* | SELECT * FROM log WHERE __time__ > to_unixtime(date_parse(\\"2022-10-19 15:46:05\\", \\"%Y-%m-%d %H:%i:%s\\")) AND __time__ < to_unixtime(now())`
        # 
        # This parameter is required.
        self.to = to
        # The log topic. Default value: an empty string. See [Topic](https://help.aliyun.com/document_detail/48881.html).
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_ is not None:
            result['from'] = self.from_

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

        if self.to is not None:
            result['to'] = self.to

        if self.topic is not None:
            result['topic'] = self.topic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('from') is not None:
            self.from_ = m.get('from')

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

        if m.get('to') is not None:
            self.to = m.get('to')

        if m.get('topic') is not None:
            self.topic = m.get('topic')

        return self

