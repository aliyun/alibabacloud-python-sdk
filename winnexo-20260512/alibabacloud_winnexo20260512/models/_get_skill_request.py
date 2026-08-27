# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSkillRequest(DaraModel):
    def __init__(
        self,
        include_skill_files: bool = None,
        skill_code: str = None,
        skill_name: str = None,
        tenant_id: str = None,
        view_mode: str = None,
    ):
        # Specifies whether to return the complete file tree. Default value: False. This avoids large response payloads.
        self.include_skill_files = include_skill_files
        # The skill code. This parameter has a value when type is set to skill.
        self.skill_code = skill_code
        # The skill name.
        self.skill_name = skill_name
        # The tenant ID to which the task belongs.
        self.tenant_id = tenant_id
        # The view mode. Valid values: draft (draft/editing view) or published (published view, default).
        self.view_mode = view_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.include_skill_files is not None:
            result['includeSkillFiles'] = self.include_skill_files

        if self.skill_code is not None:
            result['skillCode'] = self.skill_code

        if self.skill_name is not None:
            result['skillName'] = self.skill_name

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.view_mode is not None:
            result['viewMode'] = self.view_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('includeSkillFiles') is not None:
            self.include_skill_files = m.get('includeSkillFiles')

        if m.get('skillCode') is not None:
            self.skill_code = m.get('skillCode')

        if m.get('skillName') is not None:
            self.skill_name = m.get('skillName')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('viewMode') is not None:
            self.view_mode = m.get('viewMode')

        return self

