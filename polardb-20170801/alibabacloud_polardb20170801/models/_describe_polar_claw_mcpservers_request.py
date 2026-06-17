# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribePolarClawMCPServersRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        server_list: List[str] = None,
    ):
        # The application ID.
        # 
        # This parameter is required.
        self.application_id = application_id
        # A list of MCP server names. If this parameter is empty, the configurations of all MCP servers are returned.
        self.server_list = server_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.server_list is not None:
            result['ServerList'] = self.server_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ServerList') is not None:
            self.server_list = m.get('ServerList')

        return self

