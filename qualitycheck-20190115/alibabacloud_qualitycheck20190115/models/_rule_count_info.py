# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_qualitycheck20190115 import models as main_models
from darabonba.model import DaraModel

class RuleCountInfo(DaraModel):
    def __init__(
        self,
        auto_review: int = None,
        business_category_basic_info_list: List[main_models.BusinessCategoryBasicInfo] = None,
        business_category_name_list: List[str] = None,
        business_range: List[int] = None,
        check_number: int = None,
        comments: str = None,
        create_emp_name: str = None,
        create_empid: str = None,
        create_time: str = None,
        deny: int = None,
        effective: int = None,
        effective_end_time: str = None,
        effective_start_time: str = None,
        end_time: str = None,
        full_cycle: int = None,
        graph_flow: Any = None,
        hit_number: int = None,
        hit_rate: float = None,
        hit_real_violation_rate: float = None,
        is_delete: int = None,
        is_select: bool = None,
        job_name: str = None,
        last_update_emp_name: str = None,
        last_update_empid: str = None,
        last_update_time: str = None,
        name: str = None,
        operation_mode: int = None,
        pre_review_number: int = None,
        problem_number: int = None,
        quality_check_type: int = None,
        real_violation_number: int = None,
        review_accuracy_rate: float = None,
        review_number: int = None,
        review_rate: float = None,
        review_status_name: str = None,
        rid: int = None,
        rule_score_single_type: int = None,
        rule_score_type: int = None,
        rule_type: int = None,
        score_sub_id: int = None,
        start_time: str = None,
        status: int = None,
        target_type: int = None,
        type: int = None,
        type_name: str = None,
        un_review_number: int = None,
        user_group: str = None,
    ):
        self.auto_review = auto_review
        self.business_category_basic_info_list = business_category_basic_info_list
        self.business_category_name_list = business_category_name_list
        self.business_range = business_range
        self.check_number = check_number
        self.comments = comments
        self.create_emp_name = create_emp_name
        self.create_empid = create_empid
        self.create_time = create_time
        self.deny = deny
        self.effective = effective
        self.effective_end_time = effective_end_time
        self.effective_start_time = effective_start_time
        self.end_time = end_time
        self.full_cycle = full_cycle
        self.graph_flow = graph_flow
        self.hit_number = hit_number
        self.hit_rate = hit_rate
        self.hit_real_violation_rate = hit_real_violation_rate
        self.is_delete = is_delete
        self.is_select = is_select
        self.job_name = job_name
        self.last_update_emp_name = last_update_emp_name
        self.last_update_empid = last_update_empid
        self.last_update_time = last_update_time
        self.name = name
        self.operation_mode = operation_mode
        self.pre_review_number = pre_review_number
        self.problem_number = problem_number
        self.quality_check_type = quality_check_type
        self.real_violation_number = real_violation_number
        self.review_accuracy_rate = review_accuracy_rate
        self.review_number = review_number
        self.review_rate = review_rate
        self.review_status_name = review_status_name
        self.rid = rid
        self.rule_score_single_type = rule_score_single_type
        self.rule_score_type = rule_score_type
        self.rule_type = rule_type
        self.score_sub_id = score_sub_id
        self.start_time = start_time
        self.status = status
        self.target_type = target_type
        self.type = type
        self.type_name = type_name
        self.un_review_number = un_review_number
        self.user_group = user_group

    def validate(self):
        if self.business_category_basic_info_list:
            for v1 in self.business_category_basic_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_review is not None:
            result['AutoReview'] = self.auto_review

        result['BusinessCategoryBasicInfoList'] = []
        if self.business_category_basic_info_list is not None:
            for k1 in self.business_category_basic_info_list:
                result['BusinessCategoryBasicInfoList'].append(k1.to_map() if k1 else None)

        if self.business_category_name_list is not None:
            result['BusinessCategoryNameList'] = self.business_category_name_list

        if self.business_range is not None:
            result['BusinessRange'] = self.business_range

        if self.check_number is not None:
            result['CheckNumber'] = self.check_number

        if self.comments is not None:
            result['Comments'] = self.comments

        if self.create_emp_name is not None:
            result['CreateEmpName'] = self.create_emp_name

        if self.create_empid is not None:
            result['CreateEmpid'] = self.create_empid

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.deny is not None:
            result['Deny'] = self.deny

        if self.effective is not None:
            result['Effective'] = self.effective

        if self.effective_end_time is not None:
            result['EffectiveEndTime'] = self.effective_end_time

        if self.effective_start_time is not None:
            result['EffectiveStartTime'] = self.effective_start_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.full_cycle is not None:
            result['FullCycle'] = self.full_cycle

        if self.graph_flow is not None:
            result['GraphFlow'] = self.graph_flow

        if self.hit_number is not None:
            result['HitNumber'] = self.hit_number

        if self.hit_rate is not None:
            result['HitRate'] = self.hit_rate

        if self.hit_real_violation_rate is not None:
            result['HitRealViolationRate'] = self.hit_real_violation_rate

        if self.is_delete is not None:
            result['IsDelete'] = self.is_delete

        if self.is_select is not None:
            result['IsSelect'] = self.is_select

        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.last_update_emp_name is not None:
            result['LastUpdateEmpName'] = self.last_update_emp_name

        if self.last_update_empid is not None:
            result['LastUpdateEmpid'] = self.last_update_empid

        if self.last_update_time is not None:
            result['LastUpdateTime'] = self.last_update_time

        if self.name is not None:
            result['Name'] = self.name

        if self.operation_mode is not None:
            result['OperationMode'] = self.operation_mode

        if self.pre_review_number is not None:
            result['PreReviewNumber'] = self.pre_review_number

        if self.problem_number is not None:
            result['ProblemNumber'] = self.problem_number

        if self.quality_check_type is not None:
            result['QualityCheckType'] = self.quality_check_type

        if self.real_violation_number is not None:
            result['RealViolationNumber'] = self.real_violation_number

        if self.review_accuracy_rate is not None:
            result['ReviewAccuracyRate'] = self.review_accuracy_rate

        if self.review_number is not None:
            result['ReviewNumber'] = self.review_number

        if self.review_rate is not None:
            result['ReviewRate'] = self.review_rate

        if self.review_status_name is not None:
            result['ReviewStatusName'] = self.review_status_name

        if self.rid is not None:
            result['Rid'] = self.rid

        if self.rule_score_single_type is not None:
            result['RuleScoreSingleType'] = self.rule_score_single_type

        if self.rule_score_type is not None:
            result['RuleScoreType'] = self.rule_score_type

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        if self.score_sub_id is not None:
            result['ScoreSubId'] = self.score_sub_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        if self.type is not None:
            result['Type'] = self.type

        if self.type_name is not None:
            result['TypeName'] = self.type_name

        if self.un_review_number is not None:
            result['UnReviewNumber'] = self.un_review_number

        if self.user_group is not None:
            result['UserGroup'] = self.user_group

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoReview') is not None:
            self.auto_review = m.get('AutoReview')

        self.business_category_basic_info_list = []
        if m.get('BusinessCategoryBasicInfoList') is not None:
            for k1 in m.get('BusinessCategoryBasicInfoList'):
                temp_model = main_models.BusinessCategoryBasicInfo()
                self.business_category_basic_info_list.append(temp_model.from_map(k1))

        if m.get('BusinessCategoryNameList') is not None:
            self.business_category_name_list = m.get('BusinessCategoryNameList')

        if m.get('BusinessRange') is not None:
            self.business_range = m.get('BusinessRange')

        if m.get('CheckNumber') is not None:
            self.check_number = m.get('CheckNumber')

        if m.get('Comments') is not None:
            self.comments = m.get('Comments')

        if m.get('CreateEmpName') is not None:
            self.create_emp_name = m.get('CreateEmpName')

        if m.get('CreateEmpid') is not None:
            self.create_empid = m.get('CreateEmpid')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Deny') is not None:
            self.deny = m.get('Deny')

        if m.get('Effective') is not None:
            self.effective = m.get('Effective')

        if m.get('EffectiveEndTime') is not None:
            self.effective_end_time = m.get('EffectiveEndTime')

        if m.get('EffectiveStartTime') is not None:
            self.effective_start_time = m.get('EffectiveStartTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('FullCycle') is not None:
            self.full_cycle = m.get('FullCycle')

        if m.get('GraphFlow') is not None:
            self.graph_flow = m.get('GraphFlow')

        if m.get('HitNumber') is not None:
            self.hit_number = m.get('HitNumber')

        if m.get('HitRate') is not None:
            self.hit_rate = m.get('HitRate')

        if m.get('HitRealViolationRate') is not None:
            self.hit_real_violation_rate = m.get('HitRealViolationRate')

        if m.get('IsDelete') is not None:
            self.is_delete = m.get('IsDelete')

        if m.get('IsSelect') is not None:
            self.is_select = m.get('IsSelect')

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('LastUpdateEmpName') is not None:
            self.last_update_emp_name = m.get('LastUpdateEmpName')

        if m.get('LastUpdateEmpid') is not None:
            self.last_update_empid = m.get('LastUpdateEmpid')

        if m.get('LastUpdateTime') is not None:
            self.last_update_time = m.get('LastUpdateTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OperationMode') is not None:
            self.operation_mode = m.get('OperationMode')

        if m.get('PreReviewNumber') is not None:
            self.pre_review_number = m.get('PreReviewNumber')

        if m.get('ProblemNumber') is not None:
            self.problem_number = m.get('ProblemNumber')

        if m.get('QualityCheckType') is not None:
            self.quality_check_type = m.get('QualityCheckType')

        if m.get('RealViolationNumber') is not None:
            self.real_violation_number = m.get('RealViolationNumber')

        if m.get('ReviewAccuracyRate') is not None:
            self.review_accuracy_rate = m.get('ReviewAccuracyRate')

        if m.get('ReviewNumber') is not None:
            self.review_number = m.get('ReviewNumber')

        if m.get('ReviewRate') is not None:
            self.review_rate = m.get('ReviewRate')

        if m.get('ReviewStatusName') is not None:
            self.review_status_name = m.get('ReviewStatusName')

        if m.get('Rid') is not None:
            self.rid = m.get('Rid')

        if m.get('RuleScoreSingleType') is not None:
            self.rule_score_single_type = m.get('RuleScoreSingleType')

        if m.get('RuleScoreType') is not None:
            self.rule_score_type = m.get('RuleScoreType')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        if m.get('ScoreSubId') is not None:
            self.score_sub_id = m.get('ScoreSubId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')

        if m.get('UnReviewNumber') is not None:
            self.un_review_number = m.get('UnReviewNumber')

        if m.get('UserGroup') is not None:
            self.user_group = m.get('UserGroup')

        return self

