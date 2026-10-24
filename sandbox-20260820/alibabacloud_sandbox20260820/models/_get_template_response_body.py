# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sandbox20260820 import models as main_models
from darabonba.model import DaraModel

class GetTemplateResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        created_time: str = None,
        message: str = None,
        name: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        resource_tags: List[main_models.GetTemplateResponseBodyResourceTags] = None,
        runtime_config: main_models.PublicTemplateRuntimeConfig = None,
        status: main_models.PublicTemplateStatus = None,
        team_id: str = None,
        team_name: str = None,
        template_id: str = None,
    ):
        # The error code. The value is 200 if the request is successful.
        self.code = code
        # The creation time in UTC.
        self.created_time = created_time
        # The response message.
        self.message = message
        # The name of the template.
        self.name = name
        # Id of the request
        self.request_id = request_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The resource tags.
        self.resource_tags = resource_tags
        # The runtime configuration of the template.
        self.runtime_config = runtime_config
        # The status of the template.
        self.status = status
        # The team ID.
        self.team_id = team_id
        # The team name.
        self.team_name = team_name
        # The unique identifier of the template.
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
        if self.code is not None:
            result['code'] = self.code

        if self.created_time is not None:
            result['createdTime'] = self.created_time

        if self.message is not None:
            result['message'] = self.message

        if self.name is not None:
            result['name'] = self.name

        if self.request_id is not None:
            result['requestId'] = self.request_id

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
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('resourceGroupID') is not None:
            self.resource_group_id = m.get('resourceGroupID')

        if m.get('resourceTags') is not None:
            self.resource_tags = []
            for k1 in m.get('resourceTags'):
                temp_model = main_models.GetTemplateResponseBodyResourceTags()
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

class GetTemplateResponseBodyResourceTags(DaraModel):
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

