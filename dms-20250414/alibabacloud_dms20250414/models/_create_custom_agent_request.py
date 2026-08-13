# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class CreateCustomAgentRequest(DaraModel):
    def __init__(
        self,
        callback_config: main_models.CreateCustomAgentRequestCallbackConfig = None,
        dmsunit: str = None,
        data_json: str = None,
        description: str = None,
        execution_config: main_models.CreateCustomAgentRequestExecutionConfig = None,
        instruction: str = None,
        knowledge: str = None,
        knowledge_config_list: List[main_models.CreateCustomAgentRequestKnowledgeConfigList] = None,
        knowledge_semantic_config_list: List[main_models.CreateCustomAgentRequestKnowledgeSemanticConfigList] = None,
        name: str = None,
        related_session_id: str = None,
        schedule_task_config: main_models.CreateCustomAgentRequestScheduleTaskConfig = None,
        text_report_config: str = None,
        web_report_config: str = None,
        web_report_theme: str = None,
        workspace_id: str = None,
    ):
        self.callback_config = callback_config
        # The current DMS unit.
        self.dmsunit = dmsunit
        # The specified data range in **JSON string format**.
        # - Common parameter description
        #   - tableFlag: true indicates a specified data range.
        #   - scope: personal is a fixed value.
        #   - personal: pass parameters for file or database types.
        # 
        # **File type**. Pass parameters in the following format:
        # - DataSourceType: remote_data_center is a fixed value.
        # - FileId: The file ID.
        # - Database: The database name returned by the ListDataCenterTable operation, which is usually the file name.
        # - Tables: The table name returned by the ListDataCenterTable operation.
        # - TableIds: The TableId returned by the ListDataCenterTable operation.
        # - RegionId: The current region.
        # ```
        # {
        #   "tableFlag": true,
        #   "scope": "personal",
        #   "personal": {
        #     "DataSourceType": "remote_data_center",
        #     "FileId": "f-f0jksn001ibmkoo********6v2zn6",
        #     "Database": "diamonds.csv",
        #     "Tables": [
        #       "diamonds"
        #     ],
        #     "TableIds": [
        #       "35hfn94pxl********50pi"
        #     ],
        #     "RegionId": "cn-hangzhou"
        #   }
        # }
        # ```
        # 
        # **Database type**. Pass parameters as follows:
        # - DataSourceType: database is a fixed value.
        # - DmsInstanceId: The DMS instance ID returned by the data center operation.
        # - DmsDatabaseId: The DMS database ID returned by the data center operation.
        # - FileId: The instance name (deprecated).
        # - DbName: The database name returned by the data center operation.
        # - Database: The database name returned by the data center operation.
        # - Tables: The table name returned by the data center operation.
        # - TableIds: The TableId returned by the data center operation.
        # - Engine: The engine type (mysql or postgresql).
        # - RegionId: The current region.
        # ```
        # {
        #   "tableFlag": true,
        #   "scope": "personal",
        #   "personal": {
        #     "DataSourceType": "database",
        #     "DmsInstanceId": "284***8",
        #     "DmsDatabaseId": "769***45",
        #     "FileId": "pgm-bp15095e*******6t",
        #     "DbName": "pg_catalog",
        #     "Database": "pg_catalog",
        #     "Tables": [
        #       "pg_aggregate"
        #     ],
        #     "TableIds": [
        #       "5263****31"
        #     ],
        #     "Engine": "postgresql",
        #     "RegionId": "cn-hangzhou"
        #   }
        # }
        # ```
        self.data_json = data_json
        # The description of the custom agent.
        self.description = description
        # The execution configuration.
        self.execution_config = execution_config
        # The instruction.
        self.instruction = instruction
        # The knowledge.
        self.knowledge = knowledge
        # The external knowledge base configurations.
        self.knowledge_config_list = knowledge_config_list
        self.knowledge_semantic_config_list = knowledge_semantic_config_list
        # The name of the custom agent.
        self.name = name
        # The ID of the referenced historical session.
        self.related_session_id = related_session_id
        # The scheduled task configuration.
        self.schedule_task_config = schedule_task_config
        # The text report format.
        self.text_report_config = text_report_config
        # The web report format.
        self.web_report_config = web_report_config
        self.web_report_theme = web_report_theme
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        if self.callback_config:
            self.callback_config.validate()
        if self.execution_config:
            self.execution_config.validate()
        if self.knowledge_config_list:
            for v1 in self.knowledge_config_list:
                 if v1:
                    v1.validate()
        if self.knowledge_semantic_config_list:
            for v1 in self.knowledge_semantic_config_list:
                 if v1:
                    v1.validate()
        if self.schedule_task_config:
            self.schedule_task_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.callback_config is not None:
            result['CallbackConfig'] = self.callback_config.to_map()

        if self.dmsunit is not None:
            result['DMSUnit'] = self.dmsunit

        if self.data_json is not None:
            result['DataJson'] = self.data_json

        if self.description is not None:
            result['Description'] = self.description

        if self.execution_config is not None:
            result['ExecutionConfig'] = self.execution_config.to_map()

        if self.instruction is not None:
            result['Instruction'] = self.instruction

        if self.knowledge is not None:
            result['Knowledge'] = self.knowledge

        result['KnowledgeConfigList'] = []
        if self.knowledge_config_list is not None:
            for k1 in self.knowledge_config_list:
                result['KnowledgeConfigList'].append(k1.to_map() if k1 else None)

        result['KnowledgeSemanticConfigList'] = []
        if self.knowledge_semantic_config_list is not None:
            for k1 in self.knowledge_semantic_config_list:
                result['KnowledgeSemanticConfigList'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        if self.related_session_id is not None:
            result['RelatedSessionId'] = self.related_session_id

        if self.schedule_task_config is not None:
            result['ScheduleTaskConfig'] = self.schedule_task_config.to_map()

        if self.text_report_config is not None:
            result['TextReportConfig'] = self.text_report_config

        if self.web_report_config is not None:
            result['WebReportConfig'] = self.web_report_config

        if self.web_report_theme is not None:
            result['WebReportTheme'] = self.web_report_theme

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallbackConfig') is not None:
            temp_model = main_models.CreateCustomAgentRequestCallbackConfig()
            self.callback_config = temp_model.from_map(m.get('CallbackConfig'))

        if m.get('DMSUnit') is not None:
            self.dmsunit = m.get('DMSUnit')

        if m.get('DataJson') is not None:
            self.data_json = m.get('DataJson')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExecutionConfig') is not None:
            temp_model = main_models.CreateCustomAgentRequestExecutionConfig()
            self.execution_config = temp_model.from_map(m.get('ExecutionConfig'))

        if m.get('Instruction') is not None:
            self.instruction = m.get('Instruction')

        if m.get('Knowledge') is not None:
            self.knowledge = m.get('Knowledge')

        self.knowledge_config_list = []
        if m.get('KnowledgeConfigList') is not None:
            for k1 in m.get('KnowledgeConfigList'):
                temp_model = main_models.CreateCustomAgentRequestKnowledgeConfigList()
                self.knowledge_config_list.append(temp_model.from_map(k1))

        self.knowledge_semantic_config_list = []
        if m.get('KnowledgeSemanticConfigList') is not None:
            for k1 in m.get('KnowledgeSemanticConfigList'):
                temp_model = main_models.CreateCustomAgentRequestKnowledgeSemanticConfigList()
                self.knowledge_semantic_config_list.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RelatedSessionId') is not None:
            self.related_session_id = m.get('RelatedSessionId')

        if m.get('ScheduleTaskConfig') is not None:
            temp_model = main_models.CreateCustomAgentRequestScheduleTaskConfig()
            self.schedule_task_config = temp_model.from_map(m.get('ScheduleTaskConfig'))

        if m.get('TextReportConfig') is not None:
            self.text_report_config = m.get('TextReportConfig')

        if m.get('WebReportConfig') is not None:
            self.web_report_config = m.get('WebReportConfig')

        if m.get('WebReportTheme') is not None:
            self.web_report_theme = m.get('WebReportTheme')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class CreateCustomAgentRequestScheduleTaskConfig(DaraModel):
    def __init__(
        self,
        cron_expression: str = None,
        query: str = None,
        related_session_id: str = None,
    ):
        # The cron expression for time-based scheduling.
        self.cron_expression = cron_expression
        # The query for the scheduled task.
        self.query = query
        # The ID of the referenced historical session.
        self.related_session_id = related_session_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression

        if self.query is not None:
            result['Query'] = self.query

        if self.related_session_id is not None:
            result['RelatedSessionId'] = self.related_session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('RelatedSessionId') is not None:
            self.related_session_id = m.get('RelatedSessionId')

        return self

class CreateCustomAgentRequestKnowledgeSemanticConfigList(DaraModel):
    def __init__(
        self,
        db_id: str = None,
        instance_id: str = None,
        knowledge_uuid: str = None,
        type: str = None,
    ):
        self.db_id = db_id
        self.instance_id = instance_id
        self.knowledge_uuid = knowledge_uuid
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.knowledge_uuid is not None:
            result['KnowledgeUuid'] = self.knowledge_uuid

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('KnowledgeUuid') is not None:
            self.knowledge_uuid = m.get('KnowledgeUuid')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class CreateCustomAgentRequestKnowledgeConfigList(DaraModel):
    def __init__(
        self,
        access_type: str = None,
        kb_uuid: str = None,
        mcp_server_id: str = None,
    ):
        # The access type.
        self.access_type = access_type
        self.kb_uuid = kb_uuid
        # The ID of the MCP Server.
        self.mcp_server_id = mcp_server_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_type is not None:
            result['AccessType'] = self.access_type

        if self.kb_uuid is not None:
            result['KbUuid'] = self.kb_uuid

        if self.mcp_server_id is not None:
            result['McpServerId'] = self.mcp_server_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')

        if m.get('KbUuid') is not None:
            self.kb_uuid = m.get('KbUuid')

        if m.get('McpServerId') is not None:
            self.mcp_server_id = m.get('McpServerId')

        return self

class CreateCustomAgentRequestExecutionConfig(DaraModel):
    def __init__(
        self,
        forbidden_append_data_source: bool = None,
        skip_ask_human: bool = None,
        skip_plan: bool = None,
        skip_sql_confirm: bool = None,
        skip_web_report_confirm: bool = None,
    ):
        self.forbidden_append_data_source = forbidden_append_data_source
        # Specifies whether to disable user inquiries during the process.
        self.skip_ask_human = skip_ask_human
        # Specifies whether to skip the plan confirmation step.
        self.skip_plan = skip_plan
        # Specifies whether to skip all SQL confirmations.
        self.skip_sql_confirm = skip_sql_confirm
        # Specifies whether to skip the web report rendering confirmation.
        self.skip_web_report_confirm = skip_web_report_confirm

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.forbidden_append_data_source is not None:
            result['ForbiddenAppendDataSource'] = self.forbidden_append_data_source

        if self.skip_ask_human is not None:
            result['SkipAskHuman'] = self.skip_ask_human

        if self.skip_plan is not None:
            result['SkipPlan'] = self.skip_plan

        if self.skip_sql_confirm is not None:
            result['SkipSqlConfirm'] = self.skip_sql_confirm

        if self.skip_web_report_confirm is not None:
            result['SkipWebReportConfirm'] = self.skip_web_report_confirm

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForbiddenAppendDataSource') is not None:
            self.forbidden_append_data_source = m.get('ForbiddenAppendDataSource')

        if m.get('SkipAskHuman') is not None:
            self.skip_ask_human = m.get('SkipAskHuman')

        if m.get('SkipPlan') is not None:
            self.skip_plan = m.get('SkipPlan')

        if m.get('SkipSqlConfirm') is not None:
            self.skip_sql_confirm = m.get('SkipSqlConfirm')

        if m.get('SkipWebReportConfirm') is not None:
            self.skip_web_report_confirm = m.get('SkipWebReportConfirm')

        return self

class CreateCustomAgentRequestCallbackConfig(DaraModel):
    def __init__(
        self,
        callback_args: str = None,
        callback_prompt: str = None,
        callback_time: int = None,
        tool_id: str = None,
        type: str = None,
    ):
        self.callback_args = callback_args
        self.callback_prompt = callback_prompt
        self.callback_time = callback_time
        self.tool_id = tool_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.callback_args is not None:
            result['CallbackArgs'] = self.callback_args

        if self.callback_prompt is not None:
            result['CallbackPrompt'] = self.callback_prompt

        if self.callback_time is not None:
            result['CallbackTime'] = self.callback_time

        if self.tool_id is not None:
            result['ToolId'] = self.tool_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallbackArgs') is not None:
            self.callback_args = m.get('CallbackArgs')

        if m.get('CallbackPrompt') is not None:
            self.callback_prompt = m.get('CallbackPrompt')

        if m.get('CallbackTime') is not None:
            self.callback_time = m.get('CallbackTime')

        if m.get('ToolId') is not None:
            self.tool_id = m.get('ToolId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

