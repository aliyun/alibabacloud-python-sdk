# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitScriptReviewRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        from_: str = None,
        instance_id: str = None,
        script_id: str = None,
    ):
        # This parameter is required.
        self.description = description
        self.from_ = from_
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.script_id = script_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.from_ is not None:
            result['From'] = self.from_

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        return self

