# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class ListSkillReferencesResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListSkillReferencesResponseBodyData = None,
        request_id: str = None,
    ):
        # The skill reference relationship data returned by the paged query. The data is returned with paging.
        self.data = data
        # The request ID, which is used for troubleshooting.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.ListSkillReferencesResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListSkillReferencesResponseBodyData(DaraModel):
    def __init__(
        self,
        page_items: List[main_models.ListSkillReferencesResponseBodyDataPageItems] = None,
        page_number: int = None,
        pages_available: int = None,
        total_count: int = None,
    ):
        # The list of skill reference relationships on the current page.
        self.page_items = page_items
        # The current page number, starting from 1.
        self.page_number = page_number
        # The total number of available pages.
        self.pages_available = pages_available
        # The total number of reference relationships that match the filter conditions.
        self.total_count = total_count

    def validate(self):
        if self.page_items:
            for v1 in self.page_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['pageItems'] = []
        if self.page_items is not None:
            for k1 in self.page_items:
                result['pageItems'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.pages_available is not None:
            result['pagesAvailable'] = self.pages_available

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.page_items = []
        if m.get('pageItems') is not None:
            for k1 in m.get('pageItems'):
                temp_model = main_models.ListSkillReferencesResponseBodyDataPageItems()
                self.page_items.append(temp_model.from_map(k1))

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pagesAvailable') is not None:
            self.pages_available = m.get('pagesAvailable')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListSkillReferencesResponseBodyDataPageItems(DaraModel):
    def __init__(
        self,
        owner_id: str = None,
        owner_type: str = None,
        owner_version: str = None,
        selector_type: str = None,
        selector_value: str = None,
        skill_name: str = None,
        workspace_id: str = None,
    ):
        # The ID of the referencing entity (the identifier of the Agent or AgentSpec).
        self.owner_id = owner_id
        # The type of the referencing entity. Valid values: AGENT and AGENTSPEC.
        self.owner_type = owner_type
        # The version of the referencing entity.
        self.owner_version = owner_version
        # The reference selector type. Valid values: LABEL and VERSION.
        self.selector_type = selector_type
        # The reference selector value, such as latest, a named label, HEAD, or a specific version.
        self.selector_value = selector_value
        # The name of the referenced skill.
        self.skill_name = skill_name
        # The workspace ID to which the reference belongs.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.owner_id is not None:
            result['ownerId'] = self.owner_id

        if self.owner_type is not None:
            result['ownerType'] = self.owner_type

        if self.owner_version is not None:
            result['ownerVersion'] = self.owner_version

        if self.selector_type is not None:
            result['selectorType'] = self.selector_type

        if self.selector_value is not None:
            result['selectorValue'] = self.selector_value

        if self.skill_name is not None:
            result['skillName'] = self.skill_name

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ownerId') is not None:
            self.owner_id = m.get('ownerId')

        if m.get('ownerType') is not None:
            self.owner_type = m.get('ownerType')

        if m.get('ownerVersion') is not None:
            self.owner_version = m.get('ownerVersion')

        if m.get('selectorType') is not None:
            self.selector_type = m.get('selectorType')

        if m.get('selectorValue') is not None:
            self.selector_value = m.get('selectorValue')

        if m.get('skillName') is not None:
            self.skill_name = m.get('skillName')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

