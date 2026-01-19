# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeRecommendTaskDetailResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_object: main_models.DescribeRecommendTaskDetailResponseBodyResultObject = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Return result
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_object is not None:
            result['resultObject'] = self.result_object.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('resultObject') is not None:
            temp_model = main_models.DescribeRecommendTaskDetailResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('resultObject'))

        return self

class DescribeRecommendTaskDetailResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        event_code: str = None,
        event_name: str = None,
        expect_velocities: List[str] = None,
        gmt_create: int = None,
        normal_size: int = None,
        recommend_rule_dtos: List[main_models.DescribeRecommendTaskDetailResponseBodyResultObjectRecommendRuleDTOs] = None,
        recommend_variable_dtos: List[main_models.DescribeRecommendTaskDetailResponseBodyResultObjectRecommendVariableDTOs] = None,
        risk_size: int = None,
        sample_name: str = None,
        sample_scene: str = None,
        sample_scene_name: str = None,
        task_id: int = None,
        task_name: str = None,
        task_status: str = None,
    ):
        # Event code
        self.event_code = event_code
        # Event name.
        self.event_name = event_name
        # Comparison indicators
        self.expect_velocities = expect_velocities
        # Creation time
        self.gmt_create = gmt_create
        # Number of normal samples
        self.normal_size = normal_size
        # Recommended strategy list
        self.recommend_rule_dtos = recommend_rule_dtos
        # Selected variable list
        self.recommend_variable_dtos = recommend_variable_dtos
        # Number of risk samples
        self.risk_size = risk_size
        # Sample name
        self.sample_name = sample_name
        # Sample scenario
        self.sample_scene = sample_scene
        # Sample scenario name
        self.sample_scene_name = sample_scene_name
        # Task ID
        self.task_id = task_id
        # Task name
        self.task_name = task_name
        # Task status.
        self.task_status = task_status

    def validate(self):
        if self.recommend_rule_dtos:
            for v1 in self.recommend_rule_dtos:
                 if v1:
                    v1.validate()
        if self.recommend_variable_dtos:
            for v1 in self.recommend_variable_dtos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_code is not None:
            result['eventCode'] = self.event_code

        if self.event_name is not None:
            result['eventName'] = self.event_name

        if self.expect_velocities is not None:
            result['expectVelocities'] = self.expect_velocities

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.normal_size is not None:
            result['normalSize'] = self.normal_size

        result['recommendRuleDTOs'] = []
        if self.recommend_rule_dtos is not None:
            for k1 in self.recommend_rule_dtos:
                result['recommendRuleDTOs'].append(k1.to_map() if k1 else None)

        result['recommendVariableDTOs'] = []
        if self.recommend_variable_dtos is not None:
            for k1 in self.recommend_variable_dtos:
                result['recommendVariableDTOs'].append(k1.to_map() if k1 else None)

        if self.risk_size is not None:
            result['riskSize'] = self.risk_size

        if self.sample_name is not None:
            result['sampleName'] = self.sample_name

        if self.sample_scene is not None:
            result['sampleScene'] = self.sample_scene

        if self.sample_scene_name is not None:
            result['sampleSceneName'] = self.sample_scene_name

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.task_name is not None:
            result['taskName'] = self.task_name

        if self.task_status is not None:
            result['taskStatus'] = self.task_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('eventCode') is not None:
            self.event_code = m.get('eventCode')

        if m.get('eventName') is not None:
            self.event_name = m.get('eventName')

        if m.get('expectVelocities') is not None:
            self.expect_velocities = m.get('expectVelocities')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('normalSize') is not None:
            self.normal_size = m.get('normalSize')

        self.recommend_rule_dtos = []
        if m.get('recommendRuleDTOs') is not None:
            for k1 in m.get('recommendRuleDTOs'):
                temp_model = main_models.DescribeRecommendTaskDetailResponseBodyResultObjectRecommendRuleDTOs()
                self.recommend_rule_dtos.append(temp_model.from_map(k1))

        self.recommend_variable_dtos = []
        if m.get('recommendVariableDTOs') is not None:
            for k1 in m.get('recommendVariableDTOs'):
                temp_model = main_models.DescribeRecommendTaskDetailResponseBodyResultObjectRecommendVariableDTOs()
                self.recommend_variable_dtos.append(temp_model.from_map(k1))

        if m.get('riskSize') is not None:
            self.risk_size = m.get('riskSize')

        if m.get('sampleName') is not None:
            self.sample_name = m.get('sampleName')

        if m.get('sampleScene') is not None:
            self.sample_scene = m.get('sampleScene')

        if m.get('sampleSceneName') is not None:
            self.sample_scene_name = m.get('sampleSceneName')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('taskName') is not None:
            self.task_name = m.get('taskName')

        if m.get('taskStatus') is not None:
            self.task_status = m.get('taskStatus')

        return self

class DescribeRecommendTaskDetailResponseBodyResultObjectRecommendVariableDTOs(DaraModel):
    def __init__(
        self,
        id: int = None,
        title: str = None,
    ):
        # Primary key ID
        self.id = id
        # Title
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['id'] = self.id

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class DescribeRecommendTaskDetailResponseBodyResultObjectRecommendRuleDTOs(DaraModel):
    def __init__(
        self,
        compute_expression: str = None,
        hit_sample: int = None,
        id: int = None,
        not_hit_sample: int = None,
        recommend_rules: List[main_models.DescribeRecommendTaskDetailResponseBodyResultObjectRecommendRuleDTOsRecommendRules] = None,
        rule_id: str = None,
        rule_name: str = None,
        status: str = None,
        velocities: str = None,
    ):
        # Calculation path
        self.compute_expression = compute_expression
        # Number of hit samples
        self.hit_sample = hit_sample
        # Primary key ID of the rule
        self.id = id
        # Number of unhit samples
        self.not_hit_sample = not_hit_sample
        # List of candidate rules
        self.recommend_rules = recommend_rules
        # Strategy ID
        self.rule_id = rule_id
        # Rule name
        self.rule_name = rule_name
        # Status
        self.status = status
        # List of indicators in JSON string format
        self.velocities = velocities

    def validate(self):
        if self.recommend_rules:
            for v1 in self.recommend_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compute_expression is not None:
            result['computeExpression'] = self.compute_expression

        if self.hit_sample is not None:
            result['hitSample'] = self.hit_sample

        if self.id is not None:
            result['id'] = self.id

        if self.not_hit_sample is not None:
            result['notHitSample'] = self.not_hit_sample

        result['recommendRules'] = []
        if self.recommend_rules is not None:
            for k1 in self.recommend_rules:
                result['recommendRules'].append(k1.to_map() if k1 else None)

        if self.rule_id is not None:
            result['ruleId'] = self.rule_id

        if self.rule_name is not None:
            result['ruleName'] = self.rule_name

        if self.status is not None:
            result['status'] = self.status

        if self.velocities is not None:
            result['velocities'] = self.velocities

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('computeExpression') is not None:
            self.compute_expression = m.get('computeExpression')

        if m.get('hitSample') is not None:
            self.hit_sample = m.get('hitSample')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('notHitSample') is not None:
            self.not_hit_sample = m.get('notHitSample')

        self.recommend_rules = []
        if m.get('recommendRules') is not None:
            for k1 in m.get('recommendRules'):
                temp_model = main_models.DescribeRecommendTaskDetailResponseBodyResultObjectRecommendRuleDTOsRecommendRules()
                self.recommend_rules.append(temp_model.from_map(k1))

        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')

        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('velocities') is not None:
            self.velocities = m.get('velocities')

        return self

class DescribeRecommendTaskDetailResponseBodyResultObjectRecommendRuleDTOsRecommendRules(DaraModel):
    def __init__(
        self,
        left: str = None,
        operator: str = None,
        right: str = None,
    ):
        # Left variable
        self.left = left
        # Operator
        self.operator = operator
        # Right variable
        self.right = right

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.left is not None:
            result['left'] = self.left

        if self.operator is not None:
            result['operator'] = self.operator

        if self.right is not None:
            result['right'] = self.right

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('left') is not None:
            self.left = m.get('left')

        if m.get('operator') is not None:
            self.operator = m.get('operator')

        if m.get('right') is not None:
            self.right = m.get('right')

        return self

