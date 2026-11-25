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
        # The page number.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of instances returned.
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
        # The 16-character AliUid of the Alibaba Cloud account.
        self.ali_uid = ali_uid
        # The cause of the creation failure.
        self.create_error_code = create_error_code
        # The number of milliseconds between the instance creation time and 00:00:00 on January 1, 1970.
        self.create_milliseconds = create_milliseconds
        # The creation time of the instance. The time is in the yyyy-MM-dd HH:mm:ss format.
        self.create_time = create_time
        # Indicates whether the column store engine is enabled. Valid values:
        # 
        # - **true**: Enabled.
        # - **false**: Not enabled.
        self.enable_column = enable_column
        # Indicates whether the compute engine is enabled for the instance. Valid values:
        # 
        # - **true**: Enabled.
        # - **false**: Not enabled.
        self.enable_compute = enable_compute
        # Indicates whether Lindorm Tunnel Service (LTS) is enabled. Valid values:
        # 
        # - **true**: Enabled.
        # - **false**: Not enabled.
        self.enable_lts = enable_lts
        # Indicates whether the message engine is enabled. Valid values:
        # 
        # - **true**: Enabled.
        # - **false**: Not enabled.
        self.enable_message = enable_message
        # Indicates whether LindormTable 3.0 is enabled. Valid values:
        # 
        # - **true**: Enabled.
        # - **false**: Not enabled.
        self.enable_row = enable_row
        # Indicates whether the streaming engine is enabled for the instance. Valid values:
        # 
        # - **true**: The streaming engine is enabled.
        # - **false**: The streaming engine is not enabled.
        self.enable_stream = enable_stream
        # Indicates whether the vector engine is enabled. Valid values:
        # 
        # - **true**: Enabled.
        # - **false**: Not enabled.
        self.enable_vector = enable_vector
        # The engine types supported by the instance. The return value is the sum of the following engine type values:
        # 
        # - **1**: Search engine
        # - **2**: LindormTSDB
        # - **4**: LindormTable
        # - **8**: File engine
        # 
        # > For example, if the value is 15 (15 = 8 + 4 + 2 + 1), the instance supports the search engine, LindormTSDB, LindormTable, and file engine. If the value is 6 (6 = 4 + 2), the instance supports LindormTSDB and LindormTable.
        self.engine_type = engine_type
        # The expiration time of the instance. The time is in the yyyy-MM-dd HH:mm:ss format.
        # 
        # > This parameter is returned only when the billing method of the instance is subscription.
        self.expire_time = expire_time
        # The number of milliseconds between the time when the instance expires and 00:00:00 on January 1, 1970.
        self.expired_milliseconds = expired_milliseconds
        # The instance name.
        self.instance_alias = instance_alias
        # The instance ID.
        self.instance_id = instance_id
        # The instance status. Valid values:
        # 
        # - **CREATING**: Creating.
        # - **ACTIVATION**: Running.
        # - **COLD_EXPANDING**: Performing storage expansion for storage-optimized cloud storage.
        # - **MINOR_VERSION_TRANSING**: Upgrading the minor version.
        # - **RESIZING**: Scaling out nodes.
        # - **SHRINKING**: Scaling in nodes.
        # - **CLASS_CHANGING**: Upgrading or downgrading specifications.
        # - **SSL_SWITCHING**: Modifying SSL configurations.
        # - **CDC_OPENING**: Enabling the data subscription feature.
        # - **TRANSFER**: Migrating data.
        # - **DATABASE_TRANSFER**: Migrating data to the database.
        # - **GUARD_CREATING**: Creating a disaster recovery instance.
        # - **BACKUP_RECOVERING**: Restoring from a backup.
        # - **DATABASE_IMPORTING**: Importing data.
        # - **NET_MODIFYING**: Modifying network configurations.
        # - **NET_SWITCHING**: Switching between the internal network and the Internet.
        # - **NET_CREATING**: Creating a network connection.
        # - **NET_DELETING**: Performing a delete operation on the network connection.
        # - **DELETING**: Performing a delete operation.
        # - **RESTARTING**: Restarting.
        # - **LOCKED**: Locked because the instance has expired.
        self.instance_status = instance_status
        # The storage capacity of the instance.
        self.instance_storage = instance_storage
        # The network type of the instance.
        self.network_type = network_type
        # The billing method of the instance. Valid values:
        # 
        # - **PREPAY**: Subscription
        # - **POSTPAY**: Pay-as-you-go
        self.pay_type = pay_type
        # The region ID.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The instance type. Valid values:
        # 
        # - **lindorm**: Lindorm instance
        # - **serverless_lindorm**: Lindorm Serverless instance
        # - **lindorm_standalone**: Lindorm single-node instance
        # - **lts**: Lindorm Tunnel Service
        self.service_type = service_type
        # The list of tags.
        self.tags = tags
        # The VPC ID of the instance.
        self.vpc_id = vpc_id
        # The zone ID.
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
        # The tag key.
        self.key = key
        # The tag value.
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

