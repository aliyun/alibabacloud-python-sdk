# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class RetryKnowledgeBaseFailedSourcesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        directory_id: str = None,
        enqueued_count: int = None,
        enqueued_ids: List[str] = None,
        failed_count: int = None,
        failed_sources: List[main_models.RetryKnowledgeBaseFailedSourcesResponseBodyFailedSources] = None,
        message: str = None,
        request_id: str = None,
        skipped_count: int = None,
    ):
        # The business status code. A value of 200 indicates success. A failure returns a backend error code (ERR.* / InvalidParameter.*).
        self.code = code
        # The enterprise knowledge base directory ID.
        self.directory_id = directory_id
        # The number of resources successfully enqueued for retry.
        self.enqueued_count = enqueued_count
        # enqueuedIds。
        self.enqueued_ids = enqueued_ids
        # The total number of failed resources under the directory.
        self.failed_count = failed_count
        # The list of failed data sources.
        self.failed_sources = failed_sources
        # The error description. This value is empty on success.
        self.message = message
        # The request trace ID.
        self.request_id = request_id
        # The number of resources skipped because they are not in FAILED status.
        self.skipped_count = skipped_count

    def validate(self):
        if self.failed_sources:
            for v1 in self.failed_sources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.directory_id is not None:
            result['directoryId'] = self.directory_id

        if self.enqueued_count is not None:
            result['enqueuedCount'] = self.enqueued_count

        if self.enqueued_ids is not None:
            result['enqueuedIds'] = self.enqueued_ids

        if self.failed_count is not None:
            result['failedCount'] = self.failed_count

        result['failedSources'] = []
        if self.failed_sources is not None:
            for k1 in self.failed_sources:
                result['failedSources'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.skipped_count is not None:
            result['skippedCount'] = self.skipped_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')

        if m.get('enqueuedCount') is not None:
            self.enqueued_count = m.get('enqueuedCount')

        if m.get('enqueuedIds') is not None:
            self.enqueued_ids = m.get('enqueuedIds')

        if m.get('failedCount') is not None:
            self.failed_count = m.get('failedCount')

        self.failed_sources = []
        if m.get('failedSources') is not None:
            for k1 in m.get('failedSources'):
                temp_model = main_models.RetryKnowledgeBaseFailedSourcesResponseBodyFailedSources()
                self.failed_sources.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('skippedCount') is not None:
            self.skipped_count = m.get('skippedCount')

        return self

class RetryKnowledgeBaseFailedSourcesResponseBodyFailedSources(DaraModel):
    def __init__(
        self,
        name: str = None,
        source_id: str = None,
        source_type: str = None,
    ):
        # The file name.
        self.name = name
        # The data source ID.
        self.source_id = source_id
        # The data source type.
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.source_id is not None:
            result['sourceId'] = self.source_id

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        return self

