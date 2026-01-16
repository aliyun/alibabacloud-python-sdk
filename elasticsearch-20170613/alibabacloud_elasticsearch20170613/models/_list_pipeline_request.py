# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPipelineRequest(DaraModel):
    def __init__(
        self,
        page: int = None,
        pipeline_id: str = None,
        size: int = None,
    ):
        # The header of the response.
        self.page = page
        # The ID of the request.
        self.pipeline_id = pipeline_id
        # The total number of returned entries.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page is not None:
            result['page'] = self.page

        if self.pipeline_id is not None:
            result['pipelineId'] = self.pipeline_id

        if self.size is not None:
            result['size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pipelineId') is not None:
            self.pipeline_id = m.get('pipelineId')

        if m.get('size') is not None:
            self.size = m.get('size')

        return self

