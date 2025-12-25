# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_qualitycheck20190115 import models as main_models
from darabonba.model import DaraModel

class GetResultResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        count: int = None,
        data: main_models.GetResultResponseBodyData = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        result_count_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.count = count
        self.data = data
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.result_count_id = result_count_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.count is not None:
            result['Count'] = self.count

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_count_id is not None:
            result['ResultCountId'] = self.result_count_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Data') is not None:
            temp_model = main_models.GetResultResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultCountId') is not None:
            self.result_count_id = m.get('ResultCountId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetResultResponseBodyData(DaraModel):
    def __init__(
        self,
        result_info: List[main_models.GetResultResponseBodyDataResultInfo] = None,
    ):
        self.result_info = result_info

    def validate(self):
        if self.result_info:
            for v1 in self.result_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ResultInfo'] = []
        if self.result_info is not None:
            for k1 in self.result_info:
                result['ResultInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result_info = []
        if m.get('ResultInfo') is not None:
            for k1 in m.get('ResultInfo'):
                temp_model = main_models.GetResultResponseBodyDataResultInfo()
                self.result_info.append(temp_model.from_map(k1))

        return self

class GetResultResponseBodyDataResultInfo(DaraModel):
    def __init__(
        self,
        agent: main_models.GetResultResponseBodyDataResultInfoAgent = None,
        asr_result: main_models.GetResultResponseBodyDataResultInfoAsrResult = None,
        assignment_time: str = None,
        comments: str = None,
        create_time: str = None,
        create_time_long: str = None,
        error_message: str = None,
        hit_result: main_models.GetResultResponseBodyDataResultInfoHitResult = None,
        hit_score: main_models.GetResultResponseBodyDataResultInfoHitScore = None,
        last_data_id: str = None,
        recording: main_models.GetResultResponseBodyDataResultInfoRecording = None,
        resolver: str = None,
        review_history_list: main_models.GetResultResponseBodyDataResultInfoReviewHistoryList = None,
        review_result: int = None,
        review_status: int = None,
        review_time: str = None,
        review_time_long: str = None,
        review_type: int = None,
        review_type_id_list: main_models.GetResultResponseBodyDataResultInfoReviewTypeIdList = None,
        reviewer: str = None,
        scheme_id_list: main_models.GetResultResponseBodyDataResultInfoSchemeIdList = None,
        scheme_name_list: main_models.GetResultResponseBodyDataResultInfoSchemeNameList = None,
        score: int = None,
        status: int = None,
        task_id: str = None,
        task_name: str = None,
        vid: str = None,
    ):
        self.agent = agent
        self.asr_result = asr_result
        self.assignment_time = assignment_time
        self.comments = comments
        self.create_time = create_time
        self.create_time_long = create_time_long
        self.error_message = error_message
        self.hit_result = hit_result
        self.hit_score = hit_score
        self.last_data_id = last_data_id
        self.recording = recording
        self.resolver = resolver
        self.review_history_list = review_history_list
        self.review_result = review_result
        self.review_status = review_status
        self.review_time = review_time
        self.review_time_long = review_time_long
        self.review_type = review_type
        self.review_type_id_list = review_type_id_list
        self.reviewer = reviewer
        self.scheme_id_list = scheme_id_list
        self.scheme_name_list = scheme_name_list
        self.score = score
        self.status = status
        self.task_id = task_id
        self.task_name = task_name
        self.vid = vid

    def validate(self):
        if self.agent:
            self.agent.validate()
        if self.asr_result:
            self.asr_result.validate()
        if self.hit_result:
            self.hit_result.validate()
        if self.hit_score:
            self.hit_score.validate()
        if self.recording:
            self.recording.validate()
        if self.review_history_list:
            self.review_history_list.validate()
        if self.review_type_id_list:
            self.review_type_id_list.validate()
        if self.scheme_id_list:
            self.scheme_id_list.validate()
        if self.scheme_name_list:
            self.scheme_name_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent is not None:
            result['Agent'] = self.agent.to_map()

        if self.asr_result is not None:
            result['AsrResult'] = self.asr_result.to_map()

        if self.assignment_time is not None:
            result['AssignmentTime'] = self.assignment_time

        if self.comments is not None:
            result['Comments'] = self.comments

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_time_long is not None:
            result['CreateTimeLong'] = self.create_time_long

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.hit_result is not None:
            result['HitResult'] = self.hit_result.to_map()

        if self.hit_score is not None:
            result['HitScore'] = self.hit_score.to_map()

        if self.last_data_id is not None:
            result['LastDataId'] = self.last_data_id

        if self.recording is not None:
            result['Recording'] = self.recording.to_map()

        if self.resolver is not None:
            result['Resolver'] = self.resolver

        if self.review_history_list is not None:
            result['ReviewHistoryList'] = self.review_history_list.to_map()

        if self.review_result is not None:
            result['ReviewResult'] = self.review_result

        if self.review_status is not None:
            result['ReviewStatus'] = self.review_status

        if self.review_time is not None:
            result['ReviewTime'] = self.review_time

        if self.review_time_long is not None:
            result['ReviewTimeLong'] = self.review_time_long

        if self.review_type is not None:
            result['ReviewType'] = self.review_type

        if self.review_type_id_list is not None:
            result['ReviewTypeIdList'] = self.review_type_id_list.to_map()

        if self.reviewer is not None:
            result['Reviewer'] = self.reviewer

        if self.scheme_id_list is not None:
            result['SchemeIdList'] = self.scheme_id_list.to_map()

        if self.scheme_name_list is not None:
            result['SchemeNameList'] = self.scheme_name_list.to_map()

        if self.score is not None:
            result['Score'] = self.score

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.vid is not None:
            result['Vid'] = self.vid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Agent') is not None:
            temp_model = main_models.GetResultResponseBodyDataResultInfoAgent()
            self.agent = temp_model.from_map(m.get('Agent'))

        if m.get('AsrResult') is not None:
            temp_model = main_models.GetResultResponseBodyDataResultInfoAsrResult()
            self.asr_result = temp_model.from_map(m.get('AsrResult'))

        if m.get('AssignmentTime') is not None:
            self.assignment_time = m.get('AssignmentTime')

        if m.get('Comments') is not None:
            self.comments = m.get('Comments')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateTimeLong') is not None:
            self.create_time_long = m.get('CreateTimeLong')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('HitResult') is not None:
            temp_model = main_models.GetResultResponseBodyDataResultInfoHitResult()
            self.hit_result = temp_model.from_map(m.get('HitResult'))

        if m.get('HitScore') is not None:
            temp_model = main_models.GetResultResponseBodyDataResultInfoHitScore()
            self.hit_score = temp_model.from_map(m.get('HitScore'))

        if m.get('LastDataId') is not None:
            self.last_data_id = m.get('LastDataId')

        if m.get('Recording') is not None:
            temp_model = main_models.GetResultResponseBodyDataResultInfoRecording()
            self.recording = temp_model.from_map(m.get('Recording'))

        if m.get('Resolver') is not None:
            self.resolver = m.get('Resolver')

        if m.get('ReviewHistoryList') is not None:
            temp_model = main_models.GetResultResponseBodyDataResultInfoReviewHistoryList()
            self.review_history_list = temp_model.from_map(m.get('ReviewHistoryList'))

        if m.get('ReviewResult') is not None:
            self.review_result = m.get('ReviewResult')

        if m.get('ReviewStatus') is not None:
            self.review_status = m.get('ReviewStatus')

        if m.get('ReviewTime') is not None:
            self.review_time = m.get('ReviewTime')

        if m.get('ReviewTimeLong') is not None:
            self.review_time_long = m.get('ReviewTimeLong')

        if m.get('ReviewType') is not None:
            self.review_type = m.get('ReviewType')

        if m.get('ReviewTypeIdList') is not None:
            temp_model = main_models.GetResultResponseBodyDataResultInfoReviewTypeIdList()
            self.review_type_id_list = temp_model.from_map(m.get('ReviewTypeIdList'))

        if m.get('Reviewer') is not None:
            self.reviewer = m.get('Reviewer')

        if m.get('SchemeIdList') is not None:
            temp_model = main_models.GetResultResponseBodyDataResultInfoSchemeIdList()
            self.scheme_id_list = temp_model.from_map(m.get('SchemeIdList'))

        if m.get('SchemeNameList') is not None:
            temp_model = main_models.GetResultResponseBodyDataResultInfoSchemeNameList()
            self.scheme_name_list = temp_model.from_map(m.get('SchemeNameList'))

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('Vid') is not None:
            self.vid = m.get('Vid')

        return self

class GetResultResponseBodyDataResultInfoSchemeNameList(DaraModel):
    def __init__(
        self,
        scheme_name_list: List[str] = None,
    ):
        self.scheme_name_list = scheme_name_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.scheme_name_list is not None:
            result['SchemeNameList'] = self.scheme_name_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SchemeNameList') is not None:
            self.scheme_name_list = m.get('SchemeNameList')

        return self

class GetResultResponseBodyDataResultInfoSchemeIdList(DaraModel):
    def __init__(
        self,
        scheme_id_list: List[int] = None,
    ):
        self.scheme_id_list = scheme_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.scheme_id_list is not None:
            result['SchemeIdList'] = self.scheme_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SchemeIdList') is not None:
            self.scheme_id_list = m.get('SchemeIdList')

        return self

class GetResultResponseBodyDataResultInfoReviewTypeIdList(DaraModel):
    def __init__(
        self,
        review_type_id_list: List[main_models.GetResultResponseBodyDataResultInfoReviewTypeIdListReviewTypeIdList] = None,
    ):
        self.review_type_id_list = review_type_id_list

    def validate(self):
        if self.review_type_id_list:
            for v1 in self.review_type_id_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ReviewTypeIdList'] = []
        if self.review_type_id_list is not None:
            for k1 in self.review_type_id_list:
                result['ReviewTypeIdList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.review_type_id_list = []
        if m.get('ReviewTypeIdList') is not None:
            for k1 in m.get('ReviewTypeIdList'):
                temp_model = main_models.GetResultResponseBodyDataResultInfoReviewTypeIdListReviewTypeIdList()
                self.review_type_id_list.append(temp_model.from_map(k1))

        return self

class GetResultResponseBodyDataResultInfoReviewTypeIdListReviewTypeIdList(DaraModel):
    def __init__(
        self,
        review_key_id_list: main_models.GetResultResponseBodyDataResultInfoReviewTypeIdListReviewTypeIdListReviewKeyIdList = None,
        review_type_id: int = None,
    ):
        self.review_key_id_list = review_key_id_list
        self.review_type_id = review_type_id

    def validate(self):
        if self.review_key_id_list:
            self.review_key_id_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.review_key_id_list is not None:
            result['ReviewKeyIdList'] = self.review_key_id_list.to_map()

        if self.review_type_id is not None:
            result['ReviewTypeId'] = self.review_type_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReviewKeyIdList') is not None:
            temp_model = main_models.GetResultResponseBodyDataResultInfoReviewTypeIdListReviewTypeIdListReviewKeyIdList()
            self.review_key_id_list = temp_model.from_map(m.get('ReviewKeyIdList'))

        if m.get('ReviewTypeId') is not None:
            self.review_type_id = m.get('ReviewTypeId')

        return self

class GetResultResponseBodyDataResultInfoReviewTypeIdListReviewTypeIdListReviewKeyIdList(DaraModel):
    def __init__(
        self,
        review_key_id_list: List[int] = None,
    ):
        self.review_key_id_list = review_key_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.review_key_id_list is not None:
            result['ReviewKeyIdList'] = self.review_key_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReviewKeyIdList') is not None:
            self.review_key_id_list = m.get('ReviewKeyIdList')

        return self

class GetResultResponseBodyDataResultInfoReviewHistoryList(DaraModel):
    def __init__(
        self,
        review_history: List[main_models.GetResultResponseBodyDataResultInfoReviewHistoryListReviewHistory] = None,
    ):
        self.review_history = review_history

    def validate(self):
        if self.review_history:
            for v1 in self.review_history:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ReviewHistory'] = []
        if self.review_history is not None:
            for k1 in self.review_history:
                result['ReviewHistory'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.review_history = []
        if m.get('ReviewHistory') is not None:
            for k1 in m.get('ReviewHistory'):
                temp_model = main_models.GetResultResponseBodyDataResultInfoReviewHistoryListReviewHistory()
                self.review_history.append(temp_model.from_map(k1))

        return self

class GetResultResponseBodyDataResultInfoReviewHistoryListReviewHistory(DaraModel):
    def __init__(
        self,
        comments: str = None,
        complain_result: int = None,
        old_score: int = None,
        operator: int = None,
        operator_name: str = None,
        review_manager_type: str = None,
        review_result: int = None,
        review_right_rule: main_models.GetResultResponseBodyDataResultInfoReviewHistoryListReviewHistoryReviewRightRule = None,
        score: int = None,
        time: int = None,
        time_str: str = None,
        type: int = None,
    ):
        self.comments = comments
        self.complain_result = complain_result
        self.old_score = old_score
        self.operator = operator
        self.operator_name = operator_name
        self.review_manager_type = review_manager_type
        self.review_result = review_result
        self.review_right_rule = review_right_rule
        self.score = score
        self.time = time
        self.time_str = time_str
        self.type = type

    def validate(self):
        if self.review_right_rule:
            self.review_right_rule.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comments is not None:
            result['Comments'] = self.comments

        if self.complain_result is not None:
            result['ComplainResult'] = self.complain_result

        if self.old_score is not None:
            result['OldScore'] = self.old_score

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.operator_name is not None:
            result['OperatorName'] = self.operator_name

        if self.review_manager_type is not None:
            result['ReviewManagerType'] = self.review_manager_type

        if self.review_result is not None:
            result['ReviewResult'] = self.review_result

        if self.review_right_rule is not None:
            result['ReviewRightRule'] = self.review_right_rule.to_map()

        if self.score is not None:
            result['Score'] = self.score

        if self.time is not None:
            result['Time'] = self.time

        if self.time_str is not None:
            result['TimeStr'] = self.time_str

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')

        if m.get('ComplainResult') is not None:
            self.complain_result = m.get('ComplainResult')

        if m.get('OldScore') is not None:
            self.old_score = m.get('OldScore')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('OperatorName') is not None:
            self.operator_name = m.get('OperatorName')

        if m.get('ReviewManagerType') is not None:
            self.review_manager_type = m.get('ReviewManagerType')

        if m.get('ReviewResult') is not None:
            self.review_result = m.get('ReviewResult')

        if m.get('ReviewRightRule') is not None:
            temp_model = main_models.GetResultResponseBodyDataResultInfoReviewHistoryListReviewHistoryReviewRightRule()
            self.review_right_rule = temp_model.from_map(m.get('ReviewRightRule'))

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('TimeStr') is not None:
            self.time_str = m.get('TimeStr')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetResultResponseBodyDataResultInfoReviewHistoryListReviewHistoryReviewRightRule(DaraModel):
    def __init__(
        self,
        review_right_rule: List[main_models.GetResultResponseBodyDataResultInfoReviewHistoryListReviewHistoryReviewRightRuleReviewRightRule] = None,
    ):
        self.review_right_rule = review_right_rule

    def validate(self):
        if self.review_right_rule:
            for v1 in self.review_right_rule:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ReviewRightRule'] = []
        if self.review_right_rule is not None:
            for k1 in self.review_right_rule:
                result['ReviewRightRule'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.review_right_rule = []
        if m.get('ReviewRightRule') is not None:
            for k1 in m.get('ReviewRightRule'):
                temp_model = main_models.GetResultResponseBodyDataResultInfoReviewHistoryListReviewHistoryReviewRightRuleReviewRightRule()
                self.review_right_rule.append(temp_model.from_map(k1))

        return self

class GetResultResponseBodyDataResultInfoReviewHistoryListReviewHistoryReviewRightRuleReviewRightRule(DaraModel):
    def __init__(
        self,
        rid: int = None,
        rule_name: str = None,
    ):
        self.rid = rid
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rid is not None:
            result['rid'] = self.rid

        if self.rule_name is not None:
            result['ruleName'] = self.rule_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('rid') is not None:
            self.rid = m.get('rid')

        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')

        return self

class GetResultResponseBodyDataResultInfoRecording(DaraModel):
    def __init__(
        self,
        business: str = None,
        call_id: str = None,
        call_time: str = None,
        call_type: int = None,
        callee: str = None,
        caller: str = None,
        customer_name: str = None,
        data_set_name: str = None,
        dialogue_size: int = None,
        duration: int = None,
        id: str = None,
        name: str = None,
        primary_id: str = None,
        remark_1: str = None,
        remark_10: str = None,
        remark_11: str = None,
        remark_12: str = None,
        remark_13: str = None,
        remark_2: str = None,
        remark_3: str = None,
        remark_4: str = None,
        remark_5: int = None,
        remark_6: str = None,
        remark_7: str = None,
        remark_8: str = None,
        remark_9: str = None,
        task_config_id: int = None,
        task_config_name: str = None,
        url: str = None,
    ):
        self.business = business
        self.call_id = call_id
        self.call_time = call_time
        self.call_type = call_type
        self.callee = callee
        self.caller = caller
        self.customer_name = customer_name
        self.data_set_name = data_set_name
        self.dialogue_size = dialogue_size
        self.duration = duration
        self.id = id
        self.name = name
        self.primary_id = primary_id
        self.remark_1 = remark_1
        self.remark_10 = remark_10
        self.remark_11 = remark_11
        self.remark_12 = remark_12
        self.remark_13 = remark_13
        self.remark_2 = remark_2
        self.remark_3 = remark_3
        self.remark_4 = remark_4
        self.remark_5 = remark_5
        self.remark_6 = remark_6
        self.remark_7 = remark_7
        self.remark_8 = remark_8
        self.remark_9 = remark_9
        self.task_config_id = task_config_id
        self.task_config_name = task_config_name
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business is not None:
            result['Business'] = self.business

        if self.call_id is not None:
            result['CallId'] = self.call_id

        if self.call_time is not None:
            result['CallTime'] = self.call_time

        if self.call_type is not None:
            result['CallType'] = self.call_type

        if self.callee is not None:
            result['Callee'] = self.callee

        if self.caller is not None:
            result['Caller'] = self.caller

        if self.customer_name is not None:
            result['CustomerName'] = self.customer_name

        if self.data_set_name is not None:
            result['DataSetName'] = self.data_set_name

        if self.dialogue_size is not None:
            result['DialogueSize'] = self.dialogue_size

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.primary_id is not None:
            result['PrimaryId'] = self.primary_id

        if self.remark_1 is not None:
            result['Remark1'] = self.remark_1

        if self.remark_10 is not None:
            result['Remark10'] = self.remark_10

        if self.remark_11 is not None:
            result['Remark11'] = self.remark_11

        if self.remark_12 is not None:
            result['Remark12'] = self.remark_12

        if self.remark_13 is not None:
            result['Remark13'] = self.remark_13

        if self.remark_2 is not None:
            result['Remark2'] = self.remark_2

        if self.remark_3 is not None:
            result['Remark3'] = self.remark_3

        if self.remark_4 is not None:
            result['Remark4'] = self.remark_4

        if self.remark_5 is not None:
            result['Remark5'] = self.remark_5

        if self.remark_6 is not None:
            result['Remark6'] = self.remark_6

        if self.remark_7 is not None:
            result['Remark7'] = self.remark_7

        if self.remark_8 is not None:
            result['Remark8'] = self.remark_8

        if self.remark_9 is not None:
            result['Remark9'] = self.remark_9

        if self.task_config_id is not None:
            result['TaskConfigId'] = self.task_config_id

        if self.task_config_name is not None:
            result['TaskConfigName'] = self.task_config_name

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Business') is not None:
            self.business = m.get('Business')

        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')

        if m.get('CallTime') is not None:
            self.call_time = m.get('CallTime')

        if m.get('CallType') is not None:
            self.call_type = m.get('CallType')

        if m.get('Callee') is not None:
            self.callee = m.get('Callee')

        if m.get('Caller') is not None:
            self.caller = m.get('Caller')

        if m.get('CustomerName') is not None:
            self.customer_name = m.get('CustomerName')

        if m.get('DataSetName') is not None:
            self.data_set_name = m.get('DataSetName')

        if m.get('DialogueSize') is not None:
            self.dialogue_size = m.get('DialogueSize')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PrimaryId') is not None:
            self.primary_id = m.get('PrimaryId')

        if m.get('Remark1') is not None:
            self.remark_1 = m.get('Remark1')

        if m.get('Remark10') is not None:
            self.remark_10 = m.get('Remark10')

        if m.get('Remark11') is not None:
            self.remark_11 = m.get('Remark11')

        if m.get('Remark12') is not None:
            self.remark_12 = m.get('Remark12')

        if m.get('Remark13') is not None:
            self.remark_13 = m.get('Remark13')

        if m.get('Remark2') is not None:
            self.remark_2 = m.get('Remark2')

        if m.get('Remark3') is not None:
            self.remark_3 = m.get('Remark3')

        if m.get('Remark4') is not None:
            self.remark_4 = m.get('Remark4')

        if m.get('Remark5') is not None:
            self.remark_5 = m.get('Remark5')

        if m.get('Remark6') is not None:
            self.remark_6 = m.get('Remark6')

        if m.get('Remark7') is not None:
            self.remark_7 = m.get('Remark7')

        if m.get('Remark8') is not None:
            self.remark_8 = m.get('Remark8')

        if m.get('Remark9') is not None:
            self.remark_9 = m.get('Remark9')

        if m.get('TaskConfigId') is not None:
            self.task_config_id = m.get('TaskConfigId')

        if m.get('TaskConfigName') is not None:
            self.task_config_name = m.get('TaskConfigName')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class GetResultResponseBodyDataResultInfoHitScore(DaraModel):
    def __init__(
        self,
        hit_score: List[main_models.GetResultResponseBodyDataResultInfoHitScoreHitScore] = None,
    ):
        self.hit_score = hit_score

    def validate(self):
        if self.hit_score:
            for v1 in self.hit_score:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['HitScore'] = []
        if self.hit_score is not None:
            for k1 in self.hit_score:
                result['HitScore'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hit_score = []
        if m.get('HitScore') is not None:
            for k1 in m.get('HitScore'):
                temp_model = main_models.GetResultResponseBodyDataResultInfoHitScoreHitScore()
                self.hit_score.append(temp_model.from_map(k1))

        return self

class GetResultResponseBodyDataResultInfoHitScoreHitScore(DaraModel):
    def __init__(
        self,
        rule_id: str = None,
        score_id: str = None,
        score_name: str = None,
        score_number: str = None,
    ):
        self.rule_id = rule_id
        self.score_id = score_id
        self.score_name = score_name
        self.score_number = score_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.score_id is not None:
            result['ScoreId'] = self.score_id

        if self.score_name is not None:
            result['ScoreName'] = self.score_name

        if self.score_number is not None:
            result['ScoreNumber'] = self.score_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('ScoreId') is not None:
            self.score_id = m.get('ScoreId')

        if m.get('ScoreName') is not None:
            self.score_name = m.get('ScoreName')

        if m.get('ScoreNumber') is not None:
            self.score_number = m.get('ScoreNumber')

        return self

class GetResultResponseBodyDataResultInfoHitResult(DaraModel):
    def __init__(
        self,
        hit_result: List[main_models.GetResultResponseBodyDataResultInfoHitResultHitResult] = None,
    ):
        self.hit_result = hit_result

    def validate(self):
        if self.hit_result:
            for v1 in self.hit_result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['HitResult'] = []
        if self.hit_result is not None:
            for k1 in self.hit_result:
                result['HitResult'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hit_result = []
        if m.get('HitResult') is not None:
            for k1 in m.get('HitResult'):
                temp_model = main_models.GetResultResponseBodyDataResultInfoHitResultHitResult()
                self.hit_result.append(temp_model.from_map(k1))

        return self

class GetResultResponseBodyDataResultInfoHitResultHitResult(DaraModel):
    def __init__(
        self,
        conditions: main_models.GetResultResponseBodyDataResultInfoHitResultHitResultConditions = None,
        hits: main_models.GetResultResponseBodyDataResultInfoHitResultHitResultHits = None,
        name: str = None,
        review_result: int = None,
        rid: str = None,
        scheme_id: int = None,
        scheme_version: int = None,
        score: int = None,
        type: str = None,
    ):
        self.conditions = conditions
        self.hits = hits
        self.name = name
        self.review_result = review_result
        self.rid = rid
        self.scheme_id = scheme_id
        self.scheme_version = scheme_version
        self.score = score
        self.type = type

    def validate(self):
        if self.conditions:
            self.conditions.validate()
        if self.hits:
            self.hits.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conditions is not None:
            result['Conditions'] = self.conditions.to_map()

        if self.hits is not None:
            result['Hits'] = self.hits.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.review_result is not None:
            result['ReviewResult'] = self.review_result

        if self.rid is not None:
            result['Rid'] = self.rid

        if self.scheme_id is not None:
            result['SchemeId'] = self.scheme_id

        if self.scheme_version is not None:
            result['SchemeVersion'] = self.scheme_version

        if self.score is not None:
            result['Score'] = self.score

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Conditions') is not None:
            temp_model = main_models.GetResultResponseBodyDataResultInfoHitResultHitResultConditions()
            self.conditions = temp_model.from_map(m.get('Conditions'))

        if m.get('Hits') is not None:
            temp_model = main_models.GetResultResponseBodyDataResultInfoHitResultHitResultHits()
            self.hits = temp_model.from_map(m.get('Hits'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ReviewResult') is not None:
            self.review_result = m.get('ReviewResult')

        if m.get('Rid') is not None:
            self.rid = m.get('Rid')

        if m.get('SchemeId') is not None:
            self.scheme_id = m.get('SchemeId')

        if m.get('SchemeVersion') is not None:
            self.scheme_version = m.get('SchemeVersion')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetResultResponseBodyDataResultInfoHitResultHitResultHits(DaraModel):
    def __init__(
        self,
        hit: List[main_models.GetResultResponseBodyDataResultInfoHitResultHitResultHitsHit] = None,
    ):
        self.hit = hit

    def validate(self):
        if self.hit:
            for v1 in self.hit:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Hit'] = []
        if self.hit is not None:
            for k1 in self.hit:
                result['Hit'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hit = []
        if m.get('Hit') is not None:
            for k1 in m.get('Hit'):
                temp_model = main_models.GetResultResponseBodyDataResultInfoHitResultHitResultHitsHit()
                self.hit.append(temp_model.from_map(k1))

        return self

class GetResultResponseBodyDataResultInfoHitResultHitResultHitsHit(DaraModel):
    def __init__(
        self,
        cid: main_models.GetResultResponseBodyDataResultInfoHitResultHitResultHitsHitCid = None,
        key_words: main_models.GetResultResponseBodyDataResultInfoHitResultHitResultHitsHitKeyWords = None,
        phrase: main_models.GetResultResponseBodyDataResultInfoHitResultHitResultHitsHitPhrase = None,
    ):
        self.cid = cid
        self.key_words = key_words
        self.phrase = phrase

    def validate(self):
        if self.cid:
            self.cid.validate()
        if self.key_words:
            self.key_words.validate()
        if self.phrase:
            self.phrase.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cid is not None:
            result['Cid'] = self.cid.to_map()

        if self.key_words is not None:
            result['KeyWords'] = self.key_words.to_map()

        if self.phrase is not None:
            result['Phrase'] = self.phrase.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cid') is not None:
            temp_model = main_models.GetResultResponseBodyDataResultInfoHitResultHitResultHitsHitCid()
            self.cid = temp_model.from_map(m.get('Cid'))

        if m.get('KeyWords') is not None:
            temp_model = main_models.GetResultResponseBodyDataResultInfoHitResultHitResultHitsHitKeyWords()
            self.key_words = temp_model.from_map(m.get('KeyWords'))

        if m.get('Phrase') is not None:
            temp_model = main_models.GetResultResponseBodyDataResultInfoHitResultHitResultHitsHitPhrase()
            self.phrase = temp_model.from_map(m.get('Phrase'))

        return self

class GetResultResponseBodyDataResultInfoHitResultHitResultHitsHitPhrase(DaraModel):
    def __init__(
        self,
        begin: int = None,
        emotion_value: int = None,
        end: int = None,
        role: str = None,
        words: str = None,
    ):
        self.begin = begin
        self.emotion_value = emotion_value
        self.end = end
        self.role = role
        self.words = words

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin is not None:
            result['Begin'] = self.begin

        if self.emotion_value is not None:
            result['EmotionValue'] = self.emotion_value

        if self.end is not None:
            result['End'] = self.end

        if self.role is not None:
            result['Role'] = self.role

        if self.words is not None:
            result['Words'] = self.words

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')

        if m.get('EmotionValue') is not None:
            self.emotion_value = m.get('EmotionValue')

        if m.get('End') is not None:
            self.end = m.get('End')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('Words') is not None:
            self.words = m.get('Words')

        return self

class GetResultResponseBodyDataResultInfoHitResultHitResultHitsHitKeyWords(DaraModel):
    def __init__(
        self,
        key_word: List[main_models.GetResultResponseBodyDataResultInfoHitResultHitResultHitsHitKeyWordsKeyWord] = None,
    ):
        self.key_word = key_word

    def validate(self):
        if self.key_word:
            for v1 in self.key_word:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['KeyWord'] = []
        if self.key_word is not None:
            for k1 in self.key_word:
                result['KeyWord'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.key_word = []
        if m.get('KeyWord') is not None:
            for k1 in m.get('KeyWord'):
                temp_model = main_models.GetResultResponseBodyDataResultInfoHitResultHitResultHitsHitKeyWordsKeyWord()
                self.key_word.append(temp_model.from_map(k1))

        return self

class GetResultResponseBodyDataResultInfoHitResultHitResultHitsHitKeyWordsKeyWord(DaraModel):
    def __init__(
        self,
        cid: str = None,
        from_: int = None,
        to: int = None,
        val: str = None,
    ):
        self.cid = cid
        self.from_ = from_
        self.to = to
        self.val = val

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cid is not None:
            result['Cid'] = self.cid

        if self.from_ is not None:
            result['From'] = self.from_

        if self.to is not None:
            result['To'] = self.to

        if self.val is not None:
            result['Val'] = self.val

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cid') is not None:
            self.cid = m.get('Cid')

        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('To') is not None:
            self.to = m.get('To')

        if m.get('Val') is not None:
            self.val = m.get('Val')

        return self

class GetResultResponseBodyDataResultInfoHitResultHitResultHitsHitCid(DaraModel):
    def __init__(
        self,
        cid: List[str] = None,
    ):
        self.cid = cid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cid is not None:
            result['Cid'] = self.cid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cid') is not None:
            self.cid = m.get('Cid')

        return self

class GetResultResponseBodyDataResultInfoHitResultHitResultConditions(DaraModel):
    def __init__(
        self,
        conditions: List[main_models.GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditions] = None,
    ):
        self.conditions = conditions

    def validate(self):
        if self.conditions:
            for v1 in self.conditions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Conditions'] = []
        if self.conditions is not None:
            for k1 in self.conditions:
                result['Conditions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conditions = []
        if m.get('Conditions') is not None:
            for k1 in m.get('Conditions'):
                temp_model = main_models.GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditions()
                self.conditions.append(temp_model.from_map(k1))

        return self

class GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditions(DaraModel):
    def __init__(
        self,
        check_range: main_models.GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsCheckRange = None,
        cid: str = None,
        exclusion: int = None,
        id: int = None,
        lambda_: str = None,
        operators: main_models.GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsOperators = None,
        rid: str = None,
    ):
        # 检测范围
        self.check_range = check_range
        # 条件id，可能是db中的主键，也可能是转换成的a, b, c
        self.cid = cid
        # 排除
        self.exclusion = exclusion
        # 在db中的主键
        self.id = id
        # Lambda表达式：例如:a&&b
        self.lambda_ = lambda_
        # 算子列表
        self.operators = operators
        # 条件所属的规则id
        self.rid = rid

    def validate(self):
        if self.check_range:
            self.check_range.validate()
        if self.operators:
            self.operators.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_range is not None:
            result['Check_range'] = self.check_range.to_map()

        if self.cid is not None:
            result['Cid'] = self.cid

        if self.exclusion is not None:
            result['Exclusion'] = self.exclusion

        if self.id is not None:
            result['Id'] = self.id

        if self.lambda_ is not None:
            result['Lambda'] = self.lambda_

        if self.operators is not None:
            result['Operators'] = self.operators.to_map()

        if self.rid is not None:
            result['Rid'] = self.rid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Check_range') is not None:
            temp_model = main_models.GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsCheckRange()
            self.check_range = temp_model.from_map(m.get('Check_range'))

        if m.get('Cid') is not None:
            self.cid = m.get('Cid')

        if m.get('Exclusion') is not None:
            self.exclusion = m.get('Exclusion')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Lambda') is not None:
            self.lambda_ = m.get('Lambda')

        if m.get('Operators') is not None:
            temp_model = main_models.GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsOperators()
            self.operators = temp_model.from_map(m.get('Operators'))

        if m.get('Rid') is not None:
            self.rid = m.get('Rid')

        return self

class GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsOperators(DaraModel):
    def __init__(
        self,
        operator: List[main_models.GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsOperatorsOperator] = None,
    ):
        self.operator = operator

    def validate(self):
        if self.operator:
            for v1 in self.operator:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Operator'] = []
        if self.operator is not None:
            for k1 in self.operator:
                result['Operator'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.operator = []
        if m.get('Operator') is not None:
            for k1 in m.get('Operator'):
                temp_model = main_models.GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsOperatorsOperator()
                self.operator.append(temp_model.from_map(k1))

        return self

class GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsOperatorsOperator(DaraModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
        oid: str = None,
        param: main_models.GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsOperatorsOperatorParam = None,
        type: str = None,
    ):
        # 主键id
        self.id = id
        # 算子名
        self.name = name
        # 可能是主键id，也可能是前端生成的id
        self.oid = oid
        # 算子参数
        self.param = param
        # 算子类别
        self.type = type

    def validate(self):
        if self.param:
            self.param.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.oid is not None:
            result['Oid'] = self.oid

        if self.param is not None:
            result['Param'] = self.param.to_map()

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Oid') is not None:
            self.oid = m.get('Oid')

        if m.get('Param') is not None:
            temp_model = main_models.GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsOperatorsOperatorParam()
            self.param = temp_model.from_map(m.get('Param'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsOperatorsOperatorParam(DaraModel):
    def __init__(
        self,
        average: bool = None,
        begin_type: str = None,
        case_sensitive: bool = None,
        check_first_sentence: bool = None,
        check_type: int = None,
        compare_operator: str = None,
        context_chat_match: bool = None,
        delay_time: int = None,
        end_type: str = None,
        excludes: main_models.GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsOperatorsOperatorParamExcludes = None,
        flow_node_prerequisite_param: main_models.GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsOperatorsOperatorParamFlowNodePrerequisiteParam = None,
        from_: int = None,
        from_end: bool = None,
        hit_time: int = None,
        in_sentence: bool = None,
        intent_model_check_parm: main_models.GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsOperatorsOperatorParamIntentModelCheckParm = None,
        interval: int = None,
        interval_end: int = None,
        keyword_extension: int = None,
        keyword_match_size: int = None,
        keywords: main_models.GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsOperatorsOperatorParamKeywords = None,
        max_emotion_change_value: int = None,
        min_word_size: int = None,
        near_dialogue: bool = None,
        not_regex: str = None,
        phrase: str = None,
        regex: str = None,
        target: int = None,
        threshold: float = None,
    ):
        # 语速检测，是否计算整个对话平均语速，默认false
        self.average = average
        # 时长算子，时长计算开始类型，录音开始，还是某句对话开始
        self.begin_type = begin_type
        # 区分大小写
        self.case_sensitive = case_sensitive
        # 静音检测：要不要检测第一句话
        self.check_first_sentence = check_first_sentence
        # 检测方式，1 相邻句能量波动 2 最大能量跨度 默认1
        self.check_type = check_type
        # 大于，还是小于，gt/lt
        self.compare_operator = compare_operator
        # 是否单句话匹配；
        self.context_chat_match = context_chat_match
        # 抢话算子 延时时长
        self.delay_time = delay_time
        # 时长算子，时长计算结束类型，录音结束，还是某句对话结束
        self.end_type = end_type
        # 上下文重复算子：排除掉某些对话
        self.excludes = excludes
        # 流程节点前置条件参数
        self.flow_node_prerequisite_param = flow_node_prerequisite_param
        # 上下文重复算子：检测当前句的前from句是否有重复；0表示前面的所有句
        self.from_ = from_
        # from_end
        self.from_end = from_end
        # 上下文重复算子：重复几次
        self.hit_time = hit_time
        # 生效句子， true单个句子，false多个句子
        self.in_sentence = in_sentence
        # 意图模型检查参数
        self.intent_model_check_parm = intent_model_check_parm
        # interval代表区间范围开始
        self.interval = interval
        # intervalEnd 代表区间范围结束
        self.interval_end = interval_end
        # 关键字扩展
        self.keyword_extension = keyword_extension
        # 匹配到的关键字数量
        self.keyword_match_size = keyword_match_size
        # 关键词
        self.keywords = keywords
        # 能量值变化，默认3, 1~9
        self.max_emotion_change_value = max_emotion_change_value
        # 句子中最少字数，小于此字数的句子不检查
        self.min_word_size = min_word_size
        # true表示取不同角色相邻的两句话，false表示取不同角色的第一句话比较响应时间（默认）
        self.near_dialogue = near_dialogue
        # 排除的正则表达式
        self.not_regex = not_regex
        # 语句
        self.phrase = phrase
        # 正则表达式
        self.regex = regex
        # target
        self.target = target
        # 阈值
        self.threshold = threshold

    def validate(self):
        if self.excludes:
            self.excludes.validate()
        if self.flow_node_prerequisite_param:
            self.flow_node_prerequisite_param.validate()
        if self.intent_model_check_parm:
            self.intent_model_check_parm.validate()
        if self.keywords:
            self.keywords.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.average is not None:
            result['Average'] = self.average

        if self.begin_type is not None:
            result['BeginType'] = self.begin_type

        if self.case_sensitive is not None:
            result['Case_sensitive'] = self.case_sensitive

        if self.check_first_sentence is not None:
            result['CheckFirstSentence'] = self.check_first_sentence

        if self.check_type is not None:
            result['CheckType'] = self.check_type

        if self.compare_operator is not None:
            result['CompareOperator'] = self.compare_operator

        if self.context_chat_match is not None:
            result['ContextChatMatch'] = self.context_chat_match

        if self.delay_time is not None:
            result['DelayTime'] = self.delay_time

        if self.end_type is not None:
            result['EndType'] = self.end_type

        if self.excludes is not None:
            result['Excludes'] = self.excludes.to_map()

        if self.flow_node_prerequisite_param is not None:
            result['FlowNodePrerequisiteParam'] = self.flow_node_prerequisite_param.to_map()

        if self.from_ is not None:
            result['From'] = self.from_

        if self.from_end is not None:
            result['From_end'] = self.from_end

        if self.hit_time is not None:
            result['Hit_time'] = self.hit_time

        if self.in_sentence is not None:
            result['In_sentence'] = self.in_sentence

        if self.intent_model_check_parm is not None:
            result['IntentModelCheckParm'] = self.intent_model_check_parm.to_map()

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.interval_end is not None:
            result['IntervalEnd'] = self.interval_end

        if self.keyword_extension is not None:
            result['KeywordExtension'] = self.keyword_extension

        if self.keyword_match_size is not None:
            result['KeywordMatchSize'] = self.keyword_match_size

        if self.keywords is not None:
            result['Keywords'] = self.keywords.to_map()

        if self.max_emotion_change_value is not None:
            result['MaxEmotionChangeValue'] = self.max_emotion_change_value

        if self.min_word_size is not None:
            result['MinWordSize'] = self.min_word_size

        if self.near_dialogue is not None:
            result['Near_dialogue'] = self.near_dialogue

        if self.not_regex is not None:
            result['NotRegex'] = self.not_regex

        if self.phrase is not None:
            result['Phrase'] = self.phrase

        if self.regex is not None:
            result['Regex'] = self.regex

        if self.target is not None:
            result['Target'] = self.target

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Average') is not None:
            self.average = m.get('Average')

        if m.get('BeginType') is not None:
            self.begin_type = m.get('BeginType')

        if m.get('Case_sensitive') is not None:
            self.case_sensitive = m.get('Case_sensitive')

        if m.get('CheckFirstSentence') is not None:
            self.check_first_sentence = m.get('CheckFirstSentence')

        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')

        if m.get('CompareOperator') is not None:
            self.compare_operator = m.get('CompareOperator')

        if m.get('ContextChatMatch') is not None:
            self.context_chat_match = m.get('ContextChatMatch')

        if m.get('DelayTime') is not None:
            self.delay_time = m.get('DelayTime')

        if m.get('EndType') is not None:
            self.end_type = m.get('EndType')

        if m.get('Excludes') is not None:
            temp_model = main_models.GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsOperatorsOperatorParamExcludes()
            self.excludes = temp_model.from_map(m.get('Excludes'))

        if m.get('FlowNodePrerequisiteParam') is not None:
            temp_model = main_models.GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsOperatorsOperatorParamFlowNodePrerequisiteParam()
            self.flow_node_prerequisite_param = temp_model.from_map(m.get('FlowNodePrerequisiteParam'))

        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('From_end') is not None:
            self.from_end = m.get('From_end')

        if m.get('Hit_time') is not None:
            self.hit_time = m.get('Hit_time')

        if m.get('In_sentence') is not None:
            self.in_sentence = m.get('In_sentence')

        if m.get('IntentModelCheckParm') is not None:
            temp_model = main_models.GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsOperatorsOperatorParamIntentModelCheckParm()
            self.intent_model_check_parm = temp_model.from_map(m.get('IntentModelCheckParm'))

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('IntervalEnd') is not None:
            self.interval_end = m.get('IntervalEnd')

        if m.get('KeywordExtension') is not None:
            self.keyword_extension = m.get('KeywordExtension')

        if m.get('KeywordMatchSize') is not None:
            self.keyword_match_size = m.get('KeywordMatchSize')

        if m.get('Keywords') is not None:
            temp_model = main_models.GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsOperatorsOperatorParamKeywords()
            self.keywords = temp_model.from_map(m.get('Keywords'))

        if m.get('MaxEmotionChangeValue') is not None:
            self.max_emotion_change_value = m.get('MaxEmotionChangeValue')

        if m.get('MinWordSize') is not None:
            self.min_word_size = m.get('MinWordSize')

        if m.get('Near_dialogue') is not None:
            self.near_dialogue = m.get('Near_dialogue')

        if m.get('NotRegex') is not None:
            self.not_regex = m.get('NotRegex')

        if m.get('Phrase') is not None:
            self.phrase = m.get('Phrase')

        if m.get('Regex') is not None:
            self.regex = m.get('Regex')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        return self

class GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsOperatorsOperatorParamKeywords(DaraModel):
    def __init__(
        self,
        keyword: List[str] = None,
    ):
        self.keyword = keyword

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keyword is not None:
            result['Keyword'] = self.keyword

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        return self

class GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsOperatorsOperatorParamIntentModelCheckParm(DaraModel):
    def __init__(
        self,
        intents: main_models.GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsOperatorsOperatorParamIntentModelCheckParmIntents = None,
        model_scene: str = None,
    ):
        # 引用的意图模型
        self.intents = intents
        # 模型应用的场景 AGENT:客户场景、CUSTOMER:客服场景 (CUSTOMER: 客户场景, AGENT: 坐席场景)
        self.model_scene = model_scene

    def validate(self):
        if self.intents:
            self.intents.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.intents is not None:
            result['Intents'] = self.intents.to_map()

        if self.model_scene is not None:
            result['ModelScene'] = self.model_scene

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Intents') is not None:
            temp_model = main_models.GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsOperatorsOperatorParamIntentModelCheckParmIntents()
            self.intents = temp_model.from_map(m.get('Intents'))

        if m.get('ModelScene') is not None:
            self.model_scene = m.get('ModelScene')

        return self

class GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsOperatorsOperatorParamIntentModelCheckParmIntents(DaraModel):
    def __init__(
        self,
        intent: List[main_models.GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsOperatorsOperatorParamIntentModelCheckParmIntentsIntent] = None,
    ):
        self.intent = intent

    def validate(self):
        if self.intent:
            for v1 in self.intent:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Intent'] = []
        if self.intent is not None:
            for k1 in self.intent:
                result['Intent'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.intent = []
        if m.get('Intent') is not None:
            for k1 in m.get('Intent'):
                temp_model = main_models.GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsOperatorsOperatorParamIntentModelCheckParmIntentsIntent()
                self.intent.append(temp_model.from_map(k1))

        return self

class GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsOperatorsOperatorParamIntentModelCheckParmIntentsIntent(DaraModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
    ):
        # 意图模型ID
        self.id = id
        # 意图模型名称
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsOperatorsOperatorParamFlowNodePrerequisiteParam(DaraModel):
    def __init__(
        self,
        node_id: int = None,
        node_match_status: int = None,
        node_name: str = None,
    ):
        # 节点id
        self.node_id = node_id
        # 节点匹配状态。
        self.node_match_status = node_match_status
        # 冗余的节点名称
        self.node_name = node_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_match_status is not None:
            result['NodeMatchStatus'] = self.node_match_status

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeMatchStatus') is not None:
            self.node_match_status = m.get('NodeMatchStatus')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        return self

class GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsOperatorsOperatorParamExcludes(DaraModel):
    def __init__(
        self,
        exclude: List[str] = None,
    ):
        self.exclude = exclude

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exclude is not None:
            result['Exclude'] = self.exclude

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Exclude') is not None:
            self.exclude = m.get('Exclude')

        return self

class GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsCheckRange(DaraModel):
    def __init__(
        self,
        absolute: bool = None,
        all_sentences_satisfy: bool = None,
        anchor: main_models.GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsCheckRangeAnchor = None,
        range: main_models.GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsCheckRangeRange = None,
        role: str = None,
        role_id: int = None,
        time_range: main_models.GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsCheckRangeTimeRange = None,
    ):
        # false: 相对位置; 会结合anchor以及角色来决定句子位置
        self.absolute = absolute
        # true: 每句话都必须满足条件；
        self.all_sentences_satisfy = all_sentences_satisfy
        # 前置后置条件
        self.anchor = anchor
        # 相对范围
        self.range = range
        # 对应 RoleType.type
        self.role = role
        # 对应 RoleType.id
        self.role_id = role_id
        self.time_range = time_range

    def validate(self):
        if self.anchor:
            self.anchor.validate()
        if self.range:
            self.range.validate()
        if self.time_range:
            self.time_range.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.absolute is not None:
            result['Absolute'] = self.absolute

        if self.all_sentences_satisfy is not None:
            result['AllSentencesSatisfy'] = self.all_sentences_satisfy

        if self.anchor is not None:
            result['Anchor'] = self.anchor.to_map()

        if self.range is not None:
            result['Range'] = self.range.to_map()

        if self.role is not None:
            result['Role'] = self.role

        if self.role_id is not None:
            result['RoleId'] = self.role_id

        if self.time_range is not None:
            result['TimeRange'] = self.time_range.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Absolute') is not None:
            self.absolute = m.get('Absolute')

        if m.get('AllSentencesSatisfy') is not None:
            self.all_sentences_satisfy = m.get('AllSentencesSatisfy')

        if m.get('Anchor') is not None:
            temp_model = main_models.GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsCheckRangeAnchor()
            self.anchor = temp_model.from_map(m.get('Anchor'))

        if m.get('Range') is not None:
            temp_model = main_models.GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsCheckRangeRange()
            self.range = temp_model.from_map(m.get('Range'))

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')

        if m.get('TimeRange') is not None:
            temp_model = main_models.GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsCheckRangeTimeRange()
            self.time_range = temp_model.from_map(m.get('TimeRange'))

        return self

class GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsCheckRangeTimeRange(DaraModel):
    def __init__(
        self,
        from_: int = None,
        to: int = None,
    ):
        self.from_ = from_
        self.to = to

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_ is not None:
            result['From'] = self.from_

        if self.to is not None:
            result['To'] = self.to

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('To') is not None:
            self.to = m.get('To')

        return self

class GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsCheckRangeRange(DaraModel):
    def __init__(
        self,
        from_: int = None,
        to: int = None,
    ):
        # 对话开始索引
        self.from_ = from_
        # 对话结束索引
        self.to = to

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_ is not None:
            result['From'] = self.from_

        if self.to is not None:
            result['To'] = self.to

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('To') is not None:
            self.to = m.get('To')

        return self

class GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsCheckRangeAnchor(DaraModel):
    def __init__(
        self,
        cid: str = None,
        hit_time: int = None,
        location: str = None,
    ):
        # 条件ID
        self.cid = cid
        # 命中次数
        self.hit_time = hit_time
        # 位置
        self.location = location

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cid is not None:
            result['Cid'] = self.cid

        if self.hit_time is not None:
            result['Hit_time'] = self.hit_time

        if self.location is not None:
            result['Location'] = self.location

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cid') is not None:
            self.cid = m.get('Cid')

        if m.get('Hit_time') is not None:
            self.hit_time = m.get('Hit_time')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        return self

class GetResultResponseBodyDataResultInfoAsrResult(DaraModel):
    def __init__(
        self,
        asr_result: List[main_models.GetResultResponseBodyDataResultInfoAsrResultAsrResult] = None,
    ):
        self.asr_result = asr_result

    def validate(self):
        if self.asr_result:
            for v1 in self.asr_result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AsrResult'] = []
        if self.asr_result is not None:
            for k1 in self.asr_result:
                result['AsrResult'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.asr_result = []
        if m.get('AsrResult') is not None:
            for k1 in m.get('AsrResult'):
                temp_model = main_models.GetResultResponseBodyDataResultInfoAsrResultAsrResult()
                self.asr_result.append(temp_model.from_map(k1))

        return self

class GetResultResponseBodyDataResultInfoAsrResultAsrResult(DaraModel):
    def __init__(
        self,
        begin: int = None,
        emotion_value: int = None,
        end: int = None,
        identity: str = None,
        role: str = None,
        speech_rate: int = None,
        words: str = None,
    ):
        self.begin = begin
        self.emotion_value = emotion_value
        self.end = end
        self.identity = identity
        self.role = role
        self.speech_rate = speech_rate
        self.words = words

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin is not None:
            result['Begin'] = self.begin

        if self.emotion_value is not None:
            result['EmotionValue'] = self.emotion_value

        if self.end is not None:
            result['End'] = self.end

        if self.identity is not None:
            result['Identity'] = self.identity

        if self.role is not None:
            result['Role'] = self.role

        if self.speech_rate is not None:
            result['SpeechRate'] = self.speech_rate

        if self.words is not None:
            result['Words'] = self.words

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')

        if m.get('EmotionValue') is not None:
            self.emotion_value = m.get('EmotionValue')

        if m.get('End') is not None:
            self.end = m.get('End')

        if m.get('Identity') is not None:
            self.identity = m.get('Identity')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')

        if m.get('Words') is not None:
            self.words = m.get('Words')

        return self

class GetResultResponseBodyDataResultInfoAgent(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        skill_group: str = None,
    ):
        self.id = id
        self.name = name
        self.skill_group = skill_group

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.skill_group is not None:
            result['SkillGroup'] = self.skill_group

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SkillGroup') is not None:
            self.skill_group = m.get('SkillGroup')

        return self

