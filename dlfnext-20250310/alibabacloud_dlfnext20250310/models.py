# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class Catalog(TeaModel):
    def __init__(
        self,
        created_at: int = None,
        created_by: str = None,
        id: str = None,
        name: str = None,
        options: Dict[str, str] = None,
        owner: str = None,
        status: str = None,
        type: str = None,
        updated_at: int = None,
        updated_by: str = None,
    ):
        self.created_at = created_at
        self.created_by = created_by
        self.id = id
        self.name = name
        self.options = options
        self.owner = owner
        self.status = status
        self.type = type
        self.updated_at = updated_at
        self.updated_by = updated_by

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.created_by is not None:
            result['createdBy'] = self.created_by
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.options is not None:
            result['options'] = self.options
        if self.owner is not None:
            result['owner'] = self.owner
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at
        if self.updated_by is not None:
            result['updatedBy'] = self.updated_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('createdBy') is not None:
            self.created_by = m.get('createdBy')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('options') is not None:
            self.options = m.get('options')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')
        if m.get('updatedBy') is not None:
            self.updated_by = m.get('updatedBy')
        return self


class MoMValues(TeaModel):
    def __init__(
        self,
        current_value: int = None,
        last_day_value: int = None,
        last_month_value: int = None,
    ):
        # total
        self.current_value = current_value
        # daily addition
        self.last_day_value = last_day_value
        # monthly addition
        self.last_month_value = last_month_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_value is not None:
            result['currentValue'] = self.current_value
        if self.last_day_value is not None:
            result['lastDayValue'] = self.last_day_value
        if self.last_month_value is not None:
            result['lastMonthValue'] = self.last_month_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentValue') is not None:
            self.current_value = m.get('currentValue')
        if m.get('lastDayValue') is not None:
            self.last_day_value = m.get('lastDayValue')
        if m.get('lastMonthValue') is not None:
            self.last_month_value = m.get('lastMonthValue')
        return self


class CatalogSummary(TeaModel):
    def __init__(
        self,
        api_visit_count_monthly: int = None,
        database_count: MoMValues = None,
        file_access_count_monthly: int = None,
        generated_date: str = None,
        partition_count: MoMValues = None,
        table_count: MoMValues = None,
        throughput_monthly: int = None,
        total_file_count: MoMValues = None,
        total_file_size_in_bytes: MoMValues = None,
    ):
        self.api_visit_count_monthly = api_visit_count_monthly
        self.database_count = database_count
        self.file_access_count_monthly = file_access_count_monthly
        # Update date of the statistics
        self.generated_date = generated_date
        self.partition_count = partition_count
        self.table_count = table_count
        self.throughput_monthly = throughput_monthly
        self.total_file_count = total_file_count
        self.total_file_size_in_bytes = total_file_size_in_bytes

    def validate(self):
        if self.database_count:
            self.database_count.validate()
        if self.partition_count:
            self.partition_count.validate()
        if self.table_count:
            self.table_count.validate()
        if self.total_file_count:
            self.total_file_count.validate()
        if self.total_file_size_in_bytes:
            self.total_file_size_in_bytes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_visit_count_monthly is not None:
            result['apiVisitCountMonthly'] = self.api_visit_count_monthly
        if self.database_count is not None:
            result['databaseCount'] = self.database_count.to_map()
        if self.file_access_count_monthly is not None:
            result['fileAccessCountMonthly'] = self.file_access_count_monthly
        if self.generated_date is not None:
            result['generatedDate'] = self.generated_date
        if self.partition_count is not None:
            result['partitionCount'] = self.partition_count.to_map()
        if self.table_count is not None:
            result['tableCount'] = self.table_count.to_map()
        if self.throughput_monthly is not None:
            result['throughputMonthly'] = self.throughput_monthly
        if self.total_file_count is not None:
            result['totalFileCount'] = self.total_file_count.to_map()
        if self.total_file_size_in_bytes is not None:
            result['totalFileSizeInBytes'] = self.total_file_size_in_bytes.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVisitCountMonthly') is not None:
            self.api_visit_count_monthly = m.get('apiVisitCountMonthly')
        if m.get('databaseCount') is not None:
            temp_model = MoMValues()
            self.database_count = temp_model.from_map(m['databaseCount'])
        if m.get('fileAccessCountMonthly') is not None:
            self.file_access_count_monthly = m.get('fileAccessCountMonthly')
        if m.get('generatedDate') is not None:
            self.generated_date = m.get('generatedDate')
        if m.get('partitionCount') is not None:
            temp_model = MoMValues()
            self.partition_count = temp_model.from_map(m['partitionCount'])
        if m.get('tableCount') is not None:
            temp_model = MoMValues()
            self.table_count = temp_model.from_map(m['tableCount'])
        if m.get('throughputMonthly') is not None:
            self.throughput_monthly = m.get('throughputMonthly')
        if m.get('totalFileCount') is not None:
            temp_model = MoMValues()
            self.total_file_count = temp_model.from_map(m['totalFileCount'])
        if m.get('totalFileSizeInBytes') is not None:
            temp_model = MoMValues()
            self.total_file_size_in_bytes = temp_model.from_map(m['totalFileSizeInBytes'])
        return self


class DateSummary(TeaModel):
    def __init__(
        self,
        date: str = None,
        value: int = None,
    ):
        self.date = date
        # Metric value at corresponding date
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['date'] = self.date
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class CatalogSummaryTrend(TeaModel):
    def __init__(
        self,
        api_visit_count: List[DateSummary] = None,
        file_access_count: List[DateSummary] = None,
        throughput: List[DateSummary] = None,
        total_file_count: List[DateSummary] = None,
        total_file_size_in_bytes: List[DateSummary] = None,
        total_meta_count: List[DateSummary] = None,
    ):
        # API visit count trends
        self.api_visit_count = api_visit_count
        # file access count trends
        self.file_access_count = file_access_count
        # Table count trends
        self.throughput = throughput
        # Historical total file count
        self.total_file_count = total_file_count
        # Database count trends
        self.total_file_size_in_bytes = total_file_size_in_bytes
        # Latest snapshot file count
        self.total_meta_count = total_meta_count

    def validate(self):
        if self.api_visit_count:
            for k in self.api_visit_count:
                if k:
                    k.validate()
        if self.file_access_count:
            for k in self.file_access_count:
                if k:
                    k.validate()
        if self.throughput:
            for k in self.throughput:
                if k:
                    k.validate()
        if self.total_file_count:
            for k in self.total_file_count:
                if k:
                    k.validate()
        if self.total_file_size_in_bytes:
            for k in self.total_file_size_in_bytes:
                if k:
                    k.validate()
        if self.total_meta_count:
            for k in self.total_meta_count:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['apiVisitCount'] = []
        if self.api_visit_count is not None:
            for k in self.api_visit_count:
                result['apiVisitCount'].append(k.to_map() if k else None)
        result['fileAccessCount'] = []
        if self.file_access_count is not None:
            for k in self.file_access_count:
                result['fileAccessCount'].append(k.to_map() if k else None)
        result['throughput'] = []
        if self.throughput is not None:
            for k in self.throughput:
                result['throughput'].append(k.to_map() if k else None)
        result['totalFileCount'] = []
        if self.total_file_count is not None:
            for k in self.total_file_count:
                result['totalFileCount'].append(k.to_map() if k else None)
        result['totalFileSizeInBytes'] = []
        if self.total_file_size_in_bytes is not None:
            for k in self.total_file_size_in_bytes:
                result['totalFileSizeInBytes'].append(k.to_map() if k else None)
        result['totalMetaCount'] = []
        if self.total_meta_count is not None:
            for k in self.total_meta_count:
                result['totalMetaCount'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_visit_count = []
        if m.get('apiVisitCount') is not None:
            for k in m.get('apiVisitCount'):
                temp_model = DateSummary()
                self.api_visit_count.append(temp_model.from_map(k))
        self.file_access_count = []
        if m.get('fileAccessCount') is not None:
            for k in m.get('fileAccessCount'):
                temp_model = DateSummary()
                self.file_access_count.append(temp_model.from_map(k))
        self.throughput = []
        if m.get('throughput') is not None:
            for k in m.get('throughput'):
                temp_model = DateSummary()
                self.throughput.append(temp_model.from_map(k))
        self.total_file_count = []
        if m.get('totalFileCount') is not None:
            for k in m.get('totalFileCount'):
                temp_model = DateSummary()
                self.total_file_count.append(temp_model.from_map(k))
        self.total_file_size_in_bytes = []
        if m.get('totalFileSizeInBytes') is not None:
            for k in m.get('totalFileSizeInBytes'):
                temp_model = DateSummary()
                self.total_file_size_in_bytes.append(temp_model.from_map(k))
        self.total_meta_count = []
        if m.get('totalMetaCount') is not None:
            for k in m.get('totalMetaCount'):
                temp_model = DateSummary()
                self.total_meta_count.append(temp_model.from_map(k))
        return self


class FullDataType(TeaModel):
    def __init__(
        self,
        element: 'FullDataType' = None,
        fields: List[DataField] = None,
        key: 'FullDataType' = None,
        type: str = None,
        value: 'FullDataType' = None,
    ):
        self.element = element
        self.fields = fields
        self.key = key
        self.type = type
        self.value = value

    def validate(self):
        if self.element:
            self.element.validate()
        if self.fields:
            for k in self.fields:
                if k:
                    k.validate()
        if self.key:
            self.key.validate()
        if self.value:
            self.value.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.element is not None:
            result['element'] = self.element.to_map()
        result['fields'] = []
        if self.fields is not None:
            for k in self.fields:
                result['fields'].append(k.to_map() if k else None)
        if self.key is not None:
            result['key'] = self.key.to_map()
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('element') is not None:
            temp_model = FullDataType()
            self.element = temp_model.from_map(m['element'])
        self.fields = []
        if m.get('fields') is not None:
            for k in m.get('fields'):
                temp_model = DataField()
                self.fields.append(temp_model.from_map(k))
        if m.get('key') is not None:
            temp_model = FullDataType()
            self.key = temp_model.from_map(m['key'])
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            temp_model = FullDataType()
            self.value = temp_model.from_map(m['value'])
        return self


class DataField(TeaModel):
    def __init__(
        self,
        description: str = None,
        id: int = None,
        name: str = None,
        type: FullDataType = None,
    ):
        self.description = description
        self.id = id
        self.name = name
        self.type = type

    def validate(self):
        if self.type:
            self.type.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            temp_model = FullDataType()
            self.type = temp_model.from_map(m['type'])
        return self


class Database(TeaModel):
    def __init__(
        self,
        created_at: int = None,
        created_by: str = None,
        id: str = None,
        location: str = None,
        name: str = None,
        options: Dict[str, str] = None,
        owner: str = None,
        updated_at: int = None,
        updated_by: str = None,
    ):
        self.created_at = created_at
        self.created_by = created_by
        self.id = id
        self.location = location
        self.name = name
        self.options = options
        self.owner = owner
        self.updated_at = updated_at
        self.updated_by = updated_by

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.created_by is not None:
            result['createdBy'] = self.created_by
        if self.id is not None:
            result['id'] = self.id
        if self.location is not None:
            result['location'] = self.location
        if self.name is not None:
            result['name'] = self.name
        if self.options is not None:
            result['options'] = self.options
        if self.owner is not None:
            result['owner'] = self.owner
        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at
        if self.updated_by is not None:
            result['updatedBy'] = self.updated_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('createdBy') is not None:
            self.created_by = m.get('createdBy')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('options') is not None:
            self.options = m.get('options')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')
        if m.get('updatedBy') is not None:
            self.updated_by = m.get('updatedBy')
        return self


class DatabaseSummary(TeaModel):
    def __init__(
        self,
        created_at: int = None,
        database_name: str = None,
        generated_date: str = None,
        location: str = None,
        partition_count: int = None,
        table_count: int = None,
        total_file_count: int = None,
        total_file_size_in_bytes: int = None,
    ):
        # Creation timestamp in milliseconds
        self.created_at = created_at
        # 库名 - Database name
        self.database_name = database_name
        # Last profile update date in format yyyyMMdd
        self.generated_date = generated_date
        # Storage location URI
        self.location = location
        self.partition_count = partition_count
        # Total storage in bytes
        self.table_count = table_count
        self.total_file_count = total_file_count
        # Total file count
        self.total_file_size_in_bytes = total_file_size_in_bytes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.database_name is not None:
            result['databaseName'] = self.database_name
        if self.generated_date is not None:
            result['generatedDate'] = self.generated_date
        if self.location is not None:
            result['location'] = self.location
        if self.partition_count is not None:
            result['partitionCount'] = self.partition_count
        if self.table_count is not None:
            result['tableCount'] = self.table_count
        if self.total_file_count is not None:
            result['totalFileCount'] = self.total_file_count
        if self.total_file_size_in_bytes is not None:
            result['totalFileSizeInBytes'] = self.total_file_size_in_bytes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('databaseName') is not None:
            self.database_name = m.get('databaseName')
        if m.get('generatedDate') is not None:
            self.generated_date = m.get('generatedDate')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('partitionCount') is not None:
            self.partition_count = m.get('partitionCount')
        if m.get('tableCount') is not None:
            self.table_count = m.get('tableCount')
        if m.get('totalFileCount') is not None:
            self.total_file_count = m.get('totalFileCount')
        if m.get('totalFileSizeInBytes') is not None:
            self.total_file_size_in_bytes = m.get('totalFileSizeInBytes')
        return self


class ErrorResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        resource_name: str = None,
        resource_type: str = None,
    ):
        self.code = code
        self.message = message
        self.resource_name = resource_name
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.resource_name is not None:
            result['resourceName'] = self.resource_name
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('resourceName') is not None:
            self.resource_name = m.get('resourceName')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class PermissionColumns(TeaModel):
    def __init__(
        self,
        column_names: List[str] = None,
        excluded_column_names: List[str] = None,
    ):
        self.column_names = column_names
        self.excluded_column_names = excluded_column_names

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.column_names is not None:
            result['columnNames'] = self.column_names
        if self.excluded_column_names is not None:
            result['excludedColumnNames'] = self.excluded_column_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('columnNames') is not None:
            self.column_names = m.get('columnNames')
        if m.get('excludedColumnNames') is not None:
            self.excluded_column_names = m.get('excludedColumnNames')
        return self


class Permission(TeaModel):
    def __init__(
        self,
        access: str = None,
        columns: PermissionColumns = None,
        database: str = None,
        function: str = None,
        principal: str = None,
        resource_type: str = None,
        table: str = None,
        view: str = None,
    ):
        self.access = access
        self.columns = columns
        self.database = database
        self.function = function
        self.principal = principal
        self.resource_type = resource_type
        self.table = table
        self.view = view

    def validate(self):
        if self.columns:
            self.columns.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access is not None:
            result['access'] = self.access
        if self.columns is not None:
            result['columns'] = self.columns.to_map()
        if self.database is not None:
            result['database'] = self.database
        if self.function is not None:
            result['function'] = self.function
        if self.principal is not None:
            result['principal'] = self.principal
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.table is not None:
            result['table'] = self.table
        if self.view is not None:
            result['view'] = self.view
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('access') is not None:
            self.access = m.get('access')
        if m.get('columns') is not None:
            temp_model = PermissionColumns()
            self.columns = temp_model.from_map(m['columns'])
        if m.get('database') is not None:
            self.database = m.get('database')
        if m.get('function') is not None:
            self.function = m.get('function')
        if m.get('principal') is not None:
            self.principal = m.get('principal')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('table') is not None:
            self.table = m.get('table')
        if m.get('view') is not None:
            self.view = m.get('view')
        return self


class FailurePermission(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        permission: Permission = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.permission = permission

    def validate(self):
        if self.permission:
            self.permission.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.permission is not None:
            result['permission'] = self.permission.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('permission') is not None:
            temp_model = Permission()
            self.permission = temp_model.from_map(m['permission'])
        return self


class FullInstant(TeaModel):
    def __init__(
        self,
        snapshot_id: int = None,
        tag_name: str = None,
        type: str = None,
    ):
        self.snapshot_id = snapshot_id
        self.tag_name = tag_name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.snapshot_id is not None:
            result['snapshotId'] = self.snapshot_id
        if self.tag_name is not None:
            result['tagName'] = self.tag_name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('snapshotId') is not None:
            self.snapshot_id = m.get('snapshotId')
        if m.get('tagName') is not None:
            self.tag_name = m.get('tagName')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class Move(TeaModel):
    def __init__(
        self,
        field_name: str = None,
        reference_field_name: str = None,
        type: str = None,
    ):
        self.field_name = field_name
        self.reference_field_name = reference_field_name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_name is not None:
            result['fieldName'] = self.field_name
        if self.reference_field_name is not None:
            result['referenceFieldName'] = self.reference_field_name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fieldName') is not None:
            self.field_name = m.get('fieldName')
        if m.get('referenceFieldName') is not None:
            self.reference_field_name = m.get('referenceFieldName')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class FullSchemaChange(TeaModel):
    def __init__(
        self,
        action: str = None,
        comment: str = None,
        data_type: FullDataType = None,
        field_names: List[str] = None,
        keep_nullability: bool = None,
        key: str = None,
        move: Move = None,
        new_comment: str = None,
        new_data_type: FullDataType = None,
        new_name: str = None,
        new_nullability: bool = None,
        value: str = None,
    ):
        self.action = action
        # required in UpdateComment/AddColumn
        self.comment = comment
        self.data_type = data_type
        # required in AddColumn/RenameColumn/DropColumn/UpdateColumnComment/UpdateColumnType/UpdateColumnNullability
        self.field_names = field_names
        # required in UpdateColumnType
        self.keep_nullability = keep_nullability
        # required in SetOption/RemoveOption
        self.key = key
        self.move = move
        # required in UpdateColumnComment
        self.new_comment = new_comment
        self.new_data_type = new_data_type
        # required in RenameColumn
        self.new_name = new_name
        # required in UpdateColumnNullability
        self.new_nullability = new_nullability
        # required in SetOption
        self.value = value

    def validate(self):
        if self.data_type:
            self.data_type.validate()
        if self.move:
            self.move.validate()
        if self.new_data_type:
            self.new_data_type.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['action'] = self.action
        if self.comment is not None:
            result['comment'] = self.comment
        if self.data_type is not None:
            result['dataType'] = self.data_type.to_map()
        if self.field_names is not None:
            result['fieldNames'] = self.field_names
        if self.keep_nullability is not None:
            result['keepNullability'] = self.keep_nullability
        if self.key is not None:
            result['key'] = self.key
        if self.move is not None:
            result['move'] = self.move.to_map()
        if self.new_comment is not None:
            result['newComment'] = self.new_comment
        if self.new_data_type is not None:
            result['newDataType'] = self.new_data_type.to_map()
        if self.new_name is not None:
            result['newName'] = self.new_name
        if self.new_nullability is not None:
            result['newNullability'] = self.new_nullability
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('dataType') is not None:
            temp_model = FullDataType()
            self.data_type = temp_model.from_map(m['dataType'])
        if m.get('fieldNames') is not None:
            self.field_names = m.get('fieldNames')
        if m.get('keepNullability') is not None:
            self.keep_nullability = m.get('keepNullability')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('move') is not None:
            temp_model = Move()
            self.move = temp_model.from_map(m['move'])
        if m.get('newComment') is not None:
            self.new_comment = m.get('newComment')
        if m.get('newDataType') is not None:
            temp_model = FullDataType()
            self.new_data_type = temp_model.from_map(m['newDataType'])
        if m.get('newName') is not None:
            self.new_name = m.get('newName')
        if m.get('newNullability') is not None:
            self.new_nullability = m.get('newNullability')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class IcebergNestedField(TeaModel):
    def __init__(
        self,
        doc: str = None,
        id: int = None,
        name: str = None,
        optional: bool = None,
        type: str = None,
    ):
        self.doc = doc
        self.id = id
        self.name = name
        self.optional = optional
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc is not None:
            result['doc'] = self.doc
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.optional is not None:
            result['optional'] = self.optional
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('doc') is not None:
            self.doc = m.get('doc')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('optional') is not None:
            self.optional = m.get('optional')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class IcebergPartitionField(TeaModel):
    def __init__(
        self,
        field_id: int = None,
        name: str = None,
        source_id: int = None,
        transform: str = None,
    ):
        self.field_id = field_id
        self.name = name
        self.source_id = source_id
        self.transform = transform

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_id is not None:
            result['fieldId'] = self.field_id
        if self.name is not None:
            result['name'] = self.name
        if self.source_id is not None:
            result['sourceId'] = self.source_id
        if self.transform is not None:
            result['transform'] = self.transform
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fieldId') is not None:
            self.field_id = m.get('fieldId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')
        if m.get('transform') is not None:
            self.transform = m.get('transform')
        return self


class IcebergSnapshot(TeaModel):
    def __init__(
        self,
        added_rows: int = None,
        id: int = None,
        operation: str = None,
        parent_id: int = None,
        schema_id: int = None,
        sequence_number: int = None,
        summary: Dict[str, str] = None,
        timestamp_millis: int = None,
    ):
        self.added_rows = added_rows
        self.id = id
        self.operation = operation
        self.parent_id = parent_id
        self.schema_id = schema_id
        self.sequence_number = sequence_number
        self.summary = summary
        self.timestamp_millis = timestamp_millis

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.added_rows is not None:
            result['addedRows'] = self.added_rows
        if self.id is not None:
            result['id'] = self.id
        if self.operation is not None:
            result['operation'] = self.operation
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.schema_id is not None:
            result['schemaId'] = self.schema_id
        if self.sequence_number is not None:
            result['sequenceNumber'] = self.sequence_number
        if self.summary is not None:
            result['summary'] = self.summary
        if self.timestamp_millis is not None:
            result['timestampMillis'] = self.timestamp_millis
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('addedRows') is not None:
            self.added_rows = m.get('addedRows')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('operation') is not None:
            self.operation = m.get('operation')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('schemaId') is not None:
            self.schema_id = m.get('schemaId')
        if m.get('sequenceNumber') is not None:
            self.sequence_number = m.get('sequenceNumber')
        if m.get('summary') is not None:
            self.summary = m.get('summary')
        if m.get('timestampMillis') is not None:
            self.timestamp_millis = m.get('timestampMillis')
        return self


class IcebergTableMetadata(TeaModel):
    def __init__(
        self,
        current_snapshot: IcebergSnapshot = None,
        fields: List[IcebergNestedField] = None,
        partition_fields: List[IcebergPartitionField] = None,
        properties: Dict[str, str] = None,
    ):
        self.current_snapshot = current_snapshot
        self.fields = fields
        self.partition_fields = partition_fields
        self.properties = properties

    def validate(self):
        if self.current_snapshot:
            self.current_snapshot.validate()
        if self.fields:
            for k in self.fields:
                if k:
                    k.validate()
        if self.partition_fields:
            for k in self.partition_fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_snapshot is not None:
            result['currentSnapshot'] = self.current_snapshot.to_map()
        result['fields'] = []
        if self.fields is not None:
            for k in self.fields:
                result['fields'].append(k.to_map() if k else None)
        result['partitionFields'] = []
        if self.partition_fields is not None:
            for k in self.partition_fields:
                result['partitionFields'].append(k.to_map() if k else None)
        if self.properties is not None:
            result['properties'] = self.properties
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentSnapshot') is not None:
            temp_model = IcebergSnapshot()
            self.current_snapshot = temp_model.from_map(m['currentSnapshot'])
        self.fields = []
        if m.get('fields') is not None:
            for k in m.get('fields'):
                temp_model = IcebergNestedField()
                self.fields.append(temp_model.from_map(k))
        self.partition_fields = []
        if m.get('partitionFields') is not None:
            for k in m.get('partitionFields'):
                temp_model = IcebergPartitionField()
                self.partition_fields.append(temp_model.from_map(k))
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        return self


class IcebergTable(TeaModel):
    def __init__(
        self,
        created_at: int = None,
        created_by: str = None,
        iceberg_table_metadata: IcebergTableMetadata = None,
        id: str = None,
        name: str = None,
        owner: str = None,
        path: str = None,
        updated_at: int = None,
        updated_by: str = None,
        version: int = None,
    ):
        self.created_at = created_at
        self.created_by = created_by
        self.iceberg_table_metadata = iceberg_table_metadata
        self.id = id
        self.name = name
        self.owner = owner
        self.path = path
        self.updated_at = updated_at
        self.updated_by = updated_by
        self.version = version

    def validate(self):
        if self.iceberg_table_metadata:
            self.iceberg_table_metadata.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.created_by is not None:
            result['createdBy'] = self.created_by
        if self.iceberg_table_metadata is not None:
            result['icebergTableMetadata'] = self.iceberg_table_metadata.to_map()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.owner is not None:
            result['owner'] = self.owner
        if self.path is not None:
            result['path'] = self.path
        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at
        if self.updated_by is not None:
            result['updatedBy'] = self.updated_by
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('createdBy') is not None:
            self.created_by = m.get('createdBy')
        if m.get('icebergTableMetadata') is not None:
            temp_model = IcebergTableMetadata()
            self.iceberg_table_metadata = temp_model.from_map(m['icebergTableMetadata'])
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')
        if m.get('updatedBy') is not None:
            self.updated_by = m.get('updatedBy')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class Identifier(TeaModel):
    def __init__(
        self,
        database: str = None,
        object: str = None,
    ):
        self.database = database
        self.object = object

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database is not None:
            result['database'] = self.database
        if self.object is not None:
            result['object'] = self.object
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('database') is not None:
            self.database = m.get('database')
        if m.get('object') is not None:
            self.object = m.get('object')
        return self


class Namespace(TeaModel):
    def __init__(
        self,
        created_at: int = None,
        created_by: str = None,
        id: str = None,
        location: str = None,
        name: str = None,
        options: Dict[str, str] = None,
        owner: str = None,
        updated_at: int = None,
        updated_by: str = None,
    ):
        self.created_at = created_at
        self.created_by = created_by
        self.id = id
        self.location = location
        self.name = name
        self.options = options
        self.owner = owner
        self.updated_at = updated_at
        self.updated_by = updated_by

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.created_by is not None:
            result['createdBy'] = self.created_by
        if self.id is not None:
            result['id'] = self.id
        if self.location is not None:
            result['location'] = self.location
        if self.name is not None:
            result['name'] = self.name
        if self.options is not None:
            result['options'] = self.options
        if self.owner is not None:
            result['owner'] = self.owner
        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at
        if self.updated_by is not None:
            result['updatedBy'] = self.updated_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('createdBy') is not None:
            self.created_by = m.get('createdBy')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('options') is not None:
            self.options = m.get('options')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')
        if m.get('updatedBy') is not None:
            self.updated_by = m.get('updatedBy')
        return self


class Partition(TeaModel):
    def __init__(
        self,
        created_at: int = None,
        created_by: str = None,
        done: bool = None,
        file_count: int = None,
        file_size_in_bytes: int = None,
        last_file_creation_time: int = None,
        record_count: int = None,
        spec: Dict[str, Any] = None,
        updated_at: int = None,
        updated_by: str = None,
    ):
        self.created_at = created_at
        self.created_by = created_by
        self.done = done
        self.file_count = file_count
        self.file_size_in_bytes = file_size_in_bytes
        self.last_file_creation_time = last_file_creation_time
        self.record_count = record_count
        self.spec = spec
        self.updated_at = updated_at
        self.updated_by = updated_by

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.created_by is not None:
            result['createdBy'] = self.created_by
        if self.done is not None:
            result['done'] = self.done
        if self.file_count is not None:
            result['fileCount'] = self.file_count
        if self.file_size_in_bytes is not None:
            result['fileSizeInBytes'] = self.file_size_in_bytes
        if self.last_file_creation_time is not None:
            result['lastFileCreationTime'] = self.last_file_creation_time
        if self.record_count is not None:
            result['recordCount'] = self.record_count
        if self.spec is not None:
            result['spec'] = self.spec
        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at
        if self.updated_by is not None:
            result['updatedBy'] = self.updated_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('createdBy') is not None:
            self.created_by = m.get('createdBy')
        if m.get('done') is not None:
            self.done = m.get('done')
        if m.get('fileCount') is not None:
            self.file_count = m.get('fileCount')
        if m.get('fileSizeInBytes') is not None:
            self.file_size_in_bytes = m.get('fileSizeInBytes')
        if m.get('lastFileCreationTime') is not None:
            self.last_file_creation_time = m.get('lastFileCreationTime')
        if m.get('recordCount') is not None:
            self.record_count = m.get('recordCount')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')
        if m.get('updatedBy') is not None:
            self.updated_by = m.get('updatedBy')
        return self


class PartitionSummary(TeaModel):
    def __init__(
        self,
        created_at: int = None,
        database_name: str = None,
        last_access_time: int = None,
        partition_name: str = None,
        table_name: str = None,
        total_file_count: int = None,
        total_file_size_in_bytes: int = None,
        updated_at: int = None,
    ):
        # Partition creation timestamp in milliseconds
        self.created_at = created_at
        # Database name
        self.database_name = database_name
        # Total files in partition
        self.last_access_time = last_access_time
        # Partition identifier
        self.partition_name = partition_name
        # Table name
        self.table_name = table_name
        # 24h access count
        self.total_file_count = total_file_count
        # Last data access timestamp in milliseconds
        self.total_file_size_in_bytes = total_file_size_in_bytes
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.database_name is not None:
            result['databaseName'] = self.database_name
        if self.last_access_time is not None:
            result['lastAccessTime'] = self.last_access_time
        if self.partition_name is not None:
            result['partitionName'] = self.partition_name
        if self.table_name is not None:
            result['tableName'] = self.table_name
        if self.total_file_count is not None:
            result['totalFileCount'] = self.total_file_count
        if self.total_file_size_in_bytes is not None:
            result['totalFileSizeInBytes'] = self.total_file_size_in_bytes
        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('databaseName') is not None:
            self.database_name = m.get('databaseName')
        if m.get('lastAccessTime') is not None:
            self.last_access_time = m.get('lastAccessTime')
        if m.get('partitionName') is not None:
            self.partition_name = m.get('partitionName')
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        if m.get('totalFileCount') is not None:
            self.total_file_count = m.get('totalFileCount')
        if m.get('totalFileSizeInBytes') is not None:
            self.total_file_size_in_bytes = m.get('totalFileSizeInBytes')
        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')
        return self


class PartitionSummaries(TeaModel):
    def __init__(
        self,
        next_page_token: str = None,
        partitions: List[PartitionSummary] = None,
    ):
        self.next_page_token = next_page_token
        # Current page of partition profiles
        self.partitions = partitions

    def validate(self):
        if self.partitions:
            for k in self.partitions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_page_token is not None:
            result['nextPageToken'] = self.next_page_token
        result['partitions'] = []
        if self.partitions is not None:
            for k in self.partitions:
                result['partitions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nextPageToken') is not None:
            self.next_page_token = m.get('nextPageToken')
        self.partitions = []
        if m.get('partitions') is not None:
            for k in m.get('partitions'):
                temp_model = PartitionSummary()
                self.partitions.append(temp_model.from_map(k))
        return self


class User(TeaModel):
    def __init__(
        self,
        created_at: int = None,
        created_by: str = None,
        display_name: str = None,
        type: str = None,
        updated_at: int = None,
        updated_by: str = None,
        user_id: str = None,
        user_name: str = None,
        user_principal: str = None,
    ):
        self.created_at = created_at
        self.created_by = created_by
        self.display_name = display_name
        self.type = type
        self.updated_at = updated_at
        self.updated_by = updated_by
        self.user_id = user_id
        self.user_name = user_name
        self.user_principal = user_principal

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.created_by is not None:
            result['createdBy'] = self.created_by
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.type is not None:
            result['type'] = self.type
        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at
        if self.updated_by is not None:
            result['updatedBy'] = self.updated_by
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.user_name is not None:
            result['userName'] = self.user_name
        if self.user_principal is not None:
            result['userPrincipal'] = self.user_principal
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('createdBy') is not None:
            self.created_by = m.get('createdBy')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')
        if m.get('updatedBy') is not None:
            self.updated_by = m.get('updatedBy')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        if m.get('userPrincipal') is not None:
            self.user_principal = m.get('userPrincipal')
        return self


class Role(TeaModel):
    def __init__(
        self,
        created_at: int = None,
        created_by: str = None,
        description: str = None,
        display_name: str = None,
        is_predefined: str = None,
        role_name: str = None,
        role_principal: str = None,
        updated_at: int = None,
        updated_by: str = None,
        users: List[User] = None,
    ):
        self.created_at = created_at
        self.created_by = created_by
        self.description = description
        self.display_name = display_name
        self.is_predefined = is_predefined
        self.role_name = role_name
        self.role_principal = role_principal
        self.updated_at = updated_at
        self.updated_by = updated_by
        self.users = users

    def validate(self):
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.created_by is not None:
            result['createdBy'] = self.created_by
        if self.description is not None:
            result['description'] = self.description
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.is_predefined is not None:
            result['isPredefined'] = self.is_predefined
        if self.role_name is not None:
            result['roleName'] = self.role_name
        if self.role_principal is not None:
            result['rolePrincipal'] = self.role_principal
        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at
        if self.updated_by is not None:
            result['updatedBy'] = self.updated_by
        result['users'] = []
        if self.users is not None:
            for k in self.users:
                result['users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('createdBy') is not None:
            self.created_by = m.get('createdBy')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('isPredefined') is not None:
            self.is_predefined = m.get('isPredefined')
        if m.get('roleName') is not None:
            self.role_name = m.get('roleName')
        if m.get('rolePrincipal') is not None:
            self.role_principal = m.get('rolePrincipal')
        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')
        if m.get('updatedBy') is not None:
            self.updated_by = m.get('updatedBy')
        self.users = []
        if m.get('users') is not None:
            for k in m.get('users'):
                temp_model = User()
                self.users.append(temp_model.from_map(k))
        return self


class Schema(TeaModel):
    def __init__(
        self,
        comment: str = None,
        fields: List[DataField] = None,
        options: Dict[str, str] = None,
        partition_keys: List[str] = None,
        primary_keys: List[str] = None,
    ):
        self.comment = comment
        self.fields = fields
        self.options = options
        self.partition_keys = partition_keys
        self.primary_keys = primary_keys

    def validate(self):
        if self.fields:
            for k in self.fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['comment'] = self.comment
        result['fields'] = []
        if self.fields is not None:
            for k in self.fields:
                result['fields'].append(k.to_map() if k else None)
        if self.options is not None:
            result['options'] = self.options
        if self.partition_keys is not None:
            result['partitionKeys'] = self.partition_keys
        if self.primary_keys is not None:
            result['primaryKeys'] = self.primary_keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        self.fields = []
        if m.get('fields') is not None:
            for k in m.get('fields'):
                temp_model = DataField()
                self.fields.append(temp_model.from_map(k))
        if m.get('options') is not None:
            self.options = m.get('options')
        if m.get('partitionKeys') is not None:
            self.partition_keys = m.get('partitionKeys')
        if m.get('primaryKeys') is not None:
            self.primary_keys = m.get('primaryKeys')
        return self


class Snapshot(TeaModel):
    def __init__(
        self,
        base_manifest_list: str = None,
        changelog_manifest_list: str = None,
        changelog_record_count: int = None,
        commit_identifier: int = None,
        commit_kind: str = None,
        commit_user: str = None,
        delta_manifest_list: str = None,
        delta_record_count: int = None,
        id: int = None,
        index_manifest: str = None,
        log_offsets: Dict[str, int] = None,
        schema_id: int = None,
        statistics: str = None,
        time_millis: int = None,
        total_record_count: int = None,
        version: int = None,
        watermark: int = None,
    ):
        self.base_manifest_list = base_manifest_list
        self.changelog_manifest_list = changelog_manifest_list
        self.changelog_record_count = changelog_record_count
        self.commit_identifier = commit_identifier
        self.commit_kind = commit_kind
        self.commit_user = commit_user
        self.delta_manifest_list = delta_manifest_list
        self.delta_record_count = delta_record_count
        self.id = id
        self.index_manifest = index_manifest
        self.log_offsets = log_offsets
        self.schema_id = schema_id
        self.statistics = statistics
        self.time_millis = time_millis
        self.total_record_count = total_record_count
        self.version = version
        self.watermark = watermark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_manifest_list is not None:
            result['baseManifestList'] = self.base_manifest_list
        if self.changelog_manifest_list is not None:
            result['changelogManifestList'] = self.changelog_manifest_list
        if self.changelog_record_count is not None:
            result['changelogRecordCount'] = self.changelog_record_count
        if self.commit_identifier is not None:
            result['commitIdentifier'] = self.commit_identifier
        if self.commit_kind is not None:
            result['commitKind'] = self.commit_kind
        if self.commit_user is not None:
            result['commitUser'] = self.commit_user
        if self.delta_manifest_list is not None:
            result['deltaManifestList'] = self.delta_manifest_list
        if self.delta_record_count is not None:
            result['deltaRecordCount'] = self.delta_record_count
        if self.id is not None:
            result['id'] = self.id
        if self.index_manifest is not None:
            result['indexManifest'] = self.index_manifest
        if self.log_offsets is not None:
            result['logOffsets'] = self.log_offsets
        if self.schema_id is not None:
            result['schemaId'] = self.schema_id
        if self.statistics is not None:
            result['statistics'] = self.statistics
        if self.time_millis is not None:
            result['timeMillis'] = self.time_millis
        if self.total_record_count is not None:
            result['totalRecordCount'] = self.total_record_count
        if self.version is not None:
            result['version'] = self.version
        if self.watermark is not None:
            result['watermark'] = self.watermark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('baseManifestList') is not None:
            self.base_manifest_list = m.get('baseManifestList')
        if m.get('changelogManifestList') is not None:
            self.changelog_manifest_list = m.get('changelogManifestList')
        if m.get('changelogRecordCount') is not None:
            self.changelog_record_count = m.get('changelogRecordCount')
        if m.get('commitIdentifier') is not None:
            self.commit_identifier = m.get('commitIdentifier')
        if m.get('commitKind') is not None:
            self.commit_kind = m.get('commitKind')
        if m.get('commitUser') is not None:
            self.commit_user = m.get('commitUser')
        if m.get('deltaManifestList') is not None:
            self.delta_manifest_list = m.get('deltaManifestList')
        if m.get('deltaRecordCount') is not None:
            self.delta_record_count = m.get('deltaRecordCount')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('indexManifest') is not None:
            self.index_manifest = m.get('indexManifest')
        if m.get('logOffsets') is not None:
            self.log_offsets = m.get('logOffsets')
        if m.get('schemaId') is not None:
            self.schema_id = m.get('schemaId')
        if m.get('statistics') is not None:
            self.statistics = m.get('statistics')
        if m.get('timeMillis') is not None:
            self.time_millis = m.get('timeMillis')
        if m.get('totalRecordCount') is not None:
            self.total_record_count = m.get('totalRecordCount')
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('watermark') is not None:
            self.watermark = m.get('watermark')
        return self


class Table(TeaModel):
    def __init__(
        self,
        created_at: int = None,
        created_by: str = None,
        id: str = None,
        is_external: bool = None,
        name: str = None,
        owner: str = None,
        path: str = None,
        schema: Schema = None,
        schema_id: int = None,
        updated_at: int = None,
        updated_by: str = None,
    ):
        self.created_at = created_at
        self.created_by = created_by
        self.id = id
        self.is_external = is_external
        self.name = name
        self.owner = owner
        self.path = path
        self.schema = schema
        self.schema_id = schema_id
        self.updated_at = updated_at
        self.updated_by = updated_by

    def validate(self):
        if self.schema:
            self.schema.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.created_by is not None:
            result['createdBy'] = self.created_by
        if self.id is not None:
            result['id'] = self.id
        if self.is_external is not None:
            result['isExternal'] = self.is_external
        if self.name is not None:
            result['name'] = self.name
        if self.owner is not None:
            result['owner'] = self.owner
        if self.path is not None:
            result['path'] = self.path
        if self.schema is not None:
            result['schema'] = self.schema.to_map()
        if self.schema_id is not None:
            result['schemaId'] = self.schema_id
        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at
        if self.updated_by is not None:
            result['updatedBy'] = self.updated_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('createdBy') is not None:
            self.created_by = m.get('createdBy')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('isExternal') is not None:
            self.is_external = m.get('isExternal')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('schema') is not None:
            temp_model = Schema()
            self.schema = temp_model.from_map(m['schema'])
        if m.get('schemaId') is not None:
            self.schema_id = m.get('schemaId')
        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')
        if m.get('updatedBy') is not None:
            self.updated_by = m.get('updatedBy')
        return self


class TableCompaction(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        cu_usage: float = None,
        last_compacted_file_time: int = None,
        max_level_0file_count: str = None,
        table_id: str = None,
    ):
        self.catalog_id = catalog_id
        self.cu_usage = cu_usage
        self.last_compacted_file_time = last_compacted_file_time
        self.max_level_0file_count = max_level_0file_count
        self.table_id = table_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['catalogId'] = self.catalog_id
        if self.cu_usage is not None:
            result['cuUsage'] = self.cu_usage
        if self.last_compacted_file_time is not None:
            result['lastCompactedFileTime'] = self.last_compacted_file_time
        if self.max_level_0file_count is not None:
            result['maxLevel0FileCount'] = self.max_level_0file_count
        if self.table_id is not None:
            result['tableId'] = self.table_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('catalogId') is not None:
            self.catalog_id = m.get('catalogId')
        if m.get('cuUsage') is not None:
            self.cu_usage = m.get('cuUsage')
        if m.get('lastCompactedFileTime') is not None:
            self.last_compacted_file_time = m.get('lastCompactedFileTime')
        if m.get('maxLevel0FileCount') is not None:
            self.max_level_0file_count = m.get('maxLevel0FileCount')
        if m.get('tableId') is not None:
            self.table_id = m.get('tableId')
        return self


class TableSnapshot(TeaModel):
    def __init__(
        self,
        file_count: int = None,
        file_size_in_bytes: int = None,
        last_file_creation_time: int = None,
        record_count: int = None,
        snapshot: Snapshot = None,
    ):
        self.file_count = file_count
        self.file_size_in_bytes = file_size_in_bytes
        self.last_file_creation_time = last_file_creation_time
        self.record_count = record_count
        self.snapshot = snapshot

    def validate(self):
        if self.snapshot:
            self.snapshot.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_count is not None:
            result['fileCount'] = self.file_count
        if self.file_size_in_bytes is not None:
            result['fileSizeInBytes'] = self.file_size_in_bytes
        if self.last_file_creation_time is not None:
            result['lastFileCreationTime'] = self.last_file_creation_time
        if self.record_count is not None:
            result['recordCount'] = self.record_count
        if self.snapshot is not None:
            result['snapshot'] = self.snapshot.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileCount') is not None:
            self.file_count = m.get('fileCount')
        if m.get('fileSizeInBytes') is not None:
            self.file_size_in_bytes = m.get('fileSizeInBytes')
        if m.get('lastFileCreationTime') is not None:
            self.last_file_creation_time = m.get('lastFileCreationTime')
        if m.get('recordCount') is not None:
            self.record_count = m.get('recordCount')
        if m.get('snapshot') is not None:
            temp_model = Snapshot()
            self.snapshot = temp_model.from_map(m['snapshot'])
        return self


class TableSummary(TeaModel):
    def __init__(
        self,
        created_at: int = None,
        database_name: str = None,
        generated_date: str = None,
        last_access_time: int = None,
        partition_count: int = None,
        path: str = None,
        table_name: str = None,
        total_file_count: int = None,
        total_file_size_in_bytes: int = None,
    ):
        # Latest snapshot storage size
        self.created_at = created_at
        # Database name
        self.database_name = database_name
        self.generated_date = generated_date
        self.last_access_time = last_access_time
        # Creation timestamp in milliseconds
        self.partition_count = partition_count
        self.path = path
        # Table name
        self.table_name = table_name
        # 30-day access count
        self.total_file_count = total_file_count
        self.total_file_size_in_bytes = total_file_size_in_bytes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.database_name is not None:
            result['databaseName'] = self.database_name
        if self.generated_date is not None:
            result['generatedDate'] = self.generated_date
        if self.last_access_time is not None:
            result['lastAccessTime'] = self.last_access_time
        if self.partition_count is not None:
            result['partitionCount'] = self.partition_count
        if self.path is not None:
            result['path'] = self.path
        if self.table_name is not None:
            result['tableName'] = self.table_name
        if self.total_file_count is not None:
            result['totalFileCount'] = self.total_file_count
        if self.total_file_size_in_bytes is not None:
            result['totalFileSizeInBytes'] = self.total_file_size_in_bytes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('databaseName') is not None:
            self.database_name = m.get('databaseName')
        if m.get('generatedDate') is not None:
            self.generated_date = m.get('generatedDate')
        if m.get('lastAccessTime') is not None:
            self.last_access_time = m.get('lastAccessTime')
        if m.get('partitionCount') is not None:
            self.partition_count = m.get('partitionCount')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        if m.get('totalFileCount') is not None:
            self.total_file_count = m.get('totalFileCount')
        if m.get('totalFileSizeInBytes') is not None:
            self.total_file_size_in_bytes = m.get('totalFileSizeInBytes')
        return self


class AlterCatalogRequest(TeaModel):
    def __init__(
        self,
        removals: List[str] = None,
        updates: Dict[str, str] = None,
    ):
        self.removals = removals
        self.updates = updates

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.removals is not None:
            result['removals'] = self.removals
        if self.updates is not None:
            result['updates'] = self.updates
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('removals') is not None:
            self.removals = m.get('removals')
        if m.get('updates') is not None:
            self.updates = m.get('updates')
        return self


class AlterCatalogResponseBody(TeaModel):
    def __init__(
        self,
        missing: List[str] = None,
        removed: List[str] = None,
        updated: List[str] = None,
    ):
        self.missing = missing
        self.removed = removed
        self.updated = updated

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.missing is not None:
            result['missing'] = self.missing
        if self.removed is not None:
            result['removed'] = self.removed
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('missing') is not None:
            self.missing = m.get('missing')
        if m.get('removed') is not None:
            self.removed = m.get('removed')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class AlterCatalogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AlterCatalogResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AlterCatalogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AlterDatabaseRequest(TeaModel):
    def __init__(
        self,
        removals: List[str] = None,
        updates: Dict[str, str] = None,
    ):
        self.removals = removals
        self.updates = updates

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.removals is not None:
            result['removals'] = self.removals
        if self.updates is not None:
            result['updates'] = self.updates
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('removals') is not None:
            self.removals = m.get('removals')
        if m.get('updates') is not None:
            self.updates = m.get('updates')
        return self


class AlterDatabaseResponseBody(TeaModel):
    def __init__(
        self,
        missing: List[str] = None,
        removed: List[str] = None,
        updated: List[str] = None,
    ):
        self.missing = missing
        self.removed = removed
        self.updated = updated

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.missing is not None:
            result['missing'] = self.missing
        if self.removed is not None:
            result['removed'] = self.removed
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('missing') is not None:
            self.missing = m.get('missing')
        if m.get('removed') is not None:
            self.removed = m.get('removed')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class AlterDatabaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AlterDatabaseResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AlterDatabaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AlterTableRequest(TeaModel):
    def __init__(
        self,
        changes: List[FullSchemaChange] = None,
    ):
        self.changes = changes

    def validate(self):
        if self.changes:
            for k in self.changes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['changes'] = []
        if self.changes is not None:
            for k in self.changes:
                result['changes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.changes = []
        if m.get('changes') is not None:
            for k in m.get('changes'):
                temp_model = FullSchemaChange()
                self.changes.append(temp_model.from_map(k))
        return self


class AlterTableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class BatchGrantPermissionsRequest(TeaModel):
    def __init__(
        self,
        permissions: List[Permission] = None,
    ):
        self.permissions = permissions

    def validate(self):
        if self.permissions:
            for k in self.permissions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['permissions'] = []
        if self.permissions is not None:
            for k in self.permissions:
                result['permissions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.permissions = []
        if m.get('permissions') is not None:
            for k in m.get('permissions'):
                temp_model = Permission()
                self.permissions.append(temp_model.from_map(k))
        return self


class BatchGrantPermissionsResponseBody(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        failure_permissions: List[FailurePermission] = None,
        success: bool = None,
    ):
        self.error_message = error_message
        self.failure_permissions = failure_permissions
        self.success = success

    def validate(self):
        if self.failure_permissions:
            for k in self.failure_permissions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        result['failurePermissions'] = []
        if self.failure_permissions is not None:
            for k in self.failure_permissions:
                result['failurePermissions'].append(k.to_map() if k else None)
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        self.failure_permissions = []
        if m.get('failurePermissions') is not None:
            for k in m.get('failurePermissions'):
                temp_model = FailurePermission()
                self.failure_permissions.append(temp_model.from_map(k))
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class BatchGrantPermissionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchGrantPermissionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchGrantPermissionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchRevokePermissionsRequest(TeaModel):
    def __init__(
        self,
        permissions: List[Permission] = None,
    ):
        self.permissions = permissions

    def validate(self):
        if self.permissions:
            for k in self.permissions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['permissions'] = []
        if self.permissions is not None:
            for k in self.permissions:
                result['permissions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.permissions = []
        if m.get('permissions') is not None:
            for k in m.get('permissions'):
                temp_model = Permission()
                self.permissions.append(temp_model.from_map(k))
        return self


class BatchRevokePermissionsResponseBody(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        failure_permissions: List[FailurePermission] = None,
        success: bool = None,
    ):
        self.error_message = error_message
        self.failure_permissions = failure_permissions
        self.success = success

    def validate(self):
        if self.failure_permissions:
            for k in self.failure_permissions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        result['failurePermissions'] = []
        if self.failure_permissions is not None:
            for k in self.failure_permissions:
                result['failurePermissions'].append(k.to_map() if k else None)
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        self.failure_permissions = []
        if m.get('failurePermissions') is not None:
            for k in m.get('failurePermissions'):
                temp_model = FailurePermission()
                self.failure_permissions.append(temp_model.from_map(k))
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class BatchRevokePermissionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchRevokePermissionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchRevokePermissionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCatalogRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        options: Dict[str, str] = None,
        type: str = None,
    ):
        self.name = name
        self.options = options
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.options is not None:
            result['options'] = self.options
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('options') is not None:
            self.options = m.get('options')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateCatalogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class CreateDatabaseRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        options: Dict[str, str] = None,
    ):
        self.name = name
        self.options = options

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.options is not None:
            result['options'] = self.options
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('options') is not None:
            self.options = m.get('options')
        return self


class CreateDatabaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class CreateRoleRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        display_name: str = None,
        role_name: str = None,
    ):
        self.description = description
        self.display_name = display_name
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.role_name is not None:
            result['roleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('roleName') is not None:
            self.role_name = m.get('roleName')
        return self


class CreateRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class CreateTableRequest(TeaModel):
    def __init__(
        self,
        identifier: Identifier = None,
        schema: Schema = None,
    ):
        self.identifier = identifier
        self.schema = schema

    def validate(self):
        if self.identifier:
            self.identifier.validate()
        if self.schema:
            self.schema.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identifier is not None:
            result['identifier'] = self.identifier.to_map()
        if self.schema is not None:
            result['schema'] = self.schema.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('identifier') is not None:
            temp_model = Identifier()
            self.identifier = temp_model.from_map(m['identifier'])
        if m.get('schema') is not None:
            temp_model = Schema()
            self.schema = temp_model.from_map(m['schema'])
        return self


class CreateTableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteRoleRequest(TeaModel):
    def __init__(
        self,
        role_principal: str = None,
    ):
        self.role_principal = role_principal

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_principal is not None:
            result['rolePrincipal'] = self.role_principal
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('rolePrincipal') is not None:
            self.role_principal = m.get('rolePrincipal')
        return self


class DeleteRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        show_name: str = None,
        type: str = None,
    ):
        # The region description
        self.description = description
        # The region name
        self.name = name
        # The region show name
        self.show_name = show_name
        # The region type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.show_name is not None:
            result['showName'] = self.show_name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('showName') is not None:
            self.show_name = m.get('showName')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        regions: List[DescribeRegionsResponseBodyRegions] = None,
    ):
        self.regions = regions

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['regions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.regions = []
        if m.get('regions') is not None:
            for k in m.get('regions'):
                temp_model = DescribeRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRegionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DropCatalogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DropDatabaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DropTableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class GetCatalogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Catalog = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Catalog()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCatalogSummaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CatalogSummary = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CatalogSummary()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCatalogSummaryTrendRequest(TeaModel):
    def __init__(
        self,
        end_date: str = None,
        start_date: str = None,
    ):
        # This parameter is required.
        self.end_date = end_date
        # This parameter is required.
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['endDate'] = self.end_date
        if self.start_date is not None:
            result['startDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')
        if m.get('startDate') is not None:
            self.start_date = m.get('startDate')
        return self


class GetCatalogSummaryTrendResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CatalogSummaryTrend = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CatalogSummaryTrend()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCatalogTokenResponseBody(TeaModel):
    def __init__(
        self,
        expires_at_millis: int = None,
        token: Dict[str, str] = None,
    ):
        self.expires_at_millis = expires_at_millis
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expires_at_millis is not None:
            result['expiresAtMillis'] = self.expires_at_millis
        if self.token is not None:
            result['token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expiresAtMillis') is not None:
            self.expires_at_millis = m.get('expiresAtMillis')
        if m.get('token') is not None:
            self.token = m.get('token')
        return self


class GetCatalogTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCatalogTokenResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetCatalogTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDatabaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Database = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Database()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDatabaseSummaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DatabaseSummary = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DatabaseSummary()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRegionStatusResponseBody(TeaModel):
    def __init__(
        self,
        service_role_exists: bool = None,
        status: str = None,
    ):
        self.service_role_exists = service_role_exists
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_role_exists is not None:
            result['serviceRoleExists'] = self.service_role_exists
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('serviceRoleExists') is not None:
            self.service_role_exists = m.get('serviceRoleExists')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetRegionStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRegionStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetRegionStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRoleRequest(TeaModel):
    def __init__(
        self,
        role_principal: str = None,
    ):
        self.role_principal = role_principal

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_principal is not None:
            result['rolePrincipal'] = self.role_principal
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('rolePrincipal') is not None:
            self.role_principal = m.get('rolePrincipal')
        return self


class GetRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Role = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Role()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Table = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Table()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTableSummaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TableSummary = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TableSummary()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserRequest(TeaModel):
    def __init__(
        self,
        user_principal: str = None,
    ):
        self.user_principal = user_principal

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_principal is not None:
            result['userPrincipal'] = self.user_principal
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('userPrincipal') is not None:
            self.user_principal = m.get('userPrincipal')
        return self


class GetUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: User = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = User()
            self.body = temp_model.from_map(m['body'])
        return self


class GrantRoleToUsersRequest(TeaModel):
    def __init__(
        self,
        role_principal: str = None,
        user_principals: List[str] = None,
    ):
        self.role_principal = role_principal
        self.user_principals = user_principals

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_principal is not None:
            result['rolePrincipal'] = self.role_principal
        if self.user_principals is not None:
            result['userPrincipals'] = self.user_principals
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('rolePrincipal') is not None:
            self.role_principal = m.get('rolePrincipal')
        if m.get('userPrincipals') is not None:
            self.user_principals = m.get('userPrincipals')
        return self


class GrantRoleToUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class ListCatalogsRequest(TeaModel):
    def __init__(
        self,
        catalog_name_pattern: str = None,
        max_results: int = None,
        page_token: str = None,
    ):
        self.catalog_name_pattern = catalog_name_pattern
        self.max_results = max_results
        self.page_token = page_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_name_pattern is not None:
            result['catalogNamePattern'] = self.catalog_name_pattern
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.page_token is not None:
            result['pageToken'] = self.page_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('catalogNamePattern') is not None:
            self.catalog_name_pattern = m.get('catalogNamePattern')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('pageToken') is not None:
            self.page_token = m.get('pageToken')
        return self


class ListCatalogsResponseBody(TeaModel):
    def __init__(
        self,
        catalogs: List[Catalog] = None,
        next_page_token: str = None,
    ):
        self.catalogs = catalogs
        self.next_page_token = next_page_token

    def validate(self):
        if self.catalogs:
            for k in self.catalogs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['catalogs'] = []
        if self.catalogs is not None:
            for k in self.catalogs:
                result['catalogs'].append(k.to_map() if k else None)
        if self.next_page_token is not None:
            result['nextPageToken'] = self.next_page_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.catalogs = []
        if m.get('catalogs') is not None:
            for k in m.get('catalogs'):
                temp_model = Catalog()
                self.catalogs.append(temp_model.from_map(k))
        if m.get('nextPageToken') is not None:
            self.next_page_token = m.get('nextPageToken')
        return self


class ListCatalogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCatalogsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListCatalogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDatabasesRequest(TeaModel):
    def __init__(
        self,
        database_name_pattern: str = None,
        max_results: int = None,
        page_token: str = None,
    ):
        self.database_name_pattern = database_name_pattern
        self.max_results = max_results
        self.page_token = page_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_name_pattern is not None:
            result['databaseNamePattern'] = self.database_name_pattern
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.page_token is not None:
            result['pageToken'] = self.page_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('databaseNamePattern') is not None:
            self.database_name_pattern = m.get('databaseNamePattern')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('pageToken') is not None:
            self.page_token = m.get('pageToken')
        return self


class ListDatabasesResponseBody(TeaModel):
    def __init__(
        self,
        databases: List[str] = None,
        next_page_token: str = None,
    ):
        self.databases = databases
        self.next_page_token = next_page_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.databases is not None:
            result['databases'] = self.databases
        if self.next_page_token is not None:
            result['nextPageToken'] = self.next_page_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('databases') is not None:
            self.databases = m.get('databases')
        if m.get('nextPageToken') is not None:
            self.next_page_token = m.get('nextPageToken')
        return self


class ListDatabasesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDatabasesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDatabasesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPartitionSummariesRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        page_token: str = None,
        partition_name_pattern: str = None,
    ):
        self.max_results = max_results
        self.page_token = page_token
        self.partition_name_pattern = partition_name_pattern

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.page_token is not None:
            result['pageToken'] = self.page_token
        if self.partition_name_pattern is not None:
            result['partitionNamePattern'] = self.partition_name_pattern
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('pageToken') is not None:
            self.page_token = m.get('pageToken')
        if m.get('partitionNamePattern') is not None:
            self.partition_name_pattern = m.get('partitionNamePattern')
        return self


class ListPartitionSummariesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PartitionSummaries = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PartitionSummaries()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPermissionsRequest(TeaModel):
    def __init__(
        self,
        database: str = None,
        function: str = None,
        max_results: int = None,
        page_token: str = None,
        principal: str = None,
        resource_type: str = None,
        table: str = None,
        view: str = None,
    ):
        self.database = database
        self.function = function
        self.max_results = max_results
        self.page_token = page_token
        self.principal = principal
        # This parameter is required.
        self.resource_type = resource_type
        self.table = table
        self.view = view

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database is not None:
            result['database'] = self.database
        if self.function is not None:
            result['function'] = self.function
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.page_token is not None:
            result['pageToken'] = self.page_token
        if self.principal is not None:
            result['principal'] = self.principal
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.table is not None:
            result['table'] = self.table
        if self.view is not None:
            result['view'] = self.view
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('database') is not None:
            self.database = m.get('database')
        if m.get('function') is not None:
            self.function = m.get('function')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('pageToken') is not None:
            self.page_token = m.get('pageToken')
        if m.get('principal') is not None:
            self.principal = m.get('principal')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('table') is not None:
            self.table = m.get('table')
        if m.get('view') is not None:
            self.view = m.get('view')
        return self


class ListPermissionsResponseBody(TeaModel):
    def __init__(
        self,
        next_page_token: str = None,
        permissions: List[Permission] = None,
    ):
        self.next_page_token = next_page_token
        self.permissions = permissions

    def validate(self):
        if self.permissions:
            for k in self.permissions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_page_token is not None:
            result['nextPageToken'] = self.next_page_token
        result['permissions'] = []
        if self.permissions is not None:
            for k in self.permissions:
                result['permissions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nextPageToken') is not None:
            self.next_page_token = m.get('nextPageToken')
        self.permissions = []
        if m.get('permissions') is not None:
            for k in m.get('permissions'):
                temp_model = Permission()
                self.permissions.append(temp_model.from_map(k))
        return self


class ListPermissionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPermissionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListPermissionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRoleUsersRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        page_token: str = None,
        role_principal: str = None,
    ):
        self.max_results = max_results
        self.page_token = page_token
        self.role_principal = role_principal

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.page_token is not None:
            result['pageToken'] = self.page_token
        if self.role_principal is not None:
            result['rolePrincipal'] = self.role_principal
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('pageToken') is not None:
            self.page_token = m.get('pageToken')
        if m.get('rolePrincipal') is not None:
            self.role_principal = m.get('rolePrincipal')
        return self


class ListRoleUsersResponseBody(TeaModel):
    def __init__(
        self,
        next_page_token: str = None,
        users: List[User] = None,
    ):
        self.next_page_token = next_page_token
        self.users = users

    def validate(self):
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_page_token is not None:
            result['nextPageToken'] = self.next_page_token
        result['users'] = []
        if self.users is not None:
            for k in self.users:
                result['users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nextPageToken') is not None:
            self.next_page_token = m.get('nextPageToken')
        self.users = []
        if m.get('users') is not None:
            for k in m.get('users'):
                temp_model = User()
                self.users.append(temp_model.from_map(k))
        return self


class ListRoleUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRoleUsersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListRoleUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRolesRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        page_token: str = None,
        role_name: str = None,
    ):
        self.max_results = max_results
        self.page_token = page_token
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.page_token is not None:
            result['pageToken'] = self.page_token
        if self.role_name is not None:
            result['roleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('pageToken') is not None:
            self.page_token = m.get('pageToken')
        if m.get('roleName') is not None:
            self.role_name = m.get('roleName')
        return self


class ListRolesResponseBody(TeaModel):
    def __init__(
        self,
        next_page_token: str = None,
        roles: List[Role] = None,
    ):
        self.next_page_token = next_page_token
        self.roles = roles

    def validate(self):
        if self.roles:
            for k in self.roles:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_page_token is not None:
            result['nextPageToken'] = self.next_page_token
        result['roles'] = []
        if self.roles is not None:
            for k in self.roles:
                result['roles'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nextPageToken') is not None:
            self.next_page_token = m.get('nextPageToken')
        self.roles = []
        if m.get('roles') is not None:
            for k in m.get('roles'):
                temp_model = Role()
                self.roles.append(temp_model.from_map(k))
        return self


class ListRolesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRolesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListRolesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTablesRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        page_token: str = None,
        table_name_pattern: str = None,
    ):
        self.max_results = max_results
        self.page_token = page_token
        self.table_name_pattern = table_name_pattern

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.page_token is not None:
            result['pageToken'] = self.page_token
        if self.table_name_pattern is not None:
            result['tableNamePattern'] = self.table_name_pattern
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('pageToken') is not None:
            self.page_token = m.get('pageToken')
        if m.get('tableNamePattern') is not None:
            self.table_name_pattern = m.get('tableNamePattern')
        return self


class ListTablesResponseBody(TeaModel):
    def __init__(
        self,
        next_page_token: str = None,
        tables: List[str] = None,
    ):
        self.next_page_token = next_page_token
        self.tables = tables

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_page_token is not None:
            result['nextPageToken'] = self.next_page_token
        if self.tables is not None:
            result['tables'] = self.tables
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nextPageToken') is not None:
            self.next_page_token = m.get('nextPageToken')
        if m.get('tables') is not None:
            self.tables = m.get('tables')
        return self


class ListTablesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTablesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTablesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserRolesRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        page_token: str = None,
        user_principal: str = None,
    ):
        self.max_results = max_results
        self.page_token = page_token
        self.user_principal = user_principal

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.page_token is not None:
            result['pageToken'] = self.page_token
        if self.user_principal is not None:
            result['userPrincipal'] = self.user_principal
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('pageToken') is not None:
            self.page_token = m.get('pageToken')
        if m.get('userPrincipal') is not None:
            self.user_principal = m.get('userPrincipal')
        return self


class ListUserRolesResponseBody(TeaModel):
    def __init__(
        self,
        next_page_token: str = None,
        roles: List[Role] = None,
    ):
        self.next_page_token = next_page_token
        self.roles = roles

    def validate(self):
        if self.roles:
            for k in self.roles:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_page_token is not None:
            result['nextPageToken'] = self.next_page_token
        result['roles'] = []
        if self.roles is not None:
            for k in self.roles:
                result['roles'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nextPageToken') is not None:
            self.next_page_token = m.get('nextPageToken')
        self.roles = []
        if m.get('roles') is not None:
            for k in m.get('roles'):
                temp_model = Role()
                self.roles.append(temp_model.from_map(k))
        return self


class ListUserRolesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUserRolesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListUserRolesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUsersRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        page_token: str = None,
        type: str = None,
        user_name: str = None,
    ):
        self.max_results = max_results
        self.page_token = page_token
        self.type = type
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.page_token is not None:
            result['pageToken'] = self.page_token
        if self.type is not None:
            result['type'] = self.type
        if self.user_name is not None:
            result['userName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('pageToken') is not None:
            self.page_token = m.get('pageToken')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        return self


class ListUsersResponseBody(TeaModel):
    def __init__(
        self,
        next_page_token: str = None,
        users: List[User] = None,
    ):
        self.next_page_token = next_page_token
        self.users = users

    def validate(self):
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_page_token is not None:
            result['nextPageToken'] = self.next_page_token
        result['users'] = []
        if self.users is not None:
            for k in self.users:
                result['users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nextPageToken') is not None:
            self.next_page_token = m.get('nextPageToken')
        self.users = []
        if m.get('users') is not None:
            for k in m.get('users'):
                temp_model = User()
                self.users.append(temp_model.from_map(k))
        return self


class ListUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUsersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RevokeRoleFromUsersRequest(TeaModel):
    def __init__(
        self,
        role_principal: str = None,
        user_principals: List[str] = None,
    ):
        self.role_principal = role_principal
        self.user_principals = user_principals

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_principal is not None:
            result['rolePrincipal'] = self.role_principal
        if self.user_principals is not None:
            result['userPrincipals'] = self.user_principals
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('rolePrincipal') is not None:
            self.role_principal = m.get('rolePrincipal')
        if m.get('userPrincipals') is not None:
            self.user_principals = m.get('userPrincipals')
        return self


class RevokeRoleFromUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class SubscribeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class UpdateRoleRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        display_name: str = None,
        role_principal: str = None,
    ):
        self.description = description
        self.display_name = display_name
        self.role_principal = role_principal

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.role_principal is not None:
            result['rolePrincipal'] = self.role_principal
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('rolePrincipal') is not None:
            self.role_principal = m.get('rolePrincipal')
        return self


class UpdateRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class UpdateRoleUsersRequest(TeaModel):
    def __init__(
        self,
        role_principal: str = None,
        user_principals: List[str] = None,
    ):
        self.role_principal = role_principal
        self.user_principals = user_principals

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_principal is not None:
            result['rolePrincipal'] = self.role_principal
        if self.user_principals is not None:
            result['userPrincipals'] = self.user_principals
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('rolePrincipal') is not None:
            self.role_principal = m.get('rolePrincipal')
        if m.get('userPrincipals') is not None:
            self.user_principals = m.get('userPrincipals')
        return self


class UpdateRoleUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


