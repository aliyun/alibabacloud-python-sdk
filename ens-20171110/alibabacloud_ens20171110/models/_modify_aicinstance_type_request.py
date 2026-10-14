# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyAICInstanceTypeRequest(DaraModel):
    def __init__(
        self,
        environment_var: str = None,
        frequency: int = None,
        image_id: str = None,
        instance_id: str = None,
        instance_type: str = None,
        resolution: str = None,
    ):
        # One or more environment variables to set during instance initialization.
        self.environment_var = environment_var
        # The refresh rate. Unit: Hz. Valid values:
        # - 30
        # - 60
        # - 120
        self.frequency = frequency
        # The image ID.
        # 
        # This parameter is required.
        self.image_id = image_id
        # The ID of the instance whose specifications you want to modify.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The target AIC container instance specifications.
        # 
        # This parameter is required.
        self.instance_type = instance_type
        # The resolution. Valid values:
        # - 1920*1080
        # - 1080*1920
        # - 1280*720
        # - 720*1280
        # - 2400*1080
        # - 1080*2400
        # - 1920*864
        # - 864*1920
        self.resolution = resolution

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.environment_var is not None:
            result['EnvironmentVar'] = self.environment_var

        if self.frequency is not None:
            result['Frequency'] = self.frequency

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.resolution is not None:
            result['Resolution'] = self.resolution

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvironmentVar') is not None:
            self.environment_var = m.get('EnvironmentVar')

        if m.get('Frequency') is not None:
            self.frequency = m.get('Frequency')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')

        return self

