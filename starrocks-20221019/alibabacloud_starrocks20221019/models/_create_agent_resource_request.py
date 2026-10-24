# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAgentResourceRequest(DaraModel):
    def __init__(
        self,
        auto_renew: bool = None,
        cu: int = None,
        duration: int = None,
        instance_id: str = None,
        pay_type: str = None,
        pricing_cycle: str = None,
        promotion_option_no: str = None,
        spec_type: str = None,
    ):
        # Specifies whether to enable auto-renewal. This parameter is valid only when PayType is set to prePaid. Default value: false.
        self.auto_renew = auto_renew
        # The number of compute units (CUs). A CU is the basic metering unit of the service. One CU equals one vCPU and 4 GiB of memory. If SpecType is set to the memory-enhanced instance family, one CU equals one vCPU and 8 GiB of memory.
        # 
        # This parameter is required.
        self.cu = cu
        # The subscription duration. This parameter is valid only when PayType is set to prePaid.
        self.duration = duration
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The billing method. Valid values:<ol><li>prePaid: subscription.</li><li>postPaid: pay-as-you-go.</li></ol>
        # 
        # This parameter is required.
        self.pay_type = pay_type
        # The unit of the subscription duration. Valid values:<ul><li>Month</li><li>Year</li></ul>This parameter is valid only when PayType is set to prePaid.
        self.pricing_cycle = pricing_cycle
        # The coupon ID.
        self.promotion_option_no = promotion_option_no
        # The specification type of the compute group.
        self.spec_type = spec_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.cu is not None:
            result['Cu'] = self.cu

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle

        if self.promotion_option_no is not None:
            result['PromotionOptionNo'] = self.promotion_option_no

        if self.spec_type is not None:
            result['SpecType'] = self.spec_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('Cu') is not None:
            self.cu = m.get('Cu')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')

        if m.get('PromotionOptionNo') is not None:
            self.promotion_option_no = m.get('PromotionOptionNo')

        if m.get('SpecType') is not None:
            self.spec_type = m.get('SpecType')

        return self

