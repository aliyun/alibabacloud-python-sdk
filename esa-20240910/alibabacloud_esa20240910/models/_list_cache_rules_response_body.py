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
        # Response body configuration.
        self.configs = configs
        # Current page number.
        self.page_number = page_number
        # Page size.
        self.page_size = page_size
        # Request ID.
        self.request_id = request_id
        # Total number of records.
        self.total_count = total_count
        # Total number of pages.
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
        # Enable caching on specified ports. Value range: 8880, 2052, 2082, 2086, 2095, 2053, 2083, 2087, 2096.
        self.additional_cacheable_ports = additional_cacheable_ports
        # Browser cache mode. Possible values:
        # - no_cache: Do not cache.
        # - follow_origin: Follow origin cache policy.
        # - override_origin: Override origin cache policy.
        self.browser_cache_mode = browser_cache_mode
        # Browser cache expiration time, in seconds.
        self.browser_cache_ttl = browser_cache_ttl
        # Set bypass cache mode. Possible values:
        # - cache_all: Cache all requests.
        # - bypass_all: Bypass cache for all requests.
        self.bypass_cache = bypass_cache
        # Cache deception defense. Used to defend against web cache deception attacks; only verified cache content will be cached. Value range:
        # - on: Enabled.
        # - off: Disabled.
        self.cache_deception_armor = cache_deception_armor
        # Cache reserve eligibility. This is used to control whether user requests bypass the cache reserve node when returning to the origin. The value range is as follows:
        # - bypass_cache_reserve: Requests bypass the cache reserve.
        # - eligible_for_cache_reserve: Eligible for cache reserve.
        self.cache_reserve_eligibility = cache_reserve_eligibility
        # When generating the cache key, check if the cookie exists. If it does, add the cookie name (case-insensitive) to the cache key. Multiple cookie names are supported, separated by spaces.
        self.check_presence_cookie = check_presence_cookie
        # When generating the cache key, check if the header exists. If it does, add the header name (case-insensitive) to the cache key. Multiple header names are supported, separated by spaces.
        self.check_presence_header = check_presence_header
        # Configuration ID.
        self.config_id = config_id
        # Configuration type, which can be used to query global or rule-based configurations. Possible values:
        # - global: Query global configuration.
        # - rule: Query rule-based configuration.
        self.config_type = config_type
        # Edge cache mode. The value range is as follows:
        # - follow_origin: Follow the origin server\\"s cache policy (if it exists), otherwise use the default cache policy.
        # - no_cache: Do not cache.
        # - override_origin: Override the origin server\\"s cache policy.
        # - follow_origin_bypass: Follow the origin server\\"s cache policy (if it exists), otherwise do not cache.
        self.edge_cache_mode = edge_cache_mode
        # Edge cache expiration time, in seconds.
        self.edge_cache_ttl = edge_cache_ttl
        # Edge cache expiration time, in seconds.
        self.edge_status_code_cache_ttl = edge_status_code_cache_ttl
        # Include the specified cookie names and their values when generating the cache key. Multiple values are supported, separated by spaces.
        self.include_cookie = include_cookie
        # Include the specified header names and their values when generating the cache key. Multiple values are supported, separated by spaces.
        self.include_header = include_header
        self.post_body_cache_key = post_body_cache_key
        self.post_body_size_limit = post_body_size_limit
        self.post_cache = post_cache
        # The query strings to be reserved or excluded. Multiple values are supported, separated by spaces.
        self.query_string = query_string
        # The processing mode for query strings when generating the cache key. The value range is as follows:
        # - ignore_all: Ignore all query strings.
        # - exclude_query_string: Exclude specified query strings.
        # - reserve_all: Default, reserve all query strings.
        # - include_query_string: Include specified query strings.
        self.query_string_mode = query_string_mode
        # Rule content, using conditional expressions to match user requests. This parameter is not required when adding a global configuration. There are two usage scenarios:
        # - Match all incoming requests: Set the value to true
        # - Match specific requests: Set the value to a custom expression, e.g., (http.host eq \\"video.example.com\\")
        self.rule = rule
        # Rule switch. This parameter is not required when adding a global configuration. Possible values:
        # - on: Enabled.
        # - off: Disabled.
        self.rule_enable = rule_enable
        # Rule name. This parameter is not required when adding a global configuration.
        self.rule_name = rule_name
        # Rule execution order. The smaller the value, the higher the priority.
        self.sequence = sequence
        # Serve stale cache. When enabled, the node can still respond to user requests with expired cached files even when the origin server is unavailable. Value range:
        # - on: Enabled.
        # - off: Disabled.
        self.serve_stale = serve_stale
        # Site configuration version number. For sites with version management enabled, this parameter can specify the site version for which the configuration takes effect, defaulting to version 0.
        self.site_version = site_version
        # Query string sorting. The value range is as follows:
        # - on: Enable.
        # - off: Disable.
        self.sort_query_string_for_cache = sort_query_string_for_cache
        # Include the client device type when generating the cache key. The value range is as follows:
        # - on: Enable.
        # - off: Disable.
        self.user_device_type = user_device_type
        # Include the client\\"s geographic location when generating the cache key. The value range is as follows:
        # - on: Enable.
        # - off: Disable.
        self.user_geo = user_geo
        # Include the client\\"s language type when generating the cache key. The value range is as follows:
        # - on: Enable.
        # - off: Disable.
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

