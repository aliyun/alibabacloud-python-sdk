# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCacheRuleResponseBody(DaraModel):
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
        request_id: str = None,
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
        # - Additional ports on which caching is enabled.
        # 
        # - Valid values: `8880`, `2052`, `2082`, `2086`, `2095`, `2053`, `2083`, `2087`, `2096`.
        # 
        # - Separate multiple ports with commas.
        self.additional_cacheable_ports = additional_cacheable_ports
        # The browser cache mode. Valid values:
        # 
        # - `no_cache`: Does not cache content.
        # 
        # - `follow_origin`: Follows the origin cache policy.
        # 
        # - `override_origin`: Overrides the origin cache policy.
        self.browser_cache_mode = browser_cache_mode
        # The browser cache TTL, in seconds.
        self.browser_cache_ttl = browser_cache_ttl
        # Specifies whether to cache requests or bypass the cache. Valid values:
        # 
        # - `cache_all`: Caches all requests.
        # 
        # - `bypass_all`: Bypasses the cache for all requests.
        self.bypass_cache = bypass_cache
        # Specifies whether to enable Cache Deception Armor. This feature helps mitigate web cache deception attacks by ensuring that only validated content is cached. Valid values:
        # 
        # - `on`: Enabled.
        # 
        # - `off`: Disabled.
        self.cache_deception_armor = cache_deception_armor
        # The eligibility for cache reserve. This controls whether a request bypasses the cache reserve node during an origin fetch. Valid values:
        # 
        # - `bypass_cache_reserve`: The request bypasses the cache reserve.
        # 
        # - `eligible_for_cache_reserve`: The request is eligible for cache reserve.
        self.cache_reserve_eligibility = cache_reserve_eligibility
        # Specifies cookies whose presence is checked when generating a cache key. If a specified cookie exists in the request, its name (case-insensitive) is added to the cache key. Separate multiple cookie names with spaces. Cookie names can contain the following characters:
        # 
        # - Symbols: ! # $ % & \\" \\* + - . ^ _ | \\~
        # 
        # - Digits: 0-9
        # 
        # - Letters: lowercase English letters a-z
        self.check_presence_cookie = check_presence_cookie
        # Specifies headers whose presence is checked when generating a cache key. If a specified header exists in the request, its name (case-insensitive) is added to the cache key. Separate multiple header names with spaces. Header names can contain the following characters:
        # 
        # - Symbols: ! # $ % & \\" \\* + - . ^ _ | \\~
        # 
        # - Digits: 0-9
        # 
        # - Letters: lowercase English letters a-z
        self.check_presence_header = check_presence_header
        # The configuration ID.
        self.config_id = config_id
        # Indicates whether the response contains a global or a rule configuration. Valid values:
        # 
        # - `global`: A global configuration.
        # 
        # - `rule`: A rule configuration.
        self.config_type = config_type
        # The edge cache mode. Valid values:
        # 
        # - `follow_origin`: Uses the origin server\\"s cache policy. If none is provided, the default policy applies.
        # 
        # - `no_cache`: Does not cache content.
        # 
        # - `override_origin`: Overrides the origin cache policy.
        # 
        # - `follow_origin_bypass`: Uses the origin server\\"s cache policy. If none is provided, content is not cached.
        # 
        # - `follow_origin_override`: Uses the origin server\\"s cache policy. If none is provided, a custom cache TTL applies.
        self.edge_cache_mode = edge_cache_mode
        # The edge cache TTL, in seconds.
        self.edge_cache_ttl = edge_cache_ttl
        # The status code cache TTL, in seconds.
        # 
        # - Set the cache TTL for a specific status code. For example, `404=10` specifies that responses with a 404 status code are cached for 10 seconds.
        # 
        # - Set the cache TTL for status code classes, such as 4xx and 5xx. For example, `4xx=10` specifies that all responses with a 4xx status code are cached for 10 seconds.
        # 
        # - Separate multiple entries with commas.
        self.edge_status_code_cache_ttl = edge_status_code_cache_ttl
        # Specifies the cookies to include in the cache key. Both the cookie names (case-insensitive) and their values are added to the key. Separate multiple cookie names with spaces. Cookie names can contain the following characters:
        # 
        # - Symbols: ! # $ % & \\" \\* + - . ^ _ | \\~
        # 
        # - Digits: 0-9
        # 
        # - Letters: lowercase English letters a-z
        self.include_cookie = include_cookie
        # Specifies the headers to include in the cache key. Both the header names (case-insensitive) and their values are added to the key. Separate multiple header names with spaces. Header names can contain the following characters:
        # 
        # - Symbols: ! # $ % & \\" \\* + - . ^ _ | \\~
        # 
        # - Digits: 0-9
        # 
        # - Letters: lowercase English letters a-z
        self.include_header = include_header
        # The mode for handling the body content when generating a cache key for POST requests. Valid values:
        # 
        # - `md5`: Calculates the MD5 hash of the body content and adds the hash to the cache key.
        # 
        # - `ignore`: Ignores the body content in the cache key.
        self.post_body_cache_key = post_body_cache_key
        # The size limit (in KB) of the body content for POST caching. The value is an integer from 1 to 8. A null or empty value defaults to 8 KB.
        self.post_body_size_limit = post_body_size_limit
        # Specifies whether to enable the POST cache feature.
        self.post_cache = post_cache
        # Specifies the query strings to include in or exclude from the cache key. Separate multiple query strings with spaces.
        self.query_string = query_string
        # The mode for handling query strings when generating a cache key. Valid values:
        # 
        # - `ignore_all`: Ignores all query strings.
        # 
        # - `exclude_query_string`: Excludes specified query strings.
        # 
        # - `reserve_all`: Retains all query strings. This is the default value.
        # 
        # - `include_query_string`: Includes specified query strings.
        self.query_string_mode = query_string_mode
        # The request ID.
        self.request_id = request_id
        # The rule content, which is a conditional expression used to match user requests. This parameter applies only to rule configurations.
        # 
        # - To match all incoming requests, use `true`.
        # 
        # - To match specific requests, use a custom expression, such as `(http.host eq "video.example.com")`.
        self.rule = rule
        # Specifies whether the rule is enabled. This parameter applies only to rule configurations. Valid values:
        # 
        # - `on`: Enabled.
        # 
        # - `off`: Disabled.
        self.rule_enable = rule_enable
        # The name of the rule. This parameter applies only to rule configurations.
        self.rule_name = rule_name
        # The rule execution order. A smaller value indicates a higher priority.
        self.sequence = sequence
        # Specifies whether to serve stale content. If enabled, edge nodes serve stale (expired) content from the cache when the origin server is unavailable. Valid values:
        # 
        # - `on`: Enabled.
        # 
        # - `off`: Disabled.
        self.serve_stale = serve_stale
        # The version number of the site configuration. For sites with version management enabled, this indicates the configuration version. The default is 0.
        self.site_version = site_version
        # Specifies whether to sort query strings before generating the cache key. Valid values:
        # 
        # - `on`: Enabled.
        # 
        # - `off`: Disabled.
        self.sort_query_string_for_cache = sort_query_string_for_cache
        # Specifies whether to include the client\\"s device type in the cache key. Valid values:
        # 
        # - `on`: Enabled.
        # 
        # - `off`: Disabled.
        self.user_device_type = user_device_type
        # Specifies whether to include the client\\"s geographic location in the cache key. Valid values:
        # 
        # - `on`: Enabled.
        # 
        # - `off`: Disabled.
        self.user_geo = user_geo
        # Specifies whether to include the client\\"s language in the cache key. Valid values:
        # 
        # - `on`: Enabled.
        # 
        # - `off`: Disabled.
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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

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

