# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdatePolarClawAgentSkillsResponseBody(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        application_id: str = None,
        code: int = None,
        message: str = None,
        ok: bool = None,
        request_id: str = None,
        skills: List[str] = None,
    ):
        # Agent ID
        self.agent_id = agent_id
        # The application ID.
        self.application_id = application_id
        # The return code.
        self.code = code
        # The response message.
        self.message = message
        # Indicates whether the operation was successful.
        self.ok = ok
        # Id of the request
        self.request_id = request_id
        # The updated skill list.
        self.skills = skills

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.ok is not None:
            result['Ok'] = self.ok

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.skills is not None:
            result['Skills'] = self.skills

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Ok') is not None:
            self.ok = m.get('Ok')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Skills') is not None:
            self.skills = m.get('Skills')

        return self

