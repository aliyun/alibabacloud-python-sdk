# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class UpdateAggregatorRequest(DaraModel):
    def __init__(
        self,
        aggregator_accounts: List[main_models.UpdateAggregatorRequestAggregatorAccounts] = None,
        aggregator_id: str = None,
        aggregator_name: str = None,
        client_token: str = None,
        description: str = None,
        folder_id: str = None,
        tag: List[main_models.UpdateAggregatorRequestTag] = None,
    ):
        # The members in the account group.
        # 
        # >  When you modify the configurations of an account group, this parameter can be left empty. In this case, the member list is not updated. If you want to update the member list, you must configure both the `AccountId` and `AccountType` parameters.
        self.aggregator_accounts = aggregator_accounts
        # The ID of the account group.
        # 
        # For more information about how to obtain the ID of an account group, see [ListAggregators](https://help.aliyun.com/document_detail/255797.html).
        # 
        # This parameter is required.
        self.aggregator_id = aggregator_id
        # The name of the account group.
        # 
        # For more information about how to obtain the name of an account group, see [ListAggregators](https://help.aliyun.com/document_detail/255797.html).
        self.aggregator_name = aggregator_name
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The description of the account group.
        # 
        # For more information about how to obtain the description of an account group, see [ListAggregators](https://help.aliyun.com/document_detail/255797.html).
        self.description = description
        # The folder ID. Separate multiple folder IDs with commas (,).
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

        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id

        if self.aggregator_name is not None:
            result['AggregatorName'] = self.aggregator_name

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
                temp_model = main_models.UpdateAggregatorRequestAggregatorAccounts()
                self.aggregator_accounts.append(temp_model.from_map(k1))

        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')

        if m.get('AggregatorName') is not None:
            self.aggregator_name = m.get('AggregatorName')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.UpdateAggregatorRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class UpdateAggregatorRequestTag(DaraModel):
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

class UpdateAggregatorRequestAggregatorAccounts(DaraModel):
    def __init__(
        self,
        account_id: int = None,
        account_name: str = None,
        account_type: str = None,
    ):
        # The ID of the member.
        # 
        # For more information about how to obtain the ID of a member, see [ListAccounts](https://help.aliyun.com/document_detail/160016.html).
        # 
        # >  If you want to update the member list, you must configure both the `AccountId` and `AccountType` parameters.
        self.account_id = account_id
        # The display name of the member.
        # 
        # For more information about how to obtain the name of a member, see [ListAccounts](https://help.aliyun.com/document_detail/160016.html).
        # 
        # >  If you want to update the member list, you must configure both the `AccountId` and `AccountType` parameters.
        self.account_name = account_name
        # The resource directory to which the member belongs. Valid value: ResourceDirectory. ResourceDirectory indicates that the member belongs to a resource directory.
        # 
        # >  If you want to update the member list, you must configure both the `AccountId` and `AccountType` parameters.
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

