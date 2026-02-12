# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ons20190214 import models as main_models
from darabonba.model import DaraModel

class OnsTrendTopicInputTpsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.OnsTrendTopicInputTpsResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The ID of the request. This parameter is a common parameter. Each request has a unique ID. You can use the ID to troubleshoot issues.
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
            temp_model = main_models.OnsTrendTopicInputTpsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class OnsTrendTopicInputTpsResponseBodyData(DaraModel):
    def __init__(
        self,
        records: main_models.OnsTrendTopicInputTpsResponseBodyDataRecords = None,
        title: str = None,
        xunit: str = None,
        yunit: str = None,
    ):
        self.records = records
        # The name of the table.
        self.title = title
        # The unit of the timestamp.
        self.xunit = xunit
        # The unit of the Y axis.
        self.yunit = yunit

    def validate(self):
        if self.records:
            self.records.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.records is not None:
            result['Records'] = self.records.to_map()

        if self.title is not None:
            result['Title'] = self.title

        if self.xunit is not None:
            result['XUnit'] = self.xunit

        if self.yunit is not None:
            result['YUnit'] = self.yunit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Records') is not None:
            temp_model = main_models.OnsTrendTopicInputTpsResponseBodyDataRecords()
            self.records = temp_model.from_map(m.get('Records'))

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('XUnit') is not None:
            self.xunit = m.get('XUnit')

        if m.get('YUnit') is not None:
            self.yunit = m.get('YUnit')

        return self

class OnsTrendTopicInputTpsResponseBodyDataRecords(DaraModel):
    def __init__(
        self,
        stats_data_do: List[main_models.OnsTrendTopicInputTpsResponseBodyDataRecordsStatsDataDo] = None,
    ):
        self.stats_data_do = stats_data_do

    def validate(self):
        if self.stats_data_do:
            for v1 in self.stats_data_do:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['StatsDataDo'] = []
        if self.stats_data_do is not None:
            for k1 in self.stats_data_do:
                result['StatsDataDo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.stats_data_do = []
        if m.get('StatsDataDo') is not None:
            for k1 in m.get('StatsDataDo'):
                temp_model = main_models.OnsTrendTopicInputTpsResponseBodyDataRecordsStatsDataDo()
                self.stats_data_do.append(temp_model.from_map(k1))

        return self

class OnsTrendTopicInputTpsResponseBodyDataRecordsStatsDataDo(DaraModel):
    def __init__(
        self,
        x: int = None,
        y: float = None,
    ):
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.x is not None:
            result['X'] = self.x

        if self.y is not None:
            result['Y'] = self.y

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        return self

