# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class DescribeRegionsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.DescribeRegionsResponseBodyResult] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The results returned.
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
            result['requestId'] = self.request_id

        result['result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.result = []
        if m.get('result') is not None:
            for k1 in m.get('result'):
                temp_model = main_models.DescribeRegionsResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class DescribeRegionsResponseBodyResult(DaraModel):
    def __init__(
        self,
        console_url: str = None,
        endpoint: str = None,
        local_name: str = None,
        region_id: str = None,
    ):
        # The console URL.
        self.console_url = console_url
        # The endpoint.
        self.endpoint = endpoint
        # The region name.
        self.local_name = local_name
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.console_url is not None:
            result['consoleUrl'] = self.console_url

        if self.endpoint is not None:
            result['endpoint'] = self.endpoint

        if self.local_name is not None:
            result['localName'] = self.local_name

        if self.region_id is not None:
            result['regionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consoleUrl') is not None:
            self.console_url = m.get('consoleUrl')

        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')

        if m.get('localName') is not None:
            self.local_name = m.get('localName')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        return self

