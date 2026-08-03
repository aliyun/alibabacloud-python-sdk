# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_intelligentcreation20240313 import models as main_models
from darabonba.model import DaraModel

class GetAICoachDebugResultResponseBody(DaraModel):
    def __init__(
        self,
        aliyun_sub_id: str = None,
        data_id: str = None,
        data_type: int = None,
        dialogue_list: List[main_models.GetAICoachDebugResultResponseBodyDialogueList] = None,
        error_code: str = None,
        error_message: str = None,
        finish_time: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        request_id: str = None,
        script_debug_id: str = None,
        status: int = None,
        success: bool = None,
        task_id: str = None,
        task_report: main_models.GetAICoachDebugResultResponseBodyTaskReport = None,
    ):
        self.aliyun_sub_id = aliyun_sub_id
        self.data_id = data_id
        self.data_type = data_type
        self.dialogue_list = dialogue_list
        self.error_code = error_code
        self.error_message = error_message
        self.finish_time = finish_time
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.request_id = request_id
        self.script_debug_id = script_debug_id
        self.status = status
        self.success = success
        self.task_id = task_id
        self.task_report = task_report

    def validate(self):
        if self.dialogue_list:
            for v1 in self.dialogue_list:
                 if v1:
                    v1.validate()
        if self.task_report:
            self.task_report.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_sub_id is not None:
            result['aliyunSubId'] = self.aliyun_sub_id

        if self.data_id is not None:
            result['dataId'] = self.data_id

        if self.data_type is not None:
            result['dataType'] = self.data_type

        result['dialogueList'] = []
        if self.dialogue_list is not None:
            for k1 in self.dialogue_list:
                result['dialogueList'].append(k1.to_map() if k1 else None)

        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.finish_time is not None:
            result['finishTime'] = self.finish_time

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.script_debug_id is not None:
            result['scriptDebugId'] = self.script_debug_id

        if self.status is not None:
            result['status'] = self.status

        if self.success is not None:
            result['success'] = self.success

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.task_report is not None:
            result['taskReport'] = self.task_report.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliyunSubId') is not None:
            self.aliyun_sub_id = m.get('aliyunSubId')

        if m.get('dataId') is not None:
            self.data_id = m.get('dataId')

        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')

        self.dialogue_list = []
        if m.get('dialogueList') is not None:
            for k1 in m.get('dialogueList'):
                temp_model = main_models.GetAICoachDebugResultResponseBodyDialogueList()
                self.dialogue_list.append(temp_model.from_map(k1))

        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('finishTime') is not None:
            self.finish_time = m.get('finishTime')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('scriptDebugId') is not None:
            self.script_debug_id = m.get('scriptDebugId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('taskReport') is not None:
            temp_model = main_models.GetAICoachDebugResultResponseBodyTaskReport()
            self.task_report = temp_model.from_map(m.get('taskReport'))

        return self

class GetAICoachDebugResultResponseBodyTaskReport(DaraModel):
    def __init__(
        self,
        deduction_rule: main_models.GetAICoachDebugResultResponseBodyTaskReportDeductionRule = None,
        expressiveness: main_models.GetAICoachDebugResultResponseBodyTaskReportExpressiveness = None,
        point: main_models.GetAICoachDebugResultResponseBodyTaskReportPoint = None,
    ):
        self.deduction_rule = deduction_rule
        self.expressiveness = expressiveness
        self.point = point

    def validate(self):
        if self.deduction_rule:
            self.deduction_rule.validate()
        if self.expressiveness:
            self.expressiveness.validate()
        if self.point:
            self.point.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deduction_rule is not None:
            result['deductionRule'] = self.deduction_rule.to_map()

        if self.expressiveness is not None:
            result['expressiveness'] = self.expressiveness.to_map()

        if self.point is not None:
            result['point'] = self.point.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deductionRule') is not None:
            temp_model = main_models.GetAICoachDebugResultResponseBodyTaskReportDeductionRule()
            self.deduction_rule = temp_model.from_map(m.get('deductionRule'))

        if m.get('expressiveness') is not None:
            temp_model = main_models.GetAICoachDebugResultResponseBodyTaskReportExpressiveness()
            self.expressiveness = temp_model.from_map(m.get('expressiveness'))

        if m.get('point') is not None:
            temp_model = main_models.GetAICoachDebugResultResponseBodyTaskReportPoint()
            self.point = temp_model.from_map(m.get('point'))

        return self

class GetAICoachDebugResultResponseBodyTaskReportPoint(DaraModel):
    def __init__(
        self,
        answer_list: List[main_models.GetAICoachDebugResultResponseBodyTaskReportPointAnswerList] = None,
        name: str = None,
    ):
        self.answer_list = answer_list
        self.name = name

    def validate(self):
        if self.answer_list:
            for v1 in self.answer_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['answerList'] = []
        if self.answer_list is not None:
            for k1 in self.answer_list:
                result['answerList'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.answer_list = []
        if m.get('answerList') is not None:
            for k1 in m.get('answerList'):
                temp_model = main_models.GetAICoachDebugResultResponseBodyTaskReportPointAnswerList()
                self.answer_list.append(temp_model.from_map(k1))

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class GetAICoachDebugResultResponseBodyTaskReportPointAnswerList(DaraModel):
    def __init__(
        self,
        reason: List[str] = None,
        status: int = None,
    ):
        self.reason = reason
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.reason is not None:
            result['reason'] = self.reason

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('reason') is not None:
            self.reason = m.get('reason')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

class GetAICoachDebugResultResponseBodyTaskReportExpressiveness(DaraModel):
    def __init__(
        self,
        name: str = None,
        reason: List[str] = None,
        score_rounds: int = None,
        status: str = None,
        total_rounds: int = None,
    ):
        self.name = name
        self.reason = reason
        self.score_rounds = score_rounds
        self.status = status
        self.total_rounds = total_rounds

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.reason is not None:
            result['reason'] = self.reason

        if self.score_rounds is not None:
            result['scoreRounds'] = self.score_rounds

        if self.status is not None:
            result['status'] = self.status

        if self.total_rounds is not None:
            result['totalRounds'] = self.total_rounds

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('reason') is not None:
            self.reason = m.get('reason')

        if m.get('scoreRounds') is not None:
            self.score_rounds = m.get('scoreRounds')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('totalRounds') is not None:
            self.total_rounds = m.get('totalRounds')

        return self

class GetAICoachDebugResultResponseBodyTaskReportDeductionRule(DaraModel):
    def __init__(
        self,
        hit: bool = None,
        name: str = None,
        reason: List[str] = None,
    ):
        self.hit = hit
        self.name = name
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hit is not None:
            result['hit'] = self.hit

        if self.name is not None:
            result['name'] = self.name

        if self.reason is not None:
            result['reason'] = self.reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hit') is not None:
            self.hit = m.get('hit')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('reason') is not None:
            self.reason = m.get('reason')

        return self

class GetAICoachDebugResultResponseBodyDialogueList(DaraModel):
    def __init__(
        self,
        message: str = None,
        role: str = None,
    ):
        self.message = message
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['message'] = self.message

        if self.role is not None:
            result['role'] = self.role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('role') is not None:
            self.role = m.get('role')

        return self

