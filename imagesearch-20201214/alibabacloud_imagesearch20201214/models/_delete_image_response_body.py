# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imagesearch20201214 import models as main_models
from darabonba.model import DaraModel

class DeleteImageResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.DeleteImageResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code returned.
        # 
        # *   A value of 0 indicates that the operation is successful.
        # *   Values other than 0 indicate errors.
        self.code = code
        # The information about the deleted images.
        self.data = data
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DeleteImageResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DeleteImageResponseBodyData(DaraModel):
    def __init__(
        self,
        pic_names: List[str] = None,
    ):
        # The name (PicName) of the deleted image.
        self.pic_names = pic_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pic_names is not None:
            result['PicNames'] = self.pic_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PicNames') is not None:
            self.pic_names = m.get('PicNames')

        return self

