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
        # - **false** (default): Disables automatic payment. After an order is generated, you must go to the [Order Hub](https://usercenter2-intl.aliyun.com/order/list) to complete the payment.
        # 
        # - **true**: Enables automatic payment. The system automatically pays the bill.
        # 
        # > This parameter is valid only for upgrade orders.
        self.auto_pay = auto_pay
        # Specifies whether to automatically use a coupon to pay for the bill. Valid values:
        # 
        # - **true**: Use a coupon.
        # 
        # - **false** (default): Do not use a coupon.
        # 
        # > This parameter is valid only if **AutoPay** is set to **true**.
        self.auto_use_coupon = auto_use_coupon
        # The bandwidth of the standard GA instance. Unit: **Mbps**.
        # 
        # Valid values: 200 to 5000.
        # 
        # > This parameter is valid only when the access mode of the acceleration area is Anycast.
        self.bandwidth = bandwidth
        # The client token that is used to ensure the idempotence of the request.
        # 
        # Generate a parameter value from your client to make sure that the value is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the request as the **ClientToken**. The **RequestId** of each API request may be different.
        self.client_token = client_token
        # The description of the GA instance. The description can be up to 200 characters in length.
        self.description = description
        # The name of the GA instance.
        # 
        # The name must be 1 to 128 characters in length, start with a letter or a Chinese character, and can contain digits, periods (.), underscores (_), and hyphens (-).
        self.name = name
        # The region ID of the GA instance. Set the value to **cn-hangzhou**.
        self.region_id = region_id
        # The specification of the GA instance. Valid values:
        # 
        # - **1**: Small I
        # 
        # - **2**: Small II
        # 
        # - **3**: Small III
        # 
        # - **5**: Medium I
        # 
        # - **8**: Medium II
        # 
        # - **10**: Medium III
        # 
        # - **20**: Large I
        # 
        # - **30**: Large II
        # 
        # - **40**: Large III
        # 
        # - **50**: Large IV
        # 
        # - **60**: Large V
        # 
        # - **70**: Large VI
        # 
        # - **80**: Large VII
        # 
        # - **90**: Large VIII
        # 
        # - **100**: Ultra-large I
        # 
        # - **200**: Ultra-large II
        # 
        # > Large III and higher specifications are available only to whitelisted users. To use these specifications, contact your account manager.
        # 
        # The definitions of instance types vary. For more information, see [Instance types](https://help.aliyun.com/document_detail/153127.html).
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

