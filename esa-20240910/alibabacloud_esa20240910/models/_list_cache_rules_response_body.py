# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListCacheRulesResponseBody(DaraModel):
    def __init__(
        self,
        configs: List[main_models.ListCacheRulesResponseBodyConfigs] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        total_page: int = None,
    ):
        # The configuration list in the response body.
        self.configs = configs
        # The current page number, which is the same as the PageNumber request parameter.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of records.
        self.total_count = total_count
        # The total number of pages.
        self.total_page = total_page

    def validate(self):
        if self.configs:
            for v1 in self.configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Configs'] = []
        if self.configs is not None:
            for k1 in self.configs:
                result['Configs'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.configs = []
        if m.get('Configs') is not None:
            for k1 in m.get('Configs'):
                temp_model = main_models.ListCacheRulesResponseBodyConfigs()
                self.configs.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

class ListCacheRulesResponseBodyConfigs(DaraModel):
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
        config_id: int = None,
        config_type: str = None,
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
        site_version: int = None,
        sort_query_string_for_cache: str = None,
        user_device_type: str = None,
        user_geo: str = None,
        user_language: str = None,
    ):
        # - Enables caching on specified ports.
        # - Valid values: 8880, 2052, 2082, 2086, 2095, 2053, 2083, 2087, and 2096.
        # - Multiple ports are separated by commas (,).
        self.additional_cacheable_ports = additional_cacheable_ports
        # The browser cache mode. Valid values:
        # - no_cache: does not cache.
        # - follow_origin: follows the origin cache policy.
        # - override_origin: overrides the origin cache policy.
        self.browser_cache_mode = browser_cache_mode
        # The browser cache expiration time, in seconds.
        self.browser_cache_ttl = browser_cache_ttl
        # The bypass cache mode. Valid values:
        # - cache_all: caches all requests.
        # - bypass_all: bypasses cache for all requests.
        self.bypass_cache = bypass_cache
        # The cache deception armor. Protects against web cache deception attacks by caching only content that passes validation. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.cache_deception_armor = cache_deception_armor
        # The cache reserve eligibility. Controls whether user requests bypass the cache reserve node during back-to-origin. Valid values:
        # - bypass_cache_reserve: requests bypass cache reserve.
        # - eligible_for_cache_reserve: requests are eligible for cache reserve.
        self.cache_reserve_eligibility = cache_reserve_eligibility
        # When generating cache keys, checks whether the specified cookies exist. If a cookie exists, its name (case-insensitive) is added to the cache key. Multiple cookie names are separated by spaces. Cookie names support the following character types:
        # - Symbols: ! # $ % & \\" * + - . ^ _ ` | ~
        # - Digits: 0-9
        # - Letters: lowercase a-z.
        self.check_presence_cookie = check_presence_cookie
        # When generating cache keys, checks whether the specified headers exist. If a header exists, its name (case-insensitive) is added to the cache key. Multiple header names are separated by spaces. Header names support the following character types:
        # - Symbols: ! # $ % & \\" * + - . ^ _ ` | ~
        # - Digits: 0-9
        # - Letters: lowercase a-z.
        self.check_presence_header = check_presence_header
        # The configuration ID.
        self.config_id = config_id
        # The configuration type. You can use this parameter to query global or rule configurations. Valid values:
        # 
        # - global: global configuration.
        # - rule: rule configuration.
        self.config_type = config_type
        # The edge cache mode. Valid values:
        # - follow_origin: follows the origin cache policy if present. Otherwise, uses the default cache policy.
        # - no_cache: does not cache.
        # - override_origin: overrides the origin cache policy.
        # - follow_origin_bypass: follows the origin cache policy if present. Otherwise, does not cache.
        # - follow_origin_override: follows the origin cache policy if present. Otherwise, uses a custom cache TTL.
        self.edge_cache_mode = edge_cache_mode
        # The edge cache expiration time, in seconds.
        self.edge_cache_ttl = edge_cache_ttl
        # The status code cache expiration time, in seconds.
        # - You can set the cache expiration time for specific status codes. For example, 404=10 indicates that the 404 status code is cached for 10 seconds.
        # - You can set the cache expiration time for 4xx or 5xx series status codes. For example, 4xx=10 indicates that all 4xx status codes are cached for 10 seconds.
        # - You can set the cache expiration time for multiple status codes. Separate multiple status codes with commas (,).
        self.edge_status_code_cache_ttl = edge_status_code_cache_ttl
        # The specified cookie names (case-insensitive) and their values to include when generating cache keys. Multiple values are separated by spaces. Cookie names support the following character types:
        # - Symbols: ! # $ % & \\" * + - . ^ _ ` | ~
        # - Digits: 0-9
        # - Letters: lowercase a-z.
        self.include_cookie = include_cookie
        # The specified header names (case-insensitive) and their values to include when generating cache keys. Multiple values are separated by spaces. Header names support the following character types:
        # - Symbols: ! # $ % & \\" * + - . ^ _ ` | ~
        # - Digits: 0-9
        # - Letters: lowercase a-z.
        self.include_header = include_header
        # The cache key handling mode for POST caching. The following two modes are supported:
        # - md5: calculates the MD5 hash of the body content and adds the MD5 value to the cache key.
        # - ignore: ignores the body content in the cache key.
        self.post_body_cache_key = post_body_cache_key
        # The body size limit for POST caching. The value is a number in KB. Valid values: 1 to 8. If this parameter is left empty, the default value of 8 KB takes effect.
        self.post_body_size_limit = post_body_size_limit
        # Specifies whether to enable POST caching.
        self.post_cache = post_cache
        # The query strings to retain or remove when generating cache keys. Multiple values are separated by spaces.
        self.query_string = query_string
        # The query string handling mode when generating cache keys. Valid values:
        # - ignore_all: ignores all query strings.
        # - exclude_query_string: removes specified query strings.
        # - reserve_all: retains all query strings. This is the default value.
        # - include_query_string: retains specified query strings.
        self.query_string_mode = query_string_mode
        # The rule content, which uses conditional expressions to match user requests. You do not need to set this parameter when you add a global configuration. Two scenarios are supported:
        # - Match all incoming requests: set the value to true.
        # - Match specified requests: set the value to a custom expression, such as (http.host eq \\"video.example.com\\").
        self.rule = rule
        # The rule switch. You do not need to set this parameter when you add a global configuration. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.rule_enable = rule_enable
        # The rule name. You do not need to set this parameter when you add a global configuration.
        self.rule_name = rule_name
        # The rule execution order. A smaller value indicates a higher priority.
        self.sequence = sequence
        # Specifies whether to serve stale cache. When enabled, edge nodes can respond to user requests with cached expired files when the origin server is unavailable. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.serve_stale = serve_stale
        # The version number of the site configuration. For sites with configuration version management enabled, you can use this parameter to specify the site version for which the configuration takes effect. Default value: 0.
        self.site_version = site_version
        # Specifies whether to sort query strings. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.sort_query_string_for_cache = sort_query_string_for_cache
        # Specifies whether to include the type of the client when generating cache keys. Valid values:
        # - on: enabled.
        # - off: shutdown.
        self.user_device_type = user_device_type
        # Specifies whether to include the client geographic location when generating cache keys. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.user_geo = user_geo
        # Specifies whether to include the client language type when generating cache keys. Valid values:
        # - on: enabled.
        # - off: disabled.
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

        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.config_type is not None:
            result['ConfigType'] = self.config_type

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

        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')

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

