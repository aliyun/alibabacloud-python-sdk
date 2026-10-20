# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetUserMaxPlanQuotaRequest(DaraModel):
    def __init__(
        self,
        quota_name: str = None,
    ):
        # The name of the plan quota. Valid values:
        # 
        # - **waf:phase:http_anti_scan:actions**: Actions for WAF scan protection.
        # - **waf:phase:http_bot:actions**: All actions for WAF bot management.
        # - **waf:phase:http_bot:http_custom_cc_dev:characteristic:fields**: Statistical objects for custom device rate limiting in WAF bot management.
        # - **waf:phase:http_bot:http_custom_cc_ip:characteristic:fields**: Statistical objects for custom IP rate limiting in WAF bot management.
        # - **waf:phase:http_bot:match:symbols**: Match symbols for WAF bot management.
        # - **waf:phase:http_bot:http_custom_cc:characteristic:fields**: Statistical objects for custom session rate limiting in WAF bot management.
        # - **waf:phase:http_bot:match:fields**: Match fields for WAF bot management.
        # - **waf:phase:http_whitelist:match:symbols**: Match symbols for the WAF whitelist.
        # - **waf:phase:http_whitelist:match:fields**: Match fields for the WAF whitelist.
        # - **waf:phase:http_anti_scan:http_directory_traversal:characteristic:fields**: Statistical objects for folder traverse blocking in WAF scan protection.
        # - **waf:phase:http_anti_scan:http_high_frequency:characteristic:fields**: Statistical objects for high-frequency scan blocking in WAF scan protection.
        # - **waf:phase:http_anti_scan:match:symbols**: Match symbols for WAF scan protection.
        # - **waf:phase:http_anti_scan:match:fields**: Match fields for WAF scan protection.
        # - **waf:phase:http_managed:actions**: Actions for WAF managed rules.
        # - **waf:phase:http_managed:group:reference:ids**: Referenced rule groups for WAF managed rules.
        # - **waf:phase:http_ratelimit:actions**: Actions for WAF rate limiting.
        # - **waf:phase:http_ratelimit:ttls**: Durations for WAF rate limiting.
        # - **waf:phase:http_ratelimit:intervals**: Statistical durations for WAF rate limiting.
        # - **waf:phase:http_ratelimit:http_ratelimit:characteristic:fields**: Match features for control type rules in WAF rate limiting.
        # - **waf:phase:http_ratelimit:match:symbols**: Match symbols for the WAF rate limiting rule phase.
        # - **waf:phase:http_ratelimit:match:fields**: Match fields for the WAF rate limiting rule phase.
        # - **waf:phase:http_custom:actions**: Actions for the WAF custom rule phase.
        # - **waf:phase:http_custom:match:symbols**: Match symbols for the WAF custom rule phase.
        # - **waf:phase:http_custom:match:fields**: Match fields for the WAF custom rule phase.
        # - **waiting_room|queuing_method**: Queuing method for the waiting room.
        # - **origin_rules|origin_scheme**: Back-to-origin protocol for back-to-origin rules.
        # - **origin_rules|origin_sni**: Back-to-origin SNI for back-to-origin rules.
        # - **origin_rules|origin_host**: Back-to-origin host for back-to-origin rules.
        # - **fourlayeracceleration**: Layer 4 acceleration.
        # - **rtlog_service**: Real-time log feature switch.
        # - **dashboard_traffic**: Value-added capability for network traffic analysis.
        # - **custom_name_server**: Custom NS name.
        # - **waf:phase:http_bot:enable**: WAF bot management switch.
        # - **waf:phase:http_whitelist:enable**: WAF whitelist switch.
        # - **instantlog**: Whether instant logs are active.
        # - **waf:phase:http_anti_scan:enable**: WAF scan protection switch.
        # - **waf:phase:http_managed:group:reference:enable**: Switch for configuring referenced rule groups in WAF managed rules.
        # - **waf:phase:http_managed:enable**: WAF managed rules switch.
        # - **waf:phase:http_ratelimit:on_hit:enable**: Switch for applying WAF rate limiting to cached requests.
        # - **ddos**: DDoS instance.
        # - **waf:phase:http_ratelimit:enable**: Switch for the WAF rate limiting rule phase.
        # - **waf:phase:http_custom:enable**: Switch for the WAF custom rule phase.
        # - **waf:phase:all:page:reference:enable**: WAF custom response page switch.
        # - **rules_support_regex**: Whether the rule DPI engine supports regular expressions.
        # - **waiting_room_event**: Scheduled events for the waiting room.
        # - **waiting_room_rule**: Bypass the waiting room.
        # - **waiting_room|json_response**: Enable JSON response for the waiting room.
        # - **waiting_room|disable_session_renewal**: Disable session renewal for the waiting room.
        # - **origin_rules|dns_record**: DNS record for back-to-origin rules.
        # - **managed_transforms|add_client_geolocation_headers**: Whether the real client IP header is available in transformation rules.
        # - **tiered_cache|regional_enable**: Area cache.
        # - **real_client_ip_header**: Client IP header.
        # - **data_timerange**: Data query time in minutes.
        # - **cache_rules|edge_cache_ttl**: Edge node TTL for cache.
        # - **cache_rules|browser_cache_ttl**: Browser TTL for cache.
        # - **fourLayerRecordCount**: Record count limit for Layer 4 acceleration.
        # - **waitingroomRuleCount**: Number of rules that can be associated with a single waitingRoomId.
        # - **waitingroomEventCount**: Number of events that can be associated with a single waitingRoomId.
        # - **waitingroom_custom_pathhost**: Hostname and path for the waiting room.
        # - **er_routers**: Function routing.
        # - **cache_rules|rule_quota**: Cache rules.
        # - **configuration_rules|rule_quota**: Configuration rules.
        # - **redirect_rules|rule_quota**: Redirect rules.
        # - **compression_rules|rule_quota**: Compression rules.
        # - **origin_rules|rule_quota**: Back-to-origin rules.
        # - **waf:phase:http_bot:rulesets_per_instance:less_than_or_equal**: Maximum number of rule groups per instance in WAF bot management.
        # - **waf:phase:http_whitelist:rules_per_instance:less_than_or_equal**: Maximum number of rules per instance in the WAF whitelist.
        # - **rtlog_quota**: Quota for the number of real-time log push tasks.
        # - **waf:phase:http_anti_scan:rulesets_per_instance:less_than_or_equal**: Maximum number of rule groups per instance in WAF scan protection.
        # - **ddos_instance**: Number of DDoS instances.
        # - **waf:phase:http_ratelimit:rules_per_instance:less_than_or_equal**: Maximum number of WAF rate limiting rules.
        # - **waf:phase:http_custom:rules_per_instance:less_than_or_equal**: Maximum number of rules per instance in the WAF custom rule phase.
        # - **ruleNestedConditionalCount**: Nesting level of rules.
        # - **waiting_room**: Waiting room.
        # - **transition_rule**: Transformation rules.
        # - **customHttpCert**: Number of custom certificates.
        # - **free_cert**: Number of free certificates.
        # - **preload**: Prefetch.
        # - **refresh_cache_tag**: Refresh - cache tag.
        # - **refresh_ignore_param**: Refresh - refresh ignoring parameters.
        # - **refresh_directory**: Refresh - refresh by folder.
        # - **refresh_hostname**: Refresh - refresh by hostname.
        # - **refresh_all**: Refresh - purge all cache.
        # - **refresh_file**: URL refresh.
        # - **wildcard**: Number of wildcard domain names.
        # - **recordCount**: Number of Layer 7 records.
        # - **siteCount**: Number of sites.
        # - **https|rule_quota**: Number of SSL/TLS rules.
        # 
        # This parameter is required.
        self.quota_name = quota_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.quota_name is not None:
            result['QuotaName'] = self.quota_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QuotaName') is not None:
            self.quota_name = m.get('QuotaName')

        return self

