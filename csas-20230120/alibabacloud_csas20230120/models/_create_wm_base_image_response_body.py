# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class CreateWmBaseImageResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.CreateWmBaseImageResponseBodyData = None,
        request_id: str = None,
    ):
        # The transparent image information.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.CreateWmBaseImageResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateWmBaseImageResponseBodyData(DaraModel):
    def __init__(
        self,
        image_id: str = None,
        image_url: str = None,
        image_url_exp: int = None,
    ):
        # The transparent image ID. The same ID indicates that the image content is identical.
        self.image_id = image_id
        # The temporary URL for downloading the image.
        self.image_url = image_url
        # The expiration time of the temporary image URL, in UNIX timestamp format. Unit: seconds.
        self.image_url_exp = image_url_exp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.image_url_exp is not None:
            result['ImageUrlExp'] = self.image_url_exp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('ImageUrlExp') is not None:
            self.image_url_exp = m.get('ImageUrlExp')

        return self

