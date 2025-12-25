# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateLakeHouseSpaceRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        dev_db_id: str = None,
        dw_db_type: str = None,
        mode: str = None,
        prod_db_id: str = None,
        space_config: str = None,
        space_name: str = None,
        tid: int = None,
    ):
        # The description of the workspace.
        self.description = description
        # The ID of the development database. You can call the [ListDatabases](https://help.aliyun.com/document_detail/141873.html) or [SearchDatabase](https://help.aliyun.com/document_detail/141876.html) operation to obtain the ID.
        # 
        # This parameter is required.
        self.dev_db_id = dev_db_id
        # The type of the database. Valid values:
        # 
        # *   **14**: AnalyticDB for MySQL
        # *   **18**: AnalyticDB for PostgreSQL
        # 
        # This parameter is required.
        self.dw_db_type = dw_db_type
        # The mode in which the workspace runs. Valid values:
        # 
        # *   **0**: basic mode. This mode is unavailable.
        # *   **1**: standard mode.
        # 
        # This parameter is required.
        self.mode = mode
        # The ID of the production database. You can call the [ListDatabases](https://help.aliyun.com/document_detail/141873.html) or [SearchDatabase](https://help.aliyun.com/document_detail/141876.html) operation to obtain the ID.
        self.prod_db_id = prod_db_id
        # The configuration of the workspace. Valid values:
        # 
        # *   **skipManualRunCheck**: No security rule check is required in the trial run phase.
        # *   **skipPublishApprove**: No approval is required for publishing and O\\&M.
        # 
        # This parameter is required.
        self.space_config = space_config
        # The name of the workspace.
        # 
        # This parameter is required.
        self.space_name = space_name
        # The ID of the tenant. You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) or [ListUserTenants](https://help.aliyun.com/document_detail/198074.html) operation to obtain the tenant ID.
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.dev_db_id is not None:
            result['DevDbId'] = self.dev_db_id

        if self.dw_db_type is not None:
            result['DwDbType'] = self.dw_db_type

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.prod_db_id is not None:
            result['ProdDbId'] = self.prod_db_id

        if self.space_config is not None:
            result['SpaceConfig'] = self.space_config

        if self.space_name is not None:
            result['SpaceName'] = self.space_name

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DevDbId') is not None:
            self.dev_db_id = m.get('DevDbId')

        if m.get('DwDbType') is not None:
            self.dw_db_type = m.get('DwDbType')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('ProdDbId') is not None:
            self.prod_db_id = m.get('ProdDbId')

        if m.get('SpaceConfig') is not None:
            self.space_config = m.get('SpaceConfig')

        if m.get('SpaceName') is not None:
            self.space_name = m.get('SpaceName')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

