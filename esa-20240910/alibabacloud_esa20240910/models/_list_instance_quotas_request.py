# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListInstanceQuotasRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        quota_names: str = None,
        site_id: int = None,
    ):
        # The plan ID, which can be obtained by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation.
        self.instance_id = instance_id
        # The quota names in the plan. Separate multiple names with commas (,). Valid values:
        # 
        # *   **waf:phase:http_anti_scan:actions**: the actions in WAF scan protection rules.
        # *   **waf:phase:http_bot:actions**: all actions in WAF bot management rules.
        # *   **waf:phase:http_bot:http_custom_cc_dev:characteristic:fields**: the statistical objects for the custom device-based throttling in WAF bot management rules.
        # *   **waf:phase:http_bot:http_custom_cc_ip:characteristic:fields**: the statistical objects for the custom IP address-based throttling in WAF bot management rules.
        # *   ****waf:phase:http_bot:match:symbols****: the match operators in WAF bot management rules.
        # *   **waf:phase:http_bot:http_custom_cc:characteristic:fields**: the statistical objects for the custom session-based throttling in WAF bot management rules.
        # *   **waf:phase:http_bot:match:fields**: the match fields in WAF bot management rules.
        # *   **waf:phase:http_whitelist:match:symbols**: the match operators in WAF whitelist rules.
        # *   **waf:phase:http_whitelist:match:fields**: the match fields in WAF whitelist rules.
        # *   **waf:phase:http_anti_scan:http_directory_traversal:characteristic:fields**: the statistical objects for directory traversal blocking in WAF scan protection rules.
        # *   **waf:phase:http_anti_scan:http_high_frequency:characteristic:fields**: the statistical objects for high-frequency scanning blocking in WAF scan protection rules.
        # *   **waf:phase:http_anti_scan:match:symbols**: the match operators in WAF scan protection rules.
        # *   **waf:phase:http_anti_scan:match:fields**: the match fields in WAF scan protection rules.
        # *   **waf:phase:http_managed:actions**: the actions in WAF managed rules.
        # *   **waf:phase:http_managed:group:reference:ids**: the referenced rule groups in WAF managed rules.
        # *   **waf:phase:http_ratelimit:actions**: the actions in WAF rate limiting rules.
        # *   **waf:phase:http_ratelimit:ttls**: the action durations in WAF rate limiting rules.
        # *   **waf:phase:http_ratelimit:intervals**: the statistical durations in WAF rate limiting rules.
        # *   **waf:phase:http_ratelimit:http_ratelimit:characteristic:fields**: the match characteristics in WAF rate limiting rules.
        # *   **waf:phase:http_ratelimit:match:symbols**: the match operators in WAF rate limiting rules.
        # *   **waf:phase:http_ratelimit:match:fields**: the match fields in WAF rate limiting rules.
        # *   **waf:phase:http_custom:actions**: the actions in custom WAF rules.
        # *   **waf:phase:http_custom:match:symbols**: the match operators in custom WAF rules.
        # *   **waf:phase:http_custom:match:fields**: the match fields in custom WAF rules.
        # *   **waiting_room|queuing_method**: the queuing method in Waiting Room.
        # *   **origin_rules|origin_scheme**: the origin protocol in origin rules.
        # *   **origin_rules|origin_sni**: the origin Server Name Indication (SNI) in origin rules.
        # *   **origin_rules|origin_host**: the origin host in origin rules.
        # *   **fourlayeracceleration**: TCP/UDP proxy.
        # *   **rtlog_service**: the availability to collect real-time logs.
        # *   **dashboard_traffic**: the value-added capability of traffic analytics.
        # *   **custom_name_server**: the availability to configure custom nameservers.
        # *   **waf:phase:http_bot:enable**: the availability to enable WAF bot management.
        # *   **waf:phase:http_whitelist:enable**: the availability to configure WAF whitelist rules.
        # *   **instantlog**: the availability to collect instant logs.
        # *   **waf:phase:http_anti_scan:enable**: the availability to enable WAF scan protection.
        # *   **waf:phase:http_managed:group:reference:enable**: the availability to configure reference rule groups in WAF managed rules.
        # *   **waf:phase:http_managed:enable**: the availability to configure WAF managed rules.
        # *   **waf:phase:http_ratelimit:on_hit:enable**: the availability to configure whether to apply rate limiting to all requests that hit the cache.
        # *   **ddos**: DDoS mitigation.
        # *   **waf:phase:http_ratelimit:enable**: the availability to configure WAF rate limiting.
        # *   **waf:phase:http_custom:enable**: the availability to configure custom WAF rules.
        # *   **waf:phase:all:page:reference:enable**: the availability to configure custom error pages.
        # *   **rules_support_regex**: the support for regular expressions in rules engine.
        # *   **waiting_room_event**: scheduled events in Waiting Room.
        # *   **waiting_room_rule**: the availability to allow requests to bypass the waiting room.
        # *   **waiting_room|json_response**: the availability to enable JSON response in Waiting Room.
        # *   **waiting_room|disable_session_renewal**: the availability to disable session renewal in Waiting Room.
        # *   **origin_rules|dns_record**: DNS records in origin rules.
        # *   **managed_transforms|add_client_geolocation_headers**: the availability to configure whether to add geolocation headers in transform rules.
        # *   **tiered_cache|regional_enable**: regional tiered cache.
        # *   **real_client_ip_header**: the availability to configure whether to add the real IP address of a client to the request header.
        # *   **data_timerange**: minute-level time range for data query.
        # *   **cache_rules|edge_cache_ttl**: POP cache TTL.
        # *   **cache_rules|browser_cache_ttl**: browser cache TTL.
        # *   **fourLayerRecordCount**: the maximum number of records of websites for which TCP/UDP acceleration is enabled.
        # *   **waitingroomRuleCount**: the maximum number of rules per waiting room.
        # *   **waitingroomEventCount**: the maximum number of events per waiting room.
        # *   **waitingroom_custom_pathhost**: the availability to configure the hostname and path in Waiting Room.
        # *   **er_routers**: Edge Routine routes.
        # *   **cache_rules|rule_quota**: the maximum number of cache rules.
        # *   **configuration_rules|rule_quota**: the maximum number of configuration rules.
        # *   **redirect_rules|rule_quota**: the redirect rules.
        # *   **compression_rules|rule_quota**: the maximum number of compression rules.
        # *   **origin_rules|rule_quota**: the maximum number of origin rules.
        # *   **waf:phase:http_bot:rulesets_per_instance:less_than_or_equal**: the maximum number of rulesets in WAF bot management per plan.
        # *   **waf:phase:http_whitelist:rules_per_instance:less_than_or_equal**: the maximum number of WAF whitelist rules per plan.
        # *   **rtlog_quota**: the maximum number of real-time log delivery tasks.
        # *   **waf:phase:http_anti_scan:rulesets_per_instance:less_than_or_equal**: the maximum number of rulesets in WAF scan protection per plan.
        # *   **ddos_instance**: the number of Anti-DDoS Proxy instances.
        # *   **waf:phase:http_ratelimit:rules_per_instance:less_than_or_equal**: the maximum number of WAF rate limiting rules.
        # *   **waf:phase:http_custom:rules_per_instance:less_than_or_equal**: the maximum number of custom WAF rules per plan.
        # *   **ruleNestedConditionalCount**: the number of nested layers in a rule.
        # *   **waiting_room_rule**: Waiting Room.
        # *   **transition_rule**: the maximum number of transform rules.
        # *   **customHttpCert**: the maximum number of custom certificates.
        # *   **free_cert**: the maximum number of free certificates.
        # *   **preload**: prefetch.
        # *   **refresh_cache_tag**: purge by cache tag.
        # *   **refresh_ignore_param**: purge by URL with specified parameters ignored.
        # *   **refresh_directory**: purge by directory.
        # *   **refresh_hostname**: purge by hostname.
        # *   **refresh_all**: purge all cache.
        # *   **refresh_file**: purge by URL.
        # *   **wildcard**: the maximum number of wildcard domains.
        # *   **recordCount**: the maximum number of Layer 7 records.
        # *   **siteCount**: the maximum number of websites that can be associated with the plan.
        # *   **https|rule_quota**: the maximum number of SSL/TLS rules.
        # 
        # This parameter is required.
        self.quota_names = quota_names
        # The website ID, which can be obtained by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation.
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.quota_names is not None:
            result['QuotaNames'] = self.quota_names

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('QuotaNames') is not None:
            self.quota_names = m.get('QuotaNames')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        return self

