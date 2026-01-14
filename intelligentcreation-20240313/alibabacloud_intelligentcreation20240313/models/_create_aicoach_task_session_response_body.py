# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_intelligentcreation20240313 import models as main_models
from darabonba.model import DaraModel

class CreateAICoachTaskSessionResponseBody(DaraModel):
    def __init__(
        self,
        channel_token: str = None,
        request_id: str = None,
        script_info: main_models.CreateAICoachTaskSessionResponseBodyScriptInfo = None,
        session_id: str = None,
        session_status: int = None,
        token: str = None,
        web_socket_url: str = None,
    ):
        # rtctoken
        self.channel_token = channel_token
        self.request_id = request_id
        self.script_info = script_info
        self.session_id = session_id
        self.session_status = session_status
        # Token
        self.token = token
        self.web_socket_url = web_socket_url

    def validate(self):
        if self.script_info:
            self.script_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_token is not None:
            result['channelToken'] = self.channel_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.script_info is not None:
            result['scriptInfo'] = self.script_info.to_map()

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.session_status is not None:
            result['sessionStatus'] = self.session_status

        if self.token is not None:
            result['token'] = self.token

        if self.web_socket_url is not None:
            result['webSocketUrl'] = self.web_socket_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channelToken') is not None:
            self.channel_token = m.get('channelToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('scriptInfo') is not None:
            temp_model = main_models.CreateAICoachTaskSessionResponseBodyScriptInfo()
            self.script_info = temp_model.from_map(m.get('scriptInfo'))

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('sessionStatus') is not None:
            self.session_status = m.get('sessionStatus')

        if m.get('token') is not None:
            self.token = m.get('token')

        if m.get('webSocketUrl') is not None:
            self.web_socket_url = m.get('webSocketUrl')

        return self

class CreateAICoachTaskSessionResponseBodyScriptInfo(DaraModel):
    def __init__(
        self,
        agent_icon_url: str = None,
        character_name: str = None,
        dialogue_text_flag: bool = None,
        dialogue_tip_flag: bool = None,
        initiator: str = None,
        input_type_list: List[str] = None,
        max_duration: int = None,
        script_desc: str = None,
        script_name: str = None,
        script_record_id: str = None,
        script_type: int = None,
        sparring_tip_content: str = None,
        sparring_tip_title: str = None,
        student_think_time_flag: bool = None,
        student_think_time_limit: int = None,
    ):
        self.agent_icon_url = agent_icon_url
        self.character_name = character_name
        self.dialogue_text_flag = dialogue_text_flag
        self.dialogue_tip_flag = dialogue_tip_flag
        self.initiator = initiator
        self.input_type_list = input_type_list
        self.max_duration = max_duration
        self.script_desc = script_desc
        self.script_name = script_name
        self.script_record_id = script_record_id
        self.script_type = script_type
        self.sparring_tip_content = sparring_tip_content
        self.sparring_tip_title = sparring_tip_title
        self.student_think_time_flag = student_think_time_flag
        self.student_think_time_limit = student_think_time_limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_icon_url is not None:
            result['agentIconUrl'] = self.agent_icon_url

        if self.character_name is not None:
            result['characterName'] = self.character_name

        if self.dialogue_text_flag is not None:
            result['dialogueTextFlag'] = self.dialogue_text_flag

        if self.dialogue_tip_flag is not None:
            result['dialogueTipFlag'] = self.dialogue_tip_flag

        if self.initiator is not None:
            result['initiator'] = self.initiator

        if self.input_type_list is not None:
            result['inputTypeList'] = self.input_type_list

        if self.max_duration is not None:
            result['maxDuration'] = self.max_duration

        if self.script_desc is not None:
            result['scriptDesc'] = self.script_desc

        if self.script_name is not None:
            result['scriptName'] = self.script_name

        if self.script_record_id is not None:
            result['scriptRecordId'] = self.script_record_id

        if self.script_type is not None:
            result['scriptType'] = self.script_type

        if self.sparring_tip_content is not None:
            result['sparringTipContent'] = self.sparring_tip_content

        if self.sparring_tip_title is not None:
            result['sparringTipTitle'] = self.sparring_tip_title

        if self.student_think_time_flag is not None:
            result['studentThinkTimeFlag'] = self.student_think_time_flag

        if self.student_think_time_limit is not None:
            result['studentThinkTimeLimit'] = self.student_think_time_limit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentIconUrl') is not None:
            self.agent_icon_url = m.get('agentIconUrl')

        if m.get('characterName') is not None:
            self.character_name = m.get('characterName')

        if m.get('dialogueTextFlag') is not None:
            self.dialogue_text_flag = m.get('dialogueTextFlag')

        if m.get('dialogueTipFlag') is not None:
            self.dialogue_tip_flag = m.get('dialogueTipFlag')

        if m.get('initiator') is not None:
            self.initiator = m.get('initiator')

        if m.get('inputTypeList') is not None:
            self.input_type_list = m.get('inputTypeList')

        if m.get('maxDuration') is not None:
            self.max_duration = m.get('maxDuration')

        if m.get('scriptDesc') is not None:
            self.script_desc = m.get('scriptDesc')

        if m.get('scriptName') is not None:
            self.script_name = m.get('scriptName')

        if m.get('scriptRecordId') is not None:
            self.script_record_id = m.get('scriptRecordId')

        if m.get('scriptType') is not None:
            self.script_type = m.get('scriptType')

        if m.get('sparringTipContent') is not None:
            self.sparring_tip_content = m.get('sparringTipContent')

        if m.get('sparringTipTitle') is not None:
            self.sparring_tip_title = m.get('sparringTipTitle')

        if m.get('studentThinkTimeFlag') is not None:
            self.student_think_time_flag = m.get('studentThinkTimeFlag')

        if m.get('studentThinkTimeLimit') is not None:
            self.student_think_time_limit = m.get('studentThinkTimeLimit')

        return self

