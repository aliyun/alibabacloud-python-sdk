# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class RevokeDataServiceApiRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        project_id: int = None,
        revoke_command: main_models.RevokeDataServiceApiRequestRevokeCommand = None,
    ):
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.project_id = project_id
        # This parameter is required.
        self.revoke_command = revoke_command

    def validate(self):
        if self.revoke_command:
            self.revoke_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.revoke_command is not None:
            result['RevokeCommand'] = self.revoke_command.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RevokeCommand') is not None:
            temp_model = main_models.RevokeDataServiceApiRequestRevokeCommand()
            self.revoke_command = temp_model.from_map(m.get('RevokeCommand'))

        return self

class RevokeDataServiceApiRequestRevokeCommand(DaraModel):
    def __init__(
        self,
        api_id: int = None,
        app_id: int = None,
        auth_type: str = None,
        env: str = None,
        grantee_type: str = None,
        reason: str = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.api_id = api_id
        self.app_id = app_id
        self.auth_type = auth_type
        self.env = env
        self.grantee_type = grantee_type
        # This parameter is required.
        self.reason = reason
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_id is not None:
            result['ApiId'] = self.api_id

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.auth_type is not None:
            result['AuthType'] = self.auth_type

        if self.env is not None:
            result['Env'] = self.env

        if self.grantee_type is not None:
            result['GranteeType'] = self.grantee_type

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')

        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('GranteeType') is not None:
            self.grantee_type = m.get('GranteeType')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

