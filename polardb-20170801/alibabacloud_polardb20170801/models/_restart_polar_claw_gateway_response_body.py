# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RestartPolarClawGatewayResponseBody(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        code: int = None,
        downtime_ms: int = None,
        gateway_version: str = None,
        message: str = None,
        mode: str = None,
        ok: bool = None,
        operation: str = None,
        request_id: str = None,
        restarted: bool = None,
        state: str = None,
        task_id: str = None,
    ):
        self.application_id = application_id
        self.code = code
        self.downtime_ms = downtime_ms
        self.gateway_version = gateway_version
        self.message = message
        self.mode = mode
        self.ok = ok
        self.operation = operation
        self.request_id = request_id
        self.restarted = restarted
        self.state = state
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.code is not None:
            result['Code'] = self.code

        if self.downtime_ms is not None:
            result['DowntimeMs'] = self.downtime_ms

        if self.gateway_version is not None:
            result['GatewayVersion'] = self.gateway_version

        if self.message is not None:
            result['Message'] = self.message

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.ok is not None:
            result['Ok'] = self.ok

        if self.operation is not None:
            result['Operation'] = self.operation

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.restarted is not None:
            result['Restarted'] = self.restarted

        if self.state is not None:
            result['State'] = self.state

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DowntimeMs') is not None:
            self.downtime_ms = m.get('DowntimeMs')

        if m.get('GatewayVersion') is not None:
            self.gateway_version = m.get('GatewayVersion')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Ok') is not None:
            self.ok = m.get('Ok')

        if m.get('Operation') is not None:
            self.operation = m.get('Operation')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Restarted') is not None:
            self.restarted = m.get('Restarted')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

