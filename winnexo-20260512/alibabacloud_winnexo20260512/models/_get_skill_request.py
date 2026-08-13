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
        # 是否返回完整文件树（默认 False，避免大体积响应）
        self.include_skill_files = include_skill_files
        # 技能编码（全局唯一），优先级高于 skillName
        self.skill_code = skill_code
        # 技能名称，未传 skillCode 时使用；租户范围内必须唯一
        self.skill_name = skill_name
        # 租户ID，公共参数，缺省时使用调用方默认租户
        self.tenant_id = tenant_id
        # 视角：draft（草稿/编辑视角）或 published（已发布视角，默认）
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

