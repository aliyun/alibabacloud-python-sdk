# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeCrossCloudRegionMappingToAliyunResponseBody(DaraModel):
    def __init__(
        self,
        cross_cloud_region_mapping_list: List[main_models.DescribeCrossCloudRegionMappingToAliyunResponseBodyCrossCloudRegionMappingList] = None,
        request_id: str = None,
    ):
        self.cross_cloud_region_mapping_list = cross_cloud_region_mapping_list
        self.request_id = request_id

    def validate(self):
        if self.cross_cloud_region_mapping_list:
            for v1 in self.cross_cloud_region_mapping_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CrossCloudRegionMappingList'] = []
        if self.cross_cloud_region_mapping_list is not None:
            for k1 in self.cross_cloud_region_mapping_list:
                result['CrossCloudRegionMappingList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cross_cloud_region_mapping_list = []
        if m.get('CrossCloudRegionMappingList') is not None:
            for k1 in m.get('CrossCloudRegionMappingList'):
                temp_model = main_models.DescribeCrossCloudRegionMappingToAliyunResponseBodyCrossCloudRegionMappingList()
                self.cross_cloud_region_mapping_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeCrossCloudRegionMappingToAliyunResponseBodyCrossCloudRegionMappingList(DaraModel):
    def __init__(
        self,
        aliyun_region_id: str = None,
        cloud_provider: str = None,
        cross_cloud_region_id: str = None,
    ):
        self.aliyun_region_id = aliyun_region_id
        self.cloud_provider = cloud_provider
        self.cross_cloud_region_id = cross_cloud_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_region_id is not None:
            result['AliyunRegionId'] = self.aliyun_region_id

        if self.cloud_provider is not None:
            result['CloudProvider'] = self.cloud_provider

        if self.cross_cloud_region_id is not None:
            result['CrossCloudRegionId'] = self.cross_cloud_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunRegionId') is not None:
            self.aliyun_region_id = m.get('AliyunRegionId')

        if m.get('CloudProvider') is not None:
            self.cloud_provider = m.get('CloudProvider')

        if m.get('CrossCloudRegionId') is not None:
            self.cross_cloud_region_id = m.get('CrossCloudRegionId')

        return self

