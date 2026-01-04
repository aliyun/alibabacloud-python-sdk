# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConfigWebCCRuleV2Request(DaraModel):
    def __init__(
        self,
        domain: str = None,
        expires: int = None,
        rule_list: str = None,
    ):
        # This parameter is required.
        self.domain = domain
        self.expires = expires
        # The frequency control rule. This parameter is a JSON string that contains the following fields:
        # 
        # *   **action**: the action that is performed if the rule is matched. This field is required and must be of the string type. Valid values:
        # 
        #     *   **block**: The requests that match the rule are blocked.
        #     *   **challenge**: Completely Automated Public Turing test to tell Computers and Humans Apart (CAPTCHA) verification for the requests that match the rule is implemented.
        #     *   **watch**: The requests that match the rule are recorded in logs and allowed.
        # 
        # *   **name**: the name of the rule. This field is required and must be of the string type.
        # 
        # *   **condition**: the match conditions. This field is required and must be of the map type. This field contains the following parameters:
        # 
        #     **
        # 
        #     **Note** The AND logical operator is used to evaluate multiple match conditions.
        # 
        #     *   **field**: the match field. This field is required and must be of the string type.
        # 
        #     *   **match_method**: the logical relation. This field is required and must be of the string type.
        # 
        #         **
        # 
        #         **Note** For information about the mappings between the **field** and **match_method** parameters, see the "Mappings between the field and match_method parameters" section of this topic.
        # 
        #     *   **header_name**: the name of the custom HTTP header. This field is optional and must be of the string type.
        # 
        #         **
        # 
        #         **Note** This field is required only when **field** is set to **header**.
        # 
        #     *   **content**: the match content. This field is required and must be of the string type.
        # 
        # *   **ratelimit**: the frequency control field. This field is optional and must be of the string type. The frequency can be measured based on IP addresses or custom headers. This field contains the following parameters:
        # 
        #     *   **interval**: the statistical duration. Unit: seconds. This field is required and must be of the integer type.
        #     *   **ttl**: the period during which the specified action is performed. Unit: seconds. This field is required and must be of the integer type.
        #     *   **threshold**: the threshold. This field is required and must be of the integer type.
        #     *   **subkey**: the name of the field. This field is optional and must be of the string type. This field is required only when target is set to header.
        #     *   **target**: the statistical source. This field is required and must be of the string type. Valid values: ip and header.
        # 
        # *   **status_code**: the frequency control field. This field is optional and must be of the string type. Frequency control can be performed based on the quantity or percentage of status codes. This field contains the following parameters:
        # 
        #     *   **enabled**: specifies whether to enable status code statistics. This field is required and must be of the Boolean type.
        #     *   **code**: the status code. This field is required and must be of the integer type. Valid values: **100** to **599**.
        #     *   **use_ratio**: specifies whether to use a ratio. This field is required and must be of the Boolean type. To use a ratio, set this field to true.
        #     *   **ratio_threshold**: the ratio of the status code. This field is optional and must be of the integer type. If a ratio is used, the action specified in the rule is performed only when the ratio of the status code reaches **ratio_threshold**. Valid values: **1** to **100**.
        #     *   **count_threshold**: the quantity of the status code. This field is optional and must be of the integer type. If a ratio is not used, the action specified in the rule is performed only when the quantity of the status code reaches **count_threshold**. Valid values: **2** to **50000**.
        # 
        # *   **statistics**: specifies whether deduplication is used for statistics. This field is optional and must be of the string type. By default, deduplication is not used for statistics. This field contains the following parameters:
        # 
        #     *   **mode**: specifies whether deduplication is used for status code statistics. This field is required and must be of the string type. Valid values:
        # 
        #         *   **count**: Deduplication is not used for statistics.
        #         *   **distinct**: Deduplication is used for statistics.
        # 
        #     *   **field**: the statistical source. This field is required and must be of the string type. Valid values: ip, header, and uri.
        # 
        #     *   **header_name**: the name of the header. This field is optional and must be of the string type. This field is required only when field is set to header.
        # 
        # This parameter is required.
        self.rule_list = rule_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.expires is not None:
            result['Expires'] = self.expires

        if self.rule_list is not None:
            result['RuleList'] = self.rule_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Expires') is not None:
            self.expires = m.get('Expires')

        if m.get('RuleList') is not None:
            self.rule_list = m.get('RuleList')

        return self

