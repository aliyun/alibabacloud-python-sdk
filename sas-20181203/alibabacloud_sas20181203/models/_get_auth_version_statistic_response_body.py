# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetAuthVersionStatisticResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        statistics: List[main_models.GetAuthVersionStatisticResponseBodyStatistics] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The statistics about the numbers of assets protected by each edition of Security Center.
        self.statistics = statistics

    def validate(self):
        if self.statistics:
            for v1 in self.statistics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Statistics'] = []
        if self.statistics is not None:
            for k1 in self.statistics:
                result['Statistics'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.statistics = []
        if m.get('Statistics') is not None:
            for k1 in m.get('Statistics'):
                temp_model = main_models.GetAuthVersionStatisticResponseBodyStatistics()
                self.statistics.append(temp_model.from_map(k1))

        return self

class GetAuthVersionStatisticResponseBodyStatistics(DaraModel):
    def __init__(
        self,
        auth_version: int = None,
        count: int = None,
    ):
        # The edition of Security Center. Valid values:
        # 
        # *   **1**: Basic edition (Unauthorized)
        # *   **6**: Anti-virus edition
        # *   **5**: Advanced edition
        # *   **3**: Enterprise edition
        # *   **7**: Ultimate edition
        # *   **10**: Value-added Plan edition
        self.auth_version = auth_version
        # The number of authorized servers.
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_version is not None:
            result['AuthVersion'] = self.auth_version

        if self.count is not None:
            result['Count'] = self.count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthVersion') is not None:
            self.auth_version = m.get('AuthVersion')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        return self

