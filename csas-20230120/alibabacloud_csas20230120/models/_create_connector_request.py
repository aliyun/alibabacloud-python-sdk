# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateConnectorRequest(DaraModel):
    def __init__(
        self,
        bandwidth: int = None,
        name: str = None,
        region: str = None,
        switch_status: str = None,
    ):
        # The bandwidth value (Mbit/s).
        self.bandwidth = bandwidth
        # The connector name. The name must be 1 to 128 characters in length and can contain letters, digits, Chinese characters, periods (.), underscores (_), and hyphens (-).
        # 
        # This parameter is required.
        self.name = name
        # The region ID.
        # 
        # This parameter is required.
        self.region = region
        # The connector instance status. Valid values:
        # - **Enabled**: Enabled.
        # - **Disabled**: Shutdown.
        # 
        # This parameter is required.
        self.switch_status = switch_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.name is not None:
            result['Name'] = self.name

        if self.region is not None:
            result['Region'] = self.region

        if self.switch_status is not None:
            result['SwitchStatus'] = self.switch_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('SwitchStatus') is not None:
            self.switch_status = m.get('SwitchStatus')

        return self

