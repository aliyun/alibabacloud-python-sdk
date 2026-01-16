# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dm20151123 import models as main_models
from darabonba.model import DaraModel

class GetDedicatedIpWarmUpDetailResponseBody(DaraModel):
    def __init__(
        self,
        detail: List[main_models.GetDedicatedIpWarmUpDetailResponseBodyDetail] = None,
        request_id: str = None,
    ):
        self.detail = detail
        self.request_id = request_id

    def validate(self):
        if self.detail:
            for v1 in self.detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Detail'] = []
        if self.detail is not None:
            for k1 in self.detail:
                result['Detail'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detail = []
        if m.get('Detail') is not None:
            for k1 in m.get('Detail'):
                temp_model = main_models.GetDedicatedIpWarmUpDetailResponseBodyDetail()
                self.detail.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetDedicatedIpWarmUpDetailResponseBodyDetail(DaraModel):
    def __init__(
        self,
        day_mark: int = None,
        deliver_counts: int = None,
        esp: str = None,
        send_counts: int = None,
    ):
        self.day_mark = day_mark
        self.deliver_counts = deliver_counts
        self.esp = esp
        self.send_counts = send_counts

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.day_mark is not None:
            result['DayMark'] = self.day_mark

        if self.deliver_counts is not None:
            result['DeliverCounts'] = self.deliver_counts

        if self.esp is not None:
            result['Esp'] = self.esp

        if self.send_counts is not None:
            result['SendCounts'] = self.send_counts

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DayMark') is not None:
            self.day_mark = m.get('DayMark')

        if m.get('DeliverCounts') is not None:
            self.deliver_counts = m.get('DeliverCounts')

        if m.get('Esp') is not None:
            self.esp = m.get('Esp')

        if m.get('SendCounts') is not None:
            self.send_counts = m.get('SendCounts')

        return self

