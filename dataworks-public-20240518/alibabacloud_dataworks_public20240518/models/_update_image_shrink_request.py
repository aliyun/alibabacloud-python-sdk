# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateImageShrinkRequest(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        acr_associated_vpc_id: str = None,
        acr_instance_id: str = None,
        build_config_shrink: str = None,
        description: str = None,
        id: str = None,
        image_uri: str = None,
        name: str = None,
        namespace: str = None,
        provider_image_id: str = None,
        repository_name: str = None,
        supported_shrink: str = None,
    ):
        # The image visibility. Valid values:
        # - Public: visible to all users.
        # - Private: visible only to the creator.
        self.accessibility = accessibility
        # The VPC ID associated with the ACR instance. This parameter is required when referencing an ACR image.
        self.acr_associated_vpc_id = acr_associated_vpc_id
        # The Container Registry (ACR) instance ID. This parameter is required when referencing an ACR image.
        self.acr_instance_id = acr_instance_id
        # The image build configuration.
        self.build_config_shrink = build_config_shrink
        # The image description.
        self.description = description
        # The image ID.
        # 
        # This parameter is required.
        self.id = id
        # The image URI. This parameter is required when referencing an ACR image.
        self.image_uri = image_uri
        # The image name.
        self.name = name
        # The image namespace. Set this parameter to DataWorks Default when referencing a DataWorks official image.
        self.namespace = namespace
        # The provider image ID. This parameter is required when referencing a DataWorks official image.
        self.provider_image_id = provider_image_id
        # The image repository name. Set this parameter to DataWorks Default when referencing a DataWorks official image.
        self.repository_name = repository_name
        # The image sub-purpose.
        self.supported_shrink = supported_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility

        if self.acr_associated_vpc_id is not None:
            result['AcrAssociatedVpcId'] = self.acr_associated_vpc_id

        if self.acr_instance_id is not None:
            result['AcrInstanceId'] = self.acr_instance_id

        if self.build_config_shrink is not None:
            result['BuildConfig'] = self.build_config_shrink

        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.provider_image_id is not None:
            result['ProviderImageId'] = self.provider_image_id

        if self.repository_name is not None:
            result['RepositoryName'] = self.repository_name

        if self.supported_shrink is not None:
            result['Supported'] = self.supported_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')

        if m.get('AcrAssociatedVpcId') is not None:
            self.acr_associated_vpc_id = m.get('AcrAssociatedVpcId')

        if m.get('AcrInstanceId') is not None:
            self.acr_instance_id = m.get('AcrInstanceId')

        if m.get('BuildConfig') is not None:
            self.build_config_shrink = m.get('BuildConfig')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('ProviderImageId') is not None:
            self.provider_image_id = m.get('ProviderImageId')

        if m.get('RepositoryName') is not None:
            self.repository_name = m.get('RepositoryName')

        if m.get('Supported') is not None:
            self.supported_shrink = m.get('Supported')

        return self

