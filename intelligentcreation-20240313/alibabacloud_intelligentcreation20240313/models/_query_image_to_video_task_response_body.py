# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryImageToVideoTaskResponseBody(DaraModel):
    def __init__(
        self,
        message: str = None,
        origin_url: str = None,
        request_id: str = None,
        status: int = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.message = message
        self.origin_url = origin_url
        self.request_id = request_id
        self.status = status
        self.success = success
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['message'] = self.message

        if self.origin_url is not None:
            result['originUrl'] = self.origin_url

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.status is not None:
            result['status'] = self.status

        if self.success is not None:
            result['success'] = self.success

        if self.task_id is not None:
            result['taskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('originUrl') is not None:
            self.origin_url = m.get('originUrl')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        return self

