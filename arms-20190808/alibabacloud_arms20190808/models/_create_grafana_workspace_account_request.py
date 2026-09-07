# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateGrafanaWorkspaceAccountRequest(DaraModel):
    def __init__(
        self,
        account_notes: str = None,
        account_password: str = None,
        aliyun_lang: str = None,
        aliyun_uid: str = None,
        grafana_workspace_id: str = None,
        org_id: int = None,
        region_id: str = None,
        role: str = None,
    ):
        self.account_notes = account_notes
        self.account_password = account_password
        self.aliyun_lang = aliyun_lang
        # This parameter is required.
        self.aliyun_uid = aliyun_uid
        # This parameter is required.
        self.grafana_workspace_id = grafana_workspace_id
        # This parameter is required.
        self.org_id = org_id
        # This parameter is required.
        self.region_id = region_id
        # This parameter is required.
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_notes is not None:
            result['AccountNotes'] = self.account_notes

        if self.account_password is not None:
            result['AccountPassword'] = self.account_password

        if self.aliyun_lang is not None:
            result['AliyunLang'] = self.aliyun_lang

        if self.aliyun_uid is not None:
            result['AliyunUid'] = self.aliyun_uid

        if self.grafana_workspace_id is not None:
            result['GrafanaWorkspaceId'] = self.grafana_workspace_id

        if self.org_id is not None:
            result['OrgId'] = self.org_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role is not None:
            result['Role'] = self.role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountNotes') is not None:
            self.account_notes = m.get('AccountNotes')

        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')

        if m.get('AliyunLang') is not None:
            self.aliyun_lang = m.get('AliyunLang')

        if m.get('AliyunUid') is not None:
            self.aliyun_uid = m.get('AliyunUid')

        if m.get('GrafanaWorkspaceId') is not None:
            self.grafana_workspace_id = m.get('GrafanaWorkspaceId')

        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        return self

