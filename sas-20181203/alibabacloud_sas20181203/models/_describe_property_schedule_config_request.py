# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePropertyScheduleConfigRequest(DaraModel):
    def __init__(
        self,
        type: str = None,
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
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

