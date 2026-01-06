# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class RetrieveRunResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        run: main_models.RetrieveRunResponseBodyRun = None,
    ):
        self.request_id = request_id
        self.run = run

    def validate(self):
        if self.run:
            self.run.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.run is not None:
            result['run'] = self.run.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('run') is not None:
            temp_model = main_models.RetrieveRunResponseBodyRun()
            self.run = temp_model.from_map(m.get('run'))

        return self

class RetrieveRunResponseBodyRun(DaraModel):
    def __init__(
        self,
        cancelled_at: int = None,
        completed_at: int = None,
        create_at: int = None,
        expires_at: int = None,
        failed_at: int = None,
        id: str = None,
        last_error_msg: str = None,
        started_at: int = None,
        status: str = None,
        thread_id: str = None,
    ):
        self.cancelled_at = cancelled_at
        self.completed_at = completed_at
        self.create_at = create_at
        self.expires_at = expires_at
        self.failed_at = failed_at
        self.id = id
        self.last_error_msg = last_error_msg
        self.started_at = started_at
        self.status = status
        self.thread_id = thread_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cancelled_at is not None:
            result['cancelledAt'] = self.cancelled_at

        if self.completed_at is not None:
            result['completedAt'] = self.completed_at

        if self.create_at is not None:
            result['createAt'] = self.create_at

        if self.expires_at is not None:
            result['expiresAt'] = self.expires_at

        if self.failed_at is not None:
            result['failedAt'] = self.failed_at

        if self.id is not None:
            result['id'] = self.id

        if self.last_error_msg is not None:
            result['lastErrorMsg'] = self.last_error_msg

        if self.started_at is not None:
            result['startedAt'] = self.started_at

        if self.status is not None:
            result['status'] = self.status

        if self.thread_id is not None:
            result['threadId'] = self.thread_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cancelledAt') is not None:
            self.cancelled_at = m.get('cancelledAt')

        if m.get('completedAt') is not None:
            self.completed_at = m.get('completedAt')

        if m.get('createAt') is not None:
            self.create_at = m.get('createAt')

        if m.get('expiresAt') is not None:
            self.expires_at = m.get('expiresAt')

        if m.get('failedAt') is not None:
            self.failed_at = m.get('failedAt')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('lastErrorMsg') is not None:
            self.last_error_msg = m.get('lastErrorMsg')

        if m.get('startedAt') is not None:
            self.started_at = m.get('startedAt')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('threadId') is not None:
            self.thread_id = m.get('threadId')

        return self

