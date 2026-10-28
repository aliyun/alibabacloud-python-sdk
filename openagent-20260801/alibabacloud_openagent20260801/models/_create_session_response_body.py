# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_openagent20260801 import models as main_models
from darabonba.model import DaraModel

class CreateSessionResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.CreateSessionResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The session information of the created session.
        self.data = data
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.CreateSessionResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class CreateSessionResponseBodyData(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        pinned: bool = None,
        session_id: str = None,
        status: str = None,
        updated_at: str = None,
    ):
        # The time when the session was created, in ISO 8601 format.
        self.created_at = created_at
        # Indicates whether the session is pinned.
        self.pinned = pinned
        # The session ID.
        self.session_id = session_id
        # The session status. The value is fixed to `IDLE` upon successful creation.
        self.status = status
        # The time when the session was last updated, in ISO 8601 format.
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.pinned is not None:
            result['pinned'] = self.pinned

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.status is not None:
            result['status'] = self.status

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('pinned') is not None:
            self.pinned = m.get('pinned')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        return self

