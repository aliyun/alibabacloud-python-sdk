# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class Personalizedtxt2imgAddModelTrainJobRequest(DaraModel):
    def __init__(
        self,
        image_url: List[str] = None,
        name: str = None,
        object_type: str = None,
        train_steps: int = None,
    ):
        # This parameter is required.
        self.image_url = image_url
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.object_type = object_type
        self.train_steps = train_steps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_url is not None:
            result['imageUrl'] = self.image_url

        if self.name is not None:
            result['name'] = self.name

        if self.object_type is not None:
            result['objectType'] = self.object_type

        if self.train_steps is not None:
            result['trainSteps'] = self.train_steps

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('imageUrl') is not None:
            self.image_url = m.get('imageUrl')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('objectType') is not None:
            self.object_type = m.get('objectType')

        if m.get('trainSteps') is not None:
            self.train_steps = m.get('trainSteps')

        return self

