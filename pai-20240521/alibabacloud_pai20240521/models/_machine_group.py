# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class MachineGroup(DaraModel):
    def __init__(
        self,
        creator_id: str = None,
        default_driver: str = None,
        ecs_count: int = None,
        ecs_spec: str = None,
        gmt_created_time: str = None,
        gmt_expired_time: str = None,
        gmt_modified_time: str = None,
        gmt_started_time: str = None,
        machine_group_id: str = None,
        order_instance_id: str = None,
        payment_duration: str = None,
        payment_duration_unit: str = None,
        payment_type: str = None,
        reason_code: str = None,
        reason_message: str = None,
        resource_group_id: str = None,
        status: str = None,
        supported_drivers: List[str] = None,
    ):
        self.creator_id = creator_id
        self.default_driver = default_driver
        self.ecs_count = ecs_count
        self.ecs_spec = ecs_spec
        self.gmt_created_time = gmt_created_time
        self.gmt_expired_time = gmt_expired_time
        self.gmt_modified_time = gmt_modified_time
        self.gmt_started_time = gmt_started_time
        self.machine_group_id = machine_group_id
        self.order_instance_id = order_instance_id
        self.payment_duration = payment_duration
        self.payment_duration_unit = payment_duration_unit
        self.payment_type = payment_type
        self.reason_code = reason_code
        self.reason_message = reason_message
        self.resource_group_id = resource_group_id
        self.status = status
        self.supported_drivers = supported_drivers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator_id is not None:
            result['CreatorID'] = self.creator_id

        if self.default_driver is not None:
            result['DefaultDriver'] = self.default_driver

        if self.ecs_count is not None:
            result['EcsCount'] = self.ecs_count

        if self.ecs_spec is not None:
            result['EcsSpec'] = self.ecs_spec

        if self.gmt_created_time is not None:
            result['GmtCreatedTime'] = self.gmt_created_time

        if self.gmt_expired_time is not None:
            result['GmtExpiredTime'] = self.gmt_expired_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.gmt_started_time is not None:
            result['GmtStartedTime'] = self.gmt_started_time

        if self.machine_group_id is not None:
            result['MachineGroupID'] = self.machine_group_id

        if self.order_instance_id is not None:
            result['OrderInstanceId'] = self.order_instance_id

        if self.payment_duration is not None:
            result['PaymentDuration'] = self.payment_duration

        if self.payment_duration_unit is not None:
            result['PaymentDurationUnit'] = self.payment_duration_unit

        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type

        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code

        if self.reason_message is not None:
            result['ReasonMessage'] = self.reason_message

        if self.resource_group_id is not None:
            result['ResourceGroupID'] = self.resource_group_id

        if self.status is not None:
            result['Status'] = self.status

        if self.supported_drivers is not None:
            result['SupportedDrivers'] = self.supported_drivers

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatorID') is not None:
            self.creator_id = m.get('CreatorID')

        if m.get('DefaultDriver') is not None:
            self.default_driver = m.get('DefaultDriver')

        if m.get('EcsCount') is not None:
            self.ecs_count = m.get('EcsCount')

        if m.get('EcsSpec') is not None:
            self.ecs_spec = m.get('EcsSpec')

        if m.get('GmtCreatedTime') is not None:
            self.gmt_created_time = m.get('GmtCreatedTime')

        if m.get('GmtExpiredTime') is not None:
            self.gmt_expired_time = m.get('GmtExpiredTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('GmtStartedTime') is not None:
            self.gmt_started_time = m.get('GmtStartedTime')

        if m.get('MachineGroupID') is not None:
            self.machine_group_id = m.get('MachineGroupID')

        if m.get('OrderInstanceId') is not None:
            self.order_instance_id = m.get('OrderInstanceId')

        if m.get('PaymentDuration') is not None:
            self.payment_duration = m.get('PaymentDuration')

        if m.get('PaymentDurationUnit') is not None:
            self.payment_duration_unit = m.get('PaymentDurationUnit')

        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')

        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')

        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')

        if m.get('ResourceGroupID') is not None:
            self.resource_group_id = m.get('ResourceGroupID')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SupportedDrivers') is not None:
            self.supported_drivers = m.get('SupportedDrivers')

        return self

