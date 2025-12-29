# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dds20151201 import models as main_models
from darabonba.model import DaraModel

class DescribeActiveOperationTaskRegionResponseBody(DaraModel):
    def __init__(
        self,
        region_list: List[main_models.DescribeActiveOperationTaskRegionResponseBodyRegionList] = None,
        request_id: str = None,
    ):
        # The region ID.
        self.region_list = region_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.region_list:
            for v1 in self.region_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RegionList'] = []
        if self.region_list is not None:
            for k1 in self.region_list:
                result['RegionList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region_list = []
        if m.get('RegionList') is not None:
            for k1 in m.get('RegionList'):
                temp_model = main_models.DescribeActiveOperationTaskRegionResponseBodyRegionList()
                self.region_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeActiveOperationTaskRegionResponseBodyRegionList(DaraModel):
    def __init__(
        self,
        count: int = None,
        region: str = None,
    ):
        # The total number of tasks.
        self.count = count
        # The region ID of the instance.
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.region is not None:
            result['Region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        return self

