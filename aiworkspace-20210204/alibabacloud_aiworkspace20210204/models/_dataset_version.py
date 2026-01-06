# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class DatasetVersion(DaraModel):
    def __init__(
        self,
        data_count: int = None,
        data_size: int = None,
        data_source_type: str = None,
        description: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        import_info: str = None,
        labels: List[main_models.Label] = None,
        mount_access: str = None,
        options: str = None,
        property: str = None,
        source_id: str = None,
        source_type: str = None,
        uri: str = None,
        version_name: str = None,
    ):
        self.data_count = data_count
        self.data_size = data_size
        self.data_source_type = data_source_type
        self.description = description
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.import_info = import_info
        self.labels = labels
        self.mount_access = mount_access
        self.options = options
        self.property = property
        self.source_id = source_id
        self.source_type = source_type
        self.uri = uri
        self.version_name = version_name

    def validate(self):
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_count is not None:
            result['DataCount'] = self.data_count

        if self.data_size is not None:
            result['DataSize'] = self.data_size

        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type

        if self.description is not None:
            result['Description'] = self.description

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.import_info is not None:
            result['ImportInfo'] = self.import_info

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        if self.mount_access is not None:
            result['MountAccess'] = self.mount_access

        if self.options is not None:
            result['Options'] = self.options

        if self.property is not None:
            result['Property'] = self.property

        if self.source_id is not None:
            result['SourceId'] = self.source_id

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.uri is not None:
            result['Uri'] = self.uri

        if self.version_name is not None:
            result['VersionName'] = self.version_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataCount') is not None:
            self.data_count = m.get('DataCount')

        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')

        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('ImportInfo') is not None:
            self.import_info = m.get('ImportInfo')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.Label()
                self.labels.append(temp_model.from_map(k1))

        if m.get('MountAccess') is not None:
            self.mount_access = m.get('MountAccess')

        if m.get('Options') is not None:
            self.options = m.get('Options')

        if m.get('Property') is not None:
            self.property = m.get('Property')

        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('Uri') is not None:
            self.uri = m.get('Uri')

        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')

        return self

