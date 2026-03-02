# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_neuron20211115 import models as main_models
from darabonba.model import DaraModel

class DeployPipelineInfo(DaraModel):
    def __init__(
        self,
        deploy_instance_infos: List[main_models.DeployInstanceInfo] = None,
        id: str = None,
        name: str = None,
    ):
        self.deploy_instance_infos = deploy_instance_infos
        self.id = id
        self.name = name

    def validate(self):
        if self.deploy_instance_infos:
            for v1 in self.deploy_instance_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['deployInstanceInfos'] = []
        if self.deploy_instance_infos is not None:
            for k1 in self.deploy_instance_infos:
                result['deployInstanceInfos'].append(k1.to_map() if k1 else None)

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.deploy_instance_infos = []
        if m.get('deployInstanceInfos') is not None:
            for k1 in m.get('deployInstanceInfos'):
                temp_model = main_models.DeployInstanceInfo()
                self.deploy_instance_infos.append(temp_model.from_map(k1))

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

