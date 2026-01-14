# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResultCallbackRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        handle_reason: str = None,
        status: int = None,
    ):
        # The ID of the approval process.
        # 
        # This parameter is required.
        self.application_id = application_id
        # The reason for the approval.
        # 
        # This parameter is required.
        self.handle_reason = handle_reason
        # Approval result:
        # 
        # *   1: passed
        # *   2: rejected
        # 
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.handle_reason is not None:
            result['HandleReason'] = self.handle_reason

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('HandleReason') is not None:
            self.handle_reason = m.get('HandleReason')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

