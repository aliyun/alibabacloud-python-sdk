# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListQuotasMinEffectPlanRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        quota_names: str = None,
        site_id: int = None,
    ):
        # The plan instance ID. You can call the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation to obtain the instance ID. You must specify at least one of this parameter and SiteId.
        self.instance_id = instance_id
        # The plan quota names, separated by commas (,). Valid values:
        # - **waf:phase:http_anti_scan:actions**: WAF scan protection - action enumeration.
        # - **waf:phase:http_bot:actions**: WAF bot management - all action enumeration.
        # - **waf:phase:http_bot:http_custom_cc_dev:characteristic:fields**: WAF bot management - custom device rate limiting statistical object enumeration.
        # - **waf:phase:http_bot:http_custom_cc_ip:characteristic:fields**: WAF bot management - custom IP rate limiting statistical object enumeration.
        # - ****waf:phase:http_bot:match:symbols****: WAF bot management - match operator enumeration.
        # - **waf:phase:http_bot:http_custom_cc:characteristic:fields**: WAF bot management - custom session rate limiting statistical object enumeration.
        # - **waf:phase:http_bot:match:fields**: WAF bot management - match field enumeration.
        # - **waf:phase:http_whitelist:match:symbols**: WAF whitelist - match operator enumeration.
        # - **waf:phase:http_whitelist:match:fields**: WAF whitelist - match field enumeration.
        # - **waf:phase:http_anti_scan:http_directory_traversal:characteristic:fields**: WAF scan protection - folder traverse blocking statistical object enumeration.
        # - **waf:phase:http_anti_scan:http_high_frequency:characteristic:fields**: WAF scan protection - high-frequency scan blocking statistical object enumeration.
        # - **waf:phase:http_anti_scan:match:symbols**: WAF scan protection - match operator enumeration.
        # - **waf:phase:http_anti_scan:match:fields**: WAF scan protection - match field enumeration.
        # - **waf:phase:http_managed:actions**: WAF managed rules - action enumeration.
        # - **waf:phase:http_managed:group:reference:ids**: WAF managed rules - referenced rule group enumeration.
        # - **waf:phase:http_ratelimit:actions**: WAF rate limiting - action enumeration.
        # - **waf:phase:http_ratelimit:ttls**: WAF rate limiting - duration enumeration.
        # - **waf:phase:http_ratelimit:intervals**: WAF rate limiting - statistical period.
        # - **waf:phase:http_ratelimit:http_ratelimit:characteristic:fields**: WAF rate limiting - control type rule match characteristic enumeration.
        # - **waf:phase:http_ratelimit:match:symbols**: WAF rate limiting rule phase match operator enumeration.
        # - **waf:phase:http_ratelimit:match:fields**: WAF rate limiting rule phase match field enumeration.
        # - **waf:phase:http_custom:actions**: WAF custom rule phase action enumeration.
        # - **waf:phase:http_custom:match:symbols**: WAF custom rule phase match operator enumeration.
        # - **waf:phase:http_custom:match:fields**: WAF custom rule phase match field.
        # - **waiting_room|queuing_method**: waiting room - queuing method.
        # - **origin_rules|origin_scheme**: back-to-origin rule - back-to-origin protocol.
        # - **origin_rules|origin_sni**: back-to-origin rule - back-to-origin SNI.
        # - **origin_rules|origin_host**: back-to-origin rule - back-to-origin host.
        # - **fourlayeracceleration**: Layer 4 acceleration.
        # - **rtlog_service**: real-time log feature switch.
        # - **dashboard_traffic**: value-added capability for network traffic analysis.
        # - **custom_name_server**: custom NS name.
        # - **waf:phase:http_bot:enable**: WAF bot management switch.
        # - **waf:phase:http_whitelist:enable**: WAF whitelist switch.
        # - **instantlog**: instant log active or not.
        # - **waf:phase:http_anti_scan:enable**: WAF scan protection switch.
        # - **waf:phase:http_managed:group:reference:enable**: WAF managed rules - referenced rule group configuration switch.
        # - **waf:phase:http_managed:enable**: WAF managed rules switch.
        # - **waf:phase:http_ratelimit:on_hit:enable**: WAF rate limiting - apply to cache-hit requests switch.
        # - **ddos**: DDoS instance.
        # - **waf:phase:http_ratelimit:enable**: WAF rate limiting rule phase switch.
        # - **waf:phase:http_custom:enable**: WAF custom rule phase switch.
        # - **waf:phase:all:page:reference:enable**: WAF custom response page switch.
        # - **rules_support_regex**: whether the DPI engine supports regular expressions.
        # - **waiting_room_event**: waiting room - scheduled event.
        # - **waiting_room_rule**: waiting room - bypass waiting room.
        # - **waiting_room|json_response**: waiting room - enable JSON response.
        # - **waiting_room|disable_session_renewal**: waiting room - disable session renewal.
        # - **origin_rules|dns_record**: back-to-origin rule - DNS record.
        # - **managed_transforms|add_client_geolocation_headers**: whether the real client IP header is active in transform rules.
        # - **tiered_cache|regional_enable**: area cache.
        # - **real_client_ip_header**: client IP header.
        # 
        # This parameter is required.
        self.quota_names = quota_names
        # The site ID. You can call the [ListSites](~~ListSites~~) operation to obtain the site ID.
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

