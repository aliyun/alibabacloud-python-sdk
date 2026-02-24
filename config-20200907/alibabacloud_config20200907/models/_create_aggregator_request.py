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
        # The member accounts of the account group.
        # 
        # > - If you set `AggregatorType` to \\`RD, you can leave this parameter empty. This indicates that all members in the resource directory are added to the global account group.
        # >
        # > - If you set `AggregatorType` to `FOLDER`, you can leave this parameter empty. This indicates that all members in a specific folder in the resource directory are added to the folder account group.
        self.aggregator_accounts = aggregator_accounts
        # The name of the account group.
        # 
        # This parameter is required.
        self.aggregator_name = aggregator_name
        # The type of the account group. Valid values:
        # 
        # - RD: global account group.
        # 
        # - FOLDER: folder account group. You must also set the `FolderId` parameter. For more information about how to obtain a folder ID, see [ListAccounts](https://help.aliyun.com/document_detail/160016.html).
        # 
        # - CUSTOM (default): custom account group. You must also set the `AccountId` and `AccountType` parameters for `AggregatorAccounts`.
        self.aggregator_type = aggregator_type
        # A client token that is used to ensure the idempotence of the request. You must make sure that the token is unique for different requests. The `ClientToken` parameter can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The description of the account group.
        self.description = description
        # The ID of the attached folder. You can specify multiple folder IDs. Separate the IDs with commas (,).
        # 
        # This parameter is required if you set `AggregatorType` to `FOLDER`.
        self.folder_id = folder_id
        # The tags of the resource.
        # 
        # You can attach a maximum of 20 tags.
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
        # The tag key of the resource. You can specify a maximum of 20 tag keys. The tag key cannot be an empty string.
        # 
        # A tag key can be up to 128 characters in length. It cannot start with aliyun or acs: and cannot contain http\\:// or https\\://.
        self.key = key
        # The tag value of the resource. You can specify a maximum of 20 tag values. The tag value can be an empty string.
        # 
        # A tag value can be up to 128 characters in length. It cannot start with `aliyun` or `acs:` and cannot contain `http://` or `https://`.
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
        # The member ID. For more information about how to obtain the member ID, see [ListAccounts](https://help.aliyun.com/document_detail/160016.html).
        self.account_id = account_id
        # The member name. For more information about how to obtain the member name, see [ListAccounts](https://help.aliyun.com/document_detail/160016.html).
        self.account_name = account_name
        # The affiliation of the member. Only `ResourceDirectory` is supported.
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

