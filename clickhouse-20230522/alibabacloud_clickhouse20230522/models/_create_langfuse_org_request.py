# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateLangfuseOrgRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        name: str = None,
        owner_email: str = None,
        region_id: str = None,
    ):
        # The Langfuse instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The name of the Langfuse organization.
        # 
        # This parameter is required.
        self.name = name
        # The email address of the Langfuse organization owner.
        # 
        # This parameter is required.
        self.owner_email = owner_email
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_email is not None:
            result['OwnerEmail'] = self.owner_email

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerEmail') is not None:
            self.owner_email = m.get('OwnerEmail')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

