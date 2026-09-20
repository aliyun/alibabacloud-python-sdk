# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetMetaTableChangeLogRequest(DaraModel):
    def __init__(
        self,
        change_type: str = None,
        end_date: str = None,
        object_type: str = None,
        page_number: int = None,
        page_size: int = None,
        start_date: str = None,
        table_guid: str = None,
    ):
        # The type of change. Valid values: CREATE_TABLE, ALTER_TABLE, DROP_TABLE, ADD_PARTITION, and DROP_PARTITION.
        self.change_type = change_type
        # The end date of the table change. Format: yyyy-MM-dd HH:mm:ss.
        # - If the date validation fails, the system uses the current time as the end date by default.
        # - If both the start date and end date fail validation, the system automatically retrieves the table change records from the last 30 days.
        self.end_date = end_date
        # The type of the changed object. Valid values: TABLE and PARTITION.
        self.object_type = object_type
        # The page number. Used for pagination.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The start date of the table change. Format: yyyy-MM-dd HH:mm:ss.
        # - If the date validation fails, the system uses the current time as the start date by default.
        # - If both the start date and end date fail validation, the system automatically retrieves the table change records from the last 30 days.
        self.start_date = start_date
        # The globally unique identifier (GUID) of the table. Format: odps.projectName.tableName. You can call [GetMetaDBTableList](https://help.aliyun.com/document_detail/2780086.html) to obtain the GUID of the table.
        # > Currently, you can call [GetMetaTableChangeLog](https://help.aliyun.com/document_detail/2780094.html) to retrieve the change log of only MaxCompute tables.
        # 
        # This parameter is required.
        self.table_guid = table_guid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_type is not None:
            result['ChangeType'] = self.change_type

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.object_type is not None:
            result['ObjectType'] = self.object_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.table_guid is not None:
            result['TableGuid'] = self.table_guid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeType') is not None:
            self.change_type = m.get('ChangeType')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('TableGuid') is not None:
            self.table_guid = m.get('TableGuid')

        return self

