# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class Principal(TeaModel):
    def __init__(
        self,
        principal_arn: str = None,
    ):
        self.principal_arn = principal_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.principal_arn is not None:
            result['PrincipalArn'] = self.principal_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrincipalArn') is not None:
            self.principal_arn = m.get('PrincipalArn')
        return self


class CatalogResource(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
    ):
        self.catalog_id = catalog_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        return self


class ColumnResource(TeaModel):
    def __init__(
        self,
        column_names: List[str] = None,
        database_name: str = None,
        table_name: str = None,
    ):
        self.column_names = column_names
        self.database_name = database_name
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.column_names is not None:
            result['ColumnNames'] = self.column_names
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnNames') is not None:
            self.column_names = m.get('ColumnNames')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DatabaseResource(TeaModel):
    def __init__(
        self,
        database_name: str = None,
        database_wildcard: str = None,
    ):
        self.database_name = database_name
        self.database_wildcard = database_wildcard

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.database_wildcard is not None:
            result['DatabaseWildcard'] = self.database_wildcard
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('DatabaseWildcard') is not None:
            self.database_wildcard = m.get('DatabaseWildcard')
        return self


class FunctionResource(TeaModel):
    def __init__(
        self,
        database_name: str = None,
        function_name: str = None,
    ):
        self.database_name = database_name
        self.function_name = function_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        return self


class TableResource(TeaModel):
    def __init__(
        self,
        database_name: str = None,
        table_name: str = None,
    ):
        self.database_name = database_name
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class MetaResource(TeaModel):
    def __init__(
        self,
        catalog_resource: CatalogResource = None,
        column_resource: ColumnResource = None,
        database_resource: DatabaseResource = None,
        function_resource: FunctionResource = None,
        resource_type: str = None,
        table_resource: TableResource = None,
    ):
        self.catalog_resource = catalog_resource
        self.column_resource = column_resource
        self.database_resource = database_resource
        self.function_resource = function_resource
        self.resource_type = resource_type
        self.table_resource = table_resource

    def validate(self):
        if self.catalog_resource:
            self.catalog_resource.validate()
        if self.column_resource:
            self.column_resource.validate()
        if self.database_resource:
            self.database_resource.validate()
        if self.function_resource:
            self.function_resource.validate()
        if self.table_resource:
            self.table_resource.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_resource is not None:
            result['CatalogResource'] = self.catalog_resource.to_map()
        if self.column_resource is not None:
            result['ColumnResource'] = self.column_resource.to_map()
        if self.database_resource is not None:
            result['DatabaseResource'] = self.database_resource.to_map()
        if self.function_resource is not None:
            result['FunctionResource'] = self.function_resource.to_map()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.table_resource is not None:
            result['TableResource'] = self.table_resource.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogResource') is not None:
            temp_model = CatalogResource()
            self.catalog_resource = temp_model.from_map(m['CatalogResource'])
        if m.get('ColumnResource') is not None:
            temp_model = ColumnResource()
            self.column_resource = temp_model.from_map(m['ColumnResource'])
        if m.get('DatabaseResource') is not None:
            temp_model = DatabaseResource()
            self.database_resource = temp_model.from_map(m['DatabaseResource'])
        if m.get('FunctionResource') is not None:
            temp_model = FunctionResource()
            self.function_resource = temp_model.from_map(m['FunctionResource'])
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TableResource') is not None:
            temp_model = TableResource()
            self.table_resource = temp_model.from_map(m['TableResource'])
        return self


class PrivilegeResource(TeaModel):
    def __init__(
        self,
        access: str = None,
        meta_resource: MetaResource = None,
    ):
        self.access = access
        self.meta_resource = meta_resource

    def validate(self):
        if self.meta_resource:
            self.meta_resource.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access is not None:
            result['Access'] = self.access
        if self.meta_resource is not None:
            result['MetaResource'] = self.meta_resource.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Access') is not None:
            self.access = m.get('Access')
        if m.get('MetaResource') is not None:
            temp_model = MetaResource()
            self.meta_resource = temp_model.from_map(m['MetaResource'])
        return self


class AccessRequest(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        principal: Principal = None,
        privilege_resources: List[PrivilegeResource] = None,
    ):
        self.catalog_id = catalog_id
        self.principal = principal
        self.privilege_resources = privilege_resources

    def validate(self):
        if self.principal:
            self.principal.validate()
        if self.privilege_resources:
            for k in self.privilege_resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.principal is not None:
            result['Principal'] = self.principal.to_map()
        result['PrivilegeResources'] = []
        if self.privilege_resources is not None:
            for k in self.privilege_resources:
                result['PrivilegeResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('Principal') is not None:
            temp_model = Principal()
            self.principal = temp_model.from_map(m['Principal'])
        self.privilege_resources = []
        if m.get('PrivilegeResources') is not None:
            for k in m.get('PrivilegeResources'):
                temp_model = PrivilegeResource()
                self.privilege_resources.append(temp_model.from_map(k))
        return self


class Catalog(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        create_time: int = None,
        created_by: str = None,
        description: str = None,
        location_uri: str = None,
        owner: str = None,
        status: str = None,
        update_time: int = None,
    ):
        self.catalog_id = catalog_id
        self.create_time = create_time
        self.created_by = created_by
        self.description = description
        self.location_uri = location_uri
        self.owner = owner
        self.status = status
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.description is not None:
            result['Description'] = self.description
        if self.location_uri is not None:
            result['LocationUri'] = self.location_uri
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('LocationUri') is not None:
            self.location_uri = m.get('LocationUri')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class CatalogInput(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        description: str = None,
        location_uri: str = None,
        owner: str = None,
    ):
        self.catalog_id = catalog_id
        self.description = description
        self.location_uri = location_uri
        self.owner = owner

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.description is not None:
            result['Description'] = self.description
        if self.location_uri is not None:
            result['LocationUri'] = self.location_uri
        if self.owner is not None:
            result['Owner'] = self.owner
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('LocationUri') is not None:
            self.location_uri = m.get('LocationUri')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        return self


class CatalogSettings(TeaModel):
    def __init__(
        self,
        config: Dict[str, str] = None,
    ):
        self.config = config

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        return self


class ColumnStatisticsDesc(TeaModel):
    def __init__(
        self,
        last_analyzed_time: int = None,
        partition_name: str = None,
    ):
        self.last_analyzed_time = last_analyzed_time
        self.partition_name = partition_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.last_analyzed_time is not None:
            result['LastAnalyzedTime'] = self.last_analyzed_time
        if self.partition_name is not None:
            result['PartitionName'] = self.partition_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LastAnalyzedTime') is not None:
            self.last_analyzed_time = m.get('LastAnalyzedTime')
        if m.get('PartitionName') is not None:
            self.partition_name = m.get('PartitionName')
        return self


class ColumnStatisticsObjColumnStatisticsData(TeaModel):
    def __init__(
        self,
        statistics_data: str = None,
        statistics_type: str = None,
    ):
        self.statistics_data = statistics_data
        self.statistics_type = statistics_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.statistics_data is not None:
            result['StatisticsData'] = self.statistics_data
        if self.statistics_type is not None:
            result['StatisticsType'] = self.statistics_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StatisticsData') is not None:
            self.statistics_data = m.get('StatisticsData')
        if m.get('StatisticsType') is not None:
            self.statistics_type = m.get('StatisticsType')
        return self


class ColumnStatisticsObj(TeaModel):
    def __init__(
        self,
        column_name: str = None,
        column_statistics_data: ColumnStatisticsObjColumnStatisticsData = None,
        column_type: str = None,
    ):
        self.column_name = column_name
        self.column_statistics_data = column_statistics_data
        self.column_type = column_type

    def validate(self):
        if self.column_statistics_data:
            self.column_statistics_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.column_name is not None:
            result['ColumnName'] = self.column_name
        if self.column_statistics_data is not None:
            result['ColumnStatisticsData'] = self.column_statistics_data.to_map()
        if self.column_type is not None:
            result['ColumnType'] = self.column_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')
        if m.get('ColumnStatisticsData') is not None:
            temp_model = ColumnStatisticsObjColumnStatisticsData()
            self.column_statistics_data = temp_model.from_map(m['ColumnStatisticsData'])
        if m.get('ColumnType') is not None:
            self.column_type = m.get('ColumnType')
        return self


class ColumnStatistics(TeaModel):
    def __init__(
        self,
        column_statistics_desc: ColumnStatisticsDesc = None,
        column_statistics_obj_list: List[ColumnStatisticsObj] = None,
        engine: str = None,
        is_stats_compliant: bool = None,
    ):
        self.column_statistics_desc = column_statistics_desc
        self.column_statistics_obj_list = column_statistics_obj_list
        self.engine = engine
        self.is_stats_compliant = is_stats_compliant

    def validate(self):
        if self.column_statistics_desc:
            self.column_statistics_desc.validate()
        if self.column_statistics_obj_list:
            for k in self.column_statistics_obj_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.column_statistics_desc is not None:
            result['ColumnStatisticsDesc'] = self.column_statistics_desc.to_map()
        result['ColumnStatisticsObjList'] = []
        if self.column_statistics_obj_list is not None:
            for k in self.column_statistics_obj_list:
                result['ColumnStatisticsObjList'].append(k.to_map() if k else None)
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.is_stats_compliant is not None:
            result['IsStatsCompliant'] = self.is_stats_compliant
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnStatisticsDesc') is not None:
            temp_model = ColumnStatisticsDesc()
            self.column_statistics_desc = temp_model.from_map(m['ColumnStatisticsDesc'])
        self.column_statistics_obj_list = []
        if m.get('ColumnStatisticsObjList') is not None:
            for k in m.get('ColumnStatisticsObjList'):
                temp_model = ColumnStatisticsObj()
                self.column_statistics_obj_list.append(temp_model.from_map(k))
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('IsStatsCompliant') is not None:
            self.is_stats_compliant = m.get('IsStatsCompliant')
        return self


class PrivilegeGrantInfo(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        grant_option: bool = None,
        grantor: str = None,
        grantor_type: str = None,
        privilege: str = None,
    ):
        self.create_time = create_time
        self.grant_option = grant_option
        self.grantor = grantor
        self.grantor_type = grantor_type
        self.privilege = privilege

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.grant_option is not None:
            result['GrantOption'] = self.grant_option
        if self.grantor is not None:
            result['Grantor'] = self.grantor
        if self.grantor_type is not None:
            result['GrantorType'] = self.grantor_type
        if self.privilege is not None:
            result['Privilege'] = self.privilege
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('GrantOption') is not None:
            self.grant_option = m.get('GrantOption')
        if m.get('Grantor') is not None:
            self.grantor = m.get('Grantor')
        if m.get('GrantorType') is not None:
            self.grantor_type = m.get('GrantorType')
        if m.get('Privilege') is not None:
            self.privilege = m.get('Privilege')
        return self


class PrincipalPrivilegeSet(TeaModel):
    def __init__(
        self,
        group_privileges: Dict[str, List[PrivilegeGrantInfo]] = None,
        role_privileges: Dict[str, List[PrivilegeGrantInfo]] = None,
        user_privileges: Dict[str, List[PrivilegeGrantInfo]] = None,
    ):
        self.group_privileges = group_privileges
        self.role_privileges = role_privileges
        self.user_privileges = user_privileges

    def validate(self):
        if self.group_privileges:
            for v in self.group_privileges.values():
                for k1 in v:
                    if k1:
                        k1.validate()
        if self.role_privileges:
            for v in self.role_privileges.values():
                for k1 in v:
                    if k1:
                        k1.validate()
        if self.user_privileges:
            for v in self.user_privileges.values():
                for k1 in v:
                    if k1:
                        k1.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['GroupPrivileges'] = {}
        if self.group_privileges is not None:
            for k, v in self.group_privileges.items():
                l1 = []
                for k1 in v:
                    l1.append(k1.to_map() if k1 else None)
                result['groupPrivileges'][k] = l1
        result['RolePrivileges'] = {}
        if self.role_privileges is not None:
            for k, v in self.role_privileges.items():
                l1 = []
                for k1 in v:
                    l1.append(k1.to_map() if k1 else None)
                result['rolePrivileges'][k] = l1
        result['UserPrivileges'] = {}
        if self.user_privileges is not None:
            for k, v in self.user_privileges.items():
                l1 = []
                for k1 in v:
                    l1.append(k1.to_map() if k1 else None)
                result['userPrivileges'][k] = l1
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.group_privileges = {}
        if m.get('GroupPrivileges') is not None:
            for k, v in m.get('GroupPrivileges').items():
                l1 = []
                for k1 in v:
                    temp_model = PrivilegeGrantInfo()
                    l1.append(temp_model.from_map(k1))
                self.group_privileges['k'] = l1
        self.role_privileges = {}
        if m.get('RolePrivileges') is not None:
            for k, v in m.get('RolePrivileges').items():
                l1 = []
                for k1 in v:
                    temp_model = PrivilegeGrantInfo()
                    l1.append(temp_model.from_map(k1))
                self.role_privileges['k'] = l1
        self.user_privileges = {}
        if m.get('UserPrivileges') is not None:
            for k, v in m.get('UserPrivileges').items():
                l1 = []
                for k1 in v:
                    temp_model = PrivilegeGrantInfo()
                    l1.append(temp_model.from_map(k1))
                self.user_privileges['k'] = l1
        return self


class Database(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        created_by: str = None,
        description: str = None,
        location_uri: str = None,
        name: str = None,
        owner_name: str = None,
        owner_type: str = None,
        parameters: Dict[str, str] = None,
        privileges: PrincipalPrivilegeSet = None,
        update_time: int = None,
    ):
        self.create_time = create_time
        self.created_by = created_by
        self.description = description
        self.location_uri = location_uri
        self.name = name
        self.owner_name = owner_name
        self.owner_type = owner_type
        self.parameters = parameters
        self.privileges = privileges
        self.update_time = update_time

    def validate(self):
        if self.privileges:
            self.privileges.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.description is not None:
            result['Description'] = self.description
        if self.location_uri is not None:
            result['LocationUri'] = self.location_uri
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.owner_type is not None:
            result['OwnerType'] = self.owner_type
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.privileges is not None:
            result['Privileges'] = self.privileges.to_map()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('LocationUri') is not None:
            self.location_uri = m.get('LocationUri')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('OwnerType') is not None:
            self.owner_type = m.get('OwnerType')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('Privileges') is not None:
            temp_model = PrincipalPrivilegeSet()
            self.privileges = temp_model.from_map(m['Privileges'])
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DatabaseInput(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        description: str = None,
        location_uri: str = None,
        name: str = None,
        owner_name: str = None,
        owner_type: str = None,
        parameters: Dict[str, str] = None,
        privileges: PrincipalPrivilegeSet = None,
    ):
        self.create_time = create_time
        self.description = description
        self.location_uri = location_uri
        self.name = name
        self.owner_name = owner_name
        self.owner_type = owner_type
        self.parameters = parameters
        self.privileges = privileges

    def validate(self):
        if self.privileges:
            self.privileges.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.location_uri is not None:
            result['LocationUri'] = self.location_uri
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.owner_type is not None:
            result['OwnerType'] = self.owner_type
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.privileges is not None:
            result['Privileges'] = self.privileges.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('LocationUri') is not None:
            self.location_uri = m.get('LocationUri')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('OwnerType') is not None:
            self.owner_type = m.get('OwnerType')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('Privileges') is not None:
            temp_model = PrincipalPrivilegeSet()
            self.privileges = temp_model.from_map(m['Privileges'])
        return self


class DatabaseProfile(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        file_cnt: int = None,
        file_size: int = None,
        location: str = None,
        name: str = None,
    ):
        self.create_time = create_time
        self.file_cnt = file_cnt
        self.file_size = file_size
        self.location = location
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.file_cnt is not None:
            result['FileCnt'] = self.file_cnt
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.location is not None:
            result['Location'] = self.location
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('FileCnt') is not None:
            self.file_cnt = m.get('FileCnt')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DbStorageRank(TeaModel):
    def __init__(
        self,
        db_name: str = None,
        quantity: int = None,
    ):
        self.db_name = db_name
        self.quantity = quantity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        return self


class ErrorDetail(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class FieldSchema(TeaModel):
    def __init__(
        self,
        comment: str = None,
        name: str = None,
        parameters: Dict[str, str] = None,
        type: str = None,
    ):
        self.comment = comment
        self.name = name
        self.parameters = parameters
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.name is not None:
            result['Name'] = self.name
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class FileCnt(TeaModel):
    def __init__(
        self,
        large: int = None,
        middle: int = None,
        small: int = None,
        tiny: int = None,
    ):
        self.large = large
        self.middle = middle
        self.small = small
        self.tiny = tiny

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.large is not None:
            result['Large'] = self.large
        if self.middle is not None:
            result['Middle'] = self.middle
        if self.small is not None:
            result['Small'] = self.small
        if self.tiny is not None:
            result['Tiny'] = self.tiny
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Large') is not None:
            self.large = m.get('Large')
        if m.get('Middle') is not None:
            self.middle = m.get('Middle')
        if m.get('Small') is not None:
            self.small = m.get('Small')
        if m.get('Tiny') is not None:
            self.tiny = m.get('Tiny')
        return self


class ResourceUri(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
        uri: str = None,
    ):
        self.resource_type = resource_type
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class Function(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        class_name: str = None,
        create_time: int = None,
        created_by: str = None,
        database_name: str = None,
        function_name: str = None,
        function_type: str = None,
        owner_name: str = None,
        owner_type: str = None,
        resource_uri: List[ResourceUri] = None,
        update_time: int = None,
    ):
        self.catalog_id = catalog_id
        self.class_name = class_name
        self.create_time = create_time
        self.created_by = created_by
        self.database_name = database_name
        self.function_name = function_name
        self.function_type = function_type
        self.owner_name = owner_name
        self.owner_type = owner_type
        self.resource_uri = resource_uri
        self.update_time = update_time

    def validate(self):
        if self.resource_uri:
            for k in self.resource_uri:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.class_name is not None:
            result['ClassName'] = self.class_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.function_type is not None:
            result['FunctionType'] = self.function_type
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.owner_type is not None:
            result['OwnerType'] = self.owner_type
        result['ResourceUri'] = []
        if self.resource_uri is not None:
            for k in self.resource_uri:
                result['ResourceUri'].append(k.to_map() if k else None)
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('ClassName') is not None:
            self.class_name = m.get('ClassName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('FunctionType') is not None:
            self.function_type = m.get('FunctionType')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('OwnerType') is not None:
            self.owner_type = m.get('OwnerType')
        self.resource_uri = []
        if m.get('ResourceUri') is not None:
            for k in m.get('ResourceUri'):
                temp_model = ResourceUri()
                self.resource_uri.append(temp_model.from_map(k))
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class FunctionInput(TeaModel):
    def __init__(
        self,
        class_name: str = None,
        create_time: int = None,
        function_name: str = None,
        function_type: str = None,
        owner_name: str = None,
        owner_type: str = None,
        resource_uri: List[ResourceUri] = None,
    ):
        self.class_name = class_name
        self.create_time = create_time
        self.function_name = function_name
        self.function_type = function_type
        self.owner_name = owner_name
        self.owner_type = owner_type
        self.resource_uri = resource_uri

    def validate(self):
        if self.resource_uri:
            for k in self.resource_uri:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_name is not None:
            result['ClassName'] = self.class_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.function_type is not None:
            result['FunctionType'] = self.function_type
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.owner_type is not None:
            result['OwnerType'] = self.owner_type
        result['ResourceUri'] = []
        if self.resource_uri is not None:
            for k in self.resource_uri:
                result['ResourceUri'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassName') is not None:
            self.class_name = m.get('ClassName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('FunctionType') is not None:
            self.function_type = m.get('FunctionType')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('OwnerType') is not None:
            self.owner_type = m.get('OwnerType')
        self.resource_uri = []
        if m.get('ResourceUri') is not None:
            for k in m.get('ResourceUri'):
                temp_model = ResourceUri()
                self.resource_uri.append(temp_model.from_map(k))
        return self


class GrantRevokeEntry(TeaModel):
    def __init__(
        self,
        accesses: List[str] = None,
        delegate_accesses: List[str] = None,
        id: str = None,
        meta_resource: MetaResource = None,
        principal: Principal = None,
    ):
        self.accesses = accesses
        self.delegate_accesses = delegate_accesses
        self.id = id
        self.meta_resource = meta_resource
        self.principal = principal

    def validate(self):
        if self.meta_resource:
            self.meta_resource.validate()
        if self.principal:
            self.principal.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accesses is not None:
            result['Accesses'] = self.accesses
        if self.delegate_accesses is not None:
            result['DelegateAccesses'] = self.delegate_accesses
        if self.id is not None:
            result['Id'] = self.id
        if self.meta_resource is not None:
            result['MetaResource'] = self.meta_resource.to_map()
        if self.principal is not None:
            result['Principal'] = self.principal.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accesses') is not None:
            self.accesses = m.get('Accesses')
        if m.get('DelegateAccesses') is not None:
            self.delegate_accesses = m.get('DelegateAccesses')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MetaResource') is not None:
            temp_model = MetaResource()
            self.meta_resource = temp_model.from_map(m['MetaResource'])
        if m.get('Principal') is not None:
            temp_model = Principal()
            self.principal = temp_model.from_map(m['Principal'])
        return self


class GrantRevokeFailureEntry(TeaModel):
    def __init__(
        self,
        error_detail: ErrorDetail = None,
        grant_revoke_entry: GrantRevokeEntry = None,
    ):
        self.error_detail = error_detail
        self.grant_revoke_entry = grant_revoke_entry

    def validate(self):
        if self.error_detail:
            self.error_detail.validate()
        if self.grant_revoke_entry:
            self.grant_revoke_entry.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_detail is not None:
            result['ErrorDetail'] = self.error_detail.to_map()
        if self.grant_revoke_entry is not None:
            result['GrantRevokeEntry'] = self.grant_revoke_entry.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorDetail') is not None:
            temp_model = ErrorDetail()
            self.error_detail = temp_model.from_map(m['ErrorDetail'])
        if m.get('GrantRevokeEntry') is not None:
            temp_model = GrantRevokeEntry()
            self.grant_revoke_entry = temp_model.from_map(m['GrantRevokeEntry'])
        return self


class HighLight(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class IndicatorStatistic(TeaModel):
    def __init__(
        self,
        data: int = None,
        date: str = None,
    ):
        self.data = data
        self.date = date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.date is not None:
            result['Date'] = self.date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Date') is not None:
            self.date = m.get('Date')
        return self


class LifecycleResourceDatabase(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        description: str = None,
        location_uri: str = None,
        name: str = None,
        update_time: int = None,
    ):
        self.create_time = create_time
        self.description = description
        self.location_uri = location_uri
        self.name = name
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.location_uri is not None:
            result['LocationUri'] = self.location_uri
        if self.name is not None:
            result['Name'] = self.name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('LocationUri') is not None:
            self.location_uri = m.get('LocationUri')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class LifecycleResourceTableSdSerDeInfo(TeaModel):
    def __init__(
        self,
        name: str = None,
        parameters: Dict[str, str] = None,
        serialization_lib: str = None,
    ):
        self.name = name
        self.parameters = parameters
        self.serialization_lib = serialization_lib

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.serialization_lib is not None:
            result['SerializationLib'] = self.serialization_lib
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('SerializationLib') is not None:
            self.serialization_lib = m.get('SerializationLib')
        return self


class LifecycleResourceTableSd(TeaModel):
    def __init__(
        self,
        bucket_cols: List[str] = None,
        input_format: str = None,
        location: str = None,
        output_format: str = None,
        parameters: Dict[str, str] = None,
        ser_de_info: LifecycleResourceTableSdSerDeInfo = None,
    ):
        self.bucket_cols = bucket_cols
        self.input_format = input_format
        self.location = location
        self.output_format = output_format
        self.parameters = parameters
        self.ser_de_info = ser_de_info

    def validate(self):
        if self.ser_de_info:
            self.ser_de_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_cols is not None:
            result['BucketCols'] = self.bucket_cols
        if self.input_format is not None:
            result['InputFormat'] = self.input_format
        if self.location is not None:
            result['Location'] = self.location
        if self.output_format is not None:
            result['OutputFormat'] = self.output_format
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.ser_de_info is not None:
            result['SerDeInfo'] = self.ser_de_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketCols') is not None:
            self.bucket_cols = m.get('BucketCols')
        if m.get('InputFormat') is not None:
            self.input_format = m.get('InputFormat')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('OutputFormat') is not None:
            self.output_format = m.get('OutputFormat')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('SerDeInfo') is not None:
            temp_model = LifecycleResourceTableSdSerDeInfo()
            self.ser_de_info = temp_model.from_map(m['SerDeInfo'])
        return self


class LifecycleResourceTable(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        database_name: str = None,
        parameters: Dict[str, str] = None,
        sd: LifecycleResourceTableSd = None,
        table_name: str = None,
        table_type: str = None,
    ):
        self.create_time = create_time
        self.database_name = database_name
        self.parameters = parameters
        self.sd = sd
        self.table_name = table_name
        self.table_type = table_type

    def validate(self):
        if self.sd:
            self.sd.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.sd is not None:
            result['Sd'] = self.sd.to_map()
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.table_type is not None:
            result['TableType'] = self.table_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('Sd') is not None:
            temp_model = LifecycleResourceTableSd()
            self.sd = temp_model.from_map(m['Sd'])
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('TableType') is not None:
            self.table_type = m.get('TableType')
        return self


class TableProfile(TeaModel):
    def __init__(
        self,
        access_num: int = None,
        access_num_monthly: int = None,
        access_num_weekly: int = None,
        create_time: str = None,
        database_name: str = None,
        file_cnt: int = None,
        file_size: int = None,
        is_partitioned: bool = None,
        last_modify_time: str = None,
        location: str = None,
        partition_cnt: int = None,
        record_cnt: int = None,
        table_name: str = None,
    ):
        self.access_num = access_num
        self.access_num_monthly = access_num_monthly
        self.access_num_weekly = access_num_weekly
        self.create_time = create_time
        self.database_name = database_name
        self.file_cnt = file_cnt
        self.file_size = file_size
        self.is_partitioned = is_partitioned
        self.last_modify_time = last_modify_time
        self.location = location
        self.partition_cnt = partition_cnt
        self.record_cnt = record_cnt
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_num is not None:
            result['AccessNum'] = self.access_num
        if self.access_num_monthly is not None:
            result['AccessNumMonthly'] = self.access_num_monthly
        if self.access_num_weekly is not None:
            result['AccessNumWeekly'] = self.access_num_weekly
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.file_cnt is not None:
            result['FileCnt'] = self.file_cnt
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.is_partitioned is not None:
            result['IsPartitioned'] = self.is_partitioned
        if self.last_modify_time is not None:
            result['LastModifyTime'] = self.last_modify_time
        if self.location is not None:
            result['Location'] = self.location
        if self.partition_cnt is not None:
            result['PartitionCnt'] = self.partition_cnt
        if self.record_cnt is not None:
            result['RecordCnt'] = self.record_cnt
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessNum') is not None:
            self.access_num = m.get('AccessNum')
        if m.get('AccessNumMonthly') is not None:
            self.access_num_monthly = m.get('AccessNumMonthly')
        if m.get('AccessNumWeekly') is not None:
            self.access_num_weekly = m.get('AccessNumWeekly')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('FileCnt') is not None:
            self.file_cnt = m.get('FileCnt')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('IsPartitioned') is not None:
            self.is_partitioned = m.get('IsPartitioned')
        if m.get('LastModifyTime') is not None:
            self.last_modify_time = m.get('LastModifyTime')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('PartitionCnt') is not None:
            self.partition_cnt = m.get('PartitionCnt')
        if m.get('RecordCnt') is not None:
            self.record_cnt = m.get('RecordCnt')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class LifecycleResource(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        catalog_id: str = None,
        database: LifecycleResourceDatabase = None,
        database_name: str = None,
        database_profile: DatabaseProfile = None,
        gmt_create: str = None,
        lifecycle_rule_biz_id: str = None,
        owner: int = None,
        table: LifecycleResourceTable = None,
        table_name: str = None,
        table_profile: TableProfile = None,
    ):
        self.biz_id = biz_id
        self.catalog_id = catalog_id
        self.database = database
        self.database_name = database_name
        self.database_profile = database_profile
        self.gmt_create = gmt_create
        self.lifecycle_rule_biz_id = lifecycle_rule_biz_id
        self.owner = owner
        self.table = table
        self.table_name = table_name
        self.table_profile = table_profile

    def validate(self):
        if self.database:
            self.database.validate()
        if self.database_profile:
            self.database_profile.validate()
        if self.table:
            self.table.validate()
        if self.table_profile:
            self.table_profile.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.database is not None:
            result['Database'] = self.database.to_map()
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.database_profile is not None:
            result['DatabaseProfile'] = self.database_profile.to_map()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.lifecycle_rule_biz_id is not None:
            result['LifecycleRuleBizId'] = self.lifecycle_rule_biz_id
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.table is not None:
            result['Table'] = self.table.to_map()
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.table_profile is not None:
            result['TableProfile'] = self.table_profile.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('Database') is not None:
            temp_model = LifecycleResourceDatabase()
            self.database = temp_model.from_map(m['Database'])
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('DatabaseProfile') is not None:
            temp_model = DatabaseProfile()
            self.database_profile = temp_model.from_map(m['DatabaseProfile'])
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('LifecycleRuleBizId') is not None:
            self.lifecycle_rule_biz_id = m.get('LifecycleRuleBizId')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('Table') is not None:
            temp_model = LifecycleResourceTable()
            self.table = temp_model.from_map(m['Table'])
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('TableProfile') is not None:
            temp_model = TableProfile()
            self.table_profile = temp_model.from_map(m['TableProfile'])
        return self


class Workflow(TeaModel):
    def __init__(
        self,
        latest_end_time: str = None,
        latest_instance_id: str = None,
        latest_instance_status: str = None,
        latest_start_time: str = None,
    ):
        self.latest_end_time = latest_end_time
        self.latest_instance_id = latest_instance_id
        self.latest_instance_status = latest_instance_status
        self.latest_start_time = latest_start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.latest_end_time is not None:
            result['LatestEndTime'] = self.latest_end_time
        if self.latest_instance_id is not None:
            result['LatestInstanceId'] = self.latest_instance_id
        if self.latest_instance_status is not None:
            result['LatestInstanceStatus'] = self.latest_instance_status
        if self.latest_start_time is not None:
            result['LatestStartTime'] = self.latest_start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LatestEndTime') is not None:
            self.latest_end_time = m.get('LatestEndTime')
        if m.get('LatestInstanceId') is not None:
            self.latest_instance_id = m.get('LatestInstanceId')
        if m.get('LatestInstanceStatus') is not None:
            self.latest_instance_status = m.get('LatestInstanceStatus')
        if m.get('LatestStartTime') is not None:
            self.latest_start_time = m.get('LatestStartTime')
        return self


class LogInfo(TeaModel):
    def __init__(
        self,
        biz_time: str = None,
        gmt_create: str = None,
        instance_id: str = None,
        log_content: str = None,
        log_id: str = None,
        log_summary: str = None,
        log_type: str = None,
    ):
        self.biz_time = biz_time
        self.gmt_create = gmt_create
        self.instance_id = instance_id
        self.log_content = log_content
        self.log_id = log_id
        self.log_summary = log_summary
        self.log_type = log_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_time is not None:
            result['BizTime'] = self.biz_time
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.log_content is not None:
            result['LogContent'] = self.log_content
        if self.log_id is not None:
            result['LogId'] = self.log_id
        if self.log_summary is not None:
            result['LogSummary'] = self.log_summary
        if self.log_type is not None:
            result['LogType'] = self.log_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizTime') is not None:
            self.biz_time = m.get('BizTime')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LogContent') is not None:
            self.log_content = m.get('LogContent')
        if m.get('LogId') is not None:
            self.log_id = m.get('LogId')
        if m.get('LogSummary') is not None:
            self.log_summary = m.get('LogSummary')
        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')
        return self


class WorkflowInstance(TeaModel):
    def __init__(
        self,
        batch_progress: int = None,
        dlf_workflow_id: str = None,
        end_time: int = None,
        external_instance_id: str = None,
        runtime_logs: List[LogInfo] = None,
        start_time: int = None,
        status: str = None,
    ):
        self.batch_progress = batch_progress
        self.dlf_workflow_id = dlf_workflow_id
        self.end_time = end_time
        self.external_instance_id = external_instance_id
        self.runtime_logs = runtime_logs
        self.start_time = start_time
        self.status = status

    def validate(self):
        if self.runtime_logs:
            for k in self.runtime_logs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_progress is not None:
            result['BatchProgress'] = self.batch_progress
        if self.dlf_workflow_id is not None:
            result['DlfWorkflowId'] = self.dlf_workflow_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.external_instance_id is not None:
            result['ExternalInstanceId'] = self.external_instance_id
        result['RuntimeLogs'] = []
        if self.runtime_logs is not None:
            for k in self.runtime_logs:
                result['RuntimeLogs'].append(k.to_map() if k else None)
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchProgress') is not None:
            self.batch_progress = m.get('BatchProgress')
        if m.get('DlfWorkflowId') is not None:
            self.dlf_workflow_id = m.get('DlfWorkflowId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExternalInstanceId') is not None:
            self.external_instance_id = m.get('ExternalInstanceId')
        self.runtime_logs = []
        if m.get('RuntimeLogs') is not None:
            for k in m.get('RuntimeLogs'):
                temp_model = LogInfo()
                self.runtime_logs.append(temp_model.from_map(k))
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class LifecycleRule(TeaModel):
    def __init__(
        self,
        archive_days: int = None,
        bind_count: int = None,
        biz_id: str = None,
        catalog_id: str = None,
        cold_archive_days: int = None,
        config: str = None,
        description: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        ia_days: int = None,
        name: str = None,
        resource_type: str = None,
        rule_type: str = None,
        schedule_status: str = None,
        workflow: Workflow = None,
        workflow_id: str = None,
        workflow_instance: WorkflowInstance = None,
    ):
        self.archive_days = archive_days
        self.bind_count = bind_count
        self.biz_id = biz_id
        self.catalog_id = catalog_id
        self.cold_archive_days = cold_archive_days
        self.config = config
        self.description = description
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.ia_days = ia_days
        self.name = name
        self.resource_type = resource_type
        self.rule_type = rule_type
        self.schedule_status = schedule_status
        self.workflow = workflow
        self.workflow_id = workflow_id
        self.workflow_instance = workflow_instance

    def validate(self):
        if self.workflow:
            self.workflow.validate()
        if self.workflow_instance:
            self.workflow_instance.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.archive_days is not None:
            result['ArchiveDays'] = self.archive_days
        if self.bind_count is not None:
            result['BindCount'] = self.bind_count
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.cold_archive_days is not None:
            result['ColdArchiveDays'] = self.cold_archive_days
        if self.config is not None:
            result['Config'] = self.config
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.ia_days is not None:
            result['IaDays'] = self.ia_days
        if self.name is not None:
            result['Name'] = self.name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.schedule_status is not None:
            result['ScheduleStatus'] = self.schedule_status
        if self.workflow is not None:
            result['Workflow'] = self.workflow.to_map()
        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id
        if self.workflow_instance is not None:
            result['WorkflowInstance'] = self.workflow_instance.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArchiveDays') is not None:
            self.archive_days = m.get('ArchiveDays')
        if m.get('BindCount') is not None:
            self.bind_count = m.get('BindCount')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('ColdArchiveDays') is not None:
            self.cold_archive_days = m.get('ColdArchiveDays')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('IaDays') is not None:
            self.ia_days = m.get('IaDays')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('ScheduleStatus') is not None:
            self.schedule_status = m.get('ScheduleStatus')
        if m.get('Workflow') is not None:
            temp_model = Workflow()
            self.workflow = temp_model.from_map(m['Workflow'])
        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')
        if m.get('WorkflowInstance') is not None:
            temp_model = WorkflowInstance()
            self.workflow_instance = temp_model.from_map(m['WorkflowInstance'])
        return self


class LifecycleTask(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        lifecycle_rule: LifecycleRule = None,
        name: str = None,
        workflow_instance: WorkflowInstance = None,
    ):
        self.biz_id = biz_id
        self.lifecycle_rule = lifecycle_rule
        self.name = name
        self.workflow_instance = workflow_instance

    def validate(self):
        if self.lifecycle_rule:
            self.lifecycle_rule.validate()
        if self.workflow_instance:
            self.workflow_instance.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.lifecycle_rule is not None:
            result['LifecycleRule'] = self.lifecycle_rule.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.workflow_instance is not None:
            result['WorkflowInstance'] = self.workflow_instance.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('LifecycleRule') is not None:
            temp_model = LifecycleRule()
            self.lifecycle_rule = temp_model.from_map(m['LifecycleRule'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('WorkflowInstance') is not None:
            temp_model = WorkflowInstance()
            self.workflow_instance = temp_model.from_map(m['WorkflowInstance'])
        return self


class LocationStorageRankDTO(TeaModel):
    def __init__(
        self,
        file_cnt: int = None,
        location: str = None,
        storage: int = None,
    ):
        self.file_cnt = file_cnt
        self.location = location
        self.storage = storage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_cnt is not None:
            result['FileCnt'] = self.file_cnt
        if self.location is not None:
            result['Location'] = self.location
        if self.storage is not None:
            result['Storage'] = self.storage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileCnt') is not None:
            self.file_cnt = m.get('FileCnt')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Storage') is not None:
            self.storage = m.get('Storage')
        return self


class LockObj(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        database_name: str = None,
        partition_name: str = None,
        table_name: str = None,
    ):
        self.catalog_id = catalog_id
        self.database_name = database_name
        self.partition_name = partition_name
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.partition_name is not None:
            result['PartitionName'] = self.partition_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('PartitionName') is not None:
            self.partition_name = m.get('PartitionName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class LockStatus(TeaModel):
    def __init__(
        self,
        lock_id: int = None,
        lock_state: str = None,
    ):
        self.lock_id = lock_id
        self.lock_state = lock_state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lock_id is not None:
            result['LockId'] = self.lock_id
        if self.lock_state is not None:
            result['LockState'] = self.lock_state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LockId') is not None:
            self.lock_id = m.get('LockId')
        if m.get('LockState') is not None:
            self.lock_state = m.get('LockState')
        return self


class Order(TeaModel):
    def __init__(
        self,
        col: str = None,
        order: int = None,
    ):
        self.col = col
        self.order = order

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.col is not None:
            result['Col'] = self.col
        if self.order is not None:
            result['Order'] = self.order
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Col') is not None:
            self.col = m.get('Col')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        return self


class SerDeInfo(TeaModel):
    def __init__(
        self,
        name: str = None,
        parameters: Dict[str, str] = None,
        serialization_lib: str = None,
    ):
        self.name = name
        self.parameters = parameters
        self.serialization_lib = serialization_lib

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.serialization_lib is not None:
            result['SerializationLib'] = self.serialization_lib
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('SerializationLib') is not None:
            self.serialization_lib = m.get('SerializationLib')
        return self


class SkewedInfo(TeaModel):
    def __init__(
        self,
        skewed_col_names: List[str] = None,
        skewed_col_value_location_maps: Dict[str, str] = None,
        skewed_col_values: List[List[str]] = None,
    ):
        self.skewed_col_names = skewed_col_names
        self.skewed_col_value_location_maps = skewed_col_value_location_maps
        self.skewed_col_values = skewed_col_values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.skewed_col_names is not None:
            result['SkewedColNames'] = self.skewed_col_names
        if self.skewed_col_value_location_maps is not None:
            result['SkewedColValueLocationMaps'] = self.skewed_col_value_location_maps
        if self.skewed_col_values is not None:
            result['SkewedColValues'] = self.skewed_col_values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SkewedColNames') is not None:
            self.skewed_col_names = m.get('SkewedColNames')
        if m.get('SkewedColValueLocationMaps') is not None:
            self.skewed_col_value_location_maps = m.get('SkewedColValueLocationMaps')
        if m.get('SkewedColValues') is not None:
            self.skewed_col_values = m.get('SkewedColValues')
        return self


class StorageDescriptor(TeaModel):
    def __init__(
        self,
        bucket_cols: List[str] = None,
        cols: List[FieldSchema] = None,
        compressed: bool = None,
        input_format: str = None,
        location: str = None,
        num_buckets: int = None,
        output_format: str = None,
        parameters: Dict[str, str] = None,
        ser_de_info: SerDeInfo = None,
        skewed_info: SkewedInfo = None,
        sort_cols: List[Order] = None,
        stored_as_sub_directories: bool = None,
    ):
        self.bucket_cols = bucket_cols
        self.cols = cols
        self.compressed = compressed
        self.input_format = input_format
        self.location = location
        self.num_buckets = num_buckets
        self.output_format = output_format
        self.parameters = parameters
        self.ser_de_info = ser_de_info
        self.skewed_info = skewed_info
        self.sort_cols = sort_cols
        self.stored_as_sub_directories = stored_as_sub_directories

    def validate(self):
        if self.cols:
            for k in self.cols:
                if k:
                    k.validate()
        if self.ser_de_info:
            self.ser_de_info.validate()
        if self.skewed_info:
            self.skewed_info.validate()
        if self.sort_cols:
            for k in self.sort_cols:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_cols is not None:
            result['BucketCols'] = self.bucket_cols
        result['Cols'] = []
        if self.cols is not None:
            for k in self.cols:
                result['Cols'].append(k.to_map() if k else None)
        if self.compressed is not None:
            result['Compressed'] = self.compressed
        if self.input_format is not None:
            result['InputFormat'] = self.input_format
        if self.location is not None:
            result['Location'] = self.location
        if self.num_buckets is not None:
            result['NumBuckets'] = self.num_buckets
        if self.output_format is not None:
            result['OutputFormat'] = self.output_format
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.ser_de_info is not None:
            result['SerDeInfo'] = self.ser_de_info.to_map()
        if self.skewed_info is not None:
            result['SkewedInfo'] = self.skewed_info.to_map()
        result['SortCols'] = []
        if self.sort_cols is not None:
            for k in self.sort_cols:
                result['SortCols'].append(k.to_map() if k else None)
        if self.stored_as_sub_directories is not None:
            result['StoredAsSubDirectories'] = self.stored_as_sub_directories
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketCols') is not None:
            self.bucket_cols = m.get('BucketCols')
        self.cols = []
        if m.get('Cols') is not None:
            for k in m.get('Cols'):
                temp_model = FieldSchema()
                self.cols.append(temp_model.from_map(k))
        if m.get('Compressed') is not None:
            self.compressed = m.get('Compressed')
        if m.get('InputFormat') is not None:
            self.input_format = m.get('InputFormat')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('NumBuckets') is not None:
            self.num_buckets = m.get('NumBuckets')
        if m.get('OutputFormat') is not None:
            self.output_format = m.get('OutputFormat')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('SerDeInfo') is not None:
            temp_model = SerDeInfo()
            self.ser_de_info = temp_model.from_map(m['SerDeInfo'])
        if m.get('SkewedInfo') is not None:
            temp_model = SkewedInfo()
            self.skewed_info = temp_model.from_map(m['SkewedInfo'])
        self.sort_cols = []
        if m.get('SortCols') is not None:
            for k in m.get('SortCols'):
                temp_model = Order()
                self.sort_cols.append(temp_model.from_map(k))
        if m.get('StoredAsSubDirectories') is not None:
            self.stored_as_sub_directories = m.get('StoredAsSubDirectories')
        return self


class Partition(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        database_name: str = None,
        last_access_time: int = None,
        last_analyzed_time: int = None,
        parameters: Dict[str, str] = None,
        privileges: PrincipalPrivilegeSet = None,
        sd: StorageDescriptor = None,
        table_name: str = None,
        values: List[str] = None,
    ):
        self.create_time = create_time
        self.database_name = database_name
        self.last_access_time = last_access_time
        self.last_analyzed_time = last_analyzed_time
        self.parameters = parameters
        self.privileges = privileges
        self.sd = sd
        self.table_name = table_name
        self.values = values

    def validate(self):
        if self.privileges:
            self.privileges.validate()
        if self.sd:
            self.sd.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.last_access_time is not None:
            result['LastAccessTime'] = self.last_access_time
        if self.last_analyzed_time is not None:
            result['LastAnalyzedTime'] = self.last_analyzed_time
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.privileges is not None:
            result['Privileges'] = self.privileges.to_map()
        if self.sd is not None:
            result['Sd'] = self.sd.to_map()
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('LastAccessTime') is not None:
            self.last_access_time = m.get('LastAccessTime')
        if m.get('LastAnalyzedTime') is not None:
            self.last_analyzed_time = m.get('LastAnalyzedTime')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('Privileges') is not None:
            temp_model = PrincipalPrivilegeSet()
            self.privileges = temp_model.from_map(m['Privileges'])
        if m.get('Sd') is not None:
            temp_model = StorageDescriptor()
            self.sd = temp_model.from_map(m['Sd'])
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class PartitionError(TeaModel):
    def __init__(
        self,
        error_detail: ErrorDetail = None,
        partition_values: List[str] = None,
    ):
        self.error_detail = error_detail
        self.partition_values = partition_values

    def validate(self):
        if self.error_detail:
            self.error_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_detail is not None:
            result['ErrorDetail'] = self.error_detail.to_map()
        if self.partition_values is not None:
            result['PartitionValues'] = self.partition_values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorDetail') is not None:
            temp_model = ErrorDetail()
            self.error_detail = temp_model.from_map(m['ErrorDetail'])
        if m.get('PartitionValues') is not None:
            self.partition_values = m.get('PartitionValues')
        return self


class PartitionInput(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        database_name: str = None,
        last_access_time: int = None,
        last_analyzed_time: int = None,
        parameters: Dict[str, str] = None,
        privileges: PrincipalPrivilegeSet = None,
        sd: StorageDescriptor = None,
        table_name: str = None,
        values: List[str] = None,
    ):
        self.create_time = create_time
        self.database_name = database_name
        self.last_access_time = last_access_time
        self.last_analyzed_time = last_analyzed_time
        self.parameters = parameters
        self.privileges = privileges
        self.sd = sd
        self.table_name = table_name
        self.values = values

    def validate(self):
        if self.privileges:
            self.privileges.validate()
        if self.sd:
            self.sd.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.last_access_time is not None:
            result['LastAccessTime'] = self.last_access_time
        if self.last_analyzed_time is not None:
            result['LastAnalyzedTime'] = self.last_analyzed_time
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.privileges is not None:
            result['Privileges'] = self.privileges.to_map()
        if self.sd is not None:
            result['Sd'] = self.sd.to_map()
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('LastAccessTime') is not None:
            self.last_access_time = m.get('LastAccessTime')
        if m.get('LastAnalyzedTime') is not None:
            self.last_analyzed_time = m.get('LastAnalyzedTime')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('Privileges') is not None:
            temp_model = PrincipalPrivilegeSet()
            self.privileges = temp_model.from_map(m['Privileges'])
        if m.get('Sd') is not None:
            temp_model = StorageDescriptor()
            self.sd = temp_model.from_map(m['Sd'])
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class PartitionProfile(TeaModel):
    def __init__(
        self,
        archive_status: str = None,
        create_time: str = None,
        database_name: str = None,
        dml_time: str = None,
        location: str = None,
        partition_name: str = None,
        table_name: str = None,
    ):
        self.archive_status = archive_status
        self.create_time = create_time
        self.database_name = database_name
        self.dml_time = dml_time
        self.location = location
        self.partition_name = partition_name
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.archive_status is not None:
            result['ArchiveStatus'] = self.archive_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.dml_time is not None:
            result['DmlTime'] = self.dml_time
        if self.location is not None:
            result['Location'] = self.location
        if self.partition_name is not None:
            result['PartitionName'] = self.partition_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArchiveStatus') is not None:
            self.archive_status = m.get('ArchiveStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('DmlTime') is not None:
            self.dml_time = m.get('DmlTime')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('PartitionName') is not None:
            self.partition_name = m.get('PartitionName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class PartitionSpecSharedStorageDescriptor(TeaModel):
    def __init__(
        self,
        cols: List[FieldSchema] = None,
        location: str = None,
    ):
        self.cols = cols
        self.location = location

    def validate(self):
        if self.cols:
            for k in self.cols:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Cols'] = []
        if self.cols is not None:
            for k in self.cols:
                result['Cols'].append(k.to_map() if k else None)
        if self.location is not None:
            result['Location'] = self.location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cols = []
        if m.get('Cols') is not None:
            for k in m.get('Cols'):
                temp_model = FieldSchema()
                self.cols.append(temp_model.from_map(k))
        if m.get('Location') is not None:
            self.location = m.get('Location')
        return self


class PartitionSpec(TeaModel):
    def __init__(
        self,
        shared_sdpartitions: List[Partition] = None,
        shared_storage_descriptor: PartitionSpecSharedStorageDescriptor = None,
    ):
        self.shared_sdpartitions = shared_sdpartitions
        self.shared_storage_descriptor = shared_storage_descriptor

    def validate(self):
        if self.shared_sdpartitions:
            for k in self.shared_sdpartitions:
                if k:
                    k.validate()
        if self.shared_storage_descriptor:
            self.shared_storage_descriptor.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SharedSDPartitions'] = []
        if self.shared_sdpartitions is not None:
            for k in self.shared_sdpartitions:
                result['SharedSDPartitions'].append(k.to_map() if k else None)
        if self.shared_storage_descriptor is not None:
            result['SharedStorageDescriptor'] = self.shared_storage_descriptor.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.shared_sdpartitions = []
        if m.get('SharedSDPartitions') is not None:
            for k in m.get('SharedSDPartitions'):
                temp_model = Partition()
                self.shared_sdpartitions.append(temp_model.from_map(k))
        if m.get('SharedStorageDescriptor') is not None:
            temp_model = PartitionSpecSharedStorageDescriptor()
            self.shared_storage_descriptor = temp_model.from_map(m['SharedStorageDescriptor'])
        return self


class PrincipalResourcePermissions(TeaModel):
    def __init__(
        self,
        accesses: List[str] = None,
        delegate_accesses: List[str] = None,
        meta_resource: MetaResource = None,
        principal: Principal = None,
    ):
        self.accesses = accesses
        self.delegate_accesses = delegate_accesses
        self.meta_resource = meta_resource
        self.principal = principal

    def validate(self):
        if self.meta_resource:
            self.meta_resource.validate()
        if self.principal:
            self.principal.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accesses is not None:
            result['Accesses'] = self.accesses
        if self.delegate_accesses is not None:
            result['DelegateAccesses'] = self.delegate_accesses
        if self.meta_resource is not None:
            result['MetaResource'] = self.meta_resource.to_map()
        if self.principal is not None:
            result['Principal'] = self.principal.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accesses') is not None:
            self.accesses = m.get('Accesses')
        if m.get('DelegateAccesses') is not None:
            self.delegate_accesses = m.get('DelegateAccesses')
        if m.get('MetaResource') is not None:
            temp_model = MetaResource()
            self.meta_resource = temp_model.from_map(m['MetaResource'])
        if m.get('Principal') is not None:
            temp_model = Principal()
            self.principal = temp_model.from_map(m['Principal'])
        return self


class Role(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        description: str = None,
        display_name: str = None,
        is_predefined: int = None,
        name: str = None,
        principal_arn: str = None,
        update_time: int = None,
        users: List[Principal] = None,
    ):
        self.create_time = create_time
        self.description = description
        self.display_name = display_name
        self.is_predefined = is_predefined
        self.name = name
        self.principal_arn = principal_arn
        self.update_time = update_time
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
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.is_predefined is not None:
            result['IsPredefined'] = self.is_predefined
        if self.name is not None:
            result['Name'] = self.name
        if self.principal_arn is not None:
            result['PrincipalArn'] = self.principal_arn
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        result['Users'] = []
        if self.users is not None:
            for k in self.users:
                result['Users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('IsPredefined') is not None:
            self.is_predefined = m.get('IsPredefined')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PrincipalArn') is not None:
            self.principal_arn = m.get('PrincipalArn')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        self.users = []
        if m.get('Users') is not None:
            for k in m.get('Users'):
                temp_model = Principal()
                self.users.append(temp_model.from_map(k))
        return self


class RoleInput(TeaModel):
    def __init__(
        self,
        description: str = None,
        display_name: str = None,
        name: str = None,
    ):
        self.description = description
        self.display_name = display_name
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class SingleIndicatorDTO(TeaModel):
    def __init__(
        self,
        day_increment: int = None,
        day_on_day: float = None,
        month_increment: int = None,
        month_on_month: float = None,
        total: int = None,
    ):
        self.day_increment = day_increment
        self.day_on_day = day_on_day
        self.month_increment = month_increment
        self.month_on_month = month_on_month
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day_increment is not None:
            result['DayIncrement'] = self.day_increment
        if self.day_on_day is not None:
            result['DayOnDay'] = self.day_on_day
        if self.month_increment is not None:
            result['MonthIncrement'] = self.month_increment
        if self.month_on_month is not None:
            result['MonthOnMonth'] = self.month_on_month
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DayIncrement') is not None:
            self.day_increment = m.get('DayIncrement')
        if m.get('DayOnDay') is not None:
            self.day_on_day = m.get('DayOnDay')
        if m.get('MonthIncrement') is not None:
            self.month_increment = m.get('MonthIncrement')
        if m.get('MonthOnMonth') is not None:
            self.month_on_month = m.get('MonthOnMonth')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class SmallFileCntRank(TeaModel):
    def __init__(
        self,
        db_name: str = None,
        location: str = None,
        quantity: int = None,
        table_name: str = None,
    ):
        self.db_name = db_name
        self.location = location
        self.quantity = quantity
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.location is not None:
            result['Location'] = self.location
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class SortCriterion(TeaModel):
    def __init__(
        self,
        field_name: str = None,
        sort: str = None,
    ):
        self.field_name = field_name
        self.sort = sort

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_name is not None:
            result['FieldName'] = self.field_name
        if self.sort is not None:
            result['Sort'] = self.sort
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        return self


class StorageCollectTaskOperationResult(TeaModel):
    def __init__(
        self,
        dlf_created: bool = None,
        err_code: str = None,
        err_message: str = None,
        success: bool = None,
        task_id: str = None,
        task_type: str = None,
    ):
        self.dlf_created = dlf_created
        self.err_code = err_code
        self.err_message = err_message
        self.success = success
        self.task_id = task_id
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dlf_created is not None:
            result['DlfCreated'] = self.dlf_created
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DlfCreated') is not None:
            self.dlf_created = m.get('DlfCreated')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class StorageFormat(TeaModel):
    def __init__(
        self,
        avro: int = None,
        csv: int = None,
        delta: int = None,
        hudi: int = None,
        iceberg: int = None,
        json: int = None,
        orc: int = None,
        parquet: int = None,
        uncategorized: int = None,
    ):
        self.avro = avro
        self.csv = csv
        self.delta = delta
        self.hudi = hudi
        self.iceberg = iceberg
        self.json = json
        self.orc = orc
        self.parquet = parquet
        self.uncategorized = uncategorized

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avro is not None:
            result['Avro'] = self.avro
        if self.csv is not None:
            result['Csv'] = self.csv
        if self.delta is not None:
            result['Delta'] = self.delta
        if self.hudi is not None:
            result['Hudi'] = self.hudi
        if self.iceberg is not None:
            result['Iceberg'] = self.iceberg
        if self.json is not None:
            result['Json'] = self.json
        if self.orc is not None:
            result['Orc'] = self.orc
        if self.parquet is not None:
            result['Parquet'] = self.parquet
        if self.uncategorized is not None:
            result['Uncategorized'] = self.uncategorized
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Avro') is not None:
            self.avro = m.get('Avro')
        if m.get('Csv') is not None:
            self.csv = m.get('Csv')
        if m.get('Delta') is not None:
            self.delta = m.get('Delta')
        if m.get('Hudi') is not None:
            self.hudi = m.get('Hudi')
        if m.get('Iceberg') is not None:
            self.iceberg = m.get('Iceberg')
        if m.get('Json') is not None:
            self.json = m.get('Json')
        if m.get('Orc') is not None:
            self.orc = m.get('Orc')
        if m.get('Parquet') is not None:
            self.parquet = m.get('Parquet')
        if m.get('Uncategorized') is not None:
            self.uncategorized = m.get('Uncategorized')
        return self


class StorageLayer(TeaModel):
    def __init__(
        self,
        archive: int = None,
        cold_archive: int = None,
        infrequent: int = None,
        standard: int = None,
    ):
        self.archive = archive
        self.cold_archive = cold_archive
        self.infrequent = infrequent
        self.standard = standard

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.archive is not None:
            result['Archive'] = self.archive
        if self.cold_archive is not None:
            result['ColdArchive'] = self.cold_archive
        if self.infrequent is not None:
            result['Infrequent'] = self.infrequent
        if self.standard is not None:
            result['Standard'] = self.standard
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Archive') is not None:
            self.archive = m.get('Archive')
        if m.get('ColdArchive') is not None:
            self.cold_archive = m.get('ColdArchive')
        if m.get('Infrequent') is not None:
            self.infrequent = m.get('Infrequent')
        if m.get('Standard') is not None:
            self.standard = m.get('Standard')
        return self


class TableStorageRank(TeaModel):
    def __init__(
        self,
        db_name: str = None,
        quantity: int = None,
        table_name: str = None,
    ):
        self.db_name = db_name
        self.quantity = quantity
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class StorageRankDTO(TeaModel):
    def __init__(
        self,
        db_storage_rank: List[DbStorageRank] = None,
        small_file_cnt_rank: List[SmallFileCntRank] = None,
        table_storage_rank: List[TableStorageRank] = None,
    ):
        self.db_storage_rank = db_storage_rank
        self.small_file_cnt_rank = small_file_cnt_rank
        self.table_storage_rank = table_storage_rank

    def validate(self):
        if self.db_storage_rank:
            for k in self.db_storage_rank:
                if k:
                    k.validate()
        if self.small_file_cnt_rank:
            for k in self.small_file_cnt_rank:
                if k:
                    k.validate()
        if self.table_storage_rank:
            for k in self.table_storage_rank:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['dbStorageRank'] = []
        if self.db_storage_rank is not None:
            for k in self.db_storage_rank:
                result['dbStorageRank'].append(k.to_map() if k else None)
        result['smallFileCntRank'] = []
        if self.small_file_cnt_rank is not None:
            for k in self.small_file_cnt_rank:
                result['smallFileCntRank'].append(k.to_map() if k else None)
        result['tableStorageRank'] = []
        if self.table_storage_rank is not None:
            for k in self.table_storage_rank:
                result['tableStorageRank'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.db_storage_rank = []
        if m.get('dbStorageRank') is not None:
            for k in m.get('dbStorageRank'):
                temp_model = DbStorageRank()
                self.db_storage_rank.append(temp_model.from_map(k))
        self.small_file_cnt_rank = []
        if m.get('smallFileCntRank') is not None:
            for k in m.get('smallFileCntRank'):
                temp_model = SmallFileCntRank()
                self.small_file_cnt_rank.append(temp_model.from_map(k))
        self.table_storage_rank = []
        if m.get('tableStorageRank') is not None:
            for k in m.get('tableStorageRank'):
                temp_model = TableStorageRank()
                self.table_storage_rank.append(temp_model.from_map(k))
        return self


class StorageSummary(TeaModel):
    def __init__(
        self,
        database_num: int = None,
        partition_num: int = None,
        table_num: int = None,
    ):
        self.database_num = database_num
        self.partition_num = partition_num
        self.table_num = table_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_num is not None:
            result['DatabaseNum'] = self.database_num
        if self.partition_num is not None:
            result['PartitionNum'] = self.partition_num
        if self.table_num is not None:
            result['TableNum'] = self.table_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseNum') is not None:
            self.database_num = m.get('DatabaseNum')
        if m.get('PartitionNum') is not None:
            self.partition_num = m.get('PartitionNum')
        if m.get('TableNum') is not None:
            self.table_num = m.get('TableNum')
        return self


class StrogeCollectTask(TeaModel):
    def __init__(
        self,
        destination_bucket_name: str = None,
        destination_prefix: str = None,
        dlf_created: bool = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: str = None,
        inventory_id: str = None,
        location: str = None,
        status: str = None,
        task_type: str = None,
    ):
        self.destination_bucket_name = destination_bucket_name
        self.destination_prefix = destination_prefix
        self.dlf_created = dlf_created
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.inventory_id = inventory_id
        self.location = location
        self.status = status
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_bucket_name is not None:
            result['DestinationBucketName'] = self.destination_bucket_name
        if self.destination_prefix is not None:
            result['DestinationPrefix'] = self.destination_prefix
        if self.dlf_created is not None:
            result['DlfCreated'] = self.dlf_created
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.inventory_id is not None:
            result['InventoryId'] = self.inventory_id
        if self.location is not None:
            result['Location'] = self.location
        if self.status is not None:
            result['Status'] = self.status
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationBucketName') is not None:
            self.destination_bucket_name = m.get('DestinationBucketName')
        if m.get('DestinationPrefix') is not None:
            self.destination_prefix = m.get('DestinationPrefix')
        if m.get('DlfCreated') is not None:
            self.dlf_created = m.get('DlfCreated')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InventoryId') is not None:
            self.inventory_id = m.get('InventoryId')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class TableVersion(TeaModel):
    def __init__(
        self,
        table: Table = None,
        version_id: int = None,
    ):
        self.table = table
        self.version_id = version_id

    def validate(self):
        if self.table:
            self.table.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.table is not None:
            result['Table'] = self.table.to_map()
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Table') is not None:
            temp_model = Table()
            self.table = temp_model.from_map(m['Table'])
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class Table(TeaModel):
    def __init__(
        self,
        cascade: bool = None,
        create_time: int = None,
        created_by: str = None,
        database_name: str = None,
        last_access_time: int = None,
        last_analyzed_time: int = None,
        owner: str = None,
        owner_type: str = None,
        parameters: Dict[str, str] = None,
        partition_keys: List[FieldSchema] = None,
        privileges: PrincipalPrivilegeSet = None,
        retention: int = None,
        rewrite_enabled: bool = None,
        sd: StorageDescriptor = None,
        table_id: str = None,
        table_name: str = None,
        table_type: str = None,
        table_version: TableVersion = None,
        temporary: bool = None,
        update_time: int = None,
        view_expanded_text: str = None,
        view_original_text: str = None,
    ):
        self.cascade = cascade
        self.create_time = create_time
        self.created_by = created_by
        self.database_name = database_name
        self.last_access_time = last_access_time
        self.last_analyzed_time = last_analyzed_time
        self.owner = owner
        self.owner_type = owner_type
        self.parameters = parameters
        self.partition_keys = partition_keys
        self.privileges = privileges
        self.retention = retention
        self.rewrite_enabled = rewrite_enabled
        self.sd = sd
        self.table_id = table_id
        self.table_name = table_name
        self.table_type = table_type
        self.table_version = table_version
        self.temporary = temporary
        self.update_time = update_time
        self.view_expanded_text = view_expanded_text
        self.view_original_text = view_original_text

    def validate(self):
        if self.partition_keys:
            for k in self.partition_keys:
                if k:
                    k.validate()
        if self.privileges:
            self.privileges.validate()
        if self.sd:
            self.sd.validate()
        if self.table_version:
            self.table_version.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cascade is not None:
            result['Cascade'] = self.cascade
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.last_access_time is not None:
            result['LastAccessTime'] = self.last_access_time
        if self.last_analyzed_time is not None:
            result['LastAnalyzedTime'] = self.last_analyzed_time
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.owner_type is not None:
            result['OwnerType'] = self.owner_type
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        result['PartitionKeys'] = []
        if self.partition_keys is not None:
            for k in self.partition_keys:
                result['PartitionKeys'].append(k.to_map() if k else None)
        if self.privileges is not None:
            result['Privileges'] = self.privileges.to_map()
        if self.retention is not None:
            result['Retention'] = self.retention
        if self.rewrite_enabled is not None:
            result['RewriteEnabled'] = self.rewrite_enabled
        if self.sd is not None:
            result['Sd'] = self.sd.to_map()
        if self.table_id is not None:
            result['TableId'] = self.table_id
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.table_type is not None:
            result['TableType'] = self.table_type
        if self.table_version is not None:
            result['TableVersion'] = self.table_version.to_map()
        if self.temporary is not None:
            result['Temporary'] = self.temporary
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.view_expanded_text is not None:
            result['ViewExpandedText'] = self.view_expanded_text
        if self.view_original_text is not None:
            result['ViewOriginalText'] = self.view_original_text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cascade') is not None:
            self.cascade = m.get('Cascade')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('LastAccessTime') is not None:
            self.last_access_time = m.get('LastAccessTime')
        if m.get('LastAnalyzedTime') is not None:
            self.last_analyzed_time = m.get('LastAnalyzedTime')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('OwnerType') is not None:
            self.owner_type = m.get('OwnerType')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        self.partition_keys = []
        if m.get('PartitionKeys') is not None:
            for k in m.get('PartitionKeys'):
                temp_model = FieldSchema()
                self.partition_keys.append(temp_model.from_map(k))
        if m.get('Privileges') is not None:
            temp_model = PrincipalPrivilegeSet()
            self.privileges = temp_model.from_map(m['Privileges'])
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        if m.get('RewriteEnabled') is not None:
            self.rewrite_enabled = m.get('RewriteEnabled')
        if m.get('Sd') is not None:
            temp_model = StorageDescriptor()
            self.sd = temp_model.from_map(m['Sd'])
        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('TableType') is not None:
            self.table_type = m.get('TableType')
        if m.get('TableVersion') is not None:
            temp_model = TableVersion()
            self.table_version = temp_model.from_map(m['TableVersion'])
        if m.get('Temporary') is not None:
            self.temporary = m.get('Temporary')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('ViewExpandedText') is not None:
            self.view_expanded_text = m.get('ViewExpandedText')
        if m.get('ViewOriginalText') is not None:
            self.view_original_text = m.get('ViewOriginalText')
        return self


class TableError(TeaModel):
    def __init__(
        self,
        error_detail: ErrorDetail = None,
        table_name: str = None,
    ):
        self.error_detail = error_detail
        self.table_name = table_name

    def validate(self):
        if self.error_detail:
            self.error_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_detail is not None:
            result['ErrorDetail'] = self.error_detail.to_map()
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorDetail') is not None:
            temp_model = ErrorDetail()
            self.error_detail = temp_model.from_map(m['ErrorDetail'])
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class TableExtendedPrivilegesRolePrivilegesValue(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        grant_option: bool = None,
        grantor: str = None,
        grantor_type: str = None,
        privilege: str = None,
    ):
        self.create_time = create_time
        self.grant_option = grant_option
        self.grantor = grantor
        self.grantor_type = grantor_type
        self.privilege = privilege

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.grant_option is not None:
            result['GrantOption'] = self.grant_option
        if self.grantor is not None:
            result['Grantor'] = self.grantor
        if self.grantor_type is not None:
            result['GrantorType'] = self.grantor_type
        if self.privilege is not None:
            result['Privilege'] = self.privilege
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('GrantOption') is not None:
            self.grant_option = m.get('GrantOption')
        if m.get('Grantor') is not None:
            self.grantor = m.get('Grantor')
        if m.get('GrantorType') is not None:
            self.grantor_type = m.get('GrantorType')
        if m.get('Privilege') is not None:
            self.privilege = m.get('Privilege')
        return self


class TableExtendedPrivilegesUserPrivilegesValue(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        grant_option: bool = None,
        grantor: str = None,
        grantor_type: str = None,
        privilege: str = None,
    ):
        self.create_time = create_time
        self.grant_option = grant_option
        self.grantor = grantor
        self.grantor_type = grantor_type
        self.privilege = privilege

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.grant_option is not None:
            result['GrantOption'] = self.grant_option
        if self.grantor is not None:
            result['Grantor'] = self.grantor
        if self.grantor_type is not None:
            result['GrantorType'] = self.grantor_type
        if self.privilege is not None:
            result['Privilege'] = self.privilege
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('GrantOption') is not None:
            self.grant_option = m.get('GrantOption')
        if m.get('Grantor') is not None:
            self.grantor = m.get('Grantor')
        if m.get('GrantorType') is not None:
            self.grantor_type = m.get('GrantorType')
        if m.get('Privilege') is not None:
            self.privilege = m.get('Privilege')
        return self


class TableExtendedPrivilegesGroupPrivilegesValue(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        grant_option: bool = None,
        grantor: str = None,
        grantor_type: str = None,
        privilege: str = None,
    ):
        self.create_time = create_time
        self.grant_option = grant_option
        self.grantor = grantor
        self.grantor_type = grantor_type
        self.privilege = privilege

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.grant_option is not None:
            result['GrantOption'] = self.grant_option
        if self.grantor is not None:
            result['Grantor'] = self.grantor
        if self.grantor_type is not None:
            result['GrantorType'] = self.grantor_type
        if self.privilege is not None:
            result['Privilege'] = self.privilege
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('GrantOption') is not None:
            self.grant_option = m.get('GrantOption')
        if m.get('Grantor') is not None:
            self.grantor = m.get('Grantor')
        if m.get('GrantorType') is not None:
            self.grantor_type = m.get('GrantorType')
        if m.get('Privilege') is not None:
            self.privilege = m.get('Privilege')
        return self


class TableExtendedPrivileges(TeaModel):
    def __init__(
        self,
        role_privileges: Dict[str, List[TableExtendedPrivilegesRolePrivilegesValue]] = None,
        user_privileges: Dict[str, List[TableExtendedPrivilegesUserPrivilegesValue]] = None,
        group_privileges: Dict[str, List[TableExtendedPrivilegesGroupPrivilegesValue]] = None,
    ):
        self.role_privileges = role_privileges
        self.user_privileges = user_privileges
        self.group_privileges = group_privileges

    def validate(self):
        if self.role_privileges:
            for v in self.role_privileges.values():
                for k1 in v:
                    if k1:
                        k1.validate()
        if self.user_privileges:
            for v in self.user_privileges.values():
                for k1 in v:
                    if k1:
                        k1.validate()
        if self.group_privileges:
            for v in self.group_privileges.values():
                for k1 in v:
                    if k1:
                        k1.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RolePrivileges'] = {}
        if self.role_privileges is not None:
            for k, v in self.role_privileges.items():
                l1 = []
                for k1 in v:
                    l1.append(k1.to_map() if k1 else None)
                result['rolePrivileges'][k] = l1
        result['UserPrivileges'] = {}
        if self.user_privileges is not None:
            for k, v in self.user_privileges.items():
                l1 = []
                for k1 in v:
                    l1.append(k1.to_map() if k1 else None)
                result['userPrivileges'][k] = l1
        result['groupPrivileges'] = {}
        if self.group_privileges is not None:
            for k, v in self.group_privileges.items():
                l1 = []
                for k1 in v:
                    l1.append(k1.to_map() if k1 else None)
                result['groupPrivileges'][k] = l1
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.role_privileges = {}
        if m.get('RolePrivileges') is not None:
            for k, v in m.get('RolePrivileges').items():
                l1 = []
                for k1 in v:
                    temp_model = TableExtendedPrivilegesRolePrivilegesValue()
                    l1.append(temp_model.from_map(k1))
                self.role_privileges['k'] = l1
        self.user_privileges = {}
        if m.get('UserPrivileges') is not None:
            for k, v in m.get('UserPrivileges').items():
                l1 = []
                for k1 in v:
                    temp_model = TableExtendedPrivilegesUserPrivilegesValue()
                    l1.append(temp_model.from_map(k1))
                self.user_privileges['k'] = l1
        self.group_privileges = {}
        if m.get('groupPrivileges') is not None:
            for k, v in m.get('groupPrivileges').items():
                l1 = []
                for k1 in v:
                    temp_model = TableExtendedPrivilegesGroupPrivilegesValue()
                    l1.append(temp_model.from_map(k1))
                self.group_privileges['k'] = l1
        return self


class TableExtendedSdSerDeInfo(TeaModel):
    def __init__(
        self,
        name: str = None,
        parameters: Dict[str, str] = None,
        serialization_lib: str = None,
    ):
        self.name = name
        self.parameters = parameters
        self.serialization_lib = serialization_lib

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.serialization_lib is not None:
            result['SerializationLib'] = self.serialization_lib
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('SerializationLib') is not None:
            self.serialization_lib = m.get('SerializationLib')
        return self


class TableExtendedSdSkewedInfo(TeaModel):
    def __init__(
        self,
        skewed_col_names: List[str] = None,
        skewed_col_value_location_maps: Dict[str, str] = None,
        skewed_col_values: List[List[str]] = None,
    ):
        self.skewed_col_names = skewed_col_names
        self.skewed_col_value_location_maps = skewed_col_value_location_maps
        self.skewed_col_values = skewed_col_values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.skewed_col_names is not None:
            result['SkewedColNames'] = self.skewed_col_names
        if self.skewed_col_value_location_maps is not None:
            result['SkewedColValueLocationMaps'] = self.skewed_col_value_location_maps
        if self.skewed_col_values is not None:
            result['SkewedColValues'] = self.skewed_col_values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SkewedColNames') is not None:
            self.skewed_col_names = m.get('SkewedColNames')
        if m.get('SkewedColValueLocationMaps') is not None:
            self.skewed_col_value_location_maps = m.get('SkewedColValueLocationMaps')
        if m.get('SkewedColValues') is not None:
            self.skewed_col_values = m.get('SkewedColValues')
        return self


class TableExtendedSd(TeaModel):
    def __init__(
        self,
        bucket_cols: List[str] = None,
        cols: List[FieldSchema] = None,
        compressed: bool = None,
        input_format: str = None,
        location: str = None,
        num_buckets: int = None,
        output_format: str = None,
        parameters: Dict[str, str] = None,
        ser_de_info: TableExtendedSdSerDeInfo = None,
        skewed_info: TableExtendedSdSkewedInfo = None,
        sort_cols: List[Order] = None,
        stored_as_sub_directories: bool = None,
    ):
        self.bucket_cols = bucket_cols
        self.cols = cols
        self.compressed = compressed
        self.input_format = input_format
        self.location = location
        self.num_buckets = num_buckets
        self.output_format = output_format
        self.parameters = parameters
        self.ser_de_info = ser_de_info
        self.skewed_info = skewed_info
        self.sort_cols = sort_cols
        self.stored_as_sub_directories = stored_as_sub_directories

    def validate(self):
        if self.cols:
            for k in self.cols:
                if k:
                    k.validate()
        if self.ser_de_info:
            self.ser_de_info.validate()
        if self.skewed_info:
            self.skewed_info.validate()
        if self.sort_cols:
            for k in self.sort_cols:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_cols is not None:
            result['BucketCols'] = self.bucket_cols
        result['Cols'] = []
        if self.cols is not None:
            for k in self.cols:
                result['Cols'].append(k.to_map() if k else None)
        if self.compressed is not None:
            result['Compressed'] = self.compressed
        if self.input_format is not None:
            result['InputFormat'] = self.input_format
        if self.location is not None:
            result['Location'] = self.location
        if self.num_buckets is not None:
            result['NumBuckets'] = self.num_buckets
        if self.output_format is not None:
            result['OutputFormat'] = self.output_format
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.ser_de_info is not None:
            result['SerDeInfo'] = self.ser_de_info.to_map()
        if self.skewed_info is not None:
            result['SkewedInfo'] = self.skewed_info.to_map()
        result['SortCols'] = []
        if self.sort_cols is not None:
            for k in self.sort_cols:
                result['SortCols'].append(k.to_map() if k else None)
        if self.stored_as_sub_directories is not None:
            result['StoredAsSubDirectories'] = self.stored_as_sub_directories
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketCols') is not None:
            self.bucket_cols = m.get('BucketCols')
        self.cols = []
        if m.get('Cols') is not None:
            for k in m.get('Cols'):
                temp_model = FieldSchema()
                self.cols.append(temp_model.from_map(k))
        if m.get('Compressed') is not None:
            self.compressed = m.get('Compressed')
        if m.get('InputFormat') is not None:
            self.input_format = m.get('InputFormat')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('NumBuckets') is not None:
            self.num_buckets = m.get('NumBuckets')
        if m.get('OutputFormat') is not None:
            self.output_format = m.get('OutputFormat')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('SerDeInfo') is not None:
            temp_model = TableExtendedSdSerDeInfo()
            self.ser_de_info = temp_model.from_map(m['SerDeInfo'])
        if m.get('SkewedInfo') is not None:
            temp_model = TableExtendedSdSkewedInfo()
            self.skewed_info = temp_model.from_map(m['SkewedInfo'])
        self.sort_cols = []
        if m.get('SortCols') is not None:
            for k in m.get('SortCols'):
                temp_model = Order()
                self.sort_cols.append(temp_model.from_map(k))
        if m.get('StoredAsSubDirectories') is not None:
            self.stored_as_sub_directories = m.get('StoredAsSubDirectories')
        return self


class TableExtended(TeaModel):
    def __init__(
        self,
        cascade: bool = None,
        create_time: int = None,
        created_by: str = None,
        database_name: str = None,
        last_access_time: int = None,
        last_analyzed_time: int = None,
        owner: str = None,
        owner_type: str = None,
        parameters: Dict[str, str] = None,
        partition_keys: List[FieldSchema] = None,
        privileges: TableExtendedPrivileges = None,
        retention: int = None,
        rewrite_enabled: bool = None,
        sd: TableExtendedSd = None,
        table_format: str = None,
        table_name: str = None,
        table_type: str = None,
        temporary: bool = None,
        update_time: int = None,
        view_expanded_text: str = None,
        view_original_text: str = None,
    ):
        self.cascade = cascade
        self.create_time = create_time
        self.created_by = created_by
        self.database_name = database_name
        self.last_access_time = last_access_time
        self.last_analyzed_time = last_analyzed_time
        self.owner = owner
        self.owner_type = owner_type
        self.parameters = parameters
        self.partition_keys = partition_keys
        self.privileges = privileges
        self.retention = retention
        self.rewrite_enabled = rewrite_enabled
        self.sd = sd
        self.table_format = table_format
        self.table_name = table_name
        self.table_type = table_type
        self.temporary = temporary
        self.update_time = update_time
        self.view_expanded_text = view_expanded_text
        self.view_original_text = view_original_text

    def validate(self):
        if self.partition_keys:
            for k in self.partition_keys:
                if k:
                    k.validate()
        if self.privileges:
            self.privileges.validate()
        if self.sd:
            self.sd.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cascade is not None:
            result['Cascade'] = self.cascade
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.last_access_time is not None:
            result['LastAccessTime'] = self.last_access_time
        if self.last_analyzed_time is not None:
            result['LastAnalyzedTime'] = self.last_analyzed_time
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.owner_type is not None:
            result['OwnerType'] = self.owner_type
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        result['PartitionKeys'] = []
        if self.partition_keys is not None:
            for k in self.partition_keys:
                result['PartitionKeys'].append(k.to_map() if k else None)
        if self.privileges is not None:
            result['Privileges'] = self.privileges.to_map()
        if self.retention is not None:
            result['Retention'] = self.retention
        if self.rewrite_enabled is not None:
            result['RewriteEnabled'] = self.rewrite_enabled
        if self.sd is not None:
            result['Sd'] = self.sd.to_map()
        if self.table_format is not None:
            result['TableFormat'] = self.table_format
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.table_type is not None:
            result['TableType'] = self.table_type
        if self.temporary is not None:
            result['Temporary'] = self.temporary
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.view_expanded_text is not None:
            result['ViewExpandedText'] = self.view_expanded_text
        if self.view_original_text is not None:
            result['ViewOriginalText'] = self.view_original_text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cascade') is not None:
            self.cascade = m.get('Cascade')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('LastAccessTime') is not None:
            self.last_access_time = m.get('LastAccessTime')
        if m.get('LastAnalyzedTime') is not None:
            self.last_analyzed_time = m.get('LastAnalyzedTime')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('OwnerType') is not None:
            self.owner_type = m.get('OwnerType')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        self.partition_keys = []
        if m.get('PartitionKeys') is not None:
            for k in m.get('PartitionKeys'):
                temp_model = FieldSchema()
                self.partition_keys.append(temp_model.from_map(k))
        if m.get('Privileges') is not None:
            temp_model = TableExtendedPrivileges()
            self.privileges = temp_model.from_map(m['Privileges'])
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        if m.get('RewriteEnabled') is not None:
            self.rewrite_enabled = m.get('RewriteEnabled')
        if m.get('Sd') is not None:
            temp_model = TableExtendedSd()
            self.sd = temp_model.from_map(m['Sd'])
        if m.get('TableFormat') is not None:
            self.table_format = m.get('TableFormat')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('TableType') is not None:
            self.table_type = m.get('TableType')
        if m.get('Temporary') is not None:
            self.temporary = m.get('Temporary')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('ViewExpandedText') is not None:
            self.view_expanded_text = m.get('ViewExpandedText')
        if m.get('ViewOriginalText') is not None:
            self.view_original_text = m.get('ViewOriginalText')
        return self


class TableInput(TeaModel):
    def __init__(
        self,
        cascade: bool = None,
        create_time: int = None,
        created_by: str = None,
        database_name: str = None,
        last_access_time: int = None,
        last_analyzed_time: int = None,
        owner: str = None,
        owner_type: str = None,
        parameters: Dict[str, str] = None,
        partition_keys: List[FieldSchema] = None,
        privileges: PrincipalPrivilegeSet = None,
        retention: int = None,
        rewrite_enabled: bool = None,
        sd: StorageDescriptor = None,
        table_name: str = None,
        table_type: str = None,
        temporary: bool = None,
        view_expanded_text: str = None,
        view_original_text: str = None,
    ):
        self.cascade = cascade
        self.create_time = create_time
        self.created_by = created_by
        self.database_name = database_name
        self.last_access_time = last_access_time
        self.last_analyzed_time = last_analyzed_time
        self.owner = owner
        self.owner_type = owner_type
        self.parameters = parameters
        self.partition_keys = partition_keys
        self.privileges = privileges
        self.retention = retention
        self.rewrite_enabled = rewrite_enabled
        self.sd = sd
        self.table_name = table_name
        self.table_type = table_type
        self.temporary = temporary
        self.view_expanded_text = view_expanded_text
        self.view_original_text = view_original_text

    def validate(self):
        if self.partition_keys:
            for k in self.partition_keys:
                if k:
                    k.validate()
        if self.privileges:
            self.privileges.validate()
        if self.sd:
            self.sd.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cascade is not None:
            result['Cascade'] = self.cascade
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.last_access_time is not None:
            result['LastAccessTime'] = self.last_access_time
        if self.last_analyzed_time is not None:
            result['LastAnalyzedTime'] = self.last_analyzed_time
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.owner_type is not None:
            result['OwnerType'] = self.owner_type
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        result['PartitionKeys'] = []
        if self.partition_keys is not None:
            for k in self.partition_keys:
                result['PartitionKeys'].append(k.to_map() if k else None)
        if self.privileges is not None:
            result['Privileges'] = self.privileges.to_map()
        if self.retention is not None:
            result['Retention'] = self.retention
        if self.rewrite_enabled is not None:
            result['RewriteEnabled'] = self.rewrite_enabled
        if self.sd is not None:
            result['Sd'] = self.sd.to_map()
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.table_type is not None:
            result['TableType'] = self.table_type
        if self.temporary is not None:
            result['Temporary'] = self.temporary
        if self.view_expanded_text is not None:
            result['ViewExpandedText'] = self.view_expanded_text
        if self.view_original_text is not None:
            result['ViewOriginalText'] = self.view_original_text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cascade') is not None:
            self.cascade = m.get('Cascade')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('LastAccessTime') is not None:
            self.last_access_time = m.get('LastAccessTime')
        if m.get('LastAnalyzedTime') is not None:
            self.last_analyzed_time = m.get('LastAnalyzedTime')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('OwnerType') is not None:
            self.owner_type = m.get('OwnerType')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        self.partition_keys = []
        if m.get('PartitionKeys') is not None:
            for k in m.get('PartitionKeys'):
                temp_model = FieldSchema()
                self.partition_keys.append(temp_model.from_map(k))
        if m.get('Privileges') is not None:
            temp_model = PrincipalPrivilegeSet()
            self.privileges = temp_model.from_map(m['Privileges'])
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        if m.get('RewriteEnabled') is not None:
            self.rewrite_enabled = m.get('RewriteEnabled')
        if m.get('Sd') is not None:
            temp_model = StorageDescriptor()
            self.sd = temp_model.from_map(m['Sd'])
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('TableType') is not None:
            self.table_type = m.get('TableType')
        if m.get('Temporary') is not None:
            self.temporary = m.get('Temporary')
        if m.get('ViewExpandedText') is not None:
            self.view_expanded_text = m.get('ViewExpandedText')
        if m.get('ViewOriginalText') is not None:
            self.view_original_text = m.get('ViewOriginalText')
        return self


class TaskStatus(TeaModel):
    def __init__(
        self,
        message: str = None,
        status: str = None,
    ):
        self.message = message
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UnarchiveDetail(TeaModel):
    def __init__(
        self,
        api_call_times: int = None,
        cost: int = None,
        storage_size: int = None,
        storage_type: str = None,
        unarchive_task_status: str = None,
    ):
        self.api_call_times = api_call_times
        self.cost = cost
        self.storage_size = storage_size
        self.storage_type = storage_type
        self.unarchive_task_status = unarchive_task_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_call_times is not None:
            result['ApiCallTimes'] = self.api_call_times
        if self.cost is not None:
            result['Cost'] = self.cost
        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.unarchive_task_status is not None:
            result['UnarchiveTaskStatus'] = self.unarchive_task_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiCallTimes') is not None:
            self.api_call_times = m.get('ApiCallTimes')
        if m.get('Cost') is not None:
            self.cost = m.get('Cost')
        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('UnarchiveTaskStatus') is not None:
            self.unarchive_task_status = m.get('UnarchiveTaskStatus')
        return self


class UpdateTablePartitionColumnStatisticsRequest(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        column_statistics_list: List[ColumnStatistics] = None,
        database_name: str = None,
        engine: str = None,
        is_stats_compliant: bool = None,
        table_name: str = None,
        valid_write_id_list: str = None,
        write_id: str = None,
    ):
        self.catalog_id = catalog_id
        self.column_statistics_list = column_statistics_list
        self.database_name = database_name
        self.engine = engine
        self.is_stats_compliant = is_stats_compliant
        self.table_name = table_name
        self.valid_write_id_list = valid_write_id_list
        self.write_id = write_id

    def validate(self):
        if self.column_statistics_list:
            for k in self.column_statistics_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        result['ColumnStatisticsList'] = []
        if self.column_statistics_list is not None:
            for k in self.column_statistics_list:
                result['ColumnStatisticsList'].append(k.to_map() if k else None)
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.is_stats_compliant is not None:
            result['IsStatsCompliant'] = self.is_stats_compliant
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.valid_write_id_list is not None:
            result['ValidWriteIdList'] = self.valid_write_id_list
        if self.write_id is not None:
            result['WriteId'] = self.write_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        self.column_statistics_list = []
        if m.get('ColumnStatisticsList') is not None:
            for k in m.get('ColumnStatisticsList'):
                temp_model = ColumnStatistics()
                self.column_statistics_list.append(temp_model.from_map(k))
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('IsStatsCompliant') is not None:
            self.is_stats_compliant = m.get('IsStatsCompliant')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('ValidWriteIdList') is not None:
            self.valid_write_id_list = m.get('ValidWriteIdList')
        if m.get('WriteId') is not None:
            self.write_id = m.get('WriteId')
        return self


class UserRole(TeaModel):
    def __init__(
        self,
        grant_time: int = None,
        role: Role = None,
        user: Principal = None,
    ):
        self.grant_time = grant_time
        self.role = role
        self.user = user

    def validate(self):
        if self.role:
            self.role.validate()
        if self.user:
            self.user.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.grant_time is not None:
            result['GrantTime'] = self.grant_time
        if self.role is not None:
            result['Role'] = self.role.to_map()
        if self.user is not None:
            result['User'] = self.user.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GrantTime') is not None:
            self.grant_time = m.get('GrantTime')
        if m.get('Role') is not None:
            temp_model = Role()
            self.role = temp_model.from_map(m['Role'])
        if m.get('User') is not None:
            temp_model = Principal()
            self.user = temp_model.from_map(m['User'])
        return self


class AbortLockRequest(TeaModel):
    def __init__(
        self,
        lock_id: int = None,
    ):
        # LockId
        self.lock_id = lock_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lock_id is not None:
            result['LockId'] = self.lock_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LockId') is not None:
            self.lock_id = m.get('LockId')
        return self


class AbortLockResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Code
        self.code = code
        # Message
        self.message = message
        # RequestId
        self.request_id = request_id
        # Success
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AbortLockResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AbortLockResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = AbortLockResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchCreatePartitionsRequest(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        database_name: str = None,
        if_not_exists: bool = None,
        need_result: bool = None,
        partition_inputs: List[PartitionInput] = None,
        table_name: str = None,
    ):
        self.catalog_id = catalog_id
        self.database_name = database_name
        self.if_not_exists = if_not_exists
        self.need_result = need_result
        self.partition_inputs = partition_inputs
        self.table_name = table_name

    def validate(self):
        if self.partition_inputs:
            for k in self.partition_inputs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.if_not_exists is not None:
            result['IfNotExists'] = self.if_not_exists
        if self.need_result is not None:
            result['NeedResult'] = self.need_result
        result['PartitionInputs'] = []
        if self.partition_inputs is not None:
            for k in self.partition_inputs:
                result['PartitionInputs'].append(k.to_map() if k else None)
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('IfNotExists') is not None:
            self.if_not_exists = m.get('IfNotExists')
        if m.get('NeedResult') is not None:
            self.need_result = m.get('NeedResult')
        self.partition_inputs = []
        if m.get('PartitionInputs') is not None:
            for k in m.get('PartitionInputs'):
                temp_model = PartitionInput()
                self.partition_inputs.append(temp_model.from_map(k))
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class BatchCreatePartitionsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        partition_errors: List[PartitionError] = None,
        partitions: List[Partition] = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.partition_errors = partition_errors
        self.partitions = partitions
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.partition_errors:
            for k in self.partition_errors:
                if k:
                    k.validate()
        if self.partitions:
            for k in self.partitions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        result['PartitionErrors'] = []
        if self.partition_errors is not None:
            for k in self.partition_errors:
                result['PartitionErrors'].append(k.to_map() if k else None)
        result['Partitions'] = []
        if self.partitions is not None:
            for k in self.partitions:
                result['Partitions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.partition_errors = []
        if m.get('PartitionErrors') is not None:
            for k in m.get('PartitionErrors'):
                temp_model = PartitionError()
                self.partition_errors.append(temp_model.from_map(k))
        self.partitions = []
        if m.get('Partitions') is not None:
            for k in m.get('Partitions'):
                temp_model = Partition()
                self.partitions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BatchCreatePartitionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchCreatePartitionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = BatchCreatePartitionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchCreateTablesRequest(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        database_name: str = None,
        if_not_exists: bool = None,
        table_inputs: List[TableInput] = None,
    ):
        self.catalog_id = catalog_id
        self.database_name = database_name
        self.if_not_exists = if_not_exists
        self.table_inputs = table_inputs

    def validate(self):
        if self.table_inputs:
            for k in self.table_inputs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.if_not_exists is not None:
            result['IfNotExists'] = self.if_not_exists
        result['TableInputs'] = []
        if self.table_inputs is not None:
            for k in self.table_inputs:
                result['TableInputs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('IfNotExists') is not None:
            self.if_not_exists = m.get('IfNotExists')
        self.table_inputs = []
        if m.get('TableInputs') is not None:
            for k in m.get('TableInputs'):
                temp_model = TableInput()
                self.table_inputs.append(temp_model.from_map(k))
        return self


class BatchCreateTablesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        table_errors: List[TableError] = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.table_errors = table_errors

    def validate(self):
        if self.table_errors:
            for k in self.table_errors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        result['TableErrors'] = []
        if self.table_errors is not None:
            for k in self.table_errors:
                result['TableErrors'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.table_errors = []
        if m.get('TableErrors') is not None:
            for k in m.get('TableErrors'):
                temp_model = TableError()
                self.table_errors.append(temp_model.from_map(k))
        return self


class BatchCreateTablesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchCreateTablesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = BatchCreateTablesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchDeletePartitionsRequestPartitionValueList(TeaModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class BatchDeletePartitionsRequest(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        database_name: str = None,
        if_exists: bool = None,
        partition_value_list: List[BatchDeletePartitionsRequestPartitionValueList] = None,
        table_name: str = None,
    ):
        self.catalog_id = catalog_id
        self.database_name = database_name
        self.if_exists = if_exists
        self.partition_value_list = partition_value_list
        self.table_name = table_name

    def validate(self):
        if self.partition_value_list:
            for k in self.partition_value_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.if_exists is not None:
            result['IfExists'] = self.if_exists
        result['PartitionValueList'] = []
        if self.partition_value_list is not None:
            for k in self.partition_value_list:
                result['PartitionValueList'].append(k.to_map() if k else None)
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('IfExists') is not None:
            self.if_exists = m.get('IfExists')
        self.partition_value_list = []
        if m.get('PartitionValueList') is not None:
            for k in m.get('PartitionValueList'):
                temp_model = BatchDeletePartitionsRequestPartitionValueList()
                self.partition_value_list.append(temp_model.from_map(k))
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class BatchDeletePartitionsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        partition_errors: List[PartitionError] = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.partition_errors = partition_errors
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.partition_errors:
            for k in self.partition_errors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        result['PartitionErrors'] = []
        if self.partition_errors is not None:
            for k in self.partition_errors:
                result['PartitionErrors'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.partition_errors = []
        if m.get('PartitionErrors') is not None:
            for k in m.get('PartitionErrors'):
                temp_model = PartitionError()
                self.partition_errors.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BatchDeletePartitionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchDeletePartitionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = BatchDeletePartitionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchDeleteTableVersionsRequest(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        database_name: str = None,
        table_name: str = None,
        version_ids: List[int] = None,
    ):
        self.catalog_id = catalog_id
        self.database_name = database_name
        self.table_name = table_name
        self.version_ids = version_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.version_ids is not None:
            result['VersionIds'] = self.version_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('VersionIds') is not None:
            self.version_ids = m.get('VersionIds')
        return self


class BatchDeleteTableVersionsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BatchDeleteTableVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchDeleteTableVersionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = BatchDeleteTableVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchDeleteTablesRequest(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        database_name: str = None,
        if_exists: bool = None,
        table_names: List[str] = None,
    ):
        self.catalog_id = catalog_id
        self.database_name = database_name
        # IfExists
        self.if_exists = if_exists
        self.table_names = table_names

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.if_exists is not None:
            result['IfExists'] = self.if_exists
        if self.table_names is not None:
            result['TableNames'] = self.table_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('IfExists') is not None:
            self.if_exists = m.get('IfExists')
        if m.get('TableNames') is not None:
            self.table_names = m.get('TableNames')
        return self


class BatchDeleteTablesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        table_errors: List[TableError] = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.table_errors = table_errors

    def validate(self):
        if self.table_errors:
            for k in self.table_errors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        result['TableErrors'] = []
        if self.table_errors is not None:
            for k in self.table_errors:
                result['TableErrors'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.table_errors = []
        if m.get('TableErrors') is not None:
            for k in m.get('TableErrors'):
                temp_model = TableError()
                self.table_errors.append(temp_model.from_map(k))
        return self


class BatchDeleteTablesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchDeleteTablesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = BatchDeleteTablesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchGetPartitionColumnStatisticsRequest(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        column_names: List[str] = None,
        database_name: str = None,
        partition_names: List[str] = None,
        table_name: str = None,
    ):
        self.catalog_id = catalog_id
        self.column_names = column_names
        self.database_name = database_name
        self.partition_names = partition_names
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.column_names is not None:
            result['ColumnNames'] = self.column_names
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.partition_names is not None:
            result['PartitionNames'] = self.partition_names
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('ColumnNames') is not None:
            self.column_names = m.get('ColumnNames')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('PartitionNames') is not None:
            self.partition_names = m.get('PartitionNames')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class BatchGetPartitionColumnStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        partition_statistics_map: Dict[str, List[ColumnStatisticsObj]] = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.partition_statistics_map = partition_statistics_map
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.partition_statistics_map:
            for v in self.partition_statistics_map.values():
                for k1 in v:
                    if k1:
                        k1.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        result['PartitionStatisticsMap'] = {}
        if self.partition_statistics_map is not None:
            for k, v in self.partition_statistics_map.items():
                l1 = []
                for k1 in v:
                    l1.append(k1.to_map() if k1 else None)
                result['partitionStatisticsMap'][k] = l1
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.partition_statistics_map = {}
        if m.get('PartitionStatisticsMap') is not None:
            for k, v in m.get('PartitionStatisticsMap').items():
                l1 = []
                for k1 in v:
                    temp_model = ColumnStatisticsObj()
                    l1.append(temp_model.from_map(k1))
                self.partition_statistics_map['k'] = l1
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BatchGetPartitionColumnStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchGetPartitionColumnStatisticsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = BatchGetPartitionColumnStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchGetPartitionsRequestPartitionValueList(TeaModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class BatchGetPartitionsRequest(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        database_name: str = None,
        is_share_sd: bool = None,
        partition_value_list: List[BatchGetPartitionsRequestPartitionValueList] = None,
        table_name: str = None,
    ):
        self.catalog_id = catalog_id
        self.database_name = database_name
        self.is_share_sd = is_share_sd
        self.partition_value_list = partition_value_list
        self.table_name = table_name

    def validate(self):
        if self.partition_value_list:
            for k in self.partition_value_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.is_share_sd is not None:
            result['IsShareSd'] = self.is_share_sd
        result['PartitionValueList'] = []
        if self.partition_value_list is not None:
            for k in self.partition_value_list:
                result['PartitionValueList'].append(k.to_map() if k else None)
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('IsShareSd') is not None:
            self.is_share_sd = m.get('IsShareSd')
        self.partition_value_list = []
        if m.get('PartitionValueList') is not None:
            for k in m.get('PartitionValueList'):
                temp_model = BatchGetPartitionsRequestPartitionValueList()
                self.partition_value_list.append(temp_model.from_map(k))
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class BatchGetPartitionsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        partition_errors: List[PartitionError] = None,
        partition_specs: List[PartitionSpec] = None,
        partitions: List[Partition] = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.partition_errors = partition_errors
        self.partition_specs = partition_specs
        self.partitions = partitions
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.partition_errors:
            for k in self.partition_errors:
                if k:
                    k.validate()
        if self.partition_specs:
            for k in self.partition_specs:
                if k:
                    k.validate()
        if self.partitions:
            for k in self.partitions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        result['PartitionErrors'] = []
        if self.partition_errors is not None:
            for k in self.partition_errors:
                result['PartitionErrors'].append(k.to_map() if k else None)
        result['PartitionSpecs'] = []
        if self.partition_specs is not None:
            for k in self.partition_specs:
                result['PartitionSpecs'].append(k.to_map() if k else None)
        result['Partitions'] = []
        if self.partitions is not None:
            for k in self.partitions:
                result['Partitions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.partition_errors = []
        if m.get('PartitionErrors') is not None:
            for k in m.get('PartitionErrors'):
                temp_model = PartitionError()
                self.partition_errors.append(temp_model.from_map(k))
        self.partition_specs = []
        if m.get('PartitionSpecs') is not None:
            for k in m.get('PartitionSpecs'):
                temp_model = PartitionSpec()
                self.partition_specs.append(temp_model.from_map(k))
        self.partitions = []
        if m.get('Partitions') is not None:
            for k in m.get('Partitions'):
                temp_model = Partition()
                self.partitions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BatchGetPartitionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchGetPartitionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = BatchGetPartitionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchGetTablesRequest(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        database_name: str = None,
        table_names: List[str] = None,
    ):
        self.catalog_id = catalog_id
        self.database_name = database_name
        self.table_names = table_names

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.table_names is not None:
            result['TableNames'] = self.table_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('TableNames') is not None:
            self.table_names = m.get('TableNames')
        return self


class BatchGetTablesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        table_errors: List[TableError] = None,
        tables: List[Table] = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.table_errors = table_errors
        self.tables = tables

    def validate(self):
        if self.table_errors:
            for k in self.table_errors:
                if k:
                    k.validate()
        if self.tables:
            for k in self.tables:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        result['TableErrors'] = []
        if self.table_errors is not None:
            for k in self.table_errors:
                result['TableErrors'].append(k.to_map() if k else None)
        result['Tables'] = []
        if self.tables is not None:
            for k in self.tables:
                result['Tables'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.table_errors = []
        if m.get('TableErrors') is not None:
            for k in m.get('TableErrors'):
                temp_model = TableError()
                self.table_errors.append(temp_model.from_map(k))
        self.tables = []
        if m.get('Tables') is not None:
            for k in m.get('Tables'):
                temp_model = Table()
                self.tables.append(temp_model.from_map(k))
        return self


class BatchGetTablesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchGetTablesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = BatchGetTablesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchGrantPermissionsRequest(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        grant_revoke_entries: List[GrantRevokeEntry] = None,
        type: str = None,
    ):
        # catalogId
        self.catalog_id = catalog_id
        self.grant_revoke_entries = grant_revoke_entries
        self.type = type

    def validate(self):
        if self.grant_revoke_entries:
            for k in self.grant_revoke_entries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        result['GrantRevokeEntries'] = []
        if self.grant_revoke_entries is not None:
            for k in self.grant_revoke_entries:
                result['GrantRevokeEntries'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        self.grant_revoke_entries = []
        if m.get('GrantRevokeEntries') is not None:
            for k in m.get('GrantRevokeEntries'):
                temp_model = GrantRevokeEntry()
                self.grant_revoke_entries.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class BatchGrantPermissionsResponseBody(TeaModel):
    def __init__(
        self,
        batch_grant_revoke_failure_result: List[GrantRevokeFailureEntry] = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # result
        self.batch_grant_revoke_failure_result = batch_grant_revoke_failure_result
        # Response Code
        self.code = code
        # Message
        self.message = message
        # RequestId
        self.request_id = request_id
        # Success
        self.success = success

    def validate(self):
        if self.batch_grant_revoke_failure_result:
            for k in self.batch_grant_revoke_failure_result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BatchGrantRevokeFailureResult'] = []
        if self.batch_grant_revoke_failure_result is not None:
            for k in self.batch_grant_revoke_failure_result:
                result['BatchGrantRevokeFailureResult'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.batch_grant_revoke_failure_result = []
        if m.get('BatchGrantRevokeFailureResult') is not None:
            for k in m.get('BatchGrantRevokeFailureResult'):
                temp_model = GrantRevokeFailureEntry()
                self.batch_grant_revoke_failure_result.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        catalog_id: str = None,
        grant_revoke_entries: List[GrantRevokeEntry] = None,
        type: str = None,
    ):
        # catalogId
        self.catalog_id = catalog_id
        self.grant_revoke_entries = grant_revoke_entries
        self.type = type

    def validate(self):
        if self.grant_revoke_entries:
            for k in self.grant_revoke_entries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        result['GrantRevokeEntries'] = []
        if self.grant_revoke_entries is not None:
            for k in self.grant_revoke_entries:
                result['GrantRevokeEntries'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        self.grant_revoke_entries = []
        if m.get('GrantRevokeEntries') is not None:
            for k in m.get('GrantRevokeEntries'):
                temp_model = GrantRevokeEntry()
                self.grant_revoke_entries.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class BatchRevokePermissionsResponseBody(TeaModel):
    def __init__(
        self,
        batch_grant_revoke_failure_result: List[GrantRevokeFailureEntry] = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # result
        self.batch_grant_revoke_failure_result = batch_grant_revoke_failure_result
        # Response Code
        self.code = code
        # Message Code
        self.message = message
        # RequestId
        self.request_id = request_id
        # Success
        self.success = success

    def validate(self):
        if self.batch_grant_revoke_failure_result:
            for k in self.batch_grant_revoke_failure_result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BatchGrantRevokeFailureResult'] = []
        if self.batch_grant_revoke_failure_result is not None:
            for k in self.batch_grant_revoke_failure_result:
                result['BatchGrantRevokeFailureResult'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.batch_grant_revoke_failure_result = []
        if m.get('BatchGrantRevokeFailureResult') is not None:
            for k in m.get('BatchGrantRevokeFailureResult'):
                temp_model = GrantRevokeFailureEntry()
                self.batch_grant_revoke_failure_result.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class BatchUpdatePartitionsRequest(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        database_name: str = None,
        partition_inputs: List[PartitionInput] = None,
        table_name: str = None,
    ):
        self.catalog_id = catalog_id
        self.database_name = database_name
        self.partition_inputs = partition_inputs
        self.table_name = table_name

    def validate(self):
        if self.partition_inputs:
            for k in self.partition_inputs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        result['PartitionInputs'] = []
        if self.partition_inputs is not None:
            for k in self.partition_inputs:
                result['PartitionInputs'].append(k.to_map() if k else None)
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        self.partition_inputs = []
        if m.get('PartitionInputs') is not None:
            for k in m.get('PartitionInputs'):
                temp_model = PartitionInput()
                self.partition_inputs.append(temp_model.from_map(k))
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class BatchUpdatePartitionsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        partition_errors: List[PartitionError] = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.partition_errors = partition_errors
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.partition_errors:
            for k in self.partition_errors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        result['PartitionErrors'] = []
        if self.partition_errors is not None:
            for k in self.partition_errors:
                result['PartitionErrors'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.partition_errors = []
        if m.get('PartitionErrors') is not None:
            for k in m.get('PartitionErrors'):
                temp_model = PartitionError()
                self.partition_errors.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BatchUpdatePartitionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchUpdatePartitionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = BatchUpdatePartitionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchUpdateTablesRequest(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        database_name: str = None,
        is_async: bool = None,
        table_inputs: List[TableInput] = None,
    ):
        self.catalog_id = catalog_id
        self.database_name = database_name
        self.is_async = is_async
        self.table_inputs = table_inputs

    def validate(self):
        if self.table_inputs:
            for k in self.table_inputs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.is_async is not None:
            result['IsAsync'] = self.is_async
        result['TableInputs'] = []
        if self.table_inputs is not None:
            for k in self.table_inputs:
                result['TableInputs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('IsAsync') is not None:
            self.is_async = m.get('IsAsync')
        self.table_inputs = []
        if m.get('TableInputs') is not None:
            for k in m.get('TableInputs'):
                temp_model = TableInput()
                self.table_inputs.append(temp_model.from_map(k))
        return self


class BatchUpdateTablesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        table_errors: List[TableError] = None,
        task_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.table_errors = table_errors
        self.task_id = task_id

    def validate(self):
        if self.table_errors:
            for k in self.table_errors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        result['TableErrors'] = []
        if self.table_errors is not None:
            for k in self.table_errors:
                result['TableErrors'].append(k.to_map() if k else None)
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.table_errors = []
        if m.get('TableErrors') is not None:
            for k in m.get('TableErrors'):
                temp_model = TableError()
                self.table_errors.append(temp_model.from_map(k))
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class BatchUpdateTablesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchUpdateTablesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = BatchUpdateTablesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelQueryRequest(TeaModel):
    def __init__(
        self,
        query_id: str = None,
    ):
        self.query_id = query_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.query_id is not None:
            result['QueryId'] = self.query_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QueryId') is not None:
            self.query_id = m.get('QueryId')
        return self


class CancelQueryResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CancelQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelQueryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CancelQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckPermissionsRequest(TeaModel):
    def __init__(
        self,
        body: AccessRequest = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = AccessRequest()
            self.body = temp_model.from_map(m['Body'])
        return self


class CheckPermissionsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Response Code
        self.code = code
        # Message Code
        self.message = message
        # RequestId
        self.request_id = request_id
        # Success
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckPermissionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckPermissionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CheckPermissionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCatalogRequest(TeaModel):
    def __init__(
        self,
        catalog_input: CatalogInput = None,
    ):
        # cataloginput
        self.catalog_input = catalog_input

    def validate(self):
        if self.catalog_input:
            self.catalog_input.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_input is not None:
            result['CatalogInput'] = self.catalog_input.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogInput') is not None:
            temp_model = CatalogInput()
            self.catalog_input = temp_model.from_map(m['CatalogInput'])
        return self


class CreateCatalogResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Response Code
        self.code = code
        # Response Message
        self.message = message
        # RequestId
        self.request_id = request_id
        # Success
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateCatalogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCatalogResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateCatalogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDatabaseRequest(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        database_input: DatabaseInput = None,
    ):
        self.catalog_id = catalog_id
        self.database_input = database_input

    def validate(self):
        if self.database_input:
            self.database_input.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.database_input is not None:
            result['DatabaseInput'] = self.database_input.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('DatabaseInput') is not None:
            temp_model = DatabaseInput()
            self.database_input = temp_model.from_map(m['DatabaseInput'])
        return self


class CreateDatabaseResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateDatabaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDatabaseResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateDatabaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFunctionRequest(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        database_name: str = None,
        function_input: FunctionInput = None,
    ):
        self.catalog_id = catalog_id
        self.database_name = database_name
        self.function_input = function_input

    def validate(self):
        if self.function_input:
            self.function_input.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.function_input is not None:
            result['FunctionInput'] = self.function_input.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('FunctionInput') is not None:
            temp_model = FunctionInput()
            self.function_input = temp_model.from_map(m['FunctionInput'])
        return self


class CreateFunctionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateFunctionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFunctionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateFunctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLockRequest(TeaModel):
    def __init__(
        self,
        lock_obj_list: List[LockObj] = None,
    ):
        # LockObjList
        self.lock_obj_list = lock_obj_list

    def validate(self):
        if self.lock_obj_list:
            for k in self.lock_obj_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LockObjList'] = []
        if self.lock_obj_list is not None:
            for k in self.lock_obj_list:
                result['LockObjList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.lock_obj_list = []
        if m.get('LockObjList') is not None:
            for k in m.get('LockObjList'):
                temp_model = LockObj()
                self.lock_obj_list.append(temp_model.from_map(k))
        return self


class CreateLockResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        lock_status: LockStatus = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Code
        self.code = code
        self.lock_status = lock_status
        # Message
        self.message = message
        # RequestId
        self.request_id = request_id
        # Success
        self.success = success

    def validate(self):
        if self.lock_status:
            self.lock_status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.lock_status is not None:
            result['LockStatus'] = self.lock_status.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LockStatus') is not None:
            temp_model = LockStatus()
            self.lock_status = temp_model.from_map(m['LockStatus'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateLockResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateLockResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateLockResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePartitionRequest(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        database_name: str = None,
        if_not_exists: bool = None,
        need_result: bool = None,
        partition_input: PartitionInput = None,
        table_name: str = None,
    ):
        self.catalog_id = catalog_id
        self.database_name = database_name
        self.if_not_exists = if_not_exists
        self.need_result = need_result
        self.partition_input = partition_input
        self.table_name = table_name

    def validate(self):
        if self.partition_input:
            self.partition_input.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.if_not_exists is not None:
            result['IfNotExists'] = self.if_not_exists
        if self.need_result is not None:
            result['NeedResult'] = self.need_result
        if self.partition_input is not None:
            result['PartitionInput'] = self.partition_input.to_map()
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('IfNotExists') is not None:
            self.if_not_exists = m.get('IfNotExists')
        if m.get('NeedResult') is not None:
            self.need_result = m.get('NeedResult')
        if m.get('PartitionInput') is not None:
            temp_model = PartitionInput()
            self.partition_input = temp_model.from_map(m['PartitionInput'])
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class CreatePartitionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        partition: Partition = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.partition = partition
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.partition:
            self.partition.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.partition is not None:
            result['Partition'] = self.partition.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Partition') is not None:
            temp_model = Partition()
            self.partition = temp_model.from_map(m['Partition'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreatePartitionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatePartitionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreatePartitionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRoleRequest(TeaModel):
    def __init__(
        self,
        body: RoleInput = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = RoleInput()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRoleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # code
        self.code = code
        # message
        self.message = message
        # RequestId
        self.request_id = request_id
        # success
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateRoleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTableRequest(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        database_name: str = None,
        table_input: TableInput = None,
    ):
        self.catalog_id = catalog_id
        self.database_name = database_name
        self.table_input = table_input

    def validate(self):
        if self.table_input:
            self.table_input.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.table_input is not None:
            result['TableInput'] = self.table_input.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('TableInput') is not None:
            temp_model = TableInput()
            self.table_input = temp_model.from_map(m['TableInput'])
        return self


class CreateTableResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateTableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTableResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCatalogRequest(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        is_async: bool = None,
    ):
        # CatalogId
        self.catalog_id = catalog_id
        self.is_async = is_async

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.is_async is not None:
            result['IsAsync'] = self.is_async
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('IsAsync') is not None:
            self.is_async = m.get('IsAsync')
        return self


class DeleteCatalogResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        # Response Code
        self.code = code
        # Response Message
        self.message = message
        # RequestId
        self.request_id = request_id
        # Request is success or not
        self.success = success
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DeleteCatalogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCatalogResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteCatalogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDatabaseRequest(TeaModel):
    def __init__(
        self,
        cascade: bool = None,
        catalog_id: str = None,
        name: str = None,
    ):
        self.cascade = cascade
        self.catalog_id = catalog_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cascade is not None:
            result['Cascade'] = self.cascade
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cascade') is not None:
            self.cascade = m.get('Cascade')
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DeleteDatabaseResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteDatabaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDatabaseResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteDatabaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFunctionRequest(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        database_name: str = None,
        function_name: str = None,
    ):
        self.catalog_id = catalog_id
        self.database_name = database_name
        self.function_name = function_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        return self


class DeleteFunctionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteFunctionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteFunctionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteFunctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePartitionRequest(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        database_name: str = None,
        if_exists: bool = None,
        partition_values: List[str] = None,
        table_name: str = None,
    ):
        self.catalog_id = catalog_id
        self.database_name = database_name
        self.if_exists = if_exists
        self.partition_values = partition_values
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.if_exists is not None:
            result['IfExists'] = self.if_exists
        if self.partition_values is not None:
            result['PartitionValues'] = self.partition_values
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('IfExists') is not None:
            self.if_exists = m.get('IfExists')
        if m.get('PartitionValues') is not None:
            self.partition_values = m.get('PartitionValues')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DeletePartitionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeletePartitionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeletePartitionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeletePartitionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePartitionColumnStatisticsRequest(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        column_names: List[str] = None,
        database_name: str = None,
        partition_names: List[str] = None,
        table_name: str = None,
    ):
        self.catalog_id = catalog_id
        self.column_names = column_names
        self.database_name = database_name
        self.partition_names = partition_names
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.column_names is not None:
            result['ColumnNames'] = self.column_names
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.partition_names is not None:
            result['PartitionNames'] = self.partition_names
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('ColumnNames') is not None:
            self.column_names = m.get('ColumnNames')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('PartitionNames') is not None:
            self.partition_names = m.get('PartitionNames')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DeletePartitionColumnStatisticsShrinkRequest(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        column_names_shrink: str = None,
        database_name: str = None,
        partition_names_shrink: str = None,
        table_name: str = None,
    ):
        self.catalog_id = catalog_id
        self.column_names_shrink = column_names_shrink
        self.database_name = database_name
        self.partition_names_shrink = partition_names_shrink
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.column_names_shrink is not None:
            result['ColumnNames'] = self.column_names_shrink
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.partition_names_shrink is not None:
            result['PartitionNames'] = self.partition_names_shrink
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('ColumnNames') is not None:
            self.column_names_shrink = m.get('ColumnNames')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('PartitionNames') is not None:
            self.partition_names_shrink = m.get('PartitionNames')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DeletePartitionColumnStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeletePartitionColumnStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeletePartitionColumnStatisticsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeletePartitionColumnStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRoleRequest(TeaModel):
    def __init__(
        self,
        role_name: str = None,
    ):
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class DeleteRoleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # code
        self.code = code
        # message
        self.message = message
        # requestId
        self.request_id = request_id
        # success
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteRoleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTableRequest(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        database_name: str = None,
        table_name: str = None,
    ):
        self.catalog_id = catalog_id
        self.database_name = database_name
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DeleteTableResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteTableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteTableResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTableColumnStatisticsRequest(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        column_names: List[str] = None,
        database_name: str = None,
        table_name: str = None,
    ):
        self.catalog_id = catalog_id
        self.column_names = column_names
        self.database_name = database_name
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.column_names is not None:
            result['ColumnNames'] = self.column_names
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('ColumnNames') is not None:
            self.column_names = m.get('ColumnNames')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DeleteTableColumnStatisticsShrinkRequest(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        column_names_shrink: str = None,
        database_name: str = None,
        table_name: str = None,
    ):
        self.catalog_id = catalog_id
        self.column_names_shrink = column_names_shrink
        self.database_name = database_name
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.column_names_shrink is not None:
            result['ColumnNames'] = self.column_names_shrink
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('ColumnNames') is not None:
            self.column_names_shrink = m.get('ColumnNames')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DeleteTableColumnStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteTableColumnStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteTableColumnStatisticsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteTableColumnStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTableVersionRequest(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        database_name: str = None,
        table_name: str = None,
        version_id: int = None,
    ):
        self.catalog_id = catalog_id
        self.database_name = database_name
        self.table_name = table_name
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class DeleteTableVersionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteTableVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteTableVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteTableVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeregisterLocationRequest(TeaModel):
    def __init__(
        self,
        location_id: str = None,
    ):
        self.location_id = location_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.location_id is not None:
            result['LocationId'] = self.location_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocationId') is not None:
            self.location_id = m.get('LocationId')
        return self


class DeregisterLocationResponseBodyData(TeaModel):
    def __init__(
        self,
        location_id: str = None,
        storage_collect_task_operation_result_list: List[StorageCollectTaskOperationResult] = None,
    ):
        # Location ID
        self.location_id = location_id
        self.storage_collect_task_operation_result_list = storage_collect_task_operation_result_list

    def validate(self):
        if self.storage_collect_task_operation_result_list:
            for k in self.storage_collect_task_operation_result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.location_id is not None:
            result['LocationId'] = self.location_id
        result['StorageCollectTaskOperationResultList'] = []
        if self.storage_collect_task_operation_result_list is not None:
            for k in self.storage_collect_task_operation_result_list:
                result['StorageCollectTaskOperationResultList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocationId') is not None:
            self.location_id = m.get('LocationId')
        self.storage_collect_task_operation_result_list = []
        if m.get('StorageCollectTaskOperationResultList') is not None:
            for k in m.get('StorageCollectTaskOperationResultList'):
                temp_model = StorageCollectTaskOperationResult()
                self.storage_collect_task_operation_result_list.append(temp_model.from_map(k))
        return self


class DeregisterLocationResponseBody(TeaModel):
    def __init__(
        self,
        data: DeregisterLocationResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DeregisterLocationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeregisterLocationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeregisterLocationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeregisterLocationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        show_name: str = None,
        type: str = None,
    ):
        self.description = description
        self.name = name
        self.show_name = show_name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.show_name is not None:
            result['ShowName'] = self.show_name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ShowName') is not None:
            self.show_name = m.get('ShowName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        regions: List[DescribeRegionsResponseBodyRegions] = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.regions = regions
        self.request_id = request_id
        self.success = success

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
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = DescribeRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class GetAsyncTaskStatusRequest(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        task_id: str = None,
    ):
        self.catalog_id = catalog_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetAsyncTaskStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_status: TaskStatus = None,
    ):
        # Code
        self.code = code
        # Message
        self.message = message
        # RequestId
        self.request_id = request_id
        # Success
        self.success = success
        self.task_status = task_status

    def validate(self):
        if self.task_status:
            self.task_status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskStatus') is not None:
            temp_model = TaskStatus()
            self.task_status = temp_model.from_map(m['TaskStatus'])
        return self


class GetAsyncTaskStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAsyncTaskStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetAsyncTaskStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCatalogRequest(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
    ):
        # catalogId
        self.catalog_id = catalog_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        return self


class GetCatalogResponseBody(TeaModel):
    def __init__(
        self,
        catalog: Catalog = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.catalog = catalog
        # Code
        self.code = code
        # Message
        self.message = message
        # RequestId
        self.request_id = request_id
        # Success
        self.success = success

    def validate(self):
        if self.catalog:
            self.catalog.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog is not None:
            result['Catalog'] = self.catalog.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Catalog') is not None:
            temp_model = Catalog()
            self.catalog = temp_model.from_map(m['Catalog'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetCatalogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCatalogResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetCatalogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCatalogSettingsRequest(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
    ):
        self.catalog_id = catalog_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        return self


class GetCatalogSettingsResponseBody(TeaModel):
    def __init__(
        self,
        catalog_settings: CatalogSettings = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.catalog_settings = catalog_settings
        # Code
        self.code = code
        # Message
        self.message = message
        # RequestId
        self.request_id = request_id
        # Success
        self.success = success

    def validate(self):
        if self.catalog_settings:
            self.catalog_settings.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_settings is not None:
            result['CatalogSettings'] = self.catalog_settings.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogSettings') is not None:
            temp_model = CatalogSettings()
            self.catalog_settings = temp_model.from_map(m['CatalogSettings'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetCatalogSettingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCatalogSettingsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetCatalogSettingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDatabaseRequest(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        name: str = None,
    ):
        self.catalog_id = catalog_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetDatabaseResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        database: Database = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.database = database
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.database:
            self.database.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.database is not None:
            result['Database'] = self.database.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Database') is not None:
            temp_model = Database()
            self.database = temp_model.from_map(m['Database'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetDatabaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDatabaseResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetDatabaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFunctionRequest(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        database_name: str = None,
        function_name: str = None,
    ):
        self.catalog_id = catalog_id
        self.database_name = database_name
        self.function_name = function_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        return self


class GetFunctionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        function: Function = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.function = function
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.function:
            self.function.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.function is not None:
            result['Function'] = self.function.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Function') is not None:
            temp_model = Function()
            self.function = temp_model.from_map(m['Function'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetFunctionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFunctionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetFunctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLockRequest(TeaModel):
    def __init__(
        self,
        lock_id: int = None,
    ):
        # LockId
        self.lock_id = lock_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lock_id is not None:
            result['LockId'] = self.lock_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LockId') is not None:
            self.lock_id = m.get('LockId')
        return self


class GetLockResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        lock_status: LockStatus = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Code
        self.code = code
        self.lock_status = lock_status
        # Message
        self.message = message
        # RequestId
        self.request_id = request_id
        # Success
        self.success = success

    def validate(self):
        if self.lock_status:
            self.lock_status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.lock_status is not None:
            result['LockStatus'] = self.lock_status.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LockStatus') is not None:
            temp_model = LockStatus()
            self.lock_status = temp_model.from_map(m['LockStatus'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetLockResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLockResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetLockResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPartitionRequest(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        database_name: str = None,
        partition_values: List[str] = None,
        table_name: str = None,
    ):
        self.catalog_id = catalog_id
        self.database_name = database_name
        self.partition_values = partition_values
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.partition_values is not None:
            result['PartitionValues'] = self.partition_values
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('PartitionValues') is not None:
            self.partition_values = m.get('PartitionValues')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class GetPartitionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        partition: Partition = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.partition = partition
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.partition:
            self.partition.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.partition is not None:
            result['Partition'] = self.partition.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Partition') is not None:
            temp_model = Partition()
            self.partition = temp_model.from_map(m['Partition'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetPartitionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPartitionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetPartitionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPartitionColumnStatisticsRequest(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        column_names: List[str] = None,
        database_name: str = None,
        partition_names: List[str] = None,
        table_name: str = None,
    ):
        self.catalog_id = catalog_id
        self.column_names = column_names
        self.database_name = database_name
        self.partition_names = partition_names
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.column_names is not None:
            result['ColumnNames'] = self.column_names
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.partition_names is not None:
            result['PartitionNames'] = self.partition_names
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('ColumnNames') is not None:
            self.column_names = m.get('ColumnNames')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('PartitionNames') is not None:
            self.partition_names = m.get('PartitionNames')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class GetPartitionColumnStatisticsShrinkRequest(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        column_names_shrink: str = None,
        database_name: str = None,
        partition_names_shrink: str = None,
        table_name: str = None,
    ):
        self.catalog_id = catalog_id
        self.column_names_shrink = column_names_shrink
        self.database_name = database_name
        self.partition_names_shrink = partition_names_shrink
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.column_names_shrink is not None:
            result['ColumnNames'] = self.column_names_shrink
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.partition_names_shrink is not None:
            result['PartitionNames'] = self.partition_names_shrink
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('ColumnNames') is not None:
            self.column_names_shrink = m.get('ColumnNames')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('PartitionNames') is not None:
            self.partition_names_shrink = m.get('PartitionNames')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class GetPartitionColumnStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        partition_statistics_map: Dict[str, List[ColumnStatisticsObj]] = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.partition_statistics_map = partition_statistics_map
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.partition_statistics_map:
            for v in self.partition_statistics_map.values():
                for k1 in v:
                    if k1:
                        k1.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        result['PartitionStatisticsMap'] = {}
        if self.partition_statistics_map is not None:
            for k, v in self.partition_statistics_map.items():
                l1 = []
                for k1 in v:
                    l1.append(k1.to_map() if k1 else None)
                result['partitionStatisticsMap'][k] = l1
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.partition_statistics_map = {}
        if m.get('PartitionStatisticsMap') is not None:
            for k, v in m.get('PartitionStatisticsMap').items():
                l1 = []
                for k1 in v:
                    temp_model = ColumnStatisticsObj()
                    l1.append(temp_model.from_map(k1))
                self.partition_statistics_map['k'] = l1
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetPartitionColumnStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPartitionColumnStatisticsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetPartitionColumnStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQueryResultRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        query_id: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.query_id = query_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_id is not None:
            result['QueryId'] = self.query_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryId') is not None:
            self.query_id = m.get('QueryId')
        return self


class GetQueryResultResponseBody(TeaModel):
    def __init__(
        self,
        duration: int = None,
        end_time: str = None,
        error_message: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: str = None,
        job_completed: bool = None,
        logs: str = None,
        owner: int = None,
        progress: int = None,
        region_id: str = None,
        request_id: str = None,
        result_tmp_db: str = None,
        result_tmp_table: str = None,
        row_count: int = None,
        row_count_over_limit: bool = None,
        rows: str = None,
        schema: str = None,
        sql: str = None,
        start_time: str = None,
        status: str = None,
        success: bool = None,
        total_bytes_processed: int = None,
    ):
        self.duration = duration
        self.end_time = end_time
        self.error_message = error_message
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.job_completed = job_completed
        self.logs = logs
        self.owner = owner
        self.progress = progress
        self.region_id = region_id
        self.request_id = request_id
        self.result_tmp_db = result_tmp_db
        self.result_tmp_table = result_tmp_table
        self.row_count = row_count
        self.row_count_over_limit = row_count_over_limit
        self.rows = rows
        self.schema = schema
        self.sql = sql
        self.start_time = start_time
        self.status = status
        self.success = success
        self.total_bytes_processed = total_bytes_processed

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.job_completed is not None:
            result['JobCompleted'] = self.job_completed
        if self.logs is not None:
            result['Logs'] = self.logs
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_tmp_db is not None:
            result['ResultTmpDb'] = self.result_tmp_db
        if self.result_tmp_table is not None:
            result['ResultTmpTable'] = self.result_tmp_table
        if self.row_count is not None:
            result['RowCount'] = self.row_count
        if self.row_count_over_limit is not None:
            result['RowCountOverLimit'] = self.row_count_over_limit
        if self.rows is not None:
            result['Rows'] = self.rows
        if self.schema is not None:
            result['Schema'] = self.schema
        if self.sql is not None:
            result['Sql'] = self.sql
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        if self.total_bytes_processed is not None:
            result['TotalBytesProcessed'] = self.total_bytes_processed
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('JobCompleted') is not None:
            self.job_completed = m.get('JobCompleted')
        if m.get('Logs') is not None:
            self.logs = m.get('Logs')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultTmpDb') is not None:
            self.result_tmp_db = m.get('ResultTmpDb')
        if m.get('ResultTmpTable') is not None:
            self.result_tmp_table = m.get('ResultTmpTable')
        if m.get('RowCount') is not None:
            self.row_count = m.get('RowCount')
        if m.get('RowCountOverLimit') is not None:
            self.row_count_over_limit = m.get('RowCountOverLimit')
        if m.get('Rows') is not None:
            self.rows = m.get('Rows')
        if m.get('Schema') is not None:
            self.schema = m.get('Schema')
        if m.get('Sql') is not None:
            self.sql = m.get('Sql')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalBytesProcessed') is not None:
            self.total_bytes_processed = m.get('TotalBytesProcessed')
        return self


class GetQueryResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetQueryResultResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetQueryResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRegionStatusRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetRegionStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        account_status: str = None,
        is_dependency_ready: bool = None,
        is_dlf_service_open: bool = None,
        region_id: str = None,
        region_status: str = None,
    ):
        self.account_status = account_status
        self.is_dependency_ready = is_dependency_ready
        self.is_dlf_service_open = is_dlf_service_open
        self.region_id = region_id
        self.region_status = region_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_status is not None:
            result['AccountStatus'] = self.account_status
        if self.is_dependency_ready is not None:
            result['IsDependencyReady'] = self.is_dependency_ready
        if self.is_dlf_service_open is not None:
            result['IsDlfServiceOpen'] = self.is_dlf_service_open
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region_status is not None:
            result['RegionStatus'] = self.region_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountStatus') is not None:
            self.account_status = m.get('AccountStatus')
        if m.get('IsDependencyReady') is not None:
            self.is_dependency_ready = m.get('IsDependencyReady')
        if m.get('IsDlfServiceOpen') is not None:
            self.is_dlf_service_open = m.get('IsDlfServiceOpen')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegionStatus') is not None:
            self.region_status = m.get('RegionStatus')
        return self


class GetRegionStatusResponseBody(TeaModel):
    def __init__(
        self,
        data: GetRegionStatusResponseBodyData = None,
        request_id: str = None,
        success: str = None,
    ):
        self.data = data
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetRegionStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        role_name: str = None,
    ):
        # roleName
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class GetRoleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        role: Role = None,
        success: bool = None,
    ):
        # code
        self.code = code
        # message
        self.message = message
        # requestId
        self.request_id = request_id
        # role
        self.role = role
        # success
        self.success = success

    def validate(self):
        if self.role:
            self.role.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.role is not None:
            result['Role'] = self.role.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Role') is not None:
            temp_model = Role()
            self.role = temp_model.from_map(m['Role'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRoleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceStatusRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetServiceStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        has_ram_permissions: bool = None,
        is_dlf_service_open: bool = None,
        is_oss_open: bool = None,
    ):
        self.has_ram_permissions = has_ram_permissions
        self.is_dlf_service_open = is_dlf_service_open
        self.is_oss_open = is_oss_open

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_ram_permissions is not None:
            result['HasRamPermissions'] = self.has_ram_permissions
        if self.is_dlf_service_open is not None:
            result['IsDlfServiceOpen'] = self.is_dlf_service_open
        if self.is_oss_open is not None:
            result['IsOssOpen'] = self.is_oss_open
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasRamPermissions') is not None:
            self.has_ram_permissions = m.get('HasRamPermissions')
        if m.get('IsDlfServiceOpen') is not None:
            self.is_dlf_service_open = m.get('IsDlfServiceOpen')
        if m.get('IsOssOpen') is not None:
            self.is_oss_open = m.get('IsOssOpen')
        return self


class GetServiceStatusResponseBody(TeaModel):
    def __init__(
        self,
        data: GetServiceStatusResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetServiceStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetServiceStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetServiceStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetServiceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTableRequest(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        database_name: str = None,
        table_name: str = None,
    ):
        self.catalog_id = catalog_id
        self.database_name = database_name
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class GetTableResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        table: Table = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.table = table

    def validate(self):
        if self.table:
            self.table.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.table is not None:
            result['Table'] = self.table.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Table') is not None:
            temp_model = Table()
            self.table = temp_model.from_map(m['Table'])
        return self


class GetTableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTableResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTableColumnStatisticsRequest(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        column_names: List[str] = None,
        database_name: str = None,
        table_name: str = None,
    ):
        self.catalog_id = catalog_id
        self.column_names = column_names
        self.database_name = database_name
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.column_names is not None:
            result['ColumnNames'] = self.column_names
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('ColumnNames') is not None:
            self.column_names = m.get('ColumnNames')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class GetTableColumnStatisticsShrinkRequest(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        column_names_shrink: str = None,
        database_name: str = None,
        table_name: str = None,
    ):
        self.catalog_id = catalog_id
        self.column_names_shrink = column_names_shrink
        self.database_name = database_name
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.column_names_shrink is not None:
            result['ColumnNames'] = self.column_names_shrink
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('ColumnNames') is not None:
            self.column_names_shrink = m.get('ColumnNames')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class GetTableColumnStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        column_statistics_obj_list: List[ColumnStatisticsObj] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.column_statistics_obj_list = column_statistics_obj_list
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.column_statistics_obj_list:
            for k in self.column_statistics_obj_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['ColumnStatisticsObjList'] = []
        if self.column_statistics_obj_list is not None:
            for k in self.column_statistics_obj_list:
                result['ColumnStatisticsObjList'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.column_statistics_obj_list = []
        if m.get('ColumnStatisticsObjList') is not None:
            for k in m.get('ColumnStatisticsObjList'):
                temp_model = ColumnStatisticsObj()
                self.column_statistics_obj_list.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetTableColumnStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTableColumnStatisticsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetTableColumnStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTableProfileRequest(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        database_name: str = None,
        table_name: str = None,
    ):
        self.catalog_id = catalog_id
        self.database_name = database_name
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class GetTableProfileResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        table_profile: TableProfile = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.table_profile = table_profile

    def validate(self):
        if self.table_profile:
            self.table_profile.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.table_profile is not None:
            result['TableProfile'] = self.table_profile.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TableProfile') is not None:
            temp_model = TableProfile()
            self.table_profile = temp_model.from_map(m['TableProfile'])
        return self


class GetTableProfileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTableProfileResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetTableProfileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTableVersionRequest(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        database_name: str = None,
        table_name: str = None,
        version_id: int = None,
    ):
        self.catalog_id = catalog_id
        self.database_name = database_name
        self.table_name = table_name
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class GetTableVersionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        table_version: TableVersion = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.table_version = table_version

    def validate(self):
        if self.table_version:
            self.table_version.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.table_version is not None:
            result['TableVersion'] = self.table_version.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TableVersion') is not None:
            temp_model = TableVersion()
            self.table_version = temp_model.from_map(m['TableVersion'])
        return self


class GetTableVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTableVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetTableVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GrantPermissionsRequest(TeaModel):
    def __init__(
        self,
        accesses: List[str] = None,
        catalog_id: str = None,
        delegate_accesses: List[str] = None,
        meta_resource: MetaResource = None,
        principal: Principal = None,
        type: str = None,
    ):
        self.accesses = accesses
        # CatalogId
        self.catalog_id = catalog_id
        self.delegate_accesses = delegate_accesses
        self.meta_resource = meta_resource
        self.principal = principal
        self.type = type

    def validate(self):
        if self.meta_resource:
            self.meta_resource.validate()
        if self.principal:
            self.principal.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accesses is not None:
            result['Accesses'] = self.accesses
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.delegate_accesses is not None:
            result['DelegateAccesses'] = self.delegate_accesses
        if self.meta_resource is not None:
            result['MetaResource'] = self.meta_resource.to_map()
        if self.principal is not None:
            result['Principal'] = self.principal.to_map()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accesses') is not None:
            self.accesses = m.get('Accesses')
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('DelegateAccesses') is not None:
            self.delegate_accesses = m.get('DelegateAccesses')
        if m.get('MetaResource') is not None:
            temp_model = MetaResource()
            self.meta_resource = temp_model.from_map(m['MetaResource'])
        if m.get('Principal') is not None:
            temp_model = Principal()
            self.principal = temp_model.from_map(m['Principal'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GrantPermissionsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Response Code
        self.code = code
        # Message Code
        self.message = message
        # RequestId
        self.request_id = request_id
        # Success
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GrantPermissionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GrantPermissionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GrantPermissionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GrantRoleToUsersRequest(TeaModel):
    def __init__(
        self,
        role_name: str = None,
        users: List[Principal] = None,
    ):
        # RoleName
        self.role_name = role_name
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
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        result['Users'] = []
        if self.users is not None:
            for k in self.users:
                result['Users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        self.users = []
        if m.get('Users') is not None:
            for k in m.get('Users'):
                temp_model = Principal()
                self.users.append(temp_model.from_map(k))
        return self


class GrantRoleToUsersResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Code
        self.code = code
        # Message
        self.message = message
        # RequestId
        self.request_id = request_id
        # Success
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GrantRoleToUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GrantRoleToUsersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GrantRoleToUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GrantRolesToUserRequest(TeaModel):
    def __init__(
        self,
        role_names: List[str] = None,
        user: Principal = None,
    ):
        self.role_names = role_names
        self.user = user

    def validate(self):
        if self.user:
            self.user.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_names is not None:
            result['RoleNames'] = self.role_names
        if self.user is not None:
            result['User'] = self.user.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleNames') is not None:
            self.role_names = m.get('RoleNames')
        if m.get('User') is not None:
            temp_model = Principal()
            self.user = temp_model.from_map(m['User'])
        return self


class GrantRolesToUserResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Code
        self.code = code
        # Message
        self.message = message
        # RequestId
        self.request_id = request_id
        # Success
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GrantRolesToUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GrantRolesToUserResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GrantRolesToUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCatalogsRequest(TeaModel):
    def __init__(
        self,
        id_pattern: str = None,
        next_page_token: str = None,
        page_size: int = None,
    ):
        self.id_pattern = id_pattern
        self.next_page_token = next_page_token
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id_pattern is not None:
            result['IdPattern'] = self.id_pattern
        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdPattern') is not None:
            self.id_pattern = m.get('IdPattern')
        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListCatalogsResponseBody(TeaModel):
    def __init__(
        self,
        catalogs: List[Catalog] = None,
        code: str = None,
        message: str = None,
        next_page_token: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.catalogs = catalogs
        self.code = code
        self.message = message
        self.next_page_token = next_page_token
        self.request_id = request_id
        self.success = success

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
        result['Catalogs'] = []
        if self.catalogs is not None:
            for k in self.catalogs:
                result['Catalogs'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.catalogs = []
        if m.get('Catalogs') is not None:
            for k in m.get('Catalogs'):
                temp_model = Catalog()
                self.catalogs.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        catalog_id: str = None,
        name_pattern: str = None,
        next_page_token: str = None,
        page_size: int = None,
    ):
        self.catalog_id = catalog_id
        self.name_pattern = name_pattern
        self.next_page_token = next_page_token
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.name_pattern is not None:
            result['NamePattern'] = self.name_pattern
        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('NamePattern') is not None:
            self.name_pattern = m.get('NamePattern')
        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListDatabasesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        databases: List[Database] = None,
        message: str = None,
        next_page_token: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.databases = databases
        self.message = message
        self.next_page_token = next_page_token
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.databases:
            for k in self.databases:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Databases'] = []
        if self.databases is not None:
            for k in self.databases:
                result['Databases'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.databases = []
        if m.get('Databases') is not None:
            for k in m.get('Databases'):
                temp_model = Database()
                self.databases.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class ListFunctionNamesRequest(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        database_name: str = None,
        function_name_pattern: str = None,
        next_page_token: str = None,
        page_size: int = None,
    ):
        self.catalog_id = catalog_id
        self.database_name = database_name
        self.function_name_pattern = function_name_pattern
        self.next_page_token = next_page_token
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.function_name_pattern is not None:
            result['FunctionNamePattern'] = self.function_name_pattern
        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('FunctionNamePattern') is not None:
            self.function_name_pattern = m.get('FunctionNamePattern')
        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListFunctionNamesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        function_names: List[str] = None,
        message: str = None,
        next_page_token: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.function_names = function_names
        self.message = message
        self.next_page_token = next_page_token
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.function_names is not None:
            result['FunctionNames'] = self.function_names
        if self.message is not None:
            result['Message'] = self.message
        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('FunctionNames') is not None:
            self.function_names = m.get('FunctionNames')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListFunctionNamesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFunctionNamesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListFunctionNamesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFunctionsRequest(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        database_name: str = None,
        function_name_pattern: str = None,
        next_page_token: str = None,
        page_size: int = None,
    ):
        self.catalog_id = catalog_id
        self.database_name = database_name
        self.function_name_pattern = function_name_pattern
        self.next_page_token = next_page_token
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.function_name_pattern is not None:
            result['FunctionNamePattern'] = self.function_name_pattern
        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('FunctionNamePattern') is not None:
            self.function_name_pattern = m.get('FunctionNamePattern')
        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListFunctionsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        functions: List[Function] = None,
        message: str = None,
        next_page_token: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.functions = functions
        self.message = message
        self.next_page_token = next_page_token
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.functions:
            for k in self.functions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Functions'] = []
        if self.functions is not None:
            for k in self.functions:
                result['Functions'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.functions = []
        if m.get('Functions') is not None:
            for k in m.get('Functions'):
                temp_model = Function()
                self.functions.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListFunctionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFunctionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListFunctionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPartitionNamesRequest(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        database_name: str = None,
        next_page_token: str = None,
        page_size: int = None,
        partial_part_values: List[str] = None,
        table_name: str = None,
    ):
        self.catalog_id = catalog_id
        self.database_name = database_name
        self.next_page_token = next_page_token
        self.page_size = page_size
        self.partial_part_values = partial_part_values
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.partial_part_values is not None:
            result['PartialPartValues'] = self.partial_part_values
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PartialPartValues') is not None:
            self.partial_part_values = m.get('PartialPartValues')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class ListPartitionNamesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        next_page_token: str = None,
        partition_names: List[str] = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.next_page_token = next_page_token
        self.partition_names = partition_names
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token
        if self.partition_names is not None:
            result['PartitionNames'] = self.partition_names
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')
        if m.get('PartitionNames') is not None:
            self.partition_names = m.get('PartitionNames')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListPartitionNamesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPartitionNamesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListPartitionNamesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPartitionsRequest(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        database_name: str = None,
        is_share_sd: bool = None,
        next_page_token: str = None,
        page_size: int = None,
        partial_part_values: List[str] = None,
        table_name: str = None,
    ):
        self.catalog_id = catalog_id
        self.database_name = database_name
        self.is_share_sd = is_share_sd
        self.next_page_token = next_page_token
        self.page_size = page_size
        self.partial_part_values = partial_part_values
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.is_share_sd is not None:
            result['IsShareSd'] = self.is_share_sd
        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.partial_part_values is not None:
            result['PartialPartValues'] = self.partial_part_values
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('IsShareSd') is not None:
            self.is_share_sd = m.get('IsShareSd')
        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PartialPartValues') is not None:
            self.partial_part_values = m.get('PartialPartValues')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class ListPartitionsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        next_page_token: str = None,
        partition_specs: List[PartitionSpec] = None,
        partitions: List[Partition] = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.next_page_token = next_page_token
        # PartitionSpecs
        self.partition_specs = partition_specs
        self.partitions = partitions
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.partition_specs:
            for k in self.partition_specs:
                if k:
                    k.validate()
        if self.partitions:
            for k in self.partitions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token
        result['PartitionSpecs'] = []
        if self.partition_specs is not None:
            for k in self.partition_specs:
                result['PartitionSpecs'].append(k.to_map() if k else None)
        result['Partitions'] = []
        if self.partitions is not None:
            for k in self.partitions:
                result['Partitions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')
        self.partition_specs = []
        if m.get('PartitionSpecs') is not None:
            for k in m.get('PartitionSpecs'):
                temp_model = PartitionSpec()
                self.partition_specs.append(temp_model.from_map(k))
        self.partitions = []
        if m.get('Partitions') is not None:
            for k in m.get('Partitions'):
                temp_model = Partition()
                self.partitions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListPartitionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPartitionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListPartitionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPartitionsByExprResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

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


class ListPartitionsByFilterRequest(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        database_name: str = None,
        filter: str = None,
        is_share_sd: bool = None,
        next_page_token: str = None,
        page_size: int = None,
        table_name: str = None,
    ):
        self.catalog_id = catalog_id
        self.database_name = database_name
        self.filter = filter
        self.is_share_sd = is_share_sd
        self.next_page_token = next_page_token
        self.page_size = page_size
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.is_share_sd is not None:
            result['IsShareSd'] = self.is_share_sd
        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('IsShareSd') is not None:
            self.is_share_sd = m.get('IsShareSd')
        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class ListPartitionsByFilterResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        next_page_token: str = None,
        partition_specs: List[PartitionSpec] = None,
        partitions: List[Partition] = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.next_page_token = next_page_token
        # PartitionSpecs
        self.partition_specs = partition_specs
        self.partitions = partitions
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.partition_specs:
            for k in self.partition_specs:
                if k:
                    k.validate()
        if self.partitions:
            for k in self.partitions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token
        result['PartitionSpecs'] = []
        if self.partition_specs is not None:
            for k in self.partition_specs:
                result['PartitionSpecs'].append(k.to_map() if k else None)
        result['Partitions'] = []
        if self.partitions is not None:
            for k in self.partitions:
                result['Partitions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')
        self.partition_specs = []
        if m.get('PartitionSpecs') is not None:
            for k in m.get('PartitionSpecs'):
                temp_model = PartitionSpec()
                self.partition_specs.append(temp_model.from_map(k))
        self.partitions = []
        if m.get('Partitions') is not None:
            for k in m.get('Partitions'):
                temp_model = Partition()
                self.partitions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListPartitionsByFilterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPartitionsByFilterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListPartitionsByFilterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPermissionsRequest(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        is_list_user_role_permissions: bool = None,
        meta_resource: MetaResource = None,
        meta_resource_type: str = None,
        next_page_token: str = None,
        page_size: int = None,
        principal: Principal = None,
        type: str = None,
    ):
        # CatalogId
        self.catalog_id = catalog_id
        self.is_list_user_role_permissions = is_list_user_role_permissions
        self.meta_resource = meta_resource
        self.meta_resource_type = meta_resource_type
        self.next_page_token = next_page_token
        self.page_size = page_size
        self.principal = principal
        self.type = type

    def validate(self):
        if self.meta_resource:
            self.meta_resource.validate()
        if self.principal:
            self.principal.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.is_list_user_role_permissions is not None:
            result['IsListUserRolePermissions'] = self.is_list_user_role_permissions
        if self.meta_resource is not None:
            result['MetaResource'] = self.meta_resource.to_map()
        if self.meta_resource_type is not None:
            result['MetaResourceType'] = self.meta_resource_type
        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.principal is not None:
            result['Principal'] = self.principal.to_map()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('IsListUserRolePermissions') is not None:
            self.is_list_user_role_permissions = m.get('IsListUserRolePermissions')
        if m.get('MetaResource') is not None:
            temp_model = MetaResource()
            self.meta_resource = temp_model.from_map(m['MetaResource'])
        if m.get('MetaResourceType') is not None:
            self.meta_resource_type = m.get('MetaResourceType')
        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Principal') is not None:
            temp_model = Principal()
            self.principal = temp_model.from_map(m['Principal'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListPermissionsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        next_page_token: str = None,
        principal_resource_permissions_list: List[PrincipalResourcePermissions] = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # Response Code
        self.code = code
        # Message Code
        self.message = message
        # NextPageToken
        self.next_page_token = next_page_token
        self.principal_resource_permissions_list = principal_resource_permissions_list
        # RequestId
        self.request_id = request_id
        # Success
        self.success = success
        # TotalCount
        self.total_count = total_count

    def validate(self):
        if self.principal_resource_permissions_list:
            for k in self.principal_resource_permissions_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token
        result['PrincipalResourcePermissionsList'] = []
        if self.principal_resource_permissions_list is not None:
            for k in self.principal_resource_permissions_list:
                result['PrincipalResourcePermissionsList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')
        self.principal_resource_permissions_list = []
        if m.get('PrincipalResourcePermissionsList') is not None:
            for k in m.get('PrincipalResourcePermissionsList'):
                temp_model = PrincipalResourcePermissions()
                self.principal_resource_permissions_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        next_page_token: str = None,
        page_size: int = None,
        role_name: str = None,
        user_name_pattern: str = None,
    ):
        # NextPageToken
        self.next_page_token = next_page_token
        # PageSize
        self.page_size = page_size
        self.role_name = role_name
        # use name pattern filter
        self.user_name_pattern = user_name_pattern

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.user_name_pattern is not None:
            result['UserNamePattern'] = self.user_name_pattern
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('UserNamePattern') is not None:
            self.user_name_pattern = m.get('UserNamePattern')
        return self


class ListRoleUsersResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        next_page_token: str = None,
        request_id: str = None,
        success: bool = None,
        user_roles: List[UserRole] = None,
    ):
        self.code = code
        self.message = message
        # NextPageToken
        self.next_page_token = next_page_token
        # RequestId
        self.request_id = request_id
        self.success = success
        # user roles
        self.user_roles = user_roles

    def validate(self):
        if self.user_roles:
            for k in self.user_roles:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        result['UserRoles'] = []
        if self.user_roles is not None:
            for k in self.user_roles:
                result['UserRoles'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.user_roles = []
        if m.get('UserRoles') is not None:
            for k in m.get('UserRoles'):
                temp_model = UserRole()
                self.user_roles.append(temp_model.from_map(k))
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        next_page_token: str = None,
        page_size: int = None,
        role_name_pattern: str = None,
    ):
        # Next PageToken
        self.next_page_token = next_page_token
        self.page_size = page_size
        self.role_name_pattern = role_name_pattern

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.role_name_pattern is not None:
            result['RoleNamePattern'] = self.role_name_pattern
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RoleNamePattern') is not None:
            self.role_name_pattern = m.get('RoleNamePattern')
        return self


class ListRolesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        next_page_token: str = None,
        request_id: str = None,
        roles: List[Role] = None,
        success: bool = None,
    ):
        # code
        self.code = code
        # message
        self.message = message
        # data
        self.next_page_token = next_page_token
        # requestId
        self.request_id = request_id
        # role list data
        self.roles = roles
        # success
        self.success = success

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
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Roles'] = []
        if self.roles is not None:
            for k in self.roles:
                result['Roles'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.roles = []
        if m.get('Roles') is not None:
            for k in m.get('Roles'):
                temp_model = Role()
                self.roles.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class ListTableNamesRequest(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        database_name: str = None,
        next_page_token: str = None,
        page_size: int = None,
        table_name_pattern: str = None,
        table_type: str = None,
    ):
        self.catalog_id = catalog_id
        self.database_name = database_name
        self.next_page_token = next_page_token
        self.page_size = page_size
        self.table_name_pattern = table_name_pattern
        self.table_type = table_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.table_name_pattern is not None:
            result['TableNamePattern'] = self.table_name_pattern
        if self.table_type is not None:
            result['TableType'] = self.table_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TableNamePattern') is not None:
            self.table_name_pattern = m.get('TableNamePattern')
        if m.get('TableType') is not None:
            self.table_type = m.get('TableType')
        return self


class ListTableNamesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        next_page_token: str = None,
        request_id: str = None,
        success: bool = None,
        table_names: List[str] = None,
    ):
        self.code = code
        self.message = message
        self.next_page_token = next_page_token
        self.request_id = request_id
        self.success = success
        self.table_names = table_names

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.table_names is not None:
            result['TableNames'] = self.table_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TableNames') is not None:
            self.table_names = m.get('TableNames')
        return self


class ListTableNamesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTableNamesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListTableNamesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTableVersionsRequest(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        database_name: str = None,
        next_page_token: str = None,
        page_size: int = None,
        table_name: str = None,
    ):
        self.catalog_id = catalog_id
        self.database_name = database_name
        self.next_page_token = next_page_token
        self.page_size = page_size
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class ListTableVersionsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        next_page_token: str = None,
        request_id: str = None,
        success: bool = None,
        table_versions: List[TableVersion] = None,
    ):
        self.code = code
        self.message = message
        self.next_page_token = next_page_token
        self.request_id = request_id
        self.success = success
        self.table_versions = table_versions

    def validate(self):
        if self.table_versions:
            for k in self.table_versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        result['TableVersions'] = []
        if self.table_versions is not None:
            for k in self.table_versions:
                result['TableVersions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.table_versions = []
        if m.get('TableVersions') is not None:
            for k in m.get('TableVersions'):
                temp_model = TableVersion()
                self.table_versions.append(temp_model.from_map(k))
        return self


class ListTableVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTableVersionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListTableVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTablesRequest(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        database_name: str = None,
        next_page_token: str = None,
        page_size: int = None,
        table_name_pattern: str = None,
        table_type: str = None,
    ):
        self.catalog_id = catalog_id
        self.database_name = database_name
        self.next_page_token = next_page_token
        self.page_size = page_size
        self.table_name_pattern = table_name_pattern
        self.table_type = table_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.table_name_pattern is not None:
            result['TableNamePattern'] = self.table_name_pattern
        if self.table_type is not None:
            result['TableType'] = self.table_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TableNamePattern') is not None:
            self.table_name_pattern = m.get('TableNamePattern')
        if m.get('TableType') is not None:
            self.table_type = m.get('TableType')
        return self


class ListTablesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        next_page_token: str = None,
        request_id: str = None,
        success: bool = None,
        tables: List[Table] = None,
    ):
        self.code = code
        self.message = message
        self.next_page_token = next_page_token
        self.request_id = request_id
        self.success = success
        self.tables = tables

    def validate(self):
        if self.tables:
            for k in self.tables:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        result['Tables'] = []
        if self.tables is not None:
            for k in self.tables:
                result['Tables'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.tables = []
        if m.get('Tables') is not None:
            for k in m.get('Tables'):
                temp_model = Table()
                self.tables.append(temp_model.from_map(k))
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        next_page_token: str = None,
        page_size: int = None,
        principal_arn: str = None,
        role_name_pattern: str = None,
    ):
        self.next_page_token = next_page_token
        # PageSize
        self.page_size = page_size
        self.principal_arn = principal_arn
        # role name pattern filter
        self.role_name_pattern = role_name_pattern

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.principal_arn is not None:
            result['PrincipalArn'] = self.principal_arn
        if self.role_name_pattern is not None:
            result['RoleNamePattern'] = self.role_name_pattern
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PrincipalArn') is not None:
            self.principal_arn = m.get('PrincipalArn')
        if m.get('RoleNamePattern') is not None:
            self.role_name_pattern = m.get('RoleNamePattern')
        return self


class ListUserRolesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        next_page_token: str = None,
        request_id: str = None,
        success: bool = None,
        user_roles: List[UserRole] = None,
    ):
        # Code
        self.code = code
        # Message
        self.message = message
        # NextPageToken
        self.next_page_token = next_page_token
        # RequestId
        self.request_id = request_id
        # success
        self.success = success
        # UserRoles
        self.user_roles = user_roles

    def validate(self):
        if self.user_roles:
            for k in self.user_roles:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        result['UserRoles'] = []
        if self.user_roles is not None:
            for k in self.user_roles:
                result['UserRoles'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.user_roles = []
        if m.get('UserRoles') is not None:
            for k in m.get('UserRoles'):
                temp_model = UserRole()
                self.user_roles.append(temp_model.from_map(k))
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class RefreshLockRequest(TeaModel):
    def __init__(
        self,
        lock_id: int = None,
    ):
        # LockId
        self.lock_id = lock_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lock_id is not None:
            result['LockId'] = self.lock_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LockId') is not None:
            self.lock_id = m.get('LockId')
        return self


class RefreshLockResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Code
        self.code = code
        # Message
        self.message = message
        # RequestId
        self.request_id = request_id
        # Success
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RefreshLockResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RefreshLockResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = RefreshLockResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RegisterLocationRequest(TeaModel):
    def __init__(
        self,
        inventory_collect_enabled: bool = None,
        location: str = None,
        oss_log_collect_enabled: bool = None,
        role_name: str = None,
    ):
        self.inventory_collect_enabled = inventory_collect_enabled
        self.location = location
        self.oss_log_collect_enabled = oss_log_collect_enabled
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.inventory_collect_enabled is not None:
            result['InventoryCollectEnabled'] = self.inventory_collect_enabled
        if self.location is not None:
            result['Location'] = self.location
        if self.oss_log_collect_enabled is not None:
            result['OssLogCollectEnabled'] = self.oss_log_collect_enabled
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InventoryCollectEnabled') is not None:
            self.inventory_collect_enabled = m.get('InventoryCollectEnabled')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('OssLogCollectEnabled') is not None:
            self.oss_log_collect_enabled = m.get('OssLogCollectEnabled')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class RegisterLocationResponseBodyData(TeaModel):
    def __init__(
        self,
        location_id: str = None,
        storage_collect_task_operation_result_list: List[StorageCollectTaskOperationResult] = None,
    ):
        # Location ID
        self.location_id = location_id
        self.storage_collect_task_operation_result_list = storage_collect_task_operation_result_list

    def validate(self):
        if self.storage_collect_task_operation_result_list:
            for k in self.storage_collect_task_operation_result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.location_id is not None:
            result['LocationId'] = self.location_id
        result['StorageCollectTaskOperationResultList'] = []
        if self.storage_collect_task_operation_result_list is not None:
            for k in self.storage_collect_task_operation_result_list:
                result['StorageCollectTaskOperationResultList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocationId') is not None:
            self.location_id = m.get('LocationId')
        self.storage_collect_task_operation_result_list = []
        if m.get('StorageCollectTaskOperationResultList') is not None:
            for k in m.get('StorageCollectTaskOperationResultList'):
                temp_model = StorageCollectTaskOperationResult()
                self.storage_collect_task_operation_result_list.append(temp_model.from_map(k))
        return self


class RegisterLocationResponseBody(TeaModel):
    def __init__(
        self,
        data: RegisterLocationResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RegisterLocationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RegisterLocationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RegisterLocationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = RegisterLocationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenamePartitionRequest(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        database_name: str = None,
        partition_input: PartitionInput = None,
        partition_values: List[str] = None,
        table_name: str = None,
    ):
        self.catalog_id = catalog_id
        self.database_name = database_name
        self.partition_input = partition_input
        self.partition_values = partition_values
        self.table_name = table_name

    def validate(self):
        if self.partition_input:
            self.partition_input.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.partition_input is not None:
            result['PartitionInput'] = self.partition_input.to_map()
        if self.partition_values is not None:
            result['PartitionValues'] = self.partition_values
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('PartitionInput') is not None:
            temp_model = PartitionInput()
            self.partition_input = temp_model.from_map(m['PartitionInput'])
        if m.get('PartitionValues') is not None:
            self.partition_values = m.get('PartitionValues')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class RenamePartitionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RenamePartitionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RenamePartitionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = RenamePartitionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenameTableRequest(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        database_name: str = None,
        is_async: bool = None,
        table_input: TableInput = None,
        table_name: str = None,
    ):
        self.catalog_id = catalog_id
        self.database_name = database_name
        self.is_async = is_async
        self.table_input = table_input
        self.table_name = table_name

    def validate(self):
        if self.table_input:
            self.table_input.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.is_async is not None:
            result['IsAsync'] = self.is_async
        if self.table_input is not None:
            result['TableInput'] = self.table_input.to_map()
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('IsAsync') is not None:
            self.is_async = m.get('IsAsync')
        if m.get('TableInput') is not None:
            temp_model = TableInput()
            self.table_input = temp_model.from_map(m['TableInput'])
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class RenameTableResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        # Async task Id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class RenameTableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RenameTableResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = RenameTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RevokePermissionsRequest(TeaModel):
    def __init__(
        self,
        accesses: List[str] = None,
        catalog_id: str = None,
        delegate_accesses: List[str] = None,
        meta_resource: MetaResource = None,
        principal: Principal = None,
        type: str = None,
    ):
        self.accesses = accesses
        # CatalogId
        self.catalog_id = catalog_id
        self.delegate_accesses = delegate_accesses
        self.meta_resource = meta_resource
        self.principal = principal
        self.type = type

    def validate(self):
        if self.meta_resource:
            self.meta_resource.validate()
        if self.principal:
            self.principal.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accesses is not None:
            result['Accesses'] = self.accesses
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.delegate_accesses is not None:
            result['DelegateAccesses'] = self.delegate_accesses
        if self.meta_resource is not None:
            result['MetaResource'] = self.meta_resource.to_map()
        if self.principal is not None:
            result['Principal'] = self.principal.to_map()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accesses') is not None:
            self.accesses = m.get('Accesses')
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('DelegateAccesses') is not None:
            self.delegate_accesses = m.get('DelegateAccesses')
        if m.get('MetaResource') is not None:
            temp_model = MetaResource()
            self.meta_resource = temp_model.from_map(m['MetaResource'])
        if m.get('Principal') is not None:
            temp_model = Principal()
            self.principal = temp_model.from_map(m['Principal'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class RevokePermissionsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Response Code
        self.code = code
        # Message Code
        self.message = message
        # RequestId
        self.request_id = request_id
        # Success
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RevokePermissionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RevokePermissionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = RevokePermissionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RevokeRoleFromUsersRequest(TeaModel):
    def __init__(
        self,
        role_name: str = None,
        users: List[Principal] = None,
    ):
        self.role_name = role_name
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
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        result['Users'] = []
        if self.users is not None:
            for k in self.users:
                result['Users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        self.users = []
        if m.get('Users') is not None:
            for k in m.get('Users'):
                temp_model = Principal()
                self.users.append(temp_model.from_map(k))
        return self


class RevokeRoleFromUsersResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Code
        self.code = code
        # Message
        self.message = message
        # RequestId
        self.request_id = request_id
        # Success
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RevokeRoleFromUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RevokeRoleFromUsersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = RevokeRoleFromUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RevokeRolesFromUserRequest(TeaModel):
    def __init__(
        self,
        role_names: List[str] = None,
        user: Principal = None,
    ):
        self.role_names = role_names
        self.user = user

    def validate(self):
        if self.user:
            self.user.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_names is not None:
            result['RoleNames'] = self.role_names
        if self.user is not None:
            result['User'] = self.user.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleNames') is not None:
            self.role_names = m.get('RoleNames')
        if m.get('User') is not None:
            temp_model = Principal()
            self.user = temp_model.from_map(m['User'])
        return self


class RevokeRolesFromUserResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # code
        self.code = code
        # message
        self.message = message
        # RequestId
        self.request_id = request_id
        # success
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RevokeRolesFromUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RevokeRolesFromUserResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = RevokeRolesFromUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunMigrationWorkflowRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class RunMigrationWorkflowResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RunMigrationWorkflowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunMigrationWorkflowResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = RunMigrationWorkflowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchRequest(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        page_number: int = None,
        page_size: int = None,
        search_text: str = None,
        search_type: str = None,
        sort_criteria: List[SortCriterion] = None,
    ):
        # catalogid
        self.catalog_id = catalog_id
        self.page_number = page_number
        self.page_size = page_size
        self.search_text = search_text
        self.search_type = search_type
        self.sort_criteria = sort_criteria

    def validate(self):
        if self.sort_criteria:
            for k in self.sort_criteria:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_text is not None:
            result['SearchText'] = self.search_text
        if self.search_type is not None:
            result['SearchType'] = self.search_type
        result['SortCriteria'] = []
        if self.sort_criteria is not None:
            for k in self.sort_criteria:
                result['SortCriteria'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchText') is not None:
            self.search_text = m.get('SearchText')
        if m.get('SearchType') is not None:
            self.search_type = m.get('SearchType')
        self.sort_criteria = []
        if m.get('SortCriteria') is not None:
            for k in m.get('SortCriteria'):
                temp_model = SortCriterion()
                self.sort_criteria.append(temp_model.from_map(k))
        return self


class SearchResponseBodyDatabaseResultDatabases(TeaModel):
    def __init__(
        self,
        database: Database = None,
        high_light_list: List[HighLight] = None,
    ):
        self.database = database
        self.high_light_list = high_light_list

    def validate(self):
        if self.database:
            self.database.validate()
        if self.high_light_list:
            for k in self.high_light_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database is not None:
            result['Database'] = self.database.to_map()
        result['HighLightList'] = []
        if self.high_light_list is not None:
            for k in self.high_light_list:
                result['HighLightList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Database') is not None:
            temp_model = Database()
            self.database = temp_model.from_map(m['Database'])
        self.high_light_list = []
        if m.get('HighLightList') is not None:
            for k in m.get('HighLightList'):
                temp_model = HighLight()
                self.high_light_list.append(temp_model.from_map(k))
        return self


class SearchResponseBodyDatabaseResult(TeaModel):
    def __init__(
        self,
        databases: List[SearchResponseBodyDatabaseResultDatabases] = None,
        total_count: int = None,
    ):
        self.databases = databases
        self.total_count = total_count

    def validate(self):
        if self.databases:
            for k in self.databases:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Databases'] = []
        if self.databases is not None:
            for k in self.databases:
                result['Databases'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.databases = []
        if m.get('Databases') is not None:
            for k in m.get('Databases'):
                temp_model = SearchResponseBodyDatabaseResultDatabases()
                self.databases.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class SearchResponseBodyTableResultTables(TeaModel):
    def __init__(
        self,
        high_light_list: List[HighLight] = None,
        table: Table = None,
    ):
        self.high_light_list = high_light_list
        self.table = table

    def validate(self):
        if self.high_light_list:
            for k in self.high_light_list:
                if k:
                    k.validate()
        if self.table:
            self.table.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HighLightList'] = []
        if self.high_light_list is not None:
            for k in self.high_light_list:
                result['HighLightList'].append(k.to_map() if k else None)
        if self.table is not None:
            result['Table'] = self.table.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.high_light_list = []
        if m.get('HighLightList') is not None:
            for k in m.get('HighLightList'):
                temp_model = HighLight()
                self.high_light_list.append(temp_model.from_map(k))
        if m.get('Table') is not None:
            temp_model = Table()
            self.table = temp_model.from_map(m['Table'])
        return self


class SearchResponseBodyTableResult(TeaModel):
    def __init__(
        self,
        tables: List[SearchResponseBodyTableResultTables] = None,
        total_count: int = None,
    ):
        self.tables = tables
        self.total_count = total_count

    def validate(self):
        if self.tables:
            for k in self.tables:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Tables'] = []
        if self.tables is not None:
            for k in self.tables:
                result['Tables'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tables = []
        if m.get('Tables') is not None:
            for k in m.get('Tables'):
                temp_model = SearchResponseBodyTableResultTables()
                self.tables.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class SearchResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        database_result: SearchResponseBodyDatabaseResult = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        table_result: SearchResponseBodyTableResult = None,
    ):
        self.code = code
        self.database_result = database_result
        self.message = message
        self.request_id = request_id
        self.success = success
        self.table_result = table_result

    def validate(self):
        if self.database_result:
            self.database_result.validate()
        if self.table_result:
            self.table_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.database_result is not None:
            result['DatabaseResult'] = self.database_result.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.table_result is not None:
            result['TableResult'] = self.table_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DatabaseResult') is not None:
            temp_model = SearchResponseBodyDatabaseResult()
            self.database_result = temp_model.from_map(m['DatabaseResult'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TableResult') is not None:
            temp_model = SearchResponseBodyTableResult()
            self.table_result = temp_model.from_map(m['TableResult'])
        return self


class SearchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = SearchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchAcrossCatalogRequest(TeaModel):
    def __init__(
        self,
        catalog_ids: List[str] = None,
        page_number: int = None,
        page_size: int = None,
        search_text: str = None,
        search_types: List[str] = None,
        sort_criteria: List[SortCriterion] = None,
    ):
        self.catalog_ids = catalog_ids
        self.page_number = page_number
        self.page_size = page_size
        self.search_text = search_text
        self.search_types = search_types
        self.sort_criteria = sort_criteria

    def validate(self):
        if self.sort_criteria:
            for k in self.sort_criteria:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_ids is not None:
            result['CatalogIds'] = self.catalog_ids
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_text is not None:
            result['SearchText'] = self.search_text
        if self.search_types is not None:
            result['SearchTypes'] = self.search_types
        result['SortCriteria'] = []
        if self.sort_criteria is not None:
            for k in self.sort_criteria:
                result['SortCriteria'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogIds') is not None:
            self.catalog_ids = m.get('CatalogIds')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchText') is not None:
            self.search_text = m.get('SearchText')
        if m.get('SearchTypes') is not None:
            self.search_types = m.get('SearchTypes')
        self.sort_criteria = []
        if m.get('SortCriteria') is not None:
            for k in m.get('SortCriteria'):
                temp_model = SortCriterion()
                self.sort_criteria.append(temp_model.from_map(k))
        return self


class SearchAcrossCatalogResponseBodyCatalogResultCatalogs(TeaModel):
    def __init__(
        self,
        catalog: Catalog = None,
        high_light_list: List[HighLight] = None,
    ):
        self.catalog = catalog
        self.high_light_list = high_light_list

    def validate(self):
        if self.catalog:
            self.catalog.validate()
        if self.high_light_list:
            for k in self.high_light_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog is not None:
            result['Catalog'] = self.catalog.to_map()
        result['HighLightList'] = []
        if self.high_light_list is not None:
            for k in self.high_light_list:
                result['HighLightList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Catalog') is not None:
            temp_model = Catalog()
            self.catalog = temp_model.from_map(m['Catalog'])
        self.high_light_list = []
        if m.get('HighLightList') is not None:
            for k in m.get('HighLightList'):
                temp_model = HighLight()
                self.high_light_list.append(temp_model.from_map(k))
        return self


class SearchAcrossCatalogResponseBodyCatalogResult(TeaModel):
    def __init__(
        self,
        catalogs: List[SearchAcrossCatalogResponseBodyCatalogResultCatalogs] = None,
        total_count: int = None,
    ):
        self.catalogs = catalogs
        self.total_count = total_count

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
        result['Catalogs'] = []
        if self.catalogs is not None:
            for k in self.catalogs:
                result['Catalogs'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.catalogs = []
        if m.get('Catalogs') is not None:
            for k in m.get('Catalogs'):
                temp_model = SearchAcrossCatalogResponseBodyCatalogResultCatalogs()
                self.catalogs.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class SearchAcrossCatalogResponseBodyDatabaseResultDatabases(TeaModel):
    def __init__(
        self,
        database: Database = None,
        high_light_list: List[HighLight] = None,
    ):
        self.database = database
        self.high_light_list = high_light_list

    def validate(self):
        if self.database:
            self.database.validate()
        if self.high_light_list:
            for k in self.high_light_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database is not None:
            result['Database'] = self.database.to_map()
        result['HighLightList'] = []
        if self.high_light_list is not None:
            for k in self.high_light_list:
                result['HighLightList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Database') is not None:
            temp_model = Database()
            self.database = temp_model.from_map(m['Database'])
        self.high_light_list = []
        if m.get('HighLightList') is not None:
            for k in m.get('HighLightList'):
                temp_model = HighLight()
                self.high_light_list.append(temp_model.from_map(k))
        return self


class SearchAcrossCatalogResponseBodyDatabaseResult(TeaModel):
    def __init__(
        self,
        databases: List[SearchAcrossCatalogResponseBodyDatabaseResultDatabases] = None,
        total_count: int = None,
    ):
        self.databases = databases
        self.total_count = total_count

    def validate(self):
        if self.databases:
            for k in self.databases:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Databases'] = []
        if self.databases is not None:
            for k in self.databases:
                result['Databases'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.databases = []
        if m.get('Databases') is not None:
            for k in m.get('Databases'):
                temp_model = SearchAcrossCatalogResponseBodyDatabaseResultDatabases()
                self.databases.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class SearchAcrossCatalogResponseBodyTableResultTables(TeaModel):
    def __init__(
        self,
        high_light_list: List[HighLight] = None,
        table: Table = None,
    ):
        self.high_light_list = high_light_list
        self.table = table

    def validate(self):
        if self.high_light_list:
            for k in self.high_light_list:
                if k:
                    k.validate()
        if self.table:
            self.table.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HighLightList'] = []
        if self.high_light_list is not None:
            for k in self.high_light_list:
                result['HighLightList'].append(k.to_map() if k else None)
        if self.table is not None:
            result['Table'] = self.table.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.high_light_list = []
        if m.get('HighLightList') is not None:
            for k in m.get('HighLightList'):
                temp_model = HighLight()
                self.high_light_list.append(temp_model.from_map(k))
        if m.get('Table') is not None:
            temp_model = Table()
            self.table = temp_model.from_map(m['Table'])
        return self


class SearchAcrossCatalogResponseBodyTableResult(TeaModel):
    def __init__(
        self,
        tables: List[SearchAcrossCatalogResponseBodyTableResultTables] = None,
        total_count: int = None,
    ):
        self.tables = tables
        self.total_count = total_count

    def validate(self):
        if self.tables:
            for k in self.tables:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Tables'] = []
        if self.tables is not None:
            for k in self.tables:
                result['Tables'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tables = []
        if m.get('Tables') is not None:
            for k in m.get('Tables'):
                temp_model = SearchAcrossCatalogResponseBodyTableResultTables()
                self.tables.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class SearchAcrossCatalogResponseBody(TeaModel):
    def __init__(
        self,
        catalog_result: SearchAcrossCatalogResponseBodyCatalogResult = None,
        code: str = None,
        database_result: SearchAcrossCatalogResponseBodyDatabaseResult = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        table_result: SearchAcrossCatalogResponseBodyTableResult = None,
    ):
        self.catalog_result = catalog_result
        self.code = code
        self.database_result = database_result
        self.message = message
        self.request_id = request_id
        self.success = success
        self.table_result = table_result

    def validate(self):
        if self.catalog_result:
            self.catalog_result.validate()
        if self.database_result:
            self.database_result.validate()
        if self.table_result:
            self.table_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_result is not None:
            result['CatalogResult'] = self.catalog_result.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.database_result is not None:
            result['DatabaseResult'] = self.database_result.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.table_result is not None:
            result['TableResult'] = self.table_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogResult') is not None:
            temp_model = SearchAcrossCatalogResponseBodyCatalogResult()
            self.catalog_result = temp_model.from_map(m['CatalogResult'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DatabaseResult') is not None:
            temp_model = SearchAcrossCatalogResponseBodyDatabaseResult()
            self.database_result = temp_model.from_map(m['DatabaseResult'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TableResult') is not None:
            temp_model = SearchAcrossCatalogResponseBodyTableResult()
            self.table_result = temp_model.from_map(m['TableResult'])
        return self


class SearchAcrossCatalogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchAcrossCatalogResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = SearchAcrossCatalogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopMigrationWorkflowRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class StopMigrationWorkflowResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StopMigrationWorkflowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopMigrationWorkflowResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = StopMigrationWorkflowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitQueryRequest(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        sql: str = None,
        workspace_id: str = None,
    ):
        self.catalog_id = catalog_id
        self.sql = sql
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['catalogId'] = self.catalog_id
        if self.sql is not None:
            result['sql'] = self.sql
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('catalogId') is not None:
            self.catalog_id = m.get('catalogId')
        if m.get('sql') is not None:
            self.sql = m.get('sql')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class SubmitQueryResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SubmitQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitQueryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = SubmitQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnLockRequest(TeaModel):
    def __init__(
        self,
        lock_id: int = None,
    ):
        # LockId
        self.lock_id = lock_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lock_id is not None:
            result['LockId'] = self.lock_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LockId') is not None:
            self.lock_id = m.get('LockId')
        return self


class UnLockResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Code
        self.code = code
        # Message
        self.message = message
        # RequestId
        self.request_id = request_id
        # Success
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UnLockResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnLockResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UnLockResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCatalogRequest(TeaModel):
    def __init__(
        self,
        catalog_input: CatalogInput = None,
    ):
        # cataloginput
        self.catalog_input = catalog_input

    def validate(self):
        if self.catalog_input:
            self.catalog_input.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_input is not None:
            result['CatalogInput'] = self.catalog_input.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogInput') is not None:
            temp_model = CatalogInput()
            self.catalog_input = temp_model.from_map(m['CatalogInput'])
        return self


class UpdateCatalogResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateCatalogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateCatalogResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UpdateCatalogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCatalogSettingsRequest(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        catalog_settings: CatalogSettings = None,
    ):
        # CatalogId
        self.catalog_id = catalog_id
        self.catalog_settings = catalog_settings

    def validate(self):
        if self.catalog_settings:
            self.catalog_settings.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.catalog_settings is not None:
            result['CatalogSettings'] = self.catalog_settings.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('CatalogSettings') is not None:
            temp_model = CatalogSettings()
            self.catalog_settings = temp_model.from_map(m['CatalogSettings'])
        return self


class UpdateCatalogSettingsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Code
        self.code = code
        # Message
        self.message = message
        # RequestId
        self.request_id = request_id
        # Success
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateCatalogSettingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateCatalogSettingsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UpdateCatalogSettingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDatabaseRequest(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        database_input: DatabaseInput = None,
        name: str = None,
    ):
        self.catalog_id = catalog_id
        self.database_input = database_input
        self.name = name

    def validate(self):
        if self.database_input:
            self.database_input.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.database_input is not None:
            result['DatabaseInput'] = self.database_input.to_map()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('DatabaseInput') is not None:
            temp_model = DatabaseInput()
            self.database_input = temp_model.from_map(m['DatabaseInput'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateDatabaseResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateDatabaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDatabaseResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UpdateDatabaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFunctionRequest(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        database_name: str = None,
        function_input: FunctionInput = None,
        function_name: str = None,
    ):
        self.catalog_id = catalog_id
        self.database_name = database_name
        self.function_input = function_input
        self.function_name = function_name

    def validate(self):
        if self.function_input:
            self.function_input.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.function_input is not None:
            result['FunctionInput'] = self.function_input.to_map()
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('FunctionInput') is not None:
            temp_model = FunctionInput()
            self.function_input = temp_model.from_map(m['FunctionInput'])
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        return self


class UpdateFunctionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateFunctionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateFunctionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UpdateFunctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePartitionColumnStatisticsRequest(TeaModel):
    def __init__(
        self,
        update_table_partition_column_statistics_request: UpdateTablePartitionColumnStatisticsRequest = None,
    ):
        self.update_table_partition_column_statistics_request = update_table_partition_column_statistics_request

    def validate(self):
        if self.update_table_partition_column_statistics_request:
            self.update_table_partition_column_statistics_request.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.update_table_partition_column_statistics_request is not None:
            result['UpdateTablePartitionColumnStatisticsRequest'] = self.update_table_partition_column_statistics_request.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateTablePartitionColumnStatisticsRequest') is not None:
            temp_model = UpdateTablePartitionColumnStatisticsRequest()
            self.update_table_partition_column_statistics_request = temp_model.from_map(m['UpdateTablePartitionColumnStatisticsRequest'])
        return self


class UpdatePartitionColumnStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdatePartitionColumnStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdatePartitionColumnStatisticsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UpdatePartitionColumnStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePermissionsRequest(TeaModel):
    def __init__(
        self,
        accesses: List[str] = None,
        catalog_id: str = None,
        delegate_accesses: List[str] = None,
        meta_resource: MetaResource = None,
        principal: Principal = None,
        type: str = None,
    ):
        self.accesses = accesses
        # CatalogId
        self.catalog_id = catalog_id
        self.delegate_accesses = delegate_accesses
        self.meta_resource = meta_resource
        self.principal = principal
        self.type = type

    def validate(self):
        if self.meta_resource:
            self.meta_resource.validate()
        if self.principal:
            self.principal.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accesses is not None:
            result['Accesses'] = self.accesses
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.delegate_accesses is not None:
            result['DelegateAccesses'] = self.delegate_accesses
        if self.meta_resource is not None:
            result['MetaResource'] = self.meta_resource.to_map()
        if self.principal is not None:
            result['Principal'] = self.principal.to_map()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accesses') is not None:
            self.accesses = m.get('Accesses')
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('DelegateAccesses') is not None:
            self.delegate_accesses = m.get('DelegateAccesses')
        if m.get('MetaResource') is not None:
            temp_model = MetaResource()
            self.meta_resource = temp_model.from_map(m['MetaResource'])
        if m.get('Principal') is not None:
            temp_model = Principal()
            self.principal = temp_model.from_map(m['Principal'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdatePermissionsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Response Code
        self.code = code
        # Message Code
        self.message = message
        # RequestId
        self.request_id = request_id
        # Success
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdatePermissionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdatePermissionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UpdatePermissionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRegisteredLocationRequest(TeaModel):
    def __init__(
        self,
        inventory_collect_enabled: bool = None,
        location_id: str = None,
        oss_log_collect_enabled: bool = None,
    ):
        self.inventory_collect_enabled = inventory_collect_enabled
        self.location_id = location_id
        self.oss_log_collect_enabled = oss_log_collect_enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.inventory_collect_enabled is not None:
            result['InventoryCollectEnabled'] = self.inventory_collect_enabled
        if self.location_id is not None:
            result['LocationId'] = self.location_id
        if self.oss_log_collect_enabled is not None:
            result['OssLogCollectEnabled'] = self.oss_log_collect_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InventoryCollectEnabled') is not None:
            self.inventory_collect_enabled = m.get('InventoryCollectEnabled')
        if m.get('LocationId') is not None:
            self.location_id = m.get('LocationId')
        if m.get('OssLogCollectEnabled') is not None:
            self.oss_log_collect_enabled = m.get('OssLogCollectEnabled')
        return self


class UpdateRegisteredLocationResponseBodyData(TeaModel):
    def __init__(
        self,
        location_id: str = None,
        storage_collect_task_operation_result_list: List[StorageCollectTaskOperationResult] = None,
    ):
        # Location ID
        self.location_id = location_id
        self.storage_collect_task_operation_result_list = storage_collect_task_operation_result_list

    def validate(self):
        if self.storage_collect_task_operation_result_list:
            for k in self.storage_collect_task_operation_result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.location_id is not None:
            result['LocationId'] = self.location_id
        result['StorageCollectTaskOperationResultList'] = []
        if self.storage_collect_task_operation_result_list is not None:
            for k in self.storage_collect_task_operation_result_list:
                result['StorageCollectTaskOperationResultList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocationId') is not None:
            self.location_id = m.get('LocationId')
        self.storage_collect_task_operation_result_list = []
        if m.get('StorageCollectTaskOperationResultList') is not None:
            for k in m.get('StorageCollectTaskOperationResultList'):
                temp_model = StorageCollectTaskOperationResult()
                self.storage_collect_task_operation_result_list.append(temp_model.from_map(k))
        return self


class UpdateRegisteredLocationResponseBody(TeaModel):
    def __init__(
        self,
        data: UpdateRegisteredLocationResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = UpdateRegisteredLocationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateRegisteredLocationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateRegisteredLocationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UpdateRegisteredLocationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRoleRequest(TeaModel):
    def __init__(
        self,
        role_input: RoleInput = None,
        role_name: str = None,
    ):
        self.role_input = role_input
        # RoleName
        self.role_name = role_name

    def validate(self):
        if self.role_input:
            self.role_input.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_input is not None:
            result['RoleInput'] = self.role_input.to_map()
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleInput') is not None:
            temp_model = RoleInput()
            self.role_input = temp_model.from_map(m['RoleInput'])
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class UpdateRoleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # code
        self.code = code
        # message
        self.message = message
        # requestId
        self.request_id = request_id
        # success
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateRoleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UpdateRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRoleUsersRequest(TeaModel):
    def __init__(
        self,
        role_name: str = None,
        users: List[Principal] = None,
    ):
        self.role_name = role_name
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
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        result['Users'] = []
        if self.users is not None:
            for k in self.users:
                result['Users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        self.users = []
        if m.get('Users') is not None:
            for k in m.get('Users'):
                temp_model = Principal()
                self.users.append(temp_model.from_map(k))
        return self


class UpdateRoleUsersResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # code
        self.code = code
        # message
        self.message = message
        # requestId
        self.request_id = request_id
        # success
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateRoleUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateRoleUsersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UpdateRoleUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTableRequest(TeaModel):
    def __init__(
        self,
        allow_partition_key_change: bool = None,
        catalog_id: str = None,
        database_name: str = None,
        is_async: bool = None,
        skip_archive: bool = None,
        table_input: TableInput = None,
        table_name: str = None,
    ):
        self.allow_partition_key_change = allow_partition_key_change
        self.catalog_id = catalog_id
        self.database_name = database_name
        self.is_async = is_async
        self.skip_archive = skip_archive
        self.table_input = table_input
        self.table_name = table_name

    def validate(self):
        if self.table_input:
            self.table_input.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_partition_key_change is not None:
            result['AllowPartitionKeyChange'] = self.allow_partition_key_change
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.is_async is not None:
            result['IsAsync'] = self.is_async
        if self.skip_archive is not None:
            result['SkipArchive'] = self.skip_archive
        if self.table_input is not None:
            result['TableInput'] = self.table_input.to_map()
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowPartitionKeyChange') is not None:
            self.allow_partition_key_change = m.get('AllowPartitionKeyChange')
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('IsAsync') is not None:
            self.is_async = m.get('IsAsync')
        if m.get('SkipArchive') is not None:
            self.skip_archive = m.get('SkipArchive')
        if m.get('TableInput') is not None:
            temp_model = TableInput()
            self.table_input = temp_model.from_map(m['TableInput'])
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class UpdateTableResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        # Async task Id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class UpdateTableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateTableResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UpdateTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTableColumnStatisticsRequest(TeaModel):
    def __init__(
        self,
        update_table_partition_column_statistics_request: UpdateTablePartitionColumnStatisticsRequest = None,
    ):
        self.update_table_partition_column_statistics_request = update_table_partition_column_statistics_request

    def validate(self):
        if self.update_table_partition_column_statistics_request:
            self.update_table_partition_column_statistics_request.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.update_table_partition_column_statistics_request is not None:
            result['UpdateTablePartitionColumnStatisticsRequest'] = self.update_table_partition_column_statistics_request.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateTablePartitionColumnStatisticsRequest') is not None:
            temp_model = UpdateTablePartitionColumnStatisticsRequest()
            self.update_table_partition_column_statistics_request = temp_model.from_map(m['UpdateTablePartitionColumnStatisticsRequest'])
        return self


class UpdateTableColumnStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateTableColumnStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateTableColumnStatisticsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UpdateTableColumnStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


