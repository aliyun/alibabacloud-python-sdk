# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ObtainCloudAccountRoleAccessCredentialRequest(DaraModel):
    def __init__(
        self,
        cloud_account_role_external_id: str = None,
    ):
        # This parameter is required.
        self.cloud_account_role_external_id = cloud_account_role_external_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cloud_account_role_external_id is not None:
            result['cloudAccountRoleExternalId'] = self.cloud_account_role_external_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cloudAccountRoleExternalId') is not None:
            self.cloud_account_role_external_id = m.get('cloudAccountRoleExternalId')

        return self

