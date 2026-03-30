# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListScriptsRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        name: str = None,
        number: str = None,
        page_number: int = None,
        page_size: int = None,
        script_ids: List[str] = None,
        status: str = None,
    ):
        self.instance_id = instance_id
        self.name = name
        self.number = number
        self.page_number = page_number
        self.page_size = page_size
        self.script_ids = script_ids
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.number is not None:
            result['Number'] = self.number

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.script_ids is not None:
            result['ScriptIds'] = self.script_ids

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Number') is not None:
            self.number = m.get('Number')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ScriptIds') is not None:
            self.script_ids = m.get('ScriptIds')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

