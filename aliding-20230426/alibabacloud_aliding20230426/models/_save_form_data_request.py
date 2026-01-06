# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SaveFormDataRequest(DaraModel):
    def __init__(
        self,
        app_type: str = None,
        form_data_json: str = None,
        form_uuid: str = None,
        language: str = None,
        system_token: str = None,
    ):
        # This parameter is required.
        self.app_type = app_type
        # This parameter is required.
        self.form_data_json = form_data_json
        # This parameter is required.
        self.form_uuid = form_uuid
        self.language = language
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

        if self.form_data_json is not None:
            result['FormDataJson'] = self.form_data_json

        if self.form_uuid is not None:
            result['FormUuid'] = self.form_uuid

        if self.language is not None:
            result['Language'] = self.language

        if self.system_token is not None:
            result['SystemToken'] = self.system_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('FormDataJson') is not None:
            self.form_data_json = m.get('FormDataJson')

        if m.get('FormUuid') is not None:
            self.form_uuid = m.get('FormUuid')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('SystemToken') is not None:
            self.system_token = m.get('SystemToken')

        return self

