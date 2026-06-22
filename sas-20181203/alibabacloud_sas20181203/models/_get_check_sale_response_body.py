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
        # The sales information of cloud service configuration check.
        self.check_sale = check_sale
        # The ID of the request. The ID is a unique identifier that Alibaba Cloud generates for the request and can be used to troubleshoot issues.
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
        instance_consume_count: int = None,
        instance_hybrid_post_latest_cycled_resource_count: int = None,
        instance_post_consume_count: int = None,
        instance_purchase_count: int = None,
        loyal_user: bool = None,
        purchase_count: int = None,
        sale_user_type: int = None,
    ):
        # The number of consumed authorized quotas.
        self.consume_count = consume_count
        self.instance_consume_count = instance_consume_count
        self.instance_hybrid_post_latest_cycled_resource_count = instance_hybrid_post_latest_cycled_resource_count
        self.instance_post_consume_count = instance_post_consume_count
        self.instance_purchase_count = instance_purchase_count
        # Indicates whether the user is an existing user who used the cloud service configuration check feature before the sales feature was released on July 7, 2023. Valid values:
        # - **true**: The user is an existing user.
        # - **false**: The user is not an existing user.
        self.loyal_user = loyal_user
        # The number of purchased authorized quotas.
        self.purchase_count = purchase_count
        # The type of the sales user. Valid values:
        # - **1**: full-feature user who can use all check items.
        # - **2**: user who needs to upgrade and can only use check items that were available before the sales feature was released on July 7, 2023.
        # - **3**: user who needs to purchase the feature and cannot use the cloud service configuration check feature.
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

        if self.instance_consume_count is not None:
            result['InstanceConsumeCount'] = self.instance_consume_count

        if self.instance_hybrid_post_latest_cycled_resource_count is not None:
            result['InstanceHybridPostLatestCycledResourceCount'] = self.instance_hybrid_post_latest_cycled_resource_count

        if self.instance_post_consume_count is not None:
            result['InstancePostConsumeCount'] = self.instance_post_consume_count

        if self.instance_purchase_count is not None:
            result['InstancePurchaseCount'] = self.instance_purchase_count

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

        if m.get('InstanceConsumeCount') is not None:
            self.instance_consume_count = m.get('InstanceConsumeCount')

        if m.get('InstanceHybridPostLatestCycledResourceCount') is not None:
            self.instance_hybrid_post_latest_cycled_resource_count = m.get('InstanceHybridPostLatestCycledResourceCount')

        if m.get('InstancePostConsumeCount') is not None:
            self.instance_post_consume_count = m.get('InstancePostConsumeCount')

        if m.get('InstancePurchaseCount') is not None:
            self.instance_purchase_count = m.get('InstancePurchaseCount')

        if m.get('LoyalUser') is not None:
            self.loyal_user = m.get('LoyalUser')

        if m.get('PurchaseCount') is not None:
            self.purchase_count = m.get('PurchaseCount')

        if m.get('SaleUserType') is not None:
            self.sale_user_type = m.get('SaleUserType')

        return self

