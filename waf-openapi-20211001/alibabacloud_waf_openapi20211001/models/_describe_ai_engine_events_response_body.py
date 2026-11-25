# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeAiEngineEventsResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeAiEngineEventsResponseBodyItems] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of events.
        self.items = items
        # The number of entries to return per page in a paging query. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # The token for the next page. If a next page exists, this field returns a value.
        # > If this parameter returns a value, a next page exists. You can use the returned **NextToken** as a request parameter to retrieve the next page until no value is returned, which indicates that all data has been retrieved.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The total number of events that meet the query conditions.
        self.total_count = total_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeAiEngineEventsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeAiEngineEventsResponseBodyItems(DaraModel):
    def __init__(
        self,
        attack_sources: List[main_models.DescribeAiEngineEventsResponseBodyItemsAttackSources] = None,
        bypass_request_count: int = None,
        domains: List[str] = None,
        event_id: str = None,
        event_name: str = None,
        event_node_count: int = None,
        evidence_request_count: int = None,
        first_seen_at: int = None,
        handle_status: str = None,
        last_seen_at: int = None,
        related_event_ids: str = None,
        resources: List[str] = None,
        risk_level: str = None,
    ):
        # The list of attack source groups for the event.
        self.attack_sources = attack_sources
        # The statistics of suspected bypass evidence requests for the event.
        self.bypass_request_count = bypass_request_count
        # The list of domain names involved in the event.
        self.domains = domains
        # The ID of the event.
        self.event_id = event_id
        # The name of the event in the selected language.
        self.event_name = event_name
        # The number of nodes included in the event.
        self.event_node_count = event_node_count
        # The statistics of evidence requests for the event.
        self.evidence_request_count = evidence_request_count
        # The time when the event was first detected. The value is a UNIX timestamp in UTC. Unit: milliseconds.
        self.first_seen_at = first_seen_at
        # The current manual handling status. Valid values:
        # 
        # - **unhandled**: Unhandled.
        # 
        # - **handling**: In progress.
        # 
        # - **handled**: Handled.
        self.handle_status = handle_status
        # The time when the event was last detected. The value is a UNIX timestamp in UTC. Unit: milliseconds.
        self.last_seen_at = last_seen_at
        # The IDs of the related events. Multiple IDs are separated by commas (,).
        self.related_event_ids = related_event_ids
        # The list of protected objects involved in the event.
        self.resources = resources
        # The current risk level. Valid values:
        # 
        # - **critical**: Critical.
        # 
        # - **high**: High.
        # 
        # - **medium**: Medium.
        # 
        # - **low**: Low.
        self.risk_level = risk_level

    def validate(self):
        if self.attack_sources:
            for v1 in self.attack_sources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AttackSources'] = []
        if self.attack_sources is not None:
            for k1 in self.attack_sources:
                result['AttackSources'].append(k1.to_map() if k1 else None)

        if self.bypass_request_count is not None:
            result['BypassRequestCount'] = self.bypass_request_count

        if self.domains is not None:
            result['Domains'] = self.domains

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.event_name is not None:
            result['EventName'] = self.event_name

        if self.event_node_count is not None:
            result['EventNodeCount'] = self.event_node_count

        if self.evidence_request_count is not None:
            result['EvidenceRequestCount'] = self.evidence_request_count

        if self.first_seen_at is not None:
            result['FirstSeenAt'] = self.first_seen_at

        if self.handle_status is not None:
            result['HandleStatus'] = self.handle_status

        if self.last_seen_at is not None:
            result['LastSeenAt'] = self.last_seen_at

        if self.related_event_ids is not None:
            result['RelatedEventIds'] = self.related_event_ids

        if self.resources is not None:
            result['Resources'] = self.resources

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attack_sources = []
        if m.get('AttackSources') is not None:
            for k1 in m.get('AttackSources'):
                temp_model = main_models.DescribeAiEngineEventsResponseBodyItemsAttackSources()
                self.attack_sources.append(temp_model.from_map(k1))

        if m.get('BypassRequestCount') is not None:
            self.bypass_request_count = m.get('BypassRequestCount')

        if m.get('Domains') is not None:
            self.domains = m.get('Domains')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        if m.get('EventNodeCount') is not None:
            self.event_node_count = m.get('EventNodeCount')

        if m.get('EvidenceRequestCount') is not None:
            self.evidence_request_count = m.get('EvidenceRequestCount')

        if m.get('FirstSeenAt') is not None:
            self.first_seen_at = m.get('FirstSeenAt')

        if m.get('HandleStatus') is not None:
            self.handle_status = m.get('HandleStatus')

        if m.get('LastSeenAt') is not None:
            self.last_seen_at = m.get('LastSeenAt')

        if m.get('RelatedEventIds') is not None:
            self.related_event_ids = m.get('RelatedEventIds')

        if m.get('Resources') is not None:
            self.resources = m.get('Resources')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        return self

class DescribeAiEngineEventsResponseBodyItemsAttackSources(DaraModel):
    def __init__(
        self,
        sources: List[main_models.DescribeAiEngineEventsResponseBodyItemsAttackSourcesSources] = None,
        type: str = None,
    ):
        # The list of attack sources of the specified type.
        self.sources = sources
        # The type of the attack source. Valid values:
        # 
        # - **ip**: IP address.
        self.type = type

    def validate(self):
        if self.sources:
            for v1 in self.sources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Sources'] = []
        if self.sources is not None:
            for k1 in self.sources:
                result['Sources'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sources = []
        if m.get('Sources') is not None:
            for k1 in m.get('Sources'):
                temp_model = main_models.DescribeAiEngineEventsResponseBodyItemsAttackSourcesSources()
                self.sources.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeAiEngineEventsResponseBodyItemsAttackSourcesSources(DaraModel):
    def __init__(
        self,
        attribute: str = None,
        value: str = None,
    ):
        # The display attribute of the attack source, such as the region code.
        self.attribute = attribute
        # The value of the attack source. If the attack source type is IP address (the **Type** parameter is set to **ip**), the value is an IP address.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attribute is not None:
            result['Attribute'] = self.attribute

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attribute') is not None:
            self.attribute = m.get('Attribute')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

