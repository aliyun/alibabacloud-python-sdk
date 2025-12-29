# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aligenieip_1_0 import models as main_models
from darabonba.model import DaraModel

class UpdateHotelSceneItemRequest(DaraModel):
    def __init__(
        self,
        hotel_id: str = None,
        update_hotel_scene_operate_req: main_models.UpdateHotelSceneItemRequestUpdateHotelSceneOperateReq = None,
        update_hotel_scene_req: main_models.UpdateHotelSceneItemRequestUpdateHotelSceneReq = None,
    ):
        # hotelID
        # 
        # This parameter is required.
        self.hotel_id = hotel_id
        # updateHotelSceneReq
        # 
        # This parameter is required.
        self.update_hotel_scene_operate_req = update_hotel_scene_operate_req
        # UpdateHotelSceneReq
        # 
        # This parameter is required.
        self.update_hotel_scene_req = update_hotel_scene_req

    def validate(self):
        if self.update_hotel_scene_operate_req:
            self.update_hotel_scene_operate_req.validate()
        if self.update_hotel_scene_req:
            self.update_hotel_scene_req.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        if self.update_hotel_scene_operate_req is not None:
            result['UpdateHotelSceneOperateReq'] = self.update_hotel_scene_operate_req.to_map()

        if self.update_hotel_scene_req is not None:
            result['UpdateHotelSceneReq'] = self.update_hotel_scene_req.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        if m.get('UpdateHotelSceneOperateReq') is not None:
            temp_model = main_models.UpdateHotelSceneItemRequestUpdateHotelSceneOperateReq()
            self.update_hotel_scene_operate_req = temp_model.from_map(m.get('UpdateHotelSceneOperateReq'))

        if m.get('UpdateHotelSceneReq') is not None:
            temp_model = main_models.UpdateHotelSceneItemRequestUpdateHotelSceneReq()
            self.update_hotel_scene_req = temp_model.from_map(m.get('UpdateHotelSceneReq'))

        return self

class UpdateHotelSceneItemRequestUpdateHotelSceneReq(DaraModel):
    def __init__(
        self,
        beyond_limit_reply: str = None,
        delivery_method: str = None,
        dialogue_list: List[main_models.UpdateHotelSceneItemRequestUpdateHotelSceneReqDialogueList] = None,
        icon: str = None,
        id: int = None,
        limit_number: int = None,
        limit_switch: int = None,
        name: str = None,
        payment_method: str = None,
        price: int = None,
        robot_name: str = None,
        status: str = None,
    ):
        self.beyond_limit_reply = beyond_limit_reply
        self.delivery_method = delivery_method
        # This parameter is required.
        self.dialogue_list = dialogue_list
        # icon
        # 
        # This parameter is required.
        self.icon = icon
        # itemID
        self.id = id
        self.limit_number = limit_number
        self.limit_switch = limit_switch
        self.name = name
        self.payment_method = payment_method
        # This parameter is required.
        self.price = price
        self.robot_name = robot_name
        # This parameter is required.
        self.status = status

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
        if self.beyond_limit_reply is not None:
            result['BeyondLimitReply'] = self.beyond_limit_reply

        if self.delivery_method is not None:
            result['DeliveryMethod'] = self.delivery_method

        result['DialogueList'] = []
        if self.dialogue_list is not None:
            for k1 in self.dialogue_list:
                result['DialogueList'].append(k1.to_map() if k1 else None)

        if self.icon is not None:
            result['Icon'] = self.icon

        if self.id is not None:
            result['Id'] = self.id

        if self.limit_number is not None:
            result['LimitNumber'] = self.limit_number

        if self.limit_switch is not None:
            result['LimitSwitch'] = self.limit_switch

        if self.name is not None:
            result['Name'] = self.name

        if self.payment_method is not None:
            result['PaymentMethod'] = self.payment_method

        if self.price is not None:
            result['Price'] = self.price

        if self.robot_name is not None:
            result['RobotName'] = self.robot_name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeyondLimitReply') is not None:
            self.beyond_limit_reply = m.get('BeyondLimitReply')

        if m.get('DeliveryMethod') is not None:
            self.delivery_method = m.get('DeliveryMethod')

        self.dialogue_list = []
        if m.get('DialogueList') is not None:
            for k1 in m.get('DialogueList'):
                temp_model = main_models.UpdateHotelSceneItemRequestUpdateHotelSceneReqDialogueList()
                self.dialogue_list.append(temp_model.from_map(k1))

        if m.get('Icon') is not None:
            self.icon = m.get('Icon')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LimitNumber') is not None:
            self.limit_number = m.get('LimitNumber')

        if m.get('LimitSwitch') is not None:
            self.limit_switch = m.get('LimitSwitch')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PaymentMethod') is not None:
            self.payment_method = m.get('PaymentMethod')

        if m.get('Price') is not None:
            self.price = m.get('Price')

        if m.get('RobotName') is not None:
            self.robot_name = m.get('RobotName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class UpdateHotelSceneItemRequestUpdateHotelSceneReqDialogueList(DaraModel):
    def __init__(
        self,
        dialogue_id: str = None,
        no_answer: str = None,
        no_answer_template: str = None,
        process: int = None,
        question: str = None,
        service_id: str = None,
        yes_answer: str = None,
        yes_answer_template: str = None,
    ):
        self.dialogue_id = dialogue_id
        self.no_answer = no_answer
        self.no_answer_template = no_answer_template
        self.process = process
        self.question = question
        # itemId
        self.service_id = service_id
        self.yes_answer = yes_answer
        self.yes_answer_template = yes_answer_template

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.yes_answer is not None:
            result['YesAnswer'] = self.yes_answer

        if self.yes_answer_template is not None:
            result['YesAnswerTemplate'] = self.yes_answer_template

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('YesAnswer') is not None:
            self.yes_answer = m.get('YesAnswer')

        if m.get('YesAnswerTemplate') is not None:
            self.yes_answer_template = m.get('YesAnswerTemplate')

        return self

class UpdateHotelSceneItemRequestUpdateHotelSceneOperateReq(DaraModel):
    def __init__(
        self,
        is_use_template_answer: bool = None,
        operate_type: str = None,
    ):
        # This parameter is required.
        self.is_use_template_answer = is_use_template_answer
        # This parameter is required.
        self.operate_type = operate_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_use_template_answer is not None:
            result['IsUseTemplateAnswer'] = self.is_use_template_answer

        if self.operate_type is not None:
            result['OperateType'] = self.operate_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsUseTemplateAnswer') is not None:
            self.is_use_template_answer = m.get('IsUseTemplateAnswer')

        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')

        return self

