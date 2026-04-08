# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dts20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeMigrationJobDetailResponseBody(DaraModel):
    def __init__(
        self,
        data_initialization_detail_list: main_models.DescribeMigrationJobDetailResponseBodyDataInitializationDetailList = None,
        data_synchronization_detail_list: main_models.DescribeMigrationJobDetailResponseBodyDataSynchronizationDetailList = None,
        err_code: str = None,
        err_message: str = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        structure_initialization_detail_list: main_models.DescribeMigrationJobDetailResponseBodyStructureInitializationDetailList = None,
        success: str = None,
        total_record_count: int = None,
    ):
        self.data_initialization_detail_list = data_initialization_detail_list
        self.data_synchronization_detail_list = data_synchronization_detail_list
        # Specifies whether to query the details of incremental data migration. Valid values:
        # 
        # *   **true**: yes
        # 
        # *   **false**: no
        # 
        # > Default value: **false**
        self.err_code = err_code
        # The ID of the request.
        self.err_message = err_message
        # The error code returned if the call failed.
        self.page_number = page_number
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests. The **ClientToken** value can contain only ASCII characters and cannot exceed 64 characters in length.
        self.page_record_count = page_record_count
        # Specifies whether to query the details of full data migration. Valid values:
        # 
        # *   **true**: yes
        # 
        # *   **false**: no
        # 
        # > Default value: **false**
        self.request_id = request_id
        self.structure_initialization_detail_list = structure_initialization_detail_list
        # The ID of the Alibaba Cloud account. You do not need to specify this parameter because this parameter will be removed in the future.
        self.success = success
        # Resource group ID.
        self.total_record_count = total_record_count

    def validate(self):
        if self.data_initialization_detail_list:
            self.data_initialization_detail_list.validate()
        if self.data_synchronization_detail_list:
            self.data_synchronization_detail_list.validate()
        if self.structure_initialization_detail_list:
            self.structure_initialization_detail_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_initialization_detail_list is not None:
            result['DataInitializationDetailList'] = self.data_initialization_detail_list.to_map()

        if self.data_synchronization_detail_list is not None:
            result['DataSynchronizationDetailList'] = self.data_synchronization_detail_list.to_map()

        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.structure_initialization_detail_list is not None:
            result['StructureInitializationDetailList'] = self.structure_initialization_detail_list.to_map()

        if self.success is not None:
            result['Success'] = self.success

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInitializationDetailList') is not None:
            temp_model = main_models.DescribeMigrationJobDetailResponseBodyDataInitializationDetailList()
            self.data_initialization_detail_list = temp_model.from_map(m.get('DataInitializationDetailList'))

        if m.get('DataSynchronizationDetailList') is not None:
            temp_model = main_models.DescribeMigrationJobDetailResponseBodyDataSynchronizationDetailList()
            self.data_synchronization_detail_list = temp_model.from_map(m.get('DataSynchronizationDetailList'))

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StructureInitializationDetailList') is not None:
            temp_model = main_models.DescribeMigrationJobDetailResponseBodyStructureInitializationDetailList()
            self.structure_initialization_detail_list = temp_model.from_map(m.get('StructureInitializationDetailList'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeMigrationJobDetailResponseBodyStructureInitializationDetailList(DaraModel):
    def __init__(
        self,
        structure_initialization_detail: List[main_models.DescribeMigrationJobDetailResponseBodyStructureInitializationDetailListStructureInitializationDetail] = None,
    ):
        self.structure_initialization_detail = structure_initialization_detail

    def validate(self):
        if self.structure_initialization_detail:
            for v1 in self.structure_initialization_detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['StructureInitializationDetail'] = []
        if self.structure_initialization_detail is not None:
            for k1 in self.structure_initialization_detail:
                result['StructureInitializationDetail'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.structure_initialization_detail = []
        if m.get('StructureInitializationDetail') is not None:
            for k1 in m.get('StructureInitializationDetail'):
                temp_model = main_models.DescribeMigrationJobDetailResponseBodyStructureInitializationDetailListStructureInitializationDetail()
                self.structure_initialization_detail.append(temp_model.from_map(k1))

        return self

class DescribeMigrationJobDetailResponseBodyStructureInitializationDetailListStructureInitializationDetail(DaraModel):
    def __init__(
        self,
        constraint_list: main_models.DescribeMigrationJobDetailResponseBodyStructureInitializationDetailListStructureInitializationDetailConstraintList = None,
        destination_owner_dbname: str = None,
        error_message: str = None,
        object_definition: str = None,
        object_name: str = None,
        object_type: str = None,
        source_owner_dbname: str = None,
        status: str = None,
    ):
        self.constraint_list = constraint_list
        self.destination_owner_dbname = destination_owner_dbname
        self.error_message = error_message
        self.object_definition = object_definition
        self.object_name = object_name
        self.object_type = object_type
        self.source_owner_dbname = source_owner_dbname
        self.status = status

    def validate(self):
        if self.constraint_list:
            self.constraint_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.constraint_list is not None:
            result['ConstraintList'] = self.constraint_list.to_map()

        if self.destination_owner_dbname is not None:
            result['DestinationOwnerDBName'] = self.destination_owner_dbname

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.object_definition is not None:
            result['ObjectDefinition'] = self.object_definition

        if self.object_name is not None:
            result['ObjectName'] = self.object_name

        if self.object_type is not None:
            result['ObjectType'] = self.object_type

        if self.source_owner_dbname is not None:
            result['SourceOwnerDBName'] = self.source_owner_dbname

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConstraintList') is not None:
            temp_model = main_models.DescribeMigrationJobDetailResponseBodyStructureInitializationDetailListStructureInitializationDetailConstraintList()
            self.constraint_list = temp_model.from_map(m.get('ConstraintList'))

        if m.get('DestinationOwnerDBName') is not None:
            self.destination_owner_dbname = m.get('DestinationOwnerDBName')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('ObjectDefinition') is not None:
            self.object_definition = m.get('ObjectDefinition')

        if m.get('ObjectName') is not None:
            self.object_name = m.get('ObjectName')

        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')

        if m.get('SourceOwnerDBName') is not None:
            self.source_owner_dbname = m.get('SourceOwnerDBName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeMigrationJobDetailResponseBodyStructureInitializationDetailListStructureInitializationDetailConstraintList(DaraModel):
    def __init__(
        self,
        structure_initialization_detail: List[main_models.DescribeMigrationJobDetailResponseBodyStructureInitializationDetailListStructureInitializationDetailConstraintListStructureInitializationDetail] = None,
    ):
        self.structure_initialization_detail = structure_initialization_detail

    def validate(self):
        if self.structure_initialization_detail:
            for v1 in self.structure_initialization_detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['StructureInitializationDetail'] = []
        if self.structure_initialization_detail is not None:
            for k1 in self.structure_initialization_detail:
                result['StructureInitializationDetail'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.structure_initialization_detail = []
        if m.get('StructureInitializationDetail') is not None:
            for k1 in m.get('StructureInitializationDetail'):
                temp_model = main_models.DescribeMigrationJobDetailResponseBodyStructureInitializationDetailListStructureInitializationDetailConstraintListStructureInitializationDetail()
                self.structure_initialization_detail.append(temp_model.from_map(k1))

        return self

class DescribeMigrationJobDetailResponseBodyStructureInitializationDetailListStructureInitializationDetailConstraintListStructureInitializationDetail(DaraModel):
    def __init__(
        self,
        destination_owner_dbname: str = None,
        error_message: str = None,
        object_definition: str = None,
        object_name: str = None,
        object_type: str = None,
        source_owner_dbname: str = None,
        status: str = None,
    ):
        self.destination_owner_dbname = destination_owner_dbname
        self.error_message = error_message
        self.object_definition = object_definition
        self.object_name = object_name
        self.object_type = object_type
        self.source_owner_dbname = source_owner_dbname
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination_owner_dbname is not None:
            result['DestinationOwnerDBName'] = self.destination_owner_dbname

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.object_definition is not None:
            result['ObjectDefinition'] = self.object_definition

        if self.object_name is not None:
            result['ObjectName'] = self.object_name

        if self.object_type is not None:
            result['ObjectType'] = self.object_type

        if self.source_owner_dbname is not None:
            result['SourceOwnerDBName'] = self.source_owner_dbname

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationOwnerDBName') is not None:
            self.destination_owner_dbname = m.get('DestinationOwnerDBName')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('ObjectDefinition') is not None:
            self.object_definition = m.get('ObjectDefinition')

        if m.get('ObjectName') is not None:
            self.object_name = m.get('ObjectName')

        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')

        if m.get('SourceOwnerDBName') is not None:
            self.source_owner_dbname = m.get('SourceOwnerDBName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeMigrationJobDetailResponseBodyDataSynchronizationDetailList(DaraModel):
    def __init__(
        self,
        data_synchronization_detail: List[main_models.DescribeMigrationJobDetailResponseBodyDataSynchronizationDetailListDataSynchronizationDetail] = None,
    ):
        self.data_synchronization_detail = data_synchronization_detail

    def validate(self):
        if self.data_synchronization_detail:
            for v1 in self.data_synchronization_detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataSynchronizationDetail'] = []
        if self.data_synchronization_detail is not None:
            for k1 in self.data_synchronization_detail:
                result['DataSynchronizationDetail'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_synchronization_detail = []
        if m.get('DataSynchronizationDetail') is not None:
            for k1 in m.get('DataSynchronizationDetail'):
                temp_model = main_models.DescribeMigrationJobDetailResponseBodyDataSynchronizationDetailListDataSynchronizationDetail()
                self.data_synchronization_detail.append(temp_model.from_map(k1))

        return self

class DescribeMigrationJobDetailResponseBodyDataSynchronizationDetailListDataSynchronizationDetail(DaraModel):
    def __init__(
        self,
        destination_owner_dbname: str = None,
        error_message: str = None,
        source_owner_dbname: str = None,
        status: str = None,
        table_name: str = None,
    ):
        self.destination_owner_dbname = destination_owner_dbname
        self.error_message = error_message
        self.source_owner_dbname = source_owner_dbname
        self.status = status
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination_owner_dbname is not None:
            result['DestinationOwnerDBName'] = self.destination_owner_dbname

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.source_owner_dbname is not None:
            result['SourceOwnerDBName'] = self.source_owner_dbname

        if self.status is not None:
            result['Status'] = self.status

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationOwnerDBName') is not None:
            self.destination_owner_dbname = m.get('DestinationOwnerDBName')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('SourceOwnerDBName') is not None:
            self.source_owner_dbname = m.get('SourceOwnerDBName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

class DescribeMigrationJobDetailResponseBodyDataInitializationDetailList(DaraModel):
    def __init__(
        self,
        data_initialization_detail: List[main_models.DescribeMigrationJobDetailResponseBodyDataInitializationDetailListDataInitializationDetail] = None,
    ):
        self.data_initialization_detail = data_initialization_detail

    def validate(self):
        if self.data_initialization_detail:
            for v1 in self.data_initialization_detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataInitializationDetail'] = []
        if self.data_initialization_detail is not None:
            for k1 in self.data_initialization_detail:
                result['DataInitializationDetail'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_initialization_detail = []
        if m.get('DataInitializationDetail') is not None:
            for k1 in m.get('DataInitializationDetail'):
                temp_model = main_models.DescribeMigrationJobDetailResponseBodyDataInitializationDetailListDataInitializationDetail()
                self.data_initialization_detail.append(temp_model.from_map(k1))

        return self

class DescribeMigrationJobDetailResponseBodyDataInitializationDetailListDataInitializationDetail(DaraModel):
    def __init__(
        self,
        destination_owner_dbname: str = None,
        error_message: str = None,
        finish_row_num: str = None,
        migration_time: str = None,
        source_owner_dbname: str = None,
        status: str = None,
        table_name: str = None,
        total_row_num: str = None,
    ):
        self.destination_owner_dbname = destination_owner_dbname
        self.error_message = error_message
        self.finish_row_num = finish_row_num
        self.migration_time = migration_time
        self.source_owner_dbname = source_owner_dbname
        self.status = status
        self.table_name = table_name
        self.total_row_num = total_row_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination_owner_dbname is not None:
            result['DestinationOwnerDBName'] = self.destination_owner_dbname

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.finish_row_num is not None:
            result['FinishRowNum'] = self.finish_row_num

        if self.migration_time is not None:
            result['MigrationTime'] = self.migration_time

        if self.source_owner_dbname is not None:
            result['SourceOwnerDBName'] = self.source_owner_dbname

        if self.status is not None:
            result['Status'] = self.status

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.total_row_num is not None:
            result['TotalRowNum'] = self.total_row_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationOwnerDBName') is not None:
            self.destination_owner_dbname = m.get('DestinationOwnerDBName')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('FinishRowNum') is not None:
            self.finish_row_num = m.get('FinishRowNum')

        if m.get('MigrationTime') is not None:
            self.migration_time = m.get('MigrationTime')

        if m.get('SourceOwnerDBName') is not None:
            self.source_owner_dbname = m.get('SourceOwnerDBName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('TotalRowNum') is not None:
            self.total_row_num = m.get('TotalRowNum')

        return self

