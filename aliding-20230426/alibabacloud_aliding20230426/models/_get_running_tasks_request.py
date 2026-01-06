# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetRunningTasksRequest(DaraModel):
    def __init__(
        self,
        app_type: str = None,
        language: str = None,
        process_codes: str = None,
        process_instance_id: str = None,
        system_token: str = None,
    ):
        # This parameter is required.
        self.app_type = app_type
        self.language = language
        self.process_codes = process_codes
        self.process_instance_id = process_instance_id
        # This parameter is required.
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

        if self.process_codes is not None:
            result['ProcessCodes'] = self.process_codes

        if self.process_instance_id is not None:
            result['ProcessInstanceId'] = self.process_instance_id

        if self.system_token is not None:
            result['SystemToken'] = self.system_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('ProcessCodes') is not None:
            self.process_codes = m.get('ProcessCodes')

        if m.get('ProcessInstanceId') is not None:
            self.process_instance_id = m.get('ProcessInstanceId')

        if m.get('SystemToken') is not None:
            self.system_token = m.get('SystemToken')

        return self

