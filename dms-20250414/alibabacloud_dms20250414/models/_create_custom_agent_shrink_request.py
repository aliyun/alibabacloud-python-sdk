# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCustomAgentShrinkRequest(DaraModel):
    def __init__(
        self,
        agent_type: str = None,
        callback_config_shrink: str = None,
        dmsunit: str = None,
        data_json: str = None,
        description: str = None,
        execution_config_shrink: str = None,
        instruction: str = None,
        knowledge: str = None,
        knowledge_config_list_shrink: str = None,
        knowledge_semantic_config_list_shrink: str = None,
        name: str = None,
        recommend_question_list_shrink: str = None,
        related_session_id: str = None,
        schedule_task_config_shrink: str = None,
        text_report_config: str = None,
        user_specified_skill_list_shrink: str = None,
        web_report_config: str = None,
        web_report_theme: str = None,
        workspace_id: str = None,
    ):
        # The type of the custom agent. Valid values:
        # - Default: the system-built-in custom agent. Each workspace can have at most one Default agent, and it cannot be deleted.
        # - Common: a regular custom agent.
        self.agent_type = agent_type
        # The callback feature configuration.
        self.callback_config_shrink = callback_config_shrink
        # The current DMS unit.
        self.dmsunit = dmsunit
        # The specified data scope, in **JSON character string format**.
        # - General parameter descriptions
        #   - tableFlag: true specifies the data scope.
        #   - scope: personal is a fixed value.
        #   - personal: the parameters for file and database types.
        # 
        # **File type**: pass parameters in the following format:
        # - DataSourceType: remote_data_center is a fixed value.
        # - FileId: the file ID.
        # - Database: the database name returned by the ListDataCenterTable operation, which is usually the file name.
        # - Tables: the table names returned by the ListDataCenterTable operation.
        # - TableIds: the table IDs returned by the ListDataCenterTable operation.
        # - RegionId: the current region.
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
        # **Database type**: pass parameters in the following format:
        # - DataSourceType: database is a fixed value.
        # - DmsInstanceId: the DMS instance ID returned by the data center API.
        # - DmsDatabaseId: the DMS database ID returned by the data center API.
        # - FileId: the instance name (**[Deprecated]**).
        # - DbName: the database name returned by the data center API.
        # - Database: the database name returned by the data center API.
        # - Tables: the table names returned by the data center API.
        # - TableIds: the table IDs returned by the data center API.
        # - Engine: the database engine type, such as mysql or postgresql.
        # - RegionId: the current region.
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
        self.execution_config_shrink = execution_config_shrink
        # The instructions.
        # - Input limit: up to 10,000 characters.
        self.instruction = instruction
        # The knowledge.
        # - Input limit: up to 10,000 characters.
        self.knowledge = knowledge
        # The external knowledge bases.
        self.knowledge_config_list_shrink = knowledge_config_list_shrink
        # The knowledge semantic configuration list.
        self.knowledge_semantic_config_list_shrink = knowledge_semantic_config_list_shrink
        # The name of the custom agent.
        self.name = name
        # The list of recommended questions.
        # - You can configure up to 10 recommended questions.
        self.recommend_question_list_shrink = recommend_question_list_shrink
        # The ID of the referenced historical session.
        self.related_session_id = related_session_id
        # The scheduled task configuration.
        self.schedule_task_config_shrink = schedule_task_config_shrink
        # The text report format.
        self.text_report_config = text_report_config
        # The list of user-specified skills.
        self.user_specified_skill_list_shrink = user_specified_skill_list_shrink
        # The web report format.
        self.web_report_config = web_report_config
        # The web report theme.
        self.web_report_theme = web_report_theme
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_type is not None:
            result['AgentType'] = self.agent_type

        if self.callback_config_shrink is not None:
            result['CallbackConfig'] = self.callback_config_shrink

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

        if self.knowledge_semantic_config_list_shrink is not None:
            result['KnowledgeSemanticConfigList'] = self.knowledge_semantic_config_list_shrink

        if self.name is not None:
            result['Name'] = self.name

        if self.recommend_question_list_shrink is not None:
            result['RecommendQuestionList'] = self.recommend_question_list_shrink

        if self.related_session_id is not None:
            result['RelatedSessionId'] = self.related_session_id

        if self.schedule_task_config_shrink is not None:
            result['ScheduleTaskConfig'] = self.schedule_task_config_shrink

        if self.text_report_config is not None:
            result['TextReportConfig'] = self.text_report_config

        if self.user_specified_skill_list_shrink is not None:
            result['UserSpecifiedSkillList'] = self.user_specified_skill_list_shrink

        if self.web_report_config is not None:
            result['WebReportConfig'] = self.web_report_config

        if self.web_report_theme is not None:
            result['WebReportTheme'] = self.web_report_theme

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentType') is not None:
            self.agent_type = m.get('AgentType')

        if m.get('CallbackConfig') is not None:
            self.callback_config_shrink = m.get('CallbackConfig')

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

        if m.get('KnowledgeSemanticConfigList') is not None:
            self.knowledge_semantic_config_list_shrink = m.get('KnowledgeSemanticConfigList')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RecommendQuestionList') is not None:
            self.recommend_question_list_shrink = m.get('RecommendQuestionList')

        if m.get('RelatedSessionId') is not None:
            self.related_session_id = m.get('RelatedSessionId')

        if m.get('ScheduleTaskConfig') is not None:
            self.schedule_task_config_shrink = m.get('ScheduleTaskConfig')

        if m.get('TextReportConfig') is not None:
            self.text_report_config = m.get('TextReportConfig')

        if m.get('UserSpecifiedSkillList') is not None:
            self.user_specified_skill_list_shrink = m.get('UserSpecifiedSkillList')

        if m.get('WebReportConfig') is not None:
            self.web_report_config = m.get('WebReportConfig')

        if m.get('WebReportTheme') is not None:
            self.web_report_theme = m.get('WebReportTheme')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

