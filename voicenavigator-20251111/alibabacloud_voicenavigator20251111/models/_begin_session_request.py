# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BeginSessionRequest(DaraModel):
    def __init__(
        self,
        draft_version: bool = None,
        instance_id: str = None,
        script_id: str = None,
        vendor_params: str = None,
    ):
        self.draft_version = draft_version
        self.instance_id = instance_id
        self.script_id = script_id
        self.vendor_params = vendor_params

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.draft_version is not None:
            result['DraftVersion'] = self.draft_version

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        if self.vendor_params is not None:
            result['VendorParams'] = self.vendor_params

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DraftVersion') is not None:
            self.draft_version = m.get('DraftVersion')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('VendorParams') is not None:
            self.vendor_params = m.get('VendorParams')

        return self

