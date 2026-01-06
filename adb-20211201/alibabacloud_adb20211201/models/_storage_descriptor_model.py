# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class StorageDescriptorModel(DaraModel):
    def __init__(
        self,
        compressed: bool = None,
        input_format: str = None,
        location: str = None,
        num_buckets: int = None,
        output_format: str = None,
        parameters: Dict[str, str] = None,
        sd_id: int = None,
        ser_de_info: main_models.SerDeInfoModel = None,
        stored_as_sub_directories: bool = None,
    ):
        self.compressed = compressed
        self.input_format = input_format
        self.location = location
        self.num_buckets = num_buckets
        self.output_format = output_format
        self.parameters = parameters
        self.sd_id = sd_id
        self.ser_de_info = ser_de_info
        self.stored_as_sub_directories = stored_as_sub_directories

    def validate(self):
        if self.ser_de_info:
            self.ser_de_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compressed is not None:
            result['Compressed'] = self.compressed

        if self.input_format is not None:
            result['InputFormat'] = self.input_format

        if self.location is not None:
            result['Location'] = self.location

        if self.num_buckets is not None:
            result['NumBuckets'] = self.num_buckets

        if self.output_format is not None:
            result['OutputFormat'] = self.output_format

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.sd_id is not None:
            result['SdId'] = self.sd_id

        if self.ser_de_info is not None:
            result['SerDeInfo'] = self.ser_de_info.to_map()

        if self.stored_as_sub_directories is not None:
            result['StoredAsSubDirectories'] = self.stored_as_sub_directories

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Compressed') is not None:
            self.compressed = m.get('Compressed')

        if m.get('InputFormat') is not None:
            self.input_format = m.get('InputFormat')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        if m.get('NumBuckets') is not None:
            self.num_buckets = m.get('NumBuckets')

        if m.get('OutputFormat') is not None:
            self.output_format = m.get('OutputFormat')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('SdId') is not None:
            self.sd_id = m.get('SdId')

        if m.get('SerDeInfo') is not None:
            temp_model = main_models.SerDeInfoModel()
            self.ser_de_info = temp_model.from_map(m.get('SerDeInfo'))

        if m.get('StoredAsSubDirectories') is not None:
            self.stored_as_sub_directories = m.get('StoredAsSubDirectories')

        return self

