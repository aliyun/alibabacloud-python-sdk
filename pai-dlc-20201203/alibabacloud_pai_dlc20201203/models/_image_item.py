# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImageItem(DaraModel):
    def __init__(
        self,
        accelerator_type: str = None,
        author_id: str = None,
        framework: str = None,
        image_provider_type: str = None,
        image_tag: str = None,
        image_url: str = None,
        image_url_vpc: str = None,
    ):
        self.accelerator_type = accelerator_type
        self.author_id = author_id
        self.framework = framework
        self.image_provider_type = image_provider_type
        self.image_tag = image_tag
        self.image_url = image_url
        self.image_url_vpc = image_url_vpc

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerator_type is not None:
            result['AcceleratorType'] = self.accelerator_type

        if self.author_id is not None:
            result['AuthorId'] = self.author_id

        if self.framework is not None:
            result['Framework'] = self.framework

        if self.image_provider_type is not None:
            result['ImageProviderType'] = self.image_provider_type

        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.image_url_vpc is not None:
            result['ImageUrlVpc'] = self.image_url_vpc

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorType') is not None:
            self.accelerator_type = m.get('AcceleratorType')

        if m.get('AuthorId') is not None:
            self.author_id = m.get('AuthorId')

        if m.get('Framework') is not None:
            self.framework = m.get('Framework')

        if m.get('ImageProviderType') is not None:
            self.image_provider_type = m.get('ImageProviderType')

        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('ImageUrlVpc') is not None:
            self.image_url_vpc = m.get('ImageUrlVpc')

        return self

