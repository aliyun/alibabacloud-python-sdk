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
        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')
        if m.get('updatedBy') is not None:
            self.updated_by = m.get('updatedBy')
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


class Permission(TeaModel):
    def __init__(
        self,
        access: str = None,
        database: str = None,
        principal: str = None,
        resource_type: str = None,
        table: str = None,
    ):
        self.access = access
        self.database = database
        self.principal = principal
        self.resource_type = resource_type
        self.table = table

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access is not None:
            result['access'] = self.access
        if self.database is not None:
            result['database'] = self.database
        if self.principal is not None:
            result['principal'] = self.principal
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.table is not None:
            result['table'] = self.table
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('access') is not None:
            self.access = m.get('access')
        if m.get('database') is not None:
            self.database = m.get('database')
        if m.get('principal') is not None:
            self.principal = m.get('principal')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('table') is not None:
            self.table = m.get('table')
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
        optimization_config: Dict[str, str] = None,
        options: Dict[str, str] = None,
    ):
        self.name = name
        self.optimization_config = optimization_config
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
        if self.optimization_config is not None:
            result['optimizationConfig'] = self.optimization_config
        if self.options is not None:
            result['options'] = self.options
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('optimizationConfig') is not None:
            self.optimization_config = m.get('optimizationConfig')
        if m.get('options') is not None:
            self.options = m.get('options')
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


class ListPermissionsRequest(TeaModel):
    def __init__(
        self,
        database: str = None,
        max_results: int = None,
        page_token: str = None,
        principal: str = None,
        resource_type: str = None,
        table: str = None,
    ):
        self.database = database
        self.max_results = max_results
        self.page_token = page_token
        self.principal = principal
        # This parameter is required.
        self.resource_type = resource_type
        self.table = table

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database is not None:
            result['database'] = self.database
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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('database') is not None:
            self.database = m.get('database')
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
        max_results: str = None,
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


class ListUserRolesRequest(TeaModel):
    def __init__(
        self,
        max_results: str = None,
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


