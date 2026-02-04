# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDataCheckTableDetailsRequest(DaraModel):
    def __init__(
        self,
        check_type: int = None,
        dts_job_id: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        schema_name: str = None,
        status: str = None,
        table_name: str = None,
    ):
        # The data verification method. Valid values:
        # 
        # *   **1**: full data verification.
        # *   **2**: incremental data verification.
        # 
        # This parameter is required.
        self.check_type = check_type
        # The ID of the data migration or data synchronization task. You can call the [DescribeDtsJobs](https://help.aliyun.com/document_detail/209702.html) operation to query the task ID.
        # 
        # This parameter is required.
        self.dts_job_id = dts_job_id
        # The number of the page to return. The value must be an integer that is greater than **0** and does not exceed the maximum value of the Integer data type. Default value:**1**.
        self.page_number = page_number
        # The number of entries to return on each page.
        self.page_size = page_size
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The name of the schema whose data is verified in the source database.
        self.schema_name = schema_name
        # The status of the data verification result. Valid values:
        # 
        # *   **-1** (default): All status.
        # *   **6**: Inconsistent data detected in the table.
        self.status = status
        # The name of the table whose data is verified in the source database.
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_type is not None:
            result['CheckType'] = self.check_type

        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.status is not None:
            result['Status'] = self.status

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')

        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

