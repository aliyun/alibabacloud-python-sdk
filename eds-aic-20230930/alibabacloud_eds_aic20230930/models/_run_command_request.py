# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RunCommandRequest(DaraModel):
    def __init__(
        self,
        agent_type: str = None,
        command_content: str = None,
        content_encoding: str = None,
        instance_ids: List[str] = None,
        timeout: int = None,
    ):
        # The channel type for running the command.
        self.agent_type = agent_type
        # The content of the command.
        self.command_content = command_content
        # The encoding method for the command content (`CommandContent`). This value is not case-sensitive.
        # 
        # > An invalid value defaults to `PlainText`.
        self.content_encoding = content_encoding
        # A list of instance IDs. You can specify up to 50 instances per request.
        self.instance_ids = instance_ids
        # The execution timeout in seconds. The command times out if it does not complete within this period. Defaults to 60 seconds.
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_type is not None:
            result['AgentType'] = self.agent_type

        if self.command_content is not None:
            result['CommandContent'] = self.command_content

        if self.content_encoding is not None:
            result['ContentEncoding'] = self.content_encoding

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentType') is not None:
            self.agent_type = m.get('AgentType')

        if m.get('CommandContent') is not None:
            self.command_content = m.get('CommandContent')

        if m.get('ContentEncoding') is not None:
            self.content_encoding = m.get('ContentEncoding')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        return self

