# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeWebCacheConfigsResponseBody(DaraModel):
    def __init__(
        self,
        domain_cache_configs: List[main_models.DescribeWebCacheConfigsResponseBodyDomainCacheConfigs] = None,
        request_id: str = None,
    ):
        # An array that consists of Static Page Caching configurations.
        self.domain_cache_configs = domain_cache_configs
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.domain_cache_configs:
            for v1 in self.domain_cache_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DomainCacheConfigs'] = []
        if self.domain_cache_configs is not None:
            for k1 in self.domain_cache_configs:
                result['DomainCacheConfigs'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_cache_configs = []
        if m.get('DomainCacheConfigs') is not None:
            for k1 in m.get('DomainCacheConfigs'):
                temp_model = main_models.DescribeWebCacheConfigsResponseBodyDomainCacheConfigs()
                self.domain_cache_configs.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeWebCacheConfigsResponseBodyDomainCacheConfigs(DaraModel):
    def __init__(
        self,
        custom_rules: List[main_models.DescribeWebCacheConfigsResponseBodyDomainCacheConfigsCustomRules] = None,
        domain: str = None,
        enable: int = None,
        mode: str = None,
    ):
        # An array that consists of custom caching rules.
        self.custom_rules = custom_rules
        # The domain name of the website.
        self.domain = domain
        # The status of the Static Page Caching policy. Valid values:
        # 
        # *   **1**: enabled
        # *   **0**: disabled
        self.enable = enable
        # The cache mode. Valid values:
        # 
        # *   **standard**: The standard cache mode is used.
        # *   **aggressive**: The enhanced cache mode is used.
        # *   **bypass**: No data is cached.
        self.mode = mode

    def validate(self):
        if self.custom_rules:
            for v1 in self.custom_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CustomRules'] = []
        if self.custom_rules is not None:
            for k1 in self.custom_rules:
                result['CustomRules'].append(k1.to_map() if k1 else None)

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.mode is not None:
            result['Mode'] = self.mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_rules = []
        if m.get('CustomRules') is not None:
            for k1 in m.get('CustomRules'):
                temp_model = main_models.DescribeWebCacheConfigsResponseBodyDomainCacheConfigsCustomRules()
                self.custom_rules.append(temp_model.from_map(k1))

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        return self

class DescribeWebCacheConfigsResponseBodyDomainCacheConfigsCustomRules(DaraModel):
    def __init__(
        self,
        cache_ttl: int = None,
        mode: str = None,
        name: str = None,
        uri: str = None,
    ):
        # The expiration time of the page cache. Unit: seconds.
        self.cache_ttl = cache_ttl
        # The cache mode. Valid values:
        # 
        # *   **standard**: The standard cache mode is used.
        # *   **aggressive**: The enhanced cache mode is used.
        # *   **bypass**: No data is cached.
        self.mode = mode
        # The name of the rule.
        self.name = name
        # The path to the cached page.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cache_ttl is not None:
            result['CacheTtl'] = self.cache_ttl

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.name is not None:
            result['Name'] = self.name

        if self.uri is not None:
            result['Uri'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CacheTtl') is not None:
            self.cache_ttl = m.get('CacheTtl')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Uri') is not None:
            self.uri = m.get('Uri')

        return self

