# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSuspEventUserSettingRequest(DaraModel):
    def __init__(
        self,
        from_: str = None,
        id: int = None,
        source_ip: str = None,
    ):
        # The ID of the request source. Set the value to **sas**.
        self.from_ = from_
        # The ID. You do not need to specify this parameter.
        self.id = id
        # The IP address of the request. You do not need to specify this parameter.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_ is not None:
            result['From'] = self.from_

        if self.id is not None:
            result['Id'] = self.id

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self

