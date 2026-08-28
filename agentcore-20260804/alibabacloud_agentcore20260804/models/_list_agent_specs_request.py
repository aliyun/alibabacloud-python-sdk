# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAgentSpecsRequest(DaraModel):
    def __init__(
        self,
        agent_spec_name: str = None,
        biz_tag: str = None,
        order_by: str = None,
        owner: str = None,
        page_no: int = None,
        page_size: int = None,
        scope: str = None,
        search: str = None,
        with_capabilities: bool = None,
    ):
        # The AgentSpec name used as a search keyword. Use this parameter together with the search parameter.
        self.agent_spec_name = agent_spec_name
        # The business tag used for fuzzy filtering.
        self.biz_tag = biz_tag
        # The field by which to sort results. Set this parameter to download_count to sort by download count. By default, results are sorted by update time.
        self.order_by = order_by
        # The owner used to filter results.
        self.owner = owner
        # The page number. Pages start from 1. Default value: 1.
        self.page_no = page_no
        # The number of entries per page. Default value: 10. Maximum value: 50.
        self.page_size = page_size
        # The visibility scope used to filter results. Valid values:
        # 
        # - PUBLIC
        # - PRIVATE
        self.scope = scope
        # The search mode. Valid values:
        # 
        # - accurate: exact match.
        # - blur: fuzzy match.
        # 
        # Default value: blur.
        self.search = search
        # Specifies whether to return the Skills and McpServers lists. Default value: false.
        self.with_capabilities = with_capabilities

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_spec_name is not None:
            result['agentSpecName'] = self.agent_spec_name

        if self.biz_tag is not None:
            result['bizTag'] = self.biz_tag

        if self.order_by is not None:
            result['orderBy'] = self.order_by

        if self.owner is not None:
            result['owner'] = self.owner

        if self.page_no is not None:
            result['pageNo'] = self.page_no

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.scope is not None:
            result['scope'] = self.scope

        if self.search is not None:
            result['search'] = self.search

        if self.with_capabilities is not None:
            result['withCapabilities'] = self.with_capabilities

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentSpecName') is not None:
            self.agent_spec_name = m.get('agentSpecName')

        if m.get('bizTag') is not None:
            self.biz_tag = m.get('bizTag')

        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')

        if m.get('owner') is not None:
            self.owner = m.get('owner')

        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('scope') is not None:
            self.scope = m.get('scope')

        if m.get('search') is not None:
            self.search = m.get('search')

        if m.get('withCapabilities') is not None:
            self.with_capabilities = m.get('withCapabilities')

        return self

