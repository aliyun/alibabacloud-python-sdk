# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FinishValidateRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_version_id: str = None,
        status: bool = None,
        task_id: str = None,
    ):
        # The application ID used for exact match queries. If omitted, the results are not filtered by application ID.
        self.app_id = app_id
        # The application version ID. **Required**. It must match the application version corresponding to the AdaptorId. This parameter is not the image version ID.
        self.app_version_id = app_version_id
        # The verification result.
        # 
        # This parameter is required.
        self.status = status
        # The task ID.
        # 
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

