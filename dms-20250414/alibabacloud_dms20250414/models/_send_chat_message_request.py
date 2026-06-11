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
    ):
        # The agent ID. This parameter is required. You can obtain this ID from the response of the `CreateAgentSession` operation. An agent has a lifecycle, so its ID may change with each request.
        # 
        # This parameter is required.
        self.agent_id = agent_id
        # The DMS unit where your DMS instance is located. This information is used to connect to your DMS instance for database analysis. You can find this value in the DMS console. For users on the Alibaba Cloud China site, you can enter `cn-hangzhou`.
        self.dmsunit = dmsunit
        # The data source information. Optional.
        self.data_source = data_source
        # A list of data sources. Optional.
        self.data_sources = data_sources
        # The content of the message to send to the agent.
        # 
        # This parameter is required.
        self.message = message
        # The message type. The default value is `primary`. Set this parameter to `additional` when responding to a human-in-the-loop question from the agent. Set it to `cancel` to cancel the current session.
        self.message_type = message_type
        # The parent session ID.
        self.parent_session_id = parent_session_id
        # This parameter is required if the `MessageType` is `additional`. It contains the specific question asked by the agent during the human-in-the-loop process.
        self.question = question
        # The quoted content. This parameter is typically used when interacting with the agent.
        self.quoted_message = quoted_message
        # This parameter specifies the agent message to which this message is a response, enabling message deduplication. Set this to the highest checkpoint sequence number you have received. For the first message, use 0.
        self.reply_to = reply_to
        # Session-specific configurations. These apply only if provided in the first `SendMessage` request of the session.
        self.session_config = session_config
        # The session ID. This parameter is required. You can obtain the session ID by calling the `CreateAgentSession` operation.
        # 
        # This parameter is required.
        self.session_id = session_id

    def validate(self):
        if self.data_source:
            self.data_source.validate()
        if self.data_sources:
            for v1 in self.data_sources:
                 if v1:
                    v1.validate()
        if self.session_config:
            self.session_config.validate()

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

        return self

class SendChatMessageRequestSessionConfig(DaraModel):
    def __init__(
        self,
        custom_agent_id: str = None,
        custom_agent_stage: str = None,
        language: str = None,
        mode: str = None,
        report_water_mark: str = None,
    ):
        # This parameter is deprecated. Use the `CustomAgentId` request parameter from the `CreateAgentSession` operation instead.
        self.custom_agent_id = custom_agent_id
        # This parameter is deprecated. Use the `CustomAgentStage` request parameter from the `CreateAgentSession` operation instead.
        self.custom_agent_stage = custom_agent_stage
        # The language of the session. Only Chinese and English are supported. The default value is Chinese. The value must be in uppercase.
        self.language = language
        self.mode = mode
        # A text watermark of up to 64 characters that will be added to generated PDF reports.
        self.report_water_mark = report_water_mark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_agent_id is not None:
            result['CustomAgentId'] = self.custom_agent_id

        if self.custom_agent_stage is not None:
            result['CustomAgentStage'] = self.custom_agent_stage

        if self.language is not None:
            result['Language'] = self.language

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.report_water_mark is not None:
            result['ReportWaterMark'] = self.report_water_mark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomAgentId') is not None:
            self.custom_agent_id = m.get('CustomAgentId')

        if m.get('CustomAgentStage') is not None:
            self.custom_agent_stage = m.get('CustomAgentStage')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('ReportWaterMark') is not None:
            self.report_water_mark = m.get('ReportWaterMark')

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
        region_id: str = None,
        tables: List[str] = None,
    ):
        # This parameter is deprecated. Do not use it.
        self.data_source_id = data_source_id
        # The data source type. Valid values are `remote_data_center` for file analysis and `database` for database analysis.
        self.data_source_type = data_source_type
        # This parameter is deprecated. Do not use it.
        self.database = database
        # The database name.
        self.db_name = db_name
        # The ID of the database in DMS.
        self.dms_database_id = dms_database_id
        # The ID of the instance in DMS.
        self.dms_instance_id = dms_instance_id
        # The database engine type.
        self.engine = engine
        # The file ID.
        self.file_id = file_id
        # This parameter is deprecated. Do not use it.
        self.location = location
        # The region ID.
        self.region_id = region_id
        # A list of table names to analyze.
        self.tables = tables

    def validate(self):
        pass

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

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Tables') is not None:
            self.tables = m.get('Tables')

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
        region_id: str = None,
        tables: List[str] = None,
    ):
        # This parameter is deprecated. Do not use it.
        self.data_source_id = data_source_id
        # The data source type. Valid values are `remote_data_center` for file analysis and `database` for database analysis.
        self.data_source_type = data_source_type
        # This parameter is deprecated. Do not use it.
        self.database = database
        # The database name.
        self.db_name = db_name
        # The ID of the database in DMS.
        self.dms_database_id = dms_database_id
        # The ID of the instance in DMS.
        self.dms_instance_id = dms_instance_id
        # The database engine type.
        self.engine = engine
        # The file ID.
        self.file_id = file_id
        # This parameter is deprecated. Do not use it.
        self.location = location
        # The region ID.
        self.region_id = region_id
        # A list of table names to analyze.
        self.tables = tables

    def validate(self):
        pass

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

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Tables') is not None:
            self.tables = m.get('Tables')

        return self

