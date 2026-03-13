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
        # The batch window configurations.
        self.batch_window = batch_window
        # Whether to enable dead-letter queues. If you configure this parameter, dead-letter queues are enabled. By default, dead-letter queues are not enabled and messages are discarded when the retry policy is exhausted. Queues of Simple Message Queue (formerly MNS), ApsaraMQ for RocketMQ, and ApsaraMQ for Kafka, and EventBridge event buses can be used as dead-letter queues.
        self.dead_letter_queue = dead_letter_queue
        # The fault tolerance policy. Valid values:
        # 
        # *   **NONE**: does not tolerate exceptions.
        # *   **ALL**: tolerates all exceptions.
        # 
        # >  The default value is **NONE**.
        self.errors_tolerance = errors_tolerance
        # The underlying application mode when message data is pushed to Function Compute. Valid values:
        # 
        # *   **event-streaming**: the event streaming mode. In this mode, events are pushed in arrays. One or more message events are pushed to the function in batches based on your push configurations. This mode is suitable for end-to-end streaming data processing scenarios. The event streaming mode supports the following event sources: Simple Message Queue (formerly MNS), ApsaraMQ for RocketMQ, ApsaraMQ for RabbitMQ, ApsaraMQ for Kafka, ApsaraMQ for MQTT, and Data Transmission Service (DTS).
        # *   **event-driven**: the event mode. In event mode, a single message is passed to the function as event parameters at a time. Events follow the CloudEvents specifications. The event mode supports the following event sources: Default, Simple Message Queue (formerly MNS), ApsaraMQ for RocketMQ, and ApsaraMQ for RabbitMQ. In this mode, batch configurations are not supported.
        self.mode = mode
        # The retry policy that you want to use if events fail to be pushed.
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

