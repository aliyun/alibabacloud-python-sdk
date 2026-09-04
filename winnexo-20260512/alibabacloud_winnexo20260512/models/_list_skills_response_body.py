# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class ListSkillsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        items: List[main_models.ListSkillsResponseBodyItems] = None,
        message: str = None,
        page: int = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
    ):
        # The response status code.
        self.code = code
        # The list of skill cards.
        self.items = items
        # The prompt message.
        self.message = message
        # The page number.
        self.page = page
        # The number of entries per page. Default value: 20. Minimum value: 1. Maximum value: 50.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total = total

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['message'] = self.message

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.ListSkillsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListSkillsResponseBodyItems(DaraModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        execute_mode: str = None,
        global_access: bool = None,
        has_draft_changes: bool = None,
        name: str = None,
        skill_code: str = None,
        skill_hub_definition_id: int = None,
        source_type: str = None,
        status: str = None,
        tags: List[str] = None,
        updated_time: str = None,
        version_number: str = None,
    ):
        # The creation time.
        self.created_time = created_time
        # The description of the to-do card type.
        self.description = description
        # The execution mode, such as CODE_AGENT or SYSTEM.
        self.execute_mode = execute_mode
        # Indicates whether the skill is globally accessible.
        self.global_access = global_access
        # Indicates whether unpublished draft modifications exist.
        self.has_draft_changes = has_draft_changes
        # The file name.
        self.name = name
        # The actual skill code for execution.
        self.skill_code = skill_code
        # The skill definition ID.
        self.skill_hub_definition_id = skill_hub_definition_id
        # The skill source type.
        self.source_type = source_type
        # The task status. Running is returned upon submission.
        self.status = status
        # The key.
        self.tags = tags
        # The update timestamp, in milliseconds.
        self.updated_time = updated_time
        # The workflow definition version number.
        self.version_number = version_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_time is not None:
            result['createdTime'] = self.created_time

        if self.description is not None:
            result['description'] = self.description

        if self.execute_mode is not None:
            result['executeMode'] = self.execute_mode

        if self.global_access is not None:
            result['globalAccess'] = self.global_access

        if self.has_draft_changes is not None:
            result['hasDraftChanges'] = self.has_draft_changes

        if self.name is not None:
            result['name'] = self.name

        if self.skill_code is not None:
            result['skillCode'] = self.skill_code

        if self.skill_hub_definition_id is not None:
            result['skillHubDefinitionId'] = self.skill_hub_definition_id

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.status is not None:
            result['status'] = self.status

        if self.tags is not None:
            result['tags'] = self.tags

        if self.updated_time is not None:
            result['updatedTime'] = self.updated_time

        if self.version_number is not None:
            result['versionNumber'] = self.version_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('executeMode') is not None:
            self.execute_mode = m.get('executeMode')

        if m.get('globalAccess') is not None:
            self.global_access = m.get('globalAccess')

        if m.get('hasDraftChanges') is not None:
            self.has_draft_changes = m.get('hasDraftChanges')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('skillCode') is not None:
            self.skill_code = m.get('skillCode')

        if m.get('skillHubDefinitionId') is not None:
            self.skill_hub_definition_id = m.get('skillHubDefinitionId')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('tags') is not None:
            self.tags = m.get('tags')

        if m.get('updatedTime') is not None:
            self.updated_time = m.get('updatedTime')

        if m.get('versionNumber') is not None:
            self.version_number = m.get('versionNumber')

        return self

