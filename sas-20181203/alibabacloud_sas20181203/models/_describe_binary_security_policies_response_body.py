# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeBinarySecurityPoliciesResponseBody(DaraModel):
    def __init__(
        self,
        binary_security_policies: List[main_models.DescribeBinarySecurityPoliciesResponseBodyBinarySecurityPolicies] = None,
        page_info: main_models.DescribeBinarySecurityPoliciesResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # The information about security policies.
        self.binary_security_policies = binary_security_policies
        # The pagination information.
        self.page_info = page_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.binary_security_policies:
            for v1 in self.binary_security_policies:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BinarySecurityPolicies'] = []
        if self.binary_security_policies is not None:
            for k1 in self.binary_security_policies:
                result['BinarySecurityPolicies'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.binary_security_policies = []
        if m.get('BinarySecurityPolicies') is not None:
            for k1 in m.get('BinarySecurityPolicies'):
                temp_model = main_models.DescribeBinarySecurityPoliciesResponseBodyBinarySecurityPolicies()
                self.binary_security_policies.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribeBinarySecurityPoliciesResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeBinarySecurityPoliciesResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of entries returned on each page.
        self.count = count
        # The page number.
        self.current_page = current_page
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeBinarySecurityPoliciesResponseBodyBinarySecurityPolicies(DaraModel):
    def __init__(
        self,
        clusters: List[main_models.DescribeBinarySecurityPoliciesResponseBodyBinarySecurityPoliciesClusters] = None,
        name: str = None,
        policy: Dict[str, Any] = None,
        remark: str = None,
        status: str = None,
    ):
        # The information about clusters.
        self.clusters = clusters
        # The name of the policy.
        self.name = name
        # The content of the policy. The value is in the JSON format. A key supports the following values:
        # 
        # *   **policyMode**: the type of the policy. Default value: requireAttestor.
        # *   **requiredAttestors**: the required witnesses.
        self.policy = policy
        # The description.
        self.remark = remark
        # The status of the policy. Valid values:
        # 
        # *   **enabled**
        # *   **disabled**
        self.status = status

    def validate(self):
        if self.clusters:
            for v1 in self.clusters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Clusters'] = []
        if self.clusters is not None:
            for k1 in self.clusters:
                result['Clusters'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.clusters = []
        if m.get('Clusters') is not None:
            for k1 in m.get('Clusters'):
                temp_model = main_models.DescribeBinarySecurityPoliciesResponseBodyBinarySecurityPoliciesClusters()
                self.clusters.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeBinarySecurityPoliciesResponseBodyBinarySecurityPoliciesClusters(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        namespaces: List[str] = None,
    ):
        # The ID of the cluster.
        self.cluster_id = cluster_id
        # The namespaces.
        self.namespaces = namespaces

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.namespaces is not None:
            result['Namespaces'] = self.namespaces

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Namespaces') is not None:
            self.namespaces = m.get('Namespaces')

        return self

