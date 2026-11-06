# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UnbindAppRequest(DaraModel):
    def __init__(
        self,
        app_id_list: List[str] = None,
        image_id: str = None,
        version_id: str = None,
    ):
        # The list of application IDs to dissociate from the specified image version. Verify that each application is associated with the selected image version.
        # 
        # This parameter is required.
        self.app_id_list = app_id_list
        # The ID of the image from which to dissociate the applications. The image must be a custom image or a community image that the current account can manage.
        # 
        # This parameter is required.
        self.image_id = image_id
        # The ID of the image version from which to dissociate the applications. If you omit this parameter, the current effective version of the image is used. If you specify this parameter, it must belong to the image specified by ImageId.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id_list is not None:
            result['AppIdList'] = self.app_id_list

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppIdList') is not None:
            self.app_id_list = m.get('AppIdList')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        return self

