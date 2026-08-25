# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateImageShrinkRequest(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        acr_associated_vpc_id: str = None,
        acr_instance_id: str = None,
        build_config_shrink: str = None,
        client_token: str = None,
        description: str = None,
        enable_sync_max_compute: bool = None,
        image_uri: str = None,
        name: str = None,
        namespace: str = None,
        provider_image_id: str = None,
        provider_type: str = None,
        repository_name: str = None,
        supported_shrink: str = None,
    ):
        # The image visibility. Valid values:
        # - Public: visible to all users.
        # - Private: visible only to the creator.
        self.accessibility = accessibility
        # The VPC ID associated with the ACR instance. This parameter is required when referencing an ACR image.
        self.acr_associated_vpc_id = acr_associated_vpc_id
        # The ACR instance ID. This parameter is required when referencing an ACR image.
        self.acr_instance_id = acr_instance_id
        # The image build configuration.
        self.build_config_shrink = build_config_shrink
        # The client idempotency token.
        # 
        # This parameter is required.
        self.client_token = client_token
        # The image description, up to 128 characters.
        self.description = description
        # Specifies whether to synchronize the image to MaxCompute. Specify this parameter when referencing an ACR image. Default value: false.
        self.enable_sync_max_compute = enable_sync_max_compute
        # The image URI. This parameter is required when referencing an ACR image.
        self.image_uri = image_uri
        # The image name, which can contain lowercase letters, digits, and underscores (_), up to 128 characters.
        # 
        # This parameter is required.
        self.name = name
        # The image namespace. Set this parameter to DataWorks Default when referencing a DataWorks official image.
        # 
        # This parameter is required.
        self.namespace = namespace
        # The image ID from the image provider. This parameter is required when referencing a DataWorks official image.
        self.provider_image_id = provider_image_id
        # The image reference data type. Valid values:
        # 
        # - ACR: ACR image repository.
        # - DataWorks: DataWorks official image.
        # 
        # This parameter is required.
        self.provider_type = provider_type
        # The image repository name. Set this parameter to DataWorks Default when referencing a DataWorks official image.
        # 
        # This parameter is required.
        self.repository_name = repository_name
        # The image sub-purpose.
        # 
        # This parameter is required.
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

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.enable_sync_max_compute is not None:
            result['EnableSyncMaxCompute'] = self.enable_sync_max_compute

        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.provider_image_id is not None:
            result['ProviderImageId'] = self.provider_image_id

        if self.provider_type is not None:
            result['ProviderType'] = self.provider_type

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

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnableSyncMaxCompute') is not None:
            self.enable_sync_max_compute = m.get('EnableSyncMaxCompute')

        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('ProviderImageId') is not None:
            self.provider_image_id = m.get('ProviderImageId')

        if m.get('ProviderType') is not None:
            self.provider_type = m.get('ProviderType')

        if m.get('RepositoryName') is not None:
            self.repository_name = m.get('RepositoryName')

        if m.get('Supported') is not None:
            self.supported_shrink = m.get('Supported')

        return self

