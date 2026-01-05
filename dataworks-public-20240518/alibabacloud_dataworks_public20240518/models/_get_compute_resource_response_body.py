# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetComputeResourceResponseBody(DaraModel):
    def __init__(
        self,
        compute_resource: main_models.GetComputeResourceResponseBodyComputeResource = None,
        request_id: str = None,
    ):
        # The details of the computing resource.
        self.compute_resource = compute_resource
        # The request ID. You can use the request ID to locate logs and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.compute_resource:
            self.compute_resource.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compute_resource is not None:
            result['ComputeResource'] = self.compute_resource.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComputeResource') is not None:
            temp_model = main_models.GetComputeResourceResponseBodyComputeResource()
            self.compute_resource = temp_model.from_map(m.get('ComputeResource'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetComputeResourceResponseBodyComputeResource(DaraModel):
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
        name: str = None,
        project_id: int = None,
        qualified_name: str = None,
        type: str = None,
        whether_default: bool = None,
    ):
        # The specific connection configuration details for the computing resource, including the connection address, access identity, and environment information. envType, which specifies the computing resource environment, is a property of this object. Valid values:
        # 
        # *   Dev
        # *   Prod Different types of computing resources have different attribute specifications under various configuration modes (ConnectionPropertiesMode).
        self.connection_properties = connection_properties
        # The addition category of the computing resource. Different types will have different subtypes, each with corresponding parameter constraints. For instance:
        # 
        # *   InstanceMode: Instance mode
        # *   UrlMode: Connection String Mode
        # *   CdhMode: CDH mode
        self.connection_properties_mode = connection_properties_mode
        # The creation time, in timestamp format.
        self.create_time = create_time
        # The ID of the creator.
        self.create_user = create_user
        # The description of the computing resource.
        self.description = description
        # The ID of the computing resource.
        self.id = id
        # The last modification time, in timestamp format.
        self.modify_time = modify_time
        # The ID of the modifier.
        self.modify_user = modify_user
        # The name of the computing resource.
        self.name = name
        # The ID of the workspace to which the computing resource belongs.
        self.project_id = project_id
        # The business unique key for the computing resource. For example, the format for Hologres is ${tenantOwnerId}:${regionId}:${type}:${instanceId}:${database}.
        self.qualified_name = qualified_name
        # The type of the computing resource.
        self.type = type
        # Specifies whether it is the default computing resource.
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

        if self.name is not None:
            result['Name'] = self.name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.qualified_name is not None:
            result['QualifiedName'] = self.qualified_name

        if self.type is not None:
            result['Type'] = self.type

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

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('QualifiedName') is not None:
            self.qualified_name = m.get('QualifiedName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('WhetherDefault') is not None:
            self.whether_default = m.get('WhetherDefault')

        return self

