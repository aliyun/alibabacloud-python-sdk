# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribePolarFsRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        page_number: int = None,
        page_size: int = None,
        polar_fs_instance_description: str = None,
        polar_fs_instance_ids: str = None,
        polar_fs_type: str = None,
        region_id: str = None,
        relative_db_cluster_id: str = None,
        tag: List[main_models.DescribePolarFsRequestTag] = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.page_number = page_number
        self.page_size = page_size
        self.polar_fs_instance_description = polar_fs_instance_description
        self.polar_fs_instance_ids = polar_fs_instance_ids
        self.polar_fs_type = polar_fs_type
        # This parameter is required.
        self.region_id = region_id
        self.relative_db_cluster_id = relative_db_cluster_id
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.polar_fs_instance_description is not None:
            result['PolarFsInstanceDescription'] = self.polar_fs_instance_description

        if self.polar_fs_instance_ids is not None:
            result['PolarFsInstanceIds'] = self.polar_fs_instance_ids

        if self.polar_fs_type is not None:
            result['PolarFsType'] = self.polar_fs_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.relative_db_cluster_id is not None:
            result['RelativeDbClusterId'] = self.relative_db_cluster_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PolarFsInstanceDescription') is not None:
            self.polar_fs_instance_description = m.get('PolarFsInstanceDescription')

        if m.get('PolarFsInstanceIds') is not None:
            self.polar_fs_instance_ids = m.get('PolarFsInstanceIds')

        if m.get('PolarFsType') is not None:
            self.polar_fs_type = m.get('PolarFsType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RelativeDbClusterId') is not None:
            self.relative_db_cluster_id = m.get('RelativeDbClusterId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribePolarFsRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribePolarFsRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

