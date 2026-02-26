# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExecuteMultiAccountSQLQueryRequest(DaraModel):
    def __init__(
        self,
        expression: str = None,
        max_results: int = None,
        next_token: str = None,
        scope: str = None,
    ):
        # The SQL statement to be executed.
        # 
        # The number of characters in the SQL statement must be less than 2,000.
        # 
        # For more information about the SQL syntax, see [Basic SQL syntax](https://help.aliyun.com/document_detail/2539395.html).
        # 
        # This parameter is required.
        self.expression = expression
        # The maximum number of entries to return on each page.
        # 
        # Valid values: 1 to 1000.
        # 
        # Default value: 1000.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        # The search scope. The value of this parameter can be one of the following items:
        # 
        # *   ID of a resource directory: Resources within the management account and all members of the resource directory are searched.
        # *   ID of the Root folder: Resources within all members in the Root folder and the subfolders of the Root folder are searched.
        # *   ID of a folder: Resources within all members in the folder are searched.
        # *   ID of a member: Resources within the member are searched.
        # *   ID of a member/ID of a Resource group: Resources within the member in the resource group are searched.
        # 
        # For more information about how to obtain the ID of a resource directory, the Root folder, a folder, a member, or a resource group, see [GetResourceDirectory](https://help.aliyun.com/document_detail/159995.html), [ListFoldersForParent](https://help.aliyun.com/document_detail/159997.html), [ListFoldersForParent](https://help.aliyun.com/document_detail/159997.html), [ListAccounts](https://help.aliyun.com/document_detail/160016.html), or [ListResourceGroups](https://help.aliyun.com/document_detail/158855.html).
        # 
        # This parameter is required.
        self.scope = scope

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expression is not None:
            result['Expression'] = self.expression

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.scope is not None:
            result['Scope'] = self.scope

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        return self

