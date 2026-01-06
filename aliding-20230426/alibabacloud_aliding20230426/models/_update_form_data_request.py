# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateFormDataRequest(DaraModel):
    def __init__(
        self,
        app_type: str = None,
        form_instance_id: str = None,
        language: str = None,
        system_token: str = None,
        update_form_data_json: str = None,
        use_latest_version: bool = None,
    ):
        self.app_type = app_type
        self.form_instance_id = form_instance_id
        self.language = language
        self.system_token = system_token
        self.update_form_data_json = update_form_data_json
        self.use_latest_version = use_latest_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.form_instance_id is not None:
            result['FormInstanceId'] = self.form_instance_id

        if self.language is not None:
            result['Language'] = self.language

        if self.system_token is not None:
            result['SystemToken'] = self.system_token

        if self.update_form_data_json is not None:
            result['UpdateFormDataJson'] = self.update_form_data_json

        if self.use_latest_version is not None:
            result['UseLatestVersion'] = self.use_latest_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('FormInstanceId') is not None:
            self.form_instance_id = m.get('FormInstanceId')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('SystemToken') is not None:
            self.system_token = m.get('SystemToken')

        if m.get('UpdateFormDataJson') is not None:
            self.update_form_data_json = m.get('UpdateFormDataJson')

        if m.get('UseLatestVersion') is not None:
            self.use_latest_version = m.get('UseLatestVersion')

        return self

