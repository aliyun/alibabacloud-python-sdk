# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class SendChatMessageRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        dmsunit: str = None,
        data_source: main_models.SendChatMessageRequestDataSource = None,
        data_sources: List[main_models.SendChatMessageRequestDataSources] = None,
        message: str = None,
        message_type: str = None,
        parent_session_id: str = None,
        question: str = None,
        quoted_message: str = None,
        reply_to: str = None,
        session_config: main_models.SendChatMessageRequestSessionConfig = None,
        session_id: str = None,
        task_config: main_models.SendChatMessageRequestTaskConfig = None,
        user_oss_bucket: str = None,
        workspace_id: str = None,
    ):
        # **[Optimized]** This field is now automatically retrieved in the background. You do not need to specify it.
        self.agent_id = agent_id
        # **[Optimized]** This field is now automatically retrieved in the background. You do not need to specify it when calling the API.
        self.dmsunit = dmsunit
        # The data source information. This parameter can be left empty. You can specify only one data source for this parameter. Use the DataSources parameter instead.
        self.data_source = data_source
        # The detailed data source information. This parameter can be left empty.
        self.data_sources = data_sources
        # The content of the message sent to the agent.
        # 
        # This parameter is required.
        self.message = message
        # The message type. Default value: `primary`.  
        # 
        # - In normal interactions with the agent, the message type is `primary`.
        # 
        # - When the message is a response to a human-in-the-loop question from the agent, the type must be `additional`.
        # 
        # - When the message is intended to trigger report generation, the type must be `report`.
        # 
        # - When the message is intended to cancel the current session, the type must be `cancel`.
        self.message_type = message_type
        # The ID of the parent session.
        self.parent_session_id = parent_session_id
        # Required when the message type is `additional`. Specifies the specific question asked by the agent to the user through human-in-the-loop.
        self.question = question
        # The quoted content. This is typically used when interacting with the agent.
        self.quoted_message = quoted_message
        # **Important**
        # 
        # When this message is a reply to an agent message, such as an agent asking for clarification through ASK_HUMAN, `reply_to` must exactly match the checkpoint sequence number carried by that agent message. If this message is not a targeted reply, such as requesting the agent to perform further in-depth analysis after the initial analysis is complete, you can leave `reply_to` empty or set it to "0".  
        # 
        # This field affects how the agent decides to process the message. Passing an incorrect value may lead to suboptimal analysis results.
        self.reply_to = reply_to
        # The special configurations for the current session. For the same session, only the configurations specified in the first SendMessage call take effect.
        self.session_config = session_config
        # The session ID. This optional field is used for multi-turn sessions.
        # - You can start a session without specifying this field. The response will include the session ID for the current session.
        # - You can also manually create a session ID by calling the CreateDataAgentSession operation and include the ID when initiating a session.
        # - If you need multi-turn conversations, such as follow-up questions or confirming execution plans, specify the session ID returned by the previous SendChatMessage operation in this operation.
        self.session_id = session_id
        # The configuration items that affect only the current task.
        self.task_config = task_config
        # The Object Storage Service (OSS) bucket of the user. If this parameter is left empty, the analysis process is securely stored in the built-in storage.
        self.user_oss_bucket = user_oss_bucket
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        if self.data_source:
            self.data_source.validate()
        if self.data_sources:
            for v1 in self.data_sources:
                 if v1:
                    v1.validate()
        if self.session_config:
            self.session_config.validate()
        if self.task_config:
            self.task_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.dmsunit is not None:
            result['DMSUnit'] = self.dmsunit

        if self.data_source is not None:
            result['DataSource'] = self.data_source.to_map()

        result['DataSources'] = []
        if self.data_sources is not None:
            for k1 in self.data_sources:
                result['DataSources'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.message_type is not None:
            result['MessageType'] = self.message_type

        if self.parent_session_id is not None:
            result['ParentSessionId'] = self.parent_session_id

        if self.question is not None:
            result['Question'] = self.question

        if self.quoted_message is not None:
            result['QuotedMessage'] = self.quoted_message

        if self.reply_to is not None:
            result['ReplyTo'] = self.reply_to

        if self.session_config is not None:
            result['SessionConfig'] = self.session_config.to_map()

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.task_config is not None:
            result['TaskConfig'] = self.task_config.to_map()

        if self.user_oss_bucket is not None:
            result['UserOssBucket'] = self.user_oss_bucket

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('DMSUnit') is not None:
            self.dmsunit = m.get('DMSUnit')

        if m.get('DataSource') is not None:
            temp_model = main_models.SendChatMessageRequestDataSource()
            self.data_source = temp_model.from_map(m.get('DataSource'))

        self.data_sources = []
        if m.get('DataSources') is not None:
            for k1 in m.get('DataSources'):
                temp_model = main_models.SendChatMessageRequestDataSources()
                self.data_sources.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')

        if m.get('ParentSessionId') is not None:
            self.parent_session_id = m.get('ParentSessionId')

        if m.get('Question') is not None:
            self.question = m.get('Question')

        if m.get('QuotedMessage') is not None:
            self.quoted_message = m.get('QuotedMessage')

        if m.get('ReplyTo') is not None:
            self.reply_to = m.get('ReplyTo')

        if m.get('SessionConfig') is not None:
            temp_model = main_models.SendChatMessageRequestSessionConfig()
            self.session_config = temp_model.from_map(m.get('SessionConfig'))

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('TaskConfig') is not None:
            temp_model = main_models.SendChatMessageRequestTaskConfig()
            self.task_config = temp_model.from_map(m.get('TaskConfig'))

        if m.get('UserOssBucket') is not None:
            self.user_oss_bucket = m.get('UserOssBucket')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class SendChatMessageRequestTaskConfig(DaraModel):
    def __init__(
        self,
        report_config: main_models.SendChatMessageRequestTaskConfigReportConfig = None,
    ):
        # The configuration of the report rules. A report task is executed based on this configuration only when MessageType is set to REPORT.
        self.report_config = report_config

    def validate(self):
        if self.report_config:
            self.report_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.report_config is not None:
            result['ReportConfig'] = self.report_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReportConfig') is not None:
            temp_model = main_models.SendChatMessageRequestTaskConfigReportConfig()
            self.report_config = temp_model.from_map(m.get('ReportConfig'))

        return self

class SendChatMessageRequestTaskConfigReportConfig(DaraModel):
    def __init__(
        self,
        report_prompt: str = None,
        report_theme: str = None,
        report_type: str = None,
    ):
        # The prompt that must be followed for the current report.
        self.report_prompt = report_prompt
        # The report theme. Valid values: default, journal, legacy, and neobrutalism.
        self.report_theme = report_theme
        # The service type. Valid values: TextReport and WebReport, which indicate that the current task generates a text report or a web report, respectively. Only WebReport is supported.
        self.report_type = report_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.report_prompt is not None:
            result['ReportPrompt'] = self.report_prompt

        if self.report_theme is not None:
            result['ReportTheme'] = self.report_theme

        if self.report_type is not None:
            result['ReportType'] = self.report_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReportPrompt') is not None:
            self.report_prompt = m.get('ReportPrompt')

        if m.get('ReportTheme') is not None:
            self.report_theme = m.get('ReportTheme')

        if m.get('ReportType') is not None:
            self.report_type = m.get('ReportType')

        return self

class SendChatMessageRequestSessionConfig(DaraModel):
    def __init__(
        self,
        custom_agent_id: str = None,
        custom_agent_stage: str = None,
        enable_search: bool = None,
        kb_uuid_list: List[str] = None,
        language: str = None,
        mcp_server_ids: List[str] = None,
        mode: str = None,
        permission_config: main_models.SendChatMessageRequestSessionConfigPermissionConfig = None,
        plan_mode: str = None,
        report_water_mark: str = None,
        skip_ask_human: bool = None,
        skip_plan: bool = None,
        skip_sql_confirm: bool = None,
        skip_web_report_confirm: bool = None,
        user_specified_skill_list: List[str] = None,
    ):
        # The ID of the custom agent. A custom agent is an entity used to customize the analysis process. You can create a custom agent in the DataAgent console or by calling the CreateCustomAgent operation. The ID of a custom agent must start with `ca-`.
        self.custom_agent_id = custom_agent_id
        # The stage of the custom agent.
        self.custom_agent_stage = custom_agent_stage
        # Specifies whether to enable web search.
        self.enable_search = enable_search
        # The list of knowledge base IDs.
        self.kb_uuid_list = kb_uuid_list
        # The language. Only Chinese and English are supported. The default value is Chinese. Only uppercase letters are supported.
        self.language = language
        # The MCP server IDs in the session configuration.
        self.mcp_server_ids = mcp_server_ids
        # The mode. Valid values:
        #  - **ASK_DATA**: the data query mode.
        #  - **ANALYSIS**: the analysis mode.
        #  - **INSIGHT**: the insight mode.
        self.mode = mode
        # The data permission settings at the session level. If you configure this parameter multiple times in multi-turn conversations within the same session, the last configuration prevails.
        self.permission_config = permission_config
        # Specifies whether to enable the plan feature. Valid values: `disable`, `enable`, and `force`. Default value: `enable`.
        self.plan_mode = plan_mode
        # The watermark text. You can enter up to 64 characters. The text is used to add a watermark to the generated PDF report.
        self.report_water_mark = report_water_mark
        # Specifies whether to disable user inquiries during the process.
        self.skip_ask_human = skip_ask_human
        # Specifies whether to skip the plan confirmation step.
        self.skip_plan = skip_plan
        # Specifies whether to skip all SQL confirmations.
        self.skip_sql_confirm = skip_sql_confirm
        # Specifies whether to skip the web report generation confirmation.
        self.skip_web_report_confirm = skip_web_report_confirm
        # The list of user-specified skills.
        self.user_specified_skill_list = user_specified_skill_list

    def validate(self):
        if self.permission_config:
            self.permission_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_agent_id is not None:
            result['CustomAgentId'] = self.custom_agent_id

        if self.custom_agent_stage is not None:
            result['CustomAgentStage'] = self.custom_agent_stage

        if self.enable_search is not None:
            result['EnableSearch'] = self.enable_search

        if self.kb_uuid_list is not None:
            result['KbUuidList'] = self.kb_uuid_list

        if self.language is not None:
            result['Language'] = self.language

        if self.mcp_server_ids is not None:
            result['McpServerIds'] = self.mcp_server_ids

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.permission_config is not None:
            result['PermissionConfig'] = self.permission_config.to_map()

        if self.plan_mode is not None:
            result['PlanMode'] = self.plan_mode

        if self.report_water_mark is not None:
            result['ReportWaterMark'] = self.report_water_mark

        if self.skip_ask_human is not None:
            result['SkipAskHuman'] = self.skip_ask_human

        if self.skip_plan is not None:
            result['SkipPlan'] = self.skip_plan

        if self.skip_sql_confirm is not None:
            result['SkipSqlConfirm'] = self.skip_sql_confirm

        if self.skip_web_report_confirm is not None:
            result['SkipWebReportConfirm'] = self.skip_web_report_confirm

        if self.user_specified_skill_list is not None:
            result['UserSpecifiedSkillList'] = self.user_specified_skill_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomAgentId') is not None:
            self.custom_agent_id = m.get('CustomAgentId')

        if m.get('CustomAgentStage') is not None:
            self.custom_agent_stage = m.get('CustomAgentStage')

        if m.get('EnableSearch') is not None:
            self.enable_search = m.get('EnableSearch')

        if m.get('KbUuidList') is not None:
            self.kb_uuid_list = m.get('KbUuidList')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('McpServerIds') is not None:
            self.mcp_server_ids = m.get('McpServerIds')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('PermissionConfig') is not None:
            temp_model = main_models.SendChatMessageRequestSessionConfigPermissionConfig()
            self.permission_config = temp_model.from_map(m.get('PermissionConfig'))

        if m.get('PlanMode') is not None:
            self.plan_mode = m.get('PlanMode')

        if m.get('ReportWaterMark') is not None:
            self.report_water_mark = m.get('ReportWaterMark')

        if m.get('SkipAskHuman') is not None:
            self.skip_ask_human = m.get('SkipAskHuman')

        if m.get('SkipPlan') is not None:
            self.skip_plan = m.get('SkipPlan')

        if m.get('SkipSqlConfirm') is not None:
            self.skip_sql_confirm = m.get('SkipSqlConfirm')

        if m.get('SkipWebReportConfirm') is not None:
            self.skip_web_report_confirm = m.get('SkipWebReportConfirm')

        if m.get('UserSpecifiedSkillList') is not None:
            self.user_specified_skill_list = m.get('UserSpecifiedSkillList')

        return self

class SendChatMessageRequestSessionConfigPermissionConfig(DaraModel):
    def __init__(
        self,
        default_action: str = None,
    ):
        # The default behavior for table-level permissions. This parameter controls whether tables that are not configured in DataSources.[item].Permission can be queried. Valid values: `allow` and `deny`.
        # 
        # - `allow`: the default value. This value indicates that the blacklist mode is used. By default, all tables can be queried, and the actual permissions are subject to the permissions configured in DMS. Only when you configure **row-level and column-level** permissions in DataSources.[item].Permission, the row-level and column-level permissions are used for access control.
        # 
        # - `deny`: This value indicates that the whitelist mode is used. You must manually specify this value. By default, no tables can be queried. A table can be queried only when you configure permissions for the table in DataSources.[item].Permission. You can grant full access to a table by not configuring any row-level or column-level restrictions.
        self.default_action = default_action

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_action is not None:
            result['DefaultAction'] = self.default_action

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultAction') is not None:
            self.default_action = m.get('DefaultAction')

        return self

class SendChatMessageRequestDataSources(DaraModel):
    def __init__(
        self,
        data_source_id: str = None,
        data_source_type: str = None,
        database: str = None,
        db_name: str = None,
        dms_database_id: str = None,
        dms_instance_id: str = None,
        engine: str = None,
        file_id: str = None,
        location: str = None,
        permission: main_models.SendChatMessageRequestDataSourcesPermission = None,
        region_id: str = None,
        tables: List[str] = None,
        uri: str = None,
    ):
        # **[Deprecated]** You do not need to specify this field.
        self.data_source_id = data_source_id
        # The data source type. Valid values: remote_data_center and database, which indicate that the analysis is based on a file or a database, respectively.
        self.data_source_type = data_source_type
        # **[Deprecated]** You do not need to specify this field.
        self.database = database
        # The name of the database.
        self.db_name = db_name
        # The ID of the database in Data Management (DMS).
        self.dms_database_id = dms_database_id
        # The ID of the instance in DMS.
        self.dms_instance_id = dms_instance_id
        # The database engine type.
        self.engine = engine
        # The file ID.
        self.file_id = file_id
        # **[Deprecated]** You do not need to specify this field.
        self.location = location
        # The permission constraints for querying the current data source. The permission constraint feature is in canary release. This field does not take effect for users outside the canary release scope.
        self.permission = permission
        # The region ID.
        self.region_id = region_id
        # The list of names of the tables to be analyzed.
        self.tables = tables
        # The data source resource identifier.
        self.uri = uri

    def validate(self):
        if self.permission:
            self.permission.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type

        if self.database is not None:
            result['Database'] = self.database

        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.dms_database_id is not None:
            result['DmsDatabaseId'] = self.dms_database_id

        if self.dms_instance_id is not None:
            result['DmsInstanceId'] = self.dms_instance_id

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.location is not None:
            result['Location'] = self.location

        if self.permission is not None:
            result['Permission'] = self.permission.to_map()

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.tables is not None:
            result['Tables'] = self.tables

        if self.uri is not None:
            result['Uri'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')

        if m.get('Database') is not None:
            self.database = m.get('Database')

        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('DmsDatabaseId') is not None:
            self.dms_database_id = m.get('DmsDatabaseId')

        if m.get('DmsInstanceId') is not None:
            self.dms_instance_id = m.get('DmsInstanceId')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        if m.get('Permission') is not None:
            temp_model = main_models.SendChatMessageRequestDataSourcesPermission()
            self.permission = temp_model.from_map(m.get('Permission'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Tables') is not None:
            self.tables = m.get('Tables')

        if m.get('Uri') is not None:
            self.uri = m.get('Uri')

        return self

class SendChatMessageRequestDataSourcesPermission(DaraModel):
    def __init__(
        self,
        tables: List[main_models.SendChatMessageRequestDataSourcesPermissionTables] = None,
    ):
        # The table-level permission constraints for querying the current data source. Each item in the list represents the permission constraints for a specific table.
        self.tables = tables

    def validate(self):
        if self.tables:
            for v1 in self.tables:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tables'] = []
        if self.tables is not None:
            for k1 in self.tables:
                result['Tables'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tables = []
        if m.get('Tables') is not None:
            for k1 in m.get('Tables'):
                temp_model = main_models.SendChatMessageRequestDataSourcesPermissionTables()
                self.tables.append(temp_model.from_map(k1))

        return self

class SendChatMessageRequestDataSourcesPermissionTables(DaraModel):
    def __init__(
        self,
        allowed_columns: List[str] = None,
        disallowed_columns: List[str] = None,
        required_row_filter: str = None,
        table_name: str = None,
    ):
        # The list of columns that are allowed to be queried in the current table. If this parameter is left empty, all columns can be queried. If this parameter is specified, SQL statements that query columns beyond the allowed scope, such as SELECT *, are prohibited. To ensure the analysis performance of DataAgent, make sure that the prompts, knowledge, and instructions of DataAgent do not include columns beyond the allowed scope. Otherwise, unauthorized SQL statements may be generated and blocked, which degrades the analysis speed and performance of DataAgent.
        self.allowed_columns = allowed_columns
        # The list of columns that are not allowed to be queried in the current table. If you leave this field empty, all columns **can be queried**. If you specify this field, SQL statements that query columns beyond the allowed scope, such as `SELECT *`, will be blocked.  
        # 
        # If both the disallowed list and the allowed list are configured, the disallowed list takes precedence. For example, if Table 1 has columns A, B, C, and D, and you configure columns A and B as not allowed, while configuring columns B and C as allowed, only column C is ultimately allowed to be queried.
        # 
        # To ensure the analysis performance of DataAgent, make sure that the prompts, knowledge, and instructions modules of DataAgent do not include columns beyond the allowed scope. Otherwise, unauthorized SQL statements may be generated and blocked, which degrades the analysis speed and performance of DataAgent.
        self.disallowed_columns = disallowed_columns
        # The row filter condition that must be included for the current table. If you leave this field empty, it is ignored. If you specify this field, the system checks whether all SQL statements involving this table include the filter column and whether the WHERE clause meets the constraints. SQL statements that do not meet the constraints will be rejected. Pay attention to the format of the validation condition.
        self.required_row_filter = required_row_filter
        # The name of the table to which the permission constraint rules apply.
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allowed_columns is not None:
            result['AllowedColumns'] = self.allowed_columns

        if self.disallowed_columns is not None:
            result['DisallowedColumns'] = self.disallowed_columns

        if self.required_row_filter is not None:
            result['RequiredRowFilter'] = self.required_row_filter

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowedColumns') is not None:
            self.allowed_columns = m.get('AllowedColumns')

        if m.get('DisallowedColumns') is not None:
            self.disallowed_columns = m.get('DisallowedColumns')

        if m.get('RequiredRowFilter') is not None:
            self.required_row_filter = m.get('RequiredRowFilter')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

class SendChatMessageRequestDataSource(DaraModel):
    def __init__(
        self,
        data_source_id: str = None,
        data_source_type: str = None,
        database: str = None,
        db_name: str = None,
        dms_database_id: str = None,
        dms_instance_id: str = None,
        engine: str = None,
        file_id: str = None,
        location: str = None,
        permission: main_models.SendChatMessageRequestDataSourcePermission = None,
        region_id: str = None,
        tables: List[str] = None,
        uri: str = None,
    ):
        # **[Deprecated]** You do not need to specify this field.
        self.data_source_id = data_source_id
        # The data source type. Valid values: `remote_data_center` and `database`. `remote_data_center` indicates a file, and `database` indicates a database.
        self.data_source_type = data_source_type
        # **[Deprecated]** You do not need to specify this field.
        self.database = database
        # The name of the database.
        self.db_name = db_name
        # The ID of the database in Data Management (DMS).
        self.dms_database_id = dms_database_id
        # The ID of the instance in DMS.
        self.dms_instance_id = dms_instance_id
        # The database engine type.
        self.engine = engine
        # The ID of the file.
        self.file_id = file_id
        # **[Deprecated]** You do not need to specify this field.
        self.location = location
        # The permission constraints for querying the current data source. The permission constraint feature is in canary release. This field does not take effect for users outside the canary release scope.
        self.permission = permission
        # The region ID.
        self.region_id = region_id
        # The list of names of the tables to be analyzed.
        self.tables = tables
        # The data source resource identifier.
        self.uri = uri

    def validate(self):
        if self.permission:
            self.permission.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type

        if self.database is not None:
            result['Database'] = self.database

        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.dms_database_id is not None:
            result['DmsDatabaseId'] = self.dms_database_id

        if self.dms_instance_id is not None:
            result['DmsInstanceId'] = self.dms_instance_id

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.location is not None:
            result['Location'] = self.location

        if self.permission is not None:
            result['Permission'] = self.permission.to_map()

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.tables is not None:
            result['Tables'] = self.tables

        if self.uri is not None:
            result['Uri'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')

        if m.get('Database') is not None:
            self.database = m.get('Database')

        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('DmsDatabaseId') is not None:
            self.dms_database_id = m.get('DmsDatabaseId')

        if m.get('DmsInstanceId') is not None:
            self.dms_instance_id = m.get('DmsInstanceId')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        if m.get('Permission') is not None:
            temp_model = main_models.SendChatMessageRequestDataSourcePermission()
            self.permission = temp_model.from_map(m.get('Permission'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Tables') is not None:
            self.tables = m.get('Tables')

        if m.get('Uri') is not None:
            self.uri = m.get('Uri')

        return self

class SendChatMessageRequestDataSourcePermission(DaraModel):
    def __init__(
        self,
        tables: List[main_models.SendChatMessageRequestDataSourcePermissionTables] = None,
    ):
        # The table-level permission constraints for querying the current data source. Each item in the list represents the permission constraints for a specific table.
        self.tables = tables

    def validate(self):
        if self.tables:
            for v1 in self.tables:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tables'] = []
        if self.tables is not None:
            for k1 in self.tables:
                result['Tables'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tables = []
        if m.get('Tables') is not None:
            for k1 in m.get('Tables'):
                temp_model = main_models.SendChatMessageRequestDataSourcePermissionTables()
                self.tables.append(temp_model.from_map(k1))

        return self

class SendChatMessageRequestDataSourcePermissionTables(DaraModel):
    def __init__(
        self,
        allowed_columns: List[str] = None,
        disallowed_columns: List[str] = None,
        required_row_filter: str = None,
        table_name: str = None,
    ):
        # The list of columns that are allowed to be queried in the current table. If you leave this field empty, all columns can be queried. If you specify this field, SQL statements that query columns beyond the allowed scope, such as `SELECT *`, will be blocked. To ensure the analysis performance of DataAgent, make sure that the prompts, knowledge, and instructions modules of DataAgent do not include columns beyond the allowed scope. Otherwise, unauthorized SQL statements may be generated and blocked, which degrades the analysis speed and performance of DataAgent.
        self.allowed_columns = allowed_columns
        # The list of columns that are not allowed to be queried in the current table. If you leave this field empty, all columns **can be queried**. If you specify this field, SQL statements that query columns beyond the allowed scope, such as `SELECT *`, will be blocked.  
        # 
        # If both the disallowed list and the allowed list are configured, the disallowed list takes precedence. For example, if Table 1 has columns A, B, C, and D, and you configure columns A and B as not allowed, while configuring columns B and C as allowed, only column C is ultimately allowed to be queried.
        # 
        # To ensure the analysis performance of DataAgent, make sure that the prompts, knowledge, and instructions modules of DataAgent do not include columns beyond the allowed scope. Otherwise, unauthorized SQL statements may be generated and blocked, which degrades the analysis speed and performance of DataAgent.
        self.disallowed_columns = disallowed_columns
        # The row filter condition that must be included for the current table. If you leave this field empty, it is ignored. If you specify this field, the system checks whether all SQL statements involving this table include the filter column and whether the WHERE clause meets the constraints. SQL statements that do not meet the constraints will be rejected. Pay attention to the format of the validation condition.
        self.required_row_filter = required_row_filter
        # The name of the table to which the permission constraint rules apply.
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allowed_columns is not None:
            result['AllowedColumns'] = self.allowed_columns

        if self.disallowed_columns is not None:
            result['DisallowedColumns'] = self.disallowed_columns

        if self.required_row_filter is not None:
            result['RequiredRowFilter'] = self.required_row_filter

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowedColumns') is not None:
            self.allowed_columns = m.get('AllowedColumns')

        if m.get('DisallowedColumns') is not None:
            self.disallowed_columns = m.get('DisallowedColumns')

        if m.get('RequiredRowFilter') is not None:
            self.required_row_filter = m.get('RequiredRowFilter')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

