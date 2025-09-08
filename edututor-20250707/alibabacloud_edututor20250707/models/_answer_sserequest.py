# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_edututor20250707 import models as main_models
from darabonba.model import DaraModel

class AnswerSSERequest(DaraModel):
    def __init__(
        self,
        messages: List[main_models.AnswerSSERequestMessages] = None,
        parameters: main_models.AnswerSSERequestParameters = None,
        workspace_id: str = None,
    ):
        self.messages = messages
        self.parameters = parameters
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.messages:
            for v1 in self.messages:
                 if v1:
                    v1.validate()
        if self.parameters:
            self.parameters.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['messages'] = []
        if self.messages is not None:
            for k1 in self.messages:
                result['messages'].append(k1.to_map() if k1 else None)

        if self.parameters is not None:
            result['parameters'] = self.parameters.to_map()

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.messages = []
        if m.get('messages') is not None:
            for k1 in m.get('messages'):
                temp_model = main_models.AnswerSSERequestMessages()
                self.messages.append(temp_model.from_map(k1))

        if m.get('parameters') is not None:
            temp_model = main_models.AnswerSSERequestParameters()
            self.parameters = temp_model.from_map(m.get('parameters'))

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

class AnswerSSERequestParameters(DaraModel):
    def __init__(
        self,
        grade: int = None,
        stage: str = None,
        subject: str = None,
    ):
        self.grade = grade
        self.stage = stage
        self.subject = subject

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.grade is not None:
            result['grade'] = self.grade

        if self.stage is not None:
            result['stage'] = self.stage

        if self.subject is not None:
            result['subject'] = self.subject

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('grade') is not None:
            self.grade = m.get('grade')

        if m.get('stage') is not None:
            self.stage = m.get('stage')

        if m.get('subject') is not None:
            self.subject = m.get('subject')

        return self



class AnswerSSERequestMessages(DaraModel):
    def __init__(
        self,
        content: List[Dict[str, str]] = None,
        role: str = None,
    ):
        self.content = content
        # This parameter is required.
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.role is not None:
            result['role'] = self.role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('role') is not None:
            self.role = m.get('role')

        return self

