# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import BinaryIO

from darabonba.model import DaraModel

class CreateDocParserJobAdvanceRequest(DaraModel):
    def __init__(
        self,
        file_format: str = None,
        file_name: str = None,
        file_url_object: BinaryIO = None,
        output_format: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.file_format = file_format
        # This parameter is required.
        self.file_name = file_name
        # This parameter is required.
        self.file_url_object = file_url_object
        # This parameter is required.
        self.output_format = output_format
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_format is not None:
            result['FileFormat'] = self.file_format

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_url_object is not None:
            result['FileUrl'] = self.file_url_object

        if self.output_format is not None:
            result['OutputFormat'] = self.output_format

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileFormat') is not None:
            self.file_format = m.get('FileFormat')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileUrl') is not None:
            self.file_url_object = m.get('FileUrl')

        if m.get('OutputFormat') is not None:
            self.output_format = m.get('OutputFormat')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

