# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAcceleratorRequest(DaraModel):
    def __init__(
        self,
        accelerator_id: str = None,
        auto_pay: bool = None,
        auto_use_coupon: bool = None,
        bandwidth: int = None,
        client_token: str = None,
        description: str = None,
        name: str = None,
        region_id: str = None,
        spec: str = None,
    ):
        # The ID of the GA instance.
        # 
        # This parameter is required.
        self.accelerator_id = accelerator_id
        # Specifies whether to enable automatic payment. Valid values:
        # 
        # *   **false**: disables automatic payment. This is the default value. After an order is generated, you must go to the [Order Center](https://usercenter2-intl.aliyun.com/order/list) to complete the payment.
        # *   **true**: enables automatic payment. Payments are automatically completed.
        # 
        # >  This parameter takes effect only if you call the operation to upgrade a GA instance.
        self.auto_pay = auto_pay
        # Specifies whether to automatically pay bills by using coupons. Default value: false. Valid values:
        # 
        # *   **true**: automatically pays bills by using coupons.
        # *   **false**: does not automatically pay bills by using coupons.
        # 
        # >  This parameter takes effect only if the **AutoPay** parameter is set to **true**.
        self.auto_use_coupon = auto_use_coupon
        self.bandwidth = bandwidth
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # The description of the GA instance. The description can be up to 200 characters in length.
        self.description = description
        # The name of the GA instance.
        # 
        # The name must be 1 to 128 characters in length, and can contain letters, digits, periods (.), underscores (_), and hyphens (-). The name must start with a letter.
        self.name = name
        # The region where the GA instance is deployed. Set the value to **cn-hangzhou**.
        self.region_id = region_id
        # The specification of the GA instance. Valid values:
        # 
        # *   **1**: Small Ⅰ
        # *   **2**: Small Ⅱ
        # *   **3**: Small Ⅲ
        # *   **5**: Medium Ⅰ
        # *   **8**: Medium Ⅱ
        # *   **10**: Medium Ⅲ
        # *   **20**: Large Ⅰ
        # *   **30**: Large Ⅱ
        # *   **40**: Large Ⅲ
        # *   **50**: Large Ⅳ
        # *   **60**: Large Ⅴ
        # *   **70**: Large Ⅵ
        # *   **80**: Large VⅡ
        # *   **90**: Large VⅢ
        # *   **100**: Super Large Ⅰ
        # *   **200**: Super Large Ⅱ
        # 
        # >  The Large Ⅲ specification and higher specifications are available only for accounts that are added to the whitelist. To use these specifications, contact your Alibaba Cloud account manager.
        # 
        # Different specifications provide different capabilities. For more information, see [Instance specifications](https://help.aliyun.com/document_detail/153127.html).
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id

        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.auto_use_coupon is not None:
            result['AutoUseCoupon'] = self.auto_use_coupon

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.spec is not None:
            result['Spec'] = self.spec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')

        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('AutoUseCoupon') is not None:
            self.auto_use_coupon = m.get('AutoUseCoupon')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        return self

