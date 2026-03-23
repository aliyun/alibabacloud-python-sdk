# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSendifyInfoResponseBody(DaraModel):
    def __init__(
        self,
        buy_resource_package_url: str = None,
        buy_url: str = None,
        discount: str = None,
        downgrade_url: str = None,
        expire_time: str = None,
        learn_more_url: str = None,
        opened: bool = None,
        product_code: str = None,
        renew_url: str = None,
        request_id: str = None,
        spec_upgrade_url: str = None,
        status: str = None,
        support_trial: bool = None,
        upgrade_url: str = None,
    ):
        self.buy_resource_package_url = buy_resource_package_url
        self.buy_url = buy_url
        self.discount = discount
        self.downgrade_url = downgrade_url
        self.expire_time = expire_time
        self.learn_more_url = learn_more_url
        self.opened = opened
        self.product_code = product_code
        self.renew_url = renew_url
        self.request_id = request_id
        self.spec_upgrade_url = spec_upgrade_url
        self.status = status
        self.support_trial = support_trial
        self.upgrade_url = upgrade_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.buy_resource_package_url is not None:
            result['BuyResourcePackageUrl'] = self.buy_resource_package_url

        if self.buy_url is not None:
            result['BuyUrl'] = self.buy_url

        if self.discount is not None:
            result['Discount'] = self.discount

        if self.downgrade_url is not None:
            result['DowngradeUrl'] = self.downgrade_url

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.learn_more_url is not None:
            result['LearnMoreUrl'] = self.learn_more_url

        if self.opened is not None:
            result['Opened'] = self.opened

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.renew_url is not None:
            result['RenewUrl'] = self.renew_url

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.spec_upgrade_url is not None:
            result['SpecUpgradeUrl'] = self.spec_upgrade_url

        if self.status is not None:
            result['Status'] = self.status

        if self.support_trial is not None:
            result['SupportTrial'] = self.support_trial

        if self.upgrade_url is not None:
            result['UpgradeUrl'] = self.upgrade_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuyResourcePackageUrl') is not None:
            self.buy_resource_package_url = m.get('BuyResourcePackageUrl')

        if m.get('BuyUrl') is not None:
            self.buy_url = m.get('BuyUrl')

        if m.get('Discount') is not None:
            self.discount = m.get('Discount')

        if m.get('DowngradeUrl') is not None:
            self.downgrade_url = m.get('DowngradeUrl')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('LearnMoreUrl') is not None:
            self.learn_more_url = m.get('LearnMoreUrl')

        if m.get('Opened') is not None:
            self.opened = m.get('Opened')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('RenewUrl') is not None:
            self.renew_url = m.get('RenewUrl')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SpecUpgradeUrl') is not None:
            self.spec_upgrade_url = m.get('SpecUpgradeUrl')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SupportTrial') is not None:
            self.support_trial = m.get('SupportTrial')

        if m.get('UpgradeUrl') is not None:
            self.upgrade_url = m.get('UpgradeUrl')

        return self

