# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class PutDisableFwSwitchRequest(DaraModel):
    def __init__(
        self,
        ipaddr_list: List[str] = None,
        lang: str = None,
        region_list: List[str] = None,
        resource_type_list: List[str] = None,
        source_ip: str = None,
    ):
        # The IP addresses.
        # 
        # >  You must specify at least one of the IpaddrList, RegionList, and ResourceTypeList parameters.
        self.ipaddr_list = ipaddr_list
        # The language of the content within the response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The regions.
        # 
        # >  You must specify at least one of the IpaddrList, RegionList, and ResourceTypeList parameters.
        self.region_list = region_list
        # The types of the assets.
        # 
        # > You must specify at least one of the IpaddrList, RegionList, and ResourceTypeList parameters.
        self.resource_type_list = resource_type_list
        # The source IP address of the request.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipaddr_list is not None:
            result['IpaddrList'] = self.ipaddr_list

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.region_list is not None:
            result['RegionList'] = self.region_list

        if self.resource_type_list is not None:
            result['ResourceTypeList'] = self.resource_type_list

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpaddrList') is not None:
            self.ipaddr_list = m.get('IpaddrList')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RegionList') is not None:
            self.region_list = m.get('RegionList')

        if m.get('ResourceTypeList') is not None:
            self.resource_type_list = m.get('ResourceTypeList')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self

