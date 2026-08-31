# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class UpdateQualityWatchSwitchRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        op_user_id: str = None,
        update_command: main_models.UpdateQualityWatchSwitchRequestUpdateCommand = None,
    ):
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        self.op_user_id = op_user_id
        # The update instruction.
        # 
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
            temp_model = main_models.UpdateQualityWatchSwitchRequestUpdateCommand()
            self.update_command = temp_model.from_map(m.get('UpdateCommand'))

        return self

class UpdateQualityWatchSwitchRequestUpdateCommand(DaraModel):
    def __init__(
        self,
        open: bool = None,
        watch_id_list: List[int] = None,
    ):
        # Specifies whether to enable the monitored object.
        # 
        # This parameter is required.
        self.open = open
        # The list of monitoring IDs.
        # 
        # This parameter is required.
        self.watch_id_list = watch_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.open is not None:
            result['Open'] = self.open

        if self.watch_id_list is not None:
            result['WatchIdList'] = self.watch_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Open') is not None:
            self.open = m.get('Open')

        if m.get('WatchIdList') is not None:
            self.watch_id_list = m.get('WatchIdList')

        return self

