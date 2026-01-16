# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class DescribeRegionsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.DescribeRegionsResponseBodyResult] = None,
    ):
        # The available status of the region.
        self.request_id = request_id
        # The endpoint of the region.
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
                temp_model = main_models.DescribeRegionsResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class DescribeRegionsResponseBodyResult(DaraModel):
    def __init__(
        self,
        console_endpoint: str = None,
        local_name: str = None,
        region_endpoint: str = None,
        region_id: str = None,
        status: str = None,
    ):
        self.console_endpoint = console_endpoint
        self.local_name = local_name
        self.region_endpoint = region_endpoint
        # The name of the region.
        self.region_id = region_id
        # The endpoint of the region that is exposed in the console.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.console_endpoint is not None:
            result['consoleEndpoint'] = self.console_endpoint

        if self.local_name is not None:
            result['localName'] = self.local_name

        if self.region_endpoint is not None:
            result['regionEndpoint'] = self.region_endpoint

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consoleEndpoint') is not None:
            self.console_endpoint = m.get('consoleEndpoint')

        if m.get('localName') is not None:
            self.local_name = m.get('localName')

        if m.get('regionEndpoint') is not None:
            self.region_endpoint = m.get('regionEndpoint')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

