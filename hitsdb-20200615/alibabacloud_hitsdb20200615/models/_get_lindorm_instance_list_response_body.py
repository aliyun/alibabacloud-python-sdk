# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hitsdb20200615 import models as main_models
from darabonba.model import DaraModel

class GetLindormInstanceListResponseBody(DaraModel):
    def __init__(
        self,
        instance_list: List[main_models.GetLindormInstanceListResponseBodyInstanceList] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
    ):
        # The list of instances.
        self.instance_list = instance_list
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned on the page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of instances found.
        self.total = total

    def validate(self):
        if self.instance_list:
            for v1 in self.instance_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceList'] = []
        if self.instance_list is not None:
            for k1 in self.instance_list:
                result['InstanceList'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_list = []
        if m.get('InstanceList') is not None:
            for k1 in m.get('InstanceList'):
                temp_model = main_models.GetLindormInstanceListResponseBodyInstanceList()
                self.instance_list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class GetLindormInstanceListResponseBodyInstanceList(DaraModel):
    def __init__(
        self,
        ali_uid: int = None,
        create_error_code: str = None,
        create_milliseconds: int = None,
        create_time: str = None,
        enable_column: bool = None,
        enable_compute: bool = None,
        enable_lts: bool = None,
        enable_message: bool = None,
        enable_row: bool = None,
        enable_stream: bool = None,
        enable_vector: bool = None,
        engine_type: str = None,
        expire_time: str = None,
        expired_milliseconds: int = None,
        instance_alias: str = None,
        instance_id: str = None,
        instance_status: str = None,
        instance_storage: str = None,
        network_type: str = None,
        pay_type: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        service_type: str = None,
        tags: List[main_models.GetLindormInstanceListResponseBodyInstanceListTags] = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # The 16-digit ID of the Alibaba Cloud account.
        self.ali_uid = ali_uid
        # The reason why the instance failed to be created.
        self.create_error_code = create_error_code
        # The timestamp of when the instance was created. The value is the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_milliseconds = create_milliseconds
        # The time when the instance was created.
        self.create_time = create_time
        # Indicates whether the column store engine is enabled. Valid values:
        # 
        # - **true**: Enabled.
        # 
        # - **false**: Not enabled.
        self.enable_column = enable_column
        # Indicates whether the compute engine is enabled for the instance. Valid values:
        # 
        # - **true**: Enabled.
        # 
        # - **false**: Not enabled.
        self.enable_compute = enable_compute
        # Indicates whether the LTS engine is enabled. Valid values:
        # 
        # - **true**: Enabled.
        # 
        # - **false**: Not enabled.
        self.enable_lts = enable_lts
        # Indicates whether the messaging engine is enabled. Valid values:
        # 
        # - **true**: Enabled.
        # 
        # - **false**: Not enabled.
        self.enable_message = enable_message
        # Indicates whether the LindormTable 3.0 engine is enabled. Valid values:
        # 
        # true: Enabled.
        # false: Not enabled.
        self.enable_row = enable_row
        # Indicates whether the stream engine is enabled for the instance. Valid values:
        # 
        # - **true**: The stream engine is enabled.
        # 
        # - **false**: The stream engine is not enabled.
        self.enable_stream = enable_stream
        # Indicates whether the vector engine is enabled. Valid values:
        # 
        # - **true**: Enabled.
        # 
        # - **false**: Not enabled.
        self.enable_vector = enable_vector
        # The types of engines supported by the instance. The value of this parameter is the sum of the values of the supported engines.
        # 
        # - **1**: search engine.
        # 
        # - **2**: LindormTSDB.
        # 
        # - **4**: LindormTable.
        # 
        # - **8**: file engine.
        # 
        # > For example, a value of 15 (8 + 4 + 2 + 1) indicates that the instance supports the file engine, LindormTable, LindormTSDB, and the search engine. A value of 6 (4 + 2) indicates that the instance supports LindormTSDB and LindormTable.
        self.engine_type = engine_type
        # The expiration time of the instance.
        # 
        # > This parameter is returned only for subscription instances.
        self.expire_time = expire_time
        # The timestamp of when the instance expires. The value is the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.expired_milliseconds = expired_milliseconds
        # The name of the instance.
        self.instance_alias = instance_alias
        # The ID of the instance.
        self.instance_id = instance_id
        # The status of the instance. Valid values:
        # 
        # - **CREATING**: The instance is being created.
        # 
        # - **ACTIVATION**: The instance is running.
        # 
        # - **COLD_EXPANDING**: The capacity of the storage-optimized instance is being expanded.
        # 
        # - **MINOR_VERSION_TRANSING**: The minor version of the instance is being upgraded.
        # 
        # - **RESIZING**: The instance is scaling up.
        # 
        # - **SHRINKING**: The instance is scaling down.
        # 
        # - **CLASS_CHANGING**: The instance class is being changed.
        # 
        # - **SSL_SWITCHING**: The SSL certificate is being changed.
        # 
        # - **CDC_OPENING**: The data subscription feature is being enabled.
        # 
        # - **TRANSFER**: Data migration is in progress.
        # 
        # - **DATABASE_TRANSFER**: Data is being migrated to the database.
        # 
        # - **GUARD_CREATING**: A disaster recovery instance is being created.
        # 
        # - **BACKUP_RECOVERING**: A backup is being restored.
        # 
        # - **DATABASE_IMPORTING**: Data is being imported.
        # 
        # - **NET_MODIFYING**: The network settings are being modified.
        # 
        # - **NET_SWITCHING**: The network type is being switched.
        # 
        # - **NET_CREATING**: A network connection is being created.
        # 
        # - **NET_DELETING**: A network connection is being deleted.
        # 
        # - **DELETING**: The instance is being deleted.
        # 
        # - **RESTARTING**: The instance is being restarted.
        # 
        # - **LOCKED**: The instance has expired and is locked.
        self.instance_status = instance_status
        # The storage capacity of the instance.
        self.instance_storage = instance_storage
        # The network type of the instance.
        self.network_type = network_type
        # The billing method of the instance. Valid values:
        # 
        # - **PREPAY**: subscription.
        # 
        # - **POSTPAY**: pay-as-you-go.
        self.pay_type = pay_type
        # The ID of the region.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The type of the instance. Valid values:
        # 
        # - **lindorm**: a Lindorm instance.
        # 
        # - **serverless_lindorm**: a Lindorm Serverless instance.
        # 
        # - **lindorm_standalone**: a Lindorm standalone instance.
        # 
        # - **lts**: the Lindorm Tunnel Service type.
        self.service_type = service_type
        # The list of tags.
        self.tags = tags
        # The ID of the virtual private cloud (VPC) in which the instance is deployed.
        self.vpc_id = vpc_id
        # The ID of the zone.
        self.zone_id = zone_id

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.create_error_code is not None:
            result['CreateErrorCode'] = self.create_error_code

        if self.create_milliseconds is not None:
            result['CreateMilliseconds'] = self.create_milliseconds

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.enable_column is not None:
            result['EnableColumn'] = self.enable_column

        if self.enable_compute is not None:
            result['EnableCompute'] = self.enable_compute

        if self.enable_lts is not None:
            result['EnableLts'] = self.enable_lts

        if self.enable_message is not None:
            result['EnableMessage'] = self.enable_message

        if self.enable_row is not None:
            result['EnableRow'] = self.enable_row

        if self.enable_stream is not None:
            result['EnableStream'] = self.enable_stream

        if self.enable_vector is not None:
            result['EnableVector'] = self.enable_vector

        if self.engine_type is not None:
            result['EngineType'] = self.engine_type

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.expired_milliseconds is not None:
            result['ExpiredMilliseconds'] = self.expired_milliseconds

        if self.instance_alias is not None:
            result['InstanceAlias'] = self.instance_alias

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status

        if self.instance_storage is not None:
            result['InstanceStorage'] = self.instance_storage

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.service_type is not None:
            result['ServiceType'] = self.service_type

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('CreateErrorCode') is not None:
            self.create_error_code = m.get('CreateErrorCode')

        if m.get('CreateMilliseconds') is not None:
            self.create_milliseconds = m.get('CreateMilliseconds')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EnableColumn') is not None:
            self.enable_column = m.get('EnableColumn')

        if m.get('EnableCompute') is not None:
            self.enable_compute = m.get('EnableCompute')

        if m.get('EnableLts') is not None:
            self.enable_lts = m.get('EnableLts')

        if m.get('EnableMessage') is not None:
            self.enable_message = m.get('EnableMessage')

        if m.get('EnableRow') is not None:
            self.enable_row = m.get('EnableRow')

        if m.get('EnableStream') is not None:
            self.enable_stream = m.get('EnableStream')

        if m.get('EnableVector') is not None:
            self.enable_vector = m.get('EnableVector')

        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('ExpiredMilliseconds') is not None:
            self.expired_milliseconds = m.get('ExpiredMilliseconds')

        if m.get('InstanceAlias') is not None:
            self.instance_alias = m.get('InstanceAlias')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')

        if m.get('InstanceStorage') is not None:
            self.instance_storage = m.get('InstanceStorage')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetLindormInstanceListResponseBodyInstanceListTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class GetLindormInstanceListResponseBodyInstanceListTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
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

