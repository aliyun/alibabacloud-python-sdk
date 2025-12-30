# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRequestGraphRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_type: str = None,
        end_timestamp: int = None,
        lang: str = None,
        start_timestamp: int = None,
        user_client_ip: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # The business ID. BizId is specified together with BizType.
        # 
        # *   If you set BizType to AUTH_ZONE, set BizId to a zone ID.
        # *   If you set BizType to RESOLVER_RULE, set BizId to the ID of a forwarding rule.
        self.biz_id = biz_id
        # The business type. Valid values:
        # 
        # *   AUTH_ZONE: authoritative zone
        # *   RESOLVER_RULE: forwarding rule
        self.biz_type = biz_type
        # The end of the time range to query. Set the time to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # This parameter is required.
        self.end_timestamp = end_timestamp
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        # 
        # Default value: en.
        self.lang = lang
        # The beginning of the time range to query. Set the time to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # This parameter is required.
        self.start_timestamp = start_timestamp
        # The IP address of the client.
        self.user_client_ip = user_client_ip
        # The ID of the virtual private cloud (VPC).
        self.vpc_id = vpc_id
        # The zone ID.
        # 
        # >  To query the number of DNS requests for a zone, you can specify ZoneId or BizType and BizId.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

