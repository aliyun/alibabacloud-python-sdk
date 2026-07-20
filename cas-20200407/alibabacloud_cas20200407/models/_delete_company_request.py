# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteCompanyRequest(DaraModel):
    def __init__(
        self,
        company_id: int = None,
    ):
        # The company ID.
        # 
        # This parameter is required.
        self.company_id = company_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.company_id is not None:
            result['CompanyId'] = self.company_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompanyId') is not None:
            self.company_id = m.get('CompanyId')

        return self

