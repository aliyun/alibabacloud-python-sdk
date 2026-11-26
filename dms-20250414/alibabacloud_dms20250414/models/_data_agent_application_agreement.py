# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DataAgentApplicationAgreement(DaraModel):
    def __init__(
        self,
        expires_at: str = None,
        region_id: str = None,
        signed_at: str = None,
        status: str = None,
        workspace_id: str = None,
    ):
        # The expiration time of the agreement in ISO 8601 UTC string format. This field is omitted if the agreement is unsigned. The agreement expires when this time is reached. The default validity period is 10 calendar years from the signing date.
        self.expires_at = expires_at
        # The region of the workspace to which the agreement belongs.
        self.region_id = region_id
        # The signing time in ISO 8601 UTC string format. This field is omitted if the agreement is unsigned. Repeated signing within the validity period retains the original time, and re-signing after expiration updates the time.
        self.signed_at = signed_at
        # The agreement status. Valid values: NOT_SIGNED (unsigned), EXPIRED (expired), and SIGNED (signed and valid). Both NOT_SIGNED and EXPIRED are business statuses returned upon a successful query.
        self.status = status
        # The stable identifier of the workspace to which the agreement belongs.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expires_at is not None:
            result['ExpiresAt'] = self.expires_at

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.signed_at is not None:
            result['SignedAt'] = self.signed_at

        if self.status is not None:
            result['Status'] = self.status

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpiresAt') is not None:
            self.expires_at = m.get('ExpiresAt')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SignedAt') is not None:
            self.signed_at = m.get('SignedAt')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

