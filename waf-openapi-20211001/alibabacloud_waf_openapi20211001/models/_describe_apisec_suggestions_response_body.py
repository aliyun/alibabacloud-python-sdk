# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeApisecSuggestionsResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribeApisecSuggestionsResponseBodyData] = None,
        request_id: str = None,
    ):
        # The list of protection suggestions for the API asset.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeApisecSuggestionsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeApisecSuggestionsResponseBodyData(DaraModel):
    def __init__(
        self,
        api_format: str = None,
        matched_host: str = None,
        suggest_id: str = None,
        suggest_rule: str = None,
        suggest_type: str = None,
    ):
        # The request path of the API.
        self.api_format = api_format
        # The domain name or IP address associated with the API.
        self.matched_host = matched_host
        # The ID of the protection suggestion.
        self.suggest_id = suggest_id
        # The protection suggestion rule, in JSON format. The JSON string contains the following parameters:
        # 
        # - **event_tags**: the event type.
        # 
        # - **black_iplist**: the IP address blacklist.
        # 
        # - **ip_baseline**: the IP address list.
        # 
        # - **freq_baseline**: the frequency limit information.
        # 
        # - **client_id_baseline**: the client information.
        # 
        # - **country_baseline**: the country information.
        # 
        # - **province_baseline**: the region information.
        # 
        # - **sensitive_type**: the sensitive information type.
        self.suggest_rule = suggest_rule
        # The type of the protection suggestion. Valid values:
        # 
        # - **BotRule**: a bot rule.
        # 
        # - **BlackIPRule**: an IP address blacklist rule.
        # 
        # - **WhiteIPRule**: an IP address whitelist rule.
        # 
        # - **RateLimitRule**: a rate limiting rule.
        # 
        # - **ClientRule**: a client rule.
        # 
        # - **GeoRule**: a region rule.
        # 
        # - **SensitiveRule**: a sensitive information rule.
        # 
        # - **UnauthRule**: an authentication rule.
        self.suggest_type = suggest_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_format is not None:
            result['ApiFormat'] = self.api_format

        if self.matched_host is not None:
            result['MatchedHost'] = self.matched_host

        if self.suggest_id is not None:
            result['SuggestId'] = self.suggest_id

        if self.suggest_rule is not None:
            result['SuggestRule'] = self.suggest_rule

        if self.suggest_type is not None:
            result['SuggestType'] = self.suggest_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiFormat') is not None:
            self.api_format = m.get('ApiFormat')

        if m.get('MatchedHost') is not None:
            self.matched_host = m.get('MatchedHost')

        if m.get('SuggestId') is not None:
            self.suggest_id = m.get('SuggestId')

        if m.get('SuggestRule') is not None:
            self.suggest_rule = m.get('SuggestRule')

        if m.get('SuggestType') is not None:
            self.suggest_type = m.get('SuggestType')

        return self

