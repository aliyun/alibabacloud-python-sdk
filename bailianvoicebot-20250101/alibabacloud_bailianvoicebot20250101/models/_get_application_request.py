# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetApplicationRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        business_unit_id: str = None,
    ):
        # This parameter is required.
        self.application_id = application_id
        # This parameter is required.
        self.business_unit_id = business_unit_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.business_unit_id is not None:
            result['BusinessUnitId'] = self.business_unit_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('BusinessUnitId') is not None:
            self.business_unit_id = m.get('BusinessUnitId')

        return self

