# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_qualitycheck20190115 import models as main_models
from darabonba.model import DaraModel

class SchemeCheckType(DaraModel):
    def __init__(
        self,
        check_name: str = None,
        check_type: int = None,
        enable: int = None,
        scheme_id: int = None,
        scheme_score_info_list: List[main_models.SchemeCheckTypeSchemeScoreInfoList] = None,
        score: int = None,
        source_score: int = None,
        task_flow_score_info_list: List[main_models.SchemeCheckTypeTaskFlowScoreInfoList] = None,
    ):
        # Check item name
        self.check_name = check_name
        # Quality inspection dimension ID
        self.check_type = check_type
        # Is enabled
        self.enable = enable
        # Quality inspection scheme ID
        self.scheme_id = scheme_id
        # List of scoring items under the check item. See SchemeScoreInfo.
        self.scheme_score_info_list = scheme_score_info_list
        # Final score
        self.score = score
        # Original score
        self.source_score = source_score
        # List of scoring items under the check item. See TaskFlowScoreInfo.
        self.task_flow_score_info_list = task_flow_score_info_list

    def validate(self):
        if self.scheme_score_info_list:
            for v1 in self.scheme_score_info_list:
                 if v1:
                    v1.validate()
        if self.task_flow_score_info_list:
            for v1 in self.task_flow_score_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_name is not None:
            result['CheckName'] = self.check_name

        if self.check_type is not None:
            result['CheckType'] = self.check_type

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.scheme_id is not None:
            result['SchemeId'] = self.scheme_id

        result['SchemeScoreInfoList'] = []
        if self.scheme_score_info_list is not None:
            for k1 in self.scheme_score_info_list:
                result['SchemeScoreInfoList'].append(k1.to_map() if k1 else None)

        if self.score is not None:
            result['Score'] = self.score

        if self.source_score is not None:
            result['SourceScore'] = self.source_score

        result['TaskFlowScoreInfoList'] = []
        if self.task_flow_score_info_list is not None:
            for k1 in self.task_flow_score_info_list:
                result['TaskFlowScoreInfoList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')

        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('SchemeId') is not None:
            self.scheme_id = m.get('SchemeId')

        self.scheme_score_info_list = []
        if m.get('SchemeScoreInfoList') is not None:
            for k1 in m.get('SchemeScoreInfoList'):
                temp_model = main_models.SchemeCheckTypeSchemeScoreInfoList()
                self.scheme_score_info_list.append(temp_model.from_map(k1))

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('SourceScore') is not None:
            self.source_score = m.get('SourceScore')

        self.task_flow_score_info_list = []
        if m.get('TaskFlowScoreInfoList') is not None:
            for k1 in m.get('TaskFlowScoreInfoList'):
                temp_model = main_models.SchemeCheckTypeTaskFlowScoreInfoList()
                self.task_flow_score_info_list.append(temp_model.from_map(k1))

        return self

class SchemeCheckTypeTaskFlowScoreInfoList(DaraModel):
    def __init__(
        self,
        scheme_score_info_list: List[main_models.SchemeCheckTypeTaskFlowScoreInfoListSchemeScoreInfoList] = None,
        task_flow_id: int = None,
        task_flow_name: str = None,
        task_flow_type: int = None,
    ):
        # list of scoring items
        self.scheme_score_info_list = scheme_score_info_list
        # Flow ID
        self.task_flow_id = task_flow_id
        # flow name
        self.task_flow_name = task_flow_name
        # \\"Flow version: 0: tree, 1: graph\\"
        self.task_flow_type = task_flow_type

    def validate(self):
        if self.scheme_score_info_list:
            for v1 in self.scheme_score_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SchemeScoreInfoList'] = []
        if self.scheme_score_info_list is not None:
            for k1 in self.scheme_score_info_list:
                result['SchemeScoreInfoList'].append(k1.to_map() if k1 else None)

        if self.task_flow_id is not None:
            result['TaskFlowId'] = self.task_flow_id

        if self.task_flow_name is not None:
            result['TaskFlowName'] = self.task_flow_name

        if self.task_flow_type is not None:
            result['TaskFlowType'] = self.task_flow_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.scheme_score_info_list = []
        if m.get('SchemeScoreInfoList') is not None:
            for k1 in m.get('SchemeScoreInfoList'):
                temp_model = main_models.SchemeCheckTypeTaskFlowScoreInfoListSchemeScoreInfoList()
                self.scheme_score_info_list.append(temp_model.from_map(k1))

        if m.get('TaskFlowId') is not None:
            self.task_flow_id = m.get('TaskFlowId')

        if m.get('TaskFlowName') is not None:
            self.task_flow_name = m.get('TaskFlowName')

        if m.get('TaskFlowType') is not None:
            self.task_flow_type = m.get('TaskFlowType')

        return self

class SchemeCheckTypeTaskFlowScoreInfoListSchemeScoreInfoList(DaraModel):
    def __init__(
        self,
        name: str = None,
        rid: int = None,
        score_num: int = None,
        score_num_type: int = None,
        score_rule_hit_type: int = None,
        score_type: int = None,
        task_flow_id: int = None,
        task_flow_name: str = None,
    ):
        # Rule Name
        self.name = name
        # Rule ID
        self.rid = rid
        # Agent score: default is 0, range [0, 100]
        self.score_num = score_num
        # 0 – Points added or deducted after a rule is triggered
        self.score_num_type = score_num_type
        # 0—score when a hit occurs at an edge zone
        self.score_rule_hit_type = score_rule_hit_type
        # 1 for adding points, 3 for deducting points; default is 1
        self.score_type = score_type
        # Flow ID
        self.task_flow_id = task_flow_id
        # flow name
        self.task_flow_name = task_flow_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.rid is not None:
            result['Rid'] = self.rid

        if self.score_num is not None:
            result['ScoreNum'] = self.score_num

        if self.score_num_type is not None:
            result['ScoreNumType'] = self.score_num_type

        if self.score_rule_hit_type is not None:
            result['ScoreRuleHitType'] = self.score_rule_hit_type

        if self.score_type is not None:
            result['ScoreType'] = self.score_type

        if self.task_flow_id is not None:
            result['TaskFlowId'] = self.task_flow_id

        if self.task_flow_name is not None:
            result['TaskFlowName'] = self.task_flow_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Rid') is not None:
            self.rid = m.get('Rid')

        if m.get('ScoreNum') is not None:
            self.score_num = m.get('ScoreNum')

        if m.get('ScoreNumType') is not None:
            self.score_num_type = m.get('ScoreNumType')

        if m.get('ScoreRuleHitType') is not None:
            self.score_rule_hit_type = m.get('ScoreRuleHitType')

        if m.get('ScoreType') is not None:
            self.score_type = m.get('ScoreType')

        if m.get('TaskFlowId') is not None:
            self.task_flow_id = m.get('TaskFlowId')

        if m.get('TaskFlowName') is not None:
            self.task_flow_name = m.get('TaskFlowName')

        return self

class SchemeCheckTypeSchemeScoreInfoList(DaraModel):
    def __init__(
        self,
        name: str = None,
        rid: int = None,
        score_num: int = None,
        score_num_type: int = None,
        score_rule_hit_type: int = None,
        score_type: int = None,
        task_flow_id: int = None,
        task_flow_name: str = None,
    ):
        # Rule Name
        self.name = name
        # Rule ID
        self.rid = rid
        # Agent rating: default 0, [0, 100]
        self.score_num = score_num
        # 0 – Add or subtract points after triggering a rule
        self.score_num_type = score_num_type
        # 0 – Score when hitting an edge zone
        self.score_rule_hit_type = score_rule_hit_type
        # 1 for adding points, 3 for deducting points; default is 1
        self.score_type = score_type
        # Flow ID
        self.task_flow_id = task_flow_id
        # Flow name
        self.task_flow_name = task_flow_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.rid is not None:
            result['Rid'] = self.rid

        if self.score_num is not None:
            result['ScoreNum'] = self.score_num

        if self.score_num_type is not None:
            result['ScoreNumType'] = self.score_num_type

        if self.score_rule_hit_type is not None:
            result['ScoreRuleHitType'] = self.score_rule_hit_type

        if self.score_type is not None:
            result['ScoreType'] = self.score_type

        if self.task_flow_id is not None:
            result['TaskFlowId'] = self.task_flow_id

        if self.task_flow_name is not None:
            result['TaskFlowName'] = self.task_flow_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Rid') is not None:
            self.rid = m.get('Rid')

        if m.get('ScoreNum') is not None:
            self.score_num = m.get('ScoreNum')

        if m.get('ScoreNumType') is not None:
            self.score_num_type = m.get('ScoreNumType')

        if m.get('ScoreRuleHitType') is not None:
            self.score_rule_hit_type = m.get('ScoreRuleHitType')

        if m.get('ScoreType') is not None:
            self.score_type = m.get('ScoreType')

        if m.get('TaskFlowId') is not None:
            self.task_flow_id = m.get('TaskFlowId')

        if m.get('TaskFlowName') is not None:
            self.task_flow_name = m.get('TaskFlowName')

        return self

