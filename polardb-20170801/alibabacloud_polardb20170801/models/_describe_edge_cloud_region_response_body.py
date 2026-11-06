# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeEdgeCloudRegionResponseBody(DaraModel):
    def __init__(
        self,
        edge_cloud_regions: List[main_models.DescribeEdgeCloudRegionResponseBodyEdgeCloudRegions] = None,
        request_id: str = None,
    ):
        # The list of available edge cloud regions. When a whitelist is configured, only the regions available to the current account are returned.
        self.edge_cloud_regions = edge_cloud_regions
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.edge_cloud_regions:
            for v1 in self.edge_cloud_regions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EdgeCloudRegions'] = []
        if self.edge_cloud_regions is not None:
            for k1 in self.edge_cloud_regions:
                result['EdgeCloudRegions'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.edge_cloud_regions = []
        if m.get('EdgeCloudRegions') is not None:
            for k1 in m.get('EdgeCloudRegions'):
                temp_model = main_models.DescribeEdgeCloudRegionResponseBodyEdgeCloudRegions()
                self.edge_cloud_regions.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeEdgeCloudRegionResponseBodyEdgeCloudRegions(DaraModel):
    def __init__(
        self,
        central_control_region_id: str = None,
        edge_cloud_region_id: str = None,
        edge_cloud_region_name: str = None,
        standby_edge_cloud_region_list: List[main_models.DescribeEdgeCloudRegionResponseBodyEdgeCloudRegionsStandbyEdgeCloudRegionList] = None,
    ):
        # The ID of the central control region corresponding to the edge cloud region.
        self.central_control_region_id = central_control_region_id
        # The ID of the edge cloud region.
        self.edge_cloud_region_id = edge_cloud_region_id
        # The name of the edge cloud region.
        self.edge_cloud_region_name = edge_cloud_region_name
        # The list of standby edge cloud regions.
        self.standby_edge_cloud_region_list = standby_edge_cloud_region_list

    def validate(self):
        if self.standby_edge_cloud_region_list:
            for v1 in self.standby_edge_cloud_region_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.central_control_region_id is not None:
            result['CentralControlRegionId'] = self.central_control_region_id

        if self.edge_cloud_region_id is not None:
            result['EdgeCloudRegionId'] = self.edge_cloud_region_id

        if self.edge_cloud_region_name is not None:
            result['EdgeCloudRegionName'] = self.edge_cloud_region_name

        result['StandbyEdgeCloudRegionList'] = []
        if self.standby_edge_cloud_region_list is not None:
            for k1 in self.standby_edge_cloud_region_list:
                result['StandbyEdgeCloudRegionList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CentralControlRegionId') is not None:
            self.central_control_region_id = m.get('CentralControlRegionId')

        if m.get('EdgeCloudRegionId') is not None:
            self.edge_cloud_region_id = m.get('EdgeCloudRegionId')

        if m.get('EdgeCloudRegionName') is not None:
            self.edge_cloud_region_name = m.get('EdgeCloudRegionName')

        self.standby_edge_cloud_region_list = []
        if m.get('StandbyEdgeCloudRegionList') is not None:
            for k1 in m.get('StandbyEdgeCloudRegionList'):
                temp_model = main_models.DescribeEdgeCloudRegionResponseBodyEdgeCloudRegionsStandbyEdgeCloudRegionList()
                self.standby_edge_cloud_region_list.append(temp_model.from_map(k1))

        return self

class DescribeEdgeCloudRegionResponseBodyEdgeCloudRegionsStandbyEdgeCloudRegionList(DaraModel):
    def __init__(
        self,
        standby_edge_cloud_region_id: str = None,
        standby_edge_cloud_region_name: str = None,
    ):
        # The ID of the standby edge cloud region.
        self.standby_edge_cloud_region_id = standby_edge_cloud_region_id
        # The name of the standby edge cloud region.
        self.standby_edge_cloud_region_name = standby_edge_cloud_region_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.standby_edge_cloud_region_id is not None:
            result['StandbyEdgeCloudRegionId'] = self.standby_edge_cloud_region_id

        if self.standby_edge_cloud_region_name is not None:
            result['StandbyEdgeCloudRegionName'] = self.standby_edge_cloud_region_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StandbyEdgeCloudRegionId') is not None:
            self.standby_edge_cloud_region_id = m.get('StandbyEdgeCloudRegionId')

        if m.get('StandbyEdgeCloudRegionName') is not None:
            self.standby_edge_cloud_region_name = m.get('StandbyEdgeCloudRegionName')

        return self

