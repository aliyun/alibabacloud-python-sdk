# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateMobileAgentPackageRequest(DaraModel):
    def __init__(
        self,
        amount: str = None,
        auto_pay: bool = None,
        auto_renew: bool = None,
        biz_region_id: str = None,
        credit_amount: str = None,
        credit_config: str = None,
        image_id: str = None,
        instance_name: str = None,
        mobile_agent_package_spec: str = None,
        package_spec_id: int = None,
        paid_callback_url: str = None,
        period: int = None,
        period_unit: str = None,
        promotion_id: str = None,
    ):
        # The number of packages.
        self.amount = amount
        # Specifies whether to enable auto-payment. Valid values:
        # 
        # - **true**: Enables auto-payment. You must ensure that your account balance is sufficient.
        # 
        # - **false** (default): An unpaid order is generated. Your account is not charged.
        # 
        # > If your account balance is insufficient, you can set this parameter to `false` to generate an unpaid order. Then, you can log in to the Wuying Cloud Phone management console to pay for the order.
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal for the instance. Valid values:
        # 
        # - **true**: Enables auto-renewal.
        # 
        # - **false** (default): Disables auto-renewal.
        self.auto_renew = auto_renew
        # The region where the instance is located. Currently, only `cn-hangzhou` is supported.
        self.biz_region_id = biz_region_id
        # The credit amount.
        self.credit_amount = credit_amount
        # The credit limit configuration.
        self.credit_config = credit_config
        self.image_id = image_id
        # The instance name.
        self.instance_name = instance_name
        # The package specification.
        self.mobile_agent_package_spec = mobile_agent_package_spec
        self.package_spec_id = package_spec_id
        # The callback URL to which the user is redirected after a successful payment.
        self.paid_callback_url = paid_callback_url
        # The subscription period. The unit of the period is specified by the `PeriodUnit` parameter.
        self.period = period
        # The unit of the subscription period.
        # Valid values:
        # 
        # - **Month**
        # 
        # - **Year**
        self.period_unit = period_unit
        # The promotion ID.
        self.promotion_id = promotion_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

        if self.credit_amount is not None:
            result['CreditAmount'] = self.credit_amount

        if self.credit_config is not None:
            result['CreditConfig'] = self.credit_config

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.mobile_agent_package_spec is not None:
            result['MobileAgentPackageSpec'] = self.mobile_agent_package_spec

        if self.package_spec_id is not None:
            result['PackageSpecId'] = self.package_spec_id

        if self.paid_callback_url is not None:
            result['PaidCallbackUrl'] = self.paid_callback_url

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('CreditAmount') is not None:
            self.credit_amount = m.get('CreditAmount')

        if m.get('CreditConfig') is not None:
            self.credit_config = m.get('CreditConfig')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('MobileAgentPackageSpec') is not None:
            self.mobile_agent_package_spec = m.get('MobileAgentPackageSpec')

        if m.get('PackageSpecId') is not None:
            self.package_spec_id = m.get('PackageSpecId')

        if m.get('PaidCallbackUrl') is not None:
            self.paid_callback_url = m.get('PaidCallbackUrl')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')

        return self

