# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from darabonba.model import DaraModel

class ListInventoryEntriesResponseBody(DaraModel):
    def __init__(
        self,
        capture_time: str = None,
        entries: List[Dict[str, Any]] = None,
        instance_id: str = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        schema_version: str = None,
        type_name: str = None,
    ):
        # The time when the request was sent.
        self.capture_time = capture_time
        # The configurations of the component.
        self.entries = entries
        # The ID of the ECS instance.
        self.instance_id = instance_id
        # The number of entries returned per page.
        self.max_results = max_results
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The version number of the component.
        self.schema_version = schema_version
        # The name of the component.
        self.type_name = type_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capture_time is not None:
            result['CaptureTime'] = self.capture_time

        if self.entries is not None:
            result['Entries'] = self.entries

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version

        if self.type_name is not None:
            result['TypeName'] = self.type_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaptureTime') is not None:
            self.capture_time = m.get('CaptureTime')

        if m.get('Entries') is not None:
            self.entries = m.get('Entries')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')

        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')

        return self

