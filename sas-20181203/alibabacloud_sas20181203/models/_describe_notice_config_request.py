# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeNoticeConfigRequest(DaraModel):
    def __init__(
        self,
        biz_type: str = None,
        source_ip: str = None,
    ):
        # Notification configuration type, with values:
        # - **Default (not provided)**: SMS/Email/Site Message 
        # - **cms**: Cloud Monitor Push
        self.biz_type = biz_type
        # The source IP address of the request.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self

