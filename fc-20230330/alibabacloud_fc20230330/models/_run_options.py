# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_fc20230330 import models as main_models
from darabonba.model import DaraModel

class RunOptions(DaraModel):
    def __init__(
        self,
        batch_window: main_models.BatchWindow = None,
        dead_letter_queue: main_models.DeadLetterQueue = None,
        errors_tolerance: str = None,
        mode: str = None,
        retry_strategy: main_models.RetryStrategy = None,
    ):
        self.batch_window = batch_window
        self.dead_letter_queue = dead_letter_queue
        self.errors_tolerance = errors_tolerance
        self.mode = mode
        self.retry_strategy = retry_strategy

    def validate(self):
        if self.batch_window:
            self.batch_window.validate()
        if self.dead_letter_queue:
            self.dead_letter_queue.validate()
        if self.retry_strategy:
            self.retry_strategy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_window is not None:
            result['batchWindow'] = self.batch_window.to_map()

        if self.dead_letter_queue is not None:
            result['deadLetterQueue'] = self.dead_letter_queue.to_map()

        if self.errors_tolerance is not None:
            result['errorsTolerance'] = self.errors_tolerance

        if self.mode is not None:
            result['mode'] = self.mode

        if self.retry_strategy is not None:
            result['retryStrategy'] = self.retry_strategy.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('batchWindow') is not None:
            temp_model = main_models.BatchWindow()
            self.batch_window = temp_model.from_map(m.get('batchWindow'))

        if m.get('deadLetterQueue') is not None:
            temp_model = main_models.DeadLetterQueue()
            self.dead_letter_queue = temp_model.from_map(m.get('deadLetterQueue'))

        if m.get('errorsTolerance') is not None:
            self.errors_tolerance = m.get('errorsTolerance')

        if m.get('mode') is not None:
            self.mode = m.get('mode')

        if m.get('retryStrategy') is not None:
            temp_model = main_models.RetryStrategy()
            self.retry_strategy = temp_model.from_map(m.get('retryStrategy'))

        return self

