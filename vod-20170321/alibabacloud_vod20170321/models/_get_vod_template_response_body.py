# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class GetVodTemplateResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        vod_template_info: main_models.GetVodTemplateResponseBodyVodTemplateInfo = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information about the snapshot template.
        self.vod_template_info = vod_template_info

    def validate(self):
        if self.vod_template_info:
            self.vod_template_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.vod_template_info is not None:
            result['VodTemplateInfo'] = self.vod_template_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('VodTemplateInfo') is not None:
            temp_model = main_models.GetVodTemplateResponseBodyVodTemplateInfo()
            self.vod_template_info = temp_model.from_map(m.get('VodTemplateInfo'))

        return self

class GetVodTemplateResponseBodyVodTemplateInfo(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        is_default: str = None,
        modify_time: str = None,
        name: str = None,
        template_config: str = None,
        template_type: str = None,
        vod_template_id: str = None,
    ):
        # The time when the template was created. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.creation_time = creation_time
        # Indicates whether the template is the default one. Valid values:
        # 
        # *   **Default**: The template is the default one.
        # *   **NotDefault**: The template is not the default one.
        self.is_default = is_default
        # The time when the template was modified. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.modify_time = modify_time
        # The name of the template.
        self.name = name
        # The detailed configurations of the template. The value is a JSON-formatted string. For more information about the data structure, see the "SnapshotTemplateConfig" section of the [Media processing parameters](https://help.aliyun.com/document_detail/98618.html) topic.
        self.template_config = template_config
        # The type of the template. Valid values:
        # 
        # *   **Snapshot**
        # *   **DynamicImage**
        self.template_type = template_type
        # The ID of the template.
        self.vod_template_id = vod_template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.name is not None:
            result['Name'] = self.name

        if self.template_config is not None:
            result['TemplateConfig'] = self.template_config

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        if self.vod_template_id is not None:
            result['VodTemplateId'] = self.vod_template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('TemplateConfig') is not None:
            self.template_config = m.get('TemplateConfig')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        if m.get('VodTemplateId') is not None:
            self.vod_template_id = m.get('VodTemplateId')

        return self

