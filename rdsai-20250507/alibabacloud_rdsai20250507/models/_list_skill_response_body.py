# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_rdsai20250507 import models as main_models
from darabonba.model import DaraModel

class ListSkillResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListSkillResponseBodyData] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The skill list.
        self.data = data
        # The current page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The unique request identifier.
        self.request_id = request_id
        # The total number of records.
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListSkillResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListSkillResponseBodyData(DaraModel):
    def __init__(
        self,
        active_version_id: str = None,
        category: str = None,
        content: Dict[str, Any] = None,
        created_at: str = None,
        dbtypes: List[str] = None,
        description: str = None,
        display_name: str = None,
        icon: str = None,
        id: str = None,
        is_deleted: bool = None,
        name: str = None,
        scope: str = None,
        skill_type: str = None,
        slug: str = None,
        updated_at: str = None,
    ):
        # The ID of the currently active version.
        self.active_version_id = active_version_id
        # The skill category.
        self.category = category
        # The data content.
        self.content = content
        # The creation time.
        self.created_at = created_at
        # The list of database types.
        self.dbtypes = dbtypes
        # The description.
        self.description = description
        # The display name of the skill.
        self.display_name = display_name
        # The public HTTPS URL of the current icon. Empty if not configured.
        self.icon = icon
        # The unique identifier of the skill.
        self.id = id
        # Indicates whether the skill is deleted.
        self.is_deleted = is_deleted
        # The skill name.
        self.name = name
        # The visibility scope of the skill.
        self.scope = scope
        # The skill type.
        self.skill_type = skill_type
        # The stable identifier of the skill.
        self.slug = slug
        # The update time.
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_version_id is not None:
            result['ActiveVersionId'] = self.active_version_id

        if self.category is not None:
            result['Category'] = self.category

        if self.content is not None:
            result['Content'] = self.content

        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        if self.dbtypes is not None:
            result['Dbtypes'] = self.dbtypes

        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.icon is not None:
            result['Icon'] = self.icon

        if self.id is not None:
            result['Id'] = self.id

        if self.is_deleted is not None:
            result['IsDeleted'] = self.is_deleted

        if self.name is not None:
            result['Name'] = self.name

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.skill_type is not None:
            result['SkillType'] = self.skill_type

        if self.slug is not None:
            result['Slug'] = self.slug

        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveVersionId') is not None:
            self.active_version_id = m.get('ActiveVersionId')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('Dbtypes') is not None:
            self.dbtypes = m.get('Dbtypes')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Icon') is not None:
            self.icon = m.get('Icon')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IsDeleted') is not None:
            self.is_deleted = m.get('IsDeleted')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('SkillType') is not None:
            self.skill_type = m.get('SkillType')

        if m.get('Slug') is not None:
            self.slug = m.get('Slug')

        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')

        return self

