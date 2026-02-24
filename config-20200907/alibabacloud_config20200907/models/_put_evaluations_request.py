# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PutEvaluationsRequest(DaraModel):
    def __init__(
        self,
        delete_mode: bool = None,
        evaluations: str = None,
        result_token: str = None,
    ):
        self.delete_mode = delete_mode
        self.evaluations = evaluations
        # This parameter is required.
        self.result_token = result_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delete_mode is not None:
            result['DeleteMode'] = self.delete_mode

        if self.evaluations is not None:
            result['Evaluations'] = self.evaluations

        if self.result_token is not None:
            result['ResultToken'] = self.result_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeleteMode') is not None:
            self.delete_mode = m.get('DeleteMode')

        if m.get('Evaluations') is not None:
            self.evaluations = m.get('Evaluations')

        if m.get('ResultToken') is not None:
            self.result_token = m.get('ResultToken')

        return self

