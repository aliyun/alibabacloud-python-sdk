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
        # **[Optimized]** This field is now automatically obtained by the backend. You do not need to specify this field.
        self.agent_id = agent_id
        # **[Optimized]** This field is now automatically obtained by the backend. You do not need to specify this field when calling the API.
        self.dmsunit = dmsunit
        # The data source information. This parameter can be left empty. This parameter supports only one data source. Use the DataSources parameter instead.
        self.data_source = data_source
        # The detailed data source information. This parameter can be left empty.
        self.data_sources = data_sources
        # The message content to send to the Agent.
        # 
        # This parameter is required.
        self.message = message
        # The message type. Default value: `[primary]`.  
        # 
        # - For regular interactions with the Agent, the message type is `[primary]`.
        # 
        # - When the message is a response to the Agent\\"s Human-in-Loop question, the type should be `[additional]`.
        # 
        # - When the message is intended to trigger a report generation, the type should be `[report]`.
        # 
        # - When the message is intended to cancel the current session, the type should be `[cancel]`.
        self.message_type = message_type
        # The parent session ID.
        self.parent_session_id = parent_session_id
        # This field is required when the message type is `additional`. Specify the specific question that the Agent asks the user through Human-in-Loop.
        self.question = question
        # The quoted content. This is typically used during interactions with the Agent.
        self.quoted_message = quoted_message
        # **Important**
        # 
        # When this message is a reply to an Agent message (for example, the Agent asks a clarification question through ASK_HUMAN), reply_to must be set to the exact Checkpoint sequence number carried in that Agent message. If this message is not a targeted reply, such as requesting the Agent to perform further in-depth analysis after the analysis is complete, reply_to can be left empty or set to "0".  
        # 
        # This field affects how the Agent decides to process the message. Passing an incorrect value may result in analysis results that do not meet expectations.
        self.reply_to = reply_to
        # The special configuration for the current session. For the same session, only the configuration included in the first SendMessage call takes effect.
        self.session_config = session_config
        # The session ID. This is an optional field used for multi-turn conversations.
        # - You can start a conversation without specifying this field. The response includes the SessionID for the current session.
        # - You can also manually create a session ID by calling the CreateDataAgentSession operation and include the ID when initiating a conversation.
        # - If you need multi-turn conversations (such as follow-up questions or confirming execution plans), include the SessionID returned by the previous SendChatMessage call.
        self.session_id = session_id
        # The configuration items that affect only the current task.
        self.task_config = task_config
        # The user\\"s OSS bucket. If this field is left empty, the analysis results are securely stored in the built-in storage.
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
        # The report rule configuration. Only when MessageType is REPORT, a report task is executed based on this configuration.
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
        # The prompt that the report must follow.
        self.report_prompt = report_prompt
        # The report theme. Valid values: default, journal, legacy, neobrutalism.
        self.report_theme = report_theme
        # The service type. Valid values: TextReport, WebReport. These values indicate that the current task generates a text report or a web report. Currently only WebReport is supported.
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
        enable_search: str = None,
        kb_uuid_list: str = None,
        language: str = None,
        mcp_server_ids: str = None,
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
        # The custom Agent ID. A custom Agent is an entity used to customize the analysis process. You can create one in the DataAgent console or by calling the CreateCustomAgent operation. The custom Agent ID is a string that starts with `ca-`.
        self.custom_agent_id = custom_agent_id
        # The stage of the custom Agent.
        self.custom_agent_stage = custom_agent_stage
        # Specifies whether to enable web search.
        self.enable_search = enable_search
        # The list of knowledge base IDs.
        self.kb_uuid_list = kb_uuid_list
        # Currently only Chinese and English are supported. The default value is Chinese. Only uppercase values are supported.
        self.language = language
        # The MCP server IDs in the session configuration.
        self.mcp_server_ids = mcp_server_ids
        # The mode. Valid values:
        #  - **ASK_DATA**: data query mode.
        #  - **ANALYSIS**: analysis mode.
        #  - **INSIGHT**: insight mode.
        self.mode = mode
        # session 级权限生效机制配置，仅含未配置表的默认行为
        self.permission_config = permission_config
        # Specifies whether to enable the plan. Valid values: disable, enable, force. Default value: enable.
        self.plan_mode = plan_mode
        # The text (up to 64 characters) used as a watermark in the generated PDF report.
        self.report_water_mark = report_water_mark
        # Specifies whether to disable user inquiries during the process.
        self.skip_ask_human = skip_ask_human
        # Specifies whether to skip the plan confirmation step.
        self.skip_plan = skip_plan
        # Specifies whether to skip all SQL confirmations.
        self.skip_sql_confirm = skip_sql_confirm
        # Specifies whether to skip the web report generation confirmation.
        self.skip_web_report_confirm = skip_web_report_confirm
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
        # 未配置表的默认行为：allow=放行（默认），deny=拒绝
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
    ):
        # Deprecated. You do not need to specify this field.
        self.data_source_id = data_source_id
        # The data source type. Valid values: remote_data_center, database. These values indicate that the analysis is performed on a file or a database.
        self.data_source_type = data_source_type
        # Deprecated. You do not need to specify this field.
        self.database = database
        # The database name.
        self.db_name = db_name
        # The ID of the database in Data Management.
        self.dms_database_id = dms_database_id
        # The ID of the instance in Data Management.
        self.dms_instance_id = dms_instance_id
        # The database engine type.
        self.engine = engine
        # The file ID.
        self.file_id = file_id
        # Deprecated. You do not need to specify this field.
        self.location = location
        # The permission constraints for querying the current data source. The permission constraint feature is available through a canary release. This field does not take effect for users who are not included in the canary release.
        self.permission = permission
        # The region ID.
        self.region_id = region_id
        # The list of table names to analyze.
        self.tables = tables

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

        return self

class SendChatMessageRequestDataSourcesPermission(DaraModel):
    def __init__(
        self,
        tables: List[main_models.SendChatMessageRequestDataSourcesPermissionTables] = None,
    ):
        # The table-level permission constraints for querying the current data source. Each item in the list represents the permission constraints for a table.
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
        # The list of columns that are allowed to be queried in the current table. If this field is left empty, all columns can be queried. If specified, SQL statements that exceed the allowed scope are blocked. For example, syntax such as SELECT * is blocked. To ensure DataAgent analysis effectiveness, avoid specifying columns beyond the allowed scope in the DataAgent prompts, knowledge, or instructions modules. Otherwise, unauthorized SQL statements may be generated and blocked, which reduces DataAgent analysis speed and effectiveness.
        self.allowed_columns = allowed_columns
        self.disallowed_columns = disallowed_columns
        # The required row filter condition for the current table. If this field is left empty, it is ignored. If specified, all SQL statements involving this table are validated to check whether they include the filter field and whether the WHERE condition meets the constraint. SQL statements that do not meet the constraint are rejected. Ensure the validation condition format is correct.
        self.required_row_filter = required_row_filter
        # The table name to which the permission constraint rule applies.
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
    ):
        # Deprecated. You do not need to specify this field.
        self.data_source_id = data_source_id
        # The data source type. Valid values: `[remote_data_center, database]`, indicating that the analysis is performed on a file or a database.
        self.data_source_type = data_source_type
        # Deprecated. You do not need to specify this field.
        self.database = database
        # The database name.
        self.db_name = db_name
        # The ID of the database in Data Management.
        self.dms_database_id = dms_database_id
        # The ID of the instance in Data Management.
        self.dms_instance_id = dms_instance_id
        # The database engine type.
        self.engine = engine
        # The file ID.
        self.file_id = file_id
        # Deprecated. You do not need to specify this field.
        self.location = location
        # The permission constraints for querying the current data source. The permission constraint feature is available through a canary release. This field does not take effect for users who are not included in the canary release.
        self.permission = permission
        # The region ID.
        self.region_id = region_id
        # The list of table names to analyze.
        self.tables = tables

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

        return self

class SendChatMessageRequestDataSourcePermission(DaraModel):
    def __init__(
        self,
        tables: List[main_models.SendChatMessageRequestDataSourcePermissionTables] = None,
    ):
        # The table-level permission constraints for querying the current data source. Each item in the list represents the permission constraints for a table.
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
        # The list of columns that are allowed to be queried in the current table. If this field is left empty, all columns can be queried. If specified, SQL statements that exceed the allowed scope are blocked. For example, syntax such as SELECT * is blocked. To ensure DataAgent analysis effectiveness, avoid specifying columns beyond the allowed scope in the DataAgent prompts, knowledge, or instructions modules. Otherwise, unauthorized SQL statements may be generated and blocked, which reduces DataAgent analysis speed and effectiveness.
        self.allowed_columns = allowed_columns
        self.disallowed_columns = disallowed_columns
        # The required row filter condition for the current table. If this field is left empty, it is ignored. If specified, all SQL statements involving this table are validated to check whether they include the filter field and whether the WHERE condition meets the constraint. SQL statements that do not meet the constraint are rejected. Ensure the validation condition format is correct.
        self.required_row_filter = required_row_filter
        # The table name to which the permission constraint rule applies.
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

