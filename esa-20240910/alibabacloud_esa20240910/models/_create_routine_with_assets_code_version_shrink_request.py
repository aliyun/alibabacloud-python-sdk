# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRoutineWithAssetsCodeVersionShrinkRequest(DaraModel):
    def __init__(
        self,
        build_id: int = None,
        code_description: str = None,
        conf_options_shrink: str = None,
        extra_info: str = None,
        name: str = None,
    ):
        self.build_id = build_id
        self.code_description = code_description
        self.conf_options_shrink = conf_options_shrink
        self.extra_info = extra_info
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.build_id is not None:
            result['BuildId'] = self.build_id

        if self.code_description is not None:
            result['CodeDescription'] = self.code_description

        if self.conf_options_shrink is not None:
            result['ConfOptions'] = self.conf_options_shrink

        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuildId') is not None:
            self.build_id = m.get('BuildId')

        if m.get('CodeDescription') is not None:
            self.code_description = m.get('CodeDescription')

        if m.get('ConfOptions') is not None:
            self.conf_options_shrink = m.get('ConfOptions')

        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

