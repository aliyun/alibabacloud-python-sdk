# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetInstancesByIdListRequest(DaraModel):
    def __init__(
        self,
        app_type: str = None,
        language: str = None,
        process_instance_ids: str = None,
        system_token: str = None,
    ):
        self.app_type = app_type
        self.language = language
        self.process_instance_ids = process_instance_ids
        self.system_token = system_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.language is not None:
            result['Language'] = self.language

        if self.process_instance_ids is not None:
            result['ProcessInstanceIds'] = self.process_instance_ids

        if self.system_token is not None:
            result['SystemToken'] = self.system_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('ProcessInstanceIds') is not None:
            self.process_instance_ids = m.get('ProcessInstanceIds')

        if m.get('SystemToken') is not None:
            self.system_token = m.get('SystemToken')

        return self

