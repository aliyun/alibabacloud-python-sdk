# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDBInstanceTDERequest(DaraModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        encryption_key: str = None,
        region_id: str = None,
        role_arn: str = None,
        tdestatus: int = None,
    ):
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        self.encryption_key = encryption_key
        # This parameter is required.
        self.region_id = region_id
        self.role_arn = role_arn
        # This parameter is required.
        self.tdestatus = tdestatus

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.encryption_key is not None:
            result['EncryptionKey'] = self.encryption_key

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn

        if self.tdestatus is not None:
            result['TDEStatus'] = self.tdestatus

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('EncryptionKey') is not None:
            self.encryption_key = m.get('EncryptionKey')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')

        if m.get('TDEStatus') is not None:
            self.tdestatus = m.get('TDEStatus')

        return self

