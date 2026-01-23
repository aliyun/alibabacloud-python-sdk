# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetRepoTagResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        digest: str = None,
        image_create: int = None,
        image_id: str = None,
        image_size: int = None,
        image_update: int = None,
        is_success: bool = None,
        request_id: str = None,
        status: str = None,
        tag: str = None,
    ):
        # The ID of the image.
        self.code = code
        # The size of the image. Unit: Bytes.
        self.digest = digest
        # crr-tquyps22md8p****
        self.image_create = image_create
        self.image_id = image_id
        # The number of milliseconds that have elapsed since the image was last updated.
        self.image_size = image_size
        # The ID of the request.
        self.image_update = image_update
        # The status of the image. Valid values:
        # 
        # *   `NORMAL`: The image is normal.
        # *   `DELETING`: The image is being deleted.
        self.is_success = is_success
        # 1.0
        self.request_id = request_id
        # The ID of the instance.
        self.status = status
        # The version of the repository.
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.digest is not None:
            result['Digest'] = self.digest

        if self.image_create is not None:
            result['ImageCreate'] = self.image_create

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_size is not None:
            result['ImageSize'] = self.image_size

        if self.image_update is not None:
            result['ImageUpdate'] = self.image_update

        if self.is_success is not None:
            result['IsSuccess'] = self.is_success

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.tag is not None:
            result['Tag'] = self.tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Digest') is not None:
            self.digest = m.get('Digest')

        if m.get('ImageCreate') is not None:
            self.image_create = m.get('ImageCreate')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageSize') is not None:
            self.image_size = m.get('ImageSize')

        if m.get('ImageUpdate') is not None:
            self.image_update = m.get('ImageUpdate')

        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        return self

