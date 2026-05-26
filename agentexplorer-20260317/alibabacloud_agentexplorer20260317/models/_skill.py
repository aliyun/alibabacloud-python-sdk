# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Skill(DaraModel):
    def __init__(
        self,
        category_code: str = None,
        category_name: str = None,
        created_at: str = None,
        description: str = None,
        display_name: str = None,
        install_count: int = None,
        like_count: int = None,
        skill_name: str = None,
        sub_category_code: str = None,
        sub_category_name: str = None,
        updated_at: str = None,
    ):
        self.category_code = category_code
        self.category_name = category_name
        self.created_at = created_at
        self.description = description
        self.display_name = display_name
        self.install_count = install_count
        self.like_count = like_count
        self.skill_name = skill_name
        self.sub_category_code = sub_category_code
        self.sub_category_name = sub_category_name
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_code is not None:
            result['categoryCode'] = self.category_code

        if self.category_name is not None:
            result['categoryName'] = self.category_name

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.description is not None:
            result['description'] = self.description

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.install_count is not None:
            result['installCount'] = self.install_count

        if self.like_count is not None:
            result['likeCount'] = self.like_count

        if self.skill_name is not None:
            result['skillName'] = self.skill_name

        if self.sub_category_code is not None:
            result['subCategoryCode'] = self.sub_category_code

        if self.sub_category_name is not None:
            result['subCategoryName'] = self.sub_category_name

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('categoryCode') is not None:
            self.category_code = m.get('categoryCode')

        if m.get('categoryName') is not None:
            self.category_name = m.get('categoryName')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('installCount') is not None:
            self.install_count = m.get('installCount')

        if m.get('likeCount') is not None:
            self.like_count = m.get('likeCount')

        if m.get('skillName') is not None:
            self.skill_name = m.get('skillName')

        if m.get('subCategoryCode') is not None:
            self.sub_category_code = m.get('subCategoryCode')

        if m.get('subCategoryName') is not None:
            self.sub_category_name = m.get('subCategoryName')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        return self

