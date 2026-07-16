# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DisableNotifyPolicyResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        uuid: str = None,
    ):
        # The unique ID of the request. Used for troubleshooting and ticket tracking.
        self.request_id = request_id
        # Indicates whether the operation was successful.
        self.success = success
        # The uuid of the notification policy that was operated on.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        if self.uuid is not None:
            result['uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')

        return self

