# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitConvertPdfToWordJobRequest(DaraModel):
    def __init__(
        self,
        file_name: str = None,
        file_url: str = None,
        force_export_inner_image: bool = None,
        formula_enhancement: bool = None,
        option: str = None,
        oss_bucket: str = None,
        oss_endpoint: str = None,
    ):
        self.file_name = file_name
        self.file_url = file_url
        self.force_export_inner_image = force_export_inner_image
        self.formula_enhancement = formula_enhancement
        self.option = option
        self.oss_bucket = oss_bucket
        self.oss_endpoint = oss_endpoint

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.force_export_inner_image is not None:
            result['ForceExportInnerImage'] = self.force_export_inner_image

        if self.formula_enhancement is not None:
            result['FormulaEnhancement'] = self.formula_enhancement

        if self.option is not None:
            result['Option'] = self.option

        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket

        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('ForceExportInnerImage') is not None:
            self.force_export_inner_image = m.get('ForceExportInnerImage')

        if m.get('FormulaEnhancement') is not None:
            self.formula_enhancement = m.get('FormulaEnhancement')

        if m.get('Option') is not None:
            self.option = m.get('Option')

        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')

        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')

        return self

