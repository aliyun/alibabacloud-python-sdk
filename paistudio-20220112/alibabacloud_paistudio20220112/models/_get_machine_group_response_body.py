# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetMachineGroupResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        default_driver: str = None,
        duration: str = None,
        ecs_type: str = None,
        gmt_created: str = None,
        gmt_expired: str = None,
        gmt_modified: str = None,
        gmt_started: str = None,
        machine_group_id: str = None,
        order_id: str = None,
        order_instance_id: str = None,
        pairesource_id: str = None,
        pay_type: str = None,
        pricing_cycle: str = None,
        region_id: str = None,
        request_id: str = None,
        status: str = None,
        supported_drivers: List[str] = None,
    ):
        self.count = count
        self.default_driver = default_driver
        self.duration = duration
        self.ecs_type = ecs_type
        self.gmt_created = gmt_created
        self.gmt_expired = gmt_expired
        self.gmt_modified = gmt_modified
        self.gmt_started = gmt_started
        self.machine_group_id = machine_group_id
        self.order_id = order_id
        self.order_instance_id = order_instance_id
        self.pairesource_id = pairesource_id
        self.pay_type = pay_type
        self.pricing_cycle = pricing_cycle
        self.region_id = region_id
        self.request_id = request_id
        self.status = status
        self.supported_drivers = supported_drivers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.default_driver is not None:
            result['DefaultDriver'] = self.default_driver

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.ecs_type is not None:
            result['EcsType'] = self.ecs_type

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.gmt_expired is not None:
            result['GmtExpired'] = self.gmt_expired

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.gmt_started is not None:
            result['GmtStarted'] = self.gmt_started

        if self.machine_group_id is not None:
            result['MachineGroupID'] = self.machine_group_id

        if self.order_id is not None:
            result['OrderID'] = self.order_id

        if self.order_instance_id is not None:
            result['OrderInstanceId'] = self.order_instance_id

        if self.pairesource_id is not None:
            result['PAIResourceID'] = self.pairesource_id

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle

        if self.region_id is not None:
            result['RegionID'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.supported_drivers is not None:
            result['SupportedDrivers'] = self.supported_drivers

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('DefaultDriver') is not None:
            self.default_driver = m.get('DefaultDriver')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('EcsType') is not None:
            self.ecs_type = m.get('EcsType')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('GmtExpired') is not None:
            self.gmt_expired = m.get('GmtExpired')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('GmtStarted') is not None:
            self.gmt_started = m.get('GmtStarted')

        if m.get('MachineGroupID') is not None:
            self.machine_group_id = m.get('MachineGroupID')

        if m.get('OrderID') is not None:
            self.order_id = m.get('OrderID')

        if m.get('OrderInstanceId') is not None:
            self.order_instance_id = m.get('OrderInstanceId')

        if m.get('PAIResourceID') is not None:
            self.pairesource_id = m.get('PAIResourceID')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')

        if m.get('RegionID') is not None:
            self.region_id = m.get('RegionID')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SupportedDrivers') is not None:
            self.supported_drivers = m.get('SupportedDrivers')

        return self

