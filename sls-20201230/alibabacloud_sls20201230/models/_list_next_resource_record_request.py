# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListNextResourceRecordRequest(DaraModel):
    def __init__(
        self,
        ids: str = None,
        include_system_records: bool = None,
        json_filter_acc: bool = None,
        json_path: str = None,
        json_path_value: str = None,
        max_results: int = None,
        next_token: str = None,
        reverse: bool = None,
        search: str = None,
        sjson: str = None,
        tag: str = None,
    ):
        # Filters records by ID. Separate multiple IDs with commas. A maximum of 200 IDs are supported.
        self.ids = ids
        # Specifies whether to include system built-in records.
        self.include_system_records = include_system_records
        # Specifies whether to enable JSON filter acceleration.
        self.json_filter_acc = json_filter_acc
        # The JSON field path. Used together with jsonPathValue.
        self.json_path = json_path
        # The filter value for the JSON field. Used together with jsonPath.
        self.json_path_value = json_path_value
        # The maximum number of records to return in this request. Valid values: 1 to 200.
        self.max_results = max_results
        # The pagination token. Do not pass this parameter for the first request. For subsequent requests, pass the nextToken value returned in the previous response.
        self.next_token = next_token
        # Specifies whether to traverse records in reverse order.
        self.reverse = reverse
        # Searches for a specified string in record content.
        self.search = search
        # Searches by JSON content.
        self.sjson = sjson
        # Filters records by tag.
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ids is not None:
            result['ids'] = self.ids

        if self.include_system_records is not None:
            result['includeSystemRecords'] = self.include_system_records

        if self.json_filter_acc is not None:
            result['jsonFilterAcc'] = self.json_filter_acc

        if self.json_path is not None:
            result['jsonPath'] = self.json_path

        if self.json_path_value is not None:
            result['jsonPathValue'] = self.json_path_value

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.reverse is not None:
            result['reverse'] = self.reverse

        if self.search is not None:
            result['search'] = self.search

        if self.sjson is not None:
            result['sjson'] = self.sjson

        if self.tag is not None:
            result['tag'] = self.tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ids') is not None:
            self.ids = m.get('ids')

        if m.get('includeSystemRecords') is not None:
            self.include_system_records = m.get('includeSystemRecords')

        if m.get('jsonFilterAcc') is not None:
            self.json_filter_acc = m.get('jsonFilterAcc')

        if m.get('jsonPath') is not None:
            self.json_path = m.get('jsonPath')

        if m.get('jsonPathValue') is not None:
            self.json_path_value = m.get('jsonPathValue')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('reverse') is not None:
            self.reverse = m.get('reverse')

        if m.get('search') is not None:
            self.search = m.get('search')

        if m.get('sjson') is not None:
            self.sjson = m.get('sjson')

        if m.get('tag') is not None:
            self.tag = m.get('tag')

        return self

