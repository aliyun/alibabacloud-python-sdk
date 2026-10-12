# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDataSourceRequest(DaraModel):
    def __init__(
        self,
        connection_properties: str = None,
        connection_properties_mode: str = None,
        description: str = None,
        id: int = None,
        project_id: int = None,
    ):
        # The specific connection configuration of the data source, including the endpoint, access identity, and environment context. The EnvType property of the data source environment is a member attribute of this object. Valid values:
        # - Dev: development environment.
        # - Prod: production environment.
        # 
        # Different types of data sources have different attribute specifications in different configuration patterns (ConnectionPropertiesMode). For more information, see [Connection properties](https://help.aliyun.com/document_detail/2852465.html).
        # 
        # This parameter is required.
        self.connection_properties = connection_properties
        # The category used to add the data source. Different types have different subtypes and corresponding parameter constraints. Examples:
        # - InstanceMode: instance mode.
        # - UrlMode: connection string mode.
        self.connection_properties_mode = connection_properties_mode
        # The description of the data source. The description can be up to 3,000 characters in length.
        self.description = description
        # The unique identifier of the data source.
        # 
        # This parameter is required.
        self.id = id
        # The ID of the DataWorks workspace.
        # 
        # This parameter is required.
        self.project_id = project_id

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

        if self.id is not None:
            result['Id'] = self.id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionProperties') is not None:
            self.connection_properties = m.get('ConnectionProperties')

        if m.get('ConnectionPropertiesMode') is not None:
            self.connection_properties_mode = m.get('ConnectionPropertiesMode')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

