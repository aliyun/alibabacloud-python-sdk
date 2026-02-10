# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeInstallCaptchaRequest(DaraModel):
    def __init__(
        self,
        deadline: str = None,
        lang: str = None,
        source_ip: str = None,
    ):
        # The validity period of verification codes. If this parameter is not specified, only the valid verification codes are returned.
        # 
        # >  An installation verification code can be used only within the validity period. An expired installation verification code cannot be used to install the Security Center agent.
        self.deadline = deadline
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese.
        # *   **en**: English.
        self.lang = lang
        # The source IP address of the request.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deadline is not None:
            result['Deadline'] = self.deadline

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Deadline') is not None:
            self.deadline = m.get('Deadline')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self

