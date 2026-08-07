# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribePolarFsAttributeResponseBody(DaraModel):
    def __init__(
        self,
        accelerate_type: str = None,
        accelerated_storage_space: float = None,
        accelerating_enable: str = None,
        authorized_user_arn_ids: str = None,
        authorized_user_ids: str = None,
        bandwidth: float = None,
        bandwidth_base_line: float = None,
        bucket_id: str = None,
        category: str = None,
        client_download_path: str = None,
        create_time: str = None,
        custom_bucket_path: str = None,
        custom_bucket_path_list: List[main_models.DescribePolarFsAttributeResponseBodyCustomBucketPathList] = None,
        dbendpoint_id: str = None,
        dbtype: str = None,
        endpoint_items: List[main_models.DescribePolarFsAttributeResponseBodyEndpointItems] = None,
        expire_time: str = None,
        expired: str = None,
        file_system_id: str = None,
        lock_mode: str = None,
        maxscale_endpoint_id: str = None,
        meta_conn_string: str = None,
        meta_instance_name: str = None,
        meta_mxs_conn_string: str = None,
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
        user_default_acc_name: str = None,
        user_default_acc_sk: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # The acceleration type.
        self.accelerate_type = accelerate_type
        # The acceleration storage space, in GB.
        self.accelerated_storage_space = accelerated_storage_space
        # Indicates whether the acceleration cache is enabled. Valid values:
        # - **ON**: Enabled.
        # - **OFF**: Disabled.
        self.accelerating_enable = accelerating_enable
        # The list of authorized RAM role ARNs, separated by commas.
        self.authorized_user_arn_ids = authorized_user_arn_ids
        # The list of authorized UIDs, separated by commas.
        self.authorized_user_ids = authorized_user_ids
        # The bandwidth, in MB/s.
        self.bandwidth = bandwidth
        # The bandwidth baseline, in MB/s/TiB.
        self.bandwidth_base_line = bandwidth_base_line
        # The bucket ID.
        self.bucket_id = bucket_id
        # The Polarlakebase edition. Valid values:
        # 
        # - **high_performance**: High-performance Edition.
        # 
        # - **basic**: Basic Edition.
        # 
        # - **cold**: Cold Storage Edition.
        self.category = category
        # The client download URL.
        self.client_download_path = client_download_path
        # The creation time.
        self.create_time = create_time
        # The custom bucket path.
        self.custom_bucket_path = custom_bucket_path
        # The list of custom storage paths.
        self.custom_bucket_path_list = custom_bucket_path_list
        # The endpoint ID.
        self.dbendpoint_id = dbendpoint_id
        # The database ecosystem type. Valid values: 
        # * **MySQL**
        # * **PostgreSQL**
        self.dbtype = dbtype
        # The list of endpoints, including endpoint information for NAS, S3Gateway, and other types.
        self.endpoint_items = endpoint_items
        # The expiration time of the cluster.
        # 
        # > This parameter is returned only for clusters whose billing method is **Prepaid** (subscription). An empty value is returned for **Postpaid** (pay-as-you-go) clusters.
        self.expire_time = expire_time
        # Indicates whether the cluster has expired.
        # > This parameter is returned only for clusters whose billing method is **Prepaid** (subscription).
        self.expired = expired
        # The file system ID.
        self.file_system_id = file_system_id
        # The lock mode. Valid values: 
        # 
        # - **Unlock**: Not locked.
        # - **ManualLock**: Manually locked. 
        # - **LockByExpiration**: Automatically locked due to cluster expiration.
        self.lock_mode = lock_mode
        # The proxy endpoint ID.
        self.maxscale_endpoint_id = maxscale_endpoint_id
        # The metadata service cluster endpoint.
        self.meta_conn_string = meta_conn_string
        # The metadata instance name.
        self.meta_instance_name = meta_instance_name
        # The metadata proxy service cluster endpoint.
        self.meta_mxs_conn_string = meta_mxs_conn_string
        # The metadata address for Fuse mount (encrypted).
        self.meta_url = meta_url
        # The minor version of the instance.
        self.minor_version = minor_version
        # The mount configuration.
        self.mount_info = mount_info
        # The billing method. Valid values:
        # 
        # - **Postpaid**: pay-as-you-go.
        # - **Prepaid**: subscription.
        self.pay_type = pay_type
        # The description of the Polarlakebase instance.
        self.polar_fs_instance_description = polar_fs_instance_description
        # The Polarlakebase instance ID.
        self.polar_fs_instance_id = polar_fs_instance_id
        # The Polarlakebase instance status.
        self.polar_fs_status = polar_fs_status
        # The instance version. Valid values:
        # - **PolarFS 2.0**: 2.0
        # - **PolarFS 1.0**: 1.0
        self.polar_fs_type = polar_fs_type
        # The version.
        self.polar_fs_version = polar_fs_version
        # The region ID.
        self.region_id = region_id
        # The ID of the associated PolarDB cluster.
        self.relative_db_cluster_id = relative_db_cluster_id
        # The instance ID of the associated Polarlakebase instance.
        self.relative_pfs_cluster_id = relative_pfs_cluster_id
        # Id of the request
        self.request_id = request_id
        # The managed security group ID.
        self.security_group_id = security_group_id
        # The storage space, in GB.
        self.storage_space = storage_space
        # The storage type for the High-performance Edition. Valid values:
        # * **ESSDPL1**
        # * **ESSDPL0**
        # 
        # The storage type for the Basic Edition. Valid values:
        # * **city_redundancy**: cross-zone redundancy.
        self.storage_type = storage_type
        # The storage usage, in bytes.
        self.storage_used = storage_used
        # The default user account name for S3 Gateway.
        self.user_default_acc_name = user_default_acc_name
        # The default user account key for S3 Gateway (encrypted ciphertext).
        self.user_default_acc_sk = user_default_acc_sk
        # The VPC ID.
        self.vpcid = vpcid
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The zone ID of the vSwitch.
        self.zone_id = zone_id

    def validate(self):
        if self.custom_bucket_path_list:
            for v1 in self.custom_bucket_path_list:
                 if v1:
                    v1.validate()
        if self.endpoint_items:
            for v1 in self.endpoint_items:
                 if v1:
                    v1.validate()
        if self.mount_info:
            self.mount_info.validate()

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

        if self.authorized_user_arn_ids is not None:
            result['AuthorizedUserArnIds'] = self.authorized_user_arn_ids

        if self.authorized_user_ids is not None:
            result['AuthorizedUserIds'] = self.authorized_user_ids

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

        result['CustomBucketPathList'] = []
        if self.custom_bucket_path_list is not None:
            for k1 in self.custom_bucket_path_list:
                result['CustomBucketPathList'].append(k1.to_map() if k1 else None)

        if self.dbendpoint_id is not None:
            result['DBEndpointId'] = self.dbendpoint_id

        if self.dbtype is not None:
            result['DBType'] = self.dbtype

        result['EndpointItems'] = []
        if self.endpoint_items is not None:
            for k1 in self.endpoint_items:
                result['EndpointItems'].append(k1.to_map() if k1 else None)

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.expired is not None:
            result['Expired'] = self.expired

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode

        if self.maxscale_endpoint_id is not None:
            result['MaxscaleEndpointId'] = self.maxscale_endpoint_id

        if self.meta_conn_string is not None:
            result['MetaConnString'] = self.meta_conn_string

        if self.meta_instance_name is not None:
            result['MetaInstanceName'] = self.meta_instance_name

        if self.meta_mxs_conn_string is not None:
            result['MetaMxsConnString'] = self.meta_mxs_conn_string

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

        if self.user_default_acc_name is not None:
            result['UserDefaultAccName'] = self.user_default_acc_name

        if self.user_default_acc_sk is not None:
            result['UserDefaultAccSk'] = self.user_default_acc_sk

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

        if m.get('AuthorizedUserArnIds') is not None:
            self.authorized_user_arn_ids = m.get('AuthorizedUserArnIds')

        if m.get('AuthorizedUserIds') is not None:
            self.authorized_user_ids = m.get('AuthorizedUserIds')

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

        self.custom_bucket_path_list = []
        if m.get('CustomBucketPathList') is not None:
            for k1 in m.get('CustomBucketPathList'):
                temp_model = main_models.DescribePolarFsAttributeResponseBodyCustomBucketPathList()
                self.custom_bucket_path_list.append(temp_model.from_map(k1))

        if m.get('DBEndpointId') is not None:
            self.dbendpoint_id = m.get('DBEndpointId')

        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')

        self.endpoint_items = []
        if m.get('EndpointItems') is not None:
            for k1 in m.get('EndpointItems'):
                temp_model = main_models.DescribePolarFsAttributeResponseBodyEndpointItems()
                self.endpoint_items.append(temp_model.from_map(k1))

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('Expired') is not None:
            self.expired = m.get('Expired')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')

        if m.get('MaxscaleEndpointId') is not None:
            self.maxscale_endpoint_id = m.get('MaxscaleEndpointId')

        if m.get('MetaConnString') is not None:
            self.meta_conn_string = m.get('MetaConnString')

        if m.get('MetaInstanceName') is not None:
            self.meta_instance_name = m.get('MetaInstanceName')

        if m.get('MetaMxsConnString') is not None:
            self.meta_mxs_conn_string = m.get('MetaMxsConnString')

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

        if m.get('UserDefaultAccName') is not None:
            self.user_default_acc_name = m.get('UserDefaultAccName')

        if m.get('UserDefaultAccSk') is not None:
            self.user_default_acc_sk = m.get('UserDefaultAccSk')

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
        # The cluster management endpoint.
        self.polar_db_proxy = polar_db_proxy
        # The file system name.
        self.polar_fs_cluster = polar_fs_cluster
        # The token value.
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

class DescribePolarFsAttributeResponseBodyEndpointItems(DaraModel):
    def __init__(
        self,
        address_items: List[main_models.DescribePolarFsAttributeResponseBodyEndpointItemsAddressItems] = None,
        dbendpoint_id: str = None,
        endpoint_type: str = None,
    ):
        # The list of addresses.
        self.address_items = address_items
        # The endpoint ID.
        self.dbendpoint_id = dbendpoint_id
        # The endpoint type. Valid values: Nas, S3Gateway, and others.
        self.endpoint_type = endpoint_type

    def validate(self):
        if self.address_items:
            for v1 in self.address_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AddressItems'] = []
        if self.address_items is not None:
            for k1 in self.address_items:
                result['AddressItems'].append(k1.to_map() if k1 else None)

        if self.dbendpoint_id is not None:
            result['DBEndpointId'] = self.dbendpoint_id

        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.address_items = []
        if m.get('AddressItems') is not None:
            for k1 in m.get('AddressItems'):
                temp_model = main_models.DescribePolarFsAttributeResponseBodyEndpointItemsAddressItems()
                self.address_items.append(temp_model.from_map(k1))

        if m.get('DBEndpointId') is not None:
            self.dbendpoint_id = m.get('DBEndpointId')

        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')

        return self

class DescribePolarFsAttributeResponseBodyEndpointItemsAddressItems(DaraModel):
    def __init__(
        self,
        connection_string: str = None,
        ipaddress: str = None,
        net_type: str = None,
        port: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
    ):
        # The endpoint of the protocol connection.
        self.connection_string = connection_string
        # The IP address.
        self.ipaddress = ipaddress
        # The network type of the connection string. Valid values:
        # * **Public**: public endpoint.
        # * **Private**: private endpoint.
        # * **Inner**: private endpoint (classic network).
        self.net_type = net_type
        # The port number.
        self.port = port
        # The VPC ID.
        self.vpcid = vpcid
        # The vSwitch ID.
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.ipaddress is not None:
            result['IPAddress'] = self.ipaddress

        if self.net_type is not None:
            result['NetType'] = self.net_type

        if self.port is not None:
            result['Port'] = self.port

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('IPAddress') is not None:
            self.ipaddress = m.get('IPAddress')

        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

class DescribePolarFsAttributeResponseBodyCustomBucketPathList(DaraModel):
    def __init__(
        self,
        bucket: str = None,
        path: str = None,
    ):
        # The custom storage bucket.
        self.bucket = bucket
        # The custom storage path.
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket is not None:
            result['Bucket'] = self.bucket

        if self.path is not None:
            result['Path'] = self.path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        return self

