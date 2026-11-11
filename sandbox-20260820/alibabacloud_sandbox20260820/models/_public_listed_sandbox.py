# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sandbox20260820 import models as main_models
from darabonba.model import DaraModel

class PublicListedSandbox(DaraModel):
    def __init__(
        self,
        auto_pause: bool = None,
        auto_resume: bool = None,
        cpu: float = None,
        disk_size: int = None,
        end_at: str = None,
        memory_size: int = None,
        resource_group_id: str = None,
        resource_tags: List[main_models.PublicListedSandboxResourceTags] = None,
        sandbox_id: str = None,
        started_at: str = None,
        state: str = None,
        team_id: str = None,
        team_name: str = None,
        template_id: str = None,
        template_name: str = None,
        user_id: str = None,
    ):
        self.auto_pause = auto_pause
        self.auto_resume = auto_resume
        self.cpu = cpu
        self.disk_size = disk_size
        self.end_at = end_at
        self.memory_size = memory_size
        self.resource_group_id = resource_group_id
        self.resource_tags = resource_tags
        self.sandbox_id = sandbox_id
        self.started_at = started_at
        self.state = state
        self.team_id = team_id
        self.team_name = team_name
        self.template_id = template_id
        self.template_name = template_name
        self.user_id = user_id

    def validate(self):
        if self.resource_tags:
            for v1 in self.resource_tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_pause is not None:
            result['autoPause'] = self.auto_pause

        if self.auto_resume is not None:
            result['autoResume'] = self.auto_resume

        if self.cpu is not None:
            result['cpu'] = self.cpu

        if self.disk_size is not None:
            result['diskSize'] = self.disk_size

        if self.end_at is not None:
            result['endAt'] = self.end_at

        if self.memory_size is not None:
            result['memorySize'] = self.memory_size

        if self.resource_group_id is not None:
            result['resourceGroupID'] = self.resource_group_id

        if self.resource_tags is not None:
            result['resourceTags'] = []
            for k1 in self.resource_tags:
                result['resourceTags'].append(k1.to_map() if k1 else None)

        if self.sandbox_id is not None:
            result['sandboxID'] = self.sandbox_id

        if self.started_at is not None:
            result['startedAt'] = self.started_at

        if self.state is not None:
            result['state'] = self.state

        if self.team_id is not None:
            result['teamID'] = self.team_id

        if self.team_name is not None:
            result['teamName'] = self.team_name

        if self.template_id is not None:
            result['templateID'] = self.template_id

        if self.template_name is not None:
            result['templateName'] = self.template_name

        if self.user_id is not None:
            result['userID'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoPause') is not None:
            self.auto_pause = m.get('autoPause')

        if m.get('autoResume') is not None:
            self.auto_resume = m.get('autoResume')

        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')

        if m.get('diskSize') is not None:
            self.disk_size = m.get('diskSize')

        if m.get('endAt') is not None:
            self.end_at = m.get('endAt')

        if m.get('memorySize') is not None:
            self.memory_size = m.get('memorySize')

        if m.get('resourceGroupID') is not None:
            self.resource_group_id = m.get('resourceGroupID')

        if m.get('resourceTags') is not None:
            self.resource_tags = []
            for k1 in m.get('resourceTags'):
                temp_model = main_models.PublicListedSandboxResourceTags()
                self.resource_tags.append(temp_model.from_map(k1))

        if m.get('sandboxID') is not None:
            self.sandbox_id = m.get('sandboxID')

        if m.get('startedAt') is not None:
            self.started_at = m.get('startedAt')

        if m.get('state') is not None:
            self.state = m.get('state')

        if m.get('teamID') is not None:
            self.team_id = m.get('teamID')

        if m.get('teamName') is not None:
            self.team_name = m.get('teamName')

        if m.get('templateID') is not None:
            self.template_id = m.get('templateID')

        if m.get('templateName') is not None:
            self.template_name = m.get('templateName')

        if m.get('userID') is not None:
            self.user_id = m.get('userID')

        return self

class PublicListedSandboxResourceTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['tagKey'] = self.tag_key

        if self.tag_value is not None:
            result['tagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tagKey') is not None:
            self.tag_key = m.get('tagKey')

        if m.get('tagValue') is not None:
            self.tag_value = m.get('tagValue')

        return self

