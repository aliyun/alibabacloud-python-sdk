# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pai_dlc20201203 import models as main_models
from darabonba.model import DaraModel

class ContainerSpec(DaraModel):
    def __init__(
        self,
        args: List[str] = None,
        command: List[str] = None,
        env: List[main_models.EnvVar] = None,
        image: str = None,
        name: str = None,
        resources: main_models.ResourceRequirements = None,
        working_dir: str = None,
    ):
        self.args = args
        self.command = command
        self.env = env
        self.image = image
        self.name = name
        self.resources = resources
        self.working_dir = working_dir

    def validate(self):
        if self.env:
            for v1 in self.env:
                 if v1:
                    v1.validate()
        if self.resources:
            self.resources.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.args is not None:
            result['Args'] = self.args

        if self.command is not None:
            result['Command'] = self.command

        result['Env'] = []
        if self.env is not None:
            for k1 in self.env:
                result['Env'].append(k1.to_map() if k1 else None)

        if self.image is not None:
            result['Image'] = self.image

        if self.name is not None:
            result['Name'] = self.name

        if self.resources is not None:
            result['Resources'] = self.resources.to_map()

        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Args') is not None:
            self.args = m.get('Args')

        if m.get('Command') is not None:
            self.command = m.get('Command')

        self.env = []
        if m.get('Env') is not None:
            for k1 in m.get('Env'):
                temp_model = main_models.EnvVar()
                self.env.append(temp_model.from_map(k1))

        if m.get('Image') is not None:
            self.image = m.get('Image')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Resources') is not None:
            temp_model = main_models.ResourceRequirements()
            self.resources = temp_model.from_map(m.get('Resources'))

        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')

        return self

