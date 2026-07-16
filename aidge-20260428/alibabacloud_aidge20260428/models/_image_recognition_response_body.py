# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_aidge20260428 import models as main_models
from darabonba.model import DaraModel

class ImageRecognitionResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ImageRecognitionResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code. This parameter is not returned if the call is successful.
        self.code = code
        # The intelligent element recognition result.
        self.data = data
        # The error message. This parameter is not returned if the call is successful.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the call is successful.
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
            temp_model = main_models.ImageRecognitionResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ImageRecognitionResponseBodyData(DaraModel):
    def __init__(
        self,
        border_pixel: str = None,
        noobj_character: bool = None,
        noobj_logo: bool = None,
        noobj_npx: bool = None,
        noobj_watermark: bool = None,
        obj_character: bool = None,
        obj_logo: bool = None,
        obj_npx: bool = None,
        obj_watermark: bool = None,
        pd_num: int = None,
        pd_prop: str = None,
        rec_text: List[str] = None,
        text_prop: str = None,
        usage_map: Dict[str, int] = None,
    ):
        # The border pixel information, returned as a comma-separated string.
        self.border_pixel = border_pixel
        # Indicates whether the non-subject area contains text.
        self.noobj_character = noobj_character
        # Indicates whether the non-subject area contains a logo.
        self.noobj_logo = noobj_logo
        # Indicates whether the non-subject area contains irrelevant pixels or noise.
        self.noobj_npx = noobj_npx
        # Indicates whether the non-subject area contains a watermark.
        self.noobj_watermark = noobj_watermark
        # Indicates whether the subject area contains text.
        self.obj_character = obj_character
        # Indicates whether the subject area contains a logo.
        self.obj_logo = obj_logo
        # Indicates whether the subject area contains irrelevant pixels or noise.
        self.obj_npx = obj_npx
        # Indicates whether the subject area contains a watermark.
        self.obj_watermark = obj_watermark
        # The product count.
        self.pd_num = pd_num
        # The product proportion.
        self.pd_prop = pd_prop
        # The list of recognized text.
        self.rec_text = rec_text
        # The text proportion.
        self.text_prop = text_prop
        # The usage information.
        self.usage_map = usage_map

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.border_pixel is not None:
            result['BorderPixel'] = self.border_pixel

        if self.noobj_character is not None:
            result['NoobjCharacter'] = self.noobj_character

        if self.noobj_logo is not None:
            result['NoobjLogo'] = self.noobj_logo

        if self.noobj_npx is not None:
            result['NoobjNpx'] = self.noobj_npx

        if self.noobj_watermark is not None:
            result['NoobjWatermark'] = self.noobj_watermark

        if self.obj_character is not None:
            result['ObjCharacter'] = self.obj_character

        if self.obj_logo is not None:
            result['ObjLogo'] = self.obj_logo

        if self.obj_npx is not None:
            result['ObjNpx'] = self.obj_npx

        if self.obj_watermark is not None:
            result['ObjWatermark'] = self.obj_watermark

        if self.pd_num is not None:
            result['PdNum'] = self.pd_num

        if self.pd_prop is not None:
            result['PdProp'] = self.pd_prop

        if self.rec_text is not None:
            result['RecText'] = self.rec_text

        if self.text_prop is not None:
            result['TextProp'] = self.text_prop

        if self.usage_map is not None:
            result['UsageMap'] = self.usage_map

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BorderPixel') is not None:
            self.border_pixel = m.get('BorderPixel')

        if m.get('NoobjCharacter') is not None:
            self.noobj_character = m.get('NoobjCharacter')

        if m.get('NoobjLogo') is not None:
            self.noobj_logo = m.get('NoobjLogo')

        if m.get('NoobjNpx') is not None:
            self.noobj_npx = m.get('NoobjNpx')

        if m.get('NoobjWatermark') is not None:
            self.noobj_watermark = m.get('NoobjWatermark')

        if m.get('ObjCharacter') is not None:
            self.obj_character = m.get('ObjCharacter')

        if m.get('ObjLogo') is not None:
            self.obj_logo = m.get('ObjLogo')

        if m.get('ObjNpx') is not None:
            self.obj_npx = m.get('ObjNpx')

        if m.get('ObjWatermark') is not None:
            self.obj_watermark = m.get('ObjWatermark')

        if m.get('PdNum') is not None:
            self.pd_num = m.get('PdNum')

        if m.get('PdProp') is not None:
            self.pd_prop = m.get('PdProp')

        if m.get('RecText') is not None:
            self.rec_text = m.get('RecText')

        if m.get('TextProp') is not None:
            self.text_prop = m.get('TextProp')

        if m.get('UsageMap') is not None:
            self.usage_map = m.get('UsageMap')

        return self

