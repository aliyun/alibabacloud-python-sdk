# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class DescribeDataAgentSessionResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeDataAgentSessionResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response struct.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message returned if the call failed.
        self.error_message = error_message
        # Id of the request
        self.request_id = request_id
        # The return value. Valid values:
        # 
        # - **true**: Succeeded.
        # - **false**: Failed.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeDataAgentSessionResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeDataAgentSessionResponseBodyData(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        agent_status: str = None,
        artifacts: List[main_models.DescribeDataAgentSessionResponseBodyDataArtifacts] = None,
        chat_history_locations: List[main_models.DescribeDataAgentSessionResponseBodyDataChatHistoryLocations] = None,
        create_time: int = None,
        data_sources: List[main_models.DescribeDataAgentSessionResponseBodyDataDataSources] = None,
        favorite_in_workspace: str = None,
        file: str = None,
        recall_results: List[main_models.DescribeDataAgentSessionResponseBodyDataRecallResults] = None,
        saved: bool = None,
        session_config: main_models.DescribeDataAgentSessionResponseBodyDataSessionConfig = None,
        session_id: str = None,
        session_status: str = None,
        title: str = None,
        user_id: str = None,
    ):
        # The current agent ID.
        self.agent_id = agent_id
        # The current agent status.
        self.agent_status = agent_status
        self.artifacts = artifacts
        # The chat replay history.
        self.chat_history_locations = chat_history_locations
        # The session creation time.
        self.create_time = create_time
        self.data_sources = data_sources
        # Indicates whether the session is saved as a favorite in the workspace by the current logged-in user.
        self.favorite_in_workspace = favorite_in_workspace
        # The file ID.
        self.file = file
        self.recall_results = recall_results
        # Indicates whether the session is saved as a favorite by the current logged-in user.
        self.saved = saved
        # The session configuration item.
        self.session_config = session_config
        # The agent session ID.
        self.session_id = session_id
        # The session status.
        self.session_status = session_status
        # The title.
        self.title = title
        # The ID of the session owner.
        self.user_id = user_id

    def validate(self):
        if self.artifacts:
            for v1 in self.artifacts:
                 if v1:
                    v1.validate()
        if self.chat_history_locations:
            for v1 in self.chat_history_locations:
                 if v1:
                    v1.validate()
        if self.data_sources:
            for v1 in self.data_sources:
                 if v1:
                    v1.validate()
        if self.recall_results:
            for v1 in self.recall_results:
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

        if self.agent_status is not None:
            result['AgentStatus'] = self.agent_status

        result['Artifacts'] = []
        if self.artifacts is not None:
            for k1 in self.artifacts:
                result['Artifacts'].append(k1.to_map() if k1 else None)

        result['ChatHistoryLocations'] = []
        if self.chat_history_locations is not None:
            for k1 in self.chat_history_locations:
                result['ChatHistoryLocations'].append(k1.to_map() if k1 else None)

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        result['DataSources'] = []
        if self.data_sources is not None:
            for k1 in self.data_sources:
                result['DataSources'].append(k1.to_map() if k1 else None)

        if self.favorite_in_workspace is not None:
            result['FavoriteInWorkspace'] = self.favorite_in_workspace

        if self.file is not None:
            result['File'] = self.file

        result['RecallResults'] = []
        if self.recall_results is not None:
            for k1 in self.recall_results:
                result['RecallResults'].append(k1.to_map() if k1 else None)

        if self.saved is not None:
            result['Saved'] = self.saved

        if self.session_config is not None:
            result['SessionConfig'] = self.session_config.to_map()

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.session_status is not None:
            result['SessionStatus'] = self.session_status

        if self.title is not None:
            result['Title'] = self.title

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('AgentStatus') is not None:
            self.agent_status = m.get('AgentStatus')

        self.artifacts = []
        if m.get('Artifacts') is not None:
            for k1 in m.get('Artifacts'):
                temp_model = main_models.DescribeDataAgentSessionResponseBodyDataArtifacts()
                self.artifacts.append(temp_model.from_map(k1))

        self.chat_history_locations = []
        if m.get('ChatHistoryLocations') is not None:
            for k1 in m.get('ChatHistoryLocations'):
                temp_model = main_models.DescribeDataAgentSessionResponseBodyDataChatHistoryLocations()
                self.chat_history_locations.append(temp_model.from_map(k1))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        self.data_sources = []
        if m.get('DataSources') is not None:
            for k1 in m.get('DataSources'):
                temp_model = main_models.DescribeDataAgentSessionResponseBodyDataDataSources()
                self.data_sources.append(temp_model.from_map(k1))

        if m.get('FavoriteInWorkspace') is not None:
            self.favorite_in_workspace = m.get('FavoriteInWorkspace')

        if m.get('File') is not None:
            self.file = m.get('File')

        self.recall_results = []
        if m.get('RecallResults') is not None:
            for k1 in m.get('RecallResults'):
                temp_model = main_models.DescribeDataAgentSessionResponseBodyDataRecallResults()
                self.recall_results.append(temp_model.from_map(k1))

        if m.get('Saved') is not None:
            self.saved = m.get('Saved')

        if m.get('SessionConfig') is not None:
            temp_model = main_models.DescribeDataAgentSessionResponseBodyDataSessionConfig()
            self.session_config = temp_model.from_map(m.get('SessionConfig'))

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('SessionStatus') is not None:
            self.session_status = m.get('SessionStatus')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class DescribeDataAgentSessionResponseBodyDataSessionConfig(DaraModel):
    def __init__(
        self,
        custom_agent_id: str = None,
        custom_agent_stage: str = None,
        enable_search: bool = None,
        encrypt_key: str = None,
        encrypt_type: str = None,
        kb_uuid_list: List[str] = None,
        language: str = None,
        mcp_server_ids: List[str] = None,
        mode: str = None,
        report_page_width: int = None,
        report_water_mark: str = None,
        user_oss_bucket: str = None,
    ):
        # The custom agent ID.
        self.custom_agent_id = custom_agent_id
        # The stage of the custom agent. Valid values:
        # - **debug**: Debug stage.
        # - **prod**: Production stage.
        self.custom_agent_stage = custom_agent_stage
        # Specifies whether to enable web search.
        self.enable_search = enable_search
        self.encrypt_key = encrypt_key
        self.encrypt_type = encrypt_type
        self.kb_uuid_list = kb_uuid_list
        # The language. Valid values:
        # - **CHINESE**: Chinese.
        # - **ENGLISH**: English.
        self.language = language
        # The list of MCP server IDs in the session configuration.
        self.mcp_server_ids = mcp_server_ids
        # The mode. Valid values:
        # - **ASK_DATA**: Ask data mode.
        # - **ANALYSIS**: Analysis mode.
        # - **INSIGHT**: Insight mode.
        self.mode = mode
        self.report_page_width = report_page_width
        self.report_water_mark = report_water_mark
        # The name of the user OSS bucket.
        # - Analysis process files and report artifacts can be uploaded to the user-specified OSS bucket.
        self.user_oss_bucket = user_oss_bucket

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

        if self.enable_search is not None:
            result['EnableSearch'] = self.enable_search

        if self.encrypt_key is not None:
            result['EncryptKey'] = self.encrypt_key

        if self.encrypt_type is not None:
            result['EncryptType'] = self.encrypt_type

        if self.kb_uuid_list is not None:
            result['KbUuidList'] = self.kb_uuid_list

        if self.language is not None:
            result['Language'] = self.language

        if self.mcp_server_ids is not None:
            result['McpServerIds'] = self.mcp_server_ids

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.report_page_width is not None:
            result['ReportPageWidth'] = self.report_page_width

        if self.report_water_mark is not None:
            result['ReportWaterMark'] = self.report_water_mark

        if self.user_oss_bucket is not None:
            result['UserOssBucket'] = self.user_oss_bucket

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomAgentId') is not None:
            self.custom_agent_id = m.get('CustomAgentId')

        if m.get('CustomAgentStage') is not None:
            self.custom_agent_stage = m.get('CustomAgentStage')

        if m.get('EnableSearch') is not None:
            self.enable_search = m.get('EnableSearch')

        if m.get('EncryptKey') is not None:
            self.encrypt_key = m.get('EncryptKey')

        if m.get('EncryptType') is not None:
            self.encrypt_type = m.get('EncryptType')

        if m.get('KbUuidList') is not None:
            self.kb_uuid_list = m.get('KbUuidList')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('McpServerIds') is not None:
            self.mcp_server_ids = m.get('McpServerIds')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('ReportPageWidth') is not None:
            self.report_page_width = m.get('ReportPageWidth')

        if m.get('ReportWaterMark') is not None:
            self.report_water_mark = m.get('ReportWaterMark')

        if m.get('UserOssBucket') is not None:
            self.user_oss_bucket = m.get('UserOssBucket')

        return self

class DescribeDataAgentSessionResponseBodyDataRecallResults(DaraModel):
    def __init__(
        self,
        content: str = None,
        score: float = None,
        type: str = None,
    ):
        self.content = content
        self.score = score
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.score is not None:
            result['Score'] = self.score

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeDataAgentSessionResponseBodyDataDataSources(DaraModel):
    def __init__(
        self,
        category: str = None,
        detail: str = None,
    ):
        self.category = category
        self.detail = detail

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.detail is not None:
            result['Detail'] = self.detail

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        return self

class DescribeDataAgentSessionResponseBodyDataChatHistoryLocations(DaraModel):
    def __init__(
        self,
        key: str = None,
        url: str = None,
    ):
        # The key of the chat replay history.
        self.key = key
        # The OSS download URL of the chat replay history.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class DescribeDataAgentSessionResponseBodyDataArtifacts(DaraModel):
    def __init__(
        self,
        description: str = None,
        finish_time: str = None,
        id: str = None,
        name: str = None,
        receive_time: str = None,
        start_time: str = None,
        status: str = None,
        type: str = None,
    ):
        self.description = description
        self.finish_time = finish_time
        self.id = id
        self.name = name
        self.receive_time = receive_time
        self.start_time = start_time
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.receive_time is not None:
            result['ReceiveTime'] = self.receive_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ReceiveTime') is not None:
            self.receive_time = m.get('ReceiveTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

