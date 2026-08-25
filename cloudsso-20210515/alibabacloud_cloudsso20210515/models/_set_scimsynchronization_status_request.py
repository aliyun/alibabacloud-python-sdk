# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetSCIMSynchronizationStatusRequest(DaraModel):
    def __init__(
        self,
        directory_id: str = None,
        scimsynchronization_status: str = None,
    ):
        # The ID of the directory.
        self.directory_id = directory_id
        # The status of SCIM synchronization. Valid values:
        # 
        # *   Enabled
        # *   Disabled
        self.scimsynchronization_status = scimsynchronization_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.scimsynchronization_status is not None:
            result['SCIMSynchronizationStatus'] = self.scimsynchronization_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('SCIMSynchronizationStatus') is not None:
            self.scimsynchronization_status = m.get('SCIMSynchronizationStatus')

        return self

