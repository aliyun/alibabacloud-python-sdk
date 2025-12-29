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
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        # Id of the request
        self.request_id = request_id
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
        chat_history_locations: List[main_models.DescribeDataAgentSessionResponseBodyDataChatHistoryLocations] = None,
        create_time: int = None,
        favorite_in_workspace: str = None,
        file: str = None,
        saved: bool = None,
        session_config: main_models.DescribeDataAgentSessionResponseBodyDataSessionConfig = None,
        session_id: str = None,
        session_status: str = None,
        title: str = None,
        user_id: str = None,
    ):
        self.agent_id = agent_id
        self.agent_status = agent_status
        self.chat_history_locations = chat_history_locations
        self.create_time = create_time
        self.favorite_in_workspace = favorite_in_workspace
        self.file = file
        self.saved = saved
        self.session_config = session_config
        self.session_id = session_id
        self.session_status = session_status
        self.title = title
        self.user_id = user_id

    def validate(self):
        if self.chat_history_locations:
            for v1 in self.chat_history_locations:
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

        result['ChatHistoryLocations'] = []
        if self.chat_history_locations is not None:
            for k1 in self.chat_history_locations:
                result['ChatHistoryLocations'].append(k1.to_map() if k1 else None)

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.favorite_in_workspace is not None:
            result['FavoriteInWorkspace'] = self.favorite_in_workspace

        if self.file is not None:
            result['File'] = self.file

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

        self.chat_history_locations = []
        if m.get('ChatHistoryLocations') is not None:
            for k1 in m.get('ChatHistoryLocations'):
                temp_model = main_models.DescribeDataAgentSessionResponseBodyDataChatHistoryLocations()
                self.chat_history_locations.append(temp_model.from_map(k1))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('FavoriteInWorkspace') is not None:
            self.favorite_in_workspace = m.get('FavoriteInWorkspace')

        if m.get('File') is not None:
            self.file = m.get('File')

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
        language: str = None,
        mcp_server_ids: List[str] = None,
        mode: str = None,
    ):
        self.custom_agent_id = custom_agent_id
        self.custom_agent_stage = custom_agent_stage
        self.enable_search = enable_search
        self.language = language
        self.mcp_server_ids = mcp_server_ids
        self.mode = mode

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

        if self.language is not None:
            result['Language'] = self.language

        if self.mcp_server_ids is not None:
            result['McpServerIds'] = self.mcp_server_ids

        if self.mode is not None:
            result['Mode'] = self.mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomAgentId') is not None:
            self.custom_agent_id = m.get('CustomAgentId')

        if m.get('CustomAgentStage') is not None:
            self.custom_agent_stage = m.get('CustomAgentStage')

        if m.get('EnableSearch') is not None:
            self.enable_search = m.get('EnableSearch')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('McpServerIds') is not None:
            self.mcp_server_ids = m.get('McpServerIds')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        return self

class DescribeDataAgentSessionResponseBodyDataChatHistoryLocations(DaraModel):
    def __init__(
        self,
        key: str = None,
        url: str = None,
    ):
        self.key = key
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

