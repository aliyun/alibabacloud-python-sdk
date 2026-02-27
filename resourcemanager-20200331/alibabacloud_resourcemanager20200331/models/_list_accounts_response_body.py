# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcemanager20200331 import models as main_models
from darabonba.model import DaraModel

class ListAccountsResponseBody(DaraModel):
    def __init__(
        self,
        accounts: main_models.ListAccountsResponseBodyAccounts = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.accounts = accounts
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.accounts:
            self.accounts.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accounts is not None:
            result['Accounts'] = self.accounts.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accounts') is not None:
            temp_model = main_models.ListAccountsResponseBodyAccounts()
            self.accounts = temp_model.from_map(m.get('Accounts'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListAccountsResponseBodyAccounts(DaraModel):
    def __init__(
        self,
        account: List[main_models.ListAccountsResponseBodyAccountsAccount] = None,
    ):
        self.account = account

    def validate(self):
        if self.account:
            for v1 in self.account:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Account'] = []
        if self.account is not None:
            for k1 in self.account:
                result['Account'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.account = []
        if m.get('Account') is not None:
            for k1 in m.get('Account'):
                temp_model = main_models.ListAccountsResponseBodyAccountsAccount()
                self.account.append(temp_model.from_map(k1))

        return self

class ListAccountsResponseBodyAccountsAccount(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        display_name: str = None,
        folder_id: str = None,
        join_method: str = None,
        join_time: str = None,
        modify_time: str = None,
        resource_directory_id: str = None,
        resource_directory_path: str = None,
        status: str = None,
        tags: main_models.ListAccountsResponseBodyAccountsAccountTags = None,
        type: str = None,
    ):
        self.account_id = account_id
        self.display_name = display_name
        self.folder_id = folder_id
        self.join_method = join_method
        self.join_time = join_time
        self.modify_time = modify_time
        self.resource_directory_id = resource_directory_id
        self.resource_directory_path = resource_directory_path
        self.status = status
        self.tags = tags
        self.type = type

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.folder_id is not None:
            result['FolderId'] = self.folder_id

        if self.join_method is not None:
            result['JoinMethod'] = self.join_method

        if self.join_time is not None:
            result['JoinTime'] = self.join_time

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id

        if self.resource_directory_path is not None:
            result['ResourceDirectoryPath'] = self.resource_directory_path

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')

        if m.get('JoinMethod') is not None:
            self.join_method = m.get('JoinMethod')

        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')

        if m.get('ResourceDirectoryPath') is not None:
            self.resource_directory_path = m.get('ResourceDirectoryPath')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            temp_model = main_models.ListAccountsResponseBodyAccountsAccountTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListAccountsResponseBodyAccountsAccountTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.ListAccountsResponseBodyAccountsAccountTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListAccountsResponseBodyAccountsAccountTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class ListAccountsResponseBodyAccountsAccountTagsTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

