# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartRestoreTaskRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        owner_id: str = None,
        restore_task_id: str = None,
    ):
        # A client token. It ensures the idempotence of the request and prevents the same request from being submitted multiple times.
        self.client_token = client_token
        self.owner_id = owner_id
        # The ID of the restore job.
        # 
        # This parameter is required.
        self.restore_task_id = restore_task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.restore_task_id is not None:
            result['RestoreTaskId'] = self.restore_task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RestoreTaskId') is not None:
            self.restore_task_id = m.get('RestoreTaskId')

        return self

