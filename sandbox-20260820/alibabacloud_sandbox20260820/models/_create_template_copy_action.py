# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sandbox20260820 import models as main_models
from darabonba.model import DaraModel

class CreateTemplateCopyAction(DaraModel):
    def __init__(
        self,
        acr_instance_id: str = None,
        enabled: bool = None,
        image: str = None,
        registry_config: main_models.CreateTemplateRegistryConfig = None,
        registry_type: str = None,
    ):
        # The ID of the destination Container Registry Enterprise instance. This field does not inherit the instance ID of the source image.
        self.acr_instance_id = acr_instance_id
        # Specifies whether to enable the image replication action. This parameter is required when this action block is passed.
        self.enabled = enabled
        # The destination image address for the push operation. If this parameter is not provided, the service derives a new tag in the repository where the source image is located.
        self.image = image
        # The credentials, TLS settings, and network configurations required to access the destination image repository.
        self.registry_config = registry_config
        # The type of the destination image repository. Valid values: oci (standard OCI repository), acr (Container Registry Personal Edition), and acree (Container Registry Enterprise Edition). By default, the value is derived from the destination image address.
        self.registry_type = registry_type

    def validate(self):
        if self.registry_config:
            self.registry_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acr_instance_id is not None:
            result['acrInstanceId'] = self.acr_instance_id

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.image is not None:
            result['image'] = self.image

        if self.registry_config is not None:
            result['registryConfig'] = self.registry_config.to_map()

        if self.registry_type is not None:
            result['registryType'] = self.registry_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acrInstanceId') is not None:
            self.acr_instance_id = m.get('acrInstanceId')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('image') is not None:
            self.image = m.get('image')

        if m.get('registryConfig') is not None:
            temp_model = main_models.CreateTemplateRegistryConfig()
            self.registry_config = temp_model.from_map(m.get('registryConfig'))

        if m.get('registryType') is not None:
            self.registry_type = m.get('registryType')

        return self

