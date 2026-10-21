# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20241212 import models as main_models
from darabonba.model import DaraModel

class ListAlertAggregationsResponseBody(DaraModel):
    def __init__(
        self,
        alert_aggregations: List[main_models.ListAlertAggregationsResponseBodyAlertAggregations] = None,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of alert groups returned based on the specified aggregation method, sorted by alert count in descending order.
        self.alert_aggregations = alert_aggregations
        # The maximum number of entries returned in this request.
        self.max_results = max_results
        # The token for the next query.
        self.next_token = next_token
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of records.
        self.total_count = total_count

    def validate(self):
        if self.alert_aggregations:
            for v1 in self.alert_aggregations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AlertAggregations'] = []
        if self.alert_aggregations is not None:
            for k1 in self.alert_aggregations:
                result['AlertAggregations'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

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
        self.alert_aggregations = []
        if m.get('AlertAggregations') is not None:
            for k1 in m.get('AlertAggregations'):
                temp_model = main_models.ListAlertAggregationsResponseBodyAlertAggregations()
                self.alert_aggregations.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListAlertAggregationsResponseBodyAlertAggregations(DaraModel):
    def __init__(
        self,
        account_display_values: List[str] = None,
        account_ids: List[str] = None,
        aggregation_key: str = None,
        aggregation_type: str = None,
        alert_count: int = None,
        attack_stages: List[str] = None,
        defense_action_counts: List[main_models.ListAlertAggregationsResponseBodyAlertAggregationsDefenseActionCounts] = None,
        first_time: int = None,
        latest_time: int = None,
        primary_display_value: str = None,
        primary_value: str = None,
        secondary_value: str = None,
        source_codes: List[str] = None,
        status_counts: List[main_models.ListAlertAggregationsResponseBodyAlertAggregationsStatusCounts] = None,
    ):
        # The list of account display values associated with the aggregation group, in one-to-one correspondence with AccountIds. When the username is valid and differs from the account ID, the format is "username/account ID". Otherwise, only the account ID is returned.
        self.account_display_values = account_display_values
        # The list of member accounts IDs for which the report is generated. You need to specify this parameter only when you generate a multi-account report and want to limit the report to specific member accounts.
        self.account_ids = account_ids
        # The unique identifier of the aggregation group, which is a concatenation of AggregationType, PrimaryValue, and SecondaryValue joined by colons (:). The last segment is empty if no secondary aggregation value exists.
        self.aggregation_key = aggregation_key
        # The aggregation method.
        self.aggregation_type = aggregation_type
        # The number of consecutive failures. This parameter is optional.
        self.alert_count = alert_count
        # The collection of MITRE ATT&CK attack techniques associated with alerts in the aggregation group. Each element is a JSON array string.
        self.attack_stages = attack_stages
        # The quantity distribution by defense action within the aggregation group. Name is the action field value, and Value is the corresponding alert count.
        self.defense_action_counts = defense_action_counts
        # The time of the first access, represented as a UNIX timestamp in seconds.
        self.first_time = first_time
        # The most recent time when the attack event occurred.
        self.latest_time = latest_time
        # The display text of the primary aggregation value. For account aggregation, the format is "username/account ID". If no valid username exists, only the account ID is returned. For event summaries, the event name is returned based on the Lang parameter. If the name is missing, the event UUID is returned.
        self.primary_display_value = primary_display_value
        # The value corresponding to the primary query condition.
        self.primary_value = primary_value
        # The value corresponding to the secondary query condition.
        self.secondary_value = secondary_value
        # The collection of event source codes.
        # 
        # > Example: [\\\\\\"MRM\\\\\\"]
        self.source_codes = source_codes
        # The quantity distribution by alert status within the aggregation group. Name is the alert status value, and Value is the corresponding alert count.
        self.status_counts = status_counts

    def validate(self):
        if self.defense_action_counts:
            for v1 in self.defense_action_counts:
                 if v1:
                    v1.validate()
        if self.status_counts:
            for v1 in self.status_counts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_display_values is not None:
            result['AccountDisplayValues'] = self.account_display_values

        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids

        if self.aggregation_key is not None:
            result['AggregationKey'] = self.aggregation_key

        if self.aggregation_type is not None:
            result['AggregationType'] = self.aggregation_type

        if self.alert_count is not None:
            result['AlertCount'] = self.alert_count

        if self.attack_stages is not None:
            result['AttackStages'] = self.attack_stages

        result['DefenseActionCounts'] = []
        if self.defense_action_counts is not None:
            for k1 in self.defense_action_counts:
                result['DefenseActionCounts'].append(k1.to_map() if k1 else None)

        if self.first_time is not None:
            result['FirstTime'] = self.first_time

        if self.latest_time is not None:
            result['LatestTime'] = self.latest_time

        if self.primary_display_value is not None:
            result['PrimaryDisplayValue'] = self.primary_display_value

        if self.primary_value is not None:
            result['PrimaryValue'] = self.primary_value

        if self.secondary_value is not None:
            result['SecondaryValue'] = self.secondary_value

        if self.source_codes is not None:
            result['SourceCodes'] = self.source_codes

        result['StatusCounts'] = []
        if self.status_counts is not None:
            for k1 in self.status_counts:
                result['StatusCounts'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountDisplayValues') is not None:
            self.account_display_values = m.get('AccountDisplayValues')

        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')

        if m.get('AggregationKey') is not None:
            self.aggregation_key = m.get('AggregationKey')

        if m.get('AggregationType') is not None:
            self.aggregation_type = m.get('AggregationType')

        if m.get('AlertCount') is not None:
            self.alert_count = m.get('AlertCount')

        if m.get('AttackStages') is not None:
            self.attack_stages = m.get('AttackStages')

        self.defense_action_counts = []
        if m.get('DefenseActionCounts') is not None:
            for k1 in m.get('DefenseActionCounts'):
                temp_model = main_models.ListAlertAggregationsResponseBodyAlertAggregationsDefenseActionCounts()
                self.defense_action_counts.append(temp_model.from_map(k1))

        if m.get('FirstTime') is not None:
            self.first_time = m.get('FirstTime')

        if m.get('LatestTime') is not None:
            self.latest_time = m.get('LatestTime')

        if m.get('PrimaryDisplayValue') is not None:
            self.primary_display_value = m.get('PrimaryDisplayValue')

        if m.get('PrimaryValue') is not None:
            self.primary_value = m.get('PrimaryValue')

        if m.get('SecondaryValue') is not None:
            self.secondary_value = m.get('SecondaryValue')

        if m.get('SourceCodes') is not None:
            self.source_codes = m.get('SourceCodes')

        self.status_counts = []
        if m.get('StatusCounts') is not None:
            for k1 in m.get('StatusCounts'):
                temp_model = main_models.ListAlertAggregationsResponseBodyAlertAggregationsStatusCounts()
                self.status_counts.append(temp_model.from_map(k1))

        return self

class ListAlertAggregationsResponseBodyAlertAggregationsStatusCounts(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: int = None,
    ):
        # The display name of the entity attribute field that can be added to the whitelist.
        self.name = name
        # The right-hand value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListAlertAggregationsResponseBodyAlertAggregationsDefenseActionCounts(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: int = None,
    ):
        # The display name of the entity attribute field that can be added to the whitelist.
        self.name = name
        # The default right-hand value displayed for the whitelist rule.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

