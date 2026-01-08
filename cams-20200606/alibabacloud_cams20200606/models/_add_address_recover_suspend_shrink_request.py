# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddAddressRecoverSuspendShrinkRequest(DaraModel):
    def __init__(
        self,
        audit_record_shrink: str = None,
        cust_space_id: str = None,
        owner_id: int = None,
        request_type: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.audit_record_shrink = audit_record_shrink
        self.cust_space_id = cust_space_id
        self.owner_id = owner_id
        self.request_type = request_type
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_record_shrink is not None:
            result['AuditRecord'] = self.audit_record_shrink

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
            self.audit_record_shrink = m.get('AuditRecord')

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

