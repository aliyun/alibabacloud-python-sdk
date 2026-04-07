# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateProjectMemberRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        project_id: int = None,
        role_code: str = None,
        user_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. We recommend that you set this parameter to a UUID.
        self.client_token = client_token
        # The DataWorks workspace ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The code of the role. This parameter is optional. If you configure the RoleCode parameter, the user is assigned the role.
        self.role_code = role_code
        # The ID of the user to be added.
        # 
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.role_code is not None:
            result['RoleCode'] = self.role_code

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RoleCode') is not None:
            self.role_code = m.get('RoleCode')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

