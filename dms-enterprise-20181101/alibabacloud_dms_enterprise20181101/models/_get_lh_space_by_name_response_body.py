# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class GetLhSpaceByNameResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        lakehouse_space: main_models.GetLhSpaceByNameResponseBodyLakehouseSpace = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code returned if the request fails.
        self.error_code = error_code
        # The error message returned if the request fails.
        self.error_message = error_message
        # The workspace for data warehouse development.
        self.lakehouse_space = lakehouse_space
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   **true**: The request is successful.
        # *   **false**: The request fails.
        self.success = success

    def validate(self):
        if self.lakehouse_space:
            self.lakehouse_space.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.lakehouse_space is not None:
            result['LakehouseSpace'] = self.lakehouse_space.to_map()

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

        if m.get('LakehouseSpace') is not None:
            temp_model = main_models.GetLhSpaceByNameResponseBodyLakehouseSpace()
            self.lakehouse_space = temp_model.from_map(m.get('LakehouseSpace'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetLhSpaceByNameResponseBodyLakehouseSpace(DaraModel):
    def __init__(
        self,
        creator_id: str = None,
        description: str = None,
        dev_db_id: int = None,
        dw_db_type: str = None,
        id: int = None,
        is_deleted: bool = None,
        mode: int = None,
        prod_db_id: int = None,
        space_config: str = None,
        space_name: str = None,
        tenant_id: str = None,
    ):
        # The ID of the user who creates the workspace.
        self.creator_id = creator_id
        # The description of the workspace.
        self.description = description
        # The ID of the development database.
        self.dev_db_id = dev_db_id
        # The type of the database. Valid values:
        # 
        # *   **14**: AnalyticDB for MySQL
        # *   **18**: AnalyticDB for PostgreSQL
        self.dw_db_type = dw_db_type
        # The ID of the workspace.
        self.id = id
        # Indicates whether the workspace is deleted. Valid values:
        # 
        # *   **true**: The workspace is deleted.
        # *   **false**: The workspace is not deleted.
        self.is_deleted = is_deleted
        # The mode in which the workspace runs. Valid values:
        # 
        # *   **0**: basic mode
        # *   **1**: standard mode
        self.mode = mode
        # The ID of the production database.
        self.prod_db_id = prod_db_id
        # The configuration of the workspace. Valid values:
        # 
        # *   **skipManualRunCheck**: No security rule check is required in the trial run phase.
        # *   **skipPublishApprove**: No approval is required for publishing and O\\&M.
        self.space_config = space_config
        # The name of the workspace.
        self.space_name = space_name
        # The ID of the tenant to which the workspace belongs.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id

        if self.description is not None:
            result['Description'] = self.description

        if self.dev_db_id is not None:
            result['DevDbId'] = self.dev_db_id

        if self.dw_db_type is not None:
            result['DwDbType'] = self.dw_db_type

        if self.id is not None:
            result['Id'] = self.id

        if self.is_deleted is not None:
            result['IsDeleted'] = self.is_deleted

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.prod_db_id is not None:
            result['ProdDbId'] = self.prod_db_id

        if self.space_config is not None:
            result['SpaceConfig'] = self.space_config

        if self.space_name is not None:
            result['SpaceName'] = self.space_name

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DevDbId') is not None:
            self.dev_db_id = m.get('DevDbId')

        if m.get('DwDbType') is not None:
            self.dw_db_type = m.get('DwDbType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IsDeleted') is not None:
            self.is_deleted = m.get('IsDeleted')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('ProdDbId') is not None:
            self.prod_db_id = m.get('ProdDbId')

        if m.get('SpaceConfig') is not None:
            self.space_config = m.get('SpaceConfig')

        if m.get('SpaceName') is not None:
            self.space_name = m.get('SpaceName')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

