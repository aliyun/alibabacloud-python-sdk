# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateVodTemplateRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        template_config: str = None,
        vod_template_id: str = None,
    ):
        # The name of the template.
        # 
        # *   The name can be up to 128 bytes in length.
        # *   The value must be encoded in UTF-8.
        self.name = name
        # The configurations of the snapshot template. The value is a JSON-formatted string. For more information about the data structure, see the "SnapshotTemplateConfig" section of the [Media processing parameters](https://help.aliyun.com/document_detail/98618.html) topic.
        self.template_config = template_config
        # The ID of the snapshot template.
        # 
        # This parameter is required.
        self.vod_template_id = vod_template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.template_config is not None:
            result['TemplateConfig'] = self.template_config

        if self.vod_template_id is not None:
            result['VodTemplateId'] = self.vod_template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('TemplateConfig') is not None:
            self.template_config = m.get('TemplateConfig')

        if m.get('VodTemplateId') is not None:
            self.vod_template_id = m.get('VodTemplateId')

        return self

