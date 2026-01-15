# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class NodeOperationParameters(DaraModel):
    def __init__(
        self,
        cordon_parameters: main_models.NodeCordonParameters = None,
        drain_parameters: main_models.NodeDrainParameters = None,
        uncordon_parameters: main_models.NodeUncordonParameters = None,
    ):
        self.cordon_parameters = cordon_parameters
        self.drain_parameters = drain_parameters
        self.uncordon_parameters = uncordon_parameters

    def validate(self):
        if self.cordon_parameters:
            self.cordon_parameters.validate()
        if self.drain_parameters:
            self.drain_parameters.validate()
        if self.uncordon_parameters:
            self.uncordon_parameters.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cordon_parameters is not None:
            result['CordonParameters'] = self.cordon_parameters.to_map()

        if self.drain_parameters is not None:
            result['DrainParameters'] = self.drain_parameters.to_map()

        if self.uncordon_parameters is not None:
            result['UncordonParameters'] = self.uncordon_parameters.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CordonParameters') is not None:
            temp_model = main_models.NodeCordonParameters()
            self.cordon_parameters = temp_model.from_map(m.get('CordonParameters'))

        if m.get('DrainParameters') is not None:
            temp_model = main_models.NodeDrainParameters()
            self.drain_parameters = temp_model.from_map(m.get('DrainParameters'))

        if m.get('UncordonParameters') is not None:
            temp_model = main_models.NodeUncordonParameters()
            self.uncordon_parameters = temp_model.from_map(m.get('UncordonParameters'))

        return self

