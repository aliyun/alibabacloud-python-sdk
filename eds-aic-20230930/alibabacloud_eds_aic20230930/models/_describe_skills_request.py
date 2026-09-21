# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSkillsRequest(DaraModel):
    def __init__(
        self,
        keyword: str = None,
        language: str = None,
        page_number: int = None,
        page_size: int = None,
        skill_id: str = None,
        status_filter: str = None,
        type: str = None,
    ):
        # The keyword in the skill name or skill description.
        self.keyword = keyword
        # The language type. The skill description is returned in this language.
        # 
        # Valid values:
        # 
        # - en: English.
        # - zh-CN: Chinese.
        self.language = language
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The skill ID.
        self.skill_id = skill_id
        # The status filter.
        self.status_filter = status_filter
        # The skill type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.language is not None:
            result['Language'] = self.language

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.skill_id is not None:
            result['SkillId'] = self.skill_id

        if self.status_filter is not None:
            result['StatusFilter'] = self.status_filter

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SkillId') is not None:
            self.skill_id = m.get('SkillId')

        if m.get('StatusFilter') is not None:
            self.status_filter = m.get('StatusFilter')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

