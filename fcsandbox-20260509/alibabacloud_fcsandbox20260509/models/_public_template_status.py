# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_fcsandbox20260509 import models as main_models
from darabonba.model import DaraModel

class PublicTemplateStatus(DaraModel):
    def __init__(
        self,
        finished_at: str = None,
        reason: main_models.PublicTemplateStatusReason = None,
        state: str = None,
    ):
        self.finished_at = finished_at
        self.reason = reason
        self.state = state

    def validate(self):
        if self.reason:
            self.reason.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.finished_at is not None:
            result['finishedAt'] = self.finished_at

        if self.reason is not None:
            result['reason'] = self.reason.to_map()

        if self.state is not None:
            result['state'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('finishedAt') is not None:
            self.finished_at = m.get('finishedAt')

        if m.get('reason') is not None:
            temp_model = main_models.PublicTemplateStatusReason()
            self.reason = temp_model.from_map(m.get('reason'))

        if m.get('state') is not None:
            self.state = m.get('state')

        return self

