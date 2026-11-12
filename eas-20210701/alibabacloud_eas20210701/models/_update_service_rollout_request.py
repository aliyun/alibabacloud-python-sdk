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
        # **Batch**  
        # * Type: object
        # * Required: no
        # * Description: The batch rollout configuration. Used to adjust batch policy parameters. Mutually exclusive with Partition.
        self.batch = batch
        # **Partition**  
        # * Type: object
        # * Required: no
        # * Description: The partition rollout configuration. Used to adjust partition policy parameters. Mutually exclusive with Batch.
        self.partition = partition
        # Specifies whether to pause the rollout. A value of `true` indicates that the rollout is paused. A value of `false` indicates that the rollout is resumed.
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
        # **Partition**  
        # * Type: string
        # * Required: yes
        # * Description: The partition value. Two formats are supported:
        #   1. Integer format: such as "5", which indicates that 5 old replicas are retained.
        #   2. Percentage format: such as "50%", which indicates that 50% of the old replicas are retained.
        #   Adjustment strategies:
        #   - Increase the value: Roll back to the old version and increase the proportion of old replicas.
        #   - Decrease the value: Proceed to the new version and decrease the proportion of old replicas.
        #   - Set to "0%": Complete the full update and switch all replicas to the new version.
        # * Example: 30%
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
        # The batch size. The number of replicas to update in each batch. Integer or percentage formats are supported. Default value: `"25%"`.
        self.batch_size = batch_size
        # The batch interval. The wait time between two rollouts. Supported units: `s` (seconds), `m` (minutes), and `h` (hours).
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

