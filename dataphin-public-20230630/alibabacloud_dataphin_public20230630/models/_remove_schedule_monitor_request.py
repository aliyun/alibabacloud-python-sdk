# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class RemoveScheduleMonitorRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        op_user_id: str = None,
        remove_command: main_models.RemoveScheduleMonitorRequestRemoveCommand = None,
    ):
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # The ID of the operator.
        self.op_user_id = op_user_id
        # The request body for removing scheduling monitoring.
        # 
        # This parameter is required.
        self.remove_command = remove_command

    def validate(self):
        if self.remove_command:
            self.remove_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.op_user_id is not None:
            result['OpUserId'] = self.op_user_id

        if self.remove_command is not None:
            result['RemoveCommand'] = self.remove_command.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

        if m.get('RemoveCommand') is not None:
            temp_model = main_models.RemoveScheduleMonitorRequestRemoveCommand()
            self.remove_command = temp_model.from_map(m.get('RemoveCommand'))

        return self

class RemoveScheduleMonitorRequestRemoveCommand(DaraModel):
    def __init__(
        self,
        monitored_item_id: int = None,
        monitored_item_type: str = None,
    ):
        # The ID of the monitored item.
        # 
        # This parameter is required.
        self.monitored_item_id = monitored_item_id
        # The type of the monitored item. Valid values: LOGICAL_FIELD, OND_ID_NODE, SCHEDULE_PHYSICAL_NODE, MANUAL_PHYSICAL_NODE, ODM_NODE, LOGICAL_TABLE_NODE, and PROJECT.
        # 
        # This parameter is required.
        self.monitored_item_type = monitored_item_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.monitored_item_id is not None:
            result['MonitoredItemId'] = self.monitored_item_id

        if self.monitored_item_type is not None:
            result['MonitoredItemType'] = self.monitored_item_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MonitoredItemId') is not None:
            self.monitored_item_id = m.get('MonitoredItemId')

        if m.get('MonitoredItemType') is not None:
            self.monitored_item_type = m.get('MonitoredItemType')

        return self

