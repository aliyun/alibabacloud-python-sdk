# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListResourceGroupMachineGroupsRequest(DaraModel):
    def __init__(
        self,
        creator_id: str = None,
        ecs_spec: str = None,
        machine_group_ids: str = None,
        name: str = None,
        order: str = None,
        order_instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        payment_duration: str = None,
        payment_duration_unit: str = None,
        payment_type: str = None,
        sort_by: str = None,
        status: str = None,
    ):
        self.creator_id = creator_id
        self.ecs_spec = ecs_spec
        self.machine_group_ids = machine_group_ids
        self.name = name
        self.order = order
        self.order_instance_id = order_instance_id
        self.page_number = page_number
        self.page_size = page_size
        self.payment_duration = payment_duration
        self.payment_duration_unit = payment_duration_unit
        self.payment_type = payment_type
        self.sort_by = sort_by
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator_id is not None:
            result['CreatorID'] = self.creator_id

        if self.ecs_spec is not None:
            result['EcsSpec'] = self.ecs_spec

        if self.machine_group_ids is not None:
            result['MachineGroupIDs'] = self.machine_group_ids

        if self.name is not None:
            result['Name'] = self.name

        if self.order is not None:
            result['Order'] = self.order

        if self.order_instance_id is not None:
            result['OrderInstanceId'] = self.order_instance_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.payment_duration is not None:
            result['PaymentDuration'] = self.payment_duration

        if self.payment_duration_unit is not None:
            result['PaymentDurationUnit'] = self.payment_duration_unit

        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatorID') is not None:
            self.creator_id = m.get('CreatorID')

        if m.get('EcsSpec') is not None:
            self.ecs_spec = m.get('EcsSpec')

        if m.get('MachineGroupIDs') is not None:
            self.machine_group_ids = m.get('MachineGroupIDs')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('OrderInstanceId') is not None:
            self.order_instance_id = m.get('OrderInstanceId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PaymentDuration') is not None:
            self.payment_duration = m.get('PaymentDuration')

        if m.get('PaymentDurationUnit') is not None:
            self.payment_duration_unit = m.get('PaymentDurationUnit')

        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

