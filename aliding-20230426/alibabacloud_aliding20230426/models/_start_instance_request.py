# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartInstanceRequest(DaraModel):
    def __init__(
        self,
        app_type: str = None,
        department_id: str = None,
        form_data_json: str = None,
        form_uuid: str = None,
        language: str = None,
        process_code: str = None,
        process_data: str = None,
        system_token: str = None,
    ):
        self.app_type = app_type
        self.department_id = department_id
        self.form_data_json = form_data_json
        self.form_uuid = form_uuid
        self.language = language
        self.process_code = process_code
        self.process_data = process_data
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

        if self.department_id is not None:
            result['DepartmentId'] = self.department_id

        if self.form_data_json is not None:
            result['FormDataJson'] = self.form_data_json

        if self.form_uuid is not None:
            result['FormUuid'] = self.form_uuid

        if self.language is not None:
            result['Language'] = self.language

        if self.process_code is not None:
            result['ProcessCode'] = self.process_code

        if self.process_data is not None:
            result['ProcessData'] = self.process_data

        if self.system_token is not None:
            result['SystemToken'] = self.system_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')

        if m.get('FormDataJson') is not None:
            self.form_data_json = m.get('FormDataJson')

        if m.get('FormUuid') is not None:
            self.form_uuid = m.get('FormUuid')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('ProcessCode') is not None:
            self.process_code = m.get('ProcessCode')

        if m.get('ProcessData') is not None:
            self.process_data = m.get('ProcessData')

        if m.get('SystemToken') is not None:
            self.system_token = m.get('SystemToken')

        return self

