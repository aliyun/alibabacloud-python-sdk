# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListComputeResourcesResponseBody(DaraModel):
    def __init__(
        self,
        paging_info: main_models.ListComputeResourcesResponseBodyPagingInfo = None,
        request_id: str = None,
    ):
        # Pagination information.
        self.paging_info = paging_info
        # The request ID. Used to locate logs and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.paging_info:
            self.paging_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.paging_info is not None:
            result['PagingInfo'] = self.paging_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PagingInfo') is not None:
            temp_model = main_models.ListComputeResourcesResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m.get('PagingInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListComputeResourcesResponseBodyPagingInfo(DaraModel):
    def __init__(
        self,
        compute_resources: List[main_models.ListComputeResourcesResponseBodyPagingInfoComputeResources] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The list of computing resources. Each element is a computing resource group that contains information about the development environment (if any) and the production environment.
        self.compute_resources = compute_resources
        # The current page number.
        self.page_number = page_number
        # The number of records per page.
        self.page_size = page_size
        # The total number of records.
        self.total_count = total_count

    def validate(self):
        if self.compute_resources:
            for v1 in self.compute_resources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ComputeResources'] = []
        if self.compute_resources is not None:
            for k1 in self.compute_resources:
                result['ComputeResources'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.compute_resources = []
        if m.get('ComputeResources') is not None:
            for k1 in m.get('ComputeResources'):
                temp_model = main_models.ListComputeResourcesResponseBodyPagingInfoComputeResources()
                self.compute_resources.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListComputeResourcesResponseBodyPagingInfoComputeResources(DaraModel):
    def __init__(
        self,
        compute_resource: List[main_models.ListComputeResourcesResponseBodyPagingInfoComputeResourcesComputeResource] = None,
        name: str = None,
        type: str = None,
    ):
        # Details of a single computing resource.
        self.compute_resource = compute_resource
        # The name of the computing resource.
        self.name = name
        # The type of the computing resource.
        self.type = type

    def validate(self):
        if self.compute_resource:
            for v1 in self.compute_resource:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ComputeResource'] = []
        if self.compute_resource is not None:
            for k1 in self.compute_resource:
                result['ComputeResource'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.compute_resource = []
        if m.get('ComputeResource') is not None:
            for k1 in m.get('ComputeResource'):
                temp_model = main_models.ListComputeResourcesResponseBodyPagingInfoComputeResourcesComputeResource()
                self.compute_resource.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListComputeResourcesResponseBodyPagingInfoComputeResourcesComputeResource(DaraModel):
    def __init__(
        self,
        connection_properties: Any = None,
        connection_properties_mode: str = None,
        create_time: int = None,
        create_user: str = None,
        description: str = None,
        id: int = None,
        modify_time: int = None,
        modify_user: str = None,
        whether_default: bool = None,
    ):
        # The category of the added compute resource. Different types have different subtypes with corresponding parameter constraints. Examples: InstanceMode: The instance mode. UrlMode: The connection string mode.
        self.connection_properties = connection_properties
        # The specific connection configuration details for the computing resource, including the connection address, access identity, and environment information. envType, which specifies the computing resource environment, is a property of this object. Valid values:
        # 
        # *   Dev
        # *   Prod Different types of computing resources have different attribute specifications under different configuration modes (ConnectionPropertiesMode).
        self.connection_properties_mode = connection_properties_mode
        # The creation time (timestamp).
        self.create_time = create_time
        # The creator ID.
        self.create_user = create_user
        # The unique identifier of the computing resource.
        self.description = description
        # The computing resource ID, which is the unique identifier for the resource.
        self.id = id
        # The last modified time of the computing resource (timestamp).
        self.modify_time = modify_time
        # The modifier ID.
        self.modify_user = modify_user
        # Specifies whether it is the default compute resource.
        self.whether_default = whether_default

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_properties is not None:
            result['ConnectionProperties'] = self.connection_properties

        if self.connection_properties_mode is not None:
            result['ConnectionPropertiesMode'] = self.connection_properties_mode

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_user is not None:
            result['CreateUser'] = self.create_user

        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.modify_user is not None:
            result['ModifyUser'] = self.modify_user

        if self.whether_default is not None:
            result['WhetherDefault'] = self.whether_default

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionProperties') is not None:
            self.connection_properties = m.get('ConnectionProperties')

        if m.get('ConnectionPropertiesMode') is not None:
            self.connection_properties_mode = m.get('ConnectionPropertiesMode')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('ModifyUser') is not None:
            self.modify_user = m.get('ModifyUser')

        if m.get('WhetherDefault') is not None:
            self.whether_default = m.get('WhetherDefault')

        return self

