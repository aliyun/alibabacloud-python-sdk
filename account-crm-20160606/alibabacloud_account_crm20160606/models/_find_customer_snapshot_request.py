# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FindCustomerSnapshotRequest(DaraModel):
    def __init__(
        self,
        info_type: str = None,
        pk: int = None,
        version_id: str = None,
    ):
        # This parameter is required.
        self.info_type = info_type
        # This parameter is required.
        self.pk = pk
        # This parameter is required.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.info_type is not None:
            result['InfoType'] = self.info_type

        if self.pk is not None:
            result['Pk'] = self.pk

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InfoType') is not None:
            self.info_type = m.get('InfoType')

        if m.get('Pk') is not None:
            self.pk = m.get('Pk')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        return self

