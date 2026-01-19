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
        # Specifies whether to enable the delete mode. Valid values:
        # 
        # *   true: enables the delete mode
        # *   false (default): disables the delete mode
        # 
        # > This parameter is valid only when you manually trigger or periodically trigger custom rules to evaluate resources. If you enable the delete mode, the evaluation results that are not updated during the current evaluation are automatically deleted.
        self.delete_mode = delete_mode
        # The evaluation results.
        self.evaluations = evaluations
        # The callback token. When Cloud Config triggers a custom rule to evaluate resources, the token information is sent to Function Compute as an input parameter. The token must be specified when you submit the evaluation results.
        # 
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

