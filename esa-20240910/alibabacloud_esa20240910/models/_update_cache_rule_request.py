# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateCacheRuleRequest(DaraModel):
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
        sort_query_string_for_cache: str = None,
        user_device_type: str = None,
        user_geo: str = None,
        user_language: str = None,
    ):
        # - Enables caching on the specified ports.
        # 
        # - Valid values: `8880`, `2052`, `2082`, `2086`, `2095`, `2053`, `2083`, `2087`, `2096`
        # 
        # - Separate multiple ports with commas.
        self.additional_cacheable_ports = additional_cacheable_ports
        # The browser cache mode. Valid values:
        # 
        # - `no_cache`: Does not cache content in the browser.
        # 
        # - `follow_origin`: Follows the caching policy of the origin server.
        # 
        # - `override_origin`: Overrides the caching policy of the origin server.
        self.browser_cache_mode = browser_cache_mode
        # The browser cache TTL (Time to Live), in seconds.
        self.browser_cache_ttl = browser_cache_ttl
        # The cache bypass mode. Valid values:
        # 
        # - `cache_all`: Caches all requests.
        # 
        # - `bypass_all`: Bypasses the cache for all requests.
        self.bypass_cache = bypass_cache
        # Defends against Web Cache Deception attacks by caching only validated content. Valid values:
        # 
        # - `on`: Enables the feature.
        # 
        # - `off`: Disables the feature.
        self.cache_deception_armor = cache_deception_armor
        # Controls whether requests bypass the cache reserve node during an origin-pull. Valid values:
        # 
        # - `bypass_cache_reserve`: The request bypasses the cache reserve.
        # 
        # - `eligible_for_cache_reserve`: The request is eligible for cache reserve.
        self.cache_reserve_eligibility = cache_reserve_eligibility
        # The cookies to check for. If a specified cookie is present in the request, its name (case-insensitive) is added to the cache key. Separate multiple cookies with spaces. Cookie names can contain the following characters:
        # 
        # - Symbols: ! # $ % & \\" \\* + - . ^ _ | \\~
        # 
        # - Digits: 0-9
        # 
        # - Lowercase letters: a-z
        self.check_presence_cookie = check_presence_cookie
        # The headers to check for. If a specified header is present in the request, its name (case-insensitive) is added to the cache key. Separate multiple headers with spaces. Header names can contain the following characters:
        # 
        # - Symbols: ! # $ % & \\" \\* + - . ^ _ | \\~
        # 
        # - Digits: 0-9
        # 
        # - Lowercase letters: a-z
        self.check_presence_header = check_presence_header
        # The configuration ID.
        # 
        # This parameter is required.
        self.config_id = config_id
        # The cache mode for the edge node. Valid values:
        # 
        # - `follow_origin`: Follows the origin server\\"s caching policy. If the origin server has no policy, the default policy is used.
        # 
        # - `no_cache`: Does not cache content.
        # 
        # - `override_origin`: Overrides the caching policy of the origin server.
        # 
        # - `follow_origin_bypass`: Follows the caching policy of the origin server, if one exists. Otherwise, content is not cached.
        # 
        # - `follow_origin_override`: Follows the caching policy of the origin server, if one exists. Otherwise, a custom cache TTL is used.
        self.edge_cache_mode = edge_cache_mode
        # The edge node cache TTL (Time to Live), in seconds.
        self.edge_cache_ttl = edge_cache_ttl
        # The cache TTL for specific status codes, in seconds.
        # 
        # - You can set the cache TTL for a specific status code. For example, `404=10` caches responses with a 404 status code for 10 seconds.
        # 
        # - You can set the cache TTL for `4xx` and `5xx` status code ranges. For example, `4xx=10` caches all responses with a `4xx` status code for 10 seconds.
        # 
        # - Separate multiple status code settings with commas.
        self.edge_status_code_cache_ttl = edge_status_code_cache_ttl
        # The cookies to include in the cache key. Both the cookie names (case-insensitive) and their values are used. Separate multiple cookies with spaces. Cookie names can contain the following characters:
        # 
        # - Symbols: ! # $ % & \\" \\* + - . ^ _ | \\~
        # 
        # - Digits: 0-9
        # 
        # - Lowercase letters: a-z
        self.include_cookie = include_cookie
        # The headers to include in the cache key. Both the header names (case-insensitive) and their values are used. Separate multiple headers with spaces. Header names can contain the following characters:
        # 
        # - Symbols: ! # $ % & \\" \\* + - . ^ _ | \\~
        # 
        # - Digits: 0-9
        # 
        # - Lowercase letters: a-z
        self.include_header = include_header
        # Controls how the request body is used to generate the cache key for POST requests. Valid values:
        # 
        # - `md5`: Calculates the MD5 hash of the request body and includes the hash in the cache key.
        # 
        # - `ignore`: Ignores the request body when generating the cache key.
        self.post_body_cache_key = post_body_cache_key
        # The maximum size of a request body for POST caching, in KB. The value must be an integer from 1 to 8. If you leave this parameter empty, the default value of 8 KB is used.
        self.post_body_size_limit = post_body_size_limit
        # Controls whether to cache responses to POST requests.
        self.post_cache = post_cache
        # The query string parameters to include in or exclude from the cache key. Separate multiple parameters with spaces.
        self.query_string = query_string
        # Controls how query strings are used to generate a cache key. Valid values:
        # 
        # - `ignore_all`: Ignores all query strings.
        # 
        # - `exclude_query_string`: Removes specified query strings.
        # 
        # - `reserve_all`: Retains all query strings. This is the default value.
        # 
        # - `include_query_string`: Retains only specified query strings.
        self.query_string_mode = query_string_mode
        # A conditional expression that matches user requests. This parameter is optional for a global configuration. Two scenarios are supported:
        # 
        # - To match all incoming requests, set the value to `true`.
        # 
        # - To match specific requests, set the value to a custom expression, for example, `(http.host eq "video.example.com")`.
        self.rule = rule
        # Controls whether the rule is enabled. This parameter is optional for a global configuration. Valid values:
        # 
        # - `on`: Enables the rule.
        # 
        # - `off`: Disables the rule.
        self.rule_enable = rule_enable
        # The name of the rule. This parameter is optional for a global configuration.
        self.rule_name = rule_name
        # The execution priority of the rule. A smaller value indicates a higher priority.
        self.sequence = sequence
        # Controls whether to serve stale content. If enabled, an edge node can serve expired content from its cache if the origin server is unavailable. Valid values:
        # 
        # - `on`: Enables this feature.
        # 
        # - `off`: Disables this feature.
        self.serve_stale = serve_stale
        # The ID of the site. To get this ID, call the [ListSites](~~ListSites~~) operation.
        # 
        # This parameter is required.
        self.site_id = site_id
        # Controls whether to sort query string parameters when generating a cache key. Valid values:
        # 
        # - `on`: Enables sorting.
        # 
        # - `off`: Disables sorting.
        self.sort_query_string_for_cache = sort_query_string_for_cache
        # Controls whether to include the client device type in the cache key. Valid values:
        # 
        # - `on`: Enables this feature.
        # 
        # - `off`: Disables this feature.
        self.user_device_type = user_device_type
        # Controls whether to include the client\\"s geographic location in the cache key. Valid values:
        # 
        # - `on`: Enables this feature.
        # 
        # - `off`: Disables this feature.
        self.user_geo = user_geo
        # Controls whether to include the client\\"s language in the cache key. Valid values:
        # 
        # - `on`: Enables this feature.
        # 
        # - `off`: Disables this feature.
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

        if m.get('SortQueryStringForCache') is not None:
            self.sort_query_string_for_cache = m.get('SortQueryStringForCache')

        if m.get('UserDeviceType') is not None:
            self.user_device_type = m.get('UserDeviceType')

        if m.get('UserGeo') is not None:
            self.user_geo = m.get('UserGeo')

        if m.get('UserLanguage') is not None:
            self.user_language = m.get('UserLanguage')

        return self

