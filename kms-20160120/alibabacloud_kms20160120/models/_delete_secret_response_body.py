# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteSecretResponseBody(DaraModel):
    def __init__(
        self,
        planned_delete_time: str = None,
        request_id: str = None,
        secret_name: str = None,
    ):
        # The time when the secret is scheduled to be deleted.
        self.planned_delete_time = planned_delete_time
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The name of the secret.
        self.secret_name = secret_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.planned_delete_time is not None:
            result['PlannedDeleteTime'] = self.planned_delete_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.secret_name is not None:
            result['SecretName'] = self.secret_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlannedDeleteTime') is not None:
            self.planned_delete_time = m.get('PlannedDeleteTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')

        return self

