# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Source(DaraModel):
    def __init__(
        self,
        arn: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        http_package_configurations: str = None,
        source_location_name: str = None,
        source_name: str = None,
        source_type: str = None,
        state: int = None,
    ):
        self.arn = arn
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.http_package_configurations = http_package_configurations
        self.source_location_name = source_location_name
        self.source_name = source_name
        self.source_type = source_type
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arn is not None:
            result['Arn'] = self.arn

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.http_package_configurations is not None:
            result['HttpPackageConfigurations'] = self.http_package_configurations

        if self.source_location_name is not None:
            result['SourceLocationName'] = self.source_location_name

        if self.source_name is not None:
            result['SourceName'] = self.source_name

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('HttpPackageConfigurations') is not None:
            self.http_package_configurations = m.get('HttpPackageConfigurations')

        if m.get('SourceLocationName') is not None:
            self.source_location_name = m.get('SourceLocationName')

        if m.get('SourceName') is not None:
            self.source_name = m.get('SourceName')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

