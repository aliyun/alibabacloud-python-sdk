# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateVodPackagingConfigurationShrinkRequest(DaraModel):
    def __init__(
        self,
        configuration_name: str = None,
        description: str = None,
        group_name: str = None,
        package_config_shrink: str = None,
        protocol: str = None,
    ):
        # The name of the packaging configuration. The name must be unique in an account and can be up to 128 characters in length. Letters, digits, underscores (_), and hyphens (-) are supported.
        self.configuration_name = configuration_name
        # The description of the packaging configuration.
        self.description = description
        # The name of the packaging group. The name can be up to 128 characters in length. Letters, digits, underscores (_), and hyphens (-) are supported.
        self.group_name = group_name
        # The packaging configuration.
        self.package_config_shrink = package_config_shrink
        # The package type.
        # 
        # *   HLS: packages content into TS segments for delivery over the HLS protocol.
        # *   HLS_CMAF: packages content into CMAF segments for delivery over the HLS protocol.
        # *   DASH: packages content for delivery over the DASH protocol.
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.configuration_name is not None:
            result['ConfigurationName'] = self.configuration_name

        if self.description is not None:
            result['Description'] = self.description

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.package_config_shrink is not None:
            result['PackageConfig'] = self.package_config_shrink

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigurationName') is not None:
            self.configuration_name = m.get('ConfigurationName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('PackageConfig') is not None:
            self.package_config_shrink = m.get('PackageConfig')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        return self

