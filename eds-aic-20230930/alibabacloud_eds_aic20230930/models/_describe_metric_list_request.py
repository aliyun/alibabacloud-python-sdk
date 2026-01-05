# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class DescribeMetricListRequest(DaraModel):
    def __init__(
        self,
        android_instance_ids: List[str] = None,
        end_time: str = None,
        instance_ids: List[str] = None,
        length: str = None,
        metric_names: List[str] = None,
        next_token: str = None,
        period: int = None,
        process_infos: List[main_models.DescribeMetricListRequestProcessInfos] = None,
        start_time: str = None,
    ):
        self.android_instance_ids = android_instance_ids
        self.end_time = end_time
        self.instance_ids = instance_ids
        self.length = length
        # This parameter is required.
        self.metric_names = metric_names
        self.next_token = next_token
        self.period = period
        self.process_infos = process_infos
        self.start_time = start_time

    def validate(self):
        if self.process_infos:
            for v1 in self.process_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.android_instance_ids is not None:
            result['AndroidInstanceIds'] = self.android_instance_ids

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.length is not None:
            result['Length'] = self.length

        if self.metric_names is not None:
            result['MetricNames'] = self.metric_names

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.period is not None:
            result['Period'] = self.period

        result['ProcessInfos'] = []
        if self.process_infos is not None:
            for k1 in self.process_infos:
                result['ProcessInfos'].append(k1.to_map() if k1 else None)

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceIds') is not None:
            self.android_instance_ids = m.get('AndroidInstanceIds')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('Length') is not None:
            self.length = m.get('Length')

        if m.get('MetricNames') is not None:
            self.metric_names = m.get('MetricNames')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        self.process_infos = []
        if m.get('ProcessInfos') is not None:
            for k1 in m.get('ProcessInfos'):
                temp_model = main_models.DescribeMetricListRequestProcessInfos()
                self.process_infos.append(temp_model.from_map(k1))

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeMetricListRequestProcessInfos(DaraModel):
    def __init__(
        self,
        process_ids: List[int] = None,
        process_name: str = None,
    ):
        self.process_ids = process_ids
        self.process_name = process_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.process_ids is not None:
            result['ProcessIds'] = self.process_ids

        if self.process_name is not None:
            result['ProcessName'] = self.process_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProcessIds') is not None:
            self.process_ids = m.get('ProcessIds')

        if m.get('ProcessName') is not None:
            self.process_name = m.get('ProcessName')

        return self

