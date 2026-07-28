# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class ChatAiAgentRequest(DaraModel):
    def __init__(
        self,
        hitl_decisions: List[main_models.ChatAiAgentRequestHitlDecisions] = None,
        refs: main_models.ChatAiAgentRequestRefs = None,
        session_id: str = None,
        user_message: str = None,
    ):
        # The list of Human-in-the-Loop (HITL) approval decisions, used to resume a session interrupted by a hitlPending event.
        self.hitl_decisions = hitl_decisions
        # The resource references, including jobs and skill lists.
        self.refs = refs
        # The session ID. If not specified, the server generates one. For multi-turn conversations, pass the same value across requests.
        self.session_id = session_id
        # The user natural language input. The value must be 1 to 64,000 characters in length.
        self.user_message = user_message

    def validate(self):
        if self.hitl_decisions:
            for v1 in self.hitl_decisions:
                 if v1:
                    v1.validate()
        if self.refs:
            self.refs.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['hitlDecisions'] = []
        if self.hitl_decisions is not None:
            for k1 in self.hitl_decisions:
                result['hitlDecisions'].append(k1.to_map() if k1 else None)

        if self.refs is not None:
            result['refs'] = self.refs.to_map()

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.user_message is not None:
            result['userMessage'] = self.user_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hitl_decisions = []
        if m.get('hitlDecisions') is not None:
            for k1 in m.get('hitlDecisions'):
                temp_model = main_models.ChatAiAgentRequestHitlDecisions()
                self.hitl_decisions.append(temp_model.from_map(k1))

        if m.get('refs') is not None:
            temp_model = main_models.ChatAiAgentRequestRefs()
            self.refs = temp_model.from_map(m.get('refs'))

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('userMessage') is not None:
            self.user_message = m.get('userMessage')

        return self

class ChatAiAgentRequestRefs(DaraModel):
    def __init__(
        self,
        jobs: List[main_models.ChatAiAgentRequestRefsJobs] = None,
        skills: List[str] = None,
    ):
        # The list of job references.
        self.jobs = jobs
        # The list of skills to inject.
        self.skills = skills

    def validate(self):
        if self.jobs:
            for v1 in self.jobs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['jobs'] = []
        if self.jobs is not None:
            for k1 in self.jobs:
                result['jobs'].append(k1.to_map() if k1 else None)

        if self.skills is not None:
            result['skills'] = self.skills

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.jobs = []
        if m.get('jobs') is not None:
            for k1 in m.get('jobs'):
                temp_model = main_models.ChatAiAgentRequestRefsJobs()
                self.jobs.append(temp_model.from_map(k1))

        if m.get('skills') is not None:
            self.skills = m.get('skills')

        return self

class ChatAiAgentRequestRefsJobs(DaraModel):
    def __init__(
        self,
        deployment_id: str = None,
        job_id: str = None,
    ):
        # Deployment ID
        self.deployment_id = deployment_id
        # Job ID
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deployment_id is not None:
            result['deploymentId'] = self.deployment_id

        if self.job_id is not None:
            result['jobId'] = self.job_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deploymentId') is not None:
            self.deployment_id = m.get('deploymentId')

        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')

        return self

class ChatAiAgentRequestHitlDecisions(DaraModel):
    def __init__(
        self,
        decision: str = None,
        hitl_id: str = None,
    ):
        # The approval decision. Valid values: approve and deny.
        self.decision = decision
        # The approval item ID corresponding to the hitlPending event.
        self.hitl_id = hitl_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.decision is not None:
            result['decision'] = self.decision

        if self.hitl_id is not None:
            result['hitlId'] = self.hitl_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('decision') is not None:
            self.decision = m.get('decision')

        if m.get('hitlId') is not None:
            self.hitl_id = m.get('hitlId')

        return self

