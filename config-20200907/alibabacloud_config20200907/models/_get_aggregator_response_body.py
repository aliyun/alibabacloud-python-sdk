# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class GetAggregatorResponseBody(DaraModel):
    def __init__(
        self,
        aggregator: main_models.GetAggregatorResponseBodyAggregator = None,
        request_id: str = None,
    ):
        # The details of the account group.
        self.aggregator = aggregator
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.aggregator:
            self.aggregator.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aggregator is not None:
            result['Aggregator'] = self.aggregator.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Aggregator') is not None:
            temp_model = main_models.GetAggregatorResponseBodyAggregator()
            self.aggregator = temp_model.from_map(m.get('Aggregator'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetAggregatorResponseBodyAggregator(DaraModel):
    def __init__(
        self,
        account_id: int = None,
        aggregator_account_count: int = None,
        aggregator_accounts: List[main_models.GetAggregatorResponseBodyAggregatorAggregatorAccounts] = None,
        aggregator_create_timestamp: str = None,
        aggregator_id: str = None,
        aggregator_name: str = None,
        aggregator_status: int = None,
        aggregator_type: str = None,
        description: str = None,
        folder_id: str = None,
        folder_name: str = None,
        tags: List[main_models.GetAggregatorResponseBodyAggregatorTags] = None,
    ):
        # The ID of the management account that is used to create the account group.
        self.account_id = account_id
        # The number of members in the account group.
        self.aggregator_account_count = aggregator_account_count
        # The information about the members in the account group.
        self.aggregator_accounts = aggregator_accounts
        # The timestamp generated when the account group was created.
        # 
        # Unit: milliseconds.
        self.aggregator_create_timestamp = aggregator_create_timestamp
        # The ID of the account group.
        self.aggregator_id = aggregator_id
        # The name of the account group.
        self.aggregator_name = aggregator_name
        # The status of the account group. Valid values:
        # 
        # *   0: The account group is being created.
        # *   1: The account group was created.
        self.aggregator_status = aggregator_status
        # The type of the account group. Valid values:
        # 
        # *   RD: a global account group.
        # *   FOLDER: an account group for a folder.
        # *   CUSTOM: a custom account group.
        self.aggregator_type = aggregator_type
        # The description of the account group.
        self.description = description
        # The ID of the attached folder of the account group.
        self.folder_id = folder_id
        self.folder_name = folder_name
        # tags
        self.tags = tags

    def validate(self):
        if self.aggregator_accounts:
            for v1 in self.aggregator_accounts:
                 if v1:
                    v1.validate()
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

        if self.aggregator_account_count is not None:
            result['AggregatorAccountCount'] = self.aggregator_account_count

        result['AggregatorAccounts'] = []
        if self.aggregator_accounts is not None:
            for k1 in self.aggregator_accounts:
                result['AggregatorAccounts'].append(k1.to_map() if k1 else None)

        if self.aggregator_create_timestamp is not None:
            result['AggregatorCreateTimestamp'] = self.aggregator_create_timestamp

        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id

        if self.aggregator_name is not None:
            result['AggregatorName'] = self.aggregator_name

        if self.aggregator_status is not None:
            result['AggregatorStatus'] = self.aggregator_status

        if self.aggregator_type is not None:
            result['AggregatorType'] = self.aggregator_type

        if self.description is not None:
            result['Description'] = self.description

        if self.folder_id is not None:
            result['FolderId'] = self.folder_id

        if self.folder_name is not None:
            result['FolderName'] = self.folder_name

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('AggregatorAccountCount') is not None:
            self.aggregator_account_count = m.get('AggregatorAccountCount')

        self.aggregator_accounts = []
        if m.get('AggregatorAccounts') is not None:
            for k1 in m.get('AggregatorAccounts'):
                temp_model = main_models.GetAggregatorResponseBodyAggregatorAggregatorAccounts()
                self.aggregator_accounts.append(temp_model.from_map(k1))

        if m.get('AggregatorCreateTimestamp') is not None:
            self.aggregator_create_timestamp = m.get('AggregatorCreateTimestamp')

        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')

        if m.get('AggregatorName') is not None:
            self.aggregator_name = m.get('AggregatorName')

        if m.get('AggregatorStatus') is not None:
            self.aggregator_status = m.get('AggregatorStatus')

        if m.get('AggregatorType') is not None:
            self.aggregator_type = m.get('AggregatorType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')

        if m.get('FolderName') is not None:
            self.folder_name = m.get('FolderName')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetAggregatorResponseBodyAggregatorTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class GetAggregatorResponseBodyAggregatorTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

class GetAggregatorResponseBodyAggregatorAggregatorAccounts(DaraModel):
    def __init__(
        self,
        account_id: int = None,
        account_name: str = None,
        account_type: str = None,
        recorder_status: str = None,
    ):
        # The ID of the member.
        self.account_id = account_id
        # The display name of the member.
        self.account_name = account_name
        # The resource directory to which the member belongs. Valid value: ResourceDirectory. ResourceDirectory indicates that the member belongs to a resource directory.
        self.account_type = account_type
        # The status of the configuration recorder for the member. Valid values:
        # 
        # *   REGISTRABLE: The configuration recorder is not registered.
        # *   BUILDING: The configuration recorder is being deployed.
        # *   REGISTERED: The configuration recorder is registered.
        # *   REBUILDING: The configuration recorder is being redeployed.
        self.recorder_status = recorder_status

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

        if self.recorder_status is not None:
            result['RecorderStatus'] = self.recorder_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')

        if m.get('RecorderStatus') is not None:
            self.recorder_status = m.get('RecorderStatus')

        return self

