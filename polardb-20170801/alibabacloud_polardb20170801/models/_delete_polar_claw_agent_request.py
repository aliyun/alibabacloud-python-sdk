# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeletePolarClawAgentRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        application_id: str = None,
        delete_files: bool = None,
    ):
        # The ID of the agent to delete. This parameter cannot be set to `main`.
        # 
        # This parameter is required.
        self.agent_id = agent_id
        # The application ID.
        # 
        # This parameter is required.
        self.application_id = application_id
        # Specifies whether to delete the working directory and session files. Default value: `true`.
        self.delete_files = delete_files

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

        if self.delete_files is not None:
            result['DeleteFiles'] = self.delete_files

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('DeleteFiles') is not None:
            self.delete_files = m.get('DeleteFiles')

        return self

