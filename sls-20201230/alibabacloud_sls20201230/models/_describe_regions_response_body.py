# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class DescribeRegionsResponseBody(DaraModel):
    def __init__(
        self,
        regions: List[main_models.DescribeRegionsResponseBodyRegions] = None,
    ):
        self.regions = regions

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
        result['regions'] = []
        if self.regions is not None:
            for k1 in self.regions:
                result['regions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.regions = []
        if m.get('regions') is not None:
            for k1 in m.get('regions'):
                temp_model = main_models.DescribeRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k1))

        return self

class DescribeRegionsResponseBodyRegions(DaraModel):
    def __init__(
        self,
        data_redundancy_type: List[str] = None,
        internal_endpoint: str = None,
        internet_endpoint: str = None,
        intranet_endpoint: str = None,
        local_name: str = None,
        region: str = None,
    ):
        self.data_redundancy_type = data_redundancy_type
        self.internal_endpoint = internal_endpoint
        # The public endpoint of Simple Log Service.
        self.internet_endpoint = internet_endpoint
        # The internal endpoint of Simple Log Service.
        self.intranet_endpoint = intranet_endpoint
        # The name of the Simple Log Service region.
        self.local_name = local_name
        # SLS region
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_redundancy_type is not None:
            result['dataRedundancyType'] = self.data_redundancy_type

        if self.internal_endpoint is not None:
            result['internalEndpoint'] = self.internal_endpoint

        if self.internet_endpoint is not None:
            result['internetEndpoint'] = self.internet_endpoint

        if self.intranet_endpoint is not None:
            result['intranetEndpoint'] = self.intranet_endpoint

        if self.local_name is not None:
            result['localName'] = self.local_name

        if self.region is not None:
            result['region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataRedundancyType') is not None:
            self.data_redundancy_type = m.get('dataRedundancyType')

        if m.get('internalEndpoint') is not None:
            self.internal_endpoint = m.get('internalEndpoint')

        if m.get('internetEndpoint') is not None:
            self.internet_endpoint = m.get('internetEndpoint')

        if m.get('intranetEndpoint') is not None:
            self.intranet_endpoint = m.get('intranetEndpoint')

        if m.get('localName') is not None:
            self.local_name = m.get('localName')

        if m.get('region') is not None:
            self.region = m.get('region')

        return self

