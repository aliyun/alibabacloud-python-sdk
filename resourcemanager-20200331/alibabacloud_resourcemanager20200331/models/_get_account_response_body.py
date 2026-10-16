# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcemanager20200331 import models as main_models
from darabonba.model import DaraModel

class GetAccountResponseBody(DaraModel):
    def __init__(
        self,
        account: main_models.GetAccountResponseBodyAccount = None,
        request_id: str = None,
    ):
        # The member account information.
        self.account = account
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.account:
            self.account.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account is not None:
            result['Account'] = self.account.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            temp_model = main_models.GetAccountResponseBodyAccount()
            self.account = temp_model.from_map(m.get('Account'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetAccountResponseBodyAccount(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        account_name: str = None,
        display_name: str = None,
        email_status: str = None,
        folder_id: str = None,
        identity_information: str = None,
        join_method: str = None,
        join_time: str = None,
        location: str = None,
        modify_time: str = None,
        resource_directory_id: str = None,
        resource_directory_path: str = None,
        status: str = None,
        tags: List[main_models.GetAccountResponseBodyAccountTags] = None,
        type: str = None,
    ):
        # The member account ID.
        self.account_id = account_id
        # The name of the account.
        self.account_name = account_name
        # The display name of the member account.
        self.display_name = display_name
        # The email status. Valid values:
        # 
        # - Empty: No email modification record exists.
        # - WAIT_MODIFY: The modification is in progress.
        # - CANCELLED: The modification is canceled.
        # - EXPIRED: The modification has expired.
        self.email_status = email_status
        # The ID of the folder.
        self.folder_id = folder_id
        # The real-name verification information.
        self.identity_information = identity_information
        # The method used by the member account to join the resource directory. Valid values:
        # 
        # - invited: Invited.
        # - created: Created.
        self.join_method = join_method
        # The time when the member account joined the resource directory. The time is displayed in UTC, as specified by RFC 3339, with Z indicating UTC.
        self.join_time = join_time
        # The location of the member account in the resource directory.
        self.location = location
        # The time when the member account was last modified. The time is displayed in UTC, as specified by RFC 3339, with Z indicating UTC.
        self.modify_time = modify_time
        # The ID of the resource directory.
        self.resource_directory_id = resource_directory_id
        # The path ID (RDPath) of the member account in the resource directory.
        self.resource_directory_path = resource_directory_path
        # The join status of the member account. Valid values:
        # 
        # - CreateSuccess: Created.
        # - PromoteVerifying: Upgrade is being confirmed.
        # - PromoteFailed: Upgrade failed.
        # - PromoteExpired: Upgrade expired.
        # - PromoteCancelled: Upgrade canceled.
        # - PromoteSuccess: Upgrade succeeded.
        # - InviteSuccess: Invitation succeeded.
        self.status = status
        # The tags.
        self.tags = tags
        # The type of the member account. Valid values:
        # 
        # - CloudAccount: Cloud account.
        # - ResourceAccount: Resource account.
        self.type = type

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.email_status is not None:
            result['EmailStatus'] = self.email_status

        if self.folder_id is not None:
            result['FolderId'] = self.folder_id

        if self.identity_information is not None:
            result['IdentityInformation'] = self.identity_information

        if self.join_method is not None:
            result['JoinMethod'] = self.join_method

        if self.join_time is not None:
            result['JoinTime'] = self.join_time

        if self.location is not None:
            result['Location'] = self.location

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id

        if self.resource_directory_path is not None:
            result['ResourceDirectoryPath'] = self.resource_directory_path

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('EmailStatus') is not None:
            self.email_status = m.get('EmailStatus')

        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')

        if m.get('IdentityInformation') is not None:
            self.identity_information = m.get('IdentityInformation')

        if m.get('JoinMethod') is not None:
            self.join_method = m.get('JoinMethod')

        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')

        if m.get('ResourceDirectoryPath') is not None:
            self.resource_directory_path = m.get('ResourceDirectoryPath')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetAccountResponseBodyAccountTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetAccountResponseBodyAccountTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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

