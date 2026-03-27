# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ClaimCallRequest(DaraModel):
    def __init__(
        self,
        candidate_user_list_json: str = None,
        instance_id: str = None,
        job_id: str = None,
        skill_group_id: str = None,
        tags: str = None,
        user_id: str = None,
    ):
        self.candidate_user_list_json = candidate_user_list_json
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.job_id = job_id
        self.skill_group_id = skill_group_id
        self.tags = tags
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.candidate_user_list_json is not None:
            result['CandidateUserListJson'] = self.candidate_user_list_json

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CandidateUserListJson') is not None:
            self.candidate_user_list_json = m.get('CandidateUserListJson')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

