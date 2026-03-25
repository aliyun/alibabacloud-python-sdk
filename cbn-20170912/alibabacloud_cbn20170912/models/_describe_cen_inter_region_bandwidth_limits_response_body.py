# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class DescribeCenInterRegionBandwidthLimitsResponseBody(DaraModel):
    def __init__(
        self,
        cen_inter_region_bandwidth_limits: main_models.DescribeCenInterRegionBandwidthLimitsResponseBodyCenInterRegionBandwidthLimits = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.cen_inter_region_bandwidth_limits = cen_inter_region_bandwidth_limits
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.cen_inter_region_bandwidth_limits:
            self.cen_inter_region_bandwidth_limits.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cen_inter_region_bandwidth_limits is not None:
            result['CenInterRegionBandwidthLimits'] = self.cen_inter_region_bandwidth_limits.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenInterRegionBandwidthLimits') is not None:
            temp_model = main_models.DescribeCenInterRegionBandwidthLimitsResponseBodyCenInterRegionBandwidthLimits()
            self.cen_inter_region_bandwidth_limits = temp_model.from_map(m.get('CenInterRegionBandwidthLimits'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeCenInterRegionBandwidthLimitsResponseBodyCenInterRegionBandwidthLimits(DaraModel):
    def __init__(
        self,
        cen_inter_region_bandwidth_limit: List[main_models.DescribeCenInterRegionBandwidthLimitsResponseBodyCenInterRegionBandwidthLimitsCenInterRegionBandwidthLimit] = None,
    ):
        self.cen_inter_region_bandwidth_limit = cen_inter_region_bandwidth_limit

    def validate(self):
        if self.cen_inter_region_bandwidth_limit:
            for v1 in self.cen_inter_region_bandwidth_limit:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CenInterRegionBandwidthLimit'] = []
        if self.cen_inter_region_bandwidth_limit is not None:
            for k1 in self.cen_inter_region_bandwidth_limit:
                result['CenInterRegionBandwidthLimit'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cen_inter_region_bandwidth_limit = []
        if m.get('CenInterRegionBandwidthLimit') is not None:
            for k1 in m.get('CenInterRegionBandwidthLimit'):
                temp_model = main_models.DescribeCenInterRegionBandwidthLimitsResponseBodyCenInterRegionBandwidthLimitsCenInterRegionBandwidthLimit()
                self.cen_inter_region_bandwidth_limit.append(temp_model.from_map(k1))

        return self

class DescribeCenInterRegionBandwidthLimitsResponseBodyCenInterRegionBandwidthLimitsCenInterRegionBandwidthLimit(DaraModel):
    def __init__(
        self,
        bandwidth_limit: int = None,
        bandwidth_package_id: str = None,
        bandwidth_type: str = None,
        cen_id: str = None,
        geographic_span_id: str = None,
        local_region_id: str = None,
        opposite_region_id: str = None,
        status: str = None,
    ):
        self.bandwidth_limit = bandwidth_limit
        self.bandwidth_package_id = bandwidth_package_id
        self.bandwidth_type = bandwidth_type
        self.cen_id = cen_id
        self.geographic_span_id = geographic_span_id
        self.local_region_id = local_region_id
        self.opposite_region_id = opposite_region_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth_limit is not None:
            result['BandwidthLimit'] = self.bandwidth_limit

        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id

        if self.bandwidth_type is not None:
            result['BandwidthType'] = self.bandwidth_type

        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.geographic_span_id is not None:
            result['GeographicSpanId'] = self.geographic_span_id

        if self.local_region_id is not None:
            result['LocalRegionId'] = self.local_region_id

        if self.opposite_region_id is not None:
            result['OppositeRegionId'] = self.opposite_region_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthLimit') is not None:
            self.bandwidth_limit = m.get('BandwidthLimit')

        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')

        if m.get('BandwidthType') is not None:
            self.bandwidth_type = m.get('BandwidthType')

        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('GeographicSpanId') is not None:
            self.geographic_span_id = m.get('GeographicSpanId')

        if m.get('LocalRegionId') is not None:
            self.local_region_id = m.get('LocalRegionId')

        if m.get('OppositeRegionId') is not None:
            self.opposite_region_id = m.get('OppositeRegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

