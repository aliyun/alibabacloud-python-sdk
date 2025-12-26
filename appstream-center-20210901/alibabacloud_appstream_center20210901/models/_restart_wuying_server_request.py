# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RestartWuyingServerRequest(DaraModel):
    def __init__(
        self,
        wuying_server_id_list: List[str] = None,
    ):
        # The list of workstation IDs.
        self.wuying_server_id_list = wuying_server_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.wuying_server_id_list is not None:
            result['WuyingServerIdList'] = self.wuying_server_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WuyingServerIdList') is not None:
            self.wuying_server_id_list = m.get('WuyingServerIdList')

        return self

