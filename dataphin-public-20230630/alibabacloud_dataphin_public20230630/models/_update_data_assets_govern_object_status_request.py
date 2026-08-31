# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class UpdateDataAssetsGovernObjectStatusRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        op_user_id: str = None,
        update_command: main_models.UpdateDataAssetsGovernObjectStatusRequestUpdateCommand = None,
    ):
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        self.op_user_id = op_user_id
        # This parameter is required.
        self.update_command = update_command

    def validate(self):
        if self.update_command:
            self.update_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.op_user_id is not None:
            result['OpUserId'] = self.op_user_id

        if self.update_command is not None:
            result['UpdateCommand'] = self.update_command.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

        if m.get('UpdateCommand') is not None:
            temp_model = main_models.UpdateDataAssetsGovernObjectStatusRequestUpdateCommand()
            self.update_command = temp_model.from_map(m.get('UpdateCommand'))

        return self

class UpdateDataAssetsGovernObjectStatusRequestUpdateCommand(DaraModel):
    def __init__(
        self,
        alert_owners: bool = None,
        govern_object_ids: List[int] = None,
        remark: str = None,
        target_status: str = None,
    ):
        self.alert_owners = alert_owners
        # This parameter is required.
        self.govern_object_ids = govern_object_ids
        self.remark = remark
        # This parameter is required.
        self.target_status = target_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_owners is not None:
            result['AlertOwners'] = self.alert_owners

        if self.govern_object_ids is not None:
            result['GovernObjectIds'] = self.govern_object_ids

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.target_status is not None:
            result['TargetStatus'] = self.target_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertOwners') is not None:
            self.alert_owners = m.get('AlertOwners')

        if m.get('GovernObjectIds') is not None:
            self.govern_object_ids = m.get('GovernObjectIds')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('TargetStatus') is not None:
            self.target_status = m.get('TargetStatus')

        return self

