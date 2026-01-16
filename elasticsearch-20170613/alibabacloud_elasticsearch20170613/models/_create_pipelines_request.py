# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class CreatePipelinesRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        body: List[main_models.CreatePipelinesRequestBody] = None,
        trigger: bool = None,
    ):
        self.client_token = client_token
        self.body = body
        self.trigger = trigger

    def validate(self):
        if self.body:
            for v1 in self.body:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        result['body'] = []
        if self.body is not None:
            for k1 in self.body:
                result['body'].append(k1.to_map() if k1 else None)

        if self.trigger is not None:
            result['trigger'] = self.trigger

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        self.body = []
        if m.get('body') is not None:
            for k1 in m.get('body'):
                temp_model = main_models.CreatePipelinesRequestBody()
                self.body.append(temp_model.from_map(k1))

        if m.get('trigger') is not None:
            self.trigger = m.get('trigger')

        return self

class CreatePipelinesRequestBody(DaraModel):
    def __init__(
        self,
        batch_delay: int = None,
        batch_size: int = None,
        config: str = None,
        description: str = None,
        pipeline_id: str = None,
        queue_check_point_writes: int = None,
        queue_max_bytes: int = None,
        queue_type: str = None,
        workers: int = None,
    ):
        self.batch_delay = batch_delay
        self.batch_size = batch_size
        # This parameter is required.
        self.config = config
        self.description = description
        # This parameter is required.
        self.pipeline_id = pipeline_id
        self.queue_check_point_writes = queue_check_point_writes
        self.queue_max_bytes = queue_max_bytes
        self.queue_type = queue_type
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

        if self.pipeline_id is not None:
            result['pipelineId'] = self.pipeline_id

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

        if m.get('pipelineId') is not None:
            self.pipeline_id = m.get('pipelineId')

        if m.get('queueCheckPointWrites') is not None:
            self.queue_check_point_writes = m.get('queueCheckPointWrites')

        if m.get('queueMaxBytes') is not None:
            self.queue_max_bytes = m.get('queueMaxBytes')

        if m.get('queueType') is not None:
            self.queue_type = m.get('queueType')

        if m.get('workers') is not None:
            self.workers = m.get('workers')

        return self

