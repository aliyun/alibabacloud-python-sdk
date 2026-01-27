# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class ListEnterpriseAcceleratePoliciesResponseBody(DaraModel):
    def __init__(
        self,
        policies: List[main_models.ListEnterpriseAcceleratePoliciesResponseBodyPolicies] = None,
        request_id: str = None,
        total: int = None,
    ):
        self.policies = policies
        self.request_id = request_id
        self.total = total

    def validate(self):
        if self.policies:
            for v1 in self.policies:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Policies'] = []
        if self.policies is not None:
            for k1 in self.policies:
                result['Policies'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.policies = []
        if m.get('Policies') is not None:
            for k1 in m.get('Policies'):
                temp_model = main_models.ListEnterpriseAcceleratePoliciesResponseBodyPolicies()
                self.policies.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListEnterpriseAcceleratePoliciesResponseBodyPolicies(DaraModel):
    def __init__(
        self,
        acceleration_type: str = None,
        description: str = None,
        eap_id: str = None,
        enabled: int = None,
        name: str = None,
        on_tls: int = None,
        priority: int = None,
        show_in_client: int = None,
        upstream_host: str = None,
        upstream_port: int = None,
        upstream_type: str = None,
        user_attribute_group: str = None,
    ):
        self.acceleration_type = acceleration_type
        self.description = description
        self.eap_id = eap_id
        self.enabled = enabled
        self.name = name
        self.on_tls = on_tls
        self.priority = priority
        self.show_in_client = show_in_client
        self.upstream_host = upstream_host
        self.upstream_port = upstream_port
        self.upstream_type = upstream_type
        self.user_attribute_group = user_attribute_group

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acceleration_type is not None:
            result['AccelerationType'] = self.acceleration_type

        if self.description is not None:
            result['Description'] = self.description

        if self.eap_id is not None:
            result['EapId'] = self.eap_id

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.name is not None:
            result['Name'] = self.name

        if self.on_tls is not None:
            result['OnTls'] = self.on_tls

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.show_in_client is not None:
            result['ShowInClient'] = self.show_in_client

        if self.upstream_host is not None:
            result['UpstreamHost'] = self.upstream_host

        if self.upstream_port is not None:
            result['UpstreamPort'] = self.upstream_port

        if self.upstream_type is not None:
            result['UpstreamType'] = self.upstream_type

        if self.user_attribute_group is not None:
            result['UserAttributeGroup'] = self.user_attribute_group

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccelerationType') is not None:
            self.acceleration_type = m.get('AccelerationType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EapId') is not None:
            self.eap_id = m.get('EapId')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OnTls') is not None:
            self.on_tls = m.get('OnTls')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ShowInClient') is not None:
            self.show_in_client = m.get('ShowInClient')

        if m.get('UpstreamHost') is not None:
            self.upstream_host = m.get('UpstreamHost')

        if m.get('UpstreamPort') is not None:
            self.upstream_port = m.get('UpstreamPort')

        if m.get('UpstreamType') is not None:
            self.upstream_type = m.get('UpstreamType')

        if m.get('UserAttributeGroup') is not None:
            self.user_attribute_group = m.get('UserAttributeGroup')

        return self

