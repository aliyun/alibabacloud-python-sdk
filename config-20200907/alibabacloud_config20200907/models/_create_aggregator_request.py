# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class CreateAggregatorRequest(DaraModel):
    def __init__(
        self,
        aggregator_accounts: List[main_models.CreateAggregatorRequestAggregatorAccounts] = None,
        aggregator_name: str = None,
        aggregator_type: str = None,
        client_token: str = None,
        description: str = None,
        folder_id: str = None,
        tag: List[main_models.CreateAggregatorRequestTag] = None,
    ):
        # The information about the member accounts in the account group. Example:
        # 
        #     [{
        #     	"accountId": 171322098523****,
        #     	"accountType":"ResourceDirectory",
        #                     "accountName":"Alice"
        #     }, {
        #     	"accountId": 100532098349****,
        #     	"accountType":"ResourceDirectory",
        #                     "accountName":"Tom"
        #     }]
        # 
        # >  If `AggregatorType` is set to `RD` or `FOLDER`, this parameter can be left empty, which indicates that all accounts in the resource directory are added to the global account group.
        self.aggregator_accounts = aggregator_accounts
        # The name of the account group.
        # 
        # This parameter is required.
        self.aggregator_name = aggregator_name
        # The type of the account group. Valid values:
        # 
        # *   RD: global account group.
        # *   FOLDER: account group of the folder.
        # *   CUSTOM (default): custom account group.
        self.aggregator_type = aggregator_type
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The `token` can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The description of the account group.
        self.description = description
        # The ID of the folder to which the account group is attached. You must specify this parameter if `AggregatorType` is set to `FOLDER`. Multiple resource folder IDs should be separated by commas (,).
        self.folder_id = folder_id
        # The tags of the resource.
        # 
        # You can add up to 20 tags to a resource.
        self.tag = tag

    def validate(self):
        if self.aggregator_accounts:
            for v1 in self.aggregator_accounts:
                 if v1:
                    v1.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AggregatorAccounts'] = []
        if self.aggregator_accounts is not None:
            for k1 in self.aggregator_accounts:
                result['AggregatorAccounts'].append(k1.to_map() if k1 else None)

        if self.aggregator_name is not None:
            result['AggregatorName'] = self.aggregator_name

        if self.aggregator_type is not None:
            result['AggregatorType'] = self.aggregator_type

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.folder_id is not None:
            result['FolderId'] = self.folder_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.aggregator_accounts = []
        if m.get('AggregatorAccounts') is not None:
            for k1 in m.get('AggregatorAccounts'):
                temp_model = main_models.CreateAggregatorRequestAggregatorAccounts()
                self.aggregator_accounts.append(temp_model.from_map(k1))

        if m.get('AggregatorName') is not None:
            self.aggregator_name = m.get('AggregatorName')

        if m.get('AggregatorType') is not None:
            self.aggregator_type = m.get('AggregatorType')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateAggregatorRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class CreateAggregatorRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the resource. You can specify up to 20 tag keys.
        # 
        # The tag key cannot be an empty string. The tag key must be 1 to 64 characters in length and cannot start with `aliyun` or `acs`:. The tag key cannot contain `http://` or `https://`.
        self.key = key
        # The tag values.
        # 
        # The tag values can be an empty string or up to 128 characters in length. The tag values cannot start with `aliyun` or `acs:` and cannot contain `http://` or `https://`.
        # 
        # Each key-value must be unique. You can specify at most 20 tag values in each call.
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

class CreateAggregatorRequestAggregatorAccounts(DaraModel):
    def __init__(
        self,
        account_id: int = None,
        account_name: str = None,
        account_type: str = None,
    ):
        # The member account ID. For more information about how to obtain the ID of a member account, see [ListAccounts](https://help.aliyun.com/document_detail/160016.html).
        self.account_id = account_id
        # The name of the member account. For more information about how to obtain the name of a member account, see [ListAccounts](https://help.aliyun.com/document_detail/160016.html).
        self.account_name = account_name
        # The type of the member account. Set this parameter to ResourceDirectory.
        self.account_type = account_type

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

        if self.account_type is not None:
            result['AccountType'] = self.account_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')

        return self

