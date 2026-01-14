# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_quickbi_public20220101 import models as main_models
from darabonba.model import DaraModel

class GetDataSourceConnectionInfoResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.GetDataSourceConnectionInfoResponseBodyResult = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Data source information.
        self.result = result
        # Indicates whether the operation was successful.
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.GetDataSourceConnectionInfoResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetDataSourceConnectionInfoResponseBodyResult(DaraModel):
    def __init__(
        self,
        address: str = None,
        auth_level: str = None,
        creator_id: str = None,
        ds_id: str = None,
        ds_type: str = None,
        ds_version: str = None,
        instance: str = None,
        instance_id: str = None,
        modify_user: str = None,
        no_sasl: bool = None,
        parent_ds_type: str = None,
        port: str = None,
        project: str = None,
        schema: str = None,
        show_name: str = None,
        workspace_id: str = None,
    ):
        # Database connection string address (domain or IP).
        self.address = address
        # Permission level:
        # 
        # - 0 -- Private
        # - 1 -- Collaborative Editing (old)
        # - 11 -- Collaborative Editing - Space Members
        # - 12 -- Collaborative Editing - Specified to Individuals
        self.auth_level = auth_level
        # Quick BI user ID of the creator.
        self.creator_id = creator_id
        # Data source ID.
        self.ds_id = ds_id
        # Data source type.
        self.ds_type = ds_type
        # Version of the data source.
        self.ds_version = ds_version
        # Database instance, corresponding to the database name, and for ODPS, it is the project.
        self.instance = instance
        # Instance ID.
        self.instance_id = instance_id
        # Quick BI user ID of the modifier.
        self.modify_user = modify_user
        # Whether the impala data source requires authentication to log in:
        # 
        # - true - Requires account and password login  
        # - false - No authentication required (default)
        self.no_sasl = no_sasl
        # Primary data source type for multi-engine data sources.
        self.parent_ds_type = parent_ds_type
        # Port.
        self.port = port
        # Used for front-end display when obtaining connection details for ODPS.
        self.project = project
        # Database schema, only needs to be set for databases that support schemas.
        self.schema = schema
        # Display name of the data source on the front end.
        self.show_name = show_name
        # Workspace ID to which the data source belongs.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        if self.auth_level is not None:
            result['AuthLevel'] = self.auth_level

        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id

        if self.ds_id is not None:
            result['DsId'] = self.ds_id

        if self.ds_type is not None:
            result['DsType'] = self.ds_type

        if self.ds_version is not None:
            result['DsVersion'] = self.ds_version

        if self.instance is not None:
            result['Instance'] = self.instance

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.modify_user is not None:
            result['ModifyUser'] = self.modify_user

        if self.no_sasl is not None:
            result['NoSasl'] = self.no_sasl

        if self.parent_ds_type is not None:
            result['ParentDsType'] = self.parent_ds_type

        if self.port is not None:
            result['Port'] = self.port

        if self.project is not None:
            result['Project'] = self.project

        if self.schema is not None:
            result['Schema'] = self.schema

        if self.show_name is not None:
            result['ShowName'] = self.show_name

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('AuthLevel') is not None:
            self.auth_level = m.get('AuthLevel')

        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')

        if m.get('DsId') is not None:
            self.ds_id = m.get('DsId')

        if m.get('DsType') is not None:
            self.ds_type = m.get('DsType')

        if m.get('DsVersion') is not None:
            self.ds_version = m.get('DsVersion')

        if m.get('Instance') is not None:
            self.instance = m.get('Instance')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ModifyUser') is not None:
            self.modify_user = m.get('ModifyUser')

        if m.get('NoSasl') is not None:
            self.no_sasl = m.get('NoSasl')

        if m.get('ParentDsType') is not None:
            self.parent_ds_type = m.get('ParentDsType')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Project') is not None:
            self.project = m.get('Project')

        if m.get('Schema') is not None:
            self.schema = m.get('Schema')

        if m.get('ShowName') is not None:
            self.show_name = m.get('ShowName')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

