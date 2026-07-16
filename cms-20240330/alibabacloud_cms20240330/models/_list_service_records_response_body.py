# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class ListServiceRecordsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        records: List[main_models.ListServiceRecordsResponseBodyRecords] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The maximum number of entries returned.
        self.max_results = max_results
        # The pagination token.
        self.next_token = next_token
        # The list of ticket operation records.
        self.records = records
        # Id of the request
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.records:
            for v1 in self.records:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        result['records'] = []
        if self.records is not None:
            for k1 in self.records:
                result['records'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        self.records = []
        if m.get('records') is not None:
            for k1 in m.get('records'):
                temp_model = main_models.ListServiceRecordsResponseBodyRecords()
                self.records.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListServiceRecordsResponseBodyRecords(DaraModel):
    def __init__(
        self,
        record_content: str = None,
        record_type: str = None,
        service_id: str = None,
        workspace: str = None,
    ):
        # The entry content in JSON string format. The format varies depending on the recordType.
        self.record_content = record_content
        # The type of the linked entry. Currently supported:
        # logCorrelation, which indicates application log association.
        self.record_type = record_type
        # The unique identifier of the service.
        self.service_id = service_id
        # The workspace.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.record_content is not None:
            result['recordContent'] = self.record_content

        if self.record_type is not None:
            result['recordType'] = self.record_type

        if self.service_id is not None:
            result['serviceId'] = self.service_id

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('recordContent') is not None:
            self.record_content = m.get('recordContent')

        if m.get('recordType') is not None:
            self.record_type = m.get('recordType')

        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

