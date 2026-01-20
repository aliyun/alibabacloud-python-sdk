# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_paifeaturestore20230621 import models as main_models
from darabonba.model import DaraModel

class WriteFeatureViewTableRequest(DaraModel):
    def __init__(
        self,
        mode: str = None,
        partitions: Dict[str, dict] = None,
        url_datasource: main_models.WriteFeatureViewTableRequestUrlDatasource = None,
    ):
        # This parameter is required.
        self.mode = mode
        self.partitions = partitions
        self.url_datasource = url_datasource

    def validate(self):
        if self.url_datasource:
            self.url_datasource.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mode is not None:
            result['Mode'] = self.mode

        if self.partitions is not None:
            result['Partitions'] = self.partitions

        if self.url_datasource is not None:
            result['UrlDatasource'] = self.url_datasource.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Partitions') is not None:
            self.partitions = m.get('Partitions')

        if m.get('UrlDatasource') is not None:
            temp_model = main_models.WriteFeatureViewTableRequestUrlDatasource()
            self.url_datasource = temp_model.from_map(m.get('UrlDatasource'))

        return self

class WriteFeatureViewTableRequestUrlDatasource(DaraModel):
    def __init__(
        self,
        delimiter: str = None,
        omit_header: bool = None,
        path: str = None,
    ):
        self.delimiter = delimiter
        self.omit_header = omit_header
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delimiter is not None:
            result['Delimiter'] = self.delimiter

        if self.omit_header is not None:
            result['OmitHeader'] = self.omit_header

        if self.path is not None:
            result['Path'] = self.path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Delimiter') is not None:
            self.delimiter = m.get('Delimiter')

        if m.get('OmitHeader') is not None:
            self.omit_header = m.get('OmitHeader')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        return self

