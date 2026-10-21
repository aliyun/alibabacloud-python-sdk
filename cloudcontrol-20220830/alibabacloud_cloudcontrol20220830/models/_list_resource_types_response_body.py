# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_cloudcontrol20220830 import models as main_models
from darabonba.model import DaraModel

class ListResourceTypesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        resource_types: List[main_models.ListResourceTypesResponseBodyResourceTypes] = None,
        total_count: int = None,
    ):
        # The maximum number of entries returned.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The ID of a request.
        self.request_id = request_id
        # The information about the resource types.
        self.resource_types = resource_types
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.resource_types:
            for v1 in self.resource_types:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['resourceTypes'] = []
        if self.resource_types is not None:
            for k1 in self.resource_types:
                result['resourceTypes'].append(k1.to_map() if k1 else None)

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
            for k1 in m.get('resourceTypes'):
                temp_model = main_models.ListResourceTypesResponseBodyResourceTypes()
                self.resource_types.append(temp_model.from_map(k1))

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListResourceTypesResponseBodyResourceTypes(DaraModel):
    def __init__(
        self,
        create_only_properties: List[str] = None,
        delete_only_properties: List[str] = None,
        filter_properties: List[str] = None,
        get_only_properties: List[str] = None,
        get_response_properties: List[str] = None,
        handlers: main_models.ListResourceTypesResponseBodyResourceTypesHandlers = None,
        info: main_models.ListResourceTypesResponseBodyResourceTypesInfo = None,
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
        # The properties that are specific to the create operation. You need to specify these properties when you create the resource. These properties are not returned when you query the resource.
        self.create_only_properties = create_only_properties
        # The properties that are specific to the delete operation. You need to specify these properties when you delete the resource. These properties are not returned when you query the resource.
        self.delete_only_properties = delete_only_properties
        # The properties that can be used to filter the resource when you list the resource.
        self.filter_properties = filter_properties
        # The properties that are specific to the query operation. You need to specify these properties when you query the resource. These properties are not returned in the query result.
        self.get_only_properties = get_only_properties
        # The properties that are returned when you query the resource.
        self.get_response_properties = get_response_properties
        # The information about the operation, including the required Resource Access Management (RAM) permissions.
        self.handlers = handlers
        # The information about the resource type.
        self.info = info
        # The properties that are specific to the list operation. You need to specify these properties when you list the resource. These properties are not returned when you query the resource.
        self.list_only_properties = list_only_properties
        # The properties that are returned when you list the resource.
        self.list_response_properties = list_response_properties
        # The ID of the resource.
        self.primary_identifier = primary_identifier
        # The code of the service.
        self.product = product
        # The resource properties. The key specifies the property name and the value specifies the details of the property.
        self.properties = properties
        # The common properties of the resource. The common properties are not operation-specific.
        self.public_properties = public_properties
        # The read-only properties. These properties are returned only when you list or query the resource. You do not need to specify these properties when you create or update the resource.
        self.read_only_properties = read_only_properties
        # The properties that must be specified when you create the resource.
        self.required = required
        # The resource type.
        self.resource_type = resource_type
        # The sensitive properties, such as the password.
        self.sensitive_info_properties = sensitive_info_properties
        # The properties that are specific to the update operation. You need to specify these properties when you update the resource. These properties are not returned when you query the resource.
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
            temp_model = main_models.ListResourceTypesResponseBodyResourceTypesHandlers()
            self.handlers = temp_model.from_map(m.get('handlers'))

        if m.get('info') is not None:
            temp_model = main_models.ListResourceTypesResponseBodyResourceTypesInfo()
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

class ListResourceTypesResponseBodyResourceTypesInfo(DaraModel):
    def __init__(
        self,
        charge_type: str = None,
        delivery_scope: str = None,
        description: str = None,
        title: str = None,
    ):
        # Billing method\\
        # paid free
        self.charge_type = charge_type
        # The deployment level of the resource.
        # 
        # center
        # 
        # region
        # 
        # zone
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

class ListResourceTypesResponseBodyResourceTypesHandlers(DaraModel):
    def __init__(
        self,
        create: main_models.ListResourceTypesResponseBodyResourceTypesHandlersCreate = None,
        delete: main_models.ListResourceTypesResponseBodyResourceTypesHandlersDelete = None,
        get: main_models.ListResourceTypesResponseBodyResourceTypesHandlersGet = None,
        list: main_models.ListResourceTypesResponseBodyResourceTypesHandlersList = None,
        update: main_models.ListResourceTypesResponseBodyResourceTypesHandlersUpdate = None,
    ):
        # The information about the create operation.
        self.create = create
        # The information about the delete operation.
        self.delete = delete
        # The information about the query operation.
        self.get = get
        # The information about the list operation.
        self.list = list
        # The information about the update operation.
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
            temp_model = main_models.ListResourceTypesResponseBodyResourceTypesHandlersCreate()
            self.create = temp_model.from_map(m.get('create'))

        if m.get('delete') is not None:
            temp_model = main_models.ListResourceTypesResponseBodyResourceTypesHandlersDelete()
            self.delete = temp_model.from_map(m.get('delete'))

        if m.get('get') is not None:
            temp_model = main_models.ListResourceTypesResponseBodyResourceTypesHandlersGet()
            self.get = temp_model.from_map(m.get('get'))

        if m.get('list') is not None:
            temp_model = main_models.ListResourceTypesResponseBodyResourceTypesHandlersList()
            self.list = temp_model.from_map(m.get('list'))

        if m.get('update') is not None:
            temp_model = main_models.ListResourceTypesResponseBodyResourceTypesHandlersUpdate()
            self.update = temp_model.from_map(m.get('update'))

        return self

class ListResourceTypesResponseBodyResourceTypesHandlersUpdate(DaraModel):
    def __init__(
        self,
        permissions: List[str] = None,
    ):
        # The RAM permissions required.
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

class ListResourceTypesResponseBodyResourceTypesHandlersList(DaraModel):
    def __init__(
        self,
        permissions: List[str] = None,
    ):
        # The RAM permissions required.
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

class ListResourceTypesResponseBodyResourceTypesHandlersGet(DaraModel):
    def __init__(
        self,
        permissions: List[str] = None,
    ):
        # The RAM permissions required.
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

class ListResourceTypesResponseBodyResourceTypesHandlersDelete(DaraModel):
    def __init__(
        self,
        permissions: List[str] = None,
    ):
        # The RAM permissions required.
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

class ListResourceTypesResponseBodyResourceTypesHandlersCreate(DaraModel):
    def __init__(
        self,
        permissions: List[str] = None,
    ):
        # The RAM permissions required.
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

