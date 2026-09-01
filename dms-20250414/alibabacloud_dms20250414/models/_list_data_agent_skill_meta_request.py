# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDataAgentSkillMetaRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        search_key: str = None,
        skill_from: str = None,
        skill_id: str = None,
        skill_name: str = None,
        workspace_id: str = None,
    ):
        # The page number, starting from 1.
        self.page_number = page_number
        # The number of records per page. Default value: 20.
        self.page_size = page_size
        # The keyword for fuzzy match.
        self.search_key = search_key
        # The source of the skill. Valid values:
        # 
        # - User: a skill uploaded by the user.
        # - Agent: a skill derived from Agent analysis.
        self.skill_from = skill_from
        # The skill ID.
        self.skill_id = skill_id
        # The skill name.
        self.skill_name = skill_name
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.search_key is not None:
            result['SearchKey'] = self.search_key

        if self.skill_from is not None:
            result['SkillFrom'] = self.skill_from

        if self.skill_id is not None:
            result['SkillId'] = self.skill_id

        if self.skill_name is not None:
            result['SkillName'] = self.skill_name

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')

        if m.get('SkillFrom') is not None:
            self.skill_from = m.get('SkillFrom')

        if m.get('SkillId') is not None:
            self.skill_id = m.get('SkillId')

        if m.get('SkillName') is not None:
            self.skill_name = m.get('SkillName')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

