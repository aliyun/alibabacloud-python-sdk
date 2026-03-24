# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cdn20180510 import models as main_models
from darabonba.model import DaraModel

class DescribeCdnWafDomainResponseBody(DaraModel):
    def __init__(
        self,
        out_put_domains: List[main_models.DescribeCdnWafDomainResponseBodyOutPutDomains] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information about the accelerated domain name.
        self.out_put_domains = out_put_domains
        # The ID of the request.
        self.request_id = request_id
        # The number of accelerated domain names.
        self.total_count = total_count

    def validate(self):
        if self.out_put_domains:
            for v1 in self.out_put_domains:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['OutPutDomains'] = []
        if self.out_put_domains is not None:
            for k1 in self.out_put_domains:
                result['OutPutDomains'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.out_put_domains = []
        if m.get('OutPutDomains') is not None:
            for k1 in m.get('OutPutDomains'):
                temp_model = main_models.DescribeCdnWafDomainResponseBodyOutPutDomains()
                self.out_put_domains.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeCdnWafDomainResponseBodyOutPutDomains(DaraModel):
    def __init__(
        self,
        acl_status: str = None,
        cc_status: str = None,
        domain: str = None,
        status: str = None,
        waf_status: str = None,
    ):
        # The status of the access control list (ACL) feature. Valid values:
        # 
        # *   **0**: disabled
        # *   **1**: enabled
        self.acl_status = acl_status
        # The status of protection against HTTP flood attacks. Valid values:
        # 
        # *   **0**: disabled
        # *   **1**: enabled
        self.cc_status = cc_status
        # The accelerated domain name.
        self.domain = domain
        # The WAF status of the domain name. Valid values:
        # 
        # *   **1**: The domain name is added to WAF or valid.
        # *   **10**: The domain name is being added to WAF.
        # *   **11**: The domain name failed to be added to WAF.
        self.status = status
        # The status of WAF. Valid values:
        # 
        # *   **0**: disabled
        # *   **1**: enabled
        self.waf_status = waf_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_status is not None:
            result['AclStatus'] = self.acl_status

        if self.cc_status is not None:
            result['CcStatus'] = self.cc_status

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.status is not None:
            result['Status'] = self.status

        if self.waf_status is not None:
            result['WafStatus'] = self.waf_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclStatus') is not None:
            self.acl_status = m.get('AclStatus')

        if m.get('CcStatus') is not None:
            self.cc_status = m.get('CcStatus')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('WafStatus') is not None:
            self.waf_status = m.get('WafStatus')

        return self

