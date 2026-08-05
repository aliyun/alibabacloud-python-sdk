# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateYikeLoginTokenRequest(DaraModel):
    def __init__(
        self,
        auto_create_production: str = None,
        expires: str = None,
        nick_name: str = None,
        production_auth: str = None,
        sub_user_credit: str = None,
        tenant: str = None,
        user_name: str = None,
        workspace_id: str = None,
    ):
        self.auto_create_production = auto_create_production
        self.expires = expires
        self.nick_name = nick_name
        self.production_auth = production_auth
        self.sub_user_credit = sub_user_credit
        self.tenant = tenant
        self.user_name = user_name
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_create_production is not None:
            result['AutoCreateProduction'] = self.auto_create_production

        if self.expires is not None:
            result['Expires'] = self.expires

        if self.nick_name is not None:
            result['NickName'] = self.nick_name

        if self.production_auth is not None:
            result['ProductionAuth'] = self.production_auth

        if self.sub_user_credit is not None:
            result['SubUserCredit'] = self.sub_user_credit

        if self.tenant is not None:
            result['Tenant'] = self.tenant

        if self.user_name is not None:
            result['UserName'] = self.user_name

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoCreateProduction') is not None:
            self.auto_create_production = m.get('AutoCreateProduction')

        if m.get('Expires') is not None:
            self.expires = m.get('Expires')

        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')

        if m.get('ProductionAuth') is not None:
            self.production_auth = m.get('ProductionAuth')

        if m.get('SubUserCredit') is not None:
            self.sub_user_credit = m.get('SubUserCredit')

        if m.get('Tenant') is not None:
            self.tenant = m.get('Tenant')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

