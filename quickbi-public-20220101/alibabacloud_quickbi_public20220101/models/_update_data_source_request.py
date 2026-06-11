# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDataSourceRequest(DaraModel):
    def __init__(
        self,
        update_model: str = None,
    ):
        # A JSON-formatted string defining the data source configuration to update. See the example for the specific format. The JSON string includes the following parameters:
        # 
        # - `dsId`: Required. The ID of the data source.
        # 
        # - `userId`: Optional. The Quick BI user ID of the user who modifies the data source. If you specify this parameter, the update runs as this user.
        # 
        # - `dsType`: Required. The type of the data source. This value cannot be changed and must match the existing data source type.
        # 
        # - `showName`: Optional. The display name of the data source.
        # 
        # - `address`: Optional. The database connection endpoint, which can be a domain name or an IP address.
        # 
        # - `port`: Optional. The connection port for the database.
        # 
        # - `schema`: Optional. The database schema. This parameter is required only for database types that support schemas. For example, the default schema for SQL Server is `dbo`, while MySQL does not use schemas.
        # 
        # - `instance`: Optional. The database instance.
        # 
        # - `username`: Optional. The username for the database account or the AccessKey ID.
        # 
        # - `password`: Optional. The password for the database account.
        # 
        # - `resource`: Specifies the VPC type. This parameter is required if you are using a VPC connection. If the data source was created with VPC settings, you must include this parameter in your update request. Omitting this parameter from the request disables the VPC connection. For a list of `resource` values, see the **Additional information** section below.
        # 
        # - `accessId`: Optional. The AccessKey ID for the VPC instance. This parameter is required if the `resource` parameter is specified.
        # 
        # - `accessKey`: Optional. The AccessKey secret for the VPC instance. This parameter is required if the `resource` parameter is specified.
        # 
        # - `instanceId`: Optional. The ID of the VPC instance. This parameter is required if the `resource` parameter is specified.
        # 
        # - `region`: Optional. The region where the VPC instance is located. This parameter is required if the `resource` parameter is specified. For a list of region IDs, see the **Additional information** section below.
        # 
        # - `config`: Optional. A JSON object that contains additional configuration parameters for the database. You only need to include the fields that you want to update. Any field that you include is updated to the new value, even if it is an empty string. Fields that are not included in the request remain unchanged.
        # 
        # This parameter is required.
        self.update_model = update_model

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.update_model is not None:
            result['UpdateModel'] = self.update_model

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateModel') is not None:
            self.update_model = m.get('UpdateModel')

        return self

