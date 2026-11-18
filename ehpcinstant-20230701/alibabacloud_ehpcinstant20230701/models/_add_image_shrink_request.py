# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddImageShrinkRequest(DaraModel):
    def __init__(
        self,
        container_image_spec_shrink: str = None,
        description: str = None,
        image_type: str = None,
        image_version: str = None,
        name: str = None,
        vmimage_spec_shrink: str = None,
    ):
        # The container image configuration.
        self.container_image_spec_shrink = container_image_spec_shrink
        # The image description.
        self.description = description
        # The image type. Valid values:
        # 
        # - VM: virtual machine image
        # - Container: container image
        self.image_type = image_type
        # The image version.
        self.image_version = image_version
        # The image name.
        # 
        # This parameter is required.
        self.name = name
        # The virtual machine image configuration.
        self.vmimage_spec_shrink = vmimage_spec_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.container_image_spec_shrink is not None:
            result['ContainerImageSpec'] = self.container_image_spec_shrink

        if self.description is not None:
            result['Description'] = self.description

        if self.image_type is not None:
            result['ImageType'] = self.image_type

        if self.image_version is not None:
            result['ImageVersion'] = self.image_version

        if self.name is not None:
            result['Name'] = self.name

        if self.vmimage_spec_shrink is not None:
            result['VMImageSpec'] = self.vmimage_spec_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerImageSpec') is not None:
            self.container_image_spec_shrink = m.get('ContainerImageSpec')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')

        if m.get('ImageVersion') is not None:
            self.image_version = m.get('ImageVersion')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('VMImageSpec') is not None:
            self.vmimage_spec_shrink = m.get('VMImageSpec')

        return self

