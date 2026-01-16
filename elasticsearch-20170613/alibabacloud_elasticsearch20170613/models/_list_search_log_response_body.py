# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class ListSearchLogResponseBody(DaraModel):
    def __init__(
        self,
        headers: main_models.ListSearchLogResponseBodyHeaders = None,
        request_id: str = None,
        result: List[main_models.ListSearchLogResponseBodyResult] = None,
    ):
        # The level of the log. Valid values:
        # 
        # *   warn: warning log
        # *   info: information log
        # *   error: error log
        # *   trace: trace logs
        # *   debug: debug logs
        # 
        # The level information has been migrated to the contentCollection field.
        self.headers = headers
        # The list of logs returned by the request.
        self.request_id = request_id
        # The content of the log entry. Migrated to the contentCollection field.
        self.result = result

    def validate(self):
        if self.headers:
            self.headers.validate()
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.headers is not None:
            result['Headers'] = self.headers.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Headers') is not None:
            temp_model = main_models.ListSearchLogResponseBodyHeaders()
            self.headers = temp_model.from_map(m.get('Headers'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListSearchLogResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class ListSearchLogResponseBodyResult(DaraModel):
    def __init__(
        self,
        content: str = None,
        content_collection: Dict[str, Any] = None,
        host: str = None,
        instance_id: str = None,
        level: str = None,
        timestamp: int = None,
    ):
        # The ID of the instance.
        self.content = content
        self.content_collection = content_collection
        # Details of the log entry. Different content fields are returned for different log types.
        self.host = host
        self.instance_id = instance_id
        # The timestamp when the log is generated. Unit: ms.
        self.level = level
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.content_collection is not None:
            result['contentCollection'] = self.content_collection

        if self.host is not None:
            result['host'] = self.host

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.level is not None:
            result['level'] = self.level

        if self.timestamp is not None:
            result['timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('contentCollection') is not None:
            self.content_collection = m.get('contentCollection')

        if m.get('host') is not None:
            self.host = m.get('host')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('level') is not None:
            self.level = m.get('level')

        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')

        return self

class ListSearchLogResponseBodyHeaders(DaraModel):
    def __init__(
        self,
        x_total_count: int = None,
    ):
        # The IP address of the node that generates the log.
        self.x_total_count = x_total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.x_total_count is not None:
            result['X-Total-Count'] = self.x_total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Total-Count') is not None:
            self.x_total_count = m.get('X-Total-Count')

        return self

