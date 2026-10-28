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
        # Ensures the idempotence of the request. You can generate a parameter value from your client to ensure that the value is unique across different requests. **ClientToken** supports only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # Specifies whether to perform full data migration or initial full data synchronization. Valid values:
        # 
        # - **true**: yes.
        # - **false**: no.
        self.data_initialization = data_initialization
        # Specifies whether to perform incremental data migration or incremental data synchronization. Valid values:
        # 
        # - **false**: no.
        # - **true**: yes.
        self.data_synchronization = data_synchronization
        # The modified synchronization objects, in the format of a JSON string. For detailed definitions, see [Objects for data migration, synchronization, or change tracking](https://help.aliyun.com/document_detail/209545.html).
        # - The original DbList is overwritten by the new DbList. Make sure that the new DbList contains all the objects to be synchronized. Otherwise, synchronization objects may be lost. Modify the objects with caution.
        # - We recommend that you call the [DescribeDtsJobDetail](https://help.aliyun.com/document_detail/208925.html) operation to query the current synchronization objects in advance, and then specify the modified synchronization objects based on your business requirements. For example, if the current objects are Table A and Table B, and you want to add Table C, you must specify Table A, Table B, and Table C in this parameter.
        # - The DbList parameter supports a maximum of 1 MB of data.
        # - If the DbList contains filter conditions, the total length of the DbList (including the filter conditions) can be up to 1 MB.
        # - For distributed tasks (such as data migration or synchronization tasks whose source is PolarDB-X 1.0), the DbList is split based on physical table shards to generate multiple subtasks. The DbList of each subtask supports a maximum of 1 MB of data.
        self.db_list = db_list
        # The instance ID of the data synchronization instance.
        # 
        # This parameter is required.
        self.dts_instance_id = dts_instance_id
        # The ID of the synchronization task. You can call the [DescribeDtsJobs](https://help.aliyun.com/document_detail/209702.html) operation to query the ID.
        self.dts_job_id = dts_job_id
        # The dedicated field for T+1 business and ETL operators.
        self.etl_operator_column_reference = etl_operator_column_reference
        # The OSS URL of the synchronization file.
        self.file_oss_url_object = file_oss_url_object
        # The name of the table to be filtered.
        self.filter_table_name = filter_table_name
        # Specifies the method to modify the synchronization task. If you do not specify this parameter, the synchronization objects are modified by default. If you set this parameter to UPDATE_RESERVED, the reserved parameters are modified.
        self.modify_type_enum = modify_type_enum
        # The region where the instance resides. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region_id = region_id
        # The reserved parameters of DTS. The update method is addition rather than overwrite. The format is a MAP JSON string. You can specify this parameter to implement special requirements, such as whether to automatically start the precheck. The usage is similar to the Reserve parameter. For more information, see [Reserve parameter description](https://help.aliyun.com/document_detail/273111.html).
        self.reserved = reserved
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # Specifies whether to perform schema migration or initial schema synchronization. Valid values:
        # 
        # - **true**: yes.
        # - **false**: no.
        self.structure_initialization = structure_initialization
        # Specifies the synchronization direction. Valid values:
        # - **Forward**: forward synchronization.
        # - **Reverse**: reverse synchronization.
        # 
        # > - Default value: **Forward**.
        # - This parameter is required only when the synchronization topology of the data synchronization instance is two-way synchronization.
        self.synchronization_direction = synchronization_direction
        # Specifies whether the task is a zero-ETL task. Valid values:
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

