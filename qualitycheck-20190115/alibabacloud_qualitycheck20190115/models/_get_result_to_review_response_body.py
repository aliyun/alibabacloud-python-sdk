# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_qualitycheck20190115 import models as main_models
from darabonba.model import DaraModel

class GetResultToReviewResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetResultToReviewResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
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

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetResultToReviewResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetResultToReviewResponseBodyData(DaraModel):
    def __init__(
        self,
        audio_scheme: str = None,
        audio_url: str = None,
        comments: str = None,
        dialogues: main_models.GetResultToReviewResponseBodyDataDialogues = None,
        file_id: str = None,
        file_merge_name: str = None,
        hit_rule_review_info_list: main_models.GetResultToReviewResponseBodyDataHitRuleReviewInfoList = None,
        manual_score_info_list: main_models.GetResultToReviewResponseBodyDataManualScoreInfoList = None,
        review_history_list: main_models.GetResultToReviewResponseBodyDataReviewHistoryList = None,
        review_type_id_list: main_models.GetResultToReviewResponseBodyDataReviewTypeIdList = None,
        status: int = None,
        total_score: int = None,
        vid: str = None,
    ):
        self.audio_scheme = audio_scheme
        self.audio_url = audio_url
        self.comments = comments
        self.dialogues = dialogues
        self.file_id = file_id
        self.file_merge_name = file_merge_name
        self.hit_rule_review_info_list = hit_rule_review_info_list
        self.manual_score_info_list = manual_score_info_list
        self.review_history_list = review_history_list
        self.review_type_id_list = review_type_id_list
        self.status = status
        self.total_score = total_score
        self.vid = vid

    def validate(self):
        if self.dialogues:
            self.dialogues.validate()
        if self.hit_rule_review_info_list:
            self.hit_rule_review_info_list.validate()
        if self.manual_score_info_list:
            self.manual_score_info_list.validate()
        if self.review_history_list:
            self.review_history_list.validate()
        if self.review_type_id_list:
            self.review_type_id_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio_scheme is not None:
            result['AudioScheme'] = self.audio_scheme

        if self.audio_url is not None:
            result['AudioURL'] = self.audio_url

        if self.comments is not None:
            result['Comments'] = self.comments

        if self.dialogues is not None:
            result['Dialogues'] = self.dialogues.to_map()

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.file_merge_name is not None:
            result['FileMergeName'] = self.file_merge_name

        if self.hit_rule_review_info_list is not None:
            result['HitRuleReviewInfoList'] = self.hit_rule_review_info_list.to_map()

        if self.manual_score_info_list is not None:
            result['ManualScoreInfoList'] = self.manual_score_info_list.to_map()

        if self.review_history_list is not None:
            result['ReviewHistoryList'] = self.review_history_list.to_map()

        if self.review_type_id_list is not None:
            result['ReviewTypeIdList'] = self.review_type_id_list.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.total_score is not None:
            result['TotalScore'] = self.total_score

        if self.vid is not None:
            result['Vid'] = self.vid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioScheme') is not None:
            self.audio_scheme = m.get('AudioScheme')

        if m.get('AudioURL') is not None:
            self.audio_url = m.get('AudioURL')

        if m.get('Comments') is not None:
            self.comments = m.get('Comments')

        if m.get('Dialogues') is not None:
            temp_model = main_models.GetResultToReviewResponseBodyDataDialogues()
            self.dialogues = temp_model.from_map(m.get('Dialogues'))

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('FileMergeName') is not None:
            self.file_merge_name = m.get('FileMergeName')

        if m.get('HitRuleReviewInfoList') is not None:
            temp_model = main_models.GetResultToReviewResponseBodyDataHitRuleReviewInfoList()
            self.hit_rule_review_info_list = temp_model.from_map(m.get('HitRuleReviewInfoList'))

        if m.get('ManualScoreInfoList') is not None:
            temp_model = main_models.GetResultToReviewResponseBodyDataManualScoreInfoList()
            self.manual_score_info_list = temp_model.from_map(m.get('ManualScoreInfoList'))

        if m.get('ReviewHistoryList') is not None:
            temp_model = main_models.GetResultToReviewResponseBodyDataReviewHistoryList()
            self.review_history_list = temp_model.from_map(m.get('ReviewHistoryList'))

        if m.get('ReviewTypeIdList') is not None:
            temp_model = main_models.GetResultToReviewResponseBodyDataReviewTypeIdList()
            self.review_type_id_list = temp_model.from_map(m.get('ReviewTypeIdList'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TotalScore') is not None:
            self.total_score = m.get('TotalScore')

        if m.get('Vid') is not None:
            self.vid = m.get('Vid')

        return self

class GetResultToReviewResponseBodyDataReviewTypeIdList(DaraModel):
    def __init__(
        self,
        review_type_id_list: List[main_models.GetResultToReviewResponseBodyDataReviewTypeIdListReviewTypeIdList] = None,
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
                temp_model = main_models.GetResultToReviewResponseBodyDataReviewTypeIdListReviewTypeIdList()
                self.review_type_id_list.append(temp_model.from_map(k1))

        return self

class GetResultToReviewResponseBodyDataReviewTypeIdListReviewTypeIdList(DaraModel):
    def __init__(
        self,
        review_key_id_list: main_models.GetResultToReviewResponseBodyDataReviewTypeIdListReviewTypeIdListReviewKeyIdList = None,
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
            temp_model = main_models.GetResultToReviewResponseBodyDataReviewTypeIdListReviewTypeIdListReviewKeyIdList()
            self.review_key_id_list = temp_model.from_map(m.get('ReviewKeyIdList'))

        if m.get('ReviewTypeId') is not None:
            self.review_type_id = m.get('ReviewTypeId')

        return self

class GetResultToReviewResponseBodyDataReviewTypeIdListReviewTypeIdListReviewKeyIdList(DaraModel):
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

class GetResultToReviewResponseBodyDataReviewHistoryList(DaraModel):
    def __init__(
        self,
        review_history: List[main_models.GetResultToReviewResponseBodyDataReviewHistoryListReviewHistory] = None,
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
                temp_model = main_models.GetResultToReviewResponseBodyDataReviewHistoryListReviewHistory()
                self.review_history.append(temp_model.from_map(k1))

        return self

class GetResultToReviewResponseBodyDataReviewHistoryListReviewHistory(DaraModel):
    def __init__(
        self,
        comments: str = None,
        complain_result: int = None,
        old_score: int = None,
        operator: int = None,
        operator_name: str = None,
        review_manager_type: str = None,
        review_result: int = None,
        review_right_rule: main_models.GetResultToReviewResponseBodyDataReviewHistoryListReviewHistoryReviewRightRule = None,
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
            temp_model = main_models.GetResultToReviewResponseBodyDataReviewHistoryListReviewHistoryReviewRightRule()
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

class GetResultToReviewResponseBodyDataReviewHistoryListReviewHistoryReviewRightRule(DaraModel):
    def __init__(
        self,
        review_right_rule: List[main_models.GetResultToReviewResponseBodyDataReviewHistoryListReviewHistoryReviewRightRuleReviewRightRule] = None,
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
                temp_model = main_models.GetResultToReviewResponseBodyDataReviewHistoryListReviewHistoryReviewRightRuleReviewRightRule()
                self.review_right_rule.append(temp_model.from_map(k1))

        return self

class GetResultToReviewResponseBodyDataReviewHistoryListReviewHistoryReviewRightRuleReviewRightRule(DaraModel):
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

class GetResultToReviewResponseBodyDataManualScoreInfoList(DaraModel):
    def __init__(
        self,
        manual_score_info: List[main_models.GetResultToReviewResponseBodyDataManualScoreInfoListManualScoreInfo] = None,
    ):
        self.manual_score_info = manual_score_info

    def validate(self):
        if self.manual_score_info:
            for v1 in self.manual_score_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ManualScoreInfo'] = []
        if self.manual_score_info is not None:
            for k1 in self.manual_score_info:
                result['ManualScoreInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.manual_score_info = []
        if m.get('ManualScoreInfo') is not None:
            for k1 in m.get('ManualScoreInfo'):
                temp_model = main_models.GetResultToReviewResponseBodyDataManualScoreInfoListManualScoreInfo()
                self.manual_score_info.append(temp_model.from_map(k1))

        return self

class GetResultToReviewResponseBodyDataManualScoreInfoListManualScoreInfo(DaraModel):
    def __init__(
        self,
        complain_histories: main_models.GetResultToReviewResponseBodyDataManualScoreInfoListManualScoreInfoComplainHistories = None,
        complainable: bool = None,
        score_id: int = None,
        score_num: int = None,
        score_sub_id: int = None,
        score_sub_name: str = None,
    ):
        self.complain_histories = complain_histories
        self.complainable = complainable
        self.score_id = score_id
        self.score_num = score_num
        self.score_sub_id = score_sub_id
        self.score_sub_name = score_sub_name

    def validate(self):
        if self.complain_histories:
            self.complain_histories.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.complain_histories is not None:
            result['ComplainHistories'] = self.complain_histories.to_map()

        if self.complainable is not None:
            result['Complainable'] = self.complainable

        if self.score_id is not None:
            result['ScoreId'] = self.score_id

        if self.score_num is not None:
            result['ScoreNum'] = self.score_num

        if self.score_sub_id is not None:
            result['ScoreSubId'] = self.score_sub_id

        if self.score_sub_name is not None:
            result['ScoreSubName'] = self.score_sub_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComplainHistories') is not None:
            temp_model = main_models.GetResultToReviewResponseBodyDataManualScoreInfoListManualScoreInfoComplainHistories()
            self.complain_histories = temp_model.from_map(m.get('ComplainHistories'))

        if m.get('Complainable') is not None:
            self.complainable = m.get('Complainable')

        if m.get('ScoreId') is not None:
            self.score_id = m.get('ScoreId')

        if m.get('ScoreNum') is not None:
            self.score_num = m.get('ScoreNum')

        if m.get('ScoreSubId') is not None:
            self.score_sub_id = m.get('ScoreSubId')

        if m.get('ScoreSubName') is not None:
            self.score_sub_name = m.get('ScoreSubName')

        return self

class GetResultToReviewResponseBodyDataManualScoreInfoListManualScoreInfoComplainHistories(DaraModel):
    def __init__(
        self,
        complain_histories: List[main_models.GetResultToReviewResponseBodyDataManualScoreInfoListManualScoreInfoComplainHistoriesComplainHistories] = None,
    ):
        self.complain_histories = complain_histories

    def validate(self):
        if self.complain_histories:
            for v1 in self.complain_histories:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ComplainHistories'] = []
        if self.complain_histories is not None:
            for k1 in self.complain_histories:
                result['ComplainHistories'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.complain_histories = []
        if m.get('ComplainHistories') is not None:
            for k1 in m.get('ComplainHistories'):
                temp_model = main_models.GetResultToReviewResponseBodyDataManualScoreInfoListManualScoreInfoComplainHistoriesComplainHistories()
                self.complain_histories.append(temp_model.from_map(k1))

        return self

class GetResultToReviewResponseBodyDataManualScoreInfoListManualScoreInfoComplainHistoriesComplainHistories(DaraModel):
    def __init__(
        self,
        comments: str = None,
        operation_time: str = None,
        operation_type: int = None,
        operator: int = None,
        operator_name: str = None,
    ):
        self.comments = comments
        self.operation_time = operation_time
        self.operation_type = operation_type
        self.operator = operator
        self.operator_name = operator_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comments is not None:
            result['Comments'] = self.comments

        if self.operation_time is not None:
            result['OperationTime'] = self.operation_time

        if self.operation_type is not None:
            result['OperationType'] = self.operation_type

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.operator_name is not None:
            result['OperatorName'] = self.operator_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')

        if m.get('OperationTime') is not None:
            self.operation_time = m.get('OperationTime')

        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('OperatorName') is not None:
            self.operator_name = m.get('OperatorName')

        return self

class GetResultToReviewResponseBodyDataHitRuleReviewInfoList(DaraModel):
    def __init__(
        self,
        hit_rule_review_info: List[main_models.GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfo] = None,
    ):
        self.hit_rule_review_info = hit_rule_review_info

    def validate(self):
        if self.hit_rule_review_info:
            for v1 in self.hit_rule_review_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['HitRuleReviewInfo'] = []
        if self.hit_rule_review_info is not None:
            for k1 in self.hit_rule_review_info:
                result['HitRuleReviewInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hit_rule_review_info = []
        if m.get('HitRuleReviewInfo') is not None:
            for k1 in m.get('HitRuleReviewInfo'):
                temp_model = main_models.GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfo()
                self.hit_rule_review_info.append(temp_model.from_map(k1))

        return self

class GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfo(DaraModel):
    def __init__(
        self,
        auto_review: int = None,
        complain_histories: main_models.GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoComplainHistories = None,
        complainable: bool = None,
        condition_hit_info_list: main_models.GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoList = None,
        machine_hit_result: int = None,
        review_hit_result: int = None,
        review_info: main_models.GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoReviewInfo = None,
        rid: int = None,
        rule_name: str = None,
        score_id: int = None,
        score_num: int = None,
        score_sub_id: int = None,
        score_sub_name: str = None,
    ):
        self.auto_review = auto_review
        self.complain_histories = complain_histories
        self.complainable = complainable
        self.condition_hit_info_list = condition_hit_info_list
        self.machine_hit_result = machine_hit_result
        self.review_hit_result = review_hit_result
        self.review_info = review_info
        self.rid = rid
        self.rule_name = rule_name
        self.score_id = score_id
        self.score_num = score_num
        self.score_sub_id = score_sub_id
        self.score_sub_name = score_sub_name

    def validate(self):
        if self.complain_histories:
            self.complain_histories.validate()
        if self.condition_hit_info_list:
            self.condition_hit_info_list.validate()
        if self.review_info:
            self.review_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_review is not None:
            result['AutoReview'] = self.auto_review

        if self.complain_histories is not None:
            result['ComplainHistories'] = self.complain_histories.to_map()

        if self.complainable is not None:
            result['Complainable'] = self.complainable

        if self.condition_hit_info_list is not None:
            result['ConditionHitInfoList'] = self.condition_hit_info_list.to_map()

        if self.machine_hit_result is not None:
            result['MachineHitResult'] = self.machine_hit_result

        if self.review_hit_result is not None:
            result['ReviewHitResult'] = self.review_hit_result

        if self.review_info is not None:
            result['ReviewInfo'] = self.review_info.to_map()

        if self.rid is not None:
            result['Rid'] = self.rid

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.score_id is not None:
            result['ScoreId'] = self.score_id

        if self.score_num is not None:
            result['ScoreNum'] = self.score_num

        if self.score_sub_id is not None:
            result['ScoreSubId'] = self.score_sub_id

        if self.score_sub_name is not None:
            result['ScoreSubName'] = self.score_sub_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoReview') is not None:
            self.auto_review = m.get('AutoReview')

        if m.get('ComplainHistories') is not None:
            temp_model = main_models.GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoComplainHistories()
            self.complain_histories = temp_model.from_map(m.get('ComplainHistories'))

        if m.get('Complainable') is not None:
            self.complainable = m.get('Complainable')

        if m.get('ConditionHitInfoList') is not None:
            temp_model = main_models.GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoList()
            self.condition_hit_info_list = temp_model.from_map(m.get('ConditionHitInfoList'))

        if m.get('MachineHitResult') is not None:
            self.machine_hit_result = m.get('MachineHitResult')

        if m.get('ReviewHitResult') is not None:
            self.review_hit_result = m.get('ReviewHitResult')

        if m.get('ReviewInfo') is not None:
            temp_model = main_models.GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoReviewInfo()
            self.review_info = temp_model.from_map(m.get('ReviewInfo'))

        if m.get('Rid') is not None:
            self.rid = m.get('Rid')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('ScoreId') is not None:
            self.score_id = m.get('ScoreId')

        if m.get('ScoreNum') is not None:
            self.score_num = m.get('ScoreNum')

        if m.get('ScoreSubId') is not None:
            self.score_sub_id = m.get('ScoreSubId')

        if m.get('ScoreSubName') is not None:
            self.score_sub_name = m.get('ScoreSubName')

        return self

class GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoReviewInfo(DaraModel):
    def __init__(
        self,
        comment: str = None,
        hit_id: str = None,
        review_result: int = None,
        review_time: str = None,
        reviewer: str = None,
        rid: int = None,
        sentence_review_results: main_models.GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoReviewInfoSentenceReviewResults = None,
    ):
        self.comment = comment
        self.hit_id = hit_id
        self.review_result = review_result
        self.review_time = review_time
        self.reviewer = reviewer
        self.rid = rid
        self.sentence_review_results = sentence_review_results

    def validate(self):
        if self.sentence_review_results:
            self.sentence_review_results.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.hit_id is not None:
            result['HitId'] = self.hit_id

        if self.review_result is not None:
            result['ReviewResult'] = self.review_result

        if self.review_time is not None:
            result['ReviewTime'] = self.review_time

        if self.reviewer is not None:
            result['Reviewer'] = self.reviewer

        if self.rid is not None:
            result['Rid'] = self.rid

        if self.sentence_review_results is not None:
            result['SentenceReviewResults'] = self.sentence_review_results.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('HitId') is not None:
            self.hit_id = m.get('HitId')

        if m.get('ReviewResult') is not None:
            self.review_result = m.get('ReviewResult')

        if m.get('ReviewTime') is not None:
            self.review_time = m.get('ReviewTime')

        if m.get('Reviewer') is not None:
            self.reviewer = m.get('Reviewer')

        if m.get('Rid') is not None:
            self.rid = m.get('Rid')

        if m.get('SentenceReviewResults') is not None:
            temp_model = main_models.GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoReviewInfoSentenceReviewResults()
            self.sentence_review_results = temp_model.from_map(m.get('SentenceReviewResults'))

        return self

class GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoReviewInfoSentenceReviewResults(DaraModel):
    def __init__(
        self,
        sentence_review_results: List[main_models.GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoReviewInfoSentenceReviewResultsSentenceReviewResults] = None,
    ):
        self.sentence_review_results = sentence_review_results

    def validate(self):
        if self.sentence_review_results:
            for v1 in self.sentence_review_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SentenceReviewResults'] = []
        if self.sentence_review_results is not None:
            for k1 in self.sentence_review_results:
                result['SentenceReviewResults'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sentence_review_results = []
        if m.get('SentenceReviewResults') is not None:
            for k1 in m.get('SentenceReviewResults'):
                temp_model = main_models.GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoReviewInfoSentenceReviewResultsSentenceReviewResults()
                self.sentence_review_results.append(temp_model.from_map(k1))

        return self

class GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoReviewInfoSentenceReviewResultsSentenceReviewResults(DaraModel):
    def __init__(
        self,
        changed: bool = None,
        cid: int = None,
        comment: str = None,
        hit_status: int = None,
        origin_task_id: str = None,
        origin_vid: str = None,
        pid: str = None,
        review_dimension_type: str = None,
        rid: int = None,
        sid: int = None,
    ):
        self.changed = changed
        self.cid = cid
        self.comment = comment
        self.hit_status = hit_status
        self.origin_task_id = origin_task_id
        self.origin_vid = origin_vid
        self.pid = pid
        self.review_dimension_type = review_dimension_type
        self.rid = rid
        self.sid = sid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.changed is not None:
            result['Changed'] = self.changed

        if self.cid is not None:
            result['Cid'] = self.cid

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.hit_status is not None:
            result['HitStatus'] = self.hit_status

        if self.origin_task_id is not None:
            result['OriginTaskId'] = self.origin_task_id

        if self.origin_vid is not None:
            result['OriginVid'] = self.origin_vid

        if self.pid is not None:
            result['Pid'] = self.pid

        if self.review_dimension_type is not None:
            result['ReviewDimensionType'] = self.review_dimension_type

        if self.rid is not None:
            result['Rid'] = self.rid

        if self.sid is not None:
            result['Sid'] = self.sid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Changed') is not None:
            self.changed = m.get('Changed')

        if m.get('Cid') is not None:
            self.cid = m.get('Cid')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('HitStatus') is not None:
            self.hit_status = m.get('HitStatus')

        if m.get('OriginTaskId') is not None:
            self.origin_task_id = m.get('OriginTaskId')

        if m.get('OriginVid') is not None:
            self.origin_vid = m.get('OriginVid')

        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        if m.get('ReviewDimensionType') is not None:
            self.review_dimension_type = m.get('ReviewDimensionType')

        if m.get('Rid') is not None:
            self.rid = m.get('Rid')

        if m.get('Sid') is not None:
            self.sid = m.get('Sid')

        return self

class GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoList(DaraModel):
    def __init__(
        self,
        condition_hit_info: List[main_models.GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfo] = None,
    ):
        self.condition_hit_info = condition_hit_info

    def validate(self):
        if self.condition_hit_info:
            for v1 in self.condition_hit_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ConditionHitInfo'] = []
        if self.condition_hit_info is not None:
            for k1 in self.condition_hit_info:
                result['ConditionHitInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.condition_hit_info = []
        if m.get('ConditionHitInfo') is not None:
            for k1 in m.get('ConditionHitInfo'):
                temp_model = main_models.GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfo()
                self.condition_hit_info.append(temp_model.from_map(k1))

        return self

class GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfo(DaraModel):
    def __init__(
        self,
        cid: main_models.GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoCid = None,
        key_words: main_models.GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoKeyWords = None,
        phrase: main_models.GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoPhrase = None,
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
            temp_model = main_models.GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoCid()
            self.cid = temp_model.from_map(m.get('Cid'))

        if m.get('KeyWords') is not None:
            temp_model = main_models.GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoKeyWords()
            self.key_words = temp_model.from_map(m.get('KeyWords'))

        if m.get('Phrase') is not None:
            temp_model = main_models.GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoPhrase()
            self.phrase = temp_model.from_map(m.get('Phrase'))

        return self

class GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoPhrase(DaraModel):
    def __init__(
        self,
        begin: int = None,
        emotion_value: int = None,
        end: int = None,
        identity: str = None,
        pid: int = None,
        role: str = None,
        words: str = None,
    ):
        self.begin = begin
        self.emotion_value = emotion_value
        self.end = end
        self.identity = identity
        self.pid = pid
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

        if self.identity is not None:
            result['Identity'] = self.identity

        if self.pid is not None:
            result['Pid'] = self.pid

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

        if m.get('Identity') is not None:
            self.identity = m.get('Identity')

        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('Words') is not None:
            self.words = m.get('Words')

        return self

class GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoKeyWords(DaraModel):
    def __init__(
        self,
        key_word: List[main_models.GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoKeyWordsKeyWord] = None,
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
                temp_model = main_models.GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoKeyWordsKeyWord()
                self.key_word.append(temp_model.from_map(k1))

        return self

class GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoKeyWordsKeyWord(DaraModel):
    def __init__(
        self,
        cid: str = None,
        customize_code: str = None,
        from_: int = None,
        is_match: bool = None,
        pid: int = None,
        tid: str = None,
        to: int = None,
        val: str = None,
    ):
        self.cid = cid
        self.customize_code = customize_code
        self.from_ = from_
        self.is_match = is_match
        self.pid = pid
        self.tid = tid
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

        if self.customize_code is not None:
            result['CustomizeCode'] = self.customize_code

        if self.from_ is not None:
            result['From'] = self.from_

        if self.is_match is not None:
            result['IsMatch'] = self.is_match

        if self.pid is not None:
            result['Pid'] = self.pid

        if self.tid is not None:
            result['Tid'] = self.tid

        if self.to is not None:
            result['To'] = self.to

        if self.val is not None:
            result['Val'] = self.val

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cid') is not None:
            self.cid = m.get('Cid')

        if m.get('CustomizeCode') is not None:
            self.customize_code = m.get('CustomizeCode')

        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('IsMatch') is not None:
            self.is_match = m.get('IsMatch')

        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        if m.get('To') is not None:
            self.to = m.get('To')

        if m.get('Val') is not None:
            self.val = m.get('Val')

        return self

class GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoCid(DaraModel):
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

class GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoComplainHistories(DaraModel):
    def __init__(
        self,
        complain_histories: List[main_models.GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoComplainHistoriesComplainHistories] = None,
    ):
        self.complain_histories = complain_histories

    def validate(self):
        if self.complain_histories:
            for v1 in self.complain_histories:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ComplainHistories'] = []
        if self.complain_histories is not None:
            for k1 in self.complain_histories:
                result['ComplainHistories'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.complain_histories = []
        if m.get('ComplainHistories') is not None:
            for k1 in m.get('ComplainHistories'):
                temp_model = main_models.GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoComplainHistoriesComplainHistories()
                self.complain_histories.append(temp_model.from_map(k1))

        return self

class GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoComplainHistoriesComplainHistories(DaraModel):
    def __init__(
        self,
        comments: str = None,
        operation_time: str = None,
        operation_type: int = None,
        operator: int = None,
        operator_name: str = None,
    ):
        self.comments = comments
        self.operation_time = operation_time
        self.operation_type = operation_type
        self.operator = operator
        self.operator_name = operator_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comments is not None:
            result['Comments'] = self.comments

        if self.operation_time is not None:
            result['OperationTime'] = self.operation_time

        if self.operation_type is not None:
            result['OperationType'] = self.operation_type

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.operator_name is not None:
            result['OperatorName'] = self.operator_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')

        if m.get('OperationTime') is not None:
            self.operation_time = m.get('OperationTime')

        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('OperatorName') is not None:
            self.operator_name = m.get('OperatorName')

        return self

class GetResultToReviewResponseBodyDataDialogues(DaraModel):
    def __init__(
        self,
        dialogue: List[main_models.GetResultToReviewResponseBodyDataDialoguesDialogue] = None,
    ):
        self.dialogue = dialogue

    def validate(self):
        if self.dialogue:
            for v1 in self.dialogue:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Dialogue'] = []
        if self.dialogue is not None:
            for k1 in self.dialogue:
                result['Dialogue'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dialogue = []
        if m.get('Dialogue') is not None:
            for k1 in m.get('Dialogue'):
                temp_model = main_models.GetResultToReviewResponseBodyDataDialoguesDialogue()
                self.dialogue.append(temp_model.from_map(k1))

        return self

class GetResultToReviewResponseBodyDataDialoguesDialogue(DaraModel):
    def __init__(
        self,
        begin: int = None,
        begin_time: str = None,
        begin_time_ms: int = None,
        emotion_value: int = None,
        end: int = None,
        hour_min_sec: str = None,
        identity: str = None,
        role: str = None,
        silence_duration: int = None,
        speech_rate: int = None,
        words: str = None,
    ):
        self.begin = begin
        self.begin_time = begin_time
        self.begin_time_ms = begin_time_ms
        self.emotion_value = emotion_value
        self.end = end
        self.hour_min_sec = hour_min_sec
        self.identity = identity
        self.role = role
        self.silence_duration = silence_duration
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

        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.begin_time_ms is not None:
            result['BeginTimeMs'] = self.begin_time_ms

        if self.emotion_value is not None:
            result['EmotionValue'] = self.emotion_value

        if self.end is not None:
            result['End'] = self.end

        if self.hour_min_sec is not None:
            result['HourMinSec'] = self.hour_min_sec

        if self.identity is not None:
            result['Identity'] = self.identity

        if self.role is not None:
            result['Role'] = self.role

        if self.silence_duration is not None:
            result['SilenceDuration'] = self.silence_duration

        if self.speech_rate is not None:
            result['SpeechRate'] = self.speech_rate

        if self.words is not None:
            result['Words'] = self.words

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')

        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('BeginTimeMs') is not None:
            self.begin_time_ms = m.get('BeginTimeMs')

        if m.get('EmotionValue') is not None:
            self.emotion_value = m.get('EmotionValue')

        if m.get('End') is not None:
            self.end = m.get('End')

        if m.get('HourMinSec') is not None:
            self.hour_min_sec = m.get('HourMinSec')

        if m.get('Identity') is not None:
            self.identity = m.get('Identity')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('SilenceDuration') is not None:
            self.silence_duration = m.get('SilenceDuration')

        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')

        if m.get('Words') is not None:
            self.words = m.get('Words')

        return self

