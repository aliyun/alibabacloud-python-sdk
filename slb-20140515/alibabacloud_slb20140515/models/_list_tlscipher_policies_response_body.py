# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_slb20140515 import models as main_models
from darabonba.model import DaraModel

class ListTLSCipherPoliciesResponseBody(DaraModel):
    def __init__(
        self,
        is_truncated: bool = None,
        next_token: str = None,
        request_id: str = None,
        tlscipher_policies: List[main_models.ListTLSCipherPoliciesResponseBodyTLSCipherPolicies] = None,
        total_count: int = None,
    ):
        # Indicates whether the current page is the last page. Valid values:
        # 
        # *   **true**: The current page is the last page.
        # *   **false**: The current page is not the last page.
        self.is_truncated = is_truncated
        # The token that is used for the next query. Valid values:
        # 
        # *   If **NextToken** is empty, it indicates that no next query is to be sent.
        # *   If **NextToken** is not empty, the value indicates the token that is used for the next query.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The list of TLS policies.
        self.tlscipher_policies = tlscipher_policies
        # The total number of TLS policies returned.
        self.total_count = total_count

    def validate(self):
        if self.tlscipher_policies:
            for v1 in self.tlscipher_policies:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TLSCipherPolicies'] = []
        if self.tlscipher_policies is not None:
            for k1 in self.tlscipher_policies:
                result['TLSCipherPolicies'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.tlscipher_policies = []
        if m.get('TLSCipherPolicies') is not None:
            for k1 in m.get('TLSCipherPolicies'):
                temp_model = main_models.ListTLSCipherPoliciesResponseBodyTLSCipherPolicies()
                self.tlscipher_policies.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListTLSCipherPoliciesResponseBodyTLSCipherPolicies(DaraModel):
    def __init__(
        self,
        ciphers: List[str] = None,
        create_time: int = None,
        instance_id: str = None,
        name: str = None,
        relate_listeners: List[main_models.ListTLSCipherPoliciesResponseBodyTLSCipherPoliciesRelateListeners] = None,
        status: str = None,
        tlsversions: List[str] = None,
    ):
        # The cipher suites supported by the TLS version.
        # 
        # TLS 1.0 and TLS 1.1 support the following cipher suites:
        # 
        # *   ECDHE-ECDSA-AES128-SHA
        # *   ECDHE-ECDSA-AES256-SHA
        # *   ECDHE-RSA-AES128-SHA
        # *   ECDHE-RSA-AES256-SHA
        # *   AES128-SHA AES256-SHA
        # *   DES-CBC3-SHA
        # 
        # TLS 1.2 supports the following cipher suites:
        # 
        # *   ECDHE-ECDSA-AES128-SHA
        # *   ECDHE-ECDSA-AES256-SHA
        # *   ECDHE-RSA-AES128-SHA
        # *   ECDHE-RSA-AES256-SHA
        # *   AES128-SHA AES256-SHA
        # *   DES-CBC3-SHA
        # *   ECDHE-ECDSA-AES128-GCM-SHA256
        # *   ECDHE-ECDSA-AES256-GCM-SHA384
        # *   ECDHE-ECDSA-AES128-SHA256
        # *   ECDHE-ECDSA-AES256-SHA384
        # *   ECDHE-RSA-AES128-GCM-SHA256
        # *   ECDHE-RSA-AES256-GCM-SHA384
        # *   ECDHE-RSA-AES128-SHA256
        # *   ECDHE-RSA-AES256-SHA384
        # *   AES128-GCM-SHA256
        # *   AES256-GCM-SHA384
        # *   AES128-SHA256 AES256-SHA256
        # 
        # TLS 1.3 supports the following cipher suites:
        # 
        # *   TLS_AES_128_GCM_SHA256
        # *   TLS_AES_256_GCM_SHA384
        # *   TLS_CHACHA20_POLY1305_SHA256
        # *   TLS_AES_128_CCM_SHA256
        # *   TLS_AES_128_CCM_8_SHA256
        self.ciphers = ciphers
        # The timestamp generated when the TLS policy is created.
        self.create_time = create_time
        # The ID of the TLS policy.
        self.instance_id = instance_id
        # The name of the TLS policy.
        self.name = name
        # The list of associated listeners.
        self.relate_listeners = relate_listeners
        # The status of the TLS policy. Valid values:
        # 
        # *   **configuring**: The TLS policy is being configured.
        # *   **normal**: The TLS policy works as expected.
        self.status = status
        # The version of the TLS protocol.
        self.tlsversions = tlsversions

    def validate(self):
        if self.relate_listeners:
            for v1 in self.relate_listeners:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ciphers is not None:
            result['Ciphers'] = self.ciphers

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        result['RelateListeners'] = []
        if self.relate_listeners is not None:
            for k1 in self.relate_listeners:
                result['RelateListeners'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        if self.tlsversions is not None:
            result['TLSVersions'] = self.tlsversions

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ciphers') is not None:
            self.ciphers = m.get('Ciphers')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.relate_listeners = []
        if m.get('RelateListeners') is not None:
            for k1 in m.get('RelateListeners'):
                temp_model = main_models.ListTLSCipherPoliciesResponseBodyTLSCipherPoliciesRelateListeners()
                self.relate_listeners.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TLSVersions') is not None:
            self.tlsversions = m.get('TLSVersions')

        return self

class ListTLSCipherPoliciesResponseBodyTLSCipherPoliciesRelateListeners(DaraModel):
    def __init__(
        self,
        load_balancer_id: str = None,
        port: int = None,
        protocol: str = None,
    ):
        # The ID of the CLB instance.
        self.load_balancer_id = load_balancer_id
        # The listening port. Valid values: **1** to **65535**.
        self.port = port
        # The listening protocol. Valid values:
        # 
        # *   **TCP**
        # *   **UDP**
        # *   **HTTP**
        # *   **HTTPS**
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        if self.port is not None:
            result['Port'] = self.port

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        return self

