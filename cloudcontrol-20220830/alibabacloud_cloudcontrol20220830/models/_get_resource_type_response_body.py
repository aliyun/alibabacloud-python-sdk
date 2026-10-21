# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_cloudcontrol20220830 import models as main_models
from darabonba.model import DaraModel

class GetResourceTypeResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resource_type: main_models.GetResourceTypeResponseBodyResourceType = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The resource type.
        self.resource_type = resource_type

    def validate(self):
        if self.resource_type:
            self.resource_type.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
            temp_model = main_models.GetResourceTypeResponseBodyResourceType()
            self.resource_type = temp_model.from_map(m.get('resourceType'))

        return self

class GetResourceTypeResponseBodyResourceType(DaraModel):
    def __init__(
        self,
        create_only_properties: List[str] = None,
        delete_only_properties: List[str] = None,
        filter_properties: List[str] = None,
        get_only_properties: List[str] = None,
        get_response_properties: List[str] = None,
        handlers: main_models.GetResourceTypeResponseBodyResourceTypeHandlers = None,
        info: main_models.GetResourceTypeResponseBodyResourceTypeInfo = None,
        list_only_properties: List[str] = None,
        list_response_properties: List[str] = None,
        primary_identifier: str = None,
        product: str = None,
        properties: Dict[str, Any] = None,
        public_properties: List[str] = None,
        read_only_properties: List[str] = None,
        required: List[str] = None,
        resource_type: str = None,
        sensitive_info_properties: List[str] = None,
        update_only_properties: List[str] = None,
        update_type_properties: List[str] = None,
    ):
        # The properties exclusive to the create operation. These properties are not returned in resource query operations but are required as input parameters for the create operation.
        self.create_only_properties = create_only_properties
        # The properties exclusive to the delete operation. These properties are not returned in resource query operations but are required as input parameters for the delete operation.
        self.delete_only_properties = delete_only_properties
        # The properties that can be used as filter parameters in the list operation.
        self.filter_properties = filter_properties
        # The properties exclusive to the get operation. These properties are not returned in resource query operations but are required as input parameters for the get operation.
        self.get_only_properties = get_only_properties
        # The properties returned by the get operation.
        self.get_response_properties = get_response_properties
        # The supported resource operations, including RAM permissions.
        self.handlers = handlers
        # The basic information about the resource type.
        self.info = info
        # The properties exclusive to the list operation. These properties are not returned in resource query operations but are required as input parameters for the list operation.
        self.list_only_properties = list_only_properties
        # The properties returned by the list operation.
        self.list_response_properties = list_response_properties
        # The resource ID.
        self.primary_identifier = primary_identifier
        # The product code.
        self.product = product
        # The resource property definitions. The key is the property name, and the value is the detailed property information.
        self.properties = properties
        # The common properties that represent basic resource attributes. These are not operation-specific properties.
        self.public_properties = public_properties
        # The read-only properties. These properties are returned only in list or get operations and cannot be used as input parameters for create or update operations.
        self.read_only_properties = read_only_properties
        # The required parameters for resource creation.
        self.required = required
        # The resource type. If the resource has a parent resource, the format is {parentResourceTypeCode/resourceTypeCode}.
        self.resource_type = resource_type
        # The sensitive properties, such as passwords.
        self.sensitive_info_properties = sensitive_info_properties
        # The properties exclusive to the update operation. These properties are not returned in resource query operations but are required as input parameters for the update operation.
        self.update_only_properties = update_only_properties
        # The properties that can be modified.
        self.update_type_properties = update_type_properties

    def validate(self):
        if self.handlers:
            self.handlers.validate()
        if self.info:
            self.info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_only_properties is not None:
            result['createOnlyProperties'] = self.create_only_properties

        if self.delete_only_properties is not None:
            result['deleteOnlyProperties'] = self.delete_only_properties

        if self.filter_properties is not None:
            result['filterProperties'] = self.filter_properties

        if self.get_only_properties is not None:
            result['getOnlyProperties'] = self.get_only_properties

        if self.get_response_properties is not None:
            result['getResponseProperties'] = self.get_response_properties

        if self.handlers is not None:
            result['handlers'] = self.handlers.to_map()

        if self.info is not None:
            result['info'] = self.info.to_map()

        if self.list_only_properties is not None:
            result['listOnlyProperties'] = self.list_only_properties

        if self.list_response_properties is not None:
            result['listResponseProperties'] = self.list_response_properties

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

        if m.get('getResponseProperties') is not None:
            self.get_response_properties = m.get('getResponseProperties')

        if m.get('handlers') is not None:
            temp_model = main_models.GetResourceTypeResponseBodyResourceTypeHandlers()
            self.handlers = temp_model.from_map(m.get('handlers'))

        if m.get('info') is not None:
            temp_model = main_models.GetResourceTypeResponseBodyResourceTypeInfo()
            self.info = temp_model.from_map(m.get('info'))

        if m.get('listOnlyProperties') is not None:
            self.list_only_properties = m.get('listOnlyProperties')

        if m.get('listResponseProperties') is not None:
            self.list_response_properties = m.get('listResponseProperties')

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

        if m.get('sensitiveInfoProperties') is not None:
            self.sensitive_info_properties = m.get('sensitiveInfoProperties')

        if m.get('updateOnlyProperties') is not None:
            self.update_only_properties = m.get('updateOnlyProperties')

        if m.get('updateTypeProperties') is not None:
            self.update_type_properties = m.get('updateTypeProperties')

        return self

class GetResourceTypeResponseBodyResourceTypeInfo(DaraModel):
    def __init__(
        self,
        charge_type: str = None,
        delivery_scope: str = None,
        description: str = None,
        title: str = None,
    ):
        # The billing method. Valid values:
        # 
        # paid: paid.
        # 
        # free: free.
        self.charge_type = charge_type
        # The delivery scope. Valid values: 
        # 
        # center: centralized deployment.
        # 
        # region: region-level deployment.
        # 
        # zone: zone-level deployment.
        self.delivery_scope = delivery_scope
        # The description of the resource type.
        self.description = description
        # The name of the resource type.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class GetResourceTypeResponseBodyResourceTypeHandlers(DaraModel):
    def __init__(
        self,
        create: main_models.GetResourceTypeResponseBodyResourceTypeHandlersCreate = None,
        delete: main_models.GetResourceTypeResponseBodyResourceTypeHandlersDelete = None,
        get: main_models.GetResourceTypeResponseBodyResourceTypeHandlersGet = None,
        list: main_models.GetResourceTypeResponseBodyResourceTypeHandlersList = None,
        update: main_models.GetResourceTypeResponseBodyResourceTypeHandlersUpdate = None,
    ):
        # The information associated with the create operation.
        self.create = create
        # The information associated with the delete operation.
        self.delete = delete
        # The information associated with the get operation.
        self.get = get
        # The information associated with the list operation.
        self.list = list
        # The information associated with the update operation.
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
            temp_model = main_models.GetResourceTypeResponseBodyResourceTypeHandlersCreate()
            self.create = temp_model.from_map(m.get('create'))

        if m.get('delete') is not None:
            temp_model = main_models.GetResourceTypeResponseBodyResourceTypeHandlersDelete()
            self.delete = temp_model.from_map(m.get('delete'))

        if m.get('get') is not None:
            temp_model = main_models.GetResourceTypeResponseBodyResourceTypeHandlersGet()
            self.get = temp_model.from_map(m.get('get'))

        if m.get('list') is not None:
            temp_model = main_models.GetResourceTypeResponseBodyResourceTypeHandlersList()
            self.list = temp_model.from_map(m.get('list'))

        if m.get('update') is not None:
            temp_model = main_models.GetResourceTypeResponseBodyResourceTypeHandlersUpdate()
            self.update = temp_model.from_map(m.get('update'))

        return self

class GetResourceTypeResponseBodyResourceTypeHandlersUpdate(DaraModel):
    def __init__(
        self,
        permissions: List[str] = None,
    ):
        # The required RAM permissions.
        self.permissions = permissions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.permissions is not None:
            result['permissions'] = self.permissions

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('permissions') is not None:
            self.permissions = m.get('permissions')

        return self

class GetResourceTypeResponseBodyResourceTypeHandlersList(DaraModel):
    def __init__(
        self,
        permissions: List[str] = None,
    ):
        # The required RAM permissions.
        self.permissions = permissions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.permissions is not None:
            result['permissions'] = self.permissions

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('permissions') is not None:
            self.permissions = m.get('permissions')

        return self

class GetResourceTypeResponseBodyResourceTypeHandlersGet(DaraModel):
    def __init__(
        self,
        permissions: List[str] = None,
    ):
        # The required RAM permissions.
        self.permissions = permissions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.permissions is not None:
            result['permissions'] = self.permissions

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('permissions') is not None:
            self.permissions = m.get('permissions')

        return self

class GetResourceTypeResponseBodyResourceTypeHandlersDelete(DaraModel):
    def __init__(
        self,
        permissions: List[str] = None,
    ):
        # The required RAM permissions.
        self.permissions = permissions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.permissions is not None:
            result['permissions'] = self.permissions

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('permissions') is not None:
            self.permissions = m.get('permissions')

        return self

class GetResourceTypeResponseBodyResourceTypeHandlersCreate(DaraModel):
    def __init__(
        self,
        permissions: List[str] = None,
    ):
        # The required RAM permissions.
        self.permissions = permissions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.permissions is not None:
            result['permissions'] = self.permissions

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('permissions') is not None:
            self.permissions = m.get('permissions')

        return self

