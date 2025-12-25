# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class GetTableDesignProjectInfoResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        project_info: main_models.GetTableDesignProjectInfoResponseBodyProjectInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message returned if the request failed.
        self.error_message = error_message
        # The information about the schema design project.
        self.project_info = project_info
        # The request ID. You can use the request ID to query logs and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success

    def validate(self):
        if self.project_info:
            self.project_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.project_info is not None:
            result['ProjectInfo'] = self.project_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('ProjectInfo') is not None:
            temp_model = main_models.GetTableDesignProjectInfoResponseBodyProjectInfo()
            self.project_info = temp_model.from_map(m.get('ProjectInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetTableDesignProjectInfoResponseBodyProjectInfo(DaraModel):
    def __init__(
        self,
        base_database: main_models.GetTableDesignProjectInfoResponseBodyProjectInfoBaseDatabase = None,
        creator_id: int = None,
        description: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        order_id: int = None,
        project_id: int = None,
        status: str = None,
        title: str = None,
    ):
        # The information about the change base database of the schema design ticket.
        self.base_database = base_database
        # The ID of the user who created the ticket.
        self.creator_id = creator_id
        # The description of the schema design project.
        self.description = description
        # The time when the ticket was created.
        self.gmt_create = gmt_create
        # The time when the ticket was last modified.
        self.gmt_modified = gmt_modified
        # The ticket ID.
        self.order_id = order_id
        # The project ID.
        self.project_id = project_id
        # The state of the schema design project. Valid values:
        # 
        # *   **DESIGN**: The schema is being designed.
        # *   **PUBLISHED**: The schema is published.
        # *   **CLOSE**: The ticket is closed.
        self.status = status
        # The name of the schema design project.
        self.title = title

    def validate(self):
        if self.base_database:
            self.base_database.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.base_database is not None:
            result['BaseDatabase'] = self.base_database.to_map()

        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id

        if self.description is not None:
            result['Description'] = self.description

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.status is not None:
            result['Status'] = self.status

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseDatabase') is not None:
            temp_model = main_models.GetTableDesignProjectInfoResponseBodyProjectInfoBaseDatabase()
            self.base_database = temp_model.from_map(m.get('BaseDatabase'))

        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

class GetTableDesignProjectInfoResponseBodyProjectInfoBaseDatabase(DaraModel):
    def __init__(
        self,
        alias: str = None,
        db_id: int = None,
        db_type: str = None,
        env_type: str = None,
        logic: bool = None,
        schema_name: str = None,
        search_name: str = None,
    ):
        # The alias of the database instance.
        self.alias = alias
        # The database ID.
        self.db_id = db_id
        # The type of the database. For more information about the valid values of this parameter, see [DbType parameter](https://help.aliyun.com/document_detail/198106.html).
        self.db_type = db_type
        # The type of the environment in which the database instance is deployed. Valid values:
        # 
        # *   **product**: production environment.
        # *   **dev**: development environment.
        # *   **pre**: pre-release environment.
        # *   **test**: test environment.
        # *   **sit**: system integration testing (SIT) environment.
        # *   **uat**: user acceptance testing (UAT) environment.
        # *   **pet**: stress testing environment.
        # *   **stag**: staging environment.
        self.env_type = env_type
        # Indicates whether the database is a logical database. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.logic = logic
        # The database name.
        self.schema_name = schema_name
        # The name that is used to search for the database.
        self.search_name = search_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['Alias'] = self.alias

        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.logic is not None:
            result['Logic'] = self.logic

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.search_name is not None:
            result['SearchName'] = self.search_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')

        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('Logic') is not None:
            self.logic = m.get('Logic')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')

        return self

