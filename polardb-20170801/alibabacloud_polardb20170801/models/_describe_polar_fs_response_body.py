# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribePolarFsResponseBody(DaraModel):
    def __init__(
        self,
        items: main_models.DescribePolarFsResponseBodyItems = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        self.items = items
        self.page_number = page_number
        self.page_record_count = page_record_count
        self.request_id = request_id
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = main_models.DescribePolarFsResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribePolarFsResponseBodyItems(DaraModel):
    def __init__(
        self,
        polar_fs_paths: List[main_models.DescribePolarFsResponseBodyItemsPolarFsPaths] = None,
    ):
        self.polar_fs_paths = polar_fs_paths

    def validate(self):
        if self.polar_fs_paths:
            for v1 in self.polar_fs_paths:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PolarFsPaths'] = []
        if self.polar_fs_paths is not None:
            for k1 in self.polar_fs_paths:
                result['PolarFsPaths'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.polar_fs_paths = []
        if m.get('PolarFsPaths') is not None:
            for k1 in m.get('PolarFsPaths'):
                temp_model = main_models.DescribePolarFsResponseBodyItemsPolarFsPaths()
                self.polar_fs_paths.append(temp_model.from_map(k1))

        return self

class DescribePolarFsResponseBodyItemsPolarFsPaths(DaraModel):
    def __init__(
        self,
        accelerate_type: str = None,
        accelerated_storage_space: str = None,
        accelerating_enable: str = None,
        bandwidth: int = None,
        category: str = None,
        create_time: str = None,
        expire_time: str = None,
        expired: str = None,
        mount_info: main_models.DescribePolarFsResponseBodyItemsPolarFsPathsMountInfo = None,
        mounted_aidbclusters: main_models.DescribePolarFsResponseBodyItemsPolarFsPathsMountedAIDBClusters = None,
        pay_type: str = None,
        polar_fs_instance_description: str = None,
        polar_fs_instance_id: str = None,
        polar_fs_path: str = None,
        polar_fs_status: str = None,
        polar_fs_type: str = None,
        region_id: str = None,
        relative_db_cluster_id: str = None,
        security_group_id: str = None,
        storage_space: int = None,
        storage_type: str = None,
        tags: main_models.DescribePolarFsResponseBodyItemsPolarFsPathsTags = None,
        vpcid: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        self.accelerate_type = accelerate_type
        self.accelerated_storage_space = accelerated_storage_space
        self.accelerating_enable = accelerating_enable
        self.bandwidth = bandwidth
        self.category = category
        self.create_time = create_time
        self.expire_time = expire_time
        self.expired = expired
        self.mount_info = mount_info
        self.mounted_aidbclusters = mounted_aidbclusters
        self.pay_type = pay_type
        self.polar_fs_instance_description = polar_fs_instance_description
        self.polar_fs_instance_id = polar_fs_instance_id
        self.polar_fs_path = polar_fs_path
        self.polar_fs_status = polar_fs_status
        self.polar_fs_type = polar_fs_type
        self.region_id = region_id
        self.relative_db_cluster_id = relative_db_cluster_id
        self.security_group_id = security_group_id
        self.storage_space = storage_space
        self.storage_type = storage_type
        self.tags = tags
        self.vpcid = vpcid
        self.v_switch_id = v_switch_id
        self.zone_id = zone_id

    def validate(self):
        if self.mount_info:
            self.mount_info.validate()
        if self.mounted_aidbclusters:
            self.mounted_aidbclusters.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerate_type is not None:
            result['AccelerateType'] = self.accelerate_type

        if self.accelerated_storage_space is not None:
            result['AcceleratedStorageSpace'] = self.accelerated_storage_space

        if self.accelerating_enable is not None:
            result['AcceleratingEnable'] = self.accelerating_enable

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.category is not None:
            result['Category'] = self.category

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.expired is not None:
            result['Expired'] = self.expired

        if self.mount_info is not None:
            result['MountInfo'] = self.mount_info.to_map()

        if self.mounted_aidbclusters is not None:
            result['MountedAIDBClusters'] = self.mounted_aidbclusters.to_map()

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.polar_fs_instance_description is not None:
            result['PolarFsInstanceDescription'] = self.polar_fs_instance_description

        if self.polar_fs_instance_id is not None:
            result['PolarFsInstanceId'] = self.polar_fs_instance_id

        if self.polar_fs_path is not None:
            result['PolarFsPath'] = self.polar_fs_path

        if self.polar_fs_status is not None:
            result['PolarFsStatus'] = self.polar_fs_status

        if self.polar_fs_type is not None:
            result['PolarFsType'] = self.polar_fs_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.relative_db_cluster_id is not None:
            result['RelativeDbClusterId'] = self.relative_db_cluster_id

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.storage_space is not None:
            result['StorageSpace'] = self.storage_space

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccelerateType') is not None:
            self.accelerate_type = m.get('AccelerateType')

        if m.get('AcceleratedStorageSpace') is not None:
            self.accelerated_storage_space = m.get('AcceleratedStorageSpace')

        if m.get('AcceleratingEnable') is not None:
            self.accelerating_enable = m.get('AcceleratingEnable')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('Expired') is not None:
            self.expired = m.get('Expired')

        if m.get('MountInfo') is not None:
            temp_model = main_models.DescribePolarFsResponseBodyItemsPolarFsPathsMountInfo()
            self.mount_info = temp_model.from_map(m.get('MountInfo'))

        if m.get('MountedAIDBClusters') is not None:
            temp_model = main_models.DescribePolarFsResponseBodyItemsPolarFsPathsMountedAIDBClusters()
            self.mounted_aidbclusters = temp_model.from_map(m.get('MountedAIDBClusters'))

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('PolarFsInstanceDescription') is not None:
            self.polar_fs_instance_description = m.get('PolarFsInstanceDescription')

        if m.get('PolarFsInstanceId') is not None:
            self.polar_fs_instance_id = m.get('PolarFsInstanceId')

        if m.get('PolarFsPath') is not None:
            self.polar_fs_path = m.get('PolarFsPath')

        if m.get('PolarFsStatus') is not None:
            self.polar_fs_status = m.get('PolarFsStatus')

        if m.get('PolarFsType') is not None:
            self.polar_fs_type = m.get('PolarFsType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RelativeDbClusterId') is not None:
            self.relative_db_cluster_id = m.get('RelativeDbClusterId')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('StorageSpace') is not None:
            self.storage_space = m.get('StorageSpace')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribePolarFsResponseBodyItemsPolarFsPathsTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribePolarFsResponseBodyItemsPolarFsPathsTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribePolarFsResponseBodyItemsPolarFsPathsTagsTag] = None,
    ):
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
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribePolarFsResponseBodyItemsPolarFsPathsTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribePolarFsResponseBodyItemsPolarFsPathsTagsTag(DaraModel):
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

class DescribePolarFsResponseBodyItemsPolarFsPathsMountedAIDBClusters(DaraModel):
    def __init__(
        self,
        mounted_aidbclusters: List[main_models.DescribePolarFsResponseBodyItemsPolarFsPathsMountedAIDBClustersMountedAIDBClusters] = None,
    ):
        self.mounted_aidbclusters = mounted_aidbclusters

    def validate(self):
        if self.mounted_aidbclusters:
            for v1 in self.mounted_aidbclusters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MountedAIDBClusters'] = []
        if self.mounted_aidbclusters is not None:
            for k1 in self.mounted_aidbclusters:
                result['MountedAIDBClusters'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.mounted_aidbclusters = []
        if m.get('MountedAIDBClusters') is not None:
            for k1 in m.get('MountedAIDBClusters'):
                temp_model = main_models.DescribePolarFsResponseBodyItemsPolarFsPathsMountedAIDBClustersMountedAIDBClusters()
                self.mounted_aidbclusters.append(temp_model.from_map(k1))

        return self

class DescribePolarFsResponseBodyItemsPolarFsPathsMountedAIDBClustersMountedAIDBClusters(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        mount_dir: str = None,
        mount_status: str = None,
        mounted_time: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.mount_dir = mount_dir
        self.mount_status = mount_status
        self.mounted_time = mounted_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.mount_dir is not None:
            result['MountDir'] = self.mount_dir

        if self.mount_status is not None:
            result['MountStatus'] = self.mount_status

        if self.mounted_time is not None:
            result['MountedTime'] = self.mounted_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('MountDir') is not None:
            self.mount_dir = m.get('MountDir')

        if m.get('MountStatus') is not None:
            self.mount_status = m.get('MountStatus')

        if m.get('MountedTime') is not None:
            self.mounted_time = m.get('MountedTime')

        return self

class DescribePolarFsResponseBodyItemsPolarFsPathsMountInfo(DaraModel):
    def __init__(
        self,
        polar_db_proxy: str = None,
        polar_fs_cluster: str = None,
        token: str = None,
    ):
        self.polar_db_proxy = polar_db_proxy
        self.polar_fs_cluster = polar_fs_cluster
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.polar_db_proxy is not None:
            result['PolarDbProxy'] = self.polar_db_proxy

        if self.polar_fs_cluster is not None:
            result['PolarFsCluster'] = self.polar_fs_cluster

        if self.token is not None:
            result['Token'] = self.token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolarDbProxy') is not None:
            self.polar_db_proxy = m.get('PolarDbProxy')

        if m.get('PolarFsCluster') is not None:
            self.polar_fs_cluster = m.get('PolarFsCluster')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        return self

