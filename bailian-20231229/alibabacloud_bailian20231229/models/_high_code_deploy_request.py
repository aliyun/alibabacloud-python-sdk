# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class HighCodeDeployRequest(DaraModel):
    def __init__(
        self,
        agent_desc: str = None,
        agent_id: str = None,
        agent_name: str = None,
        source_code_name: str = None,
        source_code_oss_url: str = None,
        telemetry_enabled: bool = None,
    ):
        self.agent_desc = agent_desc
        self.agent_id = agent_id
        self.agent_name = agent_name
        self.source_code_name = source_code_name
        self.source_code_oss_url = source_code_oss_url
        self.telemetry_enabled = telemetry_enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_desc is not None:
            result['agentDesc'] = self.agent_desc

        if self.agent_id is not None:
            result['agentId'] = self.agent_id

        if self.agent_name is not None:
            result['agentName'] = self.agent_name

        if self.source_code_name is not None:
            result['sourceCodeName'] = self.source_code_name

        if self.source_code_oss_url is not None:
            result['sourceCodeOssUrl'] = self.source_code_oss_url

        if self.telemetry_enabled is not None:
            result['telemetryEnabled'] = self.telemetry_enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentDesc') is not None:
            self.agent_desc = m.get('agentDesc')

        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        if m.get('agentName') is not None:
            self.agent_name = m.get('agentName')

        if m.get('sourceCodeName') is not None:
            self.source_code_name = m.get('sourceCodeName')

        if m.get('sourceCodeOssUrl') is not None:
            self.source_code_oss_url = m.get('sourceCodeOssUrl')

        if m.get('telemetryEnabled') is not None:
            self.telemetry_enabled = m.get('telemetryEnabled')

        return self

