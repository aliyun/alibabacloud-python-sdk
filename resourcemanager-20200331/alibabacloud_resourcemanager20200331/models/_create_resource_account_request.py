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
        # The prefix for the Alibaba Cloud account name of the member. If you leave this parameter empty, the system randomly generates a prefix.
        # 
        # The prefix must be 2 to 37 characters in length.
        # 
        # The prefix can contain letters, digits, and special characters but cannot contain consecutive special characters. The prefix must start with a letter or digit and end with a letter or digit. Valid special characters include underscores (`_`), periods (`.`), and hyphens (-).
        # 
        # The complete Alibaba Cloud account name of a member is in the @.aliyunid.com format, such as `alice@rd-3G****.aliyunid.com`.
        # 
        # Each name must be unique in the resource directory.
        self.account_name_prefix = account_name_prefix
        # The display name of the member.
        # 
        # The name must be 2 to 50 characters in length.
        # 
        # The name can contain letters, digits, underscores (_), periods (.), hyphens (-), and spaces.
        # 
        # The name must be unique in the resource directory.
        # 
        # This parameter is required.
        self.display_name = display_name
        # The ID of the parent folder.
        self.parent_folder_id = parent_folder_id
        # The ID of the billing account. If you leave this parameter empty, the newly created member is used as its billing account.
        self.payer_account_id = payer_account_id
        # The identity type of the member. Valid values:
        # 
        # *   resell (default): The member is an account for a reseller. A relationship is automatically established between the member and the reseller. The management account of the resource directory must be used as the billing account of the member.
        # *   non_resell: The member is not an account for a reseller. The member is an account that is not associated with a reseller. You can directly use the account to purchase Alibaba Cloud resources. The member is used as its own billing account.
        # 
        # >  This parameter is available only for resellers at the international site (alibabacloud.com).
        self.resell_account_type = resell_account_type
        # The tag of the member.
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

