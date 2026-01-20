# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_paifeaturestore20230621 import models as main_models
from darabonba.model import DaraModel

class FeatureViewConfigValue(DaraModel):
    def __init__(
        self,
        partitions: Dict[str, main_models.FeatureViewConfigValuePartitionsValue] = None,
        event_time: str = None,
        equal: bool = None,
        use_mock: bool = None,
        snapshot: main_models.FeatureViewConfigValueSnapshot = None,
    ):
        self.partitions = partitions
        self.event_time = event_time
        self.equal = equal
        self.use_mock = use_mock
        self.snapshot = snapshot

    def validate(self):
        if self.partitions:
            for v1 in self.partitions.values():
                 if v1:
                    v1.validate()
        if self.snapshot:
            self.snapshot.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Partitions'] = {}
        if self.partitions is not None:
            for k1, v1 in self.partitions.items():
                result['Partitions'][k1] = v1.to_map() if v1 else None

        if self.event_time is not None:
            result['EventTime'] = self.event_time

        if self.equal is not None:
            result['Equal'] = self.equal

        if self.use_mock is not None:
            result['UseMock'] = self.use_mock

        if self.snapshot is not None:
            result['Snapshot'] = self.snapshot.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.partitions = {}
        if m.get('Partitions') is not None:
            for k1, v1 in m.get('Partitions').items():
                temp_model = main_models.FeatureViewConfigValuePartitionsValue()
                self.partitions[k1] = temp_model.from_map(v1)

        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')

        if m.get('Equal') is not None:
            self.equal = m.get('Equal')

        if m.get('UseMock') is not None:
            self.use_mock = m.get('UseMock')

        if m.get('Snapshot') is not None:
            temp_model = main_models.FeatureViewConfigValueSnapshot()
            self.snapshot = temp_model.from_map(m.get('Snapshot'))

        return self



class FeatureViewConfigValueSnapshot(DaraModel):
    def __init__(
        self,
        partitions: Dict[str, main_models.FeatureViewConfigValueSnapshotPartitionsValue] = None,
        table: str = None,
    ):
        self.partitions = partitions
        self.table = table

    def validate(self):
        if self.partitions:
            for v1 in self.partitions.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Partitions'] = {}
        if self.partitions is not None:
            for k1, v1 in self.partitions.items():
                result['Partitions'][k1] = v1.to_map() if v1 else None

        if self.table is not None:
            result['Table'] = self.table

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.partitions = {}
        if m.get('Partitions') is not None:
            for k1, v1 in m.get('Partitions').items():
                temp_model = main_models.FeatureViewConfigValueSnapshotPartitionsValue()
                self.partitions[k1] = temp_model.from_map(v1)

        if m.get('Table') is not None:
            self.table = m.get('Table')

        return self

