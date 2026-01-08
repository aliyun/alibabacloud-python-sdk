# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAclBackupDataRequest(DaraModel):
    def __init__(
        self,
        back_up_time: str = None,
        lang: str = None,
        source_ip: str = None,
    ):
        # This parameter is required.
        self.back_up_time = back_up_time
        self.lang = lang
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.back_up_time is not None:
            result['BackUpTime'] = self.back_up_time

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackUpTime') is not None:
            self.back_up_time = m.get('BackUpTime')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self

