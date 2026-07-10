# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteLangfuseUserRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        email: str = None,
        region_id: str = None,
    ):
        # The Langfuse instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The email address of the user.
        # 
        # This parameter is required.
        self.email = email
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

        if self.email is not None:
            result['Email'] = self.email

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

