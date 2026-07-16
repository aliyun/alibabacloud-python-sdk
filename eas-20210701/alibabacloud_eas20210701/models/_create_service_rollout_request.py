# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eas20210701 import models as main_models
from darabonba.model import DaraModel

class CreateServiceRolloutRequest(DaraModel):
    def __init__(
        self,
        batch: main_models.CreateServiceRolloutRequestBatch = None,
        partition: main_models.CreateServiceRolloutRequestPartition = None,
        paused: bool = None,
    ):
        # The configuration for the Batch strategy.
        self.batch = batch
        # The configuration for the Partition strategy.
        self.partition = partition
        # Specifies whether to pause the rollout.
        self.paused = paused

    def validate(self):
        if self.batch:
            self.batch.validate()
        if self.partition:
            self.partition.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch is not None:
            result['Batch'] = self.batch.to_map()

        if self.partition is not None:
            result['Partition'] = self.partition.to_map()

        if self.paused is not None:
            result['Paused'] = self.paused

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Batch') is not None:
            temp_model = main_models.CreateServiceRolloutRequestBatch()
            self.batch = temp_model.from_map(m.get('Batch'))

        if m.get('Partition') is not None:
            temp_model = main_models.CreateServiceRolloutRequestPartition()
            self.partition = temp_model.from_map(m.get('Partition'))

        if m.get('Paused') is not None:
            self.paused = m.get('Paused')

        return self

class CreateServiceRolloutRequestPartition(DaraModel):
    def __init__(
        self,
        partition: str = None,
    ):
        # The number of instances to update to the new version.
        self.partition = partition

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.partition is not None:
            result['Partition'] = self.partition

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Partition') is not None:
            self.partition = m.get('Partition')

        return self

class CreateServiceRolloutRequestBatch(DaraModel):
    def __init__(
        self,
        batch_size: str = None,
        interval: str = None,
    ):
        # The number of instances to update in each batch.
        self.batch_size = batch_size
        # The wait interval after each batch completes.
        self.interval = interval

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_size is not None:
            result['BatchSize'] = self.batch_size

        if self.interval is not None:
            result['Interval'] = self.interval

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchSize') is not None:
            self.batch_size = m.get('BatchSize')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        return self

