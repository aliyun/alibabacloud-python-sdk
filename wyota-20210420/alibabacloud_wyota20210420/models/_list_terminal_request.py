# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTerminalRequest(DaraModel):
    def __init__(
        self,
        alias: str = None,
        build_id: str = None,
        client_type: int = None,
        in_manage: bool = None,
        ipv_4: str = None,
        location_info: str = None,
        max_results: int = None,
        model: str = None,
        next_token: str = None,
        search_keyword: str = None,
        serial_number: str = None,
        terminal_group_id: str = None,
        uuid: str = None,
    ):
        self.alias = alias
        self.build_id = build_id
        self.client_type = client_type
        self.in_manage = in_manage
        self.ipv_4 = ipv_4
        self.location_info = location_info
        self.max_results = max_results
        self.model = model
        self.next_token = next_token
        self.search_keyword = search_keyword
        self.serial_number = serial_number
        self.terminal_group_id = terminal_group_id
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['Alias'] = self.alias

        if self.build_id is not None:
            result['BuildId'] = self.build_id

        if self.client_type is not None:
            result['ClientType'] = self.client_type

        if self.in_manage is not None:
            result['InManage'] = self.in_manage

        if self.ipv_4 is not None:
            result['Ipv4'] = self.ipv_4

        if self.location_info is not None:
            result['LocationInfo'] = self.location_info

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.model is not None:
            result['Model'] = self.model

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.search_keyword is not None:
            result['SearchKeyword'] = self.search_keyword

        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number

        if self.terminal_group_id is not None:
            result['TerminalGroupId'] = self.terminal_group_id

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')

        if m.get('BuildId') is not None:
            self.build_id = m.get('BuildId')

        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')

        if m.get('InManage') is not None:
            self.in_manage = m.get('InManage')

        if m.get('Ipv4') is not None:
            self.ipv_4 = m.get('Ipv4')

        if m.get('LocationInfo') is not None:
            self.location_info = m.get('LocationInfo')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('SearchKeyword') is not None:
            self.search_keyword = m.get('SearchKeyword')

        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')

        if m.get('TerminalGroupId') is not None:
            self.terminal_group_id = m.get('TerminalGroupId')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

