# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quickbi_public20220101 import models as main_models
from darabonba.model import DaraModel

class QueryShareListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.QueryShareListResponseBodyResult] = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # Returns the list of objects to which the work has been shared.
        self.result = result
        # Indicates whether the request was successful. Possible values:
        # 
        # - true: The request was successful.
        # - false: The request failed.
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
                temp_model = main_models.QueryShareListResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryShareListResponseBodyResult(DaraModel):
    def __init__(
        self,
        auth_point: int = None,
        expire_date: int = None,
        report_id: str = None,
        share_id: str = None,
        share_to_id: str = None,
        share_to_name: str = None,
        share_to_type: int = None,
        share_type: str = None,
    ):
        # Sharing permissions. Possible values:
        # 
        # - 1: View only
        # - 3: View and export
        self.auth_point = auth_point
        # The timestamp in milliseconds indicating the expiration time of the authorization.
        self.expire_date = expire_date
        # The ID of the work.
        self.report_id = report_id
        # The ID of the sharing configuration.
        self.share_id = share_id
        # The ID of the sharing target, which could be a user ID or a group ID in Quick BI.
        # 
        # - When ShareToType=2 (all members within an organization), ShareToId is the organization ID.
        self.share_to_id = share_to_id
        # The name of the sharing target.
        self.share_to_name = share_to_name
        # The type of sharing. Possible values:
        # 
        # - 0: User
        # - 1: Group
        # - 2: Organization
        # - 3: Space
        self.share_to_type = share_to_type
        # The type of the shared work. The value range includes: 
        # - dataProduct: Data Portal 
        # - dashboard: Dashboard 
        # - report: Spreadsheet 
        # - dashboardOfflineQuery: Self-service Data Extraction 
        # - ANALYSIS: Ad-hoc Analysis 
        # - DATAFORM: Data Entry 
        # - SCREEN: Data Visualization Screen
        self.share_type = share_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_point is not None:
            result['AuthPoint'] = self.auth_point

        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date

        if self.report_id is not None:
            result['ReportId'] = self.report_id

        if self.share_id is not None:
            result['ShareId'] = self.share_id

        if self.share_to_id is not None:
            result['ShareToId'] = self.share_to_id

        if self.share_to_name is not None:
            result['ShareToName'] = self.share_to_name

        if self.share_to_type is not None:
            result['ShareToType'] = self.share_to_type

        if self.share_type is not None:
            result['ShareType'] = self.share_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthPoint') is not None:
            self.auth_point = m.get('AuthPoint')

        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')

        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')

        if m.get('ShareId') is not None:
            self.share_id = m.get('ShareId')

        if m.get('ShareToId') is not None:
            self.share_to_id = m.get('ShareToId')

        if m.get('ShareToName') is not None:
            self.share_to_name = m.get('ShareToName')

        if m.get('ShareToType') is not None:
            self.share_to_type = m.get('ShareToType')

        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')

        return self

