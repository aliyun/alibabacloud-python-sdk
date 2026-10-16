# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcemanager20200331 import models as main_models
from darabonba.model import DaraModel

class CreateResourceAccountRequest(DaraModel):
    def __init__(
        self,
        account_name_prefix: str = None,
        display_name: str = None,
        parent_folder_id: str = None,
        payer_account_id: str = None,
        resell_account_type: str = None,
        tag: List[main_models.CreateResourceAccountRequestTag] = None,
    ):
        # The prefix of the account name. If you leave this parameter empty, the system randomly generates a prefix.
        # 
        # <props="china">Length: 2 to 50 characters.
        # 
        # <props="intl">Length: 2 to 37 characters.
        # 
        # Format: Can contain letters, digits, and special characters `_.-`. Must start and end with a letter or digit. Consecutive special characters `_.-` are not allowed.
        # 
        # The full account name is in the format of <AccountNamePrefix>@<ResourceDirectoryId>.aliyunid.com. Example: `alice@rd-3G****.aliyunid.com`.
        # 
        # The account name must be unique within the resource directory.
        self.account_name_prefix = account_name_prefix
        # The display name of the member.
        # 
        # Length: 2 to 50 characters.
        # 
        # Format: Can contain letters, digits, underscores (_), periods (.), hyphens (-), and spaces.
        # 
        # The display name must be unique within the resource directory.
        # 
        # This parameter is required.
        self.display_name = display_name
        # The ID of the parent folder.
        self.parent_folder_id = parent_folder_id
        # The ID of the billing account. If you leave this parameter empty, the newly created member pays for its own resource consumption.
        self.payer_account_id = payer_account_id
        # The identity type of the member. Valid values:
        # 
        # - resell (default): reseller account. The created member automatically establishes a reseller relationship with your distributor. You must use the management account to pay for the new member.
        # - non_resell: non-reseller account. The created member is a regular Alibaba Cloud account that has no relationship with your current distributor. This account purchases resources directly from Alibaba Cloud and pays for its own resource consumption.
        # 
        # > This parameter is supported only for China site (Chinese mainland) distributor customers.
        self.resell_account_type = resell_account_type
        # The tags of the member.
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
        if self.account_name_prefix is not None:
            result['AccountNamePrefix'] = self.account_name_prefix

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.parent_folder_id is not None:
            result['ParentFolderId'] = self.parent_folder_id

        if self.payer_account_id is not None:
            result['PayerAccountId'] = self.payer_account_id

        if self.resell_account_type is not None:
            result['ResellAccountType'] = self.resell_account_type

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountNamePrefix') is not None:
            self.account_name_prefix = m.get('AccountNamePrefix')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('ParentFolderId') is not None:
            self.parent_folder_id = m.get('ParentFolderId')

        if m.get('PayerAccountId') is not None:
            self.payer_account_id = m.get('PayerAccountId')

        if m.get('ResellAccountType') is not None:
            self.resell_account_type = m.get('ResellAccountType')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateResourceAccountRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class CreateResourceAccountRequestTag(DaraModel):
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

