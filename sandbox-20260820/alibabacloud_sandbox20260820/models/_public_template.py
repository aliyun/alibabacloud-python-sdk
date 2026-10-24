# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sandbox20260820 import models as main_models
from darabonba.model import DaraModel

class PublicTemplate(DaraModel):
    def __init__(
        self,
        created_time: str = None,
        name: str = None,
        resource_group_id: str = None,
        resource_tags: List[main_models.PublicTemplateResourceTags] = None,
        runtime_config: main_models.PublicTemplateRuntimeConfig = None,
        status: main_models.PublicTemplateStatus = None,
        team_id: str = None,
        team_name: str = None,
        template_id: str = None,
    ):
        # The time when the template was created, in UTC and RFC 3339 format.
        self.created_time = created_time
        # The name of the template, which is unique within a team.
        self.name = name
        # The ID of the Alibaba Cloud resource group to which the team belongs.
        self.resource_group_id = resource_group_id
        # The resource tags.
        self.resource_tags = resource_tags
        # The runtime configuration of the template, which determines the specifications and environment of the sandbox instances created from the template.
        self.runtime_config = runtime_config
        # The current status of the template.
        self.status = status
        # The ID of the team to which the resource belongs, in UUID format.
        self.team_id = team_id
        # The name of the team.
        self.team_name = team_name
        # The ID of the sandbox template.
        self.template_id = template_id

    def validate(self):
        if self.resource_tags:
            for v1 in self.resource_tags:
                 if v1:
                    v1.validate()
        if self.runtime_config:
            self.runtime_config.validate()
        if self.status:
            self.status.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_time is not None:
            result['createdTime'] = self.created_time

        if self.name is not None:
            result['name'] = self.name

        if self.resource_group_id is not None:
            result['resourceGroupID'] = self.resource_group_id

        if self.resource_tags is not None:
            result['resourceTags'] = []
            for k1 in self.resource_tags:
                result['resourceTags'].append(k1.to_map() if k1 else None)

        if self.runtime_config is not None:
            result['runtimeConfig'] = self.runtime_config.to_map()

        if self.status is not None:
            result['status'] = self.status.to_map()

        if self.team_id is not None:
            result['teamID'] = self.team_id

        if self.team_name is not None:
            result['teamName'] = self.team_name

        if self.template_id is not None:
            result['templateID'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('resourceGroupID') is not None:
            self.resource_group_id = m.get('resourceGroupID')

        if m.get('resourceTags') is not None:
            self.resource_tags = []
            for k1 in m.get('resourceTags'):
                temp_model = main_models.PublicTemplateResourceTags()
                self.resource_tags.append(temp_model.from_map(k1))

        if m.get('runtimeConfig') is not None:
            temp_model = main_models.PublicTemplateRuntimeConfig()
            self.runtime_config = temp_model.from_map(m.get('runtimeConfig'))

        if m.get('status') is not None:
            temp_model = main_models.PublicTemplateStatus()
            self.status = temp_model.from_map(m.get('status'))

        if m.get('teamID') is not None:
            self.team_id = m.get('teamID')

        if m.get('teamName') is not None:
            self.team_name = m.get('teamName')

        if m.get('templateID') is not None:
            self.template_id = m.get('templateID')

        return self

class PublicTemplateResourceTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
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

