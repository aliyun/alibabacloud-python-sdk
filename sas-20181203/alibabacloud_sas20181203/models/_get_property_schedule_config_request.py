# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetPropertyScheduleConfigRequest(DaraModel):
    def __init__(
        self,
        type: str = None,
        uuid: str = None,
    ):
        # The type of the asset fingerprints. Valid values:
        # 
        # *   **scheduler_port_period**: listening port
        # *   **scheduler_process_period**: running process
        # *   **scheduler_account_period**: account
        # *   **scheduler_software_period**: software
        # *   **scheduler_cron_period**: scheduled task
        # *   **scheduler_sca_period**: middleware
        # *   **scheduler_autorun_period**: startup item
        # *   **scheduler_lkm_period**: kernel module
        # *   **scheduler_sca_proxy_period**: website
        self.type = type
        # The UUID of the server.
        # 
        # >  You can call the [DescribeCloudCenterInstances](~~DescribeCloudCenterInstances~~) operation to query the UUIDs of servers.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['Type'] = self.type

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

