# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class DescribeKnowledgeBaseStatsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeKnowledgeBaseStatsResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The object that contains the knowledge base statistics.
        self.data = data
        # The error code returned if the request fails.
        self.error_code = error_code
        # The error message returned if the request fails.
        self.error_message = error_message
        # The unique ID of the request. Use this ID to troubleshoot errors.
        self.request_id = request_id
        # Indicates whether the request succeeded. A value of `true` indicates success, and a value of `false` indicates failure.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeKnowledgeBaseStatsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeKnowledgeBaseStatsResponseBodyData(DaraModel):
    def __init__(
        self,
        document_count: int = None,
        kb_hits: int = None,
        kb_uuid: str = None,
        total_chunk_count: int = None,
        total_file_size: int = None,
    ):
        # The number of documents in the knowledge base.
        self.document_count = document_count
        # The number of hits for the knowledge base.
        self.kb_hits = kb_hits
        # The ID of the knowledge base.
        self.kb_uuid = kb_uuid
        # The total number of knowledge chunks in the knowledge base.
        self.total_chunk_count = total_chunk_count
        # The total size of all files in the knowledge base, in bytes.
        self.total_file_size = total_file_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.document_count is not None:
            result['DocumentCount'] = self.document_count

        if self.kb_hits is not None:
            result['KbHits'] = self.kb_hits

        if self.kb_uuid is not None:
            result['KbUuid'] = self.kb_uuid

        if self.total_chunk_count is not None:
            result['TotalChunkCount'] = self.total_chunk_count

        if self.total_file_size is not None:
            result['TotalFileSize'] = self.total_file_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocumentCount') is not None:
            self.document_count = m.get('DocumentCount')

        if m.get('KbHits') is not None:
            self.kb_hits = m.get('KbHits')

        if m.get('KbUuid') is not None:
            self.kb_uuid = m.get('KbUuid')

        if m.get('TotalChunkCount') is not None:
            self.total_chunk_count = m.get('TotalChunkCount')

        if m.get('TotalFileSize') is not None:
            self.total_file_size = m.get('TotalFileSize')

        return self

