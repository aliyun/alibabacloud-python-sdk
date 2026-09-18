# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateGraphInfoRequest(DaraModel):
    def __init__(
        self,
        business_profile: str = None,
        display_name: str = None,
        graph_name: str = None,
        tenant_id: str = None,
    ):
        # The business description of the knowledge graph. If not configured, the value is an empty string.
        self.business_profile = business_profile
        # The display name of the knowledge graph.
        self.display_name = display_name
        # The name of the knowledge graph.
        # 
        # This parameter is required.
        self.graph_name = graph_name
        # The tenant ID.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_profile is not None:
            result['businessProfile'] = self.business_profile

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.graph_name is not None:
            result['graphName'] = self.graph_name

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('businessProfile') is not None:
            self.business_profile = m.get('businessProfile')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('graphName') is not None:
            self.graph_name = m.get('graphName')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

