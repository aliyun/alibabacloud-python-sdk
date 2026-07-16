# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class UpdatePolarClawAgentToolsResponseBody(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        application_id: str = None,
        code: int = None,
        message: str = None,
        ok: bool = None,
        request_id: str = None,
        tools: main_models.UpdatePolarClawAgentToolsResponseBodyTools = None,
    ):
        # Agent ID
        self.agent_id = agent_id
        # The application ID.
        self.application_id = application_id
        # The status code.
        self.code = code
        # The response message.
        self.message = message
        # Indicates whether the operation was successful.
        self.ok = ok
        # Id of the request
        self.request_id = request_id
        # The updated tool configuration.
        self.tools = tools

    def validate(self):
        if self.tools:
            self.tools.validate()

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

        if self.tools is not None:
            result['Tools'] = self.tools.to_map()

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

        if m.get('Tools') is not None:
            temp_model = main_models.UpdatePolarClawAgentToolsResponseBodyTools()
            self.tools = temp_model.from_map(m.get('Tools'))

        return self

class UpdatePolarClawAgentToolsResponseBodyTools(DaraModel):
    def __init__(
        self,
        allow: List[str] = None,
        also_allow: List[str] = None,
        deny: List[str] = None,
        profile: str = None,
    ):
        # The list of explicitly allowed tools.
        self.allow = allow
        # The list of additionally allowed tools.
        self.also_allow = also_allow
        # The list of denied tools.
        self.deny = deny
        # The tool profile.
        self.profile = profile

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow is not None:
            result['Allow'] = self.allow

        if self.also_allow is not None:
            result['AlsoAllow'] = self.also_allow

        if self.deny is not None:
            result['Deny'] = self.deny

        if self.profile is not None:
            result['Profile'] = self.profile

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Allow') is not None:
            self.allow = m.get('Allow')

        if m.get('AlsoAllow') is not None:
            self.also_allow = m.get('AlsoAllow')

        if m.get('Deny') is not None:
            self.deny = m.get('Deny')

        if m.get('Profile') is not None:
            self.profile = m.get('Profile')

        return self

