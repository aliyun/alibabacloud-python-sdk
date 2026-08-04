# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class PutWorkspaceRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        display_name: str = None,
        resource_group_id: str = None,
        sls_project: str = None,
        tags: List[main_models.PutWorkspaceRequestTags] = None,
    ):
        # The description of the workspace.
        self.description = description
        # The display name of the workspace.
        self.display_name = display_name
        # The ID of the resource group specified when the workspace is created.
        self.resource_group_id = resource_group_id
        # The name of the Simple Log Service project.
        # 
        # This parameter is required.
        self.sls_project = sls_project
        # The tags attached to the workspace when it is created.
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.sls_project is not None:
            result['slsProject'] = self.sls_project

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('slsProject') is not None:
            self.sls_project = m.get('slsProject')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.PutWorkspaceRequestTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class PutWorkspaceRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['key'] = self.key

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

