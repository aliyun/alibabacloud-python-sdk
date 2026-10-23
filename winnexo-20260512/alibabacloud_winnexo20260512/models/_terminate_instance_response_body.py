# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TerminateInstanceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        instance_id: str = None,
        instance_status: str = None,
        message: str = None,
        request_id: str = None,
        state_version: int = None,
        terminated: bool = None,
    ):
        # The business status code. A value of 200 indicates success.
        self.code = code
        # The physical instance ID.
        self.instance_id = instance_id
        # The status after termination.
        self.instance_status = instance_status
        # The error message.
        self.message = message
        # The request tracking ID.
        self.request_id = request_id
        # The state version.
        self.state_version = state_version
        # Indicates whether the termination was successful. A value of true indicates success. If the termination fails, the error code and message are returned.
        self.terminated = terminated

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.instance_status is not None:
            result['instanceStatus'] = self.instance_status

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.state_version is not None:
            result['stateVersion'] = self.state_version

        if self.terminated is not None:
            result['terminated'] = self.terminated

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('instanceStatus') is not None:
            self.instance_status = m.get('instanceStatus')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('stateVersion') is not None:
            self.state_version = m.get('stateVersion')

        if m.get('terminated') is not None:
            self.terminated = m.get('terminated')

        return self

