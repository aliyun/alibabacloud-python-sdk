# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ObtainCloudAccountRoleAccessCredentialRequest(DaraModel):
    def __init__(
        self,
        cloud_account_role_external_id: str = None,
        duration_seconds: int = None,
    ):
        # This parameter is required.
        self.cloud_account_role_external_id = cloud_account_role_external_id
        self.duration_seconds = duration_seconds

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cloud_account_role_external_id is not None:
            result['cloudAccountRoleExternalId'] = self.cloud_account_role_external_id

        if self.duration_seconds is not None:
            result['durationSeconds'] = self.duration_seconds

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cloudAccountRoleExternalId') is not None:
            self.cloud_account_role_external_id = m.get('cloudAccountRoleExternalId')

        if m.get('durationSeconds') is not None:
            self.duration_seconds = m.get('durationSeconds')

        return self

