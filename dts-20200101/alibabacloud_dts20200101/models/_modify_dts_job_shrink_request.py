# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDtsJobShrinkRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        data_initialization: bool = None,
        data_synchronization: bool = None,
        db_list_shrink: str = None,
        dts_instance_id: str = None,
        dts_job_id: str = None,
        etl_operator_column_reference: str = None,
        file_oss_url: str = None,
        filter_table_name: str = None,
        modify_type_enum: str = None,
        region_id: str = None,
        reserved: str = None,
        resource_group_id: str = None,
        structure_initialization: bool = None,
        synchronization_direction: str = None,
        zero_etl_job: bool = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The **ClientToken** parameter can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # Specifies whether to perform full data migration or synchronization. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.data_initialization = data_initialization
        # Specifies whether to perform incremental data migration or synchronization. Valid values:
        # 
        # *   **false**
        # *   **true**
        self.data_synchronization = data_synchronization
        # The objects of the data synchronization task after modification. The value must be a JSON string. For more information, see [Objects of DTS tasks](https://help.aliyun.com/document_detail/209545.html).
        # 
        # > 
        # 
        # *   The new value of DbList overwrites the original value. Make sure that all the objects that you want to synchronize are specified. Otherwise, some objects may be lost. Specify this parameter with caution.
        # 
        # *   Before you call the ModifyDtsJob operation, we recommend that you call the [DescribeDtsJobDetail](https://help.aliyun.com/document_detail/208925.html) operation to query the current objects of the data synchronization task. Then, you can specify the new objects based on your business requirements. For example, if the current objects are Table A and Table B and you need to add Table C, you must specify Table A, Table B, and Table C for this parameter.
        self.db_list_shrink = db_list_shrink
        # The ID of the data synchronization instance.
        # 
        # This parameter is required.
        self.dts_instance_id = dts_instance_id
        # The synchronization task ID. You can call the [DescribeDtsJobs](https://help.aliyun.com/document_detail/209702.html) operation to query the task ID.
        self.dts_job_id = dts_job_id
        # The operator that is related to the extract, transform, and load (ETL) feature and dedicated to T+1 business.
        self.etl_operator_column_reference = etl_operator_column_reference
        # The endpoint of the Object Storage Service (OSS) bucket in which the files to be synchronized are stored.
        self.file_oss_url = file_oss_url
        # The name of the table to be filtered.
        self.filter_table_name = filter_table_name
        # The method that is used to modify the data synchronization task. If you do not specify the parameter, the objects of the data synchronization task are modified by default. If you specify UPDATE_RESERVED for the parameter, the reserved parameters are modified.
        self.modify_type_enum = modify_type_enum
        # The ID of the region in which the data synchronization instance resides. For more information, see [List of supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region_id = region_id
        # The reserved parameters of the data synchronization task. You can add reserved parameters instead of overwriting the existing reserved parameters. The value of the parameter is a MAP JSON string. You can specify this parameter to meet special requirements, such as specifying whether to automatically start the precheck of the data synchronization task. For more information, see [MigrationReserved](https://help.aliyun.com/document_detail/176470.html).
        self.reserved = reserved
        # Resource group ID.
        self.resource_group_id = resource_group_id
        # Specifies whether to perform schema migration or synchronization. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.structure_initialization = structure_initialization
        # The synchronization direction. Valid values:
        # 
        # *   **Forward**: Data is synchronized from the source database to the destination database.
        # *   **Reverse**: Data is synchronized from the destination database to the source database.
        # 
        # > 
        # *   Default value: **Forward**.
        # *   This parameter is required only if the topology of the data synchronization instance is two-way synchronization.
        self.synchronization_direction = synchronization_direction
        # Whether it is a seamless integration (Zero-ETL) task, the value can be:
        # - **false**: No. - **true**: Yes.
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

        if self.db_list_shrink is not None:
            result['DbList'] = self.db_list_shrink

        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id

        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id

        if self.etl_operator_column_reference is not None:
            result['EtlOperatorColumnReference'] = self.etl_operator_column_reference

        if self.file_oss_url is not None:
            result['FileOssUrl'] = self.file_oss_url

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
            self.db_list_shrink = m.get('DbList')

        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')

        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')

        if m.get('EtlOperatorColumnReference') is not None:
            self.etl_operator_column_reference = m.get('EtlOperatorColumnReference')

        if m.get('FileOssUrl') is not None:
            self.file_oss_url = m.get('FileOssUrl')

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

