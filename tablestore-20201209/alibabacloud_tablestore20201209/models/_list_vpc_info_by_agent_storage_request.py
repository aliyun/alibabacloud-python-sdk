# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListVpcInfoByAgentStorageRequest(DaraModel):
    def __init__(
        self,
        agent_storage_name: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        # The agent storage name.
        # 
        # This parameter is required.
        self.agent_storage_name = agent_storage_name
        # The page number.
        self.page_num = page_num
        # The number of VPCs per page for the query.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_storage_name is not None:
            result['AgentStorageName'] = self.agent_storage_name

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentStorageName') is not None:
            self.agent_storage_name = m.get('AgentStorageName')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

