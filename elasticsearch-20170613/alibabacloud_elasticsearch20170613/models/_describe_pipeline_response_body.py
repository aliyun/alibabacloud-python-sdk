# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class DescribePipelineResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.DescribePipelineResponseBodyResult = None,
    ):
        # The time when the pipeline was updated.
        self.request_id = request_id
        # The type of the queue. Valid values:
        # 
        # *   MEMORY: a traditional memory-based queue.
        # *   PERSISTED: disk-based ACKed queue (persistent queue).
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.DescribePipelineResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class DescribePipelineResponseBodyResult(DaraModel):
    def __init__(
        self,
        batch_delay: int = None,
        batch_size: int = None,
        config: str = None,
        description: str = None,
        gmt_created_time: str = None,
        gmt_update_time: str = None,
        pipeline_id: str = None,
        pipeline_status: str = None,
        queue_check_point_writes: int = None,
        queue_max_bytes: int = None,
        queue_type: str = None,
        workers: int = None,
    ):
        # The time when the pipeline was created.
        self.batch_delay = batch_delay
        self.batch_size = batch_size
        # The description of the pipeline.
        self.config = config
        # The state of the MPS queue. Valid values:
        # 
        # *   NOT_DEPLOYED: The node is not deployed.
        # *   RUNNING
        # *   DELETED: Deleted. The console does not display this status.
        self.description = description
        self.gmt_created_time = gmt_created_time
        # The total capacity of the queue in bytes. Unit: MB.
        self.gmt_update_time = gmt_update_time
        # Number of queue checkpoint writes.
        self.pipeline_id = pipeline_id
        self.pipeline_status = pipeline_status
        # Pipeline batch delay. Unit: milliseconds.
        self.queue_check_point_writes = queue_check_point_writes
        # The number of pipeline workers.
        self.queue_max_bytes = queue_max_bytes
        # The specific configuration of the pipeline.
        self.queue_type = queue_type
        # The size of the pipeline batch.
        self.workers = workers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_delay is not None:
            result['batchDelay'] = self.batch_delay

        if self.batch_size is not None:
            result['batchSize'] = self.batch_size

        if self.config is not None:
            result['config'] = self.config

        if self.description is not None:
            result['description'] = self.description

        if self.gmt_created_time is not None:
            result['gmtCreatedTime'] = self.gmt_created_time

        if self.gmt_update_time is not None:
            result['gmtUpdateTime'] = self.gmt_update_time

        if self.pipeline_id is not None:
            result['pipelineId'] = self.pipeline_id

        if self.pipeline_status is not None:
            result['pipelineStatus'] = self.pipeline_status

        if self.queue_check_point_writes is not None:
            result['queueCheckPointWrites'] = self.queue_check_point_writes

        if self.queue_max_bytes is not None:
            result['queueMaxBytes'] = self.queue_max_bytes

        if self.queue_type is not None:
            result['queueType'] = self.queue_type

        if self.workers is not None:
            result['workers'] = self.workers

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('batchDelay') is not None:
            self.batch_delay = m.get('batchDelay')

        if m.get('batchSize') is not None:
            self.batch_size = m.get('batchSize')

        if m.get('config') is not None:
            self.config = m.get('config')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('gmtCreatedTime') is not None:
            self.gmt_created_time = m.get('gmtCreatedTime')

        if m.get('gmtUpdateTime') is not None:
            self.gmt_update_time = m.get('gmtUpdateTime')

        if m.get('pipelineId') is not None:
            self.pipeline_id = m.get('pipelineId')

        if m.get('pipelineStatus') is not None:
            self.pipeline_status = m.get('pipelineStatus')

        if m.get('queueCheckPointWrites') is not None:
            self.queue_check_point_writes = m.get('queueCheckPointWrites')

        if m.get('queueMaxBytes') is not None:
            self.queue_max_bytes = m.get('queueMaxBytes')

        if m.get('queueType') is not None:
            self.queue_type = m.get('queueType')

        if m.get('workers') is not None:
            self.workers = m.get('workers')

        return self

