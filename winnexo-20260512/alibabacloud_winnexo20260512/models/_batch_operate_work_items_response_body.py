# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class BatchOperateWorkItemsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        items: List[main_models.BatchOperateWorkItemsResponseBodyItems] = None,
        message: str = None,
        request_id: str = None,
        skipped: int = None,
        succeeded: int = None,
    ):
        # The business status code. A value of 200 indicates success.
        self.code = code
        # The results for each item. The order of the results matches the order of the items in the request.
        self.items = items
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The number of skipped or failed operations.
        self.skipped = skipped
        # The number of successful operations.
        self.succeeded = succeeded

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.skipped is not None:
            result['skipped'] = self.skipped

        if self.succeeded is not None:
            result['succeeded'] = self.succeeded

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.BatchOperateWorkItemsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('skipped') is not None:
            self.skipped = m.get('skipped')

        if m.get('succeeded') is not None:
            self.succeeded = m.get('succeeded')

        return self



class BatchOperateWorkItemsResponseBodyItems(DaraModel):
    def __init__(
        self,
        reason: str = None,
        success: bool = None,
        work_item_id: str = None,
    ):
        # The reason for skipping or failure.
        self.reason = reason
        # Indicates whether the execution was successful.
        self.success = success
        # The ID of the work item.
        self.work_item_id = work_item_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.reason is not None:
            result['reason'] = self.reason

        if self.success is not None:
            result['success'] = self.success

        if self.work_item_id is not None:
            result['workItemId'] = self.work_item_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('reason') is not None:
            self.reason = m.get('reason')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('workItemId') is not None:
            self.work_item_id = m.get('workItemId')

        return self

