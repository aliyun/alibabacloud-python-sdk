# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDnsCacheDomainRemarkRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        lang: str = None,
        remark: str = None,
    ):
        # The domain name.<props="china">Call [DescribeDomains](https://help.aliyun.com/en/dns/api-alidns-2015-01-09-describedomains?spm=a2c4g.11186623.help-menu-search-29697.d_0) to obtain the domain name.
        # <props="intl">Call [DescribeDomains](https://www.alibabacloud.com/help/en/dns/api-alidns-2015-01-09-describedomains?spm=a2c63.p38356.help-menu-search-29697.d_0) to obtain the domain name.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The language of the request and response. Valid values:
        # 
        # - **zh**: Chinese
        # 
        # - **en**: English
        # 
        # Default value: **zh**.
        self.lang = lang
        # The remark. The remark can be up to 50 characters in length and can contain Chinese characters, letters, digits, periods (.), underscores (_), and hyphens (-).
        # 
        # Leave this parameter empty to delete the existing remark.
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.remark is not None:
            result['Remark'] = self.remark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        return self

