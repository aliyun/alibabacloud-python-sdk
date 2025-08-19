# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AyncTradeDocumentPackageExtractSmartAppRequest(DaraModel):
    def __init__(
        self,
        custom_extraction_range: List[str] = None,
        file_name: str = None,
        file_url: str = None,
        option: str = None,
        template_name: str = None,
    ):
        self.custom_extraction_range = custom_extraction_range
        self.file_name = file_name
        # This parameter is required.
        self.file_url = file_url
        self.option = option
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_extraction_range is not None:
            result['CustomExtractionRange'] = self.custom_extraction_range

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.option is not None:
            result['Option'] = self.option

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomExtractionRange') is not None:
            self.custom_extraction_range = m.get('CustomExtractionRange')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('Option') is not None:
            self.option = m.get('Option')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        return self

