# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeAiEngineEventResponseBody(DaraModel):
    def __init__(
        self,
        attack_sources: List[main_models.DescribeAiEngineEventResponseBodyAttackSources] = None,
        bypass_request_count: int = None,
        domains: List[str] = None,
        event_id: str = None,
        event_name: str = None,
        event_node_count: int = None,
        event_summary: str = None,
        evidence_request_count: int = None,
        first_seen_at: int = None,
        handle_status: str = None,
        last_seen_at: int = None,
        related_event_ids: str = None,
        report_markdown: str = None,
        request_id: str = None,
        resources: List[str] = None,
        risk_level: str = None,
    ):
        # The grouped list of attack sources for the event.
        self.attack_sources = attack_sources
        # The statistical value of suspected bypass evidence requests for the event.
        self.bypass_request_count = bypass_request_count
        # The domain names involved in the event.
        self.domains = domains
        # The event ID.
        self.event_id = event_id
        # The name of the event in the specified language.
        self.event_name = event_name
        # The number of nodes included in the event.
        self.event_node_count = event_node_count
        # The summary of the event in the specified language.
        self.event_summary = event_summary
        # The statistical value of evidence requests for the event.
        self.evidence_request_count = evidence_request_count
        # The time when the event was first detected. The time is a UNIX timestamp in UTC. Unit: milliseconds.
        self.first_seen_at = first_seen_at
        # The current manual handling status. Valid values:
        # 
        # - **unhandled**: Unhandled.
        # 
        # - **handling**: Handling.
        # 
        # - **handled**: Handled.
        self.handle_status = handle_status
        # The time when the event was last detected. The time is a UNIX timestamp in UTC. Unit: milliseconds.
        self.last_seen_at = last_seen_at
        # The IDs of the related events. Multiple IDs are separated by commas (,).
        self.related_event_ids = related_event_ids
        # The event analysis report in Markdown format in the specified language.
        self.report_markdown = report_markdown
        # The ID of the request.
        self.request_id = request_id
        # The IDs of the protected objects involved in the event.
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

        if self.event_summary is not None:
            result['EventSummary'] = self.event_summary

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

        if self.report_markdown is not None:
            result['ReportMarkdown'] = self.report_markdown

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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
                temp_model = main_models.DescribeAiEngineEventResponseBodyAttackSources()
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

        if m.get('EventSummary') is not None:
            self.event_summary = m.get('EventSummary')

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

        if m.get('ReportMarkdown') is not None:
            self.report_markdown = m.get('ReportMarkdown')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Resources') is not None:
            self.resources = m.get('Resources')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        return self

class DescribeAiEngineEventResponseBodyAttackSources(DaraModel):
    def __init__(
        self,
        sources: List[main_models.DescribeAiEngineEventResponseBodyAttackSourcesSources] = None,
        type: str = None,
    ):
        # The list of sources of this type.
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
                temp_model = main_models.DescribeAiEngineEventResponseBodyAttackSourcesSources()
                self.sources.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeAiEngineEventResponseBodyAttackSourcesSources(DaraModel):
    def __init__(
        self,
        attribute: str = None,
        value: str = None,
    ):
        # The display attribute of the source, such as the region code.
        self.attribute = attribute
        # The value of the attack source. If the attack source type is IP address (**Type** is set to **ip**), this parameter indicates the IP address.
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

