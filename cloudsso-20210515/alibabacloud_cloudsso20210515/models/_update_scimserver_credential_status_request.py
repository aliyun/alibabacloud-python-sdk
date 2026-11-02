# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSCIMServerCredentialStatusRequest(DaraModel):
    def __init__(
        self,
        credential_id: str = None,
        directory_id: str = None,
        new_status: str = None,
    ):
        # The ID of the SCIM credential.
        self.credential_id = credential_id
        # The directory ID.
        self.directory_id = directory_id
        # The status of the SCIM credential. Valid values:
        # 
        # - Enabled: Enabled.
        # - Disabled: Disabled.
        self.new_status = new_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credential_id is not None:
            result['CredentialId'] = self.credential_id

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.new_status is not None:
            result['NewStatus'] = self.new_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialId') is not None:
            self.credential_id = m.get('CredentialId')

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('NewStatus') is not None:
            self.new_status = m.get('NewStatus')

        return self

