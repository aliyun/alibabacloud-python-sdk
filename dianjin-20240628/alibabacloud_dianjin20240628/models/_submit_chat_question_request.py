# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dianjin20240628 import models as main_models
from darabonba.model import DaraModel

class SubmitChatQuestionRequest(DaraModel):
    def __init__(
        self,
        gmt_service: str = None,
        live_script_content: str = None,
        open_small_talk: bool = None,
        question_list: List[main_models.SubmitChatQuestionRequestQuestionList] = None,
        request_id: str = None,
        session_id: str = None,
    ):
        # This parameter is required.
        self.gmt_service = gmt_service
        # This parameter is required.
        self.live_script_content = live_script_content
        self.open_small_talk = open_small_talk
        # This parameter is required.
        self.question_list = question_list
        # This parameter is required.
        self.request_id = request_id
        # This parameter is required.
        self.session_id = session_id

    def validate(self):
        if self.question_list:
            for v1 in self.question_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_service is not None:
            result['gmtService'] = self.gmt_service

        if self.live_script_content is not None:
            result['liveScriptContent'] = self.live_script_content

        if self.open_small_talk is not None:
            result['openSmallTalk'] = self.open_small_talk

        result['questionList'] = []
        if self.question_list is not None:
            for k1 in self.question_list:
                result['questionList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtService') is not None:
            self.gmt_service = m.get('gmtService')

        if m.get('liveScriptContent') is not None:
            self.live_script_content = m.get('liveScriptContent')

        if m.get('openSmallTalk') is not None:
            self.open_small_talk = m.get('openSmallTalk')

        self.question_list = []
        if m.get('questionList') is not None:
            for k1 in m.get('questionList'):
                temp_model = main_models.SubmitChatQuestionRequestQuestionList()
                self.question_list.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        return self

class SubmitChatQuestionRequestQuestionList(DaraModel):
    def __init__(
        self,
        content: str = None,
        gmt_create: str = None,
        reply: str = None,
        session_id: str = None,
        type: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        # This parameter is required.
        self.content = content
        # This parameter is required.
        self.gmt_create = gmt_create
        self.reply = reply
        # This parameter is required.
        self.session_id = session_id
        self.type = type
        # This parameter is required.
        self.user_id = user_id
        # This parameter is required.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.reply is not None:
            result['reply'] = self.reply

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.type is not None:
            result['type'] = self.type

        if self.user_id is not None:
            result['userId'] = self.user_id

        if self.user_name is not None:
            result['userName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('reply') is not None:
            self.reply = m.get('reply')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        if m.get('userName') is not None:
            self.user_name = m.get('userName')

        return self

