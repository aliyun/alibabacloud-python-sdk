# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateImageRequest(DaraModel):
    def __init__(
        self,
        adaptor_id_list: List[str] = None,
        description: str = None,
        distro: str = None,
        image_id: str = None,
        image_name: str = None,
        language: str = None,
        version_id: str = None,
        version_name: str = None,
    ):
        # The complete list of application adapter IDs for the selected image version. A maximum of 100 items are supported. **When a non-empty list is passed, it must include the adapters that you still want to retain. Omitting this parameter or passing an empty list does not clear the existing associations.**
        self.adaptor_id_list = adaptor_id_list
        # The updated description of the image.
        self.description = description
        # The operating system distribution information of the image. This must be consistent with the actual operating system distribution of the image.
        self.distro = distro
        # The ID of the image to be modified. You must provide at least one of ImageId and VersionId. If both are provided, they must belong to the same image.
        self.image_id = image_id
        # The new name of the image. Specify this parameter only when you need to update the name.
        self.image_name = image_name
        # The language of the image. Valid values:
        # 
        # - **zh-CN**: Simplified Chinese.
        # - **zh-HK**: Traditional Chinese (Hong Kong).
        # - **en-US**: English.
        # - **ja-JP**: Japanese.
        # - **CN**: A compatible value for Simplified Chinese.
        # - **EN**: A compatible value for English.
        # - **JP**: A compatible value for Japanese.
        # - **CN-HK**: A compatible value for Traditional Chinese (Hong Kong).
        self.language = language
        # The ID of the image version to be modified. If this parameter is omitted, the current effective version of the image specified by ImageId is used. You must provide at least one of ImageId and VersionId.
        self.version_id = version_id
        # The new display name of the image version.
        self.version_name = version_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adaptor_id_list is not None:
            result['AdaptorIdList'] = self.adaptor_id_list

        if self.description is not None:
            result['Description'] = self.description

        if self.distro is not None:
            result['Distro'] = self.distro

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        if self.language is not None:
            result['Language'] = self.language

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        if self.version_name is not None:
            result['VersionName'] = self.version_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdaptorIdList') is not None:
            self.adaptor_id_list = m.get('AdaptorIdList')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Distro') is not None:
            self.distro = m.get('Distro')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')

        return self

