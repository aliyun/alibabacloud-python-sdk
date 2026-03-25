# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class DescribeGeographicRegionMembershipResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        region_ids: main_models.DescribeGeographicRegionMembershipResponseBodyRegionIds = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        self.region_ids = region_ids
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.region_ids:
            self.region_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionIds') is not None:
            temp_model = main_models.DescribeGeographicRegionMembershipResponseBodyRegionIds()
            self.region_ids = temp_model.from_map(m.get('RegionIds'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeGeographicRegionMembershipResponseBodyRegionIds(DaraModel):
    def __init__(
        self,
        region_id: List[main_models.DescribeGeographicRegionMembershipResponseBodyRegionIdsRegionId] = None,
    ):
        self.region_id = region_id

    def validate(self):
        if self.region_id:
            for v1 in self.region_id:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RegionId'] = []
        if self.region_id is not None:
            for k1 in self.region_id:
                result['RegionId'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region_id = []
        if m.get('RegionId') is not None:
            for k1 in m.get('RegionId'):
                temp_model = main_models.DescribeGeographicRegionMembershipResponseBodyRegionIdsRegionId()
                self.region_id.append(temp_model.from_map(k1))

        return self

class DescribeGeographicRegionMembershipResponseBodyRegionIdsRegionId(DaraModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

