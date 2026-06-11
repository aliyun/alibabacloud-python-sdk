# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCustomAgentShrinkRequest(DaraModel):
    def __init__(
        self,
        callback_config_shrink: str = None,
        dmsunit: str = None,
        data_json: str = None,
        description: str = None,
        execution_config_shrink: str = None,
        instruction: str = None,
        knowledge: str = None,
        knowledge_config_list_shrink: str = None,
        name: str = None,
        related_session_id: str = None,
        schedule_task_config_shrink: str = None,
        text_report_config: str = None,
        web_report_config: str = None,
        workspace_id: str = None,
    ):
        self.callback_config_shrink = callback_config_shrink
        # The ID of the DMS unit.
        self.dmsunit = dmsunit
        # The data range, specified as a **JSON string**.
        # 
        # - General parameters
        # 
        #   - `tableFlag`: Set to `true` to specify a data range.
        # 
        #   - `scope`: The value must be `personal`.
        # 
        #   - `personal`: Contains the parameters for a file or database.
        # 
        # **File type**: Use the following parameters.
        # 
        # - `DataSourceType`: The value must be `remote_data_center`.
        # 
        # - `FileId`: The ID of the file.
        # 
        # - `Database`: The name of the database returned by the `ListDataCenterTable` operation. This is typically the file name.
        # 
        # - `Tables`: The names of the tables returned by the `ListDataCenterTable` operation.
        # 
        # - `TableIds`: The table IDs returned by the `ListDataCenterTable` operation.
        # 
        # - `RegionId`: The current region.
        # 
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
        # **Database type**: Use the following parameters.
        # 
        # - `DataSourceType`: The value must be `database`.
        # 
        # - `DmsInstanceId`: The ID of the DMS instance returned by the data center API.
        # 
        # - `DmsDatabaseId`: The ID of the DMS database returned by the data center API.
        # 
        # - `FileId`: The instance name. This parameter is deprecated.
        # 
        # - `DbName`: The name of the database returned by the data center API.
        # 
        # - `Database`: The name of the database returned by the data center API.
        # 
        # - `Tables`: The names of the tables returned by the data center API.
        # 
        # - `TableIds`: The table IDs returned by the data center API.
        # 
        # - `Engine`: The database engine. Valid values: `mysql` and `postgresql`.
        # 
        # - `RegionId`: The current region.
        # 
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
        # The instruction for the custom agent.
        # 
        # - Maximum length: 10,000 characters.
        self.instruction = instruction
        # The knowledge for the custom agent.
        # 
        # - Maximum length: 10,000 characters.
        self.knowledge = knowledge
        # A list of external knowledge bases.
        self.knowledge_config_list_shrink = knowledge_config_list_shrink
        # The name of the custom agent.
        self.name = name
        self.related_session_id = related_session_id
        # The configuration for the scheduled task.
        self.schedule_task_config_shrink = schedule_task_config_shrink
        # The formatting requirements for the text report.
        self.text_report_config = text_report_config
        # The formatting requirements for the web report.
        self.web_report_config = web_report_config
        # The ID of the workspace.
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

        if self.related_session_id is not None:
            result['RelatedSessionId'] = self.related_session_id

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

        if m.get('RelatedSessionId') is not None:
            self.related_session_id = m.get('RelatedSessionId')

        if m.get('ScheduleTaskConfig') is not None:
            self.schedule_task_config_shrink = m.get('ScheduleTaskConfig')

        if m.get('TextReportConfig') is not None:
            self.text_report_config = m.get('TextReportConfig')

        if m.get('WebReportConfig') is not None:
            self.web_report_config = m.get('WebReportConfig')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

