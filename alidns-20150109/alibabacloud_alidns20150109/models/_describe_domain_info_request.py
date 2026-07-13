# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDomainInfoRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        lang: str = None,
        need_detail_attributes: bool = None,
    ):
        # The domain name. Call [DescribeDomains](https://help.aliyun.com/document_detail/2357286.html) to obtain the domain name.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The language of the response. Valid values:
        # 
        # - zh: Chinese
        # 
        # - en: English
        # 
        # Default value: en.
        self.lang = lang
        # Specifies whether to return detailed attributes of the domain name. Valid values:
        # 
        # - true
        # 
        # - false
        # 
        # The default value is false.
        # 
        # If you set this parameter to **true**, the response includes the following parameters: lineType, minTtl, recordLineTreeJson, recordLines, lineCode, lineDisplayName, lineName, regionLines, and slaveDns.
        self.need_detail_attributes = need_detail_attributes

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

        if self.need_detail_attributes is not None:
            result['NeedDetailAttributes'] = self.need_detail_attributes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('NeedDetailAttributes') is not None:
            self.need_detail_attributes = m.get('NeedDetailAttributes')

        return self

