# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_fc20230330 import models as main_models
from darabonba.model import DaraModel

class PutAsyncInvokeConfigInput(DaraModel):
    def __init__(
        self,
        async_task: bool = None,
        destination_config: main_models.DestinationConfig = None,
        max_async_event_age_in_seconds: int = None,
        max_async_retry_attempts: int = None,
    ):
        # Optional. Specify whether to enable the asynchronous task feature.
        self.async_task = async_task
        # Optional. The struct of the destination of asynchronous invocations.
        self.destination_config = destination_config
        # Optional. The maximum validity period of a message. Valid values: [1,604800]. Default value: 86400. Unit: seconds.
        self.max_async_event_age_in_seconds = max_async_event_age_in_seconds
        # Optional. The maximum number of retries if an asynchronous invocation fails. Valid values: [0,8]. If you do not configure this parameter, the default number of retries is 3.
        self.max_async_retry_attempts = max_async_retry_attempts

    def validate(self):
        if self.destination_config:
            self.destination_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.async_task is not None:
            result['asyncTask'] = self.async_task

        if self.destination_config is not None:
            result['destinationConfig'] = self.destination_config.to_map()

        if self.max_async_event_age_in_seconds is not None:
            result['maxAsyncEventAgeInSeconds'] = self.max_async_event_age_in_seconds

        if self.max_async_retry_attempts is not None:
            result['maxAsyncRetryAttempts'] = self.max_async_retry_attempts

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('asyncTask') is not None:
            self.async_task = m.get('asyncTask')

        if m.get('destinationConfig') is not None:
            temp_model = main_models.DestinationConfig()
            self.destination_config = temp_model.from_map(m.get('destinationConfig'))

        if m.get('maxAsyncEventAgeInSeconds') is not None:
            self.max_async_event_age_in_seconds = m.get('maxAsyncEventAgeInSeconds')

        if m.get('maxAsyncRetryAttempts') is not None:
            self.max_async_retry_attempts = m.get('maxAsyncRetryAttempts')

        return self

