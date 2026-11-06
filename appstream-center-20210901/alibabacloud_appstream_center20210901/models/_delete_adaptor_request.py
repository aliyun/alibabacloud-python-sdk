# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAdaptorRequest(DaraModel):
    def __init__(
        self,
        adaptor_id: str = None,
        app_id: str = None,
        app_version_id: str = None,
        image_id: str = None,
        version_id: str = None,
    ):
        # The ID of the application adapter to process. **Required**. It must correspond to the same application adapter as AppId and AppVersionId.
        self.adaptor_id = adaptor_id
        # The ID of the application. **Required**. It must correspond to the same application as AdaptorId.
        self.app_id = app_id
        # The ID of the application version. **Required**. It must correspond to the same application version as AdaptorId. This parameter is not the image version ID.
        self.app_version_id = app_version_id
        # The ID of the image to dissociate. **Must be provided together with VersionId**. If both parameters are not specified at the same time, the adapter deletion process is initiated.
        self.image_id = image_id
        # The ID of the image version to dissociate. It must be provided together with ImageId and belong to the specified image.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adaptor_id is not None:
            result['AdaptorId'] = self.adaptor_id

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdaptorId') is not None:
            self.adaptor_id = m.get('AdaptorId')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        return self

