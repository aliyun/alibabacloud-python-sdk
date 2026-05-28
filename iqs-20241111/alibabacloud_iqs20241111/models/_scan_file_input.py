# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_iqs20241111 import models as main_models
from darabonba.model import DaraModel

class ScanFileInput(DaraModel):
    def __init__(
        self,
        image_base_64: str = None,
        image_url: str = None,
        scan_file_input_config: main_models.ScanFileInputConfig = None,
    ):
        self.image_base_64 = image_base_64
        self.image_url = image_url
        self.scan_file_input_config = scan_file_input_config

    def validate(self):
        if self.scan_file_input_config:
            self.scan_file_input_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_base_64 is not None:
            result['imageBase64'] = self.image_base_64

        if self.image_url is not None:
            result['imageUrl'] = self.image_url

        if self.scan_file_input_config is not None:
            result['scanFileInputConfig'] = self.scan_file_input_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('imageBase64') is not None:
            self.image_base_64 = m.get('imageBase64')

        if m.get('imageUrl') is not None:
            self.image_url = m.get('imageUrl')

        if m.get('scanFileInputConfig') is not None:
            temp_model = main_models.ScanFileInputConfig()
            self.scan_file_input_config = temp_model.from_map(m.get('scanFileInputConfig'))

        return self

