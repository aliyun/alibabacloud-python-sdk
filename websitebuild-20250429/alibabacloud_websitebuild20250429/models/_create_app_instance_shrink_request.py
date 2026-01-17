# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAppInstanceShrinkRequest(DaraModel):
    def __init__(
        self,
        application_type: str = None,
        auto_renew: bool = None,
        client_token: str = None,
        deploy_area: str = None,
        duration: int = None,
        extend: str = None,
        payment_type: str = None,
        pricing_cycle: str = None,
        quantity: int = None,
        resource_group_id: str = None,
        site_version: str = None,
        tags_shrink: str = None,
    ):
        # Application type
        self.application_type = application_type
        # Whether to enable auto-renewal upon expiration
        self.auto_renew = auto_renew
        # Ensures idempotence of the request. Generate a unique value from your client to ensure that it is unique across different requests. ClientToken only supports ASCII characters and cannot exceed 64 characters
        self.client_token = client_token
        # Deployment area
        self.deploy_area = deploy_area
        # Required. The number of subscription periods
        self.duration = duration
        # Extended information
        self.extend = extend
        # Payment type
        self.payment_type = payment_type
        # Required. The unit of the subscription period, Year: Year, Month: Month, Day: Day, Hour: Hour
        self.pricing_cycle = pricing_cycle
        # Required. The quantity of instances to be ordered.
        self.quantity = quantity
        self.resource_group_id = resource_group_id
        # Site version
        self.site_version = site_version
        self.tags_shrink = tags_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_type is not None:
            result['ApplicationType'] = self.application_type

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.deploy_area is not None:
            result['DeployArea'] = self.deploy_area

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.extend is not None:
            result['Extend'] = self.extend

        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type

        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle

        if self.quantity is not None:
            result['Quantity'] = self.quantity

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.site_version is not None:
            result['SiteVersion'] = self.site_version

        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DeployArea') is not None:
            self.deploy_area = m.get('DeployArea')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Extend') is not None:
            self.extend = m.get('Extend')

        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')

        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')

        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')

        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')

        return self

