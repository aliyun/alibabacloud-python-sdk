# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeDefenseRecordsResponseBody(DaraModel):
    def __init__(
        self,
        defense_records: List[main_models.DescribeDefenseRecordsResponseBodyDefenseRecords] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # An array that consists of details of the log of an advanced mitigation session.
        self.defense_records = defense_records
        # The ID of the request.
        self.request_id = request_id
        # The total number of advanced mitigation sessions.
        self.total_count = total_count

    def validate(self):
        if self.defense_records:
            for v1 in self.defense_records:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DefenseRecords'] = []
        if self.defense_records is not None:
            for k1 in self.defense_records:
                result['DefenseRecords'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.defense_records = []
        if m.get('DefenseRecords') is not None:
            for k1 in m.get('DefenseRecords'):
                temp_model = main_models.DescribeDefenseRecordsResponseBodyDefenseRecords()
                self.defense_records.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDefenseRecordsResponseBodyDefenseRecords(DaraModel):
    def __init__(
        self,
        attack_peak: int = None,
        end_time: int = None,
        event_count: int = None,
        instance_id: str = None,
        start_time: int = None,
        status: int = None,
    ):
        # The peak attack traffic. Unit: bit/s.
        self.attack_peak = attack_peak
        # The end time of the advanced mitigation session. This value is a UNIX timestamp. Units: miliseconds.
        self.end_time = end_time
        # The number of attacks.
        self.event_count = event_count
        # The ID of the instance.
        self.instance_id = instance_id
        # The start time of the advanced mitigation session. This value is a UNIX timestamp. Units: miliseconds.
        self.start_time = start_time
        # The status of the advanced mitigation session. Valid values:
        # 
        # *   **0**: The advanced mitigation session is being used.
        # *   **1**: The advanced mitigation session is used.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attack_peak is not None:
            result['AttackPeak'] = self.attack_peak

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.event_count is not None:
            result['EventCount'] = self.event_count

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttackPeak') is not None:
            self.attack_peak = m.get('AttackPeak')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EventCount') is not None:
            self.event_count = m.get('EventCount')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

