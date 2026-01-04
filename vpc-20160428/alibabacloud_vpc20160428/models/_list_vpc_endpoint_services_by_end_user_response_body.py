# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class ListVpcEndpointServicesByEndUserResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        services: List[main_models.ListVpcEndpointServicesByEndUserResponseBodyServices] = None,
        total_count: str = None,
    ):
        # The number of entries returned per page.
        self.max_results = max_results
        # The token that is used for the next query. Valid values:
        # 
        # *   If no value is returned for **NextToken**, no next queries are sent.
        # *   If **NextToken** is returned, the value is the token that is used for the next query.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The list of entries returned.
        self.services = services
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.services:
            for v1 in self.services:
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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Services'] = []
        if self.services is not None:
            for k1 in self.services:
                result['Services'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.services = []
        if m.get('Services') is not None:
            for k1 in m.get('Services'):
                temp_model = main_models.ListVpcEndpointServicesByEndUserResponseBodyServices()
                self.services.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListVpcEndpointServicesByEndUserResponseBodyServices(DaraModel):
    def __init__(
        self,
        default_policy_document: str = None,
        service_domain: str = None,
        service_id: str = None,
        service_name: str = None,
        support_policy: bool = None,
    ):
        # The default access policy.
        self.default_policy_document = default_policy_document
        # The domain name of the cloud service to which the endpoint service belongs.
        self.service_domain = service_domain
        # The ID of the endpoint service.
        self.service_id = service_id
        # The name of the endpoint service.
        self.service_name = service_name
        # Indicate whether the endpoint service supports the access policy. Valid values:
        # 
        # *   **false**
        # *   **true**
        self.support_policy = support_policy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_policy_document is not None:
            result['DefaultPolicyDocument'] = self.default_policy_document

        if self.service_domain is not None:
            result['ServiceDomain'] = self.service_domain

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.support_policy is not None:
            result['SupportPolicy'] = self.support_policy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultPolicyDocument') is not None:
            self.default_policy_document = m.get('DefaultPolicyDocument')

        if m.get('ServiceDomain') is not None:
            self.service_domain = m.get('ServiceDomain')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('SupportPolicy') is not None:
            self.support_policy = m.get('SupportPolicy')

        return self

