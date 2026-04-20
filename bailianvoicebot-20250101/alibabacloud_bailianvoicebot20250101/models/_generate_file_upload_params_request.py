# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateFileUploadParamsRequest(DaraModel):
    def __init__(
        self,
        business_type: str = None,
        business_unit_id: str = None,
        file_name: str = None,
    ):
        self.business_type = business_type
        self.business_unit_id = business_unit_id
        self.file_name = file_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_type is not None:
            result['BusinessType'] = self.business_type

        if self.business_unit_id is not None:
            result['BusinessUnitId'] = self.business_unit_id

        if self.file_name is not None:
            result['FileName'] = self.file_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')

        if m.get('BusinessUnitId') is not None:
            self.business_unit_id = m.get('BusinessUnitId')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        return self

