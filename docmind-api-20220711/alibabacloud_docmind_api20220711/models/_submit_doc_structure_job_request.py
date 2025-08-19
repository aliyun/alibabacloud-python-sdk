# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitDocStructureJobRequest(DaraModel):
    def __init__(
        self,
        allow_ppt_format: bool = None,
        file_name: str = None,
        file_name_extension: str = None,
        file_url: str = None,
        formula_enhancement: bool = None,
        oss_bucket: str = None,
        oss_endpoint: str = None,
        page_index: str = None,
        structure_type: str = None,
    ):
        self.allow_ppt_format = allow_ppt_format
        self.file_name = file_name
        self.file_name_extension = file_name_extension
        self.file_url = file_url
        self.formula_enhancement = formula_enhancement
        self.oss_bucket = oss_bucket
        self.oss_endpoint = oss_endpoint
        self.page_index = page_index
        self.structure_type = structure_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_ppt_format is not None:
            result['AllowPptFormat'] = self.allow_ppt_format

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_name_extension is not None:
            result['FileNameExtension'] = self.file_name_extension

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.formula_enhancement is not None:
            result['FormulaEnhancement'] = self.formula_enhancement

        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket

        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint

        if self.page_index is not None:
            result['PageIndex'] = self.page_index

        if self.structure_type is not None:
            result['StructureType'] = self.structure_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowPptFormat') is not None:
            self.allow_ppt_format = m.get('AllowPptFormat')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileNameExtension') is not None:
            self.file_name_extension = m.get('FileNameExtension')

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('FormulaEnhancement') is not None:
            self.formula_enhancement = m.get('FormulaEnhancement')

        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')

        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')

        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')

        if m.get('StructureType') is not None:
            self.structure_type = m.get('StructureType')

        return self

