# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteEventAnalysisJobShrinkRequest(DaraModel):
    def __init__(
        self,
        source_resource_shrink: str = None,
    ):
        # The identifier of the source resource.
        # 
        # This parameter is required.
        self.source_resource_shrink = source_resource_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source_resource_shrink is not None:
            result['SourceResource'] = self.source_resource_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceResource') is not None:
            self.source_resource_shrink = m.get('SourceResource')

        return self

