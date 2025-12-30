# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AiRtcLicenseInfoDTO(DaraModel):
    def __init__(
        self,
        available_capacity: int = None,
        begin_on: str = None,
        contract_no: str = None,
        creation_time: str = None,
        expired_on: str = None,
        instance_id: str = None,
        license_count: int = None,
        license_item_id: str = None,
        modification_time: str = None,
        status: int = None,
        type: int = None,
        valid_days: int = None,
    ):
        self.available_capacity = available_capacity
        self.begin_on = begin_on
        self.contract_no = contract_no
        self.creation_time = creation_time
        self.expired_on = expired_on
        self.instance_id = instance_id
        self.license_count = license_count
        self.license_item_id = license_item_id
        self.modification_time = modification_time
        self.status = status
        self.type = type
        self.valid_days = valid_days

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_capacity is not None:
            result['AvailableCapacity'] = self.available_capacity

        if self.begin_on is not None:
            result['BeginOn'] = self.begin_on

        if self.contract_no is not None:
            result['ContractNo'] = self.contract_no

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.expired_on is not None:
            result['ExpiredOn'] = self.expired_on

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.license_count is not None:
            result['LicenseCount'] = self.license_count

        if self.license_item_id is not None:
            result['LicenseItemId'] = self.license_item_id

        if self.modification_time is not None:
            result['ModificationTime'] = self.modification_time

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        if self.valid_days is not None:
            result['ValidDays'] = self.valid_days

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableCapacity') is not None:
            self.available_capacity = m.get('AvailableCapacity')

        if m.get('BeginOn') is not None:
            self.begin_on = m.get('BeginOn')

        if m.get('ContractNo') is not None:
            self.contract_no = m.get('ContractNo')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('ExpiredOn') is not None:
            self.expired_on = m.get('ExpiredOn')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LicenseCount') is not None:
            self.license_count = m.get('LicenseCount')

        if m.get('LicenseItemId') is not None:
            self.license_item_id = m.get('LicenseItemId')

        if m.get('ModificationTime') is not None:
            self.modification_time = m.get('ModificationTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('ValidDays') is not None:
            self.valid_days = m.get('ValidDays')

        return self

