# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DownloadAgentSpecViaOssRequest(DaraModel):
    def __init__(
        self,
        agent_spec_version: str = None,
    ):
        # The version number. If not specified, the version corresponding to the latest label is downloaded.
        self.agent_spec_version = agent_spec_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_spec_version is not None:
            result['agentSpecVersion'] = self.agent_spec_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentSpecVersion') is not None:
            self.agent_spec_version = m.get('agentSpecVersion')

        return self

