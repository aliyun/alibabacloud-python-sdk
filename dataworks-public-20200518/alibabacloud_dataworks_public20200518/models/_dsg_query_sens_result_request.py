# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DsgQuerySensResultRequest(DaraModel):
    def __init__(
        self,
        col: str = None,
        db_type: str = None,
        level: str = None,
        node_name: str = None,
        order: str = None,
        order_field: str = None,
        page_no: int = None,
        page_size: int = None,
        project_name: str = None,
        schema_name: str = None,
        sens_status: str = None,
        sensitive_id: str = None,
        sensitive_name: str = None,
        table: str = None,
        tenant_id: str = None,
    ):
        # The name of the field.
        self.col = col
        # The type of the database. Valid values:
        # 
        # *   **ODPS.ODPS**
        # *   **HOLO.POSTGRES**
        # *   **EMR**
        self.db_type = db_type
        # The sensitivity level of the field.
        self.level = level
        # The name of a data category.
        self.node_name = node_name
        # The sorting method. Valid values:
        # 
        # *   DESC
        # *   ASC
        self.order = order
        # The field used for sorting.
        # 
        # *   gmt_create
        # *   gmt_modified
        self.order_field = order_field
        # The page number. Pages start from page 1.
        self.page_no = page_no
        # The number of entries per page. Default value: 10. Maximum value: 20.
        self.page_size = page_size
        # The name of the DataWorks workspace. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to obtain the workspace name.
        self.project_name = project_name
        # The name of the schema.
        self.schema_name = schema_name
        # The sensitivity status of the field.
        # 
        # *   1: indicates sensitive.
        # *   \\-1: indicates non-sensitive.
        self.sens_status = sens_status
        # The sensitive field ID.
        self.sensitive_id = sensitive_id
        # The name of the sensitive field.
        self.sensitive_name = sensitive_name
        # The name of the table.
        self.table = table
        # The tenant ID. To obtain the tenant ID, perform the following steps: Log on to the [DataWorks console](https://workbench.data.aliyun.com/console). Find your workspace and go to the DataStudio page. On the DataStudio page, click the logon username in the upper-right corner and click User Info in the Menu section.
        # 
        # This parameter is required.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.col is not None:
            result['Col'] = self.col

        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.level is not None:
            result['Level'] = self.level

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.order is not None:
            result['Order'] = self.order

        if self.order_field is not None:
            result['OrderField'] = self.order_field

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.sens_status is not None:
            result['SensStatus'] = self.sens_status

        if self.sensitive_id is not None:
            result['SensitiveId'] = self.sensitive_id

        if self.sensitive_name is not None:
            result['SensitiveName'] = self.sensitive_name

        if self.table is not None:
            result['Table'] = self.table

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Col') is not None:
            self.col = m.get('Col')

        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('OrderField') is not None:
            self.order_field = m.get('OrderField')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('SensStatus') is not None:
            self.sens_status = m.get('SensStatus')

        if m.get('SensitiveId') is not None:
            self.sensitive_id = m.get('SensitiveId')

        if m.get('SensitiveName') is not None:
            self.sensitive_name = m.get('SensitiveName')

        if m.get('Table') is not None:
            self.table = m.get('Table')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

