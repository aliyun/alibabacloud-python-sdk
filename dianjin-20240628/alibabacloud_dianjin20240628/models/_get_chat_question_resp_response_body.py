# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dianjin20240628 import models as main_models
from darabonba.model import DaraModel

class GetChatQuestionRespResponseBody(DaraModel):
    def __init__(
        self,
        cost: int = None,
        data: main_models.GetChatQuestionRespResponseBodyData = None,
        data_type: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time: str = None,
    ):
        self.cost = cost
        self.data = data
        self.data_type = data_type
        self.err_code = err_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.time = time

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cost is not None:
            result['cost'] = self.cost

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.data_type is not None:
            result['dataType'] = self.data_type

        if self.err_code is not None:
            result['errCode'] = self.err_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        if self.time is not None:
            result['time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            self.cost = m.get('cost')

        if m.get('data') is not None:
            temp_model = main_models.GetChatQuestionRespResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')

        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('time') is not None:
            self.time = m.get('time')

        return self

class GetChatQuestionRespResponseBodyData(DaraModel):
    def __init__(
        self,
        current_state: str = None,
        question_list: List[main_models.GetChatQuestionRespResponseBodyDataQuestionList] = None,
    ):
        self.current_state = current_state
        self.question_list = question_list

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
        if self.current_state is not None:
            result['currentState'] = self.current_state

        result['questionList'] = []
        if self.question_list is not None:
            for k1 in self.question_list:
                result['questionList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentState') is not None:
            self.current_state = m.get('currentState')

        self.question_list = []
        if m.get('questionList') is not None:
            for k1 in m.get('questionList'):
                temp_model = main_models.GetChatQuestionRespResponseBodyDataQuestionList()
                self.question_list.append(temp_model.from_map(k1))

        return self

class GetChatQuestionRespResponseBodyDataQuestionList(DaraModel):
    def __init__(
        self,
        content: str = None,
        gmt_create: str = None,
        ori_content: str = None,
        reply: str = None,
        session_id: str = None,
        type: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.content = content
        self.gmt_create = gmt_create
        self.ori_content = ori_content
        self.reply = reply
        self.session_id = session_id
        self.type = type
        self.user_id = user_id
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

        if self.ori_content is not None:
            result['oriContent'] = self.ori_content

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

        if m.get('oriContent') is not None:
            self.ori_content = m.get('oriContent')

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

