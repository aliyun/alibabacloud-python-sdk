# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, BinaryIO

from darabonba.model import DaraModel

class ModifyDtsJobAdvanceRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        data_initialization: bool = None,
        data_synchronization: bool = None,
        db_list: Dict[str, Any] = None,
        dts_instance_id: str = None,
        dts_job_id: str = None,
        etl_operator_column_reference: str = None,
        file_oss_url_object: BinaryIO = None,
        filter_table_name: str = None,
        modify_type_enum: str = None,
        region_id: str = None,
        reserved: str = None,
        resource_group_id: str = None,
        structure_initialization: bool = None,
        synchronization_direction: str = None,
        zero_etl_job: bool = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. **ClientToken** can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # Specifies whether to perform full data migration or initial full data synchronization. Valid values:
        # 
        # - **true**: yes.
        # - **false**: no.
        self.data_initialization = data_initialization
        # Specifies whether to perform incremental data migration or synchronization. Valid values:
        # 
        # - **false**: no.
        # - **true**: yes.
        self.data_synchronization = data_synchronization
        # The modified synchronization objects, in JSON format. For more information about the definition, see [Objects of DTS tasks](https://help.aliyun.com/document_detail/209545.html).
        # - The original DbList is overwritten by the new DbList. Make sure that the new DbList contains all the objects that need to be synchronized. Otherwise, synchronization objects may be lost. Modify this parameter with caution.
        # - Call [DescribeDtsJobDetail](https://help.aliyun.com/document_detail/208925.html) to query the current synchronization objects before you modify them based on your business requirements. For example, if the current objects are tables A and B, and you want to add table C, specify tables A, B, and C in this parameter.
        # - The maximum size of DbList is 1 MB.
        # - If DbList contains filter conditions, the total length of DbList (including filter conditions) cannot exceed 1 MB.
        # - For distributed tasks (such as migration or synchronization tasks whose source is PolarDB-X 1.0), DbList is split based on physical shards and multiple subtasks are generated. The maximum size of DbList for each subtask is 1 MB.
        self.db_list = db_list
        # The instance ID of the data synchronization instance.
        # 
        # This parameter is required.
        self.dts_instance_id = dts_instance_id
        # The ID of the synchronization task. You can call [DescribeDtsJobs](https://help.aliyun.com/document_detail/209702.html) to query the task ID.
        self.dts_job_id = dts_job_id
        # A field dedicated to T+1 business scenarios. This is an ETL operator and a business-specific field.
        self.etl_operator_column_reference = etl_operator_column_reference
        # The OSS URL of the synchronization file.
        self.file_oss_url_object = file_oss_url_object
        # The name of the table to be filtered.
        self.filter_table_name = filter_table_name
        # The method used to modify the synchronization task. If this parameter is not specified, the synchronization objects are modified by default. Set this parameter to UPDATE_RESERVED to modify reserved parameters.
        self.modify_type_enum = modify_type_enum
        # The region in which the instance resides. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region_id = region_id
        # The reserved parameters of DTS. The update method is append rather than overwrite. The value is in the MAP JSON format. You can specify this parameter to meet special requirements, such as whether to automatically start a precheck. The usage is similar to that of the Reserve parameter. For details, see [Reserve parameter description](https://help.aliyun.com/document_detail/273111.html).
        self.reserved = reserved
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # Specifies whether to perform schema migration or initial schema synchronization. Valid values:
        # 
        # - **true**: yes.
        # - **false**: no.
        self.structure_initialization = structure_initialization
        # The synchronization direction. Valid values:
        # - **Forward**: forward.
        # - **Reverse**: reverse.
        # 
        # > - Default value: **Forward**.
        # - This parameter is required only when the synchronization topology of the data synchronization instance is two-way synchronization.
        self.synchronization_direction = synchronization_direction
        # Specifies whether this is a seamless integration (zero-ETL) node. Valid values:
        # - **true**: yes.
        # - **false**: no.
        self.zero_etl_job = zero_etl_job

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.data_initialization is not None:
            result['DataInitialization'] = self.data_initialization

        if self.data_synchronization is not None:
            result['DataSynchronization'] = self.data_synchronization

        if self.db_list is not None:
            result['DbList'] = self.db_list

        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id

        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id

        if self.etl_operator_column_reference is not None:
            result['EtlOperatorColumnReference'] = self.etl_operator_column_reference

        if self.file_oss_url_object is not None:
            result['FileOssUrl'] = self.file_oss_url_object

        if self.filter_table_name is not None:
            result['FilterTableName'] = self.filter_table_name

        if self.modify_type_enum is not None:
            result['ModifyTypeEnum'] = self.modify_type_enum

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.reserved is not None:
            result['Reserved'] = self.reserved

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.structure_initialization is not None:
            result['StructureInitialization'] = self.structure_initialization

        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction

        if self.zero_etl_job is not None:
            result['ZeroEtlJob'] = self.zero_etl_job

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DataInitialization') is not None:
            self.data_initialization = m.get('DataInitialization')

        if m.get('DataSynchronization') is not None:
            self.data_synchronization = m.get('DataSynchronization')

        if m.get('DbList') is not None:
            self.db_list = m.get('DbList')

        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')

        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')

        if m.get('EtlOperatorColumnReference') is not None:
            self.etl_operator_column_reference = m.get('EtlOperatorColumnReference')

        if m.get('FileOssUrl') is not None:
            self.file_oss_url_object = m.get('FileOssUrl')

        if m.get('FilterTableName') is not None:
            self.filter_table_name = m.get('FilterTableName')

        if m.get('ModifyTypeEnum') is not None:
            self.modify_type_enum = m.get('ModifyTypeEnum')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Reserved') is not None:
            self.reserved = m.get('Reserved')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('StructureInitialization') is not None:
            self.structure_initialization = m.get('StructureInitialization')

        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')

        if m.get('ZeroEtlJob') is not None:
            self.zero_etl_job = m.get('ZeroEtlJob')

        return self

