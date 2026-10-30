# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeApplicationRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_versions: str = None,
        level: str = None,
        out_detail_stat_params: str = None,
        resource_selector: str = None,
    ):
        # The ID of the application. You can obtain the ID by calling the ListApplications operation.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The business service version numbers of the application. Multiple values are supported and separated by commas (,). If you enter All, data of all versions is returned. By default, only data associated with the stable version number is returned.
        self.app_versions = app_versions
        # The regional statistical level of the application edge resources. Valid values:
        # 
        # - National: nationwide
        # - Big: region
        # - Middle: province
        # - Small: city
        # - RegionId: edge node
        # 
        # Default value: National.
        self.level = level
        # Specifies whether to return information about statistical resource instances and container pods. The value is a JSON string. By default, all information is returned.
        self.out_detail_stat_params = out_detail_stat_params
        # The resource filter conditions.
        self.resource_selector = resource_selector

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_versions is not None:
            result['AppVersions'] = self.app_versions

        if self.level is not None:
            result['Level'] = self.level

        if self.out_detail_stat_params is not None:
            result['OutDetailStatParams'] = self.out_detail_stat_params

        if self.resource_selector is not None:
            result['ResourceSelector'] = self.resource_selector

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppVersions') is not None:
            self.app_versions = m.get('AppVersions')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('OutDetailStatParams') is not None:
            self.out_detail_stat_params = m.get('OutDetailStatParams')

        if m.get('ResourceSelector') is not None:
            self.resource_selector = m.get('ResourceSelector')

        return self

