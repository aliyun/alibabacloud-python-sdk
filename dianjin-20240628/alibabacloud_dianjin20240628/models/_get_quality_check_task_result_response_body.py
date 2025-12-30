# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_dianjin20240628 import models as main_models
from darabonba.model import DaraModel

class GetQualityCheckTaskResultResponseBody(DaraModel):
    def __init__(
        self,
        cost: int = None,
        data: main_models.GetQualityCheckTaskResultResponseBodyData = None,
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
            temp_model = main_models.GetQualityCheckTaskResultResponseBodyData()
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

class GetQualityCheckTaskResultResponseBodyData(DaraModel):
    def __init__(
        self,
        conversation_list: main_models.GetQualityCheckTaskResultResponseBodyDataConversationList = None,
        gmt_create: str = None,
        gmt_end: str = None,
        gmt_start: str = None,
        quality_check_list: List[main_models.GetQualityCheckTaskResultResponseBodyDataQualityCheckList] = None,
        status: str = None,
        task_id: str = None,
    ):
        self.conversation_list = conversation_list
        self.gmt_create = gmt_create
        self.gmt_end = gmt_end
        self.gmt_start = gmt_start
        self.quality_check_list = quality_check_list
        self.status = status
        self.task_id = task_id

    def validate(self):
        if self.conversation_list:
            self.conversation_list.validate()
        if self.quality_check_list:
            for v1 in self.quality_check_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conversation_list is not None:
            result['conversationList'] = self.conversation_list.to_map()

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_end is not None:
            result['gmtEnd'] = self.gmt_end

        if self.gmt_start is not None:
            result['gmtStart'] = self.gmt_start

        result['qualityCheckList'] = []
        if self.quality_check_list is not None:
            for k1 in self.quality_check_list:
                result['qualityCheckList'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['status'] = self.status

        if self.task_id is not None:
            result['taskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('conversationList') is not None:
            temp_model = main_models.GetQualityCheckTaskResultResponseBodyDataConversationList()
            self.conversation_list = temp_model.from_map(m.get('conversationList'))

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtEnd') is not None:
            self.gmt_end = m.get('gmtEnd')

        if m.get('gmtStart') is not None:
            self.gmt_start = m.get('gmtStart')

        self.quality_check_list = []
        if m.get('qualityCheckList') is not None:
            for k1 in m.get('qualityCheckList'):
                temp_model = main_models.GetQualityCheckTaskResultResponseBodyDataQualityCheckList()
                self.quality_check_list.append(temp_model.from_map(k1))

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        return self

class GetQualityCheckTaskResultResponseBodyDataQualityCheckList(DaraModel):
    def __init__(
        self,
        biz_type: str = None,
        check_explanation: str = None,
        check_passed: str = None,
        check_process: str = None,
        checked: str = None,
        gmt_end: str = None,
        gmt_start: str = None,
        mode: str = None,
        origin_dialogue: List[main_models.GetQualityCheckTaskResultResponseBodyDataQualityCheckListOriginDialogue] = None,
        quality_group_id: str = None,
        rule_description: str = None,
        rule_id: str = None,
        rule_type: str = None,
        sub_node_col: List[Any] = None,
    ):
        self.biz_type = biz_type
        self.check_explanation = check_explanation
        self.check_passed = check_passed
        self.check_process = check_process
        self.checked = checked
        self.gmt_end = gmt_end
        self.gmt_start = gmt_start
        self.mode = mode
        self.origin_dialogue = origin_dialogue
        self.quality_group_id = quality_group_id
        self.rule_description = rule_description
        self.rule_id = rule_id
        self.rule_type = rule_type
        self.sub_node_col = sub_node_col

    def validate(self):
        if self.origin_dialogue:
            for v1 in self.origin_dialogue:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_type is not None:
            result['bizType'] = self.biz_type

        if self.check_explanation is not None:
            result['checkExplanation'] = self.check_explanation

        if self.check_passed is not None:
            result['checkPassed'] = self.check_passed

        if self.check_process is not None:
            result['checkProcess'] = self.check_process

        if self.checked is not None:
            result['checked'] = self.checked

        if self.gmt_end is not None:
            result['gmtEnd'] = self.gmt_end

        if self.gmt_start is not None:
            result['gmtStart'] = self.gmt_start

        if self.mode is not None:
            result['mode'] = self.mode

        result['originDialogue'] = []
        if self.origin_dialogue is not None:
            for k1 in self.origin_dialogue:
                result['originDialogue'].append(k1.to_map() if k1 else None)

        if self.quality_group_id is not None:
            result['qualityGroupId'] = self.quality_group_id

        if self.rule_description is not None:
            result['ruleDescription'] = self.rule_description

        if self.rule_id is not None:
            result['ruleId'] = self.rule_id

        if self.rule_type is not None:
            result['ruleType'] = self.rule_type

        if self.sub_node_col is not None:
            result['subNodeCol'] = self.sub_node_col

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizType') is not None:
            self.biz_type = m.get('bizType')

        if m.get('checkExplanation') is not None:
            self.check_explanation = m.get('checkExplanation')

        if m.get('checkPassed') is not None:
            self.check_passed = m.get('checkPassed')

        if m.get('checkProcess') is not None:
            self.check_process = m.get('checkProcess')

        if m.get('checked') is not None:
            self.checked = m.get('checked')

        if m.get('gmtEnd') is not None:
            self.gmt_end = m.get('gmtEnd')

        if m.get('gmtStart') is not None:
            self.gmt_start = m.get('gmtStart')

        if m.get('mode') is not None:
            self.mode = m.get('mode')

        self.origin_dialogue = []
        if m.get('originDialogue') is not None:
            for k1 in m.get('originDialogue'):
                temp_model = main_models.GetQualityCheckTaskResultResponseBodyDataQualityCheckListOriginDialogue()
                self.origin_dialogue.append(temp_model.from_map(k1))

        if m.get('qualityGroupId') is not None:
            self.quality_group_id = m.get('qualityGroupId')

        if m.get('ruleDescription') is not None:
            self.rule_description = m.get('ruleDescription')

        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')

        if m.get('ruleType') is not None:
            self.rule_type = m.get('ruleType')

        if m.get('subNodeCol') is not None:
            self.sub_node_col = m.get('subNodeCol')

        return self

class GetQualityCheckTaskResultResponseBodyDataQualityCheckListOriginDialogue(DaraModel):
    def __init__(
        self,
        begin: int = None,
        begin_time: str = None,
        content: str = None,
        customer_id: str = None,
        customer_service_id: str = None,
        customer_service_type: str = None,
        end: int = None,
        id: int = None,
        role: str = None,
        type: str = None,
    ):
        self.begin = begin
        self.begin_time = begin_time
        self.content = content
        self.customer_id = customer_id
        self.customer_service_id = customer_service_id
        self.customer_service_type = customer_service_type
        self.end = end
        self.id = id
        self.role = role
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin is not None:
            result['begin'] = self.begin

        if self.begin_time is not None:
            result['beginTime'] = self.begin_time

        if self.content is not None:
            result['content'] = self.content

        if self.customer_id is not None:
            result['customerId'] = self.customer_id

        if self.customer_service_id is not None:
            result['customerServiceId'] = self.customer_service_id

        if self.customer_service_type is not None:
            result['customerServiceType'] = self.customer_service_type

        if self.end is not None:
            result['end'] = self.end

        if self.id is not None:
            result['id'] = self.id

        if self.role is not None:
            result['role'] = self.role

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('begin') is not None:
            self.begin = m.get('begin')

        if m.get('beginTime') is not None:
            self.begin_time = m.get('beginTime')

        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')

        if m.get('customerServiceId') is not None:
            self.customer_service_id = m.get('customerServiceId')

        if m.get('customerServiceType') is not None:
            self.customer_service_type = m.get('customerServiceType')

        if m.get('end') is not None:
            self.end = m.get('end')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('role') is not None:
            self.role = m.get('role')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class GetQualityCheckTaskResultResponseBodyDataConversationList(DaraModel):
    def __init__(
        self,
        call_type: str = None,
        customer_id: str = None,
        customer_name: str = None,
        customer_service_id: str = None,
        customer_service_name: str = None,
        dialogue_list: List[main_models.GetQualityCheckTaskResultResponseBodyDataConversationListDialogueList] = None,
        gmt_service: str = None,
    ):
        self.call_type = call_type
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.customer_service_id = customer_service_id
        self.customer_service_name = customer_service_name
        self.dialogue_list = dialogue_list
        self.gmt_service = gmt_service

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
        if self.call_type is not None:
            result['callType'] = self.call_type

        if self.customer_id is not None:
            result['customerId'] = self.customer_id

        if self.customer_name is not None:
            result['customerName'] = self.customer_name

        if self.customer_service_id is not None:
            result['customerServiceId'] = self.customer_service_id

        if self.customer_service_name is not None:
            result['customerServiceName'] = self.customer_service_name

        result['dialogueList'] = []
        if self.dialogue_list is not None:
            for k1 in self.dialogue_list:
                result['dialogueList'].append(k1.to_map() if k1 else None)

        if self.gmt_service is not None:
            result['gmtService'] = self.gmt_service

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('callType') is not None:
            self.call_type = m.get('callType')

        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')

        if m.get('customerName') is not None:
            self.customer_name = m.get('customerName')

        if m.get('customerServiceId') is not None:
            self.customer_service_id = m.get('customerServiceId')

        if m.get('customerServiceName') is not None:
            self.customer_service_name = m.get('customerServiceName')

        self.dialogue_list = []
        if m.get('dialogueList') is not None:
            for k1 in m.get('dialogueList'):
                temp_model = main_models.GetQualityCheckTaskResultResponseBodyDataConversationListDialogueList()
                self.dialogue_list.append(temp_model.from_map(k1))

        if m.get('gmtService') is not None:
            self.gmt_service = m.get('gmtService')

        return self

class GetQualityCheckTaskResultResponseBodyDataConversationListDialogueList(DaraModel):
    def __init__(
        self,
        begin: int = None,
        begin_time: str = None,
        content: str = None,
        customer_id: str = None,
        customer_service_id: str = None,
        customer_service_type: str = None,
        end: int = None,
        id: int = None,
        role: str = None,
        type: str = None,
    ):
        self.begin = begin
        self.begin_time = begin_time
        self.content = content
        self.customer_id = customer_id
        self.customer_service_id = customer_service_id
        self.customer_service_type = customer_service_type
        self.end = end
        self.id = id
        self.role = role
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin is not None:
            result['begin'] = self.begin

        if self.begin_time is not None:
            result['beginTime'] = self.begin_time

        if self.content is not None:
            result['content'] = self.content

        if self.customer_id is not None:
            result['customerId'] = self.customer_id

        if self.customer_service_id is not None:
            result['customerServiceId'] = self.customer_service_id

        if self.customer_service_type is not None:
            result['customerServiceType'] = self.customer_service_type

        if self.end is not None:
            result['end'] = self.end

        if self.id is not None:
            result['id'] = self.id

        if self.role is not None:
            result['role'] = self.role

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('begin') is not None:
            self.begin = m.get('begin')

        if m.get('beginTime') is not None:
            self.begin_time = m.get('beginTime')

        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')

        if m.get('customerServiceId') is not None:
            self.customer_service_id = m.get('customerServiceId')

        if m.get('customerServiceType') is not None:
            self.customer_service_type = m.get('customerServiceType')

        if m.get('end') is not None:
            self.end = m.get('end')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('role') is not None:
            self.role = m.get('role')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

