# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class UpdatePolarClawAgentRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        application_id: str = None,
        avatar: str = None,
        files: List[main_models.UpdatePolarClawAgentRequestFiles] = None,
        model: str = None,
        name: str = None,
        restart: bool = None,
        workspace: str = None,
    ):
        # This parameter is required.
        self.agent_id = agent_id
        # This parameter is required.
        self.application_id = application_id
        self.avatar = avatar
        self.files = files
        self.model = model
        self.name = name
        self.restart = restart
        self.workspace = workspace

    def validate(self):
        if self.files:
            for v1 in self.files:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.avatar is not None:
            result['Avatar'] = self.avatar

        result['Files'] = []
        if self.files is not None:
            for k1 in self.files:
                result['Files'].append(k1.to_map() if k1 else None)

        if self.model is not None:
            result['Model'] = self.model

        if self.name is not None:
            result['Name'] = self.name

        if self.restart is not None:
            result['Restart'] = self.restart

        if self.workspace is not None:
            result['Workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('Avatar') is not None:
            self.avatar = m.get('Avatar')

        self.files = []
        if m.get('Files') is not None:
            for k1 in m.get('Files'):
                temp_model = main_models.UpdatePolarClawAgentRequestFiles()
                self.files.append(temp_model.from_map(k1))

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Restart') is not None:
            self.restart = m.get('Restart')

        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')

        return self

class UpdatePolarClawAgentRequestFiles(DaraModel):
    def __init__(
        self,
        file_content: str = None,
        file_name: str = None,
    ):
        self.file_content = file_content
        self.file_name = file_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_content is not None:
            result['FileContent'] = self.file_content

        if self.file_name is not None:
            result['FileName'] = self.file_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileContent') is not None:
            self.file_content = m.get('FileContent')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        return self

