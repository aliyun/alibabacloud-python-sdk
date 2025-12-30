# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDomainGroupRequest(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        group_name: str = None,
        lang: str = None,
    ):
        # The ID of the domain name group whose name you want to modify. You can call the [DescribeDomainGroups ](https://www.alibabacloud.com/help/zh/dns/api-alidns-2015-01-09-describedomaingroups?spm=a2c63.p38356.help-menu-search-29697.d_0)operation to obtain the ID.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The new name of the domain name group.
        # 
        # This parameter is required.
        self.group_name = group_name
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        # 
        # Default value: en.
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.lang is not None:
            result['Lang'] = self.lang

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        return self

