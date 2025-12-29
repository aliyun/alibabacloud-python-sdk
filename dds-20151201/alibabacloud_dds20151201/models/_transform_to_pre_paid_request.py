# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TransformToPrePaidRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        auto_renew: str = None,
        business_info: str = None,
        coupon_no: str = None,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        period: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Specifies whether to enable automatic payment. Valid values:
        # 
        # *   **true**: enables automatic payment.
        # *   **false**: disables automatic payment. For more information, see [Renew an ApsaraDB for MongoDB subscription instance](https://help.aliyun.com/document_detail/85052.html).
        # 
        # >  Default value: **true**.
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal for the instance. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # >  Default value: **false**.
        self.auto_renew = auto_renew
        # The business information. This is an additional parameter.
        self.business_info = business_info
        # The coupon code. Default value: `youhuiquan_promotion_option_id_for_blank`.
        self.coupon_no = coupon_no
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The subscription duration of the instance. Unit: months. Valid values: **1**, **2**, **3**, **4**, **5**, **6**, **7**, **8**, **9**, **12**, **24**, and **36**.
        # 
        # This parameter is required.
        self.period = period
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.business_info is not None:
            result['BusinessInfo'] = self.business_info

        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.period is not None:
            result['Period'] = self.period

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('BusinessInfo') is not None:
            self.business_info = m.get('BusinessInfo')

        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

