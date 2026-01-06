# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class CreateThreadResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        thread: main_models.CreateThreadResponseBodyThread = None,
    ):
        self.request_id = request_id
        self.thread = thread

    def validate(self):
        if self.thread:
            self.thread.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.thread is not None:
            result['thread'] = self.thread.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('thread') is not None:
            temp_model = main_models.CreateThreadResponseBodyThread()
            self.thread = temp_model.from_map(m.get('thread'))

        return self

class CreateThreadResponseBodyThread(DaraModel):
    def __init__(
        self,
        create_at: int = None,
        id: str = None,
    ):
        self.create_at = create_at
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_at is not None:
            result['createAt'] = self.create_at

        if self.id is not None:
            result['id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createAt') is not None:
            self.create_at = m.get('createAt')

        if m.get('id') is not None:
            self.id = m.get('id')

        return self

