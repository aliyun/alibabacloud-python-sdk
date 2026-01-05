# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCrossCloudLevelsRequest(DaraModel):
    def __init__(
        self,
        dbtype: str = None,
        dbversion: str = None,
        project_id: str = None,
        storage_type: str = None,
    ):
        # This parameter is required.
        self.dbtype = dbtype
        self.dbversion = dbversion
        # This parameter is required.
        self.project_id = project_id
        # This parameter is required.
        self.storage_type = storage_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbtype is not None:
            result['DBType'] = self.dbtype

        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')

        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        return self

