# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSmsVerifyStatisticRecordsExportTaskRequest(DaraModel):
    def __init__(
        self,
        from_date: int = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scheme_name: str = None,
        to_date: int = None,
    ):
        # This parameter is required.
        self.from_date = from_date
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.scheme_name = scheme_name
        # This parameter is required.
        self.to_date = to_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_date is not None:
            result['FromDate'] = self.from_date

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.scheme_name is not None:
            result['SchemeName'] = self.scheme_name

        if self.to_date is not None:
            result['ToDate'] = self.to_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromDate') is not None:
            self.from_date = m.get('FromDate')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SchemeName') is not None:
            self.scheme_name = m.get('SchemeName')

        if m.get('ToDate') is not None:
            self.to_date = m.get('ToDate')

        return self

