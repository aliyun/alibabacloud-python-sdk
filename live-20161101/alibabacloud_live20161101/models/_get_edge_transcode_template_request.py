# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetEdgeTranscodeTemplateRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        owner_id: int = None,
        region_id: str = None,
        template_id: str = None,
    ):
        # The ID of the data center.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        self.owner_id = owner_id
        self.region_id = region_id
        # The template ID.
        # 
        # This parameter is required.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

