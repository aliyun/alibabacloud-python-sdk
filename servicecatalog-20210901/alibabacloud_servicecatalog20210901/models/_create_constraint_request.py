# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateConstraintRequest(DaraModel):
    def __init__(
        self,
        config: str = None,
        constraint_type: str = None,
        description: str = None,
        portfolio_id: str = None,
        product_id: str = None,
    ):
        # The configuration of the constraint.
        # 
        # Format: { "LocalRoleName": "\\<role_name>" }.
        # 
        # This parameter is required.
        self.config = config
        # The type of the constraint.
        # 
        # The value is fixed as Launch, which specifies the launch constraint.
        # 
        # This parameter is required.
        self.constraint_type = constraint_type
        # The description of the constraint.
        # 
        # The value must be 1 to 128 characters in length.
        self.description = description
        # The ID of the product portfolio to which the constraint belongs.
        # 
        # This parameter is required.
        self.portfolio_id = portfolio_id
        # The ID of the product for which the constraint is created.
        # 
        # This parameter is required.
        self.product_id = product_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.constraint_type is not None:
            result['ConstraintType'] = self.constraint_type

        if self.description is not None:
            result['Description'] = self.description

        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('ConstraintType') is not None:
            self.constraint_type = m.get('ConstraintType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        return self

