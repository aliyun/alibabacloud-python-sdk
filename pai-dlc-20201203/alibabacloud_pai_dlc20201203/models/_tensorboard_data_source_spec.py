# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TensorboardDataSourceSpec(DaraModel):
    def __init__(
        self,
        data_source_type: str = None,
        directory_name: str = None,
        full_summary_path: str = None,
        id: str = None,
        name: str = None,
        source_type: str = None,
        summary_path: str = None,
        uri: str = None,
    ):
        self.data_source_type = data_source_type
        self.directory_name = directory_name
        self.full_summary_path = full_summary_path
        self.id = id
        self.name = name
        self.source_type = source_type
        self.summary_path = summary_path
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type

        if self.directory_name is not None:
            result['DirectoryName'] = self.directory_name

        if self.full_summary_path is not None:
            result['FullSummaryPath'] = self.full_summary_path

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.summary_path is not None:
            result['SummaryPath'] = self.summary_path

        if self.uri is not None:
            result['Uri'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')

        if m.get('DirectoryName') is not None:
            self.directory_name = m.get('DirectoryName')

        if m.get('FullSummaryPath') is not None:
            self.full_summary_path = m.get('FullSummaryPath')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('SummaryPath') is not None:
            self.summary_path = m.get('SummaryPath')

        if m.get('Uri') is not None:
            self.uri = m.get('Uri')

        return self

