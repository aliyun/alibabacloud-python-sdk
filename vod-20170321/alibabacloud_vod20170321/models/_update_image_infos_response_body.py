# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class UpdateImageInfosResponseBody(DaraModel):
    def __init__(
        self,
        non_exist_image_ids: main_models.UpdateImageInfosResponseBodyNonExistImageIds = None,
        request_id: str = None,
    ):
        self.non_exist_image_ids = non_exist_image_ids
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.non_exist_image_ids:
            self.non_exist_image_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.non_exist_image_ids is not None:
            result['NonExistImageIds'] = self.non_exist_image_ids.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NonExistImageIds') is not None:
            temp_model = main_models.UpdateImageInfosResponseBodyNonExistImageIds()
            self.non_exist_image_ids = temp_model.from_map(m.get('NonExistImageIds'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class UpdateImageInfosResponseBodyNonExistImageIds(DaraModel):
    def __init__(
        self,
        image_id: List[str] = None,
    ):
        self.image_id = image_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_id is not None:
            result['ImageId'] = self.image_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        return self

