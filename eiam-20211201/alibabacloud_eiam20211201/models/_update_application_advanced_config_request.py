# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class UpdateApplicationAdvancedConfigRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        instance_id: str = None,
        scim_server_advanced_config: main_models.UpdateApplicationAdvancedConfigRequestScimServerAdvancedConfig = None,
    ):
        # The application ID.
        # 
        # This parameter is required.
        self.application_id = application_id
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The advanced configuration of the SCIM server.
        self.scim_server_advanced_config = scim_server_advanced_config

    def validate(self):
        if self.scim_server_advanced_config:
            self.scim_server_advanced_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.scim_server_advanced_config is not None:
            result['ScimServerAdvancedConfig'] = self.scim_server_advanced_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ScimServerAdvancedConfig') is not None:
            temp_model = main_models.UpdateApplicationAdvancedConfigRequestScimServerAdvancedConfig()
            self.scim_server_advanced_config = temp_model.from_map(m.get('ScimServerAdvancedConfig'))

        return self

class UpdateApplicationAdvancedConfigRequestScimServerAdvancedConfig(DaraModel):
    def __init__(
        self,
        supported_user_custom_field_ids: List[str] = None,
        user_custom_field_namespace: str = None,
    ):
        # A list of IDs of supported custom user fields.
        self.supported_user_custom_field_ids = supported_user_custom_field_ids
        # The namespace of the user extension fields.
        self.user_custom_field_namespace = user_custom_field_namespace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.supported_user_custom_field_ids is not None:
            result['SupportedUserCustomFieldIds'] = self.supported_user_custom_field_ids

        if self.user_custom_field_namespace is not None:
            result['UserCustomFieldNamespace'] = self.user_custom_field_namespace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SupportedUserCustomFieldIds') is not None:
            self.supported_user_custom_field_ids = m.get('SupportedUserCustomFieldIds')

        if m.get('UserCustomFieldNamespace') is not None:
            self.user_custom_field_namespace = m.get('UserCustomFieldNamespace')

        return self

