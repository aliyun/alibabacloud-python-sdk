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
        message: str = None,
        message_type: str = None,
        question: str = None,
        quoted_message: str = None,
        reply_to: str = None,
        session_config: main_models.SendChatMessageRequestSessionConfig = None,
        session_id: str = None,
    ):
        # This parameter is required.
        self.agent_id = agent_id
        self.dmsunit = dmsunit
        self.data_source = data_source
        # This parameter is required.
        self.message = message
        self.message_type = message_type
        self.question = question
        self.quoted_message = quoted_message
        self.reply_to = reply_to
        self.session_config = session_config
        # This parameter is required.
        self.session_id = session_id

    def validate(self):
        if self.data_source:
            self.data_source.validate()
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

        if self.message is not None:
            result['Message'] = self.message

        if self.message_type is not None:
            result['MessageType'] = self.message_type

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

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')

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
        report_water_mark: str = None,
    ):
        self.custom_agent_id = custom_agent_id
        self.custom_agent_stage = custom_agent_stage
        self.language = language
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

        if m.get('ReportWaterMark') is not None:
            self.report_water_mark = m.get('ReportWaterMark')

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
        self.data_source_id = data_source_id
        self.data_source_type = data_source_type
        self.database = database
        self.db_name = db_name
        self.dms_database_id = dms_database_id
        self.dms_instance_id = dms_instance_id
        self.engine = engine
        self.file_id = file_id
        self.location = location
        self.region_id = region_id
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

