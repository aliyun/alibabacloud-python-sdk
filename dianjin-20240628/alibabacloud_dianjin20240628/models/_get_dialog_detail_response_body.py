# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dianjin20240628 import models as main_models
from darabonba.model import DaraModel

class GetDialogDetailResponseBody(DaraModel):
    def __init__(
        self,
        cost: int = None,
        data: main_models.GetDialogDetailResponseBodyData = None,
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
            temp_model = main_models.GetDialogDetailResponseBodyData()
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

class GetDialogDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        dialogue_list: List[main_models.GetDialogDetailResponseBodyDataDialogueList] = None,
        gmt_create: str = None,
        status: str = None,
        total_dialog_turns: int = None,
        valid_dialog_turns: int = None,
    ):
        self.dialogue_list = dialogue_list
        self.gmt_create = gmt_create
        self.status = status
        self.total_dialog_turns = total_dialog_turns
        self.valid_dialog_turns = valid_dialog_turns

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
        result['dialogueList'] = []
        if self.dialogue_list is not None:
            for k1 in self.dialogue_list:
                result['dialogueList'].append(k1.to_map() if k1 else None)

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.status is not None:
            result['status'] = self.status

        if self.total_dialog_turns is not None:
            result['totalDialogTurns'] = self.total_dialog_turns

        if self.valid_dialog_turns is not None:
            result['validDialogTurns'] = self.valid_dialog_turns

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dialogue_list = []
        if m.get('dialogueList') is not None:
            for k1 in m.get('dialogueList'):
                temp_model = main_models.GetDialogDetailResponseBodyDataDialogueList()
                self.dialogue_list.append(temp_model.from_map(k1))

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('totalDialogTurns') is not None:
            self.total_dialog_turns = m.get('totalDialogTurns')

        if m.get('validDialogTurns') is not None:
            self.valid_dialog_turns = m.get('validDialogTurns')

        return self

class GetDialogDetailResponseBodyDataDialogueList(DaraModel):
    def __init__(
        self,
        content: str = None,
        customer_id: str = None,
        customer_service_id: str = None,
        customer_service_type: str = None,
        hang_up_dialog: bool = None,
        id: int = None,
        intent_code: str = None,
        intent_name: str = None,
        role: str = None,
        type: str = None,
    ):
        self.content = content
        self.customer_id = customer_id
        self.customer_service_id = customer_service_id
        self.customer_service_type = customer_service_type
        self.hang_up_dialog = hang_up_dialog
        self.id = id
        self.intent_code = intent_code
        self.intent_name = intent_name
        self.role = role
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.customer_id is not None:
            result['customerId'] = self.customer_id

        if self.customer_service_id is not None:
            result['customerServiceId'] = self.customer_service_id

        if self.customer_service_type is not None:
            result['customerServiceType'] = self.customer_service_type

        if self.hang_up_dialog is not None:
            result['hangUpDialog'] = self.hang_up_dialog

        if self.id is not None:
            result['id'] = self.id

        if self.intent_code is not None:
            result['intentCode'] = self.intent_code

        if self.intent_name is not None:
            result['intentName'] = self.intent_name

        if self.role is not None:
            result['role'] = self.role

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')

        if m.get('customerServiceId') is not None:
            self.customer_service_id = m.get('customerServiceId')

        if m.get('customerServiceType') is not None:
            self.customer_service_type = m.get('customerServiceType')

        if m.get('hangUpDialog') is not None:
            self.hang_up_dialog = m.get('hangUpDialog')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('intentCode') is not None:
            self.intent_code = m.get('intentCode')

        if m.get('intentName') is not None:
            self.intent_name = m.get('intentName')

        if m.get('role') is not None:
            self.role = m.get('role')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

