# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class MediaConvertOutputGroupConfig(DaraModel):
    def __init__(
        self,
        manifest_name: str = None,
        output_file_base: main_models.MediaObject = None,
        type: str = None,
    ):
        self.manifest_name = manifest_name
        self.output_file_base = output_file_base
        self.type = type

    def validate(self):
        if self.output_file_base:
            self.output_file_base.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.manifest_name is not None:
            result['ManifestName'] = self.manifest_name

        if self.output_file_base is not None:
            result['OutputFileBase'] = self.output_file_base.to_map()

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ManifestName') is not None:
            self.manifest_name = m.get('ManifestName')

        if m.get('OutputFileBase') is not None:
            temp_model = main_models.MediaObject()
            self.output_file_base = temp_model.from_map(m.get('OutputFileBase'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

