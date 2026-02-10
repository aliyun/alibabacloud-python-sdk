# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyWebLockProcessStatusRequest(DaraModel):
    def __init__(
        self,
        deal_all: int = None,
        operate_info: str = None,
        process_path: List[str] = None,
        status: int = None,
        uuid: str = None,
    ):
        # Specifies whether to change the status of the process on multiple servers on which the process runs at the same time. Valid values:
        # 
        # *   **0**: no
        # *   **1**: yes
        self.deal_all = deal_all
        # The parameters required to change the status of multiple processes at a time. The value is in the JSON format.
        self.operate_info = operate_info
        # The paths to the processes.
        self.process_path = process_path
        # The status of the process. Valid values:
        # 
        # *   **0**: cancels adding the process to the process whitelist
        # *   **1**: adds the process to the process whitelist
        self.status = status
        # The UUID of the server.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deal_all is not None:
            result['DealAll'] = self.deal_all

        if self.operate_info is not None:
            result['OperateInfo'] = self.operate_info

        if self.process_path is not None:
            result['ProcessPath'] = self.process_path

        if self.status is not None:
            result['Status'] = self.status

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DealAll') is not None:
            self.deal_all = m.get('DealAll')

        if m.get('OperateInfo') is not None:
            self.operate_info = m.get('OperateInfo')

        if m.get('ProcessPath') is not None:
            self.process_path = m.get('ProcessPath')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

