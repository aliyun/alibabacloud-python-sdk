# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribePolarFsAttributeResponseBody(DaraModel):
    def __init__(
        self,
        accelerated_storage_space: float = None,
        accelerating_enable: str = None,
        bandwidth: float = None,
        bandwidth_base_line: float = None,
        bucket_id: str = None,
        category: str = None,
        client_download_path: str = None,
        create_time: str = None,
        custom_bucket_path: str = None,
        dbtype: str = None,
        expire_time: str = None,
        expired: str = None,
        file_system_id: str = None,
        lock_mode: str = None,
        meta_url: str = None,
        minor_version: str = None,
        mount_info: main_models.DescribePolarFsAttributeResponseBodyMountInfo = None,
        pay_type: str = None,
        polar_fs_instance_description: str = None,
        polar_fs_instance_id: str = None,
        polar_fs_status: str = None,
        polar_fs_type: str = None,
        polar_fs_version: str = None,
        region_id: str = None,
        relative_db_cluster_id: str = None,
        relative_pfs_cluster_id: str = None,
        request_id: str = None,
        security_group_id: str = None,
        storage_space: float = None,
        storage_type: str = None,
        storage_used: float = None,
        vpcid: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        self.accelerated_storage_space = accelerated_storage_space
        self.accelerating_enable = accelerating_enable
        self.bandwidth = bandwidth
        self.bandwidth_base_line = bandwidth_base_line
        self.bucket_id = bucket_id
        self.category = category
        self.client_download_path = client_download_path
        self.create_time = create_time
        self.custom_bucket_path = custom_bucket_path
        self.dbtype = dbtype
        self.expire_time = expire_time
        self.expired = expired
        self.file_system_id = file_system_id
        self.lock_mode = lock_mode
        self.meta_url = meta_url
        self.minor_version = minor_version
        self.mount_info = mount_info
        self.pay_type = pay_type
        self.polar_fs_instance_description = polar_fs_instance_description
        self.polar_fs_instance_id = polar_fs_instance_id
        self.polar_fs_status = polar_fs_status
        self.polar_fs_type = polar_fs_type
        self.polar_fs_version = polar_fs_version
        self.region_id = region_id
        self.relative_db_cluster_id = relative_db_cluster_id
        self.relative_pfs_cluster_id = relative_pfs_cluster_id
        # Id of the request
        self.request_id = request_id
        self.security_group_id = security_group_id
        self.storage_space = storage_space
        self.storage_type = storage_type
        self.storage_used = storage_used
        self.vpcid = vpcid
        self.v_switch_id = v_switch_id
        self.zone_id = zone_id

    def validate(self):
        if self.mount_info:
            self.mount_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerated_storage_space is not None:
            result['AcceleratedStorageSpace'] = self.accelerated_storage_space

        if self.accelerating_enable is not None:
            result['AcceleratingEnable'] = self.accelerating_enable

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.bandwidth_base_line is not None:
            result['BandwidthBaseLine'] = self.bandwidth_base_line

        if self.bucket_id is not None:
            result['BucketId'] = self.bucket_id

        if self.category is not None:
            result['Category'] = self.category

        if self.client_download_path is not None:
            result['ClientDownloadPath'] = self.client_download_path

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.custom_bucket_path is not None:
            result['CustomBucketPath'] = self.custom_bucket_path

        if self.dbtype is not None:
            result['DBType'] = self.dbtype

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.expired is not None:
            result['Expired'] = self.expired

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode

        if self.meta_url is not None:
            result['MetaUrl'] = self.meta_url

        if self.minor_version is not None:
            result['MinorVersion'] = self.minor_version

        if self.mount_info is not None:
            result['MountInfo'] = self.mount_info.to_map()

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.polar_fs_instance_description is not None:
            result['PolarFsInstanceDescription'] = self.polar_fs_instance_description

        if self.polar_fs_instance_id is not None:
            result['PolarFsInstanceId'] = self.polar_fs_instance_id

        if self.polar_fs_status is not None:
            result['PolarFsStatus'] = self.polar_fs_status

        if self.polar_fs_type is not None:
            result['PolarFsType'] = self.polar_fs_type

        if self.polar_fs_version is not None:
            result['PolarFsVersion'] = self.polar_fs_version

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.relative_db_cluster_id is not None:
            result['RelativeDbClusterId'] = self.relative_db_cluster_id

        if self.relative_pfs_cluster_id is not None:
            result['RelativePfsClusterId'] = self.relative_pfs_cluster_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.storage_space is not None:
            result['StorageSpace'] = self.storage_space

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.storage_used is not None:
            result['StorageUsed'] = self.storage_used

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratedStorageSpace') is not None:
            self.accelerated_storage_space = m.get('AcceleratedStorageSpace')

        if m.get('AcceleratingEnable') is not None:
            self.accelerating_enable = m.get('AcceleratingEnable')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('BandwidthBaseLine') is not None:
            self.bandwidth_base_line = m.get('BandwidthBaseLine')

        if m.get('BucketId') is not None:
            self.bucket_id = m.get('BucketId')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('ClientDownloadPath') is not None:
            self.client_download_path = m.get('ClientDownloadPath')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CustomBucketPath') is not None:
            self.custom_bucket_path = m.get('CustomBucketPath')

        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('Expired') is not None:
            self.expired = m.get('Expired')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')

        if m.get('MetaUrl') is not None:
            self.meta_url = m.get('MetaUrl')

        if m.get('MinorVersion') is not None:
            self.minor_version = m.get('MinorVersion')

        if m.get('MountInfo') is not None:
            temp_model = main_models.DescribePolarFsAttributeResponseBodyMountInfo()
            self.mount_info = temp_model.from_map(m.get('MountInfo'))

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('PolarFsInstanceDescription') is not None:
            self.polar_fs_instance_description = m.get('PolarFsInstanceDescription')

        if m.get('PolarFsInstanceId') is not None:
            self.polar_fs_instance_id = m.get('PolarFsInstanceId')

        if m.get('PolarFsStatus') is not None:
            self.polar_fs_status = m.get('PolarFsStatus')

        if m.get('PolarFsType') is not None:
            self.polar_fs_type = m.get('PolarFsType')

        if m.get('PolarFsVersion') is not None:
            self.polar_fs_version = m.get('PolarFsVersion')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RelativeDbClusterId') is not None:
            self.relative_db_cluster_id = m.get('RelativeDbClusterId')

        if m.get('RelativePfsClusterId') is not None:
            self.relative_pfs_cluster_id = m.get('RelativePfsClusterId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('StorageSpace') is not None:
            self.storage_space = m.get('StorageSpace')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('StorageUsed') is not None:
            self.storage_used = m.get('StorageUsed')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribePolarFsAttributeResponseBodyMountInfo(DaraModel):
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

