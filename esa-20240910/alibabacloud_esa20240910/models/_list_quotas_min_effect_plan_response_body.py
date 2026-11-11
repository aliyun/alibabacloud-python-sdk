# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListQuotasMinEffectPlanResponseBody(DaraModel):
    def __init__(
        self,
        quotas: List[main_models.ListQuotasMinEffectPlanResponseBodyQuotas] = None,
        request_id: str = None,
    ):
        # The details of the minimum required plan versions for the quotas.
        self.quotas = quotas
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.quotas:
            for v1 in self.quotas:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Quotas'] = []
        if self.quotas is not None:
            for k1 in self.quotas:
                result['Quotas'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.quotas = []
        if m.get('Quotas') is not None:
            for k1 in m.get('Quotas'):
                temp_model = main_models.ListQuotasMinEffectPlanResponseBodyQuotas()
                self.quotas.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListQuotasMinEffectPlanResponseBodyQuotas(DaraModel):
    def __init__(
        self,
        quota_name: str = None,
        quota_value_detail: List[main_models.ListQuotasMinEffectPlanResponseBodyQuotasQuotaValueDetail] = None,
        quota_value_type: str = None,
    ):
        # The name of the quota. Valid values:
        # - **waf:phase:http_anti_scan:actions**: WAF scan protection - action enumeration
        # - **waf:phase:http_bot:actions**: WAF bot management - all action enumerations
        # - **waf:phase:http_bot:http_custom_cc_dev:characteristic:fields**: WAF bot management - statistical object enumeration for custom device rate limiting
        # - **waf:phase:http_bot:http_custom_cc_ip:characteristic:fields**: WAF bot management - statistical object enumeration for custom IP rate limiting
        # - ****waf:phase:http_bot:match:symbols****: WAF bot management - match symbol enumeration
        # - **waf:phase:http_bot:http_custom_cc:characteristic:fields**: WAF bot management - statistical object enumeration for custom session rate limiting
        # - **waf:phase:http_bot:match:fields**: WAF bot management phase - match field enumeration
        # - **waf:phase:http_whitelist:match:symbols**: WAF whitelist - match symbol enumeration
        # - **waf:phase:http_whitelist:match:fields**: WAF whitelist - match field enumeration
        # - **waf:phase:http_anti_scan:http_directory_traversal:characteristic:fields**: WAF scan protection - statistical object enumeration for folder traverse blocking
        # - **waf:phase:http_anti_scan:http_high_frequency:characteristic:fields**: WAF scan protection - statistical object enumeration for high-frequency scan blocking
        # - **waf:phase:http_anti_scan:match:symbols**: WAF scan protection - match symbol enumeration
        # - **waf:phase:http_anti_scan:match:fields**: WAF scan protection - match field enumeration
        # - **waf:phase:http_managed:actions**: WAF managed rules - action enumeration
        # - **waf:phase:http_managed:group:reference:ids**: WAF managed rules - referenced rule group enumeration
        # - **waf:phase:http_ratelimit:actions**: WAF rate limiting - action enumeration
        # - **waf:phase:http_ratelimit:ttls**: WAF rate limiting - duration enumeration
        # - **waf:phase:http_ratelimit:intervals**: WAF rate limiting - statistical duration
        # - **waf:phase:http_ratelimit:http_ratelimit:characteristic:fields**: WAF rate limiting - match characteristic enumeration for control type rules
        # - **waf:phase:http_ratelimit:match:symbols**: WAF rate limiting rule phase - match symbol enumeration
        # - **waf:phase:http_ratelimit:match:fields**: WAF rate limiting rule phase - match field enumeration
        # - **waf:phase:http_custom:actions**: WAF custom rule phase - action enumeration
        # - **waf:phase:http_custom:match:symbols**: WAF custom rule phase - match symbol enumeration
        # - **waf:phase:http_custom:match:fields**: WAF custom rule phase - match fields
        # - **waitingroom|wr_queueing_method**: Waiting room - queuing method
        # - **origin_rules|origin_scheme**: Back-to-origin rules - back-to-origin protocol
        # - **origin_rules|origin_sni**: Back-to-origin rules - back-to-origin SNI
        # - **origin_rules|origin_host**: Back-to-origin rules - back-to-origin host
        # - **fourlayeracceleration**: Layer 4 acceleration
        # - **rtlog_service**: Real-time log feature switch
        # - **dashboard_traffic**: Value-added capability for network traffic analysis
        # - **custom_name_server**: Custom NS name
        # - **waf:phase:http_bot:enable**: WAF bot management switch
        # - **waf:phase:http_whitelist:enable**: WAF whitelist switch
        # - **instantlog**: Whether instant logs are active
        # - **waf:phase:http_anti_scan:enable**: WAF scan protection switch
        # - **waf:phase:http_managed:group:reference:enable**: WAF managed rules - configure referenced rule group switch
        # - **waf:phase:http_managed:enable**: WAF managed rules switch
        # - **waf:phase:http_ratelimit:on_hit:enable**: WAF rate limiting - apply to cached requests switch
        # - **ddos**: DDoS instance
        # - **waf:phase:http_ratelimit:enable**: WAF rate limiting rule phase switch
        # - **waf:phase:http_custom:enable**: WAF custom rule phase switch
        # - **waf:phase:all:page:reference:enable**: WAF custom response page switch
        # - **rules_support_regex**: Whether the rule DPI engine supports regular expression operations
        # - **waitingroom_event**: Waiting room - scheduled events
        # - **waitingroom_rule**: Waiting room - bypass waiting room
        # - **waitingroom|wr_json_response**: Waiting room - enable JSON response
        # - **waitingroom|wr_disable_session_renewal**: Waiting room - disable session renewal
        # - **origin_rules|dns_record**: Back-to-origin rules - DNS record
        # - **managed_transforms|add_client_geolocation_headers**: Whether the real client IP header is active in transformation rules
        # - **tiered_cache|regional_enable**: Area cache
        # - **real_client_ip_header**: Client IP header
        self.quota_name = quota_name
        # The threshold details of the quota.
        self.quota_value_detail = quota_value_detail
        # The threshold type of the quota. Valid values:
        # - value: enumeration type. A quota of the enumeration type has multiple enumeration thresholds. For each enumeration threshold, the response indicates whether it is available in the current plan version. If it is unavailable, the response indicates the minimum required plan version.
        # - bool: Boolean type. A quota of the Boolean type is abstracted into two enumeration thresholds: true and false. To check whether the quota is available in the current plan version and identify the minimum required plan version, you only need to focus on the quota details where the enumeration value is true.
        self.quota_value_type = quota_value_type

    def validate(self):
        if self.quota_value_detail:
            for v1 in self.quota_value_detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.quota_name is not None:
            result['QuotaName'] = self.quota_name

        result['QuotaValueDetail'] = []
        if self.quota_value_detail is not None:
            for k1 in self.quota_value_detail:
                result['QuotaValueDetail'].append(k1.to_map() if k1 else None)

        if self.quota_value_type is not None:
            result['QuotaValueType'] = self.quota_value_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QuotaName') is not None:
            self.quota_name = m.get('QuotaName')

        self.quota_value_detail = []
        if m.get('QuotaValueDetail') is not None:
            for k1 in m.get('QuotaValueDetail'):
                temp_model = main_models.ListQuotasMinEffectPlanResponseBodyQuotasQuotaValueDetail()
                self.quota_value_detail.append(temp_model.from_map(k1))

        if m.get('QuotaValueType') is not None:
            self.quota_value_type = m.get('QuotaValueType')

        return self

class ListQuotasMinEffectPlanResponseBodyQuotasQuotaValueDetail(DaraModel):
    def __init__(
        self,
        is_effect: str = None,
        min_effect_plan: str = None,
        value: str = None,
    ):
        # Specifies whether the quota value is available in the plan version corresponding to the current site. Valid values:
        # - ture: Available.
        # - false: Unavailable.
        self.is_effect = is_effect
        # The minimum required plan version for the quota value. Valid values:
        # - basic: Basic Edition.
        # - medium: Standard Edition.
        # - high: Advanced Edition.
        # - enterprise_standard_cn: Enterprise Edition.
        # The return value of this parameter follows these rules:
        # - If the quota value is already available in the current plan version, this parameter is left empty, meaning the minimum required plan version is not displayed.
        # - If the quota value is unavailable in the current plan version, the minimum required plan version is displayed.
        # - If the current plan is already the Enterprise Edition, this parameter is always empty.
        self.min_effect_plan = min_effect_plan
        # The quota value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_effect is not None:
            result['IsEffect'] = self.is_effect

        if self.min_effect_plan is not None:
            result['MinEffectPlan'] = self.min_effect_plan

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsEffect') is not None:
            self.is_effect = m.get('IsEffect')

        if m.get('MinEffectPlan') is not None:
            self.min_effect_plan = m.get('MinEffectPlan')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

