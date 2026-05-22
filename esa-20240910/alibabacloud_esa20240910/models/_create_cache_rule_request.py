# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCacheRuleRequest(DaraModel):
    def __init__(
        self,
        additional_cacheable_ports: str = None,
        browser_cache_mode: str = None,
        browser_cache_ttl: str = None,
        bypass_cache: str = None,
        cache_deception_armor: str = None,
        cache_reserve_eligibility: str = None,
        check_presence_cookie: str = None,
        check_presence_header: str = None,
        edge_cache_mode: str = None,
        edge_cache_ttl: str = None,
        edge_status_code_cache_ttl: str = None,
        include_cookie: str = None,
        include_header: str = None,
        post_body_cache_key: str = None,
        post_body_size_limit: str = None,
        post_cache: str = None,
        query_string: str = None,
        query_string_mode: str = None,
        rule: str = None,
        rule_enable: str = None,
        rule_name: str = None,
        sequence: int = None,
        serve_stale: str = None,
        site_id: int = None,
        site_version: int = None,
        sort_query_string_for_cache: str = None,
        user_device_type: str = None,
        user_geo: str = None,
        user_language: str = None,
    ):
        self.additional_cacheable_ports = additional_cacheable_ports
        self.browser_cache_mode = browser_cache_mode
        self.browser_cache_ttl = browser_cache_ttl
        self.bypass_cache = bypass_cache
        self.cache_deception_armor = cache_deception_armor
        self.cache_reserve_eligibility = cache_reserve_eligibility
        self.check_presence_cookie = check_presence_cookie
        self.check_presence_header = check_presence_header
        self.edge_cache_mode = edge_cache_mode
        self.edge_cache_ttl = edge_cache_ttl
        self.edge_status_code_cache_ttl = edge_status_code_cache_ttl
        self.include_cookie = include_cookie
        self.include_header = include_header
        self.post_body_cache_key = post_body_cache_key
        self.post_body_size_limit = post_body_size_limit
        self.post_cache = post_cache
        self.query_string = query_string
        self.query_string_mode = query_string_mode
        self.rule = rule
        self.rule_enable = rule_enable
        self.rule_name = rule_name
        self.sequence = sequence
        self.serve_stale = serve_stale
        # This parameter is required.
        self.site_id = site_id
        self.site_version = site_version
        self.sort_query_string_for_cache = sort_query_string_for_cache
        self.user_device_type = user_device_type
        self.user_geo = user_geo
        self.user_language = user_language

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.additional_cacheable_ports is not None:
            result['AdditionalCacheablePorts'] = self.additional_cacheable_ports

        if self.browser_cache_mode is not None:
            result['BrowserCacheMode'] = self.browser_cache_mode

        if self.browser_cache_ttl is not None:
            result['BrowserCacheTtl'] = self.browser_cache_ttl

        if self.bypass_cache is not None:
            result['BypassCache'] = self.bypass_cache

        if self.cache_deception_armor is not None:
            result['CacheDeceptionArmor'] = self.cache_deception_armor

        if self.cache_reserve_eligibility is not None:
            result['CacheReserveEligibility'] = self.cache_reserve_eligibility

        if self.check_presence_cookie is not None:
            result['CheckPresenceCookie'] = self.check_presence_cookie

        if self.check_presence_header is not None:
            result['CheckPresenceHeader'] = self.check_presence_header

        if self.edge_cache_mode is not None:
            result['EdgeCacheMode'] = self.edge_cache_mode

        if self.edge_cache_ttl is not None:
            result['EdgeCacheTtl'] = self.edge_cache_ttl

        if self.edge_status_code_cache_ttl is not None:
            result['EdgeStatusCodeCacheTtl'] = self.edge_status_code_cache_ttl

        if self.include_cookie is not None:
            result['IncludeCookie'] = self.include_cookie

        if self.include_header is not None:
            result['IncludeHeader'] = self.include_header

        if self.post_body_cache_key is not None:
            result['PostBodyCacheKey'] = self.post_body_cache_key

        if self.post_body_size_limit is not None:
            result['PostBodySizeLimit'] = self.post_body_size_limit

        if self.post_cache is not None:
            result['PostCache'] = self.post_cache

        if self.query_string is not None:
            result['QueryString'] = self.query_string

        if self.query_string_mode is not None:
            result['QueryStringMode'] = self.query_string_mode

        if self.rule is not None:
            result['Rule'] = self.rule

        if self.rule_enable is not None:
            result['RuleEnable'] = self.rule_enable

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.sequence is not None:
            result['Sequence'] = self.sequence

        if self.serve_stale is not None:
            result['ServeStale'] = self.serve_stale

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.site_version is not None:
            result['SiteVersion'] = self.site_version

        if self.sort_query_string_for_cache is not None:
            result['SortQueryStringForCache'] = self.sort_query_string_for_cache

        if self.user_device_type is not None:
            result['UserDeviceType'] = self.user_device_type

        if self.user_geo is not None:
            result['UserGeo'] = self.user_geo

        if self.user_language is not None:
            result['UserLanguage'] = self.user_language

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdditionalCacheablePorts') is not None:
            self.additional_cacheable_ports = m.get('AdditionalCacheablePorts')

        if m.get('BrowserCacheMode') is not None:
            self.browser_cache_mode = m.get('BrowserCacheMode')

        if m.get('BrowserCacheTtl') is not None:
            self.browser_cache_ttl = m.get('BrowserCacheTtl')

        if m.get('BypassCache') is not None:
            self.bypass_cache = m.get('BypassCache')

        if m.get('CacheDeceptionArmor') is not None:
            self.cache_deception_armor = m.get('CacheDeceptionArmor')

        if m.get('CacheReserveEligibility') is not None:
            self.cache_reserve_eligibility = m.get('CacheReserveEligibility')

        if m.get('CheckPresenceCookie') is not None:
            self.check_presence_cookie = m.get('CheckPresenceCookie')

        if m.get('CheckPresenceHeader') is not None:
            self.check_presence_header = m.get('CheckPresenceHeader')

        if m.get('EdgeCacheMode') is not None:
            self.edge_cache_mode = m.get('EdgeCacheMode')

        if m.get('EdgeCacheTtl') is not None:
            self.edge_cache_ttl = m.get('EdgeCacheTtl')

        if m.get('EdgeStatusCodeCacheTtl') is not None:
            self.edge_status_code_cache_ttl = m.get('EdgeStatusCodeCacheTtl')

        if m.get('IncludeCookie') is not None:
            self.include_cookie = m.get('IncludeCookie')

        if m.get('IncludeHeader') is not None:
            self.include_header = m.get('IncludeHeader')

        if m.get('PostBodyCacheKey') is not None:
            self.post_body_cache_key = m.get('PostBodyCacheKey')

        if m.get('PostBodySizeLimit') is not None:
            self.post_body_size_limit = m.get('PostBodySizeLimit')

        if m.get('PostCache') is not None:
            self.post_cache = m.get('PostCache')

        if m.get('QueryString') is not None:
            self.query_string = m.get('QueryString')

        if m.get('QueryStringMode') is not None:
            self.query_string_mode = m.get('QueryStringMode')

        if m.get('Rule') is not None:
            self.rule = m.get('Rule')

        if m.get('RuleEnable') is not None:
            self.rule_enable = m.get('RuleEnable')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')

        if m.get('ServeStale') is not None:
            self.serve_stale = m.get('ServeStale')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')

        if m.get('SortQueryStringForCache') is not None:
            self.sort_query_string_for_cache = m.get('SortQueryStringForCache')

        if m.get('UserDeviceType') is not None:
            self.user_device_type = m.get('UserDeviceType')

        if m.get('UserGeo') is not None:
            self.user_geo = m.get('UserGeo')

        if m.get('UserLanguage') is not None:
            self.user_language = m.get('UserLanguage')

        return self

