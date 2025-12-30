# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTemplateMaterialsRequest(DaraModel):
    def __init__(
        self,
        file_list: str = None,
        template_id: str = None,
    ):
        # The materials that you want to query.
        self.file_list = file_list
        # The template ID.
        # 
        # This parameter is required.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_list is not None:
            result['FileList'] = self.file_list

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileList') is not None:
            self.file_list = m.get('FileList')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

