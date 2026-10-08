# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class BatchHandoverAssetRequest(DaraModel):
    def __init__(
        self,
        handover_command: main_models.BatchHandoverAssetRequestHandoverCommand = None,
        op_tenant_id: int = None,
        op_user_id: str = None,
    ):
        # This parameter is required.
        self.handover_command = handover_command
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        self.op_user_id = op_user_id

    def validate(self):
        if self.handover_command:
            self.handover_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.handover_command is not None:
            result['HandoverCommand'] = self.handover_command.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.op_user_id is not None:
            result['OpUserId'] = self.op_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HandoverCommand') is not None:
            temp_model = main_models.BatchHandoverAssetRequestHandoverCommand()
            self.handover_command = temp_model.from_map(m.get('HandoverCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

        return self

class BatchHandoverAssetRequestHandoverCommand(DaraModel):
    def __init__(
        self,
        guid_list: List[str] = None,
        target_user_id: str = None,
    ):
        # This parameter is required.
        self.guid_list = guid_list
        # This parameter is required.
        self.target_user_id = target_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.guid_list is not None:
            result['GuidList'] = self.guid_list

        if self.target_user_id is not None:
            result['TargetUserId'] = self.target_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GuidList') is not None:
            self.guid_list = m.get('GuidList')

        if m.get('TargetUserId') is not None:
            self.target_user_id = m.get('TargetUserId')

        return self

