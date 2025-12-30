# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChangeDomainGroupRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        group_id: str = None,
        lang: str = None,
    ):
        # The domain name. You can call the [DescribeDomains ](https://www.alibabacloud.com/help/zh/dns/api-alidns-2015-01-09-describedomains?spm=a2c63.p38356.help-menu-search-29697.d_0)operation to obtain the domain name.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The ID of the target domain name group.
        # 
        # *   If you do not specify GroupId, the domain name belongs to the default group.
        # *   If you specify an empty string "" for GroupId, the domain name belongs to the default group.
        # *   If you set GroupId to defaultGroup, the domain name belongs to the default group.
        # *   If you specify GroupId to another value and the value is verified existent, the value of GroupId for the target domain name is updated. If the value is verified inexistent, the value of GroupId for the target domain name is not updated.
        self.group_id = group_id
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        # 
        # Default value: en
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.lang is not None:
            result['Lang'] = self.lang

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        return self

