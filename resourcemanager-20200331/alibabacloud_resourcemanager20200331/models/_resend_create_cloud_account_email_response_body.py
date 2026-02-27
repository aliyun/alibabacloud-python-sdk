# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_resourcemanager20200331 import models as main_models
from darabonba.model import DaraModel

class ResendCreateCloudAccountEmailResponseBody(DaraModel):
    def __init__(
        self,
        account: main_models.ResendCreateCloudAccountEmailResponseBodyAccount = None,
        request_id: str = None,
    ):
        # The information of the member account.
        self.account = account
        # The ID of the request.
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
            temp_model = main_models.ResendCreateCloudAccountEmailResponseBodyAccount()
            self.account = temp_model.from_map(m.get('Account'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ResendCreateCloudAccountEmailResponseBodyAccount(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        account_name: str = None,
        display_name: str = None,
        folder_id: str = None,
        join_method: str = None,
        join_time: str = None,
        modify_time: str = None,
        record_id: str = None,
        resource_directory_id: str = None,
        status: str = None,
        type: str = None,
    ):
        # The ID of the account.
        self.account_id = account_id
        # The name of the account.
        self.account_name = account_name
        # The display name of the member account.
        self.display_name = display_name
        # The ID of the folder.
        self.folder_id = folder_id
        # The way in which the member account joined the resource directory. Valid values:
        # 
        # *   invited: The member account is invited to join the resource directory.
        # *   created: The member account is directly created in the resource directory.
        self.join_method = join_method
        # The time when the member account joined the resource directory.
        self.join_time = join_time
        # The time when the member account was modified.
        self.modify_time = modify_time
        # The account record ID.
        self.record_id = record_id
        # The ID of the resource directory.
        self.resource_directory_id = resource_directory_id
        # The status of the member account. Valid values:
        # 
        # *   CreateSuccess: The member account is created.
        # *   CreateVerifying: The creation of the member account is under confirmation.
        # *   CreateFailed: The member account failed to be created.
        # *   CreateExpired: The creation of the member account expired.
        # *   CreateCancelled: The creation of the member account is canceled.
        # *   PromoteVerifying: The upgrade of the member account is under confirmation.
        # *   PromoteFailed: The member account failed to be upgraded.
        # *   PromoteExpired: The upgrade of the member account expired.
        # *   PromoteCancelled: The upgrade of the member account is canceled.
        # *   PromoteSuccess: The member account is upgraded.
        # *   InviteSuccess: The owner of the member account accepted the invitation.
        # *   Removed: The member account is removed from the resource directory.
        self.status = status
        # The type of the member account. The value CloudAccount indicates that the member account is a cloud account.
        self.type = type

    def validate(self):
        pass

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

        if self.folder_id is not None:
            result['FolderId'] = self.folder_id

        if self.join_method is not None:
            result['JoinMethod'] = self.join_method

        if self.join_time is not None:
            result['JoinTime'] = self.join_time

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.record_id is not None:
            result['RecordId'] = self.record_id

        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id

        if self.status is not None:
            result['Status'] = self.status

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

        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')

        if m.get('JoinMethod') is not None:
            self.join_method = m.get('JoinMethod')

        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')

        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

