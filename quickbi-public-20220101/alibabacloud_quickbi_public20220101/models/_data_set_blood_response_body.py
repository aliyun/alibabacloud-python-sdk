# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quickbi_public20220101 import models as main_models
from darabonba.model import DaraModel

class DataSetBloodResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.DataSetBloodResponseBodyResult] = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Array of works.
        self.result = result
        # Indicates whether the request was successful. Possible values:
        # 
        # - true: Request succeeded
        # - false: Request failed
        self.success = success

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.DataSetBloodResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DataSetBloodResponseBodyResult(DaraModel):
    def __init__(
        self,
        works_id: str = None,
        works_type: str = None,
    ):
        # Work ID.
        self.works_id = works_id
        # Work types: - REPORT: 
        # - REPORT: Workbooks
        # - dashboardOfflineQuery: Downloads
        # - DASHBOARD: Dashboard
        # - ANALYSIS: Ad Hoc Analysis
        # - SCREEN: Visualization Screen
        # - PAGE: Old dashboard
        self.works_type = works_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.works_id is not None:
            result['WorksId'] = self.works_id

        if self.works_type is not None:
            result['WorksType'] = self.works_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WorksId') is not None:
            self.works_id = m.get('WorksId')

        if m.get('WorksType') is not None:
            self.works_type = m.get('WorksType')

        return self

