# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class GetHistogramsResponse(DaraModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: List[main_models.GetHistogramsResponseBody] = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            for v1 in self.body:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.headers is not None:
            result['headers'] = self.headers

        if self.status_code is not None:
            result['statusCode'] = self.status_code

        result['body'] = []
        if self.body is not None:
            for k1 in self.body:
                result['body'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')

        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')

        self.body = []
        if m.get('body') is not None:
            for k1 in m.get('body'):
                temp_model = main_models.GetHistogramsResponseBody()
                self.body.append(temp_model.from_map(k1))

        return self

class GetHistogramsResponseBody(DaraModel):
    def __init__(
        self,
        from_: int = None,
        to: int = None,
        count: int = None,
        progress: str = None,
    ):
        # The beginning of the time range for the subinterval. The value is a UNIX timestamp that represents the number of seconds that have elapsed since 1970-01-01 00:00:00 UTC.
        # 
        # The time range is a left-closed, right-open interval. This means that the subinterval includes the start time but not the end time. If the values of from and to are the same, the interval is invalid and an error is returned.
        self.from_ = from_
        # The end of the time range for the subinterval. The value is a UNIX timestamp that represents the number of seconds that have elapsed since 1970-01-01 00:00:00 UTC.
        # 
        # The time range is a left-closed, right-open interval. This means that the subinterval includes the start time but not the end time. If the values of from and to are the same, the interval is invalid and an error is returned.
        self.to = to
        # The number of logs that are found in the subinterval.
        self.count = count
        # Indicates whether the query result in the subinterval is complete.
        # 
        # Complete: The query is complete and the result is complete.
        # 
        # Incomplete: The query is complete but the result is incomplete. Send the request again to obtain the complete result.
        self.progress = progress

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_ is not None:
            result['from'] = self.from_

        if self.to is not None:
            result['to'] = self.to

        if self.count is not None:
            result['count'] = self.count

        if self.progress is not None:
            result['progress'] = self.progress

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('from') is not None:
            self.from_ = m.get('from')

        if m.get('to') is not None:
            self.to = m.get('to')

        if m.get('count') is not None:
            self.count = m.get('count')

        if m.get('progress') is not None:
            self.progress = m.get('progress')

        return self

