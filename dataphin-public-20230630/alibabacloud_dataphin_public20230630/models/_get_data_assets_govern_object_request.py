# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetDataAssetsGovernObjectRequest(DaraModel):
    def __init__(
        self,
        command: main_models.GetDataAssetsGovernObjectRequestCommand = None,
        op_tenant_id: int = None,
        op_user_id: str = None,
    ):
        # The query instruction.
        # 
        # This parameter is required.
        self.command = command
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # The ID of the operation user.
        self.op_user_id = op_user_id

    def validate(self):
        if self.command:
            self.command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.command is not None:
            result['Command'] = self.command.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.op_user_id is not None:
            result['OpUserId'] = self.op_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Command') is not None:
            temp_model = main_models.GetDataAssetsGovernObjectRequestCommand()
            self.command = temp_model.from_map(m.get('Command'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

        return self

class GetDataAssetsGovernObjectRequestCommand(DaraModel):
    def __init__(
        self,
        govern_object_id: int = None,
    ):
        # The governance object ID.
        # 
        # This parameter is required.
        self.govern_object_id = govern_object_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.govern_object_id is not None:
            result['GovernObjectId'] = self.govern_object_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GovernObjectId') is not None:
            self.govern_object_id = m.get('GovernObjectId')

        return self

