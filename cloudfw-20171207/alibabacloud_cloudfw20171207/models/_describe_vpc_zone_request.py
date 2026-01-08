# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVpcZoneRequest(DaraModel):
    def __init__(
        self,
        environment: str = None,
        lang: str = None,
        member_uid: str = None,
        region_no: str = None,
    ):
        # The environment. Valid values:
        # 
        # *   **VPC**
        # *   **TransitRouter**
        self.environment = environment
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang
        # The UID of the member in Cloud Firewall.
        self.member_uid = member_uid
        # The region ID.
        # 
        # This parameter is required.
        self.region_no = region_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.environment is not None:
            result['Environment'] = self.environment

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Environment') is not None:
            self.environment = m.get('Environment')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        return self

