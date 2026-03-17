# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smartag20180313 import models as main_models
from darabonba.model import DaraModel

class DescribeQosPoliciesResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        qos_policies: main_models.DescribeQosPoliciesResponseBodyQosPolicies = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        self.qos_policies = qos_policies
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.qos_policies:
            self.qos_policies.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.qos_policies is not None:
            result['QosPolicies'] = self.qos_policies.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('QosPolicies') is not None:
            temp_model = main_models.DescribeQosPoliciesResponseBodyQosPolicies()
            self.qos_policies = temp_model.from_map(m.get('QosPolicies'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeQosPoliciesResponseBodyQosPolicies(DaraModel):
    def __init__(
        self,
        qos_policy: List[main_models.DescribeQosPoliciesResponseBodyQosPoliciesQosPolicy] = None,
    ):
        self.qos_policy = qos_policy

    def validate(self):
        if self.qos_policy:
            for v1 in self.qos_policy:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['QosPolicy'] = []
        if self.qos_policy is not None:
            for k1 in self.qos_policy:
                result['QosPolicy'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.qos_policy = []
        if m.get('QosPolicy') is not None:
            for k1 in m.get('QosPolicy'):
                temp_model = main_models.DescribeQosPoliciesResponseBodyQosPoliciesQosPolicy()
                self.qos_policy.append(temp_model.from_map(k1))

        return self

class DescribeQosPoliciesResponseBodyQosPoliciesQosPolicy(DaraModel):
    def __init__(
        self,
        description: str = None,
        dest_cidr: str = None,
        dest_port_range: str = None,
        dpi_group_ids: main_models.DescribeQosPoliciesResponseBodyQosPoliciesQosPolicyDpiGroupIds = None,
        dpi_signature_ids: main_models.DescribeQosPoliciesResponseBodyQosPoliciesQosPolicyDpiSignatureIds = None,
        end_time: str = None,
        ip_protocol: str = None,
        name: str = None,
        priority: int = None,
        qos_id: str = None,
        qos_policy_id: str = None,
        source_cidr: str = None,
        source_port_range: str = None,
        start_time: str = None,
    ):
        self.description = description
        self.dest_cidr = dest_cidr
        self.dest_port_range = dest_port_range
        self.dpi_group_ids = dpi_group_ids
        self.dpi_signature_ids = dpi_signature_ids
        self.end_time = end_time
        self.ip_protocol = ip_protocol
        self.name = name
        self.priority = priority
        self.qos_id = qos_id
        self.qos_policy_id = qos_policy_id
        self.source_cidr = source_cidr
        self.source_port_range = source_port_range
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
            temp_model = main_models.DescribeQosPoliciesResponseBodyQosPoliciesQosPolicyDpiGroupIds()
            self.dpi_group_ids = temp_model.from_map(m.get('DpiGroupIds'))

        if m.get('DpiSignatureIds') is not None:
            temp_model = main_models.DescribeQosPoliciesResponseBodyQosPoliciesQosPolicyDpiSignatureIds()
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

        if m.get('SourceCidr') is not None:
            self.source_cidr = m.get('SourceCidr')

        if m.get('SourcePortRange') is not None:
            self.source_port_range = m.get('SourcePortRange')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeQosPoliciesResponseBodyQosPoliciesQosPolicyDpiSignatureIds(DaraModel):
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

class DescribeQosPoliciesResponseBodyQosPoliciesQosPolicyDpiGroupIds(DaraModel):
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

