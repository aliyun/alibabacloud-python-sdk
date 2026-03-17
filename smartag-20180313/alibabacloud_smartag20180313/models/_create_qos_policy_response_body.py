# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smartag20180313 import models as main_models
from darabonba.model import DaraModel

class CreateQosPolicyResponseBody(DaraModel):
    def __init__(
        self,
        description: str = None,
        dest_cidr: str = None,
        dest_port_range: str = None,
        dpi_group_ids: main_models.CreateQosPolicyResponseBodyDpiGroupIds = None,
        dpi_signature_ids: main_models.CreateQosPolicyResponseBodyDpiSignatureIds = None,
        end_time: str = None,
        ip_protocol: str = None,
        name: str = None,
        priority: int = None,
        qos_id: str = None,
        qos_policy_id: str = None,
        request_id: str = None,
        source_cidr: str = None,
        source_port_range: str = None,
        start_time: str = None,
    ):
        # The description of the traffic classification rule.
        self.description = description
        # The destination CIDR block.
        self.dest_cidr = dest_cidr
        # The destination port range.
        self.dest_port_range = dest_port_range
        self.dpi_group_ids = dpi_group_ids
        self.dpi_signature_ids = dpi_signature_ids
        # The time when the traffic classification rule expires.
        self.end_time = end_time
        # The protocol that applies to the traffic classification rule.
        self.ip_protocol = ip_protocol
        # The name of the traffic classification rule.
        self.name = name
        # The priority of the traffic throttling policy to which the traffic classification rule belongs.
        self.priority = priority
        # The ID of the QoS policy.
        self.qos_id = qos_id
        # The ID of the traffic classification rule.
        self.qos_policy_id = qos_policy_id
        # The ID of the request.
        self.request_id = request_id
        # The source CIDR block.
        self.source_cidr = source_cidr
        # The source port range.
        self.source_port_range = source_port_range
        # The time when the traffic classification rule takes effect.
        self.start_time = start_time

    def validate(self):
        if self.dpi_group_ids:
            self.dpi_group_ids.validate()
        if self.dpi_signature_ids:
            self.dpi_signature_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.dest_cidr is not None:
            result['DestCidr'] = self.dest_cidr

        if self.dest_port_range is not None:
            result['DestPortRange'] = self.dest_port_range

        if self.dpi_group_ids is not None:
            result['DpiGroupIds'] = self.dpi_group_ids.to_map()

        if self.dpi_signature_ids is not None:
            result['DpiSignatureIds'] = self.dpi_signature_ids.to_map()

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol

        if self.name is not None:
            result['Name'] = self.name

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.qos_id is not None:
            result['QosId'] = self.qos_id

        if self.qos_policy_id is not None:
            result['QosPolicyId'] = self.qos_policy_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.source_cidr is not None:
            result['SourceCidr'] = self.source_cidr

        if self.source_port_range is not None:
            result['SourcePortRange'] = self.source_port_range

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DestCidr') is not None:
            self.dest_cidr = m.get('DestCidr')

        if m.get('DestPortRange') is not None:
            self.dest_port_range = m.get('DestPortRange')

        if m.get('DpiGroupIds') is not None:
            temp_model = main_models.CreateQosPolicyResponseBodyDpiGroupIds()
            self.dpi_group_ids = temp_model.from_map(m.get('DpiGroupIds'))

        if m.get('DpiSignatureIds') is not None:
            temp_model = main_models.CreateQosPolicyResponseBodyDpiSignatureIds()
            self.dpi_signature_ids = temp_model.from_map(m.get('DpiSignatureIds'))

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('QosId') is not None:
            self.qos_id = m.get('QosId')

        if m.get('QosPolicyId') is not None:
            self.qos_policy_id = m.get('QosPolicyId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SourceCidr') is not None:
            self.source_cidr = m.get('SourceCidr')

        if m.get('SourcePortRange') is not None:
            self.source_port_range = m.get('SourcePortRange')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class CreateQosPolicyResponseBodyDpiSignatureIds(DaraModel):
    def __init__(
        self,
        dpi_signature_id: List[str] = None,
    ):
        self.dpi_signature_id = dpi_signature_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dpi_signature_id is not None:
            result['DpiSignatureId'] = self.dpi_signature_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DpiSignatureId') is not None:
            self.dpi_signature_id = m.get('DpiSignatureId')

        return self

class CreateQosPolicyResponseBodyDpiGroupIds(DaraModel):
    def __init__(
        self,
        dpi_group_id: List[str] = None,
    ):
        self.dpi_group_id = dpi_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dpi_group_id is not None:
            result['DpiGroupId'] = self.dpi_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DpiGroupId') is not None:
            self.dpi_group_id = m.get('DpiGroupId')

        return self

