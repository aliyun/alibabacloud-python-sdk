# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_foasconsole20190601 import models as main_models
from darabonba.model import DaraModel

class RenewInstanceRequest(DaraModel):
    def __init__(
        self,
        renew_instance_request: main_models.RenewInstanceRequestRenewInstanceRequest = None,
    ):
        # This parameter is required.
        self.renew_instance_request = renew_instance_request

    def validate(self):
        if self.renew_instance_request:
            self.renew_instance_request.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.renew_instance_request is not None:
            result['RenewInstanceRequest'] = self.renew_instance_request.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RenewInstanceRequest') is not None:
            temp_model = main_models.RenewInstanceRequestRenewInstanceRequest()
            self.renew_instance_request = temp_model.from_map(m.get('RenewInstanceRequest'))

        return self

class RenewInstanceRequestRenewInstanceRequest(DaraModel):
    def __init__(
        self,
        duration: int = None,
        instance_id: str = None,
        pricing_cycle: str = None,
        region: str = None,
    ):
        # This parameter is required.
        self.duration = duration
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.pricing_cycle = pricing_cycle
        # This parameter is required.
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle

        if self.region is not None:
            result['Region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        return self

