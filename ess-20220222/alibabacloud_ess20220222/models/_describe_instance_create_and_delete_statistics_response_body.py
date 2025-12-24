# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ess20220222 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceCreateAndDeleteStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        instance_create_and_delete_statistics: main_models.DescribeInstanceCreateAndDeleteStatisticsResponseBodyInstanceCreateAndDeleteStatistics = None,
        request_id: str = None,
    ):
        self.instance_create_and_delete_statistics = instance_create_and_delete_statistics
        self.request_id = request_id

    def validate(self):
        if self.instance_create_and_delete_statistics:
            self.instance_create_and_delete_statistics.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_create_and_delete_statistics is not None:
            result['InstanceCreateAndDeleteStatistics'] = self.instance_create_and_delete_statistics.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceCreateAndDeleteStatistics') is not None:
            temp_model = main_models.DescribeInstanceCreateAndDeleteStatisticsResponseBodyInstanceCreateAndDeleteStatistics()
            self.instance_create_and_delete_statistics = temp_model.from_map(m.get('InstanceCreateAndDeleteStatistics'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeInstanceCreateAndDeleteStatisticsResponseBodyInstanceCreateAndDeleteStatistics(DaraModel):
    def __init__(
        self,
        statistic: List[main_models.DescribeInstanceCreateAndDeleteStatisticsResponseBodyInstanceCreateAndDeleteStatisticsStatistic] = None,
    ):
        self.statistic = statistic

    def validate(self):
        if self.statistic:
            for v1 in self.statistic:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Statistic'] = []
        if self.statistic is not None:
            for k1 in self.statistic:
                result['Statistic'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.statistic = []
        if m.get('Statistic') is not None:
            for k1 in m.get('Statistic'):
                temp_model = main_models.DescribeInstanceCreateAndDeleteStatisticsResponseBodyInstanceCreateAndDeleteStatisticsStatistic()
                self.statistic.append(temp_model.from_map(k1))

        return self

class DescribeInstanceCreateAndDeleteStatisticsResponseBodyInstanceCreateAndDeleteStatisticsStatistic(DaraModel):
    def __init__(
        self,
        created_vm_count: int = None,
        destroyed_vm_count: int = None,
        started_vm_count: int = None,
        stopped_vm_count: int = None,
        time: str = None,
    ):
        self.created_vm_count = created_vm_count
        self.destroyed_vm_count = destroyed_vm_count
        self.started_vm_count = started_vm_count
        self.stopped_vm_count = stopped_vm_count
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_vm_count is not None:
            result['CreatedVmCount'] = self.created_vm_count

        if self.destroyed_vm_count is not None:
            result['DestroyedVmCount'] = self.destroyed_vm_count

        if self.started_vm_count is not None:
            result['StartedVmCount'] = self.started_vm_count

        if self.stopped_vm_count is not None:
            result['StoppedVmCount'] = self.stopped_vm_count

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedVmCount') is not None:
            self.created_vm_count = m.get('CreatedVmCount')

        if m.get('DestroyedVmCount') is not None:
            self.destroyed_vm_count = m.get('DestroyedVmCount')

        if m.get('StartedVmCount') is not None:
            self.started_vm_count = m.get('StartedVmCount')

        if m.get('StoppedVmCount') is not None:
            self.stopped_vm_count = m.get('StoppedVmCount')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self

