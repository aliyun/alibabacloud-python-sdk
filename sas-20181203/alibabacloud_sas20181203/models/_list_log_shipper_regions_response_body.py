# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListLogShipperRegionsResponseBody(DaraModel):
    def __init__(
        self,
        log_shipper_region_list: List[main_models.ListLogShipperRegionsResponseBodyLogShipperRegionList] = None,
        request_id: str = None,
    ):
        # The regions supported by the log delivery feature.
        self.log_shipper_region_list = log_shipper_region_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.log_shipper_region_list:
            for v1 in self.log_shipper_region_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LogShipperRegionList'] = []
        if self.log_shipper_region_list is not None:
            for k1 in self.log_shipper_region_list:
                result['LogShipperRegionList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.log_shipper_region_list = []
        if m.get('LogShipperRegionList') is not None:
            for k1 in m.get('LogShipperRegionList'):
                temp_model = main_models.ListLogShipperRegionsResponseBodyLogShipperRegionList()
                self.log_shipper_region_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListLogShipperRegionsResponseBodyLogShipperRegionList(DaraModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        # The ID of the region.
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

