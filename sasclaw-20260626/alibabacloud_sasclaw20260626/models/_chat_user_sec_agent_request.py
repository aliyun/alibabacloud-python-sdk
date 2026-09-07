# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel



class ChatUserSecAgentRequest(DaraModel):
    def __init__(
        self,
        agent: str = None,
        attachment_staging_id: str = None,
        attachments: str = None,
        channel: str = None,
        execution_mode: str = None,
        extra_params: str = None,
        memory: bool = None,
        model: str = None,
        prompt: str = None,
        response_language: str = None,
        session_id: str = None,
        skill: str = None,
        stream: bool = None,
        talk_id: str = None,
        target: str = None,
        time_zone: str = None,
        user_input_info: str = None,
    ):
        self.agent = agent
        # 附件暂存 ID
        self.attachment_staging_id = attachment_staging_id
        # 附件列表 JSON 字符串
        self.attachments = attachments
        # 逻辑渠道名
        self.channel = channel
        # 执行模式: single/team/role
        self.execution_mode = execution_mode
        # 扩展参数 JSON 字符串，如 execution_mode、target 等
        self.extra_params = extra_params
        self.memory = memory
        self.model = model
        # 用户提问；新会话时必填，恢复/交互时可空
        self.prompt = prompt
        self.response_language = response_language
        self.session_id = session_id
        self.skill = skill
        self.stream = stream
        self.talk_id = talk_id
        # 执行目标
        self.target = target
        self.time_zone = time_zone
        # 会话恢复/交互提交信息 JSON 字符串
        self.user_input_info = user_input_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent is not None:
            result['Agent'] = self.agent

        if self.attachment_staging_id is not None:
            result['AttachmentStagingId'] = self.attachment_staging_id

        if self.attachments is not None:
            result['Attachments'] = self.attachments

        if self.channel is not None:
            result['Channel'] = self.channel

        if self.execution_mode is not None:
            result['ExecutionMode'] = self.execution_mode

        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.model is not None:
            result['Model'] = self.model

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.response_language is not None:
            result['ResponseLanguage'] = self.response_language

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.skill is not None:
            result['Skill'] = self.skill

        if self.stream is not None:
            result['Stream'] = self.stream

        if self.talk_id is not None:
            result['TalkId'] = self.talk_id

        if self.target is not None:
            result['Target'] = self.target

        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone

        if self.user_input_info is not None:
            result['UserInputInfo'] = self.user_input_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Agent') is not None:
            self.agent = m.get('Agent')

        if m.get('AttachmentStagingId') is not None:
            self.attachment_staging_id = m.get('AttachmentStagingId')

        if m.get('Attachments') is not None:
            self.attachments = m.get('Attachments')

        if m.get('Channel') is not None:
            self.channel = m.get('Channel')

        if m.get('ExecutionMode') is not None:
            self.execution_mode = m.get('ExecutionMode')

        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('ResponseLanguage') is not None:
            self.response_language = m.get('ResponseLanguage')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('Skill') is not None:
            self.skill = m.get('Skill')

        if m.get('Stream') is not None:
            self.stream = m.get('Stream')

        if m.get('TalkId') is not None:
            self.talk_id = m.get('TalkId')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')

        if m.get('UserInputInfo') is not None:
            self.user_input_info = m.get('UserInputInfo')

        return self

