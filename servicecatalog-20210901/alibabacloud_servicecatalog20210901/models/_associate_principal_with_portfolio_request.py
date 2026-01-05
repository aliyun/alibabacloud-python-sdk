# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AssociatePrincipalWithPortfolioRequest(DaraModel):
    def __init__(
        self,
        portfolio_id: str = None,
        principal_id: str = None,
        principal_type: str = None,
    ):
        # This parameter is required.
        self.portfolio_id = portfolio_id
        # This parameter is required.
        self.principal_id = principal_id
        # This parameter is required.
        self.principal_type = principal_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id

        if self.principal_id is not None:
            result['PrincipalId'] = self.principal_id

        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')

        if m.get('PrincipalId') is not None:
            self.principal_id = m.get('PrincipalId')

        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')

        return self

