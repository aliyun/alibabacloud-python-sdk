# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListScriptRecordingRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        ref_ids_json: str = None,
        script_id: str = None,
        search: str = None,
        states_json: str = None,
        uuids_json: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size
        self.ref_ids_json = ref_ids_json
        # This parameter is required.
        self.script_id = script_id
        self.search = search
        self.states_json = states_json
        self.uuids_json = uuids_json

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.ref_ids_json is not None:
            result['RefIdsJson'] = self.ref_ids_json

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        if self.search is not None:
            result['Search'] = self.search

        if self.states_json is not None:
            result['StatesJson'] = self.states_json

        if self.uuids_json is not None:
            result['UuidsJson'] = self.uuids_json

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RefIdsJson') is not None:
            self.ref_ids_json = m.get('RefIdsJson')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('Search') is not None:
            self.search = m.get('Search')

        if m.get('StatesJson') is not None:
            self.states_json = m.get('StatesJson')

        if m.get('UuidsJson') is not None:
            self.uuids_json = m.get('UuidsJson')

        return self

