# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDataSourceRequest(DaraModel):
    def __init__(
        self,
        connection_properties: str = None,
        connection_properties_mode: str = None,
        description: str = None,
        name: str = None,
        project_id: int = None,
        type: str = None,
    ):
        # The connection configurations of the data source, including the connection address, access identity, and environment information. The envType parameter specifies the environment in which the data source is used. Valid values of the envType parameter:
        # 
        # *   Dev: development environment
        # *   Prod: production environment
        # 
        # The parameters that you need to configure for the data source vary based on the mode in which the data source is added. For more information, see [Data source connection information (ConnectionProperties)](https://help.aliyun.com/document_detail/2852465.html).
        # 
        # This parameter is required.
        self.connection_properties = connection_properties
        # The mode in which you want to add the data source. The mode varies based on the data source type. Valid values for MySQL data sources:
        # 
        # *   InstanceMode: instance mode
        # *   UrlMode: connection string mode
        # 
        # This parameter is required.
        self.connection_properties_mode = connection_properties_mode
        # The description of the data source. The description cannot exceed 3,000 characters in length.
        self.description = description
        # The name of the data source. The name can be up to 255 characters in length and can contain letters, digits, and underscores (_). The name must start with a letter.
        # 
        # This parameter is required.
        self.name = name
        # The ID of the DataWorks workspace. You can log on to the [DataWorks console](https://dataworks.console.aliyun.com/overview) and go to the workspace management page to obtain the ID.
        # 
        # This parameter is used to determine the DataWorks workspaces used for this API call.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The type of the data source. More than 70 types of data sources are supported in DataWorks. For more information, see [Data source types](https://help.aliyun.com/document_detail/2852465.html).
        # 
        # This parameter is required.
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

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionProperties') is not None:
            self.connection_properties = m.get('ConnectionProperties')

        if m.get('ConnectionPropertiesMode') is not None:
            self.connection_properties_mode = m.get('ConnectionPropertiesMode')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

