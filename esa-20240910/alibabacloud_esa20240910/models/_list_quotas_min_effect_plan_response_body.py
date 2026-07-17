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
        # The list of minimum effective plan editions for quotas.
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
        # The quota name. Valid values:
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
        # - **waitingroom|wr_queueing_method**: waiting room - queuing method.
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
        # - **waitingroom_event**: waiting room - scheduled event.
        # - **waitingroom_rule**: waiting room - bypass waiting room.
        # - **waitingroom|wr_json_response**: waiting room - enable JSON response.
        # - **waitingroom|wr_disable_session_renewal**: waiting room - disable session renewal.
        # - **origin_rules|dns_record**: back-to-origin rule - DNS record.
        # - **managed_transforms|add_client_geolocation_headers**: whether the real client IP header is active in transform rules.
        # - **tiered_cache|regional_enable**: area cache.
        # - **real_client_ip_header**: client IP header.
        self.quota_name = quota_name
        # The list of quota threshold details.
        self.quota_value_detail = quota_value_detail
        # The threshold type of the quota. Valid values:
        # 
        # - value: enumeration type. An enumeration-type quota has multiple enumeration thresholds. For each enumeration threshold, the system indicates whether it is available in the current edition and, if not, the minimum plan edition in which it becomes available.
        # - bool: Boolean type. A Boolean-type quota is abstracted into two enumeration thresholds: true and false. To check whether the quota is available in the current plan edition and the minimum available plan edition, you only need to check the quota details for the true enumeration in the quota details list.
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
        # Indicates whether the quota value is available in the plan edition associated with the current site. Valid values:
        # 
        # - true: Available.
        # - false: Not available.
        self.is_effect = is_effect
        # The minimum plan edition in which the quota value is available. Valid values:
        # 
        # - basic: Basic Edition.
        # - medium: Standard Edition.
        # - high: Pro Edition.
        # - enterprise_standard_cn: Enterprise Edition.
        # 
        # This parameter follows these rules:
        # 
        # - If the quota value is already available in the current edition, this parameter is empty, meaning the minimum available plan edition is not displayed.
        # - If the quota value is not available in the current edition, the minimum available edition is displayed.
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

