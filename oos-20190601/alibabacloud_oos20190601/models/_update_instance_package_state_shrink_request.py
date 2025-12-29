# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateInstancePackageStateShrinkRequest(DaraModel):
    def __init__(
        self,
        configuration_info: str = None,
        configure_action: str = None,
        instance_id: str = None,
        parameters_shrink: str = None,
        region_id: str = None,
        template_name: str = None,
        template_version: str = None,
    ):
        self.configuration_info = configuration_info
        # The operation type.
        # 
        # Valid values:
        # 
        # *   uninstall
        # *   install
        # 
        # This parameter is required.
        self.configure_action = configure_action
        # The ID of the Elastic Compute Service (ECS) instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The parameters for installing or uninstalling the extensions.
        self.parameters_shrink = parameters_shrink
        # The region ID.
        self.region_id = region_id
        # The name of the template.
        # 
        # This parameter is required.
        self.template_name = template_name
        # The version of the template.
        self.template_version = template_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.configuration_info is not None:
            result['ConfigurationInfo'] = self.configuration_info

        if self.configure_action is not None:
            result['ConfigureAction'] = self.configure_action

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.parameters_shrink is not None:
            result['Parameters'] = self.parameters_shrink

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigurationInfo') is not None:
            self.configuration_info = m.get('ConfigurationInfo')

        if m.get('ConfigureAction') is not None:
            self.configure_action = m.get('ConfigureAction')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Parameters') is not None:
            self.parameters_shrink = m.get('Parameters')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')

        return self

