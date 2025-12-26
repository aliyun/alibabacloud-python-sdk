# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAlgorithmRequest(DaraModel):
    def __init__(
        self,
        algorithm_description: str = None,
        display_name: str = None,
    ):
        self.algorithm_description = algorithm_description
        self.display_name = display_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.algorithm_description is not None:
            result['AlgorithmDescription'] = self.algorithm_description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmDescription') is not None:
            self.algorithm_description = m.get('AlgorithmDescription')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        return self

