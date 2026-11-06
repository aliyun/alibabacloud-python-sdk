# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class CreatePolarFsRequest(DaraModel):
    def __init__(
        self,
        accelerate_storage_size: int = None,
        accelerate_switch: str = None,
        accelerate_type: str = None,
        authorized_user_ids: str = None,
        auto_renew: bool = None,
        auto_use_coupon: bool = None,
        creation_category: str = None,
        custom_bucket_count: int = None,
        custom_bucket_path: str = None,
        custom_bucket_path_list: List[main_models.CreatePolarFsRequestCustomBucketPathList] = None,
        custom_oss_ak: str = None,
        custom_oss_sk: str = None,
        dbcluster_id: str = None,
        dbtype: str = None,
        pay_type: str = None,
        period: str = None,
        promotion_code: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        storage_space: int = None,
        storage_type: str = None,
        used_time: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # The size of the acceleration space. Unit: GB. The value must be no less than 5000 and must be a multiple of 1000. This parameter is required when acceleration is enabled for the Basic Edition.
        self.accelerate_storage_size = accelerate_storage_size
        # The acceleration startup mode. Valid values:
        # 
        # - **ONLY**: enables acceleration only.
        # - **ON**: enables cold data and acceleration.
        self.accelerate_switch = accelerate_switch
        # The acceleration type. Valid values: 
        # 
        # - **juice**: file system acceleration.
        # - **alluxio**: transparent acceleration.
        self.accelerate_type = accelerate_type
        # The list of authorized accounts for the Cold Storage Edition instance, separated by commas (`,`).
        self.authorized_user_ids = authorized_user_ids
        # Specifies whether to enable auto-renewal. Valid values:
        # 
        # - **true**: enables auto-renewal.
        # - **false**: disables auto-renewal.
        # 
        # Default value: **false**.
        # 
        # > This parameter takes effect only when the **PayType** parameter is set to **Prepaid**.
        self.auto_renew = auto_renew
        # Specifies whether to automatically use coupons. Valid values:
        # - **true**: uses coupons. This is the default value.
        # - **false**: does not use coupons.
        self.auto_use_coupon = auto_use_coupon
        # The edition. Valid values: basic (Basic Edition, default), high_performance (High-performance Edition), and cold (Cold Storage Edition). For the basic edition, you must specify AccelerateSwitch and AccelerateStorageSize. For the high_performance edition, you must specify StorageType (essdpl0 or essdpl1). For the cold edition, StorageType (local_redundancy or city_redundancy) is optional.
        self.creation_category = creation_category
        # The number of buckets.
        # 
        # > This parameter is required only when acceleration (file system acceleration) is enabled.
        self.custom_bucket_count = custom_bucket_count
        # The bucket path.
        # 
        # > This parameter is required only when acceleration (file system acceleration) is enabled.
        self.custom_bucket_path = custom_bucket_path
        # The bucket and corresponding path information.
        # 
        # > This parameter is required for transparent acceleration.
        self.custom_bucket_path_list = custom_bucket_path_list
        # The custom AccessKey ID.
        self.custom_oss_ak = custom_oss_ak
        # The custom AccessKey secret.
        self.custom_oss_sk = custom_oss_sk
        # The PolarDB cluster ID. This parameter is required when you call this operation. If this parameter is not specified, the InvalidDBClusterId.Malformed error is returned.
        self.dbcluster_id = dbcluster_id
        # The database ecosystem. Valid values:
        # - **MySQL**
        # - **PostgreSQL**
        self.dbtype = dbtype
        # The billing method. Valid values: 
        # 
        # - **Postpaid**: pay-as-you-go
        # - **Prepaid**: subscription
        self.pay_type = pay_type
        # If the **PayType** parameter is set to **Prepaid**, this parameter is required. Specifies the billing cycle of the upfront cluster. Valid values: 
        # 
        # - **Year**: year.
        # - **Month**: month.
        self.period = period
        # The coupon code. If this parameter is not specified, the default coupon is used.
        self.promotion_code = promotion_code
        # The region ID.
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/98041.html) operation to query region IDs.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The storage space. Unit: GB.
        self.storage_space = storage_space
        # The storage type. For the high_performance edition, use lowercase essdpl0 or essdpl1. For the cold edition, use local_redundancy or city_redundancy. Select the value based on the edition. The value is case-sensitive.
        self.storage_type = storage_type
        # This parameter is required when the **PayType** parameter is set to **Prepaid**.
        # - If the **Period** parameter is set to **Month**, the value of **UsedTime** must be an integer in the range of `[1-9]`.
        # - If the **Period** parameter is set to **Year**, the value of **UsedTime** must be an integer in the range of `[1-3]`.
        self.used_time = used_time
        # The VPC ID.
        self.vpcid = vpcid
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.custom_bucket_path_list:
            for v1 in self.custom_bucket_path_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerate_storage_size is not None:
            result['AccelerateStorageSize'] = self.accelerate_storage_size

        if self.accelerate_switch is not None:
            result['AccelerateSwitch'] = self.accelerate_switch

        if self.accelerate_type is not None:
            result['AccelerateType'] = self.accelerate_type

        if self.authorized_user_ids is not None:
            result['AuthorizedUserIds'] = self.authorized_user_ids

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.auto_use_coupon is not None:
            result['AutoUseCoupon'] = self.auto_use_coupon

        if self.creation_category is not None:
            result['CreationCategory'] = self.creation_category

        if self.custom_bucket_count is not None:
            result['CustomBucketCount'] = self.custom_bucket_count

        if self.custom_bucket_path is not None:
            result['CustomBucketPath'] = self.custom_bucket_path

        result['CustomBucketPathList'] = []
        if self.custom_bucket_path_list is not None:
            for k1 in self.custom_bucket_path_list:
                result['CustomBucketPathList'].append(k1.to_map() if k1 else None)

        if self.custom_oss_ak is not None:
            result['CustomOssAk'] = self.custom_oss_ak

        if self.custom_oss_sk is not None:
            result['CustomOssSk'] = self.custom_oss_sk

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dbtype is not None:
            result['DBType'] = self.dbtype

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.period is not None:
            result['Period'] = self.period

        if self.promotion_code is not None:
            result['PromotionCode'] = self.promotion_code

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.storage_space is not None:
            result['StorageSpace'] = self.storage_space

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.used_time is not None:
            result['UsedTime'] = self.used_time

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccelerateStorageSize') is not None:
            self.accelerate_storage_size = m.get('AccelerateStorageSize')

        if m.get('AccelerateSwitch') is not None:
            self.accelerate_switch = m.get('AccelerateSwitch')

        if m.get('AccelerateType') is not None:
            self.accelerate_type = m.get('AccelerateType')

        if m.get('AuthorizedUserIds') is not None:
            self.authorized_user_ids = m.get('AuthorizedUserIds')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('AutoUseCoupon') is not None:
            self.auto_use_coupon = m.get('AutoUseCoupon')

        if m.get('CreationCategory') is not None:
            self.creation_category = m.get('CreationCategory')

        if m.get('CustomBucketCount') is not None:
            self.custom_bucket_count = m.get('CustomBucketCount')

        if m.get('CustomBucketPath') is not None:
            self.custom_bucket_path = m.get('CustomBucketPath')

        self.custom_bucket_path_list = []
        if m.get('CustomBucketPathList') is not None:
            for k1 in m.get('CustomBucketPathList'):
                temp_model = main_models.CreatePolarFsRequestCustomBucketPathList()
                self.custom_bucket_path_list.append(temp_model.from_map(k1))

        if m.get('CustomOssAk') is not None:
            self.custom_oss_ak = m.get('CustomOssAk')

        if m.get('CustomOssSk') is not None:
            self.custom_oss_sk = m.get('CustomOssSk')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PromotionCode') is not None:
            self.promotion_code = m.get('PromotionCode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('StorageSpace') is not None:
            self.storage_space = m.get('StorageSpace')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class CreatePolarFsRequestCustomBucketPathList(DaraModel):
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

