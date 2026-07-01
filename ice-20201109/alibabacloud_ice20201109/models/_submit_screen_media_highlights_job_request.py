# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitScreenMediaHighlightsJobRequest(DaraModel):
    def __init__(
        self,
        editing_config: str = None,
        input_config: str = None,
        output_config: str = None,
        user_data: str = None,
    ):
        # Specifies the editing configuration. For more information, see [EditingConfig Parameter Description](~~2863940#9b05519d46e0x~~).
        self.editing_config = editing_config
        # Specifies the input configuration. For more information, see [InputConfig Parameter Description](~~2863940#dda38bf6ec2pk~~).
        self.input_config = input_config
        # Specifies the output configuration. For more information, see [OutputConfig Parameter Description](~~2863940#4111a373d0xbz~~).
        self.output_config = output_config
        # Specifies the user data and callback configuration. For details about the structure, see [UserData Configuration](https://help.aliyun.com/document_detail/357745.html).
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.editing_config is not None:
            result['EditingConfig'] = self.editing_config

        if self.input_config is not None:
            result['InputConfig'] = self.input_config

        if self.output_config is not None:
            result['OutputConfig'] = self.output_config

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EditingConfig') is not None:
            self.editing_config = m.get('EditingConfig')

        if m.get('InputConfig') is not None:
            self.input_config = m.get('InputConfig')

        if m.get('OutputConfig') is not None:
            self.output_config = m.get('OutputConfig')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

