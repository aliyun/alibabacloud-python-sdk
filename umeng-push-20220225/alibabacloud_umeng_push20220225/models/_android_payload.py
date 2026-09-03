# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_umeng_push20220225 import models as main_models
from darabonba.model import DaraModel

class AndroidPayload(DaraModel):
    def __init__(
        self,
        body: main_models.Body = None,
        display_type: str = None,
        extra: Dict[str, Any] = None,
        message_2third_channel: main_models.Message2ThirdChannel = None,
    ):
        self.body = body
        self.display_type = display_type
        self.extra = extra
        self.message_2third_channel = message_2third_channel

    def validate(self):
        if self.body:
            self.body.validate()
        if self.message_2third_channel:
            self.message_2third_channel.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body.to_map()

        if self.display_type is not None:
            result['displayType'] = self.display_type

        if self.extra is not None:
            result['extra'] = self.extra

        if self.message_2third_channel is not None:
            result['message2ThirdChannel'] = self.message_2third_channel.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = main_models.Body()
            self.body = temp_model.from_map(m.get('body'))

        if m.get('displayType') is not None:
            self.display_type = m.get('displayType')

        if m.get('extra') is not None:
            self.extra = m.get('extra')

        if m.get('message2ThirdChannel') is not None:
            temp_model = main_models.Message2ThirdChannel()
            self.message_2third_channel = temp_model.from_map(m.get('message2ThirdChannel'))

        return self

