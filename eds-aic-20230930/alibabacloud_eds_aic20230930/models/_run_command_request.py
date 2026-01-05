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
        self.agent_type = agent_type
        # The content of the command.
        self.command_content = command_content
        # The encoding method of the command content (`CommandContent`). The value is not case-sensitive.
        # 
        # >  If you set the value to an invalid encoding method, the system will process the command content as `PlainText`.
        # 
        # Valid values:
        # 
        # *   Base64: encodes the command content in Base64.
        # *   PlainText (default): does not encode the command content. The command content is input as plain text.
        self.content_encoding = content_encoding
        # The IDs of the cloud phone instances. You can specify a maximum of 50 cloud phone instances.
        self.instance_ids = instance_ids
        # The timeout period of the command execution. If the command execution exceeds the timeout period, it will be considered timed out. If you leave this parameter empty, it defaults to 60.
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

