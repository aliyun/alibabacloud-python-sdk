# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dts20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeInitializationStatusResponseBody(DaraModel):
    def __init__(
        self,
        data_initialization_details: List[main_models.DescribeInitializationStatusResponseBodyDataInitializationDetails] = None,
        data_synchronization_details: List[main_models.DescribeInitializationStatusResponseBodyDataSynchronizationDetails] = None,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        structure_initialization_details: List[main_models.DescribeInitializationStatusResponseBodyStructureInitializationDetails] = None,
        success: str = None,
    ):
        # The details of initial full data synchronization.
        self.data_initialization_details = data_initialization_details
        # The details of incremental data synchronization.
        # 
        # >  This parameter and the parameters it contains will be removed in the future.
        self.data_synchronization_details = data_synchronization_details
        # The error code returned if the call failed.
        self.err_code = err_code
        # The error message returned if the call failed.
        self.err_message = err_message
        # The ID of the request.
        self.request_id = request_id
        # The details of initial schema synchronization.
        self.structure_initialization_details = structure_initialization_details
        # Indicates whether the call was successful.
        self.success = success

    def validate(self):
        if self.data_initialization_details:
            for v1 in self.data_initialization_details:
                 if v1:
                    v1.validate()
        if self.data_synchronization_details:
            for v1 in self.data_synchronization_details:
                 if v1:
                    v1.validate()
        if self.structure_initialization_details:
            for v1 in self.structure_initialization_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataInitializationDetails'] = []
        if self.data_initialization_details is not None:
            for k1 in self.data_initialization_details:
                result['DataInitializationDetails'].append(k1.to_map() if k1 else None)

        result['DataSynchronizationDetails'] = []
        if self.data_synchronization_details is not None:
            for k1 in self.data_synchronization_details:
                result['DataSynchronizationDetails'].append(k1.to_map() if k1 else None)

        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['StructureInitializationDetails'] = []
        if self.structure_initialization_details is not None:
            for k1 in self.structure_initialization_details:
                result['StructureInitializationDetails'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_initialization_details = []
        if m.get('DataInitializationDetails') is not None:
            for k1 in m.get('DataInitializationDetails'):
                temp_model = main_models.DescribeInitializationStatusResponseBodyDataInitializationDetails()
                self.data_initialization_details.append(temp_model.from_map(k1))

        self.data_synchronization_details = []
        if m.get('DataSynchronizationDetails') is not None:
            for k1 in m.get('DataSynchronizationDetails'):
                temp_model = main_models.DescribeInitializationStatusResponseBodyDataSynchronizationDetails()
                self.data_synchronization_details.append(temp_model.from_map(k1))

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.structure_initialization_details = []
        if m.get('StructureInitializationDetails') is not None:
            for k1 in m.get('StructureInitializationDetails'):
                temp_model = main_models.DescribeInitializationStatusResponseBodyStructureInitializationDetails()
                self.structure_initialization_details.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeInitializationStatusResponseBodyStructureInitializationDetails(DaraModel):
    def __init__(
        self,
        constraints: List[main_models.DescribeInitializationStatusResponseBodyStructureInitializationDetailsConstraints] = None,
        destination_owner_dbname: str = None,
        error_message: str = None,
        object_definition: str = None,
        object_name: str = None,
        object_type: str = None,
        source_owner_dbname: str = None,
        status: str = None,
    ):
        # The constraints of the synchronization object, such as indexes and foreign keys.
        # 
        # >  This parameter is returned only if the **ObjectType** parameter is set to **Table** and the synchronization object has constraints.
        self.constraints = constraints
        # The name of the database to which the object in the destination instance belongs.
        self.destination_owner_dbname = destination_owner_dbname
        # The error message returned if initial schema synchronization failed.
        self.error_message = error_message
        # The schema of the object.
        self.object_definition = object_definition
        # The name of the object.
        self.object_name = object_name
        # The type of the object. Valid values:
        # 
        # **Table**, **Constraint**, **Index**, **View**, **Materialize View**, **Type**, **Synonym**, **Trigger**, **Function**, **Procedure**, **Package**, **Default**, **Rule**, **PlanGuide**, and **Sequence**.
        self.object_type = object_type
        # The name of the database to which the object in the source instance belongs.
        self.source_owner_dbname = source_owner_dbname
        # The status of initial schema synchronization. Valid values:
        # 
        # *   **NotStarted**
        # *   **Migrating**
        # *   **Failed**
        # *   **Finished**
        self.status = status

    def validate(self):
        if self.constraints:
            for v1 in self.constraints:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Constraints'] = []
        if self.constraints is not None:
            for k1 in self.constraints:
                result['Constraints'].append(k1.to_map() if k1 else None)

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
        self.constraints = []
        if m.get('Constraints') is not None:
            for k1 in m.get('Constraints'):
                temp_model = main_models.DescribeInitializationStatusResponseBodyStructureInitializationDetailsConstraints()
                self.constraints.append(temp_model.from_map(k1))

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

class DescribeInitializationStatusResponseBodyStructureInitializationDetailsConstraints(DaraModel):
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
        # The name of the database to which the object in the destination instance belongs.
        self.destination_owner_dbname = destination_owner_dbname
        # The error message returned if constraints failed to be created.
        self.error_message = error_message
        # The syntax to create constraints.
        self.object_definition = object_definition
        # The name of the object.
        self.object_name = object_name
        # The type of the object. Valid value: **Table**.
        self.object_type = object_type
        # The name of the database to which the object in the source instance belongs.
        self.source_owner_dbname = source_owner_dbname
        # The status of constraint creation. Valid values:
        # 
        # *   **NotStarted**
        # *   **Migrating**
        # *   **Failed**
        # *   **Finished**
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

class DescribeInitializationStatusResponseBodyDataSynchronizationDetails(DaraModel):
    def __init__(
        self,
        destination_owner_dbname: str = None,
        error_message: str = None,
        source_owner_dbname: str = None,
        status: str = None,
        table_name: str = None,
    ):
        # The name of the database to which the object in the destination instance belongs.
        self.destination_owner_dbname = destination_owner_dbname
        # The error message returned if incremental data synchronization failed.
        self.error_message = error_message
        # The name of the database to which the object in the source instance belongs.
        self.source_owner_dbname = source_owner_dbname
        # The status of incremental data synchronization. Valid values:
        # 
        # *   **NotStarted**
        # *   **Migrating**
        # *   **Failed**
        # *   **Finished**
        self.status = status
        # The table name.
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

class DescribeInitializationStatusResponseBodyDataInitializationDetails(DaraModel):
    def __init__(
        self,
        destination_owner_dbname: str = None,
        error_message: str = None,
        finish_row_num: str = None,
        source_owner_dbname: str = None,
        status: str = None,
        table_name: str = None,
        total_row_num: str = None,
        used_time: str = None,
    ):
        # The name of the database to which the object in the destination instance belongs.
        self.destination_owner_dbname = destination_owner_dbname
        # The error message returned if initial full data synchronization failed.
        self.error_message = error_message
        # The total number of rows that are actually synchronized.
        # 
        # >  This parameter indicates the total number of actually synchronized rows. In contrast, the value of the **TotalRowNum** parameter is calculated based on the system tables in the source database. The values of the two parameters may be different due to time difference.
        self.finish_row_num = finish_row_num
        # The name of the database to which the object in the source instance belongs.
        self.source_owner_dbname = source_owner_dbname
        # The status of initial full data synchronization. Valid values:
        # 
        # *   **NotStarted**
        # *   **Migrating**
        # *   **Failed**
        # *   **Finished**
        self.status = status
        # The table name.
        self.table_name = table_name
        # The total number of rows that are supposed to be synchronized.
        # 
        # >  The value of this parameter is calculated based on the system tables in the source database. In contrast, the **FinishRowNum** parameter indicates the total number of actually synchronized rows. The values of the two parameters may be different due to time difference.
        self.total_row_num = total_row_num
        # The time spent on full data synchronization.
        self.used_time = used_time

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

        if self.source_owner_dbname is not None:
            result['SourceOwnerDBName'] = self.source_owner_dbname

        if self.status is not None:
            result['Status'] = self.status

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.total_row_num is not None:
            result['TotalRowNum'] = self.total_row_num

        if self.used_time is not None:
            result['UsedTime'] = self.used_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationOwnerDBName') is not None:
            self.destination_owner_dbname = m.get('DestinationOwnerDBName')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('FinishRowNum') is not None:
            self.finish_row_num = m.get('FinishRowNum')

        if m.get('SourceOwnerDBName') is not None:
            self.source_owner_dbname = m.get('SourceOwnerDBName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('TotalRowNum') is not None:
            self.total_row_num = m.get('TotalRowNum')

        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')

        return self

