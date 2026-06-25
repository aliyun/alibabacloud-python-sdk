# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eas20210701 import models as main_models
from darabonba.model import DaraModel

class UpdateServiceRolloutRequest(DaraModel):
    def __init__(
        self,
        batch: main_models.UpdateServiceRolloutRequestBatch = None,
        partition: main_models.UpdateServiceRolloutRequestPartition = None,
        paused: bool = None,
    ):
        # The batch rollout configuration. This parameter is mutually exclusive with `Partition`.
        # 
        # - Type: object
        # 
        # - Required: No
        # 
        # - Description: The batch rollout configuration for adjusting batch policy parameters. This parameter is mutually exclusive with Partition.
        self.batch = batch
        # The partition rollout configuration. This parameter is mutually exclusive with `Batch`.
        # 
        # - Type: object
        # 
        # - Required: No
        # 
        # - Description: The partition rollout configuration. This parameter adjusts the parameters for the partition strategy. It is mutually exclusive with `Batch`.
        self.partition = partition
        # Set to `true` to pause the rollout or `false` to resume it.
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
            temp_model = main_models.UpdateServiceRolloutRequestBatch()
            self.batch = temp_model.from_map(m.get('Batch'))

        if m.get('Partition') is not None:
            temp_model = main_models.UpdateServiceRolloutRequestPartition()
            self.partition = temp_model.from_map(m.get('Partition'))

        if m.get('Paused') is not None:
            self.paused = m.get('Paused')

        return self

class UpdateServiceRolloutRequestPartition(DaraModel):
    def __init__(
        self,
        partition: str = None,
    ):
        # **Partition value**
        # 
        # - Type: string
        # 
        # - Required: Yes
        # 
        # - Description: The partition value. This parameter specifies the number or percentage of old-version replicas to retain. It supports two formats:
        # 
        #   1. An integer, such as "5", for the number of replicas.
        # 
        #   2. A percentage, such as "50%", for the proportion of replicas.
        # 
        #   Adjustment strategy:
        # 
        #   - Increasing the value rolls back to the previous version by increasing the number of old-version replicas.
        # 
        #   - Decreasing the value continues the rollout by reducing the number of old-version replicas.
        # 
        #   - Setting the value to "0" or "0%" completes the rollout, replacing all old-version replicas.
        # 
        # - Example: 30%
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

class UpdateServiceRolloutRequestBatch(DaraModel):
    def __init__(
        self,
        batch_size: str = None,
        interval: str = None,
    ):
        # The number of replicas to update in each batch. This can be an integer or a percentage. The default is `"25%"`.
        self.batch_size = batch_size
        # The interval to wait between batches. Supported units include `s` (seconds), `m` (minutes), and `h` (hours).
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

