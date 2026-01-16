# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class ListLogstashLogResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.ListLogstashLogResponseBodyResult] = None,
    ):
        # The details of the log.
        self.request_id = request_id
        # The timestamp of log generation. Unit: ms.
        self.result = result

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListLogstashLogResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class ListLogstashLogResponseBodyResult(DaraModel):
    def __init__(
        self,
        content: str = None,
        host: str = None,
        instance_id: str = None,
        level: str = None,
        timestamp: int = None,
    ):
        # The IP address of the node that generates the log.
        self.content = content
        self.host = host
        self.instance_id = instance_id
        # The ID of the instance.
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

        if m.get('host') is not None:
            self.host = m.get('host')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('level') is not None:
            self.level = m.get('level')

        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')

        return self

