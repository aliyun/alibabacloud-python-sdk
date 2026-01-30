# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ValidationOptions(DaraModel):
    def __init__(
        self,
        skip_verify_aichat_completion: bool = None,
    ):
        self.skip_verify_aichat_completion = skip_verify_aichat_completion

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.skip_verify_aichat_completion is not None:
            result['skipVerifyAIChatCompletion'] = self.skip_verify_aichat_completion

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('skipVerifyAIChatCompletion') is not None:
            self.skip_verify_aichat_completion = m.get('skipVerifyAIChatCompletion')

        return self

