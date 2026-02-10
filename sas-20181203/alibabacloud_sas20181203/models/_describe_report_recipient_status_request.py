# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeReportRecipientStatusRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        recipients: str = None,
        source_ip: str = None,
    ):
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The email address of the recipient. Separate multiple email addresses with commas (,).
        # 
        # This parameter is required.
        self.recipients = recipients
        # The source IP address of the request.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.recipients is not None:
            result['Recipients'] = self.recipients

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Recipients') is not None:
            self.recipients = m.get('Recipients')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self

