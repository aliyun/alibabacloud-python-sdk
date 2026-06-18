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
        # - Specifies additional ports on which caching is enabled.
        # 
        # - Valid values: 8880, 2052, 2082, 2086, 2095, 2053, 2083, 2087, and 2096.
        # 
        # - You can specify multiple ports, separated by commas (,).
        self.additional_cacheable_ports = additional_cacheable_ports
        # The browser cache mode. Valid values:
        # 
        # - `no_cache`: Disables browser caching.
        # 
        # - `follow_origin`: Follows the origin server cache policy.
        # 
        # - `override_origin`: Overrides the origin server cache policy.
        self.browser_cache_mode = browser_cache_mode
        # The browser cache TTL, in seconds.
        self.browser_cache_ttl = browser_cache_ttl
        # The bypass cache mode. Valid values:
        # 
        # - `cache_all`: Caches all requests.
        # 
        # - `bypass_all`: Bypasses the cache for all requests.
        self.bypass_cache = bypass_cache
        # Specifies whether to enable cache deception defense. This feature helps defend against web cache deception attacks. When this feature is enabled, only content that passes validation is cached. Valid values:
        # 
        # - `on`: Enables the defense.
        # 
        # - `off`: Disables the defense.
        self.cache_deception_armor = cache_deception_armor
        # Specifies whether requests bypass cache reservation nodes during an origin fetch. Valid values:
        # 
        # - `bypass_cache_reserve`: The request bypasses cache reservation.
        # 
        # - `eligible_for_cache_reserve`: The request is eligible for cache reservation.
        self.cache_reserve_eligibility = cache_reserve_eligibility
        # Specifies the cookies to check for presence when generating a cache key. If a specified cookie is present in the request, its name (case-insensitive) is included in the cache key. To specify multiple cookies, separate their names with spaces. The cookie names can contain the following characters:
        # 
        # - Symbols: ! # $ % & \\" \\* + - . ^ _ | \\~
        # 
        # - Digits: 0-9
        # 
        # - Letters: a-z (lowercase)
        self.check_presence_cookie = check_presence_cookie
        # Specifies the headers to check for presence when generating a cache key. If a specified header is present in the request, its name (case-insensitive) is included in the cache key. To specify multiple headers, separate their names with spaces. The header names can contain the following characters:
        # 
        # - Symbols: ! # $ % & \\" \\* + - . ^ _ | \\~
        # 
        # - Digits: 0-9
        # 
        # - Letters: a-z (lowercase)
        self.check_presence_header = check_presence_header
        # The edge cache mode. Valid values:
        # 
        # - `follow_origin`: Follows the origin server cache policy if one exists; otherwise, uses the default cache policy.
        # 
        # - `no_cache`: Disables caching on the edge node.
        # 
        # - `override_origin`: Overrides the origin server cache policy.
        # 
        # - `follow_origin_bypass`: Follows the origin server cache policy if one exists; otherwise, the content is not cached.
        # 
        # - `follow_origin_override`: Follows the origin server cache policy if one exists; otherwise, uses a custom edge cache TTL.
        self.edge_cache_mode = edge_cache_mode
        # The edge cache TTL, in seconds.
        self.edge_cache_ttl = edge_cache_ttl
        # The status code cache TTL, in seconds.
        # 
        # - You can set the cache TTL for a specific status code. For example, `404=10` caches responses with a 404 status code for 10 seconds.
        # 
        # - You can set the cache TTL for a series of status codes, such as 4xx or 5xx. For example, `4xx=10` caches all responses that have a status code in the 4xx series for 10 seconds.
        # 
        # - You can specify multiple status code TTLs, separated by commas (,).
        self.edge_status_code_cache_ttl = edge_status_code_cache_ttl
        # The cookies to include in the cache key. Both the cookie names (case-insensitive) and their values are included. Separate multiple cookie names with spaces. The cookie names can contain the following characters:
        # 
        # - Symbols: ! # $ % & \\" \\* + - . ^ _ | \\~
        # 
        # - Digits: 0-9
        # 
        # - Letters: a-z (lowercase)
        self.include_cookie = include_cookie
        # The headers to include in the cache key. Both the header names (case-insensitive) and their values are included. Separate multiple header names with spaces. The header names can contain the following characters:
        # 
        # - Symbols: ! # $ % & \\" \\* + - . ^ _ | \\~
        # 
        # - Digits: 0-9
        # 
        # - Letters: a-z (lowercase)
        self.include_header = include_header
        # Specifies how to process the request body when generating a cache key for POST requests. The following modes are supported:
        # 
        # - `md5`: Calculates the MD5 hash of the request body and adds the hash value to the cache key.
        # 
        # - `ignore`: Ignores the request body when the cache key is generated.
        self.post_body_cache_key = post_body_cache_key
        # The size limit for the request body when using POST request caching, in KB. Supported values range from 1 to 8. If unspecified, the default is 8 KB.
        self.post_body_size_limit = post_body_size_limit
        # Specifies whether to enable POST request caching.
        self.post_cache = post_cache
        # The query strings to include in or exclude from the cache key. Separate multiple query strings with spaces.
        self.query_string = query_string
        # The mode for processing query strings when generating a cache key. Valid values:
        # 
        # - `ignore_all`: Ignores all query strings.
        # 
        # - `exclude_query_string`: Excludes specified query strings.
        # 
        # - `reserve_all`: Includes all query strings (the default).
        # 
        # - `include_query_string`: Includes only specified query strings.
        self.query_string_mode = query_string_mode
        # The content of the rule, which is a conditional expression used to match user requests. This parameter is not required for a global configuration.
        # 
        # - To match all requests, set the value to `true`.
        # 
        # - To match specific requests, set the value to a custom expression, such as `(http.host eq "video.example.com")`.
        self.rule = rule
        # Specifies whether to enable the rule. This parameter is not required for a global configuration. Valid values:
        # 
        # - `on`: Enables the rule.
        # 
        # - `off`: Disables the rule.
        self.rule_enable = rule_enable
        # The rule name. This parameter is not required for a global configuration.
        self.rule_name = rule_name
        # The execution order of the rule. A smaller number indicates a higher priority.
        self.sequence = sequence
        # Specifies whether to serve stale content. If enabled, an edge node can serve stale (expired) content when the origin server is unavailable. Valid values:
        # 
        # - `on`: Enables serving stale content.
        # 
        # - `off`: Disables serving stale content.
        self.serve_stale = serve_stale
        # The site ID. You can call the [ListSites](~~ListSites~~) operation to get this ID.
        # 
        # This parameter is required.
        self.site_id = site_id
        # The site configuration version. For sites with version management enabled, this parameter specifies the site version to which the configuration applies.
        self.site_version = site_version
        # Specifies whether to sort query strings. This feature is disabled by default. Valid values:
        # 
        # - `on`: Enables sorting.
        # 
        # - `off`: Disables sorting.
        self.sort_query_string_for_cache = sort_query_string_for_cache
        # Specifies whether to include the client device type in the cache key. Valid values:
        # 
        # - `on`: Includes the client device type.
        # 
        # - `off`: Does not include the client device type.
        self.user_device_type = user_device_type
        # Specifies whether to include the client\\"s geographic location in the cache key. Valid values:
        # 
        # - `on`: Includes the geographic location.
        # 
        # - `off`: Does not include the geographic location.
        self.user_geo = user_geo
        # Specifies whether to include the client\\"s language in the cache key. Valid values:
        # 
        # - `on`: Includes the language.
        # 
        # - `off`: Does not include the language.
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

