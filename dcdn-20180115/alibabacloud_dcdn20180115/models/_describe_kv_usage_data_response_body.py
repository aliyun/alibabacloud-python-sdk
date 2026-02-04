# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class DescribeKvUsageDataResponseBody(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        kv_usage_data: List[main_models.DescribeKvUsageDataResponseBodyKvUsageData] = None,
        request_id: str = None,
        start_time: str = None,
    ):
        # The end of the time range during which data was queried.
        self.end_time = end_time
        # The usage details.
        self.kv_usage_data = kv_usage_data
        # The request ID.
        self.request_id = request_id
        # The beginning of the time range during which data was queried.
        self.start_time = start_time

    def validate(self):
        if self.kv_usage_data:
            for v1 in self.kv_usage_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        result['KvUsageData'] = []
        if self.kv_usage_data is not None:
            for k1 in self.kv_usage_data:
                result['KvUsageData'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        self.kv_usage_data = []
        if m.get('KvUsageData') is not None:
            for k1 in m.get('KvUsageData'):
                temp_model = main_models.DescribeKvUsageDataResponseBodyKvUsageData()
                self.kv_usage_data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeKvUsageDataResponseBodyKvUsageData(DaraModel):
    def __init__(
        self,
        acc: int = None,
        access_type: str = None,
        namespace_id: str = None,
        time_stamp: str = None,
    ):
        # The number of visits.
        self.acc = acc
        # The request method. This parameter is available only when the **SplitBy** parameter is set to **type**.
        self.access_type = access_type
        # The namespace ID. This parameter is available only when the **SplitBy** parameter is set to **namespace**.
        self.namespace_id = namespace_id
        # The timestamp of the data returned.
        self.time_stamp = time_stamp

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

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Acc') is not None:
            self.acc = m.get('Acc')

        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        return self

