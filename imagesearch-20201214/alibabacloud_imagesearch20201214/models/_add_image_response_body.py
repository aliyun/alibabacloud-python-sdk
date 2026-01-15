# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_imagesearch20201214 import models as main_models
from darabonba.model import DaraModel

class AddImageResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        pic_info: main_models.AddImageResponseBodyPicInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The code returned.
        # 
        # *   A value of 0 indicates that the request was successful.
        # *   Values other than 0 indicate that the request failed.
        self.code = code
        # The error message returned if the request failed.
        # 
        # > No value is returned if the request was successful, and an error message is returned if the request failed.
        self.message = message
        # The results of category prediction and subject identification.
        self.pic_info = pic_info
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.pic_info:
            self.pic_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.pic_info is not None:
            result['PicInfo'] = self.pic_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PicInfo') is not None:
            temp_model = main_models.AddImageResponseBodyPicInfo()
            self.pic_info = temp_model.from_map(m.get('PicInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self



class AddImageResponseBodyPicInfo(DaraModel):
    def __init__(
        self,
        category_id: int = None,
        region: str = None,
    ):
        # The result of category prediction. If a category is specified in the request, the specified category prevails.
        self.category_id = category_id
        # The result of subject identification. The subject area of the image is in the format of `x1,x2,y1,y2`. `x1 and y1` represent the position in the upper-left corner, in pixels. `x2 and y2` represent the position in the lower-right corner, in pixels. If a subject area is specified in the request, the specified subject area prevails.
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.region is not None:
            result['Region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        return self

