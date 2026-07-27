# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class AddChunkRequest(DaraModel):
    def __init__(
        self,
        pipeline_id: str = None,
        data_id: str = None,
        field: Dict[str, Any] = None,
    ):
        # The knowledge base ID.
        # 
        # This parameter is required.
        self.pipeline_id = pipeline_id
        # The file ID.
        self.data_id = data_id
        # The chunk content to insert, passed as key-value pairs. For document search knowledge bases, use the following fixed key list:
        # - content (**String**): **Required**. The body content of the chunk.
        # - title (**String**): **Optional**. The title of the chunk.
        # - image_urls (**Array**): **Optional**. Image URLs included in the chunk. A maximum of 10 images are supported.
        # 
        # For data query and image Q&A knowledge bases, the keys are not fixed and are determined by the data source spreadsheet of the knowledge base. The key is the Excel column header, and the value is the corresponding column value.
        self.field = field

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id

        if self.data_id is not None:
            result['dataId'] = self.data_id

        if self.field is not None:
            result['field'] = self.field

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')

        if m.get('dataId') is not None:
            self.data_id = m.get('dataId')

        if m.get('field') is not None:
            self.field = m.get('field')

        return self

