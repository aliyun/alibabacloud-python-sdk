# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class BatchRemoveConsumerGroupConsumersResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.BatchRemoveConsumerGroupConsumersResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response status code. Ok is returned if the request is successful.
        self.code = code
        # The response data.
        self.data = data
        # The response message.
        self.message = message
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.BatchRemoveConsumerGroupConsumersResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class BatchRemoveConsumerGroupConsumersResponseBodyData(DaraModel):
    def __init__(
        self,
        failed_consumer_ids: List[str] = None,
        skipped_consumer_ids: List[str] = None,
        success_consumer_ids: List[str] = None,
    ):
        # The list of consumer IDs that failed to be removed.
        self.failed_consumer_ids = failed_consumer_ids
        # The list of consumer IDs skipped because they are not in the consumer group.
        self.skipped_consumer_ids = skipped_consumer_ids
        # The list of consumer IDs successfully removed from the consumer group.
        self.success_consumer_ids = success_consumer_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed_consumer_ids is not None:
            result['failedConsumerIds'] = self.failed_consumer_ids

        if self.skipped_consumer_ids is not None:
            result['skippedConsumerIds'] = self.skipped_consumer_ids

        if self.success_consumer_ids is not None:
            result['successConsumerIds'] = self.success_consumer_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('failedConsumerIds') is not None:
            self.failed_consumer_ids = m.get('failedConsumerIds')

        if m.get('skippedConsumerIds') is not None:
            self.skipped_consumer_ids = m.get('skippedConsumerIds')

        if m.get('successConsumerIds') is not None:
            self.success_consumer_ids = m.get('successConsumerIds')

        return self

