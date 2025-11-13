# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTextFileRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        contract_id: str = None,
        create_time: str = None,
        text_file_name: str = None,
        text_file_url: str = None,
    ):
        self.client_token = client_token
        self.contract_id = contract_id
        self.create_time = create_time
        self.text_file_name = text_file_name
        self.text_file_url = text_file_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.contract_id is not None:
            result['ContractId'] = self.contract_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.text_file_name is not None:
            result['TextFileName'] = self.text_file_name

        if self.text_file_url is not None:
            result['TextFileUrl'] = self.text_file_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ContractId') is not None:
            self.contract_id = m.get('ContractId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('TextFileName') is not None:
            self.text_file_name = m.get('TextFileName')

        if m.get('TextFileUrl') is not None:
            self.text_file_url = m.get('TextFileUrl')

        return self

