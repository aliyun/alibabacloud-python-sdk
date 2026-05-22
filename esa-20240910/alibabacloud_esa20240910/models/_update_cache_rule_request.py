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
        # Enable caching on specified ports. Value range: 8880, 2052, 2082, 2086, 2095, 2053, 2083, 2087, 2096.
        self.additional_cacheable_ports = additional_cacheable_ports
        # Browser cache mode. Value range:
        # - no_cache: Do not cache.
        # - follow_origin: Follow origin cache policy.
        # - override_origin: Override origin cache policy.
        self.browser_cache_mode = browser_cache_mode
        # Browser cache expiration time, in seconds.
        self.browser_cache_ttl = browser_cache_ttl
        # Set bypass cache mode. Value range:
        # - cache_all: Cache all requests.
        # - bypass_all: Bypass cache for all requests.
        self.bypass_cache = bypass_cache
        # Cache deception defense. Used to defend against web cache deception attacks; only the cache content that passes the validation will be cached. Value range:
        # - on: Enable.
        # - off: Disable.
        self.cache_deception_armor = cache_deception_armor
        # Cache retention eligibility. Used to control whether user requests bypass the cache retention node when returning to the origin. Value range:
        # - bypass_cache_reserve: Requests bypass cache retention.
        # - eligible_for_cache_reserve: Eligible for cache retention.
        self.cache_reserve_eligibility = cache_reserve_eligibility
        # Check if the cookie exists when generating cache keys, and if it does, add the cookie name (case-insensitive) to the cache key. Supports multiple cookie names, separated by spaces.
        self.check_presence_cookie = check_presence_cookie
        # Check if the header exists when generating cache keys, and if it does, add the header name (case-insensitive) to the cache key. Supports multiple header names, separated by spaces.
        self.check_presence_header = check_presence_header
        # Configuration ID.
        # 
        # This parameter is required.
        self.config_id = config_id
        # Edge cache mode. Value range:
        # - follow_origin: Follow origin cache policy (if exists), otherwise use the default cache policy.
        # - no_cache: Do not cache.
        # - override_origin: Override origin cache policy.
        # - follow_origin_bypass: Follow origin cache policy (if exists), otherwise do not cache.
        self.edge_cache_mode = edge_cache_mode
        # Edge cache expiration time, in seconds.
        self.edge_cache_ttl = edge_cache_ttl
        # Status code cache expiration time, in seconds.
        self.edge_status_code_cache_ttl = edge_status_code_cache_ttl
        # Include the specified cookie names and their values when generating cache keys, supporting multiple values separated by spaces.
        self.include_cookie = include_cookie
        # Include the specified header names and their values when generating cache keys, supporting multiple values separated by spaces.
        self.include_header = include_header
        self.post_body_cache_key = post_body_cache_key
        self.post_body_size_limit = post_body_size_limit
        self.post_cache = post_cache
        # Query strings to be retained or excluded, supporting multiple values separated by spaces.
        self.query_string = query_string
        # The processing mode of query strings when generating cache keys. Values:
        # - ignore_all: Ignore all.
        # - exclude_query_string: Exclude specified query strings.
        # - reserve_all: Default, reserve all.
        # - include_query_string: Include specified query strings.
        self.query_string_mode = query_string_mode
        # Rule content, using conditional expressions to match user requests. This parameter is not required when adding a global configuration. There are two usage scenarios:
        # - Match all incoming requests: Set the value to true
        # - Match specific requests: Set the value to a custom expression, for example: (http.host eq \\"video.example.com\\")
        self.rule = rule
        # Rule switch. This parameter is not required when adding a global configuration. Value range:
        # - on: Enable.
        # - off: Disable.
        self.rule_enable = rule_enable
        # Rule name. This parameter is not required when adding a global configuration.
        self.rule_name = rule_name
        self.sequence = sequence
        # Serve stale cache. When enabled, the node can still use the expired cached files to respond to user requests even if the origin server is unavailable. Value range:
        # - on: Enable.
        # - off: Disable.
        self.serve_stale = serve_stale
        # Site ID, which can be obtained by calling the [ListSites](~~ListSites~~) interface.
        # 
        # This parameter is required.
        self.site_id = site_id
        # Query string sorting. Value range:
        # - on: Enable.
        # - off: Disable.
        self.sort_query_string_for_cache = sort_query_string_for_cache
        # When generating cache keys, include the client device type. Value range: 
        # - on: enabled. 
        # - off: disabled.
        self.user_device_type = user_device_type
        # Include the client\\"s geographical location when generating the cache key. Value range:
        # - on: Enable.
        # - off: Disable.
        self.user_geo = user_geo
        # Include the client\\"s language type when generating the cache key. Value range:
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

