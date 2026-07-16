# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetHistogramsRequest(DaraModel):
    def __init__(
        self,
        from_: int = None,
        query: str = None,
        to: int = None,
        topic: str = None,
    ):
        # The beginning of the time range for the subinterval. The value is a UNIX timestamp that represents the number of seconds that have elapsed since 1970-01-01 00:00:00 UTC.
        # 
        # This parameter is required.
        self.from_ = from_
        # The search statement. Only search statements are supported. Analytic statements are not supported. For more information about the syntax of search statements, see [Search syntax](https://help.aliyun.com/document_detail/43772.html).
        self.query = query
        # The end of the time range for the subinterval. The value is a UNIX timestamp that represents the number of seconds that have elapsed since 1970-01-01 00:00:00 UTC.
        # 
        # This parameter is required.
        self.to = to
        # The topic of the log.
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

        if self.query is not None:
            result['query'] = self.query

        if self.to is not None:
            result['to'] = self.to

        if self.topic is not None:
            result['topic'] = self.topic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('from') is not None:
            self.from_ = m.get('from')

        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('to') is not None:
            self.to = m.get('to')

        if m.get('topic') is not None:
            self.topic = m.get('topic')

        return self

