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
        # The business identifier of the cloud account role.
        # 
        # This parameter is required.
        self.cloud_account_role_external_id = cloud_account_role_external_id
        # Specifies the validity duration of the temporary security credentials (STS Token) for the cloud account role, in seconds. Valid values: 900 to 43200 (15 minutes to 12 hours).
        # Constraints:
        # - The minimum value cannot be less than 900 seconds.
        # - The maximum value is subject to the maximum session duration of the cloud provider role or service account. For example, the default maximum session duration for an AWS role is 3600 seconds.
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

