# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetProcessDefinitionRequest(DaraModel):
    def __init__(
        self,
        app_type: str = None,
        corp_id: str = None,
        group_id: str = None,
        language: str = None,
        name_space: str = None,
        order_number: str = None,
        process_instance_id: str = None,
        system_token: str = None,
        system_type: str = None,
    ):
        self.app_type = app_type
        self.corp_id = corp_id
        self.group_id = group_id
        self.language = language
        self.name_space = name_space
        self.order_number = order_number
        self.process_instance_id = process_instance_id
        self.system_token = system_token
        self.system_type = system_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.corp_id is not None:
            result['CorpId'] = self.corp_id

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.language is not None:
            result['Language'] = self.language

        if self.name_space is not None:
            result['NameSpace'] = self.name_space

        if self.order_number is not None:
            result['OrderNumber'] = self.order_number

        if self.process_instance_id is not None:
            result['ProcessInstanceId'] = self.process_instance_id

        if self.system_token is not None:
            result['SystemToken'] = self.system_token

        if self.system_type is not None:
            result['SystemType'] = self.system_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('NameSpace') is not None:
            self.name_space = m.get('NameSpace')

        if m.get('OrderNumber') is not None:
            self.order_number = m.get('OrderNumber')

        if m.get('ProcessInstanceId') is not None:
            self.process_instance_id = m.get('ProcessInstanceId')

        if m.get('SystemToken') is not None:
            self.system_token = m.get('SystemToken')

        if m.get('SystemType') is not None:
            self.system_type = m.get('SystemType')

        return self

