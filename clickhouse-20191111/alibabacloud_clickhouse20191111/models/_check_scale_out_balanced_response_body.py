# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_clickhouse20191111 import models as main_models
from darabonba.model import DaraModel

class CheckScaleOutBalancedResponseBody(DaraModel):
    def __init__(
        self,
        check_code: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        table_details: main_models.CheckScaleOutBalancedResponseBodyTableDetails = None,
        time_duration: str = None,
        total_count: int = None,
    ):
        # The check result. Valid values:
        # 
        # *   **400**: The cluster failed the check.
        # *   **200**: The cluster passed the check.
        self.check_code = check_code
        # The total number of returned pages.
        self.page_number = page_number
        # The number of entries returned per page. Valid values:
        # 
        # *   **30** (default)
        # *   **50**
        # *   **100**
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The error information returned for a check failure.
        self.table_details = table_details
        # The amount of time that is required for the migration and scale-out. Unit: minutes.
        self.time_duration = time_duration
        # The total number of entries that are returned.
        self.total_count = total_count

    def validate(self):
        if self.table_details:
            self.table_details.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_code is not None:
            result['CheckCode'] = self.check_code

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.table_details is not None:
            result['TableDetails'] = self.table_details.to_map()

        if self.time_duration is not None:
            result['TimeDuration'] = self.time_duration

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckCode') is not None:
            self.check_code = m.get('CheckCode')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TableDetails') is not None:
            temp_model = main_models.CheckScaleOutBalancedResponseBodyTableDetails()
            self.table_details = temp_model.from_map(m.get('TableDetails'))

        if m.get('TimeDuration') is not None:
            self.time_duration = m.get('TimeDuration')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class CheckScaleOutBalancedResponseBodyTableDetails(DaraModel):
    def __init__(
        self,
        table_detail: List[main_models.CheckScaleOutBalancedResponseBodyTableDetailsTableDetail] = None,
    ):
        self.table_detail = table_detail

    def validate(self):
        if self.table_detail:
            for v1 in self.table_detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TableDetail'] = []
        if self.table_detail is not None:
            for k1 in self.table_detail:
                result['TableDetail'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.table_detail = []
        if m.get('TableDetail') is not None:
            for k1 in m.get('TableDetail'):
                temp_model = main_models.CheckScaleOutBalancedResponseBodyTableDetailsTableDetail()
                self.table_detail.append(temp_model.from_map(k1))

        return self



class CheckScaleOutBalancedResponseBodyTableDetailsTableDetail(DaraModel):
    def __init__(
        self,
        cluster: str = None,
        database: str = None,
        detail: int = None,
        table_name: str = None,
    ):
        # The cluster. The value is fixed as **default**.
        self.cluster = cluster
        # The database name.
        self.database = database
        # The error details. Valid values:
        # 
        # *   **1**: The unique distributed table is missing.
        # *   **2**: More than one distributed table exists for the local table.
        self.detail = detail
        # The name of the local table.
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster is not None:
            result['Cluster'] = self.cluster

        if self.database is not None:
            result['Database'] = self.database

        if self.detail is not None:
            result['Detail'] = self.detail

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cluster') is not None:
            self.cluster = m.get('Cluster')

        if m.get('Database') is not None:
            self.database = m.get('Database')

        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

