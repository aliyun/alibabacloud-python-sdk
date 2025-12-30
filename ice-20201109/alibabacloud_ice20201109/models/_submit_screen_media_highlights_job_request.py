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
        # The editing configuration. For detailed parameters, see [EditingConfig](~~2863940#9b05519d46e0x~~).
        self.editing_config = editing_config
        # The input configuration. For detailed parameters, see [InputConfig](~~2863940#dda38bf6ec2pk~~).
        self.input_config = input_config
        # The output configuration. For detailed parameters, see [OutputConfig](~~2863940#4111a373d0xbz~~).
        self.output_config = output_config
        # The user-defined data, including the business and callback configurations. For more information, see [UserData](https://help.aliyun.com/document_detail/357745.html).
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

