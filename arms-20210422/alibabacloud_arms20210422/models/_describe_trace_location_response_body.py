# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20210422 import models as main_models
from darabonba.model import DaraModel

class DescribeTraceLocationResponseBody(DaraModel):
    def __init__(
        self,
        region_configs: List[main_models.DescribeTraceLocationResponseBodyRegionConfigs] = None,
        request_id: str = None,
    ):
        self.region_configs = region_configs
        self.request_id = request_id

    def validate(self):
        if self.region_configs:
            for v1 in self.region_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RegionConfigs'] = []
        if self.region_configs is not None:
            for k1 in self.region_configs:
                result['RegionConfigs'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region_configs = []
        if m.get('RegionConfigs') is not None:
            for k1 in m.get('RegionConfigs'):
                temp_model = main_models.DescribeTraceLocationResponseBodyRegionConfigs()
                self.region_configs.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeTraceLocationResponseBodyRegionConfigs(DaraModel):
    def __init__(
        self,
        region_no: str = None,
        url: str = None,
    ):
        self.region_no = region_no
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

