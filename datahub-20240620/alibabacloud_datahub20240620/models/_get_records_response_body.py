# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_datahub20240620 import models as main_models
from darabonba.model import DaraModel

class GetRecordsResponseBody(DaraModel):
    def __init__(
        self,
        records: List[main_models.GetRecordsResponseBodyRecords] = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.records = records
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.records:
            for v1 in self.records:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Records'] = []
        if self.records is not None:
            for k1 in self.records:
                result['Records'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.records = []
        if m.get('Records') is not None:
            for k1 in m.get('Records'):
                temp_model = main_models.GetRecordsResponseBodyRecords()
                self.records.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self



class GetRecordsResponseBodyRecords(DaraModel):
    def __init__(
        self,
        attributes: Dict[str, str] = None,
        data: List[str] = None,
        system_time: int = None,
    ):
        self.attributes = attributes
        self.data = data
        self.system_time = system_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attributes is not None:
            result['Attributes'] = self.attributes

        if self.data is not None:
            result['Data'] = self.data

        if self.system_time is not None:
            result['SystemTime'] = self.system_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')

        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('SystemTime') is not None:
            self.system_time = m.get('SystemTime')

        return self

