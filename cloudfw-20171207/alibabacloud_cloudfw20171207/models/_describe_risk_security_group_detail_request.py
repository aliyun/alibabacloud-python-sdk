# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRiskSecurityGroupDetailRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_name: str = None,
        lang: str = None,
        page_no: str = None,
        page_size: str = None,
        region_id: str = None,
        rule_uuid: str = None,
        source_ip: str = None,
    ):
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.lang = lang
        # This parameter is required.
        self.page_no = page_no
        # This parameter is required.
        self.page_size = page_size
        self.region_id = region_id
        self.rule_uuid = rule_uuid
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.rule_uuid is not None:
            result['RuleUuid'] = self.rule_uuid

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RuleUuid') is not None:
            self.rule_uuid = m.get('RuleUuid')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self

