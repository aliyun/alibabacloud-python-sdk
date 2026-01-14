# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateChunkRequest(DaraModel):
    def __init__(
        self,
        chunk_id: str = None,
        data_id: str = None,
        is_displayed_chunk_content: bool = None,
        pipeline_id: str = None,
        content: str = None,
        title: str = None,
    ):
        # The ID of the text chunk to be modified. You can find it in the Node.Metadata._id field returned by **ListChunks**.
        # 
        # This parameter is required.
        self.chunk_id = chunk_id
        # The file ID, which is the `FileId` returned by **AddFile**. You can also go to the [Application Data](https://modelstudio.console.alibabacloud.com/?tab=app#/data-center) page. Click the ID icon next to your file to get its ID.
        # 
        # This parameter is required.
        self.data_id = data_id
        # Specifies whether this text chunk participates in knowledge base retrieval. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: true.
        # 
        # This parameter is required.
        self.is_displayed_chunk_content = is_displayed_chunk_content
        # The knowledge base ID, which is the `Data.Id` returned by **CreateIndex**. You can also get it on the [Knowledge Base](https://modelstudio.console.alibabacloud.com/?tab=app#/knowledge-base) page.
        # 
        # This parameter is required.
        self.pipeline_id = pipeline_id
        # The new content of the chunk. The content must be between 10 and 6,000 characters in length and cannot exceed the maximum chunk length set when the knowledge base was created.
        # 
        # This parameter is required.
        self.content = content
        # The new title of the chunk. The title must be 0 to 50 characters in length and can be an empty string. If you specify an empty string, the existing title is cleared. If you do not pass this parameter, the original title remains unchanged.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chunk_id is not None:
            result['ChunkId'] = self.chunk_id

        if self.data_id is not None:
            result['DataId'] = self.data_id

        if self.is_displayed_chunk_content is not None:
            result['IsDisplayedChunkContent'] = self.is_displayed_chunk_content

        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id

        if self.content is not None:
            result['content'] = self.content

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChunkId') is not None:
            self.chunk_id = m.get('ChunkId')

        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')

        if m.get('IsDisplayedChunkContent') is not None:
            self.is_displayed_chunk_content = m.get('IsDisplayedChunkContent')

        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')

        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

