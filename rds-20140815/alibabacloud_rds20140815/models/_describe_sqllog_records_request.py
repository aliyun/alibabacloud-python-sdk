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
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The instance ID. You can call DescribeDBInstances to query the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The name of the database. By default, all databases are queried. You can also enter a database name to query. Only one database name can be entered at a time.
        self.database = database
        # The end time of the query. The end time must be later than the start time, and the interval between the start time and end time must be 7 days or less. Specify the time in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format (UTC).
        # 
        # > If DAS Enterprise Edition V3 is activated and you use the SQL Explorer and Audit feature it provides, you can query data within the hot data storage duration. You can call [DescribeSqlLogConfig](https://help.aliyun.com/document_detail/2778837.html) to query the activated Enterprise Edition information.
        # 
        # This parameter is required.
        self.end_time = end_time
        # Specifies whether to generate an audit file or return a list of SQL records. Valid values:
        # * **File**: If you set this parameter to File, an audit file is generated. Only common parameters are returned. You must call the DescribeSQLLogFiles operation to obtain the download URL of the file.
        # * **Stream**: This is the default value. A list of SQL records is returned.
        # 
        # > If this parameter is set to **File**, only MySQL (with Premium Local SSDs) and SQL Server instances are supported, and a maximum of 1,000,000 log entries are recorded.
        self.form = form
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number. The value must be a positive integer that does not exceed the maximum value of the Integer data type.
        # 
        # Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Valid values: **30** to **100**. Default value: **30**.
        self.page_size = page_size
        # The keywords that are used for the query.
        # 
        # - When you generate an audit file by calling this operation (the **Form** request parameter is set to **File**), keyword-based filtering is not supported.
        # 
        # - Separate multiple keywords with spaces. You can specify up to 10 keywords. The logical relationship among keywords is **and**.
        # 
        # - If a field name in the SQL statement uses backticks (\\`), you must also include the backticks when using the field name as a keyword. For example, if the field name is \\`id\\`, enter \\`id\\` instead of id.
        # 
        # > After you enter keywords, the system matches the keywords against the **Database**, **User**, and **QueryKeywords** parameters simultaneously. The logical relationship among the three request parameters is **and**.
        self.query_keywords = query_keywords
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # A reserved parameter.
        self.sqlid = sqlid
        # The start time of the query. You can query data within the last 7 days from the current date. Specify the time in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format (UTC).
        # 
        # > If DAS Enterprise Edition V3 is activated and you use the SQL Explorer and Audit feature it provides, you can query data within the hot data storage duration. You can call [DescribeSqlLogConfig](https://help.aliyun.com/document_detail/2778837.html) to query the activated Enterprise Edition information.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The username. By default, all users are queried. You can also enter a username to query. Only one username can be entered at a time.
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

