# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetUserMaxPlanQuotaRequest(DaraModel):
    def __init__(
        self,
        quota_name: str = None,
    ):
        # The plan quota name. Valid values:
        # 
        # - **waf:phase:http_anti_scan:actions**: WAF scan protection - action enumeration.
        # - **waf:phase:http_bot:actions**: WAF bot management - all action enumeration.
        # - **waf:phase:http_bot:http_custom_cc_dev:characteristic:fields**: WAF bot management - custom device rate limiting type statistical object enumeration.
        # - **waf:phase:http_bot:http_custom_cc_ip:characteristic:fields**: WAF bot management - custom IP rate limiting type statistical object enumeration.
        # - ****waf:phase:http_bot:match:symbols****: WAF bot management - match operator enumeration.
        # - **waf:phase:http_bot:http_custom_cc:characteristic:fields**: WAF bot management - custom session rate limiting type statistical object enumeration.
        # - **waf:phase:http_bot:match:fields**: WAF bot management - match field enumeration.
        # - **waf:phase:http_whitelist:match:symbols**: WAF whitelist - match operator enumeration.
        # - **waf:phase:http_whitelist:match:fields**: WAF whitelist - match field enumeration.
        # - **waf:phase:http_anti_scan:http_directory_traversal:characteristic:fields**: WAF scan protection - folder traverse blocking type statistical object enumeration.
        # - **waf:phase:http_anti_scan:http_high_frequency:characteristic:fields**: WAF scan protection - high-frequency scan blocking type statistical object enumeration.
        # - **waf:phase:http_anti_scan:match:symbols**: WAF scan protection - match operator enumeration.
        # - **waf:phase:http_anti_scan:match:fields**: WAF scan protection - match field enumeration.
        # - **waf:phase:http_managed:actions**: WAF managed rules - action enumeration.
        # - **waf:phase:http_managed:group:reference:ids**: WAF managed rules - referenced rule group enumeration.
        # - **waf:phase:http_ratelimit:actions**: WAF rate limiting - action enumeration.
        # - **waf:phase:http_ratelimit:ttls**: WAF rate limiting - duration enumeration.
        # - **waf:phase:http_ratelimit:intervals**: WAF rate limiting - statistical duration.
        # - **waf:phase:http_ratelimit:http_ratelimit:characteristic:fields**: WAF rate limiting - control type rule - match characteristic enumeration.
        # - **waf:phase:http_ratelimit:match:symbols**: WAF rate limiting rule phase match operator enumeration.
        # - **waf:phase:http_ratelimit:match:fields**: WAF rate limiting rule phase match field enumeration.
        # - **waf:phase:http_custom:actions**: WAF custom rule phase action enumeration.
        # - **waf:phase:http_custom:match:symbols**: WAF custom rule phase match operator enumeration.
        # - **waf:phase:http_custom:match:fields**: WAF custom rule phase match field.
        # - **waiting_room|queuing_method**: Waiting room - queuing method.
        # - **origin_rules|origin_scheme**: Back-to-origin rules - back-to-origin protocol.
        # - **origin_rules|origin_sni**: Back-to-origin rules - back-to-origin SNI.
        # - **origin_rules|origin_host**: Back-to-origin rules - back-to-origin host.
        # - **fourlayeracceleration**: Layer 4 acceleration.
        # - **rtlog_service**: Real-time log feature switch.
        # - **dashboard_traffic**: Value-added capability of network traffic analysis.
        # - **custom_name_server**: Custom NS name.
        # - **waf:phase:http_bot:enable**: WAF bot management switch.
        # - **waf:phase:http_whitelist:enable**: WAF whitelist switch.
        # - **instantlog**: Instant log active or not.
        # - **waf:phase:http_anti_scan:enable**: WAF scan protection switch.
        # - **waf:phase:http_managed:group:reference:enable**: WAF managed rules - referenced rule group configuration switch.
        # - **waf:phase:http_managed:enable**: WAF managed rules switch.
        # - **waf:phase:http_ratelimit:on_hit:enable**: WAF rate limiting - apply on cache-hit requests switch.
        # - **ddos**: DDoS instance.
        # - **waf:phase:http_ratelimit:enable**: WAF rate limiting rule phase switch.
        # - **waf:phase:http_custom:enable**: WAF custom rule phase switch.
        # - **waf:phase:all:page:reference:enable**: WAF custom response page switch.
        # - **rules_support_regex**: Specifies whether the DPI engine supports regular expressions.
        # - **waiting_room_event**: Waiting room - scheduled event.
        # - **waiting_room_rule**: Waiting room - bypass waiting room.
        # - **waiting_room|json_response**: Waiting room - enable JSON response.
        # - **waiting_room|disable_session_renewal**: Waiting room - disable session renewal.
        # - **origin_rules|dns_record**: Back-to-origin rules - DNS record.
        # - **managed_transforms|add_client_geolocation_headers**: Specifies whether the real client IP header is active in transform rules.
        # - **tiered_cache|regional_enable**: Area cache.
        # - **real_client_ip_header**: Client IP header.
        # - **data_timerange**: Data query time range - in minutes.
        # - **cache_rules|edge_cache_ttl**: Cache - node TTL.
        # - **cache_rules|browser_cache_ttl**: Cache - browser TTL.
        # - **fourLayerRecordCount**: Record count limit for Layer 4 acceleration.
        # - **waitingroomRuleCount**: Maximum number of rules per waiting room ID.
        # - **waitingroomEventCount**: Maximum number of events per waiting room ID.
        # - **waitingroom_custom_pathhost**: Waiting room - hostname and path.
        # - **er_routers**: Function routing.
        # - **cache_rules|rule_quota**: Cache rules.
        # - **configuration_rules|rule_quota**: Configuration rules.
        # - **redirect_rules|rule_quota**: Redirect rules.
        # - **compression_rules|rule_quota**: Compression rules.
        # - **origin_rules|rule_quota**: Back-to-origin rules.
        # - **waf:phase:http_bot:rulesets_per_instance:less_than_or_equal**: WAF bot management - maximum number of rule groups per instance.
        # - **waf:phase:http_whitelist:rules_per_instance:less_than_or_equal**: WAF whitelist - maximum number of rules per instance.
        # - **rtlog_quota**: Quota for real-time log push node count.
        # - **waf:phase:http_anti_scan:rulesets_per_instance:less_than_or_equal**: WAF scan protection - maximum number of rule groups per instance.
        # - **ddos_instance**: Number of DDoS instances.
        # - **waf:phase:http_ratelimit:rules_per_instance:less_than_or_equal**: Maximum number of WAF rate limiting rules.
        # - **waf:phase:http_custom:rules_per_instance:less_than_or_equal**: WAF custom rule phase - maximum number of rules per instance.
        # - **ruleNestedConditionalCount**: Number of rule nesting levels.
        # - **waiting_room**: Waiting room.
        # - **transition_rule**: Transform rules.
        # - **customHttpCert**: Number of custom certificates.
        # - **free_cert**: Number of free certificates.
        # - **preload**: Resource prefetch.
        # - **refresh_cache_tag**: Refresh - cache tag.
        # - **refresh_ignore_param**: Refresh - purge without parameters.
        # - **refresh_directory**: Refresh - purge by folder.
        # - **refresh_hostname**: Refresh - purge by hostname.
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

