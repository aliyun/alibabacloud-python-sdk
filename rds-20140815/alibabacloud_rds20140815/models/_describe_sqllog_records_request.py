# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSQLLogRecordsRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dbinstance_id: str = None,
        database: str = None,
        end_time: str = None,
        form: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        query_keywords: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sqlid: int = None,
        start_time: str = None,
        user: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the generated token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The instance ID. You can call the DescribeDBInstances operation to query the ID of the instance.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The name of the database. You can enter only one database name. If you specify this parameter, this operation returns the logs that are generated only for the specified database. If you do not specify this parameter, this operation returns the logs that are generated for all databases on the instance.
        self.database = database
        # The end of the time range to query. The end time must be later than the start time. The time span between the start time and the end time must be less than 15 days. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        # 
        # This parameter is required.
        self.end_time = end_time
        # Specifies whether to generate an SQL audit log file or return SQL audit logs. Valid values:
        # 
        # *   **File**: If you set this parameter to File, this operation generates an SQL audit log file and returns only common response parameters. After you call this operation, you must call the DescribeSQLLogFiles operation to obtain the download URL of the SQL audit log file.
        # *   **Stream** (default): If you set this parameter to Stream, this operation returns SQL audit logs.
        # 
        # >  If you set this parameter to **File**, only ApsaraDB RDS for MySQL instances that use local disks and ApsaraDB RDS for SQL Server instances are supported, and a maximum of 1 million logs are returned.
        self.form = form
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number. Pages start from 1.
        # 
        # Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Valid values: **30** to **100**. Default value: **30**.
        self.page_size = page_size
        # The keyword that is used for the query.
        # 
        # *   When you call this operation and set the **Form** parameter to **File** to generate an audit file, you cannot filter log entries by keyword.
        # *   You can specify up to 10 keywords. The keywords are evaluated by using the **AND** operator. Separate multiple keywords with spaces.
        # *   If a field name in the specified SQL statement is enclosed in grave accents (\\`) and you want to use the field name as a keyword, you must enter the grave accents (\\`) as part of the field name. For example, if the field name is \\`id\\`, enter \\`id\\` instead of id.
        # 
        # >  After you enter a keyword, the system matches the keyword based on the **Database**, **User**, and **QueryKeywords** parameters. The parameters are evaluated by using the **AND** operator.
        self.query_keywords = query_keywords
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The unique ID of the SQL statement.
        self.sqlid = sqlid
        # The beginning of the time range to query. You can query data in the last 15 days before the current date. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The username of the account. You can enter only one username. If you specify this parameter, this operation returns the logs that are generated only for the specified account. If you do not specify this parameter, this operation returns the logs that are generated for all accounts on the instance.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.database is not None:
            result['Database'] = self.database

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.form is not None:
            result['Form'] = self.form

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query_keywords is not None:
            result['QueryKeywords'] = self.query_keywords

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.sqlid is not None:
            result['SQLId'] = self.sqlid

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.user is not None:
            result['User'] = self.user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('Database') is not None:
            self.database = m.get('Database')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('QueryKeywords') is not None:
            self.query_keywords = m.get('QueryKeywords')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SQLId') is not None:
            self.sqlid = m.get('SQLId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('User') is not None:
            self.user = m.get('User')

        return self

