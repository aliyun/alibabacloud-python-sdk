# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Skill(DaraModel):
    def __init__(
        self,
        category_code: str = None,
        category_name: str = None,
        category_name_en: str = None,
        created_at: str = None,
        description: str = None,
        description_en: str = None,
        display_name: str = None,
        github_path: str = None,
        install_count: int = None,
        like_count: int = None,
        name_en: str = None,
        skill_name: str = None,
        sub_category_code: str = None,
        sub_category_name: str = None,
        sub_category_name_en: str = None,
        updated_at: str = None,
    ):
        # The primary category code.
        self.category_code = category_code
        # The primary category name.
        self.category_name = category_name
        self.category_name_en = category_name_en
        # The time when the Agent Skill was created.
        self.created_at = created_at
        # The description of the Agent Skill.
        self.description = description
        self.description_en = description_en
        # The display name of the Agent Skill.
        self.display_name = display_name
        self.github_path = github_path
        # The number of installations.
        self.install_count = install_count
        # The number of likes.
        self.like_count = like_count
        self.name_en = name_en
        # The English name of the Agent Skill, which serves as a unique identifier.
        self.skill_name = skill_name
        # The secondary category code.
        self.sub_category_code = sub_category_code
        # The secondary category name.
        self.sub_category_name = sub_category_name
        self.sub_category_name_en = sub_category_name_en
        # The time when the Agent Skill was last updated.
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

        if self.category_name_en is not None:
            result['categoryNameEn'] = self.category_name_en

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.description is not None:
            result['description'] = self.description

        if self.description_en is not None:
            result['descriptionEn'] = self.description_en

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.github_path is not None:
            result['githubPath'] = self.github_path

        if self.install_count is not None:
            result['installCount'] = self.install_count

        if self.like_count is not None:
            result['likeCount'] = self.like_count

        if self.name_en is not None:
            result['nameEn'] = self.name_en

        if self.skill_name is not None:
            result['skillName'] = self.skill_name

        if self.sub_category_code is not None:
            result['subCategoryCode'] = self.sub_category_code

        if self.sub_category_name is not None:
            result['subCategoryName'] = self.sub_category_name

        if self.sub_category_name_en is not None:
            result['subCategoryNameEn'] = self.sub_category_name_en

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('categoryCode') is not None:
            self.category_code = m.get('categoryCode')

        if m.get('categoryName') is not None:
            self.category_name = m.get('categoryName')

        if m.get('categoryNameEn') is not None:
            self.category_name_en = m.get('categoryNameEn')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('descriptionEn') is not None:
            self.description_en = m.get('descriptionEn')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('githubPath') is not None:
            self.github_path = m.get('githubPath')

        if m.get('installCount') is not None:
            self.install_count = m.get('installCount')

        if m.get('likeCount') is not None:
            self.like_count = m.get('likeCount')

        if m.get('nameEn') is not None:
            self.name_en = m.get('nameEn')

        if m.get('skillName') is not None:
            self.skill_name = m.get('skillName')

        if m.get('subCategoryCode') is not None:
            self.sub_category_code = m.get('subCategoryCode')

        if m.get('subCategoryName') is not None:
            self.sub_category_name = m.get('subCategoryName')

        if m.get('subCategoryNameEn') is not None:
            self.sub_category_name_en = m.get('subCategoryNameEn')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        return self

