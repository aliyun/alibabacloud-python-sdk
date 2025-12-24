# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveDomainSnapshotDataResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        snapshot_data_infos: main_models.DescribeLiveDomainSnapshotDataResponseBodySnapshotDataInfos = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The daily statistics on the number of snapshots.
        self.snapshot_data_infos = snapshot_data_infos

    def validate(self):
        if self.snapshot_data_infos:
            self.snapshot_data_infos.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.snapshot_data_infos is not None:
            result['SnapshotDataInfos'] = self.snapshot_data_infos.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SnapshotDataInfos') is not None:
            temp_model = main_models.DescribeLiveDomainSnapshotDataResponseBodySnapshotDataInfos()
            self.snapshot_data_infos = temp_model.from_map(m.get('SnapshotDataInfos'))

        return self

class DescribeLiveDomainSnapshotDataResponseBodySnapshotDataInfos(DaraModel):
    def __init__(
        self,
        snapshot_data_info: List[main_models.DescribeLiveDomainSnapshotDataResponseBodySnapshotDataInfosSnapshotDataInfo] = None,
    ):
        self.snapshot_data_info = snapshot_data_info

    def validate(self):
        if self.snapshot_data_info:
            for v1 in self.snapshot_data_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SnapshotDataInfo'] = []
        if self.snapshot_data_info is not None:
            for k1 in self.snapshot_data_info:
                result['SnapshotDataInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.snapshot_data_info = []
        if m.get('SnapshotDataInfo') is not None:
            for k1 in m.get('SnapshotDataInfo'):
                temp_model = main_models.DescribeLiveDomainSnapshotDataResponseBodySnapshotDataInfosSnapshotDataInfo()
                self.snapshot_data_info.append(temp_model.from_map(k1))

        return self

class DescribeLiveDomainSnapshotDataResponseBodySnapshotDataInfosSnapshotDataInfo(DaraModel):
    def __init__(
        self,
        date: str = None,
        total: int = None,
    ):
        # The date.
        self.date = date
        # The total number of snapshots that were captured on the day.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date is not None:
            result['Date'] = self.date

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

