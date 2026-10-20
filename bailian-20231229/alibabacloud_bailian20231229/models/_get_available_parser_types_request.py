# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAvailableParserTypesRequest(DaraModel):
    def __init__(
        self,
        file_type: str = None,
    ):
        # The file type (extension) for which to retrieve supported parsers. Valid values: 
        # - doc
        # - docx
        # - ppt
        # - pptx
        # - xls
        # - xlsx
        # - md
        # - txt
        # - pdf
        # - png
        # - jpg
        # - jpeg
        # - bmp
        # - gif
        # - html
        # 
        # This parameter is required.
        self.file_type = file_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_type is not None:
            result['FileType'] = self.file_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')

        return self

