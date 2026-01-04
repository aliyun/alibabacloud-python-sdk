# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeCloudDiskTypesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        support_resources: main_models.DescribeCloudDiskTypesResponseBodySupportResources = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The specifications of resources that you can purchase.
        self.support_resources = support_resources

    def validate(self):
        if self.support_resources:
            self.support_resources.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.support_resources is not None:
            result['SupportResources'] = self.support_resources.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SupportResources') is not None:
            temp_model = main_models.DescribeCloudDiskTypesResponseBodySupportResources()
            self.support_resources = temp_model.from_map(m.get('SupportResources'))

        return self

class DescribeCloudDiskTypesResponseBodySupportResources(DaraModel):
    def __init__(
        self,
        support_resource: List[main_models.DescribeCloudDiskTypesResponseBodySupportResourcesSupportResource] = None,
    ):
        self.support_resource = support_resource

    def validate(self):
        if self.support_resource:
            for v1 in self.support_resource:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SupportResource'] = []
        if self.support_resource is not None:
            for k1 in self.support_resource:
                result['SupportResource'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.support_resource = []
        if m.get('SupportResource') is not None:
            for k1 in m.get('SupportResource'):
                temp_model = main_models.DescribeCloudDiskTypesResponseBodySupportResourcesSupportResource()
                self.support_resource.append(temp_model.from_map(k1))

        return self

class DescribeCloudDiskTypesResponseBodySupportResourcesSupportResource(DaraModel):
    def __init__(
        self,
        category: str = None,
        ens_region_id: str = None,
    ):
        # The category of the disk.
        # 
        # *   cloud_efficiency: ultra disk.
        # *   cloud_ssd: all-flash disk.
        # *   local_hdd: local HDD.
        # *   local_ssd: local SSD.
        self.category = category
        # The ID of the edge node.
        self.ens_region_id = ens_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        return self

