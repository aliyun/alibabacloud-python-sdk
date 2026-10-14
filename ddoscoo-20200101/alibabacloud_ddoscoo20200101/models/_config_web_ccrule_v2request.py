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
        # The domain name of the website service.
        # > The domain name must have a website service forwarding rule configured. You can call [DescribeDomains](https://help.aliyun.com/document_detail/91724.html) to query all domain names.
        # 
        # This parameter is required.
        self.domain = domain
        # The validity period of the rule. Unit: seconds. Default value: 0, which indicates that the rule is permanently effective.
        self.expires = expires
        # The configuration of the frequency control rule, expressed as a JSON-formatted string with the following structure:
        # - **action**: String type. Required. The matching action. Valid values:
        #     - **block**: Block.
        #     - **challenge**: JavaScript Challenge.
        #     - **watch**: Monitor.
        # - **name**: String type. Required. The rule name.
        # - **condition**: Map type. Required. The matching condition. The structure is as follows:
        # 
        #     > If multiple matching conditions are specified, the conditions are evaluated using the AND logic.
        # 
        #     - **field**: String type. Required. The matching field.
        #     - **match_method**: String type. Required. The matching method.
        #  
        #         > For the valid values of **field** and **match_method**, see the supplementary description below the request parameters table.
        # 
        #     - **header_name**: String type. Optional. The name of the custom HTTP header field.
        # 
        #         > This parameter takes effect only when **field** is set to **header**.
        # 
        #     - **content**: String type. Required. The matching content.
        # - **ratelimit**: String type. Required. The frequency control field. You can collect frequency statistics by IP address or custom header. The structure is as follows:
        #   - **interval**: Integer type. Required. The statistical period (seconds).
        #   - **ttl**: Integer type. Required. The action duration (seconds).
        #   - **threshold**: Integer type. Required. The threshold (count).
        #   - **subkey**: String type. Optional. The field name. Set this parameter only when the statistical source is header.
        #   - **target**: String type. Required. The statistical source. Valid values: ip and header.
        # - **status_code**: String type. Optional. The frequency control field. You can collect statistics based on the count or ratio of status codes. The structure is as follows:
        #   - **enabled**: Boolean type. Required. Specifies whether to enable status code statistics.
        #   - **code**: Integer type. Required. Enabling status code. Valid values: **100** to **599**.
        #   - **use_ratio**: Boolean type. Required. Specifies whether to use the ratio. If set to true, the ratio is used.
        #   - **ratio_threshold**: Integer type. Optional. The ratio at which enabling status code appears. When the ratio is used, the action is triggered only when the corresponding status code reaches **ratio_threshold**. Valid values: **1** to **100**.
        #   - **count_threshold**: Integer type. Optional. The count at which enabling status code appears. When the ratio is not used, the action is triggered only when the corresponding status code reaches **count_threshold**. Valid values: **2** to **50000**.
        # - **statistics**: String type. Optional. The deduplication statistics. This parameter can be left empty, which indicates that deduplication is not performed. The structure is as follows:
        #   - **mode**: String type. Required. Specifies whether to enable deduplication statistics. Valid values:
        #     - **count**: deduplication disabled
        #     - **distinct**: deduplication enabled
        #   - **field**: String type. Required. The statistical source for deduplication. Valid values: ip, header, and uri.
        #   - **header_name**: String type. Optional. The field name. Set this parameter only when the statistical source is header.
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

