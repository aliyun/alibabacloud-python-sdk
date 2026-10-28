# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_openagent20260801 import models as main_models
from darabonba.model import DaraModel

class SendMessageRequest(DaraModel):
    def __init__(
        self,
        content: str = None,
        resume: List[main_models.SendMessageRequestResume] = None,
        run_id: str = None,
        type: str = None,
    ):
        # The message text in MESSAGE mode. This parameter cannot be empty. The type can be omitted in this mode.
        self.content = content
        # The list of interrupt replies. This parameter is required when `type` is set to `RESUME`. You must reply to all pending interrupts at once, and each `interruptId` can appear only once.
        self.resume = resume
        # The ID of the active run to resubscribe to. This parameter is required in RECONNECT mode.
        self.run_id = run_id
        # The request type. Valid values: `MESSAGE` (sends a message), `RESUME` (resumes a run), and `RECONNECT` (reconnects to a run). Default value: `MESSAGE`.
        self.type = type

    def validate(self):
        if self.resume:
            for v1 in self.resume:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        result['resume'] = []
        if self.resume is not None:
            for k1 in self.resume:
                result['resume'].append(k1.to_map() if k1 else None)

        if self.run_id is not None:
            result['runId'] = self.run_id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        self.resume = []
        if m.get('resume') is not None:
            for k1 in m.get('resume'):
                temp_model = main_models.SendMessageRequestResume()
                self.resume.append(temp_model.from_map(k1))

        if m.get('runId') is not None:
            self.run_id = m.get('runId')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class SendMessageRequestResume(DaraModel):
    def __init__(
        self,
        interrupt_id: str = None,
        payload: Any = None,
        status: str = None,
    ):
        # The ID of the interrupt to be replied to. Obtain this value from `data.outcome.interrupts[].id` in the SSE `RUN_FINISHED` event or `data.outcome.interrupts[].id` in the `GetRun` response.
        self.interrupt_id = interrupt_id
        # The interrupt handling result. This parameter is required when `status` is set to `resolved` and must conform to the `responseSchema` of the corresponding interrupt. Do not pass this parameter when `status` is set to `cancelled`.
        self.payload = payload
        # The reply method for the current interrupt. `resolved` indicates that the answer, confirmation, or tool result required by the interrupt is submitted, and `payload` must be provided. `cancelled` indicates that the interrupt is canceled, and `payload` is not passed.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.interrupt_id is not None:
            result['interruptId'] = self.interrupt_id

        if self.payload is not None:
            result['payload'] = self.payload

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('interruptId') is not None:
            self.interrupt_id = m.get('interruptId')

        if m.get('payload') is not None:
            self.payload = m.get('payload')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

