# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_domain20160511 import models as main_models
from darabonba.model import DaraModel

class QueryFailReasonListResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.QueryFailReasonListResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.QueryFailReasonListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryFailReasonListResponseBodyData(DaraModel):
    def __init__(
        self,
        fail_record: List[main_models.QueryFailReasonListResponseBodyDataFailRecord] = None,
    ):
        self.fail_record = fail_record

    def validate(self):
        if self.fail_record:
            for v1 in self.fail_record:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FailRecord'] = []
        if self.fail_record is not None:
            for k1 in self.fail_record:
                result['FailRecord'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fail_record = []
        if m.get('FailRecord') is not None:
            for k1 in m.get('FailRecord'):
                temp_model = main_models.QueryFailReasonListResponseBodyDataFailRecord()
                self.fail_record.append(temp_model.from_map(k1))

        return self

class QueryFailReasonListResponseBodyDataFailRecord(DaraModel):
    def __init__(
        self,
        date: str = None,
        fail_reason: str = None,
    ):
        self.date = date
        self.fail_reason = fail_reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date is not None:
            result['Date'] = self.date

        if self.fail_reason is not None:
            result['FailReason'] = self.fail_reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')

        if m.get('FailReason') is not None:
            self.fail_reason = m.get('FailReason')

        return self

