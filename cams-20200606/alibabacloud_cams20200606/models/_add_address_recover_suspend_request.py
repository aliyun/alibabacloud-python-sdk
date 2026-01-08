# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cams20200606 import models as main_models
from darabonba.model import DaraModel

class AddAddressRecoverSuspendRequest(DaraModel):
    def __init__(
        self,
        audit_record: main_models.AddAddressRecoverSuspendRequestAuditRecord = None,
        cust_space_id: str = None,
        owner_id: int = None,
        request_type: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.audit_record = audit_record
        self.cust_space_id = cust_space_id
        self.owner_id = owner_id
        self.request_type = request_type
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        if self.audit_record:
            self.audit_record.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_record is not None:
            result['AuditRecord'] = self.audit_record.to_map()

        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.request_type is not None:
            result['RequestType'] = self.request_type

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditRecord') is not None:
            temp_model = main_models.AddAddressRecoverSuspendRequestAuditRecord()
            self.audit_record = temp_model.from_map(m.get('AuditRecord'))

        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RequestType') is not None:
            self.request_type = m.get('RequestType')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self



class AddAddressRecoverSuspendRequestAuditRecord(DaraModel):
    def __init__(
        self,
        apply_reason: str = None,
        message_destination_country: List[str] = None,
        message_destination_international_country: List[str] = None,
        recovery_date: str = None,
        suspension_date: str = None,
    ):
        self.apply_reason = apply_reason
        self.message_destination_country = message_destination_country
        self.message_destination_international_country = message_destination_international_country
        self.recovery_date = recovery_date
        self.suspension_date = suspension_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_reason is not None:
            result['ApplyReason'] = self.apply_reason

        if self.message_destination_country is not None:
            result['MessageDestinationCountry'] = self.message_destination_country

        if self.message_destination_international_country is not None:
            result['MessageDestinationInternationalCountry'] = self.message_destination_international_country

        if self.recovery_date is not None:
            result['RecoveryDate'] = self.recovery_date

        if self.suspension_date is not None:
            result['SuspensionDate'] = self.suspension_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyReason') is not None:
            self.apply_reason = m.get('ApplyReason')

        if m.get('MessageDestinationCountry') is not None:
            self.message_destination_country = m.get('MessageDestinationCountry')

        if m.get('MessageDestinationInternationalCountry') is not None:
            self.message_destination_international_country = m.get('MessageDestinationInternationalCountry')

        if m.get('RecoveryDate') is not None:
            self.recovery_date = m.get('RecoveryDate')

        if m.get('SuspensionDate') is not None:
            self.suspension_date = m.get('SuspensionDate')

        return self

