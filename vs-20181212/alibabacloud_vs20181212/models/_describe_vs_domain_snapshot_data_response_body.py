# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class DescribeVsDomainSnapshotDataResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        snapshot_data_per_interval: main_models.DescribeVsDomainSnapshotDataResponseBodySnapshotDataPerInterval = None,
    ):
        self.request_id = request_id
        self.snapshot_data_per_interval = snapshot_data_per_interval

    def validate(self):
        if self.snapshot_data_per_interval:
            self.snapshot_data_per_interval.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.snapshot_data_per_interval is not None:
            result['SnapshotDataPerInterval'] = self.snapshot_data_per_interval.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SnapshotDataPerInterval') is not None:
            temp_model = main_models.DescribeVsDomainSnapshotDataResponseBodySnapshotDataPerInterval()
            self.snapshot_data_per_interval = temp_model.from_map(m.get('SnapshotDataPerInterval'))

        return self

class DescribeVsDomainSnapshotDataResponseBodySnapshotDataPerInterval(DaraModel):
    def __init__(
        self,
        data_module: List[main_models.DescribeVsDomainSnapshotDataResponseBodySnapshotDataPerIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for v1 in self.data_module:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataModule'] = []
        if self.data_module is not None:
            for k1 in self.data_module:
                result['DataModule'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k1 in m.get('DataModule'):
                temp_model = main_models.DescribeVsDomainSnapshotDataResponseBodySnapshotDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k1))

        return self

class DescribeVsDomainSnapshotDataResponseBodySnapshotDataPerIntervalDataModule(DaraModel):
    def __init__(
        self,
        snapshot_value: str = None,
        time_stamp: str = None,
    ):
        self.snapshot_value = snapshot_value
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.snapshot_value is not None:
            result['SnapshotValue'] = self.snapshot_value

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SnapshotValue') is not None:
            self.snapshot_value = m.get('SnapshotValue')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        return self

