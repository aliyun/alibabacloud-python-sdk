# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateConnectorRequest(DaraModel):
    def __init__(
        self,
        accelerate_status: str = None,
        connector_id: str = None,
        name: str = None,
        switch_status: str = None,
        vip_cidr: str = None,
    ):
        # Specifies whether to enable Global Accelerator. Valid values:
        # - **Enabled**: Enabled.
        # - **Disabled**: Disabled.
        self.accelerate_status = accelerate_status
        # The Connector ID. You can obtain the value by calling [ListConnectors](~~ListConnectors~~).
        # 
        # This parameter is required.
        self.connector_id = connector_id
        # The Connector name. The name must be 1 to 128 characters in length and can contain Chinese characters, letters, digits, periods (.), underscores (_), and hyphens (-).
        self.name = name
        # The instance status of the Connector. Valid values:
        # - **Enabled**: Enabled.
        # - **Disabled**: Shutdown.
        self.switch_status = switch_status
        # The CIDR block of the virtual IP address.
        self.vip_cidr = vip_cidr

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerate_status is not None:
            result['AccelerateStatus'] = self.accelerate_status

        if self.connector_id is not None:
            result['ConnectorId'] = self.connector_id

        if self.name is not None:
            result['Name'] = self.name

        if self.switch_status is not None:
            result['SwitchStatus'] = self.switch_status

        if self.vip_cidr is not None:
            result['VipCidr'] = self.vip_cidr

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccelerateStatus') is not None:
            self.accelerate_status = m.get('AccelerateStatus')

        if m.get('ConnectorId') is not None:
            self.connector_id = m.get('ConnectorId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SwitchStatus') is not None:
            self.switch_status = m.get('SwitchStatus')

        if m.get('VipCidr') is not None:
            self.vip_cidr = m.get('VipCidr')

        return self

