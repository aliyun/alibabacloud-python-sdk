# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dianjin20240628 import models as main_models
from darabonba.model import DaraModel

class GetDialogLogResponseBody(DaraModel):
    def __init__(
        self,
        cost: int = None,
        data: main_models.GetDialogLogResponseBodyData = None,
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
            temp_model = main_models.GetDialogLogResponseBodyData()
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

class GetDialogLogResponseBodyData(DaraModel):
    def __init__(
        self,
        analysis_process: str = None,
        conversation_list: str = None,
        hit_intention_list: List[main_models.GetDialogLogResponseBodyDataHitIntentionList] = None,
        intention_list: List[main_models.GetDialogLogResponseBodyDataIntentionList] = None,
        model_cost_time: int = None,
        recall_list: str = None,
    ):
        self.analysis_process = analysis_process
        self.conversation_list = conversation_list
        self.hit_intention_list = hit_intention_list
        self.intention_list = intention_list
        self.model_cost_time = model_cost_time
        self.recall_list = recall_list

    def validate(self):
        if self.hit_intention_list:
            for v1 in self.hit_intention_list:
                 if v1:
                    v1.validate()
        if self.intention_list:
            for v1 in self.intention_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.analysis_process is not None:
            result['analysisProcess'] = self.analysis_process

        if self.conversation_list is not None:
            result['conversationList'] = self.conversation_list

        result['hitIntentionList'] = []
        if self.hit_intention_list is not None:
            for k1 in self.hit_intention_list:
                result['hitIntentionList'].append(k1.to_map() if k1 else None)

        result['intentionList'] = []
        if self.intention_list is not None:
            for k1 in self.intention_list:
                result['intentionList'].append(k1.to_map() if k1 else None)

        if self.model_cost_time is not None:
            result['modelCostTime'] = self.model_cost_time

        if self.recall_list is not None:
            result['recallList'] = self.recall_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analysisProcess') is not None:
            self.analysis_process = m.get('analysisProcess')

        if m.get('conversationList') is not None:
            self.conversation_list = m.get('conversationList')

        self.hit_intention_list = []
        if m.get('hitIntentionList') is not None:
            for k1 in m.get('hitIntentionList'):
                temp_model = main_models.GetDialogLogResponseBodyDataHitIntentionList()
                self.hit_intention_list.append(temp_model.from_map(k1))

        self.intention_list = []
        if m.get('intentionList') is not None:
            for k1 in m.get('intentionList'):
                temp_model = main_models.GetDialogLogResponseBodyDataIntentionList()
                self.intention_list.append(temp_model.from_map(k1))

        if m.get('modelCostTime') is not None:
            self.model_cost_time = m.get('modelCostTime')

        if m.get('recallList') is not None:
            self.recall_list = m.get('recallList')

        return self

class GetDialogLogResponseBodyDataIntentionList(DaraModel):
    def __init__(
        self,
        description: str = None,
        intention_name: str = None,
        intention_script: str = None,
    ):
        self.description = description
        self.intention_name = intention_name
        self.intention_script = intention_script

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.intention_name is not None:
            result['intentionName'] = self.intention_name

        if self.intention_script is not None:
            result['intentionScript'] = self.intention_script

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('intentionName') is not None:
            self.intention_name = m.get('intentionName')

        if m.get('intentionScript') is not None:
            self.intention_script = m.get('intentionScript')

        return self

class GetDialogLogResponseBodyDataHitIntentionList(DaraModel):
    def __init__(
        self,
        description: str = None,
        intention_name: str = None,
        intention_script: str = None,
    ):
        self.description = description
        self.intention_name = intention_name
        self.intention_script = intention_script

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.intention_name is not None:
            result['intentionName'] = self.intention_name

        if self.intention_script is not None:
            result['intentionScript'] = self.intention_script

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('intentionName') is not None:
            self.intention_name = m.get('intentionName')

        if m.get('intentionScript') is not None:
            self.intention_script = m.get('intentionScript')

        return self

