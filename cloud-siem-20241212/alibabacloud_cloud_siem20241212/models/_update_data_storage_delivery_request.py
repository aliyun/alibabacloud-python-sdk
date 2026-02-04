# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDataStorageDeliveryRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        log_code: str = None,
        log_delivery_status: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.lang = lang
        # This parameter is required.
        self.log_code = log_code
        self.log_delivery_status = log_delivery_status
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.log_code is not None:
            result['LogCode'] = self.log_code

        if self.log_delivery_status is not None:
            result['LogDeliveryStatus'] = self.log_delivery_status

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('LogCode') is not None:
            self.log_code = m.get('LogCode')

        if m.get('LogDeliveryStatus') is not None:
            self.log_delivery_status = m.get('LogDeliveryStatus')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        return self

