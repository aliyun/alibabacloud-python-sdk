# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class SubmitDeepWriteTaskRequest(DaraModel):
    def __init__(
        self,
        agent_orchestration: main_models.SubmitDeepWriteTaskRequestAgentOrchestration = None,
        files: List[main_models.SubmitDeepWriteTaskRequestFiles] = None,
        input: str = None,
        instructions: str = None,
        workspace_id: str = None,
    ):
        self.agent_orchestration = agent_orchestration
        self.files = files
        # This parameter is required.
        self.input = input
        self.instructions = instructions
        self.workspace_id = workspace_id

    def validate(self):
        if self.agent_orchestration:
            self.agent_orchestration.validate()
        if self.files:
            for v1 in self.files:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_orchestration is not None:
            result['AgentOrchestration'] = self.agent_orchestration.to_map()

        result['Files'] = []
        if self.files is not None:
            for k1 in self.files:
                result['Files'].append(k1.to_map() if k1 else None)

        if self.input is not None:
            result['Input'] = self.input

        if self.instructions is not None:
            result['Instructions'] = self.instructions

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentOrchestration') is not None:
            temp_model = main_models.SubmitDeepWriteTaskRequestAgentOrchestration()
            self.agent_orchestration = temp_model.from_map(m.get('AgentOrchestration'))

        self.files = []
        if m.get('Files') is not None:
            for k1 in m.get('Files'):
                temp_model = main_models.SubmitDeepWriteTaskRequestFiles()
                self.files.append(temp_model.from_map(k1))

        if m.get('Input') is not None:
            self.input = m.get('Input')

        if m.get('Instructions') is not None:
            self.instructions = m.get('Instructions')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class SubmitDeepWriteTaskRequestFiles(DaraModel):
    def __init__(
        self,
        file_description: str = None,
        file_key: str = None,
        file_name: str = None,
    ):
        self.file_description = file_description
        self.file_key = file_key
        self.file_name = file_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_description is not None:
            result['FileDescription'] = self.file_description

        if self.file_key is not None:
            result['FileKey'] = self.file_key

        if self.file_name is not None:
            result['FileName'] = self.file_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileDescription') is not None:
            self.file_description = m.get('FileDescription')

        if m.get('FileKey') is not None:
            self.file_key = m.get('FileKey')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        return self

class SubmitDeepWriteTaskRequestAgentOrchestration(DaraModel):
    def __init__(
        self,
        data_analyst_agent: main_models.SubmitDeepWriteTaskRequestAgentOrchestrationDataAnalystAgent = None,
        data_collector_agent: main_models.SubmitDeepWriteTaskRequestAgentOrchestrationDataCollectorAgent = None,
        reporter_agent: main_models.SubmitDeepWriteTaskRequestAgentOrchestrationReporterAgent = None,
    ):
        self.data_analyst_agent = data_analyst_agent
        self.data_collector_agent = data_collector_agent
        self.reporter_agent = reporter_agent

    def validate(self):
        if self.data_analyst_agent:
            self.data_analyst_agent.validate()
        if self.data_collector_agent:
            self.data_collector_agent.validate()
        if self.reporter_agent:
            self.reporter_agent.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_analyst_agent is not None:
            result['DataAnalystAgent'] = self.data_analyst_agent.to_map()

        if self.data_collector_agent is not None:
            result['DataCollectorAgent'] = self.data_collector_agent.to_map()

        if self.reporter_agent is not None:
            result['ReporterAgent'] = self.reporter_agent.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataAnalystAgent') is not None:
            temp_model = main_models.SubmitDeepWriteTaskRequestAgentOrchestrationDataAnalystAgent()
            self.data_analyst_agent = temp_model.from_map(m.get('DataAnalystAgent'))

        if m.get('DataCollectorAgent') is not None:
            temp_model = main_models.SubmitDeepWriteTaskRequestAgentOrchestrationDataCollectorAgent()
            self.data_collector_agent = temp_model.from_map(m.get('DataCollectorAgent'))

        if m.get('ReporterAgent') is not None:
            temp_model = main_models.SubmitDeepWriteTaskRequestAgentOrchestrationReporterAgent()
            self.reporter_agent = temp_model.from_map(m.get('ReporterAgent'))

        return self

class SubmitDeepWriteTaskRequestAgentOrchestrationReporterAgent(DaraModel):
    def __init__(
        self,
        enable_citation: bool = None,
        name: str = None,
    ):
        self.enable_citation = enable_citation
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_citation is not None:
            result['EnableCitation'] = self.enable_citation

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableCitation') is not None:
            self.enable_citation = m.get('EnableCitation')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class SubmitDeepWriteTaskRequestAgentOrchestrationDataCollectorAgent(DaraModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class SubmitDeepWriteTaskRequestAgentOrchestrationDataAnalystAgent(DaraModel):
    def __init__(
        self,
        enable_search: bool = None,
        name: str = None,
    ):
        self.enable_search = enable_search
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_search is not None:
            result['EnableSearch'] = self.enable_search

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableSearch') is not None:
            self.enable_search = m.get('EnableSearch')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

