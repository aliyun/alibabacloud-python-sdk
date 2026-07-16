# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDNSSLBWeightRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        record_id: str = None,
        user_client_ip: str = None,
        weight: int = None,
    ):
        # The language of the request and response. Default value: **zh**. Valid values:
        # 
        # - **zh**: Chinese
        # 
        # - **en**: English
        self.lang = lang
        # The ID of the DNS record. Call the [DescribeDomainRecords](https://www.alibabacloud.com/help/zh/dns/api-alidns-2015-01-09-describedomainrecords?spm=a2c63.p38356.help-menu-search-29697.d_0) operation to obtain the record ID.
        # 
        # This parameter is required.
        self.record_id = record_id
        # The client IP address.
        self.user_client_ip = user_client_ip
        # The new weight. The value must be an integer in the range of `[1,100]`.
        # 
        # This parameter is required.
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.record_id is not None:
            result['RecordId'] = self.record_id

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

