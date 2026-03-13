# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ElectronicItineraryGetApplyResultRequest(DaraModel):
    def __init__(
        self,
        batch_apply_no: str = None,
    ):
        # This parameter is required.
        self.batch_apply_no = batch_apply_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_apply_no is not None:
            result['batch_apply_no'] = self.batch_apply_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('batch_apply_no') is not None:
            self.batch_apply_no = m.get('batch_apply_no')

        return self

