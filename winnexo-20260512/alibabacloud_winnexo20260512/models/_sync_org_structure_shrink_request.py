# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SyncOrgStructureShrinkRequest(DaraModel):
    def __init__(
        self,
        corp_id: str = None,
        departments_shrink: str = None,
        members_shrink: str = None,
        platform_type: str = None,
        sso_settings_id: str = None,
        sync_members: bool = None,
        tenant_id: str = None,
    ):
        # 企业标识（必须与 listAvailableConfigs 返回的 corpId 一致）
        # 
        # This parameter is required.
        self.corp_id = corp_id
        # 部门列表（至少包含一个根部门）
        # 
        # This parameter is required.
        self.departments_shrink = departments_shrink
        # 成员列表（syncMembers=true 时必须提供）
        self.members_shrink = members_shrink
        # 平台类型: saml / oauth2 / custom
        # 
        # This parameter is required.
        self.platform_type = platform_type
        # SSO 配置 ID（SAML/OAuth2 可选：不传时按 corpId 自动推导；若存在多个 IdP 使用相同 corpId 则必须显式传入，否则报 AMBIGUOUS 错误；custom 不需要）
        self.sso_settings_id = sso_settings_id
        # 是否同步成员关系（custom 模式强制为 false）
        self.sync_members = sync_members
        # 租户ID，公共参数，缺省时使用调用方默认租户
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.corp_id is not None:
            result['corpId'] = self.corp_id

        if self.departments_shrink is not None:
            result['departments'] = self.departments_shrink

        if self.members_shrink is not None:
            result['members'] = self.members_shrink

        if self.platform_type is not None:
            result['platformType'] = self.platform_type

        if self.sso_settings_id is not None:
            result['ssoSettingsId'] = self.sso_settings_id

        if self.sync_members is not None:
            result['syncMembers'] = self.sync_members

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')

        if m.get('departments') is not None:
            self.departments_shrink = m.get('departments')

        if m.get('members') is not None:
            self.members_shrink = m.get('members')

        if m.get('platformType') is not None:
            self.platform_type = m.get('platformType')

        if m.get('ssoSettingsId') is not None:
            self.sso_settings_id = m.get('ssoSettingsId')

        if m.get('syncMembers') is not None:
            self.sync_members = m.get('syncMembers')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

