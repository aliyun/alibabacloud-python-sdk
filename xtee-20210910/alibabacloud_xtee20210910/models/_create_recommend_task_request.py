# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRecommendTaskRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        name: str = None,
        reg_id: str = None,
        sample_id: int = None,
        variables_str: str = None,
        velocities_str: str = None,
    ):
        # Set the language type for requests and received messages, default value is **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Name
        # 
        # This parameter is required.
        self.name = name
        # Region code
        self.reg_id = reg_id
        # Task ID.
        # 
        # This parameter is required.
        self.sample_id = sample_id
        # Variables to be calculated, variables
        # 
        # This parameter is required.
        self.variables_str = variables_str
        # Indicator effect
        # 
        # This parameter is required.
        self.velocities_str = velocities_str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.name is not None:
            result['name'] = self.name

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.sample_id is not None:
            result['sampleId'] = self.sample_id

        if self.variables_str is not None:
            result['variablesStr'] = self.variables_str

        if self.velocities_str is not None:
            result['velocitiesStr'] = self.velocities_str

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('sampleId') is not None:
            self.sample_id = m.get('sampleId')

        if m.get('variablesStr') is not None:
            self.variables_str = m.get('variablesStr')

        if m.get('velocitiesStr') is not None:
            self.velocities_str = m.get('velocitiesStr')

        return self

