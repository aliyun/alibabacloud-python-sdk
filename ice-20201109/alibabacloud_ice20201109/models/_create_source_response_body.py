# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class CreateSourceResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        source: main_models.ChannelAssemblySource = None,
    ):
        # **Request ID**
        self.request_id = request_id
        # The source information.
        self.source = source

    def validate(self):
        if self.source:
            self.source.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.source is not None:
            result['Source'] = self.source.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Source') is not None:
            temp_model = main_models.ChannelAssemblySource()
            self.source = temp_model.from_map(m.get('Source'))

        return self

