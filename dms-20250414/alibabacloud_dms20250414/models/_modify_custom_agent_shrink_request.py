# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyCustomAgentShrinkRequest(DaraModel):
    def __init__(
        self,
        callback_config_shrink: str = None,
        custom_agent_id: str = None,
        dmsunit: str = None,
        data_json: str = None,
        description: str = None,
        execution_config_shrink: str = None,
        instruction: str = None,
        knowledge: str = None,
        knowledge_config_list_shrink: str = None,
        name: str = None,
        schedule_task_config_shrink: str = None,
        text_report_config: str = None,
        web_report_config: str = None,
        workspace_id: str = None,
    ):
        self.callback_config_shrink = callback_config_shrink
        # This parameter is required.
        self.custom_agent_id = custom_agent_id
        self.dmsunit = dmsunit
        self.data_json = data_json
        self.description = description
        self.execution_config_shrink = execution_config_shrink
        self.instruction = instruction
        self.knowledge = knowledge
        self.knowledge_config_list_shrink = knowledge_config_list_shrink
        self.name = name
        self.schedule_task_config_shrink = schedule_task_config_shrink
        self.text_report_config = text_report_config
        self.web_report_config = web_report_config
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.callback_config_shrink is not None:
            result['CallbackConfig'] = self.callback_config_shrink

        if self.custom_agent_id is not None:
            result['CustomAgentId'] = self.custom_agent_id

        if self.dmsunit is not None:
            result['DMSUnit'] = self.dmsunit

        if self.data_json is not None:
            result['DataJson'] = self.data_json

        if self.description is not None:
            result['Description'] = self.description

        if self.execution_config_shrink is not None:
            result['ExecutionConfig'] = self.execution_config_shrink

        if self.instruction is not None:
            result['Instruction'] = self.instruction

        if self.knowledge is not None:
            result['Knowledge'] = self.knowledge

        if self.knowledge_config_list_shrink is not None:
            result['KnowledgeConfigList'] = self.knowledge_config_list_shrink

        if self.name is not None:
            result['Name'] = self.name

        if self.schedule_task_config_shrink is not None:
            result['ScheduleTaskConfig'] = self.schedule_task_config_shrink

        if self.text_report_config is not None:
            result['TextReportConfig'] = self.text_report_config

        if self.web_report_config is not None:
            result['WebReportConfig'] = self.web_report_config

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallbackConfig') is not None:
            self.callback_config_shrink = m.get('CallbackConfig')

        if m.get('CustomAgentId') is not None:
            self.custom_agent_id = m.get('CustomAgentId')

        if m.get('DMSUnit') is not None:
            self.dmsunit = m.get('DMSUnit')

        if m.get('DataJson') is not None:
            self.data_json = m.get('DataJson')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExecutionConfig') is not None:
            self.execution_config_shrink = m.get('ExecutionConfig')

        if m.get('Instruction') is not None:
            self.instruction = m.get('Instruction')

        if m.get('Knowledge') is not None:
            self.knowledge = m.get('Knowledge')

        if m.get('KnowledgeConfigList') is not None:
            self.knowledge_config_list_shrink = m.get('KnowledgeConfigList')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ScheduleTaskConfig') is not None:
            self.schedule_task_config_shrink = m.get('ScheduleTaskConfig')

        if m.get('TextReportConfig') is not None:
            self.text_report_config = m.get('TextReportConfig')

        if m.get('WebReportConfig') is not None:
            self.web_report_config = m.get('WebReportConfig')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

