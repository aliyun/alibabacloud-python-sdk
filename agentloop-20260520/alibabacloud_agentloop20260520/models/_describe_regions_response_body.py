# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentloop20260520 import models as main_models
from darabonba.model import DaraModel

class DescribeRegionsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        regions: List[main_models.DescribeRegionsResponseBodyRegions] = None,
        request_id: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.regions = regions
        self.request_id = request_id

    def validate(self):
        if self.regions:
            for v1 in self.regions:
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

        result['regions'] = []
        if self.regions is not None:
            for k1 in self.regions:
                result['regions'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        self.regions = []
        if m.get('regions') is not None:
            for k1 in m.get('regions'):
                temp_model = main_models.DescribeRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class DescribeRegionsResponseBodyRegions(DaraModel):
    def __init__(
        self,
        internet_endpoint: str = None,
        local_name: str = None,
        region_id: str = None,
        vpc_endpoint: str = None,
    ):
        self.internet_endpoint = internet_endpoint
        self.local_name = local_name
        self.region_id = region_id
        self.vpc_endpoint = vpc_endpoint

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.internet_endpoint is not None:
            result['internetEndpoint'] = self.internet_endpoint

        if self.local_name is not None:
            result['localName'] = self.local_name

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.vpc_endpoint is not None:
            result['vpcEndpoint'] = self.vpc_endpoint

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('internetEndpoint') is not None:
            self.internet_endpoint = m.get('internetEndpoint')

        if m.get('localName') is not None:
            self.local_name = m.get('localName')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('vpcEndpoint') is not None:
            self.vpc_endpoint = m.get('vpcEndpoint')

        return self

