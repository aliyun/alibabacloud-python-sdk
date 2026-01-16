# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_fc20230330 import models as main_models
from darabonba.model import DaraModel

class UpdateSessionRequest(DaraModel):
    def __init__(
        self,
        body: main_models.UpdateSessionInput = None,
        qualifier: str = None,
    ):
        # The session update configuration.
        self.body = body
        # The function alias or version associated with the session to be updated.
        self.qualifier = qualifier

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body.to_map()

        if self.qualifier is not None:
            result['qualifier'] = self.qualifier

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = main_models.UpdateSessionInput()
            self.body = temp_model.from_map(m.get('body'))

        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')

        return self

