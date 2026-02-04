# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class DescribeKvRealTimeQpsDataResponseBody(DaraModel):
    def __init__(
        self,
        aggregate_data: List[main_models.DescribeKvRealTimeQpsDataResponseBodyAggregateData] = None,
        end_time: str = None,
        kv_qps_data: List[main_models.DescribeKvRealTimeQpsDataResponseBodyKvQpsData] = None,
        request_id: str = None,
        start_time: str = None,
    ):
        self.aggregate_data = aggregate_data
        self.end_time = end_time
        self.kv_qps_data = kv_qps_data
        self.request_id = request_id
        self.start_time = start_time

    def validate(self):
        if self.aggregate_data:
            for v1 in self.aggregate_data:
                 if v1:
                    v1.validate()
        if self.kv_qps_data:
            for v1 in self.kv_qps_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AggregateData'] = []
        if self.aggregate_data is not None:
            for k1 in self.aggregate_data:
                result['AggregateData'].append(k1.to_map() if k1 else None)

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        result['KvQpsData'] = []
        if self.kv_qps_data is not None:
            for k1 in self.kv_qps_data:
                result['KvQpsData'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.aggregate_data = []
        if m.get('AggregateData') is not None:
            for k1 in m.get('AggregateData'):
                temp_model = main_models.DescribeKvRealTimeQpsDataResponseBodyAggregateData()
                self.aggregate_data.append(temp_model.from_map(k1))

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        self.kv_qps_data = []
        if m.get('KvQpsData') is not None:
            for k1 in m.get('KvQpsData'):
                temp_model = main_models.DescribeKvRealTimeQpsDataResponseBodyKvQpsData()
                self.kv_qps_data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeKvRealTimeQpsDataResponseBodyKvQpsData(DaraModel):
    def __init__(
        self,
        access_type: str = None,
        key_qps: int = None,
        key_succ_qps: int = None,
        namespace_id: str = None,
        qps: int = None,
        time_stamp: str = None,
    ):
        self.access_type = access_type
        self.key_qps = key_qps
        self.key_succ_qps = key_succ_qps
        self.namespace_id = namespace_id
        self.qps = qps
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_type is not None:
            result['AccessType'] = self.access_type

        if self.key_qps is not None:
            result['KeyQps'] = self.key_qps

        if self.key_succ_qps is not None:
            result['KeySuccQps'] = self.key_succ_qps

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.qps is not None:
            result['Qps'] = self.qps

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')

        if m.get('KeyQps') is not None:
            self.key_qps = m.get('KeyQps')

        if m.get('KeySuccQps') is not None:
            self.key_succ_qps = m.get('KeySuccQps')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('Qps') is not None:
            self.qps = m.get('Qps')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        return self

class DescribeKvRealTimeQpsDataResponseBodyAggregateData(DaraModel):
    def __init__(
        self,
        acc: int = None,
        access_type: str = None,
        key_acc: int = None,
        key_succ_acc: int = None,
    ):
        self.acc = acc
        self.access_type = access_type
        self.key_acc = key_acc
        self.key_succ_acc = key_succ_acc

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acc is not None:
            result['Acc'] = self.acc

        if self.access_type is not None:
            result['AccessType'] = self.access_type

        if self.key_acc is not None:
            result['KeyAcc'] = self.key_acc

        if self.key_succ_acc is not None:
            result['KeySuccAcc'] = self.key_succ_acc

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Acc') is not None:
            self.acc = m.get('Acc')

        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')

        if m.get('KeyAcc') is not None:
            self.key_acc = m.get('KeyAcc')

        if m.get('KeySuccAcc') is not None:
            self.key_succ_acc = m.get('KeySuccAcc')

        return self

