# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateApplicationRequest(DaraModel):
    def __init__(
        self,
        business_unit_id: str = None,
        concurrency: int = None,
        description: str = None,
        name: str = None,
        nlu_access_type: str = None,
    ):
        # This parameter is required.
        self.business_unit_id = business_unit_id
        self.concurrency = concurrency
        self.description = description
        # This parameter is required.
        self.name = name
        self.nlu_access_type = nlu_access_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_unit_id is not None:
            result['BusinessUnitId'] = self.business_unit_id

        if self.concurrency is not None:
            result['Concurrency'] = self.concurrency

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.nlu_access_type is not None:
            result['NluAccessType'] = self.nlu_access_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessUnitId') is not None:
            self.business_unit_id = m.get('BusinessUnitId')

        if m.get('Concurrency') is not None:
            self.concurrency = m.get('Concurrency')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NluAccessType') is not None:
            self.nlu_access_type = m.get('NluAccessType')

        return self

