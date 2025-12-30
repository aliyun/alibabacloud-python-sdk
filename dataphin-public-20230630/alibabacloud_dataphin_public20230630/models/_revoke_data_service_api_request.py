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
        reason: str = None,
    ):
        # This parameter is required.
        self.api_id = api_id
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.reason = reason

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

        if self.reason is not None:
            result['Reason'] = self.reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        return self

