# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class CreateResourceRequest(TeaModel):
    def __init__(
        self,
        body: str = None,
        resource_type_version: str = None,
    ):
        self.body = body
        self.resource_type_version = resource_type_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.resource_type_version is not None:
            result['resourceTypeVersion'] = self.resource_type_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('resourceTypeVersion') is not None:
            self.resource_type_version = m.get('resourceTypeVersion')
        return self


class CreateResourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_id: str = None,
        task_id: str = None,
    ):
        # 请求id
        self.request_id = request_id
        # 资源id
        self.resource_id = resource_id
        # 任务id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class CreateResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateResourceResponseBody = None,
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
            temp_model = CreateResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteResourceRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_type_version: str = None,
    ):
        self.region_id = region_id
        self.resource_type_version = resource_type_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.resource_type_version is not None:
            result['resourceTypeVersion'] = self.resource_type_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('resourceTypeVersion') is not None:
            self.resource_type_version = m.get('resourceTypeVersion')
        return self


class DeleteResourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class DeleteResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteResourceResponseBody = None,
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
            temp_model = DeleteResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceRequest(TeaModel):
    def __init__(
        self,
        data_type: str = None,
        region_id: str = None,
    ):
        self.data_type = data_type
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class GetResourceResponseBodyResource(TeaModel):
    def __init__(
        self,
        product_code: str = None,
        region_id: str = None,
        resource_attributes: str = None,
        resource_id: str = None,
        resource_type_code: str = None,
    ):
        self.product_code = product_code
        self.region_id = region_id
        self.resource_attributes = resource_attributes
        self.resource_id = resource_id
        self.resource_type_code = resource_type_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_code is not None:
            result['productCode'] = self.product_code
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.resource_attributes is not None:
            result['resourceAttributes'] = self.resource_attributes
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_type_code is not None:
            result['resourceTypeCode'] = self.resource_type_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('resourceAttributes') is not None:
            self.resource_attributes = m.get('resourceAttributes')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceTypeCode') is not None:
            self.resource_type_code = m.get('resourceTypeCode')
        return self


class GetResourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource: GetResourceResponseBodyResource = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.resource = resource

    def validate(self):
        if self.resource:
            self.resource.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.resource is not None:
            result['resource'] = self.resource.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('resource') is not None:
            temp_model = GetResourceResponseBodyResource()
            self.resource = temp_model.from_map(m['resource'])
        return self


class GetResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetResourceResponseBody = None,
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
            temp_model = GetResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceTypeRequest(TeaModel):
    def __init__(
        self,
        resource_type_version: str = None,
    ):
        self.resource_type_version = resource_type_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_type_version is not None:
            result['resourceTypeVersion'] = self.resource_type_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceTypeVersion') is not None:
            self.resource_type_version = m.get('resourceTypeVersion')
        return self


class GetResourceTypeResponseBodyResourceTypeHandlersCreate(TeaModel):
    def __init__(
        self,
        permissions: List[str] = None,
    ):
        self.permissions = permissions

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.permissions is not None:
            result['permissions'] = self.permissions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('permissions') is not None:
            self.permissions = m.get('permissions')
        return self


class GetResourceTypeResponseBodyResourceTypeHandlersDelete(TeaModel):
    def __init__(
        self,
        permissions: List[str] = None,
    ):
        self.permissions = permissions

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.permissions is not None:
            result['permissions'] = self.permissions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('permissions') is not None:
            self.permissions = m.get('permissions')
        return self


class GetResourceTypeResponseBodyResourceTypeHandlersGet(TeaModel):
    def __init__(
        self,
        permissions: List[str] = None,
    ):
        self.permissions = permissions

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.permissions is not None:
            result['permissions'] = self.permissions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('permissions') is not None:
            self.permissions = m.get('permissions')
        return self


class GetResourceTypeResponseBodyResourceTypeHandlersList(TeaModel):
    def __init__(
        self,
        permissions: List[str] = None,
    ):
        self.permissions = permissions

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.permissions is not None:
            result['permissions'] = self.permissions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('permissions') is not None:
            self.permissions = m.get('permissions')
        return self


class GetResourceTypeResponseBodyResourceTypeHandlersUpdate(TeaModel):
    def __init__(
        self,
        permissions: List[str] = None,
    ):
        self.permissions = permissions

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.permissions is not None:
            result['permissions'] = self.permissions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('permissions') is not None:
            self.permissions = m.get('permissions')
        return self


class GetResourceTypeResponseBodyResourceTypeHandlers(TeaModel):
    def __init__(
        self,
        create: GetResourceTypeResponseBodyResourceTypeHandlersCreate = None,
        delete: GetResourceTypeResponseBodyResourceTypeHandlersDelete = None,
        get: GetResourceTypeResponseBodyResourceTypeHandlersGet = None,
        list: GetResourceTypeResponseBodyResourceTypeHandlersList = None,
        update: GetResourceTypeResponseBodyResourceTypeHandlersUpdate = None,
    ):
        self.create = create
        self.delete = delete
        self.get = get
        self.list = list
        self.update = update

    def validate(self):
        if self.create:
            self.create.validate()
        if self.delete:
            self.delete.validate()
        if self.get:
            self.get.validate()
        if self.list:
            self.list.validate()
        if self.update:
            self.update.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create is not None:
            result['create'] = self.create.to_map()
        if self.delete is not None:
            result['delete'] = self.delete.to_map()
        if self.get is not None:
            result['get'] = self.get.to_map()
        if self.list is not None:
            result['list'] = self.list.to_map()
        if self.update is not None:
            result['update'] = self.update.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('create') is not None:
            temp_model = GetResourceTypeResponseBodyResourceTypeHandlersCreate()
            self.create = temp_model.from_map(m['create'])
        if m.get('delete') is not None:
            temp_model = GetResourceTypeResponseBodyResourceTypeHandlersDelete()
            self.delete = temp_model.from_map(m['delete'])
        if m.get('get') is not None:
            temp_model = GetResourceTypeResponseBodyResourceTypeHandlersGet()
            self.get = temp_model.from_map(m['get'])
        if m.get('list') is not None:
            temp_model = GetResourceTypeResponseBodyResourceTypeHandlersList()
            self.list = temp_model.from_map(m['list'])
        if m.get('update') is not None:
            temp_model = GetResourceTypeResponseBodyResourceTypeHandlersUpdate()
            self.update = temp_model.from_map(m['update'])
        return self


class GetResourceTypeResponseBodyResourceTypeInfo(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        delivery_scope: str = None,
        description: str = None,
        title: str = None,
    ):
        self.charge_type = charge_type
        self.delivery_scope = delivery_scope
        self.description = description
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.delivery_scope is not None:
            result['deliveryScope'] = self.delivery_scope
        if self.description is not None:
            result['description'] = self.description
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('deliveryScope') is not None:
            self.delivery_scope = m.get('deliveryScope')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class GetResourceTypeResponseBodyResourceType(TeaModel):
    def __init__(
        self,
        create_only_properties: List[str] = None,
        delete_only_properties: List[str] = None,
        filter_properties: List[str] = None,
        get_only_properties: List[str] = None,
        handlers: GetResourceTypeResponseBodyResourceTypeHandlers = None,
        info: GetResourceTypeResponseBodyResourceTypeInfo = None,
        list_only_properties: List[str] = None,
        primary_identifier: str = None,
        product: str = None,
        properties: Dict[str, Any] = None,
        public_properties: List[str] = None,
        read_only_properties: List[str] = None,
        required: List[str] = None,
        resource_type: str = None,
        resource_type_version: str = None,
        sensitive_info_properties: List[str] = None,
        update_only_properties: List[str] = None,
        update_type_properties: List[str] = None,
    ):
        self.create_only_properties = create_only_properties
        self.delete_only_properties = delete_only_properties
        self.filter_properties = filter_properties
        self.get_only_properties = get_only_properties
        self.handlers = handlers
        self.info = info
        self.list_only_properties = list_only_properties
        self.primary_identifier = primary_identifier
        self.product = product
        self.properties = properties
        self.public_properties = public_properties
        self.read_only_properties = read_only_properties
        self.required = required
        self.resource_type = resource_type
        self.resource_type_version = resource_type_version
        self.sensitive_info_properties = sensitive_info_properties
        self.update_only_properties = update_only_properties
        self.update_type_properties = update_type_properties

    def validate(self):
        if self.handlers:
            self.handlers.validate()
        if self.info:
            self.info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_only_properties is not None:
            result['createOnlyProperties'] = self.create_only_properties
        if self.delete_only_properties is not None:
            result['deleteOnlyProperties'] = self.delete_only_properties
        if self.filter_properties is not None:
            result['filterProperties'] = self.filter_properties
        if self.get_only_properties is not None:
            result['getOnlyProperties'] = self.get_only_properties
        if self.handlers is not None:
            result['handlers'] = self.handlers.to_map()
        if self.info is not None:
            result['info'] = self.info.to_map()
        if self.list_only_properties is not None:
            result['listOnlyProperties'] = self.list_only_properties
        if self.primary_identifier is not None:
            result['primaryIdentifier'] = self.primary_identifier
        if self.product is not None:
            result['product'] = self.product
        if self.properties is not None:
            result['properties'] = self.properties
        if self.public_properties is not None:
            result['publicProperties'] = self.public_properties
        if self.read_only_properties is not None:
            result['readOnlyProperties'] = self.read_only_properties
        if self.required is not None:
            result['required'] = self.required
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.resource_type_version is not None:
            result['resourceTypeVersion'] = self.resource_type_version
        if self.sensitive_info_properties is not None:
            result['sensitiveInfoProperties'] = self.sensitive_info_properties
        if self.update_only_properties is not None:
            result['updateOnlyProperties'] = self.update_only_properties
        if self.update_type_properties is not None:
            result['updateTypeProperties'] = self.update_type_properties
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createOnlyProperties') is not None:
            self.create_only_properties = m.get('createOnlyProperties')
        if m.get('deleteOnlyProperties') is not None:
            self.delete_only_properties = m.get('deleteOnlyProperties')
        if m.get('filterProperties') is not None:
            self.filter_properties = m.get('filterProperties')
        if m.get('getOnlyProperties') is not None:
            self.get_only_properties = m.get('getOnlyProperties')
        if m.get('handlers') is not None:
            temp_model = GetResourceTypeResponseBodyResourceTypeHandlers()
            self.handlers = temp_model.from_map(m['handlers'])
        if m.get('info') is not None:
            temp_model = GetResourceTypeResponseBodyResourceTypeInfo()
            self.info = temp_model.from_map(m['info'])
        if m.get('listOnlyProperties') is not None:
            self.list_only_properties = m.get('listOnlyProperties')
        if m.get('primaryIdentifier') is not None:
            self.primary_identifier = m.get('primaryIdentifier')
        if m.get('product') is not None:
            self.product = m.get('product')
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        if m.get('publicProperties') is not None:
            self.public_properties = m.get('publicProperties')
        if m.get('readOnlyProperties') is not None:
            self.read_only_properties = m.get('readOnlyProperties')
        if m.get('required') is not None:
            self.required = m.get('required')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('resourceTypeVersion') is not None:
            self.resource_type_version = m.get('resourceTypeVersion')
        if m.get('sensitiveInfoProperties') is not None:
            self.sensitive_info_properties = m.get('sensitiveInfoProperties')
        if m.get('updateOnlyProperties') is not None:
            self.update_only_properties = m.get('updateOnlyProperties')
        if m.get('updateTypeProperties') is not None:
            self.update_type_properties = m.get('updateTypeProperties')
        return self


class GetResourceTypeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_type: GetResourceTypeResponseBodyResourceType = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.resource_type = resource_type

    def validate(self):
        if self.resource_type:
            self.resource_type.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('resourceType') is not None:
            temp_model = GetResourceTypeResponseBodyResourceType()
            self.resource_type = temp_model.from_map(m['resourceType'])
        return self


class GetResourceTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetResourceTypeResponseBody = None,
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
            temp_model = GetResourceTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskResponseBodyTaskError(TeaModel):
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
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class GetTaskResponseBodyTask(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        error: GetTaskResponseBodyTaskError = None,
        product_code: str = None,
        resource_id: str = None,
        resource_type_code: str = None,
        retry_after: int = None,
        status: str = None,
        task_action: str = None,
        task_id: str = None,
    ):
        self.create_time = create_time
        self.error = error
        self.product_code = product_code
        self.resource_id = resource_id
        self.resource_type_code = resource_type_code
        self.retry_after = retry_after
        self.status = status
        self.task_action = task_action
        self.task_id = task_id

    def validate(self):
        if self.error:
            self.error.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.error is not None:
            result['error'] = self.error.to_map()
        if self.product_code is not None:
            result['productCode'] = self.product_code
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_type_code is not None:
            result['resourceTypeCode'] = self.resource_type_code
        if self.retry_after is not None:
            result['retryAfter'] = self.retry_after
        if self.status is not None:
            result['status'] = self.status
        if self.task_action is not None:
            result['taskAction'] = self.task_action
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('error') is not None:
            temp_model = GetTaskResponseBodyTaskError()
            self.error = temp_model.from_map(m['error'])
        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceTypeCode') is not None:
            self.resource_type_code = m.get('resourceTypeCode')
        if m.get('retryAfter') is not None:
            self.retry_after = m.get('retryAfter')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('taskAction') is not None:
            self.task_action = m.get('taskAction')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class GetTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task: GetTaskResponseBodyTask = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.task = task

    def validate(self):
        if self.task:
            self.task.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.task is not None:
            result['task'] = self.task.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('task') is not None:
            temp_model = GetTaskResponseBodyTask()
            self.task = temp_model.from_map(m['task'])
        return self


class GetTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTaskResponseBody = None,
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
            temp_model = GetTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataSourcesRequest(TeaModel):
    def __init__(
        self,
        filter: Dict[str, Any] = None,
    ):
        self.filter = filter

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter is not None:
            result['filter'] = self.filter
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filter') is not None:
            self.filter = m.get('filter')
        return self


class ListDataSourcesShrinkRequest(TeaModel):
    def __init__(
        self,
        filter_shrink: str = None,
    ):
        self.filter_shrink = filter_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_shrink is not None:
            result['filter'] = self.filter_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filter') is not None:
            self.filter_shrink = m.get('filter')
        return self


class ListDataSourcesResponseBodyDataSources(TeaModel):
    def __init__(
        self,
        data_source_attributes: str = None,
        id: str = None,
    ):
        self.data_source_attributes = data_source_attributes
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_attributes is not None:
            result['dataSourceAttributes'] = self.data_source_attributes
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataSourceAttributes') is not None:
            self.data_source_attributes = m.get('dataSourceAttributes')
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class ListDataSourcesResponseBody(TeaModel):
    def __init__(
        self,
        data_sources: List[ListDataSourcesResponseBodyDataSources] = None,
        request_id: str = None,
    ):
        self.data_sources = data_sources
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data_sources:
            for k in self.data_sources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['dataSources'] = []
        if self.data_sources is not None:
            for k in self.data_sources:
                result['dataSources'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_sources = []
        if m.get('dataSources') is not None:
            for k in m.get('dataSources'):
                temp_model = ListDataSourcesResponseBodyDataSources()
                self.data_sources.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListDataSourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDataSourcesResponseBody = None,
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
            temp_model = ListDataSourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListProductsResponseBodyProducts(TeaModel):
    def __init__(
        self,
        product_code: str = None,
        product_name: str = None,
    ):
        self.product_code = product_code
        self.product_name = product_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_code is not None:
            result['productCode'] = self.product_code
        if self.product_name is not None:
            result['productName'] = self.product_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        return self


class ListProductsResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        products: List[ListProductsResponseBodyProducts] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        # 表示当前调用返回读取到的位置，空代表数据已经读取完毕
        self.next_token = next_token
        self.products = products
        # Id of the request
        self.request_id = request_id
        # TotalCount本次请求条件下的数据总量，此参数为可选参数，默认可不返回
        self.total_count = total_count

    def validate(self):
        if self.products:
            for k in self.products:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        result['products'] = []
        if self.products is not None:
            for k in self.products:
                result['products'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        self.products = []
        if m.get('products') is not None:
            for k in m.get('products'):
                temp_model = ListProductsResponseBodyProducts()
                self.products.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListProductsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProductsResponseBody = None,
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
            temp_model = ListProductsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourceTypesRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        resource_type_codes: List[str] = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.resource_type_codes = resource_type_codes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.resource_type_codes is not None:
            result['resourceTypeCodes'] = self.resource_type_codes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('resourceTypeCodes') is not None:
            self.resource_type_codes = m.get('resourceTypeCodes')
        return self


class ListResourceTypesShrinkRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        resource_type_codes_shrink: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.resource_type_codes_shrink = resource_type_codes_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.resource_type_codes_shrink is not None:
            result['resourceTypeCodes'] = self.resource_type_codes_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('resourceTypeCodes') is not None:
            self.resource_type_codes_shrink = m.get('resourceTypeCodes')
        return self


class ListResourceTypesResponseBodyResourceTypesHandlersCreate(TeaModel):
    def __init__(
        self,
        permissions: List[str] = None,
    ):
        self.permissions = permissions

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.permissions is not None:
            result['permissions'] = self.permissions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('permissions') is not None:
            self.permissions = m.get('permissions')
        return self


class ListResourceTypesResponseBodyResourceTypesHandlersDelete(TeaModel):
    def __init__(
        self,
        permissions: List[str] = None,
    ):
        self.permissions = permissions

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.permissions is not None:
            result['permissions'] = self.permissions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('permissions') is not None:
            self.permissions = m.get('permissions')
        return self


class ListResourceTypesResponseBodyResourceTypesHandlersGet(TeaModel):
    def __init__(
        self,
        permissions: List[str] = None,
    ):
        self.permissions = permissions

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.permissions is not None:
            result['permissions'] = self.permissions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('permissions') is not None:
            self.permissions = m.get('permissions')
        return self


class ListResourceTypesResponseBodyResourceTypesHandlersList(TeaModel):
    def __init__(
        self,
        permissions: List[str] = None,
    ):
        self.permissions = permissions

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.permissions is not None:
            result['permissions'] = self.permissions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('permissions') is not None:
            self.permissions = m.get('permissions')
        return self


class ListResourceTypesResponseBodyResourceTypesHandlersUpdate(TeaModel):
    def __init__(
        self,
        permissions: List[str] = None,
    ):
        self.permissions = permissions

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.permissions is not None:
            result['permissions'] = self.permissions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('permissions') is not None:
            self.permissions = m.get('permissions')
        return self


class ListResourceTypesResponseBodyResourceTypesHandlers(TeaModel):
    def __init__(
        self,
        create: ListResourceTypesResponseBodyResourceTypesHandlersCreate = None,
        delete: ListResourceTypesResponseBodyResourceTypesHandlersDelete = None,
        get: ListResourceTypesResponseBodyResourceTypesHandlersGet = None,
        list: ListResourceTypesResponseBodyResourceTypesHandlersList = None,
        update: ListResourceTypesResponseBodyResourceTypesHandlersUpdate = None,
    ):
        self.create = create
        self.delete = delete
        self.get = get
        self.list = list
        self.update = update

    def validate(self):
        if self.create:
            self.create.validate()
        if self.delete:
            self.delete.validate()
        if self.get:
            self.get.validate()
        if self.list:
            self.list.validate()
        if self.update:
            self.update.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create is not None:
            result['create'] = self.create.to_map()
        if self.delete is not None:
            result['delete'] = self.delete.to_map()
        if self.get is not None:
            result['get'] = self.get.to_map()
        if self.list is not None:
            result['list'] = self.list.to_map()
        if self.update is not None:
            result['update'] = self.update.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('create') is not None:
            temp_model = ListResourceTypesResponseBodyResourceTypesHandlersCreate()
            self.create = temp_model.from_map(m['create'])
        if m.get('delete') is not None:
            temp_model = ListResourceTypesResponseBodyResourceTypesHandlersDelete()
            self.delete = temp_model.from_map(m['delete'])
        if m.get('get') is not None:
            temp_model = ListResourceTypesResponseBodyResourceTypesHandlersGet()
            self.get = temp_model.from_map(m['get'])
        if m.get('list') is not None:
            temp_model = ListResourceTypesResponseBodyResourceTypesHandlersList()
            self.list = temp_model.from_map(m['list'])
        if m.get('update') is not None:
            temp_model = ListResourceTypesResponseBodyResourceTypesHandlersUpdate()
            self.update = temp_model.from_map(m['update'])
        return self


class ListResourceTypesResponseBodyResourceTypesInfo(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        delivery_scope: str = None,
        description: str = None,
        title: str = None,
    ):
        self.charge_type = charge_type
        self.delivery_scope = delivery_scope
        self.description = description
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.delivery_scope is not None:
            result['deliveryScope'] = self.delivery_scope
        if self.description is not None:
            result['description'] = self.description
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('deliveryScope') is not None:
            self.delivery_scope = m.get('deliveryScope')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class ListResourceTypesResponseBodyResourceTypes(TeaModel):
    def __init__(
        self,
        create_only_properties: List[str] = None,
        delete_only_properties: List[str] = None,
        filter_properties: List[str] = None,
        get_only_properties: List[str] = None,
        handlers: ListResourceTypesResponseBodyResourceTypesHandlers = None,
        info: ListResourceTypesResponseBodyResourceTypesInfo = None,
        list_only_properties: List[str] = None,
        primary_identifier: str = None,
        product: str = None,
        properties: Dict[str, Any] = None,
        public_properties: List[str] = None,
        read_only_properties: List[str] = None,
        required: List[str] = None,
        resource_type: str = None,
        resource_type_version: str = None,
        sensitive_info_properties: List[str] = None,
        update_only_properties: List[str] = None,
        update_type_properties: List[str] = None,
    ):
        self.create_only_properties = create_only_properties
        self.delete_only_properties = delete_only_properties
        self.filter_properties = filter_properties
        self.get_only_properties = get_only_properties
        self.handlers = handlers
        self.info = info
        self.list_only_properties = list_only_properties
        self.primary_identifier = primary_identifier
        self.product = product
        self.properties = properties
        self.public_properties = public_properties
        self.read_only_properties = read_only_properties
        self.required = required
        self.resource_type = resource_type
        self.resource_type_version = resource_type_version
        self.sensitive_info_properties = sensitive_info_properties
        self.update_only_properties = update_only_properties
        self.update_type_properties = update_type_properties

    def validate(self):
        if self.handlers:
            self.handlers.validate()
        if self.info:
            self.info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_only_properties is not None:
            result['createOnlyProperties'] = self.create_only_properties
        if self.delete_only_properties is not None:
            result['deleteOnlyProperties'] = self.delete_only_properties
        if self.filter_properties is not None:
            result['filterProperties'] = self.filter_properties
        if self.get_only_properties is not None:
            result['getOnlyProperties'] = self.get_only_properties
        if self.handlers is not None:
            result['handlers'] = self.handlers.to_map()
        if self.info is not None:
            result['info'] = self.info.to_map()
        if self.list_only_properties is not None:
            result['listOnlyProperties'] = self.list_only_properties
        if self.primary_identifier is not None:
            result['primaryIdentifier'] = self.primary_identifier
        if self.product is not None:
            result['product'] = self.product
        if self.properties is not None:
            result['properties'] = self.properties
        if self.public_properties is not None:
            result['publicProperties'] = self.public_properties
        if self.read_only_properties is not None:
            result['readOnlyProperties'] = self.read_only_properties
        if self.required is not None:
            result['required'] = self.required
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.resource_type_version is not None:
            result['resourceTypeVersion'] = self.resource_type_version
        if self.sensitive_info_properties is not None:
            result['sensitiveInfoProperties'] = self.sensitive_info_properties
        if self.update_only_properties is not None:
            result['updateOnlyProperties'] = self.update_only_properties
        if self.update_type_properties is not None:
            result['updateTypeProperties'] = self.update_type_properties
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createOnlyProperties') is not None:
            self.create_only_properties = m.get('createOnlyProperties')
        if m.get('deleteOnlyProperties') is not None:
            self.delete_only_properties = m.get('deleteOnlyProperties')
        if m.get('filterProperties') is not None:
            self.filter_properties = m.get('filterProperties')
        if m.get('getOnlyProperties') is not None:
            self.get_only_properties = m.get('getOnlyProperties')
        if m.get('handlers') is not None:
            temp_model = ListResourceTypesResponseBodyResourceTypesHandlers()
            self.handlers = temp_model.from_map(m['handlers'])
        if m.get('info') is not None:
            temp_model = ListResourceTypesResponseBodyResourceTypesInfo()
            self.info = temp_model.from_map(m['info'])
        if m.get('listOnlyProperties') is not None:
            self.list_only_properties = m.get('listOnlyProperties')
        if m.get('primaryIdentifier') is not None:
            self.primary_identifier = m.get('primaryIdentifier')
        if m.get('product') is not None:
            self.product = m.get('product')
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        if m.get('publicProperties') is not None:
            self.public_properties = m.get('publicProperties')
        if m.get('readOnlyProperties') is not None:
            self.read_only_properties = m.get('readOnlyProperties')
        if m.get('required') is not None:
            self.required = m.get('required')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('resourceTypeVersion') is not None:
            self.resource_type_version = m.get('resourceTypeVersion')
        if m.get('sensitiveInfoProperties') is not None:
            self.sensitive_info_properties = m.get('sensitiveInfoProperties')
        if m.get('updateOnlyProperties') is not None:
            self.update_only_properties = m.get('updateOnlyProperties')
        if m.get('updateTypeProperties') is not None:
            self.update_type_properties = m.get('updateTypeProperties')
        return self


class ListResourceTypesResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        resource_types: List[ListResourceTypesResponseBodyResourceTypes] = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        # 表示当前调用返回读取到的位置，空代表数据已经读取完毕
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        self.resource_types = resource_types
        # TotalCount本次请求条件下的数据总量，此参数为可选参数，默认可不返回
        self.total_count = total_count

    def validate(self):
        if self.resource_types:
            for k in self.resource_types:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['resourceTypes'] = []
        if self.resource_types is not None:
            for k in self.resource_types:
                result['resourceTypes'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.resource_types = []
        if m.get('resourceTypes') is not None:
            for k in m.get('resourceTypes'):
                temp_model = ListResourceTypesResponseBodyResourceTypes()
                self.resource_types.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListResourceTypesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListResourceTypesResponseBody = None,
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
            temp_model = ListResourceTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourcesHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_roag_cache: bool = None,
    ):
        self.common_headers = common_headers
        self.x_roag_cache = x_roag_cache

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_roag_cache is not None:
            result['x-roag-cache'] = self.x_roag_cache
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-roag-cache') is not None:
            self.x_roag_cache = m.get('x-roag-cache')
        return self


class ListResourcesRequest(TeaModel):
    def __init__(
        self,
        data_type: str = None,
        filter: Dict[str, Any] = None,
        max_results: int = None,
        next_token: str = None,
        page_num: int = None,
        page_size: int = None,
        region_ids: List[str] = None,
    ):
        self.data_type = data_type
        self.filter = filter
        self.max_results = max_results
        self.next_token = next_token
        self.page_num = page_num
        self.page_size = page_size
        self.region_ids = region_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.filter is not None:
            result['filter'] = self.filter
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.region_ids is not None:
            result['regionIds'] = self.region_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('filter') is not None:
            self.filter = m.get('filter')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('regionIds') is not None:
            self.region_ids = m.get('regionIds')
        return self


class ListResourcesShrinkRequest(TeaModel):
    def __init__(
        self,
        data_type: str = None,
        filter_shrink: str = None,
        max_results: int = None,
        next_token: str = None,
        page_num: int = None,
        page_size: int = None,
        region_ids_shrink: str = None,
    ):
        self.data_type = data_type
        self.filter_shrink = filter_shrink
        self.max_results = max_results
        self.next_token = next_token
        self.page_num = page_num
        self.page_size = page_size
        self.region_ids_shrink = region_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.filter_shrink is not None:
            result['filter'] = self.filter_shrink
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.region_ids_shrink is not None:
            result['regionIds'] = self.region_ids_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('filter') is not None:
            self.filter_shrink = m.get('filter')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('regionIds') is not None:
            self.region_ids_shrink = m.get('regionIds')
        return self


class ListResourcesResponseBodyResources(TeaModel):
    def __init__(
        self,
        product_code: str = None,
        region_id: str = None,
        resource_attributes: str = None,
        resource_id: str = None,
        resource_type_code: str = None,
    ):
        self.product_code = product_code
        self.region_id = region_id
        self.resource_attributes = resource_attributes
        self.resource_id = resource_id
        self.resource_type_code = resource_type_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_code is not None:
            result['productCode'] = self.product_code
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.resource_attributes is not None:
            result['resourceAttributes'] = self.resource_attributes
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_type_code is not None:
            result['resourceTypeCode'] = self.resource_type_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('resourceAttributes') is not None:
            self.resource_attributes = m.get('resourceAttributes')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceTypeCode') is not None:
            self.resource_type_code = m.get('resourceTypeCode')
        return self


class ListResourcesResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        page_num: int = None,
        page_size: int = None,
        request_id: str = None,
        resources: List[ListResourcesResponseBodyResources] = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.page_num = page_num
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        self.resources = resources
        self.total_count = total_count

    def validate(self):
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['resources'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.resources = []
        if m.get('resources') is not None:
            for k in m.get('resources'):
                temp_model = ListResourcesResponseBodyResources()
                self.resources.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListResourcesResponseBody = None,
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
            temp_model = ListResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTasksRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        task_ids: List[str] = None,
    ):
        # 本次读取的最大数据记录数量
        self.max_results = max_results
        # 标记当前开始读取的位置，置空表示从头开始
        self.next_token = next_token
        # 任务Id列表
        self.task_ids = task_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.task_ids is not None:
            result['taskIds'] = self.task_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('taskIds') is not None:
            self.task_ids = m.get('taskIds')
        return self


class ListTasksShrinkRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        task_ids_shrink: str = None,
    ):
        # 本次读取的最大数据记录数量
        self.max_results = max_results
        # 标记当前开始读取的位置，置空表示从头开始
        self.next_token = next_token
        # 任务Id列表
        self.task_ids_shrink = task_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.task_ids_shrink is not None:
            result['taskIds'] = self.task_ids_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('taskIds') is not None:
            self.task_ids_shrink = m.get('taskIds')
        return self


class ListTasksResponseBodyTasksError(TeaModel):
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
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class ListTasksResponseBodyTasks(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        error: ListTasksResponseBodyTasksError = None,
        product_code: str = None,
        resource_id: str = None,
        resource_type_code: str = None,
        retry_after: int = None,
        status: str = None,
        task_action: str = None,
        task_id: str = None,
    ):
        self.create_time = create_time
        self.error = error
        self.product_code = product_code
        self.resource_id = resource_id
        self.resource_type_code = resource_type_code
        self.retry_after = retry_after
        self.status = status
        self.task_action = task_action
        self.task_id = task_id

    def validate(self):
        if self.error:
            self.error.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.error is not None:
            result['error'] = self.error.to_map()
        if self.product_code is not None:
            result['productCode'] = self.product_code
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_type_code is not None:
            result['resourceTypeCode'] = self.resource_type_code
        if self.retry_after is not None:
            result['retryAfter'] = self.retry_after
        if self.status is not None:
            result['status'] = self.status
        if self.task_action is not None:
            result['taskAction'] = self.task_action
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('error') is not None:
            temp_model = ListTasksResponseBodyTasksError()
            self.error = temp_model.from_map(m['error'])
        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceTypeCode') is not None:
            self.resource_type_code = m.get('resourceTypeCode')
        if m.get('retryAfter') is not None:
            self.retry_after = m.get('retryAfter')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('taskAction') is not None:
            self.task_action = m.get('taskAction')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class ListTasksResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        tasks: List[ListTasksResponseBodyTasks] = None,
        total_count: int = None,
    ):
        # maxResults本次请求所返回的最大记录条数
        self.max_results = max_results
        # 表示当前调用返回读取到的位置，空代表数据已经读取完毕
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        self.tasks = tasks
        # totalCount本次请求条件下的数据总量，此参数为可选参数，默认可不返回
        self.total_count = total_count

    def validate(self):
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['tasks'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.tasks = []
        if m.get('tasks') is not None:
            for k in m.get('tasks'):
                temp_model = ListTasksResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTasksResponseBody = None,
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
            temp_model = ListTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReloadResourcesRequest(TeaModel):
    def __init__(
        self,
        region_ids: List[str] = None,
    ):
        self.region_ids = region_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_ids is not None:
            result['regionIds'] = self.region_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('regionIds') is not None:
            self.region_ids = m.get('regionIds')
        return self


class ReloadResourcesShrinkRequest(TeaModel):
    def __init__(
        self,
        region_ids_shrink: str = None,
    ):
        self.region_ids_shrink = region_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_ids_shrink is not None:
            result['regionIds'] = self.region_ids_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('regionIds') is not None:
            self.region_ids_shrink = m.get('regionIds')
        return self


class ReloadResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class ReloadResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReloadResourcesResponseBody = None,
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
            temp_model = ReloadResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateResourceRequest(TeaModel):
    def __init__(
        self,
        body: str = None,
        resource_type_version: str = None,
    ):
        self.body = body
        self.resource_type_version = resource_type_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.resource_type_version is not None:
            result['resourceTypeVersion'] = self.resource_type_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('resourceTypeVersion') is not None:
            self.resource_type_version = m.get('resourceTypeVersion')
        return self


class UpdateResourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        # 请求id
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class UpdateResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateResourceResponseBody = None,
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
            temp_model = UpdateResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


