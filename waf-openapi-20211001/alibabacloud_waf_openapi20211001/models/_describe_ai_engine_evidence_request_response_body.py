# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeAiEngineEvidenceRequestResponseBody(DaraModel):
    def __init__(
        self,
        ai_interpretation: str = None,
        attack_sources: List[main_models.DescribeAiEngineEvidenceRequestResponseBodyAttackSources] = None,
        evidence_id: str = None,
        host: str = None,
        http_status: int = None,
        impact_type: str = None,
        method: str = None,
        node_id: str = None,
        request: str = None,
        request_id: str = None,
        request_path: str = None,
        request_time: int = None,
        resource: str = None,
        response: str = None,
        suspected_bypass: int = None,
        trace_id: str = None,
    ):
        # The AI interpretation result in the specified language, in Markdown format.
        self.ai_interpretation = ai_interpretation
        # The list of attack source groups for the request.
        self.attack_sources = attack_sources
        # The evidence ID.
        self.evidence_id = evidence_id
        # The host of the request.
        self.host = host
        # The HTTP response status code.
        self.http_status = http_status
        # The impact tag of the evidence. Valid values:
        # 
        # - **block**: The request is blocked.
        # 
        # - **challenge**: The request triggers a challenge.
        # 
        # - **monitor**: The request is monitored.
        # 
        # - **bypass**: The request is suspected to be a bypass.
        # 
        # - **attempt**: The request is a reconnaissance probe.
        self.impact_type = impact_type
        # The HTTP method.
        self.method = method
        # The ID of the associated node, which corresponds to the NodeId in the node list.
        self.node_id = node_id
        # The request content.
        self.request = request
        # The ID of the request.
        self.request_id = request_id
        # The masked request path.
        self.request_path = request_path
        # The time when the original request was made. The value is a UNIX timestamp in milliseconds.
        self.request_time = request_time
        # The ID of the protected object to which the request belongs.
        self.resource = resource
        # The response content.
        self.response = response
        # Specifies whether the request is suspected to be a bypass. Valid values:
        # 
        # - **1**: The request is suspected to be a bypass.
        # - **0**: The request is not a bypass.
        self.suspected_bypass = suspected_bypass
        # The trace ID of the original request, which can be up to 128 ASCII characters in length.
        self.trace_id = trace_id

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
        if self.ai_interpretation is not None:
            result['AiInterpretation'] = self.ai_interpretation

        result['AttackSources'] = []
        if self.attack_sources is not None:
            for k1 in self.attack_sources:
                result['AttackSources'].append(k1.to_map() if k1 else None)

        if self.evidence_id is not None:
            result['EvidenceId'] = self.evidence_id

        if self.host is not None:
            result['Host'] = self.host

        if self.http_status is not None:
            result['HttpStatus'] = self.http_status

        if self.impact_type is not None:
            result['ImpactType'] = self.impact_type

        if self.method is not None:
            result['Method'] = self.method

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.request is not None:
            result['Request'] = self.request

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.request_path is not None:
            result['RequestPath'] = self.request_path

        if self.request_time is not None:
            result['RequestTime'] = self.request_time

        if self.resource is not None:
            result['Resource'] = self.resource

        if self.response is not None:
            result['Response'] = self.response

        if self.suspected_bypass is not None:
            result['SuspectedBypass'] = self.suspected_bypass

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AiInterpretation') is not None:
            self.ai_interpretation = m.get('AiInterpretation')

        self.attack_sources = []
        if m.get('AttackSources') is not None:
            for k1 in m.get('AttackSources'):
                temp_model = main_models.DescribeAiEngineEvidenceRequestResponseBodyAttackSources()
                self.attack_sources.append(temp_model.from_map(k1))

        if m.get('EvidenceId') is not None:
            self.evidence_id = m.get('EvidenceId')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('HttpStatus') is not None:
            self.http_status = m.get('HttpStatus')

        if m.get('ImpactType') is not None:
            self.impact_type = m.get('ImpactType')

        if m.get('Method') is not None:
            self.method = m.get('Method')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('Request') is not None:
            self.request = m.get('Request')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RequestPath') is not None:
            self.request_path = m.get('RequestPath')

        if m.get('RequestTime') is not None:
            self.request_time = m.get('RequestTime')

        if m.get('Resource') is not None:
            self.resource = m.get('Resource')

        if m.get('Response') is not None:
            self.response = m.get('Response')

        if m.get('SuspectedBypass') is not None:
            self.suspected_bypass = m.get('SuspectedBypass')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self

class DescribeAiEngineEvidenceRequestResponseBodyAttackSources(DaraModel):
    def __init__(
        self,
        sources: List[main_models.DescribeAiEngineEvidenceRequestResponseBodyAttackSourcesSources] = None,
        type: str = None,
    ):
        # The list of sources of this type.
        self.sources = sources
        # The type of the attack source.
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
                temp_model = main_models.DescribeAiEngineEvidenceRequestResponseBodyAttackSourcesSources()
                self.sources.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeAiEngineEvidenceRequestResponseBodyAttackSourcesSources(DaraModel):
    def __init__(
        self,
        attribute: str = None,
        value: str = None,
    ):
        # The display attribute of the source, such as the region code.
        self.attribute = attribute
        # The value of the source, such as an IP address.
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

