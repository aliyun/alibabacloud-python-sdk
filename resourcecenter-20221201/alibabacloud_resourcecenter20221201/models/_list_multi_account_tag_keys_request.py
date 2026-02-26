# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListMultiAccountTagKeysRequest(DaraModel):
    def __init__(
        self,
        match_type: str = None,
        max_results: int = None,
        next_token: str = None,
        scope: str = None,
        tag_key: str = None,
    ):
        # The matching mode. Valid values:
        # 
        # *   Equals: equal match
        # *   Prefix: match by prefix
        self.match_type = match_type
        # The maximum number of entries to return on each page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results.
        # 
        # If the total number of entries returned for the current request exceeds the value of the `MaxResults` parameter, the entries are truncated. In this case, you can use the `token` to initiate another request and obtain the remaining entries.
        self.next_token = next_token
        # The search scope. The value of this parameter can be one of the following items:
        # 
        # *   ID of a resource directory: Resources within the management account and all members of the resource directory are searched. You can call the [GetResourceDirectory](https://help.aliyun.com/document_detail/159995.html) operation to obtain the ID of the resource directory. The ID is indicated by the `ResourceDirectoryId` parameter in the response of the operation.
        # *   ID of the Root folder: Resources within all members in the Root folder and the subfolders of the Root folder are searched. You can call the [GetResourceDirectory](https://help.aliyun.com/document_detail/159995.html) operation to obtain the ID of the Root folder. The ID is indicated by the `RootFolderId` parameter in the response of the operation.
        # *   ID of a folder: Resources within all members in the folder are searched. You can call the [ListFoldersForParent](https://help.aliyun.com/document_detail/159997.html) operation to obtain the ID of the folder. The ID is indicated by the `FolderId` parameter in the response of the operation.
        # *   ID of a member: Resources within the member are searched. You can call the [ListAccounts](https://help.aliyun.com/document_detail/160016.html) operation to obtain the ID of the member. The ID is indicated by the `AccountId` parameter in the response of the operation.
        # 
        # This parameter is required.
        self.scope = scope
        # The tag key.
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.match_type is not None:
            result['MatchType'] = self.match_type

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        return self

