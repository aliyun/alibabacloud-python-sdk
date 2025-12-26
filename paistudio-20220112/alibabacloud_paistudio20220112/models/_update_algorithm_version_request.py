# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class UpdateAlgorithmVersionRequest(DaraModel):
    def __init__(
        self,
        algorithm_spec: main_models.AlgorithmSpec = None,
    ):
        self.algorithm_spec = algorithm_spec

    def validate(self):
        if self.algorithm_spec:
            self.algorithm_spec.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.algorithm_spec is not None:
            result['AlgorithmSpec'] = self.algorithm_spec.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmSpec') is not None:
            temp_model = main_models.AlgorithmSpec()
            self.algorithm_spec = temp_model.from_map(m.get('AlgorithmSpec'))

        return self

