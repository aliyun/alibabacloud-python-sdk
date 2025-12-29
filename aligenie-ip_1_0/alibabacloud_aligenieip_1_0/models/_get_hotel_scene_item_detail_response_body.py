# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aligenieip_1_0 import models as main_models
from darabonba.model import DaraModel

class GetHotelSceneItemDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: main_models.GetHotelSceneItemDetailResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.GetHotelSceneItemDetailResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class GetHotelSceneItemDetailResponseBodyResult(DaraModel):
    def __init__(
        self,
        category: str = None,
        dialogue_list: List[main_models.GetHotelSceneItemDetailResponseBodyResultDialogueList] = None,
        icon: str = None,
        id: int = None,
        name: str = None,
        price: int = None,
        status: str = None,
        type: str = None,
        update_time: int = None,
    ):
        self.category = category
        self.dialogue_list = dialogue_list
        self.icon = icon
        self.id = id
        self.name = name
        self.price = price
        self.status = status
        self.type = type
        self.update_time = update_time

    def validate(self):
        if self.dialogue_list:
            for v1 in self.dialogue_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        result['DialogueList'] = []
        if self.dialogue_list is not None:
            for k1 in self.dialogue_list:
                result['DialogueList'].append(k1.to_map() if k1 else None)

        if self.icon is not None:
            result['Icon'] = self.icon

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.price is not None:
            result['Price'] = self.price

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        self.dialogue_list = []
        if m.get('DialogueList') is not None:
            for k1 in m.get('DialogueList'):
                temp_model = main_models.GetHotelSceneItemDetailResponseBodyResultDialogueList()
                self.dialogue_list.append(temp_model.from_map(k1))

        if m.get('Icon') is not None:
            self.icon = m.get('Icon')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Price') is not None:
            self.price = m.get('Price')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class GetHotelSceneItemDetailResponseBodyResultDialogueList(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        dialogue_id: str = None,
        no_answer: str = None,
        no_answer_template: str = None,
        process: int = None,
        question: str = None,
        service_id: str = None,
        update_time: int = None,
        yes_answer: str = None,
        yes_answer_template: str = None,
    ):
        self.create_time = create_time
        self.dialogue_id = dialogue_id
        self.no_answer = no_answer
        self.no_answer_template = no_answer_template
        self.process = process
        self.question = question
        self.service_id = service_id
        self.update_time = update_time
        self.yes_answer = yes_answer
        self.yes_answer_template = yes_answer_template

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.dialogue_id is not None:
            result['DialogueId'] = self.dialogue_id

        if self.no_answer is not None:
            result['NoAnswer'] = self.no_answer

        if self.no_answer_template is not None:
            result['NoAnswerTemplate'] = self.no_answer_template

        if self.process is not None:
            result['Process'] = self.process

        if self.question is not None:
            result['Question'] = self.question

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.yes_answer is not None:
            result['YesAnswer'] = self.yes_answer

        if self.yes_answer_template is not None:
            result['YesAnswerTemplate'] = self.yes_answer_template

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DialogueId') is not None:
            self.dialogue_id = m.get('DialogueId')

        if m.get('NoAnswer') is not None:
            self.no_answer = m.get('NoAnswer')

        if m.get('NoAnswerTemplate') is not None:
            self.no_answer_template = m.get('NoAnswerTemplate')

        if m.get('Process') is not None:
            self.process = m.get('Process')

        if m.get('Question') is not None:
            self.question = m.get('Question')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('YesAnswer') is not None:
            self.yes_answer = m.get('YesAnswer')

        if m.get('YesAnswerTemplate') is not None:
            self.yes_answer_template = m.get('YesAnswerTemplate')

        return self

