# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteServiceAccountRequest(DaraModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        region_id: str = None,
        service_account_type: str = None,
    ):
        # The instance name.
        # 
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        # The region where the instance resides.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The service account type.
        # 
        # This parameter is required.
        self.service_account_type = service_account_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.service_account_type is not None:
            result['ServiceAccountType'] = self.service_account_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ServiceAccountType') is not None:
            self.service_account_type = m.get('ServiceAccountType')

        return self

