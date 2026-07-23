# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateExperimentRunResponseBody(DaraModel):
    def __init__(
        self,
        message: str = None,
        record_id: str = None,
        request_id: str = None,
        status: str = None,
    ):
        # The message.
        self.message = message
        # The experiment record ID. For online experiments, the format is typically exp-run-{uuid32}. For offline experiments, the format may also be a standard UUID.
        self.record_id = record_id
        # The request ID.
        self.request_id = request_id
        # The experiment record status. After creation, the status is typically pending.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['message'] = self.message

        if self.record_id is not None:
            result['recordId'] = self.record_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('recordId') is not None:
            self.record_id = m.get('recordId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

