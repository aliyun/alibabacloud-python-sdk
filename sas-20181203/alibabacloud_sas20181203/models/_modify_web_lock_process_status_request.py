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
        # The identity is simultaneous processing of servers that have the same process. Valid values:
        # - **0**: Do not use simultaneous processing.
        # - **1**: Use simultaneous processing.
        self.deal_all = deal_all
        # The operation parameters for batch setting the tamper-proofing process status. The value is in JSON format.
        self.operate_info = operate_info
        # The list of process paths.
        self.process_path = process_path
        # The status of the tamper-proofing process. Valid values:
        # - **0**: Remove from the whitelist.
        # - **1**: Add to the whitelist.
        self.status = status
        # The UUID of the server for which you want to set the tamper-proofing process status.
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

