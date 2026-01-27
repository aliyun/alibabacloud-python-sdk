# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDownloadRequest(DaraModel):
    def __init__(
        self,
        admin_database: str = None,
        bak_set_id: str = None,
        bak_set_size: str = None,
        bak_set_type: str = None,
        cluster_name: str = None,
        download_point_in_time: str = None,
        format_type: str = None,
        instance_name: str = None,
        is_cluster: str = None,
        is_physical: bool = None,
        primary_key_type_only: str = None,
        region_code: str = None,
        target_bucket: str = None,
        target_oss_region: str = None,
        target_path: str = None,
        target_type: str = None,
        use_zstd: str = None,
    ):
        self.admin_database = admin_database
        # The ID of the backup set. You can call the [DescribeBackups](https://help.aliyun.com/document_detail/26273.html) operation to query the ID of the backup set.
        # 
        # > This parameter is required if the BakSetType parameter is set to full.
        self.bak_set_id = bak_set_id
        # The size of the full backup set. Unit: bytes. You can call the [DescribeBackups](https://help.aliyun.com/document_detail/26273.html) operation to query the size of the full backup set.
        self.bak_set_size = bak_set_size
        # The type of the download task. Valid values:
        # 
        # *   **full**: downloads a full backup set.
        # *   **pitr**: downloads a backup set at a specific point in time.
        self.bak_set_type = bak_set_type
        self.cluster_name = cluster_name
        # The point in time at which the backup set is downloaded. Specify a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # > This parameter is required if the BakSetType parameter is set to pitr.
        self.download_point_in_time = download_point_in_time
        # The format to which the downloaded backup set is converted. Valid values:
        # 
        # *   **CSV**
        # *   **SQL**
        # *   **Parquet**
        # 
        # > This parameter is required.
        self.format_type = format_type
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_name = instance_name
        self.is_cluster = is_cluster
        self.is_physical = is_physical
        self.primary_key_type_only = primary_key_type_only
        # The ID of the region in which the instance resides. You can call the [DescribeDBInstanceAttribute](https://help.aliyun.com/document_detail/26231.html) operation to query the region ID of the instance.
        # 
        # This parameter is required.
        self.region_code = region_code
        # The name of the OSS bucket that is used to store the backup set.
        # 
        # *   This parameter is required if the TargetType parameter is set to OSS.
        # *   Make sure that your account is granted the **AliyunDBSDefaultRole** permission. For more information, see [Use RAM for resource authorization](https://help.aliyun.com/document_detail/26307.html). You can also grant permissions based on the operation instructions in the Resource Access Management (RAM) console.
        self.target_bucket = target_bucket
        # The region in which the OSS bucket resides.
        # 
        # > This parameter is required if the TargetType parameter is set to OSS.
        self.target_oss_region = target_oss_region
        # The destination path to which the backup set is downloaded.
        # 
        # > This parameter is required if the TargetType parameter is set to OSS.
        self.target_path = target_path
        # The type of the destination to which the backup set is downloaded. Valid values:
        # 
        # *   **OSS**
        # *   **URL**
        self.target_type = target_type
        self.use_zstd = use_zstd

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.admin_database is not None:
            result['AdminDatabase'] = self.admin_database

        if self.bak_set_id is not None:
            result['BakSetId'] = self.bak_set_id

        if self.bak_set_size is not None:
            result['BakSetSize'] = self.bak_set_size

        if self.bak_set_type is not None:
            result['BakSetType'] = self.bak_set_type

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.download_point_in_time is not None:
            result['DownloadPointInTime'] = self.download_point_in_time

        if self.format_type is not None:
            result['FormatType'] = self.format_type

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.is_cluster is not None:
            result['IsCluster'] = self.is_cluster

        if self.is_physical is not None:
            result['IsPhysical'] = self.is_physical

        if self.primary_key_type_only is not None:
            result['PrimaryKeyTypeOnly'] = self.primary_key_type_only

        if self.region_code is not None:
            result['RegionCode'] = self.region_code

        if self.target_bucket is not None:
            result['TargetBucket'] = self.target_bucket

        if self.target_oss_region is not None:
            result['TargetOssRegion'] = self.target_oss_region

        if self.target_path is not None:
            result['TargetPath'] = self.target_path

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        if self.use_zstd is not None:
            result['UseZstd'] = self.use_zstd

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdminDatabase') is not None:
            self.admin_database = m.get('AdminDatabase')

        if m.get('BakSetId') is not None:
            self.bak_set_id = m.get('BakSetId')

        if m.get('BakSetSize') is not None:
            self.bak_set_size = m.get('BakSetSize')

        if m.get('BakSetType') is not None:
            self.bak_set_type = m.get('BakSetType')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('DownloadPointInTime') is not None:
            self.download_point_in_time = m.get('DownloadPointInTime')

        if m.get('FormatType') is not None:
            self.format_type = m.get('FormatType')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('IsCluster') is not None:
            self.is_cluster = m.get('IsCluster')

        if m.get('IsPhysical') is not None:
            self.is_physical = m.get('IsPhysical')

        if m.get('PrimaryKeyTypeOnly') is not None:
            self.primary_key_type_only = m.get('PrimaryKeyTypeOnly')

        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')

        if m.get('TargetBucket') is not None:
            self.target_bucket = m.get('TargetBucket')

        if m.get('TargetOssRegion') is not None:
            self.target_oss_region = m.get('TargetOssRegion')

        if m.get('TargetPath') is not None:
            self.target_path = m.get('TargetPath')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        if m.get('UseZstd') is not None:
            self.use_zstd = m.get('UseZstd')

        return self

