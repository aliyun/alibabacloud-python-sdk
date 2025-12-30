# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class CreateSourceLocationResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        source_location: main_models.ChannelAssemblySourceLocation = None,
    ):
        # **Request ID**
        self.request_id = request_id
        # The source location information.
        self.source_location = source_location

    def validate(self):
        if self.source_location:
            self.source_location.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.source_location is not None:
            result['SourceLocation'] = self.source_location.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SourceLocation') is not None:
            temp_model = main_models.ChannelAssemblySourceLocation()
            self.source_location = temp_model.from_map(m.get('SourceLocation'))

        return self

