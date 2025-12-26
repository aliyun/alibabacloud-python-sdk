# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class StopWuyingServerRequest(DaraModel):
    def __init__(
        self,
        force: bool = None,
        wuying_server_id_list: List[str] = None,
    ):
        # Force restart.
        # 
        # Valid values:
        # 
        # *   True.
        # *   False
        self.force = force
        # The list of workstation IDs.
        self.wuying_server_id_list = wuying_server_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.force is not None:
            result['Force'] = self.force

        if self.wuying_server_id_list is not None:
            result['WuyingServerIdList'] = self.wuying_server_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Force') is not None:
            self.force = m.get('Force')

        if m.get('WuyingServerIdList') is not None:
            self.wuying_server_id_list = m.get('WuyingServerIdList')

        return self

