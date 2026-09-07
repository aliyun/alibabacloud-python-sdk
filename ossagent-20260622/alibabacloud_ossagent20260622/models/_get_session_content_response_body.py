# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ossagent20260622 import models as main_models
from darabonba.model import DaraModel

class GetSessionContentResponseBody(DaraModel):
    def __init__(
        self,
        content: List[main_models.GetSessionContentResponseBodyContent] = None,
        request_id: str = None,
        session_id: str = None,
    ):
        # The conversation text content.
        self.content = content
        # Id of the request
        self.request_id = request_id
        # The session ID.
        self.session_id = session_id

    def validate(self):
        if self.content:
            for v1 in self.content:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['content'] = []
        if self.content is not None:
            for k1 in self.content:
                result['content'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content = []
        if m.get('content') is not None:
            for k1 in m.get('content'):
                temp_model = main_models.GetSessionContentResponseBodyContent()
                self.content.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        return self

class GetSessionContentResponseBodyContent(DaraModel):
    def __init__(
        self,
        agent_contents: List[main_models.GetSessionContentResponseBodyContentAgentContents] = None,
        timestamp: str = None,
        tool_confirm: bool = None,
        user_content: str = None,
    ):
        # The detailed conversation content.
        self.agent_contents = agent_contents
        # The time when the session occurred, in the yyyy-MM-dd HH:mm:ss,SSS format.
        self.timestamp = timestamp
        # Indicates whether tool confirmation is required.
        self.tool_confirm = tool_confirm
        # The user content of the first message in the session.
        self.user_content = user_content

    def validate(self):
        if self.agent_contents:
            for v1 in self.agent_contents:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['agentContents'] = []
        if self.agent_contents is not None:
            for k1 in self.agent_contents:
                result['agentContents'].append(k1.to_map() if k1 else None)

        if self.timestamp is not None:
            result['timestamp'] = self.timestamp

        if self.tool_confirm is not None:
            result['toolConfirm'] = self.tool_confirm

        if self.user_content is not None:
            result['userContent'] = self.user_content

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.agent_contents = []
        if m.get('agentContents') is not None:
            for k1 in m.get('agentContents'):
                temp_model = main_models.GetSessionContentResponseBodyContentAgentContents()
                self.agent_contents.append(temp_model.from_map(k1))

        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')

        if m.get('toolConfirm') is not None:
            self.tool_confirm = m.get('toolConfirm')

        if m.get('userContent') is not None:
            self.user_content = m.get('userContent')

        return self

class GetSessionContentResponseBodyContentAgentContents(DaraModel):
    def __init__(
        self,
        agent_content: str = None,
        timestamp: str = None,
    ):
        # The detailed conversation chunk content. All chunks compose the complete response.
        self.agent_content = agent_content
        # The time when the content was generated, in the yyyy-MM-dd HH:mm:ss,SSS format.
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_content is not None:
            result['agentContent'] = self.agent_content

        if self.timestamp is not None:
            result['timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentContent') is not None:
            self.agent_content = m.get('agentContent')

        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')

        return self

