# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddVodTemplateRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        name: str = None,
        template_config: str = None,
        template_type: str = None,
    ):
        # The ID of the application. Default value: **app-1000000**. For more information, see [Multi-application service](https://help.aliyun.com/document_detail/113600.html).
        self.app_id = app_id
        # The name of the template.
        # 
        # *   The name cannot exceed 128 bytes.
        # *   The value must be encoded in UTF-8.
        # 
        # This parameter is required.
        self.name = name
        # The configurations of the snapshot template. The value must be a JSON string. For more information about the data structure, see [SnapshotTemplateConfig](https://help.aliyun.com/document_detail/98618.html) and [DynamicImageTemplateConfig](https://help.aliyun.com/document_detail/98618.html).
        # 
        # This parameter is required.
        self.template_config = template_config
        # The type of the template. Set the value to **Snapshot**.
        # 
        # This parameter is required.
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.name is not None:
            result['Name'] = self.name

        if self.template_config is not None:
            result['TemplateConfig'] = self.template_config

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('TemplateConfig') is not None:
            self.template_config = m.get('TemplateConfig')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        return self

