# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_openagent20260801 import models as main_models
from darabonba.model import DaraModel

class GetRunResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetRunResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned data.
        self.data = data
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
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
            temp_model = main_models.GetRunResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class GetRunResponseBodyData(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        outcome: main_models.GetRunResponseBodyDataOutcome = None,
        run_id: str = None,
        session_id: str = None,
        status: str = None,
        updated_at: str = None,
    ):
        # The time when the run was created, in ISO 8601 format.
        self.created_at = created_at
        # The run outcome.
        self.outcome = outcome
        # The run ID.
        self.run_id = run_id
        # The session ID.
        self.session_id = session_id
        # The run status: `PENDING` (pending execution), `RUNNING` (running), `WAITING_USER` (waiting for interrupt processing), `COMPLETED` (completed), `FAILED` (failed), `CANCELLED` (canceled), or `REJECTED` (rejected).
        self.status = status
        # The time when the run was last updated, in ISO 8601 format.
        self.updated_at = updated_at

    def validate(self):
        if self.outcome:
            self.outcome.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.outcome is not None:
            result['outcome'] = self.outcome.to_map()

        if self.run_id is not None:
            result['runId'] = self.run_id

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.status is not None:
            result['status'] = self.status

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('outcome') is not None:
            temp_model = main_models.GetRunResponseBodyDataOutcome()
            self.outcome = temp_model.from_map(m.get('outcome'))

        if m.get('runId') is not None:
            self.run_id = m.get('runId')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        return self

class GetRunResponseBodyDataOutcome(DaraModel):
    def __init__(
        self,
        interrupts: List[main_models.GetRunResponseBodyDataOutcomeInterrupts] = None,
        type: str = None,
    ):
        # The list of interrupts.
        self.interrupts = interrupts
        # The outcome type: `success` (completed successfully) or `interrupt` (waiting for interrupt processing).
        self.type = type

    def validate(self):
        if self.interrupts:
            for v1 in self.interrupts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['interrupts'] = []
        if self.interrupts is not None:
            for k1 in self.interrupts:
                result['interrupts'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.interrupts = []
        if m.get('interrupts') is not None:
            for k1 in m.get('interrupts'):
                temp_model = main_models.GetRunResponseBodyDataOutcomeInterrupts()
                self.interrupts.append(temp_model.from_map(k1))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class GetRunResponseBodyDataOutcomeInterrupts(DaraModel):
    def __init__(
        self,
        data: main_models.GetRunResponseBodyDataOutcomeInterruptsData = None,
        expires_at: str = None,
        id: str = None,
        message: str = None,
        metadata: Dict[str, Any] = None,
        reason: str = None,
        response_schema: Dict[str, Any] = None,
        tool_call_id: str = None,
    ):
        # The interrupt data.
        self.data = data
        # The expiration time of the interrupt, in ISO 8601 format.
        self.expires_at = expires_at
        # The interrupt ID.
        self.id = id
        # The interrupt prompt.
        self.message = message
        # The extended information.
        self.metadata = metadata
        # The reason for the interrupt: `tool_call` (tool calling requires processing), `input_required` (user input is required), `confirmation` (confirmation is required), or `out_of_band_approval` (waiting for out-of-band approval).
        self.reason = reason
        # The JSON Schema that the payload must conform to when resuming the interrupt.
        self.response_schema = response_schema
        # The ID used to invoke the tool calling.
        self.tool_call_id = tool_call_id

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

        if self.expires_at is not None:
            result['expiresAt'] = self.expires_at

        if self.id is not None:
            result['id'] = self.id

        if self.message is not None:
            result['message'] = self.message

        if self.metadata is not None:
            result['metadata'] = self.metadata

        if self.reason is not None:
            result['reason'] = self.reason

        if self.response_schema is not None:
            result['responseSchema'] = self.response_schema

        if self.tool_call_id is not None:
            result['toolCallId'] = self.tool_call_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.GetRunResponseBodyDataOutcomeInterruptsData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('expiresAt') is not None:
            self.expires_at = m.get('expiresAt')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('metadata') is not None:
            self.metadata = m.get('metadata')

        if m.get('reason') is not None:
            self.reason = m.get('reason')

        if m.get('responseSchema') is not None:
            self.response_schema = m.get('responseSchema')

        if m.get('toolCallId') is not None:
            self.tool_call_id = m.get('toolCallId')

        return self

class GetRunResponseBodyDataOutcomeInterruptsData(DaraModel):
    def __init__(
        self,
        api_calls: List[main_models.GetRunResponseBodyDataOutcomeInterruptsDataApiCalls] = None,
        approval_id: str = None,
        approval_url: str = None,
        cancellable: bool = None,
        change_digest: str = None,
        title: str = None,
    ):
        # The list of APIs pending approval.
        self.api_calls = api_calls
        # The approval ID.
        self.approval_id = approval_id
        # The approval URL.
        self.approval_url = approval_url
        # Specifies whether the interrupt can be canceled.
        self.cancellable = cancellable
        # The change digest.
        self.change_digest = change_digest
        # The approval title.
        self.title = title

    def validate(self):
        if self.api_calls:
            for v1 in self.api_calls:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['apiCalls'] = []
        if self.api_calls is not None:
            for k1 in self.api_calls:
                result['apiCalls'].append(k1.to_map() if k1 else None)

        if self.approval_id is not None:
            result['approvalId'] = self.approval_id

        if self.approval_url is not None:
            result['approvalUrl'] = self.approval_url

        if self.cancellable is not None:
            result['cancellable'] = self.cancellable

        if self.change_digest is not None:
            result['changeDigest'] = self.change_digest

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_calls = []
        if m.get('apiCalls') is not None:
            for k1 in m.get('apiCalls'):
                temp_model = main_models.GetRunResponseBodyDataOutcomeInterruptsDataApiCalls()
                self.api_calls.append(temp_model.from_map(k1))

        if m.get('approvalId') is not None:
            self.approval_id = m.get('approvalId')

        if m.get('approvalUrl') is not None:
            self.approval_url = m.get('approvalUrl')

        if m.get('cancellable') is not None:
            self.cancellable = m.get('cancellable')

        if m.get('changeDigest') is not None:
            self.change_digest = m.get('changeDigest')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class GetRunResponseBodyDataOutcomeInterruptsDataApiCalls(DaraModel):
    def __init__(
        self,
        action: str = None,
        description: str = None,
    ):
        # The API name.
        self.action = action
        # The operation description.
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['action'] = self.action

        if self.description is not None:
            result['description'] = self.description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')

        if m.get('description') is not None:
            self.description = m.get('description')

        return self

