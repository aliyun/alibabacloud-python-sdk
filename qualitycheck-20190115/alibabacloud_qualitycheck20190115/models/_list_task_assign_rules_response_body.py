# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_qualitycheck20190115 import models as main_models
from darabonba.model import DaraModel

class ListTaskAssignRulesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        count: int = None,
        data: main_models.ListTaskAssignRulesResponseBodyData = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.count = count
        self.data = data
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
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
            temp_model = main_models.ListTaskAssignRulesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListTaskAssignRulesResponseBodyData(DaraModel):
    def __init__(
        self,
        task_assign_rule_info: List[main_models.ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfo] = None,
    ):
        self.task_assign_rule_info = task_assign_rule_info

    def validate(self):
        if self.task_assign_rule_info:
            for v1 in self.task_assign_rule_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TaskAssignRuleInfo'] = []
        if self.task_assign_rule_info is not None:
            for k1 in self.task_assign_rule_info:
                result['TaskAssignRuleInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.task_assign_rule_info = []
        if m.get('TaskAssignRuleInfo') is not None:
            for k1 in m.get('TaskAssignRuleInfo'):
                temp_model = main_models.ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfo()
                self.task_assign_rule_info.append(temp_model.from_map(k1))

        return self

class ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfo(DaraModel):
    def __init__(
        self,
        agents: main_models.ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoAgents = None,
        agents_str: str = None,
        assignment_type: int = None,
        call_time_end: int = None,
        call_time_start: int = None,
        call_type: int = None,
        create_time: str = None,
        duration_max: int = None,
        duration_min: int = None,
        enabled: int = None,
        priority: int = None,
        reviewers: main_models.ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoReviewers = None,
        rule_id: int = None,
        rule_name: str = None,
        rules: main_models.ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoRules = None,
        sampling_mode: main_models.ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoSamplingMode = None,
        skill_groups: main_models.ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoSkillGroups = None,
        skill_groups_str: str = None,
        update_time: str = None,
    ):
        self.agents = agents
        self.agents_str = agents_str
        self.assignment_type = assignment_type
        self.call_time_end = call_time_end
        self.call_time_start = call_time_start
        self.call_type = call_type
        self.create_time = create_time
        self.duration_max = duration_max
        self.duration_min = duration_min
        self.enabled = enabled
        self.priority = priority
        self.reviewers = reviewers
        self.rule_id = rule_id
        self.rule_name = rule_name
        self.rules = rules
        self.sampling_mode = sampling_mode
        self.skill_groups = skill_groups
        self.skill_groups_str = skill_groups_str
        self.update_time = update_time

    def validate(self):
        if self.agents:
            self.agents.validate()
        if self.reviewers:
            self.reviewers.validate()
        if self.rules:
            self.rules.validate()
        if self.sampling_mode:
            self.sampling_mode.validate()
        if self.skill_groups:
            self.skill_groups.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agents is not None:
            result['Agents'] = self.agents.to_map()

        if self.agents_str is not None:
            result['AgentsStr'] = self.agents_str

        if self.assignment_type is not None:
            result['AssignmentType'] = self.assignment_type

        if self.call_time_end is not None:
            result['CallTimeEnd'] = self.call_time_end

        if self.call_time_start is not None:
            result['CallTimeStart'] = self.call_time_start

        if self.call_type is not None:
            result['CallType'] = self.call_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.duration_max is not None:
            result['DurationMax'] = self.duration_max

        if self.duration_min is not None:
            result['DurationMin'] = self.duration_min

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.reviewers is not None:
            result['Reviewers'] = self.reviewers.to_map()

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.rules is not None:
            result['Rules'] = self.rules.to_map()

        if self.sampling_mode is not None:
            result['SamplingMode'] = self.sampling_mode.to_map()

        if self.skill_groups is not None:
            result['SkillGroups'] = self.skill_groups.to_map()

        if self.skill_groups_str is not None:
            result['SkillGroupsStr'] = self.skill_groups_str

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Agents') is not None:
            temp_model = main_models.ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoAgents()
            self.agents = temp_model.from_map(m.get('Agents'))

        if m.get('AgentsStr') is not None:
            self.agents_str = m.get('AgentsStr')

        if m.get('AssignmentType') is not None:
            self.assignment_type = m.get('AssignmentType')

        if m.get('CallTimeEnd') is not None:
            self.call_time_end = m.get('CallTimeEnd')

        if m.get('CallTimeStart') is not None:
            self.call_time_start = m.get('CallTimeStart')

        if m.get('CallType') is not None:
            self.call_type = m.get('CallType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DurationMax') is not None:
            self.duration_max = m.get('DurationMax')

        if m.get('DurationMin') is not None:
            self.duration_min = m.get('DurationMin')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('Reviewers') is not None:
            temp_model = main_models.ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoReviewers()
            self.reviewers = temp_model.from_map(m.get('Reviewers'))

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Rules') is not None:
            temp_model = main_models.ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoRules()
            self.rules = temp_model.from_map(m.get('Rules'))

        if m.get('SamplingMode') is not None:
            temp_model = main_models.ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoSamplingMode()
            self.sampling_mode = temp_model.from_map(m.get('SamplingMode'))

        if m.get('SkillGroups') is not None:
            temp_model = main_models.ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoSkillGroups()
            self.skill_groups = temp_model.from_map(m.get('SkillGroups'))

        if m.get('SkillGroupsStr') is not None:
            self.skill_groups_str = m.get('SkillGroupsStr')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoSkillGroups(DaraModel):
    def __init__(
        self,
        skill_group: List[main_models.ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoSkillGroupsSkillGroup] = None,
    ):
        self.skill_group = skill_group

    def validate(self):
        if self.skill_group:
            for v1 in self.skill_group:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SkillGroup'] = []
        if self.skill_group is not None:
            for k1 in self.skill_group:
                result['SkillGroup'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.skill_group = []
        if m.get('SkillGroup') is not None:
            for k1 in m.get('SkillGroup'):
                temp_model = main_models.ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoSkillGroupsSkillGroup()
                self.skill_group.append(temp_model.from_map(k1))

        return self

class ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoSkillGroupsSkillGroup(DaraModel):
    def __init__(
        self,
        skill_id: str = None,
        skill_name: str = None,
    ):
        self.skill_id = skill_id
        self.skill_name = skill_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.skill_id is not None:
            result['SkillId'] = self.skill_id

        if self.skill_name is not None:
            result['SkillName'] = self.skill_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SkillId') is not None:
            self.skill_id = m.get('SkillId')

        if m.get('SkillName') is not None:
            self.skill_name = m.get('SkillName')

        return self

class ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoSamplingMode(DaraModel):
    def __init__(
        self,
        any_number_of_draws: int = None,
        designated: bool = None,
        dimension: int = None,
        limit: int = None,
        number_of_draws: int = None,
        proportion: float = None,
        random_inspection_number: int = None,
        sampling_mode_agents: main_models.ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoSamplingModeSamplingModeAgents = None,
    ):
        self.any_number_of_draws = any_number_of_draws
        self.designated = designated
        self.dimension = dimension
        self.limit = limit
        self.number_of_draws = number_of_draws
        self.proportion = proportion
        self.random_inspection_number = random_inspection_number
        self.sampling_mode_agents = sampling_mode_agents

    def validate(self):
        if self.sampling_mode_agents:
            self.sampling_mode_agents.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.any_number_of_draws is not None:
            result['AnyNumberOfDraws'] = self.any_number_of_draws

        if self.designated is not None:
            result['Designated'] = self.designated

        if self.dimension is not None:
            result['Dimension'] = self.dimension

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.number_of_draws is not None:
            result['NumberOfDraws'] = self.number_of_draws

        if self.proportion is not None:
            result['Proportion'] = self.proportion

        if self.random_inspection_number is not None:
            result['RandomInspectionNumber'] = self.random_inspection_number

        if self.sampling_mode_agents is not None:
            result['SamplingModeAgents'] = self.sampling_mode_agents.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnyNumberOfDraws') is not None:
            self.any_number_of_draws = m.get('AnyNumberOfDraws')

        if m.get('Designated') is not None:
            self.designated = m.get('Designated')

        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('NumberOfDraws') is not None:
            self.number_of_draws = m.get('NumberOfDraws')

        if m.get('Proportion') is not None:
            self.proportion = m.get('Proportion')

        if m.get('RandomInspectionNumber') is not None:
            self.random_inspection_number = m.get('RandomInspectionNumber')

        if m.get('SamplingModeAgents') is not None:
            temp_model = main_models.ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoSamplingModeSamplingModeAgents()
            self.sampling_mode_agents = temp_model.from_map(m.get('SamplingModeAgents'))

        return self

class ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoSamplingModeSamplingModeAgents(DaraModel):
    def __init__(
        self,
        sampling_mode_agent: List[main_models.ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoSamplingModeSamplingModeAgentsSamplingModeAgent] = None,
    ):
        self.sampling_mode_agent = sampling_mode_agent

    def validate(self):
        if self.sampling_mode_agent:
            for v1 in self.sampling_mode_agent:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SamplingModeAgent'] = []
        if self.sampling_mode_agent is not None:
            for k1 in self.sampling_mode_agent:
                result['SamplingModeAgent'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sampling_mode_agent = []
        if m.get('SamplingModeAgent') is not None:
            for k1 in m.get('SamplingModeAgent'):
                temp_model = main_models.ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoSamplingModeSamplingModeAgentsSamplingModeAgent()
                self.sampling_mode_agent.append(temp_model.from_map(k1))

        return self

class ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoSamplingModeSamplingModeAgentsSamplingModeAgent(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        agent_name: str = None,
    ):
        self.agent_id = agent_id
        self.agent_name = agent_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.agent_name is not None:
            result['AgentName'] = self.agent_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        return self

class ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoRules(DaraModel):
    def __init__(
        self,
        rule_basic_info: List[main_models.ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoRulesRuleBasicInfo] = None,
    ):
        self.rule_basic_info = rule_basic_info

    def validate(self):
        if self.rule_basic_info:
            for v1 in self.rule_basic_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RuleBasicInfo'] = []
        if self.rule_basic_info is not None:
            for k1 in self.rule_basic_info:
                result['RuleBasicInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rule_basic_info = []
        if m.get('RuleBasicInfo') is not None:
            for k1 in m.get('RuleBasicInfo'):
                temp_model = main_models.ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoRulesRuleBasicInfo()
                self.rule_basic_info.append(temp_model.from_map(k1))

        return self

class ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoRulesRuleBasicInfo(DaraModel):
    def __init__(
        self,
        name: str = None,
        rid: str = None,
    ):
        self.name = name
        self.rid = rid

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Rid') is not None:
            self.rid = m.get('Rid')

        return self

class ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoReviewers(DaraModel):
    def __init__(
        self,
        reviewer: List[main_models.ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoReviewersReviewer] = None,
    ):
        self.reviewer = reviewer

    def validate(self):
        if self.reviewer:
            for v1 in self.reviewer:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Reviewer'] = []
        if self.reviewer is not None:
            for k1 in self.reviewer:
                result['Reviewer'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.reviewer = []
        if m.get('Reviewer') is not None:
            for k1 in m.get('Reviewer'):
                temp_model = main_models.ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoReviewersReviewer()
                self.reviewer.append(temp_model.from_map(k1))

        return self

class ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoReviewersReviewer(DaraModel):
    def __init__(
        self,
        reviewer_id: str = None,
        reviewer_name: str = None,
    ):
        self.reviewer_id = reviewer_id
        self.reviewer_name = reviewer_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.reviewer_id is not None:
            result['ReviewerId'] = self.reviewer_id

        if self.reviewer_name is not None:
            result['ReviewerName'] = self.reviewer_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReviewerId') is not None:
            self.reviewer_id = m.get('ReviewerId')

        if m.get('ReviewerName') is not None:
            self.reviewer_name = m.get('ReviewerName')

        return self

class ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoAgents(DaraModel):
    def __init__(
        self,
        agent: List[main_models.ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoAgentsAgent] = None,
    ):
        self.agent = agent

    def validate(self):
        if self.agent:
            for v1 in self.agent:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Agent'] = []
        if self.agent is not None:
            for k1 in self.agent:
                result['Agent'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.agent = []
        if m.get('Agent') is not None:
            for k1 in m.get('Agent'):
                temp_model = main_models.ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoAgentsAgent()
                self.agent.append(temp_model.from_map(k1))

        return self

class ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoAgentsAgent(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        agent_name: str = None,
    ):
        self.agent_id = agent_id
        self.agent_name = agent_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.agent_name is not None:
            result['AgentName'] = self.agent_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        return self

