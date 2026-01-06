# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetHDMAliyunResourceSyncResultRequest(DaraModel):
    def __init__(
        self,
        task_id: str = None,
        uid: str = None,
        user_id: str = None,
        context: str = None,
        access_key: str = None,
        signature: str = None,
        skip_auth: str = None,
        timestamp: str = None,
    ):
        self.task_id = task_id
        self.uid = uid
        self.user_id = user_id
        self.context = context
        self.access_key = access_key
        self.signature = signature
        self.skip_auth = skip_auth
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.uid is not None:
            result['Uid'] = self.uid

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.context is not None:
            result['__context'] = self.context

        if self.access_key is not None:
            result['accessKey'] = self.access_key

        if self.signature is not None:
            result['signature'] = self.signature

        if self.skip_auth is not None:
            result['skipAuth'] = self.skip_auth

        if self.timestamp is not None:
            result['timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('__context') is not None:
            self.context = m.get('__context')

        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')

        if m.get('signature') is not None:
            self.signature = m.get('signature')

        if m.get('skipAuth') is not None:
            self.skip_auth = m.get('skipAuth')

        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')

        return self

