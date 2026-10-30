# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAgentConfigRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        config_id: str = None,
        config_name: str = None,
        current: str = None,
        page_size: str = None,
        region: str = None,
    ):
        # The ID of the component.
        # 
        # This parameter is required.
        self.agent_id = agent_id
        # The ID of the component configuration to retrieve.
        self.config_id = config_id
        # The name of the configuration.
        self.config_name = config_name
        # The current page number. This parameter is available only when pagination by page number is used.
        self.current = current
        # The number of entries to return on each page. Default value: 10.
        self.page_size = page_size
        # The region ID.
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['agentId'] = self.agent_id

        if self.config_id is not None:
            result['configId'] = self.config_id

        if self.config_name is not None:
            result['configName'] = self.config_name

        if self.current is not None:
            result['current'] = self.current

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.region is not None:
            result['region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        if m.get('configId') is not None:
            self.config_id = m.get('configId')

        if m.get('configName') is not None:
            self.config_name = m.get('configName')

        if m.get('current') is not None:
            self.current = m.get('current')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('region') is not None:
            self.region = m.get('region')

        return self

