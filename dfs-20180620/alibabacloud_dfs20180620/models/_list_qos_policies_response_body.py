# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dfs20180620 import models as main_models
from darabonba.model import DaraModel

class ListQosPoliciesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        qos_policies: List[main_models.ListQosPoliciesResponseBodyQosPolicies] = None,
        request_id: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.qos_policies = qos_policies
        self.request_id = request_id

    def validate(self):
        if self.qos_policies:
            for v1 in self.qos_policies:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['QosPolicies'] = []
        if self.qos_policies is not None:
            for k1 in self.qos_policies:
                result['QosPolicies'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.qos_policies = []
        if m.get('QosPolicies') is not None:
            for k1 in m.get('QosPolicies'):
                temp_model = main_models.ListQosPoliciesResponseBodyQosPolicies()
                self.qos_policies.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListQosPoliciesResponseBodyQosPolicies(DaraModel):
    def __init__(
        self,
        description: str = None,
        federation_id: str = None,
        file_system_id: str = None,
        flow_ids: str = None,
        max_ioband_width: int = None,
        max_iops: int = None,
        max_meta_qps: int = None,
        qos_policy_id: str = None,
        req_tags: str = None,
        zone_ids: str = None,
    ):
        self.description = description
        self.federation_id = federation_id
        self.file_system_id = file_system_id
        self.flow_ids = flow_ids
        self.max_ioband_width = max_ioband_width
        self.max_iops = max_iops
        self.max_meta_qps = max_meta_qps
        self.qos_policy_id = qos_policy_id
        self.req_tags = req_tags
        self.zone_ids = zone_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.federation_id is not None:
            result['FederationId'] = self.federation_id

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.flow_ids is not None:
            result['FlowIds'] = self.flow_ids

        if self.max_ioband_width is not None:
            result['MaxIOBandWidth'] = self.max_ioband_width

        if self.max_iops is not None:
            result['MaxIOps'] = self.max_iops

        if self.max_meta_qps is not None:
            result['MaxMetaQps'] = self.max_meta_qps

        if self.qos_policy_id is not None:
            result['QosPolicyId'] = self.qos_policy_id

        if self.req_tags is not None:
            result['ReqTags'] = self.req_tags

        if self.zone_ids is not None:
            result['ZoneIds'] = self.zone_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FederationId') is not None:
            self.federation_id = m.get('FederationId')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('FlowIds') is not None:
            self.flow_ids = m.get('FlowIds')

        if m.get('MaxIOBandWidth') is not None:
            self.max_ioband_width = m.get('MaxIOBandWidth')

        if m.get('MaxIOps') is not None:
            self.max_iops = m.get('MaxIOps')

        if m.get('MaxMetaQps') is not None:
            self.max_meta_qps = m.get('MaxMetaQps')

        if m.get('QosPolicyId') is not None:
            self.qos_policy_id = m.get('QosPolicyId')

        if m.get('ReqTags') is not None:
            self.req_tags = m.get('ReqTags')

        if m.get('ZoneIds') is not None:
            self.zone_ids = m.get('ZoneIds')

        return self

