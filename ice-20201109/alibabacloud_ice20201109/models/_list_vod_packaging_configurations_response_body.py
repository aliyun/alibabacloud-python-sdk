# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class ListVodPackagingConfigurationsResponseBody(DaraModel):
    def __init__(
        self,
        packaging_configurations: List[main_models.VodPackagingConfiguration] = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        sort_by: str = None,
        total_count: int = None,
    ):
        # The packaging configurations.
        self.packaging_configurations = packaging_configurations
        # The page number. Default value: 1.
        self.page_no = page_no
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The sorting order of the packaging configurations based on the time when they were created. Valid values:
        # 
        # *   desc: descending order.
        # *   asc: ascending order.
        self.sort_by = sort_by
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.packaging_configurations:
            for v1 in self.packaging_configurations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PackagingConfigurations'] = []
        if self.packaging_configurations is not None:
            for k1 in self.packaging_configurations:
                result['PackagingConfigurations'].append(k1.to_map() if k1 else None)

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.packaging_configurations = []
        if m.get('PackagingConfigurations') is not None:
            for k1 in m.get('PackagingConfigurations'):
                temp_model = main_models.VodPackagingConfiguration()
                self.packaging_configurations.append(temp_model.from_map(k1))

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

