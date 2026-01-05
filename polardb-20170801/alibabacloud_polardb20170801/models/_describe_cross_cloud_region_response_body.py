# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeCrossCloudRegionResponseBody(DaraModel):
    def __init__(
        self,
        cross_cloud_region_list: List[main_models.DescribeCrossCloudRegionResponseBodyCrossCloudRegionList] = None,
        request_id: str = None,
    ):
        self.cross_cloud_region_list = cross_cloud_region_list
        self.request_id = request_id

    def validate(self):
        if self.cross_cloud_region_list:
            for v1 in self.cross_cloud_region_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CrossCloudRegionList'] = []
        if self.cross_cloud_region_list is not None:
            for k1 in self.cross_cloud_region_list:
                result['CrossCloudRegionList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cross_cloud_region_list = []
        if m.get('CrossCloudRegionList') is not None:
            for k1 in m.get('CrossCloudRegionList'):
                temp_model = main_models.DescribeCrossCloudRegionResponseBodyCrossCloudRegionList()
                self.cross_cloud_region_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeCrossCloudRegionResponseBodyCrossCloudRegionList(DaraModel):
    def __init__(
        self,
        cross_cloud_region_id: str = None,
        cross_cloud_region_name: str = None,
        cross_cloud_zone_list: List[main_models.DescribeCrossCloudRegionResponseBodyCrossCloudRegionListCrossCloudZoneList] = None,
        project_id: str = None,
    ):
        self.cross_cloud_region_id = cross_cloud_region_id
        self.cross_cloud_region_name = cross_cloud_region_name
        self.cross_cloud_zone_list = cross_cloud_zone_list
        self.project_id = project_id

    def validate(self):
        if self.cross_cloud_zone_list:
            for v1 in self.cross_cloud_zone_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cross_cloud_region_id is not None:
            result['CrossCloudRegionId'] = self.cross_cloud_region_id

        if self.cross_cloud_region_name is not None:
            result['CrossCloudRegionName'] = self.cross_cloud_region_name

        result['CrossCloudZoneList'] = []
        if self.cross_cloud_zone_list is not None:
            for k1 in self.cross_cloud_zone_list:
                result['CrossCloudZoneList'].append(k1.to_map() if k1 else None)

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CrossCloudRegionId') is not None:
            self.cross_cloud_region_id = m.get('CrossCloudRegionId')

        if m.get('CrossCloudRegionName') is not None:
            self.cross_cloud_region_name = m.get('CrossCloudRegionName')

        self.cross_cloud_zone_list = []
        if m.get('CrossCloudZoneList') is not None:
            for k1 in m.get('CrossCloudZoneList'):
                temp_model = main_models.DescribeCrossCloudRegionResponseBodyCrossCloudRegionListCrossCloudZoneList()
                self.cross_cloud_zone_list.append(temp_model.from_map(k1))

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

class DescribeCrossCloudRegionResponseBodyCrossCloudRegionListCrossCloudZoneList(DaraModel):
    def __init__(
        self,
        cross_cloud_zone_id: str = None,
        cross_cloud_zone_name: str = None,
    ):
        self.cross_cloud_zone_id = cross_cloud_zone_id
        self.cross_cloud_zone_name = cross_cloud_zone_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cross_cloud_zone_id is not None:
            result['CrossCloudZoneId'] = self.cross_cloud_zone_id

        if self.cross_cloud_zone_name is not None:
            result['CrossCloudZoneName'] = self.cross_cloud_zone_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CrossCloudZoneId') is not None:
            self.cross_cloud_zone_id = m.get('CrossCloudZoneId')

        if m.get('CrossCloudZoneName') is not None:
            self.cross_cloud_zone_name = m.get('CrossCloudZoneName')

        return self

