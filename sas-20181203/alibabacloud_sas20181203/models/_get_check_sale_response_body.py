# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetCheckSaleResponseBody(DaraModel):
    def __init__(
        self,
        check_sale: main_models.GetCheckSaleResponseBodyCheckSale = None,
        request_id: str = None,
    ):
        # The sales information about the configuration assessment quota.
        self.check_sale = check_sale
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.check_sale:
            self.check_sale.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_sale is not None:
            result['CheckSale'] = self.check_sale.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckSale') is not None:
            temp_model = main_models.GetCheckSaleResponseBodyCheckSale()
            self.check_sale = temp_model.from_map(m.get('CheckSale'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetCheckSaleResponseBodyCheckSale(DaraModel):
    def __init__(
        self,
        consume_count: int = None,
        loyal_user: bool = None,
        purchase_count: int = None,
        sale_user_type: int = None,
    ):
        # The consumed quota.
        self.consume_count = consume_count
        # Indicates whether the user is an existing user and whether the user uses the configuration assessment feature before the feature is released for sale on July 07, 2023. Valid values:
        # 
        # *   **true**: existing user
        # *   **false**: new user
        self.loyal_user = loyal_user
        # The purchased quota.
        self.purchase_count = purchase_count
        # The type of the user. Valid values:
        # 
        # *   **1**: a user who can use all check items.
        # *   **2**: an user who can only use the check items before the release of the feature on July 07, 2023. This type of users must upgrade Security Center before the users can use all check items.
        # *   **3**: a new user who cannot use the configuration assessment feature. This type of users must make a purchase before the users can use the feature.
        self.sale_user_type = sale_user_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consume_count is not None:
            result['ConsumeCount'] = self.consume_count

        if self.loyal_user is not None:
            result['LoyalUser'] = self.loyal_user

        if self.purchase_count is not None:
            result['PurchaseCount'] = self.purchase_count

        if self.sale_user_type is not None:
            result['SaleUserType'] = self.sale_user_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumeCount') is not None:
            self.consume_count = m.get('ConsumeCount')

        if m.get('LoyalUser') is not None:
            self.loyal_user = m.get('LoyalUser')

        if m.get('PurchaseCount') is not None:
            self.purchase_count = m.get('PurchaseCount')

        if m.get('SaleUserType') is not None:
            self.sale_user_type = m.get('SaleUserType')

        return self

