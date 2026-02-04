# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcedirectorymaster20220419 import models as main_models
from darabonba.model import DaraModel

class ListAccountsForParentResponseBody(DaraModel):
    def __init__(
        self,
        accounts: main_models.ListAccountsForParentResponseBodyAccounts = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information about the members.
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
            temp_model = main_models.ListAccountsForParentResponseBodyAccounts()
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

class ListAccountsForParentResponseBodyAccounts(DaraModel):
    def __init__(
        self,
        account: List[main_models.ListAccountsForParentResponseBodyAccountsAccount] = None,
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
                temp_model = main_models.ListAccountsForParentResponseBodyAccountsAccount()
                self.account.append(temp_model.from_map(k1))

        return self

class ListAccountsForParentResponseBodyAccountsAccount(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        account_name: str = None,
        deletion_status: str = None,
        display_name: str = None,
        folder_id: str = None,
        join_method: str = None,
        join_time: str = None,
        modify_time: str = None,
        resource_directory_id: str = None,
        status: str = None,
        tags: main_models.ListAccountsForParentResponseBodyAccountsAccountTags = None,
        type: str = None,
    ):
        # The Alibaba Cloud account ID of the member.
        self.account_id = account_id
        # The Alibaba Cloud account name of the member.
        self.account_name = account_name
        # The deletion status of the member. Valid values:
        # 
        # *   Checking: A deletion check is being performed for the member.
        # *   Deleting: The member is being deleted.
        # *   CheckFailed: The deletion check for the member fails.
        # *   DeleteFailed: The member fails to be deleted.
        # 
        # >  If deletion is not performed for the member, the value of this parameter is empty.
        self.deletion_status = deletion_status
        # The display name of the member.
        self.display_name = display_name
        # The ID of the folder.
        self.folder_id = folder_id
        # The way in which the member joins the resource directory.
        # 
        # *   invited: The member is invited to join the resource directory.
        # *   created: The member is directly created in the resource directory.
        self.join_method = join_method
        # The time when the member joined the resource directory. The time is displayed in UTC.
        self.join_time = join_time
        # The time when the member was modified. The time is displayed in UTC.
        self.modify_time = modify_time
        # The ID of the resource directory.
        self.resource_directory_id = resource_directory_id
        # The status of the member. Valid values:
        # 
        # *   CreateSuccess: The member is created.
        # *   PromoteVerifying: The upgrade of the member is under confirmation.
        # *   PromoteFailed: The upgrade of the member fails.
        # *   PromoteExpired: The upgrade of the member expires.
        # *   PromoteCancelled: The upgrade of the member is canceled.
        # *   PromoteSuccess: The member is upgraded.
        # *   InviteSuccess: The member accepts the invitation.
        self.status = status
        # The tags that are added to the member.
        self.tags = tags
        # The type of the member. Valid values:
        # 
        # *   CloudAccount: cloud account
        # *   ResourceAccount: resource account
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

        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.deletion_status is not None:
            result['DeletionStatus'] = self.deletion_status

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

        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('DeletionStatus') is not None:
            self.deletion_status = m.get('DeletionStatus')

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

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            temp_model = main_models.ListAccountsForParentResponseBodyAccountsAccountTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListAccountsForParentResponseBodyAccountsAccountTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.ListAccountsForParentResponseBodyAccountsAccountTagsTag] = None,
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
                temp_model = main_models.ListAccountsForParentResponseBodyAccountsAccountTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class ListAccountsForParentResponseBodyAccountsAccountTagsTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
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

