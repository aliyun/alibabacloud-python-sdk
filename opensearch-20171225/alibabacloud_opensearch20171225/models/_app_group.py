# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class AppGroup(DaraModel):
    def __init__(
        self,
        charge_type: str = None,
        description: str = None,
        domain: str = None,
        name: str = None,
        order: main_models.AppGroupOrder = None,
        quota: main_models.Quota = None,
        resource_group_id: str = None,
        type: str = None,
    ):
        self.charge_type = charge_type
        self.description = description
        self.domain = domain
        self.name = name
        self.order = order
        self.quota = quota
        self.resource_group_id = resource_group_id
        self.type = type

    def validate(self):
        if self.order:
            self.order.validate()
        if self.quota:
            self.quota.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type

        if self.description is not None:
            result['description'] = self.description

        if self.domain is not None:
            result['domain'] = self.domain

        if self.name is not None:
            result['name'] = self.name

        if self.order is not None:
            result['order'] = self.order.to_map()

        if self.quota is not None:
            result['quota'] = self.quota.to_map()

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('domain') is not None:
            self.domain = m.get('domain')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('order') is not None:
            temp_model = main_models.AppGroupOrder()
            self.order = temp_model.from_map(m.get('order'))

        if m.get('quota') is not None:
            temp_model = main_models.Quota()
            self.quota = temp_model.from_map(m.get('quota'))

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class AppGroupOrder(DaraModel):
    def __init__(
        self,
        auto_renew: bool = None,
        duration: int = None,
        pricing_cycle: str = None,
    ):
        self.auto_renew = auto_renew
        self.duration = duration
        self.pricing_cycle = pricing_cycle

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_renew is not None:
            result['autoRenew'] = self.auto_renew

        if self.duration is not None:
            result['duration'] = self.duration

        if self.pricing_cycle is not None:
            result['pricingCycle'] = self.pricing_cycle

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoRenew') is not None:
            self.auto_renew = m.get('autoRenew')

        if m.get('duration') is not None:
            self.duration = m.get('duration')

        if m.get('pricingCycle') is not None:
            self.pricing_cycle = m.get('pricingCycle')

        return self

