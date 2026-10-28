# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_openagent20260801 import models as main_models
from darabonba.model import DaraModel

class UpdateSessionResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.UpdateSessionResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The session information.
        self.data = data
        # The request ID, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request is successful. A value of true indicates success.
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
            temp_model = main_models.UpdateSessionResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class UpdateSessionResponseBodyData(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        last_run_id: str = None,
        last_run_status: str = None,
        pinned: bool = None,
        session_id: str = None,
        status: str = None,
        title: str = None,
        updated_at: str = None,
    ):
        # The time when the session was created, in RFC 3339 format.
        self.created_at = created_at
        # The ID of the last run.
        self.last_run_id = last_run_id
        # The status of the last run. Valid values:
        # - `PENDING`: Pending.
        # - `RUNNING`: Running.
        # - `WAITING_USER`: Waiting for interrupt handling.
        # - `COMPLETED`: Completed.
        # - `FAILED`: Failed.
        # - `CANCELLED`: Cancelled.
        # - `REJECTED`: Rejected.
        self.last_run_status = last_run_status
        # Indicates whether the session is pinned.
        self.pinned = pinned
        # The session ID.
        self.session_id = session_id
        # The session status. Valid values:
        # - `IDLE`: Idle.
        # - `ACTIVE`: Active.
        # - `WAITING_USER_INPUT`: Waiting for user input.
        # - `WAITING_APPROVAL`: Waiting for user confirmation.
        # - `WAITING_OUT_OF_BAND_APPROVAL`: Waiting for out-of-band approval.
        # - `CLOSED`: Closed.
        self.status = status
        # The session title.
        self.title = title
        # The time when the session was last updated, in RFC 3339 format.
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

        if self.last_run_id is not None:
            result['lastRunId'] = self.last_run_id

        if self.last_run_status is not None:
            result['lastRunStatus'] = self.last_run_status

        if self.pinned is not None:
            result['pinned'] = self.pinned

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.status is not None:
            result['status'] = self.status

        if self.title is not None:
            result['title'] = self.title

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('lastRunId') is not None:
            self.last_run_id = m.get('lastRunId')

        if m.get('lastRunStatus') is not None:
            self.last_run_status = m.get('lastRunStatus')

        if m.get('pinned') is not None:
            self.pinned = m.get('pinned')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        return self

