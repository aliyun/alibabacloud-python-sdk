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
        # The request ID. A unique identifier returned with each request, used for troubleshooting and tracing.
        self.request_id = request_id
        # The rollout strategy information. Contains the strategy configuration (Strategy) and execution status (Status).
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
        # The rollout execution status. Contains the current rollout progress and phase information.
        self.status = status
        # The rollout strategy configuration. Contains the specific configuration parameters for partition-based or batch-based rollout.
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
        # The batch rollout configuration. This field is returned only if a batch-based rollout strategy is used.
        self.batch = batch
        # The partition rollout configuration. This field is returned only if a partition-based rollout strategy is used.
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
        # The partition value. Specifies the number or percentage of old replicas to retain. For example, \\"50%\\" indicates that 50% of the old replicas are retained.
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
        # The batch size. The number or percentage of replicas to update in each batch.
        self.batch_size = batch_size
        # The batch interval. The wait time between two consecutive rollout batches.
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
        # The current revision. The identifier of the version that is currently running.
        self.current_revision = current_revision
        # The time when the next batch starts updating, in the format of YYYY/MM/DD HH:mm:ss.
        self.next_batch_start_time = next_batch_start_time
        # The rollout phase. Valid values:
        # - Pending: Waiting to start the rollout.
        # - Running: The rollout is in progress.
        # - Paused: The rollout is paused.
        # - Completed: The rollout is completed.
        # - Failed: The rollout failed.
        self.phase = phase
        # The total number of replicas for the service.
        self.total_replicas = total_replicas
        # The update revision. The identifier of the target version to which the service is being updated.
        self.update_revision = update_revision
        # The number of replicas that have been updated to the new version.
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

