# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class ListRelatedResourceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListRelatedResourceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code. This field is returned when the request fails. A successful response may not contain this field.
        self.code = code
        # The returned data object.
        self.data = data
        # The description of the request processing result. The value `success` is typically returned when the request is successful.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. A value of true indicates that the request is successful, and a value of false indicates that the request fails.
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
            temp_model = main_models.ListRelatedResourceResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListRelatedResourceResponseBodyData(DaraModel):
    def __init__(
        self,
        desktop_count: int = None,
        desktop_group_count: int = None,
        template_count: int = None,
    ):
        # The number of cloud desktops associated with the image.
        self.desktop_count = desktop_count
        # The number of cloud desktop pools associated with the image.
        self.desktop_group_count = desktop_group_count
        # The number of associated templates.
        self.template_count = template_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desktop_count is not None:
            result['DesktopCount'] = self.desktop_count

        if self.desktop_group_count is not None:
            result['DesktopGroupCount'] = self.desktop_group_count

        if self.template_count is not None:
            result['TemplateCount'] = self.template_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopCount') is not None:
            self.desktop_count = m.get('DesktopCount')

        if m.get('DesktopGroupCount') is not None:
            self.desktop_group_count = m.get('DesktopGroupCount')

        if m.get('TemplateCount') is not None:
            self.template_count = m.get('TemplateCount')

        return self

