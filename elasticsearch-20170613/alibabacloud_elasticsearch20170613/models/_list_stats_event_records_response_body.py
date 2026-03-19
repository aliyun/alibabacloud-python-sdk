# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class ListStatsEventRecordsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.ListStatsEventRecordsResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.ListStatsEventRecordsResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class ListStatsEventRecordsResponseBodyResult(DaraModel):
    def __init__(
        self,
        result: List[main_models.ListStatsEventRecordsResponseBodyResultResult] = None,
        total: str = None,
    ):
        self.result = result
        self.total = total

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['result'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('result') is not None:
            for k1 in m.get('result'):
                temp_model = main_models.ListStatsEventRecordsResponseBodyResultResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListStatsEventRecordsResponseBodyResultResult(DaraModel):
    def __init__(
        self,
        cnt: str = None,
        level: str = None,
        status: str = None,
        type: str = None,
    ):
        self.cnt = cnt
        self.level = level
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cnt is not None:
            result['cnt'] = self.cnt

        if self.level is not None:
            result['level'] = self.level

        if self.status is not None:
            result['status'] = self.status

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cnt') is not None:
            self.cnt = m.get('cnt')

        if m.get('level') is not None:
            self.level = m.get('level')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

