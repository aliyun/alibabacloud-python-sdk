# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_fc20230330 import models as main_models
from darabonba.model import DaraModel

class AsyncConfig(DaraModel):
    def __init__(
        self,
        async_task: bool = None,
        created_time: str = None,
        destination_config: main_models.DestinationConfig = None,
        function_arn: str = None,
        last_modified_time: str = None,
        max_async_event_age_in_seconds: int = None,
        max_async_retry_attempts: int = None,
    ):
        # Specifies whether to enable the asynchronous task feature.
        self.async_task = async_task
        # The time when the asynchronous invocation configuration was created.
        self.created_time = created_time
        # The destination configuration.
        self.destination_config = destination_config
        # The Alibaba Cloud Resource Name (ARN) of the function.
        self.function_arn = function_arn
        # The time when the asynchronous invocation was last modified.
        self.last_modified_time = last_modified_time
        # The maximum time to live (TTL) value of an event.
        self.max_async_event_age_in_seconds = max_async_event_age_in_seconds
        # The number of times when an asynchronous invocation is retried.
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

        if self.created_time is not None:
            result['createdTime'] = self.created_time

        if self.destination_config is not None:
            result['destinationConfig'] = self.destination_config.to_map()

        if self.function_arn is not None:
            result['functionArn'] = self.function_arn

        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time

        if self.max_async_event_age_in_seconds is not None:
            result['maxAsyncEventAgeInSeconds'] = self.max_async_event_age_in_seconds

        if self.max_async_retry_attempts is not None:
            result['maxAsyncRetryAttempts'] = self.max_async_retry_attempts

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('asyncTask') is not None:
            self.async_task = m.get('asyncTask')

        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')

        if m.get('destinationConfig') is not None:
            temp_model = main_models.DestinationConfig()
            self.destination_config = temp_model.from_map(m.get('destinationConfig'))

        if m.get('functionArn') is not None:
            self.function_arn = m.get('functionArn')

        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')

        if m.get('maxAsyncEventAgeInSeconds') is not None:
            self.max_async_event_age_in_seconds = m.get('maxAsyncEventAgeInSeconds')

        if m.get('maxAsyncRetryAttempts') is not None:
            self.max_async_retry_attempts = m.get('maxAsyncRetryAttempts')

        return self

