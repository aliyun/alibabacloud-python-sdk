# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetDataSourceResponseBody(DaraModel):
    def __init__(
        self,
        data_source: main_models.GetDataSourceResponseBodyDataSource = None,
        request_id: str = None,
    ):
        # The information about the data source.
        self.data_source = data_source
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data_source:
            self.data_source.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_source is not None:
            result['DataSource'] = self.data_source.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSource') is not None:
            temp_model = main_models.GetDataSourceResponseBodyDataSource()
            self.data_source = temp_model.from_map(m.get('DataSource'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetDataSourceResponseBodyDataSource(DaraModel):
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
    ):
        # The connection configurations of the data source, including the connection address, access identity, and environment information. The envType parameter specifies the environment in which the data source is used. Valid values of the envType parameter:
        # 
        # *   Dev: development environment
        # *   Prod: production environment
        # 
        # The parameters that you need to configure for the data source vary based on the mode in which the data source is added. For more information, see [Data source connection information (ConnectionProperties)](https://help.aliyun.com/document_detail/2852465.html).
        self.connection_properties = connection_properties
        # The mode in which the data source is added. The mode varies based on the data source type. Valid values:
        # 
        # *   InstanceMode: instance mode
        # *   UrlMode: connection string mode
        # *   CdhMode: CDH cluster mode
        self.connection_properties_mode = connection_properties_mode
        # The time when the data source was added. This value is a UNIX timestamp.
        self.create_time = create_time
        # The ID of the user who adds the data source.
        self.create_user = create_user
        # The description of the data source.
        self.description = description
        # The data source ID.
        self.id = id
        # The time when the data source was last modified. This value is a UNIX timestamp.
        self.modify_time = modify_time
        # The ID of the user who modifies the data source.
        self.modify_user = modify_user
        # The name of the data source.
        self.name = name
        # The ID of the workspace with which the data source is associated.
        self.project_id = project_id
        # The unique business key of the data source. For example, the unique business key of a Hologres data source is in the `${tenantOwnerId}:${regionId}:${type}:${instanceId}:${database}` format.
        self.qualified_name = qualified_name
        # The type of the data source.
        self.type = type

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

        return self

