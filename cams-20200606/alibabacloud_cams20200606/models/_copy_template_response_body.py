# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cams20200606 import models as main_models
from darabonba.model import DaraModel

class CopyTemplateResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.CopyTemplateResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

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
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.CopyTemplateResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CopyTemplateResponseBodyData(DaraModel):
    def __init__(
        self,
        scene_template_code: str = None,
        scene_template_name: str = None,
        whatsapp_catagory: str = None,
    ):
        self.scene_template_code = scene_template_code
        self.scene_template_name = scene_template_name
        self.whatsapp_catagory = whatsapp_catagory

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.scene_template_code is not None:
            result['SceneTemplateCode'] = self.scene_template_code

        if self.scene_template_name is not None:
            result['SceneTemplateName'] = self.scene_template_name

        if self.whatsapp_catagory is not None:
            result['WhatsappCatagory'] = self.whatsapp_catagory

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneTemplateCode') is not None:
            self.scene_template_code = m.get('SceneTemplateCode')

        if m.get('SceneTemplateName') is not None:
            self.scene_template_name = m.get('SceneTemplateName')

        if m.get('WhatsappCatagory') is not None:
            self.whatsapp_catagory = m.get('WhatsappCatagory')

        return self

