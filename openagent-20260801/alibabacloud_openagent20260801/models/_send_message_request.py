# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_openagent20260801 import models as main_models
from darabonba.model import DaraModel

class SendMessageRequest(DaraModel):
    def __init__(
        self,
        attachments: List[main_models.SendMessageRequestAttachments] = None,
        content: str = None,
        resume: List[main_models.SendMessageRequestResume] = None,
        run_id: str = None,
        type: str = None,
    ):
        # The list of attachments.
        self.attachments = attachments
        # The message text in MESSAGE mode. This parameter cannot be empty. The type parameter can be omitted in this mode.
        self.content = content
        # The list of interrupt replies. This parameter is required when type is set to RESUME. You must reply to all pending interrupts at once. Each interruptId can appear only once.
        self.resume = resume
        # The ID of the active run to resubscribe to. This parameter is required in RECONNECT mode.
        self.run_id = run_id
        # The request type. Valid values: MESSAGE (sends a message), RESUME (resumes a run), and RECONNECT (reconnects to a run). Default value: MESSAGE.
        self.type = type

    def validate(self):
        if self.attachments:
            for v1 in self.attachments:
                 if v1:
                    v1.validate()
        if self.resume:
            for v1 in self.resume:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['attachments'] = []
        if self.attachments is not None:
            for k1 in self.attachments:
                result['attachments'].append(k1.to_map() if k1 else None)

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
        self.attachments = []
        if m.get('attachments') is not None:
            for k1 in m.get('attachments'):
                temp_model = main_models.SendMessageRequestAttachments()
                self.attachments.append(temp_model.from_map(k1))

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
        # The ID of the interrupt to be replied to. Obtain this value from data.outcome.interrupts[].id in the SSE RUN_FINISHED event or the GetRun response.
        self.interrupt_id = interrupt_id
        # The interrupt handling result. This parameter is required when status is set to resolved and must conform to the responseSchema of the corresponding interrupt. Do not pass this parameter when status is set to cancelled.
        self.payload = payload
        # The reply method for the interrupt. Valid values: resolved (submits the answer, confirmation, or tool result required by the interrupt, and must include payload) and cancelled (cancels the interrupt without passing payload).
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

class SendMessageRequestAttachments(DaraModel):
    def __init__(
        self,
        file_extension: str = None,
        file_id: str = None,
        source_name: str = None,
        workspace_path: str = None,
    ):
        # The file name extension.
        self.file_extension = file_extension
        # The ID of the file after it is uploaded.
        self.file_id = file_id
        # The original name of the file.
        self.source_name = source_name
        # The workspace path.
        self.workspace_path = workspace_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_extension is not None:
            result['fileExtension'] = self.file_extension

        if self.file_id is not None:
            result['fileId'] = self.file_id

        if self.source_name is not None:
            result['sourceName'] = self.source_name

        if self.workspace_path is not None:
            result['workspacePath'] = self.workspace_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileExtension') is not None:
            self.file_extension = m.get('fileExtension')

        if m.get('fileId') is not None:
            self.file_id = m.get('fileId')

        if m.get('sourceName') is not None:
            self.source_name = m.get('sourceName')

        if m.get('workspacePath') is not None:
            self.workspace_path = m.get('workspacePath')

        return self

