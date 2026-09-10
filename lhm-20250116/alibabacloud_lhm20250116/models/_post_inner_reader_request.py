# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_lhm20250116 import models as main_models
from darabonba.model import DaraModel

class PostInnerReaderRequest(DaraModel):
    def __init__(
        self,
        data_source_descriptor: main_models.PostInnerReaderRequestDataSourceDescriptor = None,
        data_source_name: str = None,
    ):
        self.data_source_descriptor = data_source_descriptor
        self.data_source_name = data_source_name

    def validate(self):
        if self.data_source_descriptor:
            self.data_source_descriptor.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_source_descriptor is not None:
            result['dataSourceDescriptor'] = self.data_source_descriptor.to_map()

        if self.data_source_name is not None:
            result['dataSourceName'] = self.data_source_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataSourceDescriptor') is not None:
            temp_model = main_models.PostInnerReaderRequestDataSourceDescriptor()
            self.data_source_descriptor = temp_model.from_map(m.get('dataSourceDescriptor'))

        if m.get('dataSourceName') is not None:
            self.data_source_name = m.get('dataSourceName')

        return self

class PostInnerReaderRequestDataSourceDescriptor(DaraModel):
    def __init__(
        self,
        ds_name: str = None,
    ):
        self.ds_name = ds_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ds_name is not None:
            result['dsName'] = self.ds_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dsName') is not None:
            self.ds_name = m.get('dsName')

        return self

