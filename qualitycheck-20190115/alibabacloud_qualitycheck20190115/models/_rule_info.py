# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_qualitycheck20190115 import models as main_models
from darabonba.model import DaraModel

class RuleInfo(DaraModel):
    def __init__(
        self,
        auto_review: int = None,
        business_category_name_list: List[str] = None,
        check_type: int = None,
        comments: str = None,
        config_type: int = None,
        create_emp_name: str = None,
        create_empid: str = None,
        create_time: str = None,
        deny: int = None,
        dialogues: List[main_models.RuleTestDialogue] = None,
        effective: int = None,
        effective_end_time: str = None,
        effective_start_time: str = None,
        end_time: str = None,
        external_property: int = None,
        full_cycle: int = None,
        graph_flow: Any = None,
        is_delete: int = None,
        is_online: int = None,
        lambda_: str = None,
        last_update_emp_name: str = None,
        last_update_empid: str = None,
        last_update_time: str = None,
        level: int = None,
        meet: int = None,
        modify_type: int = None,
        name: str = None,
        operation_mode: int = None,
        quality_check_type: int = None,
        rid: str = None,
        rule_category_name: str = None,
        rule_score_type: int = None,
        rule_type: int = None,
        scheme_check_type: main_models.SchemeCheckType = None,
        scheme_id: int = None,
        scheme_name: str = None,
        scheme_rule_mapping_id: int = None,
        score_deleted: bool = None,
        score_id: int = None,
        score_name: str = None,
        score_num: int = None,
        score_num_type: int = None,
        score_rule_hit_type: int = None,
        score_sub_id: int = None,
        score_sub_name: str = None,
        score_type: int = None,
        sort_index: int = None,
        start_time: str = None,
        status: int = None,
        target_type: int = None,
        task_flow_id: int = None,
        task_flow_type: int = None,
        triggers: List[str] = None,
        type: int = None,
        weight: str = None,
    ):
        self.auto_review = auto_review
        self.business_category_name_list = business_category_name_list
        self.check_type = check_type
        self.comments = comments
        self.config_type = config_type
        self.create_emp_name = create_emp_name
        self.create_empid = create_empid
        self.create_time = create_time
        self.deny = deny
        self.dialogues = dialogues
        self.effective = effective
        self.effective_end_time = effective_end_time
        self.effective_start_time = effective_start_time
        self.end_time = end_time
        self.external_property = external_property
        self.full_cycle = full_cycle
        self.graph_flow = graph_flow
        self.is_delete = is_delete
        self.is_online = is_online
        self.lambda_ = lambda_
        self.last_update_emp_name = last_update_emp_name
        self.last_update_empid = last_update_empid
        self.last_update_time = last_update_time
        self.level = level
        self.meet = meet
        self.modify_type = modify_type
        self.name = name
        self.operation_mode = operation_mode
        self.quality_check_type = quality_check_type
        self.rid = rid
        self.rule_category_name = rule_category_name
        self.rule_score_type = rule_score_type
        self.rule_type = rule_type
        self.scheme_check_type = scheme_check_type
        self.scheme_id = scheme_id
        self.scheme_name = scheme_name
        self.scheme_rule_mapping_id = scheme_rule_mapping_id
        self.score_deleted = score_deleted
        self.score_id = score_id
        self.score_name = score_name
        self.score_num = score_num
        self.score_num_type = score_num_type
        self.score_rule_hit_type = score_rule_hit_type
        self.score_sub_id = score_sub_id
        self.score_sub_name = score_sub_name
        self.score_type = score_type
        self.sort_index = sort_index
        self.start_time = start_time
        self.status = status
        self.target_type = target_type
        self.task_flow_id = task_flow_id
        self.task_flow_type = task_flow_type
        self.triggers = triggers
        self.type = type
        self.weight = weight

    def validate(self):
        if self.dialogues:
            for v1 in self.dialogues:
                 if v1:
                    v1.validate()
        if self.scheme_check_type:
            self.scheme_check_type.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_review is not None:
            result['AutoReview'] = self.auto_review

        if self.business_category_name_list is not None:
            result['BusinessCategoryNameList'] = self.business_category_name_list

        if self.check_type is not None:
            result['CheckType'] = self.check_type

        if self.comments is not None:
            result['Comments'] = self.comments

        if self.config_type is not None:
            result['ConfigType'] = self.config_type

        if self.create_emp_name is not None:
            result['CreateEmpName'] = self.create_emp_name

        if self.create_empid is not None:
            result['CreateEmpid'] = self.create_empid

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.deny is not None:
            result['Deny'] = self.deny

        result['Dialogues'] = []
        if self.dialogues is not None:
            for k1 in self.dialogues:
                result['Dialogues'].append(k1.to_map() if k1 else None)

        if self.effective is not None:
            result['Effective'] = self.effective

        if self.effective_end_time is not None:
            result['EffectiveEndTime'] = self.effective_end_time

        if self.effective_start_time is not None:
            result['EffectiveStartTime'] = self.effective_start_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.external_property is not None:
            result['ExternalProperty'] = self.external_property

        if self.full_cycle is not None:
            result['FullCycle'] = self.full_cycle

        if self.graph_flow is not None:
            result['GraphFlow'] = self.graph_flow

        if self.is_delete is not None:
            result['IsDelete'] = self.is_delete

        if self.is_online is not None:
            result['IsOnline'] = self.is_online

        if self.lambda_ is not None:
            result['Lambda'] = self.lambda_

        if self.last_update_emp_name is not None:
            result['LastUpdateEmpName'] = self.last_update_emp_name

        if self.last_update_empid is not None:
            result['LastUpdateEmpid'] = self.last_update_empid

        if self.last_update_time is not None:
            result['LastUpdateTime'] = self.last_update_time

        if self.level is not None:
            result['Level'] = self.level

        if self.meet is not None:
            result['Meet'] = self.meet

        if self.modify_type is not None:
            result['ModifyType'] = self.modify_type

        if self.name is not None:
            result['Name'] = self.name

        if self.operation_mode is not None:
            result['OperationMode'] = self.operation_mode

        if self.quality_check_type is not None:
            result['QualityCheckType'] = self.quality_check_type

        if self.rid is not None:
            result['Rid'] = self.rid

        if self.rule_category_name is not None:
            result['RuleCategoryName'] = self.rule_category_name

        if self.rule_score_type is not None:
            result['RuleScoreType'] = self.rule_score_type

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        if self.scheme_check_type is not None:
            result['SchemeCheckType'] = self.scheme_check_type.to_map()

        if self.scheme_id is not None:
            result['SchemeId'] = self.scheme_id

        if self.scheme_name is not None:
            result['SchemeName'] = self.scheme_name

        if self.scheme_rule_mapping_id is not None:
            result['SchemeRuleMappingId'] = self.scheme_rule_mapping_id

        if self.score_deleted is not None:
            result['ScoreDeleted'] = self.score_deleted

        if self.score_id is not None:
            result['ScoreId'] = self.score_id

        if self.score_name is not None:
            result['ScoreName'] = self.score_name

        if self.score_num is not None:
            result['ScoreNum'] = self.score_num

        if self.score_num_type is not None:
            result['ScoreNumType'] = self.score_num_type

        if self.score_rule_hit_type is not None:
            result['ScoreRuleHitType'] = self.score_rule_hit_type

        if self.score_sub_id is not None:
            result['ScoreSubId'] = self.score_sub_id

        if self.score_sub_name is not None:
            result['ScoreSubName'] = self.score_sub_name

        if self.score_type is not None:
            result['ScoreType'] = self.score_type

        if self.sort_index is not None:
            result['SortIndex'] = self.sort_index

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        if self.task_flow_id is not None:
            result['TaskFlowId'] = self.task_flow_id

        if self.task_flow_type is not None:
            result['TaskFlowType'] = self.task_flow_type

        if self.triggers is not None:
            result['Triggers'] = self.triggers

        if self.type is not None:
            result['Type'] = self.type

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoReview') is not None:
            self.auto_review = m.get('AutoReview')

        if m.get('BusinessCategoryNameList') is not None:
            self.business_category_name_list = m.get('BusinessCategoryNameList')

        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')

        if m.get('Comments') is not None:
            self.comments = m.get('Comments')

        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')

        if m.get('CreateEmpName') is not None:
            self.create_emp_name = m.get('CreateEmpName')

        if m.get('CreateEmpid') is not None:
            self.create_empid = m.get('CreateEmpid')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Deny') is not None:
            self.deny = m.get('Deny')

        self.dialogues = []
        if m.get('Dialogues') is not None:
            for k1 in m.get('Dialogues'):
                temp_model = main_models.RuleTestDialogue()
                self.dialogues.append(temp_model.from_map(k1))

        if m.get('Effective') is not None:
            self.effective = m.get('Effective')

        if m.get('EffectiveEndTime') is not None:
            self.effective_end_time = m.get('EffectiveEndTime')

        if m.get('EffectiveStartTime') is not None:
            self.effective_start_time = m.get('EffectiveStartTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ExternalProperty') is not None:
            self.external_property = m.get('ExternalProperty')

        if m.get('FullCycle') is not None:
            self.full_cycle = m.get('FullCycle')

        if m.get('GraphFlow') is not None:
            self.graph_flow = m.get('GraphFlow')

        if m.get('IsDelete') is not None:
            self.is_delete = m.get('IsDelete')

        if m.get('IsOnline') is not None:
            self.is_online = m.get('IsOnline')

        if m.get('Lambda') is not None:
            self.lambda_ = m.get('Lambda')

        if m.get('LastUpdateEmpName') is not None:
            self.last_update_emp_name = m.get('LastUpdateEmpName')

        if m.get('LastUpdateEmpid') is not None:
            self.last_update_empid = m.get('LastUpdateEmpid')

        if m.get('LastUpdateTime') is not None:
            self.last_update_time = m.get('LastUpdateTime')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Meet') is not None:
            self.meet = m.get('Meet')

        if m.get('ModifyType') is not None:
            self.modify_type = m.get('ModifyType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OperationMode') is not None:
            self.operation_mode = m.get('OperationMode')

        if m.get('QualityCheckType') is not None:
            self.quality_check_type = m.get('QualityCheckType')

        if m.get('Rid') is not None:
            self.rid = m.get('Rid')

        if m.get('RuleCategoryName') is not None:
            self.rule_category_name = m.get('RuleCategoryName')

        if m.get('RuleScoreType') is not None:
            self.rule_score_type = m.get('RuleScoreType')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        if m.get('SchemeCheckType') is not None:
            temp_model = main_models.SchemeCheckType()
            self.scheme_check_type = temp_model.from_map(m.get('SchemeCheckType'))

        if m.get('SchemeId') is not None:
            self.scheme_id = m.get('SchemeId')

        if m.get('SchemeName') is not None:
            self.scheme_name = m.get('SchemeName')

        if m.get('SchemeRuleMappingId') is not None:
            self.scheme_rule_mapping_id = m.get('SchemeRuleMappingId')

        if m.get('ScoreDeleted') is not None:
            self.score_deleted = m.get('ScoreDeleted')

        if m.get('ScoreId') is not None:
            self.score_id = m.get('ScoreId')

        if m.get('ScoreName') is not None:
            self.score_name = m.get('ScoreName')

        if m.get('ScoreNum') is not None:
            self.score_num = m.get('ScoreNum')

        if m.get('ScoreNumType') is not None:
            self.score_num_type = m.get('ScoreNumType')

        if m.get('ScoreRuleHitType') is not None:
            self.score_rule_hit_type = m.get('ScoreRuleHitType')

        if m.get('ScoreSubId') is not None:
            self.score_sub_id = m.get('ScoreSubId')

        if m.get('ScoreSubName') is not None:
            self.score_sub_name = m.get('ScoreSubName')

        if m.get('ScoreType') is not None:
            self.score_type = m.get('ScoreType')

        if m.get('SortIndex') is not None:
            self.sort_index = m.get('SortIndex')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        if m.get('TaskFlowId') is not None:
            self.task_flow_id = m.get('TaskFlowId')

        if m.get('TaskFlowType') is not None:
            self.task_flow_type = m.get('TaskFlowType')

        if m.get('Triggers') is not None:
            self.triggers = m.get('Triggers')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

