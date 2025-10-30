# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class DescribeIMVInfosResponseBody(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        imv_infos: List[main_models.DescribeIMVInfosResponseBodyImvInfos] = None,
        request_id: str = None,
    ):
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        self.dbinstance_id = dbinstance_id
        # The queried materialized views.
        self.imv_infos = imv_infos
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.imv_infos:
            for v1 in self.imv_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        result['ImvInfos'] = []
        if self.imv_infos is not None:
            for k1 in self.imv_infos:
                result['ImvInfos'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        self.imv_infos = []
        if m.get('ImvInfos') is not None:
            for k1 in m.get('ImvInfos'):
                temp_model = main_models.DescribeIMVInfosResponseBodyImvInfos()
                self.imv_infos.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeIMVInfosResponseBodyImvInfos(DaraModel):
    def __init__(
        self,
        base: str = None,
        detail_info: str = None,
        mv: str = None,
    ):
        # The name of the table based on which the materialized view is created.
        self.base = base
        # The dependency between the materialized view and the base table and all metric values, which can be used to build a lineage graph.
        self.detail_info = detail_info
        # The name of the materialized view.
        self.mv = mv

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.base is not None:
            result['Base'] = self.base

        if self.detail_info is not None:
            result['DetailInfo'] = self.detail_info

        if self.mv is not None:
            result['MV'] = self.mv

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Base') is not None:
            self.base = m.get('Base')

        if m.get('DetailInfo') is not None:
            self.detail_info = m.get('DetailInfo')

        if m.get('MV') is not None:
            self.mv = m.get('MV')

        return self

