# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_servicecatalog20210901 import models as main_models
from darabonba.model import DaraModel

class GetConstraintResponseBody(DaraModel):
    def __init__(
        self,
        constraint_detail: main_models.GetConstraintResponseBodyConstraintDetail = None,
        request_id: str = None,
    ):
        # The details of the constraint.
        self.constraint_detail = constraint_detail
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.constraint_detail:
            self.constraint_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.constraint_detail is not None:
            result['ConstraintDetail'] = self.constraint_detail.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConstraintDetail') is not None:
            temp_model = main_models.GetConstraintResponseBodyConstraintDetail()
            self.constraint_detail = temp_model.from_map(m.get('ConstraintDetail'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetConstraintResponseBodyConstraintDetail(DaraModel):
    def __init__(
        self,
        config: str = None,
        constraint_id: str = None,
        constraint_type: str = None,
        create_time: str = None,
        description: str = None,
        portfolio_id: str = None,
        product_id: str = None,
        product_name: str = None,
    ):
        # The configuration of the constraint.
        # 
        # Format: { "LocalRoleName": "\\<role_name>" }.
        self.config = config
        # The ID of the constraint.
        self.constraint_id = constraint_id
        # The type of the constraint.
        # 
        # The value is fixed as Launch, which indicates the launch constraint.
        self.constraint_type = constraint_type
        # The time when the constraint was created.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        # The description of the constraint.
        self.description = description
        # The ID of the product portfolio to which the constraint belongs.
        self.portfolio_id = portfolio_id
        # The ID of the product for which the constraint is created.
        self.product_id = product_id
        # The name of the product.
        self.product_name = product_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.constraint_id is not None:
            result['ConstraintId'] = self.constraint_id

        if self.constraint_type is not None:
            result['ConstraintType'] = self.constraint_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.product_name is not None:
            result['ProductName'] = self.product_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('ConstraintId') is not None:
            self.constraint_id = m.get('ConstraintId')

        if m.get('ConstraintType') is not None:
            self.constraint_type = m.get('ConstraintType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')

        return self

