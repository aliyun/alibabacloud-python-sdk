# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PageQueryAgentListNewRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        agent_name: str = None,
        inbound_configurable_only: bool = None,
        is_available: bool = None,
        page_index: int = None,
        page_no: int = None,
        page_size: int = None,
        service_direction: str = None,
        template_id: int = None,
    ):
        # Agent ID
        self.agent_id = agent_id
        # The agent name.
        self.agent_name = agent_name
        # Specifies whether to return only candidate agents that are configurable for inbound calls.
        self.inbound_configurable_only = inbound_configurable_only
        # Specifies whether the agent is available for outbound calls. A value of True indicates that the current deployment branch of the agent has a published version and is available for outbound calls.
        self.is_available = is_available
        # The page number. This parameter is deprecated. Use PageNo instead.
        self.page_index = page_index
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The service direction.
        self.service_direction = service_direction
        # The source template ID.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.agent_name is not None:
            result['AgentName'] = self.agent_name

        if self.inbound_configurable_only is not None:
            result['InboundConfigurableOnly'] = self.inbound_configurable_only

        if self.is_available is not None:
            result['IsAvailable'] = self.is_available

        if self.page_index is not None:
            result['PageIndex'] = self.page_index

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.service_direction is not None:
            result['ServiceDirection'] = self.service_direction

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        if m.get('InboundConfigurableOnly') is not None:
            self.inbound_configurable_only = m.get('InboundConfigurableOnly')

        if m.get('IsAvailable') is not None:
            self.is_available = m.get('IsAvailable')

        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ServiceDirection') is not None:
            self.service_direction = m.get('ServiceDirection')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

