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
        # The application ID. Default value: **app-1000000**. For more information, see [Multi-application](https://help.aliyun.com/document_detail/113600.html).
        self.app_id = app_id
        # The template name.
        # 
        # - The name can be up to 128 bytes in length.
        # - UTF-8 encoded.
        # 
        # This parameter is required.
        self.name = name
        # The template configuration data in JSON format. For more information about the data structure, see [Snapshot template configuration](https://help.aliyun.com/document_detail/98618.html) or [Animated image template configuration](https://help.aliyun.com/document_detail/98618.html).
        # 
        # This parameter is required.
        self.template_config = template_config
        # The templatetype. Valid values:
        # - **Snapshot**: snapshot.
        # - **DynamicImage**: animated image.
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

