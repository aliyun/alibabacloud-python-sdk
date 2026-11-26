# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSkillRequest(DaraModel):
    def __init__(
        self,
        app_token: str = None,
        include_skill_files: bool = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        skill_code: str = None,
        skill_name: str = None,
        tenant_id: str = None,
        view_mode: str = None,
    ):
        # 平台应用 Token（控制台签发）。传入后将以 opsUserId 或 opsUserCode 指定的用户身份执行
        self.app_token = app_token
        # Specifies whether to return the complete file tree. Default value: false. This prevents large response payloads.
        self.include_skill_files = include_skill_files
        # 代理用户编码（租户内唯一），仅当应用凭证配置为 source_uid 时使用
        self.ops_user_code = ops_user_code
        # 代理用户ID（WINNEXO 平台用户ID），仅当应用凭证配置为 winnexo_uid 时使用
        self.ops_user_id = ops_user_id
        # The skill code. This parameter has a value when type is set to skill.
        self.skill_code = skill_code
        # The name of the skill.
        self.skill_name = skill_name
        # The ID of the tenant to which the task belongs.
        self.tenant_id = tenant_id
        # The view mode. Valid values: draft (draft or edit view) and published (published view, default).
        self.view_mode = view_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_token is not None:
            result['appToken'] = self.app_token

        if self.include_skill_files is not None:
            result['includeSkillFiles'] = self.include_skill_files

        if self.ops_user_code is not None:
            result['opsUserCode'] = self.ops_user_code

        if self.ops_user_id is not None:
            result['opsUserId'] = self.ops_user_id

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
        if m.get('appToken') is not None:
            self.app_token = m.get('appToken')

        if m.get('includeSkillFiles') is not None:
            self.include_skill_files = m.get('includeSkillFiles')

        if m.get('opsUserCode') is not None:
            self.ops_user_code = m.get('opsUserCode')

        if m.get('opsUserId') is not None:
            self.ops_user_id = m.get('opsUserId')

        if m.get('skillCode') is not None:
            self.skill_code = m.get('skillCode')

        if m.get('skillName') is not None:
            self.skill_name = m.get('skillName')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('viewMode') is not None:
            self.view_mode = m.get('viewMode')

        return self

