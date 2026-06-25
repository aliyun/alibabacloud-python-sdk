# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eas20210701 import models as main_models
from darabonba.model import DaraModel

class DescribeServiceRolloutResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        rollout: main_models.DescribeServiceRolloutResponseBodyRollout = None,
    ):
        # The request ID. This ID is unique to each request and is used for troubleshooting.
        self.request_id = request_id
        # Details of the service rollout, including the rollout strategy (`Strategy`) and execution status (`Status`).
        self.rollout = rollout

    def validate(self):
        if self.rollout:
            self.rollout.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.rollout is not None:
            result['Rollout'] = self.rollout.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Rollout') is not None:
            temp_model = main_models.DescribeServiceRolloutResponseBodyRollout()
            self.rollout = temp_model.from_map(m.get('Rollout'))

        return self

class DescribeServiceRolloutResponseBodyRollout(DaraModel):
    def __init__(
        self,
        status: main_models.DescribeServiceRolloutResponseBodyRolloutStatus = None,
        strategy: main_models.DescribeServiceRolloutResponseBodyRolloutStrategy = None,
    ):
        # The current progress and phase of the rollout.
        self.status = status
        # The rollout strategy configuration. This object contains the parameters for a canary release or batch release.
        self.strategy = strategy

    def validate(self):
        if self.status:
            self.status.validate()
        if self.strategy:
            self.strategy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['Status'] = self.status.to_map()

        if self.strategy is not None:
            result['Strategy'] = self.strategy.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            temp_model = main_models.DescribeServiceRolloutResponseBodyRolloutStatus()
            self.status = temp_model.from_map(m.get('Status'))

        if m.get('Strategy') is not None:
            temp_model = main_models.DescribeServiceRolloutResponseBodyRolloutStrategy()
            self.strategy = temp_model.from_map(m.get('Strategy'))

        return self

class DescribeServiceRolloutResponseBodyRolloutStrategy(DaraModel):
    def __init__(
        self,
        batch: main_models.DescribeServiceRolloutResponseBodyRolloutStrategyBatch = None,
        partition: main_models.DescribeServiceRolloutResponseBodyRolloutStrategyPartition = None,
    ):
        # The configuration for a batch release. This object is returned only when the batch release strategy is used.
        self.batch = batch
        # The configuration for a canary release. This object is returned only when the canary release strategy is used.
        self.partition = partition

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Batch') is not None:
            temp_model = main_models.DescribeServiceRolloutResponseBodyRolloutStrategyBatch()
            self.batch = temp_model.from_map(m.get('Batch'))

        if m.get('Partition') is not None:
            temp_model = main_models.DescribeServiceRolloutResponseBodyRolloutStrategyPartition()
            self.partition = temp_model.from_map(m.get('Partition'))

        return self

class DescribeServiceRolloutResponseBodyRolloutStrategyPartition(DaraModel):
    def __init__(
        self,
        partition: str = None,
    ):
        # Specifies the number or percentage of old replicas to keep. For example, a value of `50%` indicates that 50% of the old replicas are retained.
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

class DescribeServiceRolloutResponseBodyRolloutStrategyBatch(DaraModel):
    def __init__(
        self,
        batch_size: str = None,
        interval: str = None,
    ):
        # The number or percentage of replicas to update in each batch.
        self.batch_size = batch_size
        # The time to wait between batches.
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

class DescribeServiceRolloutResponseBodyRolloutStatus(DaraModel):
    def __init__(
        self,
        current_revision: str = None,
        next_batch_start_time: str = None,
        phase: str = None,
        total_replicas: int = None,
        update_revision: str = None,
        updated_replicas: int = None,
    ):
        # The identifier for the currently running revision.
        self.current_revision = current_revision
        # The scheduled start time for the next batch.
        self.next_batch_start_time = next_batch_start_time
        # The current release phase. Valid values:
        # 
        # - `Pending`: The rollout is waiting to start.
        # 
        # - `Running`: The rollout is in progress.
        # 
        # - `Paused`: The rollout is paused.
        # 
        # - `Completed`: The rollout is complete.
        # 
        # - `Failed`: The rollout has failed.
        self.phase = phase
        # The total number of desired replicas for the service.
        self.total_replicas = total_replicas
        # The identifier for the target revision.
        self.update_revision = update_revision
        # The number of replicas updated to the new revision.
        self.updated_replicas = updated_replicas

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_revision is not None:
            result['CurrentRevision'] = self.current_revision

        if self.next_batch_start_time is not None:
            result['NextBatchStartTime'] = self.next_batch_start_time

        if self.phase is not None:
            result['Phase'] = self.phase

        if self.total_replicas is not None:
            result['TotalReplicas'] = self.total_replicas

        if self.update_revision is not None:
            result['UpdateRevision'] = self.update_revision

        if self.updated_replicas is not None:
            result['UpdatedReplicas'] = self.updated_replicas

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentRevision') is not None:
            self.current_revision = m.get('CurrentRevision')

        if m.get('NextBatchStartTime') is not None:
            self.next_batch_start_time = m.get('NextBatchStartTime')

        if m.get('Phase') is not None:
            self.phase = m.get('Phase')

        if m.get('TotalReplicas') is not None:
            self.total_replicas = m.get('TotalReplicas')

        if m.get('UpdateRevision') is not None:
            self.update_revision = m.get('UpdateRevision')

        if m.get('UpdatedReplicas') is not None:
            self.updated_replicas = m.get('UpdatedReplicas')

        return self

