# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class VodPackagingConfiguration(DaraModel):
    def __init__(
        self,
        configuration_name: str = None,
        create_time: str = None,
        description: str = None,
        group_name: str = None,
        package_config: main_models.VodPackagingConfig = None,
        protocol: str = None,
    ):
        self.configuration_name = configuration_name
        self.create_time = create_time
        self.description = description
        self.group_name = group_name
        self.package_config = package_config
        self.protocol = protocol

    def validate(self):
        if self.package_config:
            self.package_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.configuration_name is not None:
            result['ConfigurationName'] = self.configuration_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.package_config is not None:
            result['PackageConfig'] = self.package_config.to_map()

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigurationName') is not None:
            self.configuration_name = m.get('ConfigurationName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('PackageConfig') is not None:
            temp_model = main_models.VodPackagingConfig()
            self.package_config = temp_model.from_map(m.get('PackageConfig'))

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        return self

