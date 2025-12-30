# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class TransferOwnershipForAllObjectRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        privilege_transfer_record: main_models.TransferOwnershipForAllObjectRequestPrivilegeTransferRecord = None,
    ):
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        self.privilege_transfer_record = privilege_transfer_record

    def validate(self):
        if self.privilege_transfer_record:
            self.privilege_transfer_record.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.privilege_transfer_record is not None:
            result['PrivilegeTransferRecord'] = self.privilege_transfer_record.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('PrivilegeTransferRecord') is not None:
            temp_model = main_models.TransferOwnershipForAllObjectRequestPrivilegeTransferRecord()
            self.privilege_transfer_record = temp_model.from_map(m.get('PrivilegeTransferRecord'))

        return self

class TransferOwnershipForAllObjectRequestPrivilegeTransferRecord(DaraModel):
    def __init__(
        self,
        new_owner: str = None,
        old_owner: str = None,
        transfer_comment: str = None,
    ):
        # This parameter is required.
        self.new_owner = new_owner
        # This parameter is required.
        self.old_owner = old_owner
        self.transfer_comment = transfer_comment

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.new_owner is not None:
            result['NewOwner'] = self.new_owner

        if self.old_owner is not None:
            result['OldOwner'] = self.old_owner

        if self.transfer_comment is not None:
            result['TransferComment'] = self.transfer_comment

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewOwner') is not None:
            self.new_owner = m.get('NewOwner')

        if m.get('OldOwner') is not None:
            self.old_owner = m.get('OldOwner')

        if m.get('TransferComment') is not None:
            self.transfer_comment = m.get('TransferComment')

        return self

