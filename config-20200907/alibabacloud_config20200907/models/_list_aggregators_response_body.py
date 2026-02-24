# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class ListAggregatorsResponseBody(DaraModel):
    def __init__(
        self,
        aggregators_result: main_models.ListAggregatorsResponseBodyAggregatorsResult = None,
        request_id: str = None,
    ):
        self.aggregators_result = aggregators_result
        self.request_id = request_id

    def validate(self):
        if self.aggregators_result:
            self.aggregators_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aggregators_result is not None:
            result['AggregatorsResult'] = self.aggregators_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorsResult') is not None:
            temp_model = main_models.ListAggregatorsResponseBodyAggregatorsResult()
            self.aggregators_result = temp_model.from_map(m.get('AggregatorsResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListAggregatorsResponseBodyAggregatorsResult(DaraModel):
    def __init__(
        self,
        aggregators: List[main_models.ListAggregatorsResponseBodyAggregatorsResultAggregators] = None,
        next_token: str = None,
    ):
        self.aggregators = aggregators
        self.next_token = next_token

    def validate(self):
        if self.aggregators:
            for v1 in self.aggregators:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Aggregators'] = []
        if self.aggregators is not None:
            for k1 in self.aggregators:
                result['Aggregators'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.aggregators = []
        if m.get('Aggregators') is not None:
            for k1 in m.get('Aggregators'):
                temp_model = main_models.ListAggregatorsResponseBodyAggregatorsResultAggregators()
                self.aggregators.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

class ListAggregatorsResponseBodyAggregatorsResultAggregators(DaraModel):
    def __init__(
        self,
        account_id: int = None,
        aggregator_account_count: int = None,
        aggregator_create_timestamp: int = None,
        aggregator_id: str = None,
        aggregator_name: str = None,
        aggregator_status: int = None,
        aggregator_type: str = None,
        description: str = None,
        folder_id: str = None,
        tags: List[main_models.ListAggregatorsResponseBodyAggregatorsResultAggregatorsTags] = None,
    ):
        self.account_id = account_id
        self.aggregator_account_count = aggregator_account_count
        self.aggregator_create_timestamp = aggregator_create_timestamp
        self.aggregator_id = aggregator_id
        self.aggregator_name = aggregator_name
        self.aggregator_status = aggregator_status
        self.aggregator_type = aggregator_type
        self.description = description
        self.folder_id = folder_id
        self.tags = tags

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

        if self.aggregator_account_count is not None:
            result['AggregatorAccountCount'] = self.aggregator_account_count

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

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListAggregatorsResponseBodyAggregatorsResultAggregatorsTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class ListAggregatorsResponseBodyAggregatorsResultAggregatorsTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
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

