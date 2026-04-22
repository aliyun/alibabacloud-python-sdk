# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribeInterAuthStatisticsZoneOverviewResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeInterAuthStatisticsZoneOverviewResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeInterAuthStatisticsZoneOverviewResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeInterAuthStatisticsZoneOverviewResponseBodyData(DaraModel):
    def __init__(
        self,
        refused_domain_count: int = None,
        sudden_drop_domain_count: int = None,
        sudden_increase_domain_count: int = None,
    ):
        self.refused_domain_count = refused_domain_count
        self.sudden_drop_domain_count = sudden_drop_domain_count
        self.sudden_increase_domain_count = sudden_increase_domain_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.refused_domain_count is not None:
            result['RefusedDomainCount'] = self.refused_domain_count

        if self.sudden_drop_domain_count is not None:
            result['SuddenDropDomainCount'] = self.sudden_drop_domain_count

        if self.sudden_increase_domain_count is not None:
            result['SuddenIncreaseDomainCount'] = self.sudden_increase_domain_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RefusedDomainCount') is not None:
            self.refused_domain_count = m.get('RefusedDomainCount')

        if m.get('SuddenDropDomainCount') is not None:
            self.sudden_drop_domain_count = m.get('SuddenDropDomainCount')

        if m.get('SuddenIncreaseDomainCount') is not None:
            self.sudden_increase_domain_count = m.get('SuddenIncreaseDomainCount')

        return self

