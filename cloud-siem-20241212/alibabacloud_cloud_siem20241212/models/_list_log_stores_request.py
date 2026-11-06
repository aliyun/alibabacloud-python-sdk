# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListLogStoresRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        log_project_name: str = None,
        log_region_id: str = None,
        log_user_id: int = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        # The language of the response message. Valid values:
        # - **zh** (default): Chinese.
        # - **en**: English.
        # Note: This parameter is actually required. If it is not provided, the API returns a 400 error (The specified Lang can not be empty.).
        self.lang = lang
        # The name of the Simple Log Service project. The project name follows the naming convention aliyun-cloudsiem-data-{userId}-{regionId}. You can call the GetDataStorage operation and obtain a valid project name from the Data.LogProject field in the response. This parameter is actually required. You can call the GetDataStorage operation to obtain valid values.
        self.log_project_name = log_project_name
        # The log storage region ID. This parameter is required when LogProjectName is provided, and the log storage region must match the log project. You can call the GetDataStorage operation to obtain valid values.
        self.log_region_id = log_region_id
        # The ID of the data ingestion user.
        self.log_user_id = log_user_id
        # The maximum number of data entries to return in this request.
        self.max_results = max_results
        # The token for the next query. You do not need to specify this parameter for the first query or when no subsequent query is required. If a subsequent query is required, set the value to the NextToken value returned by the previous API call.
        self.next_token = next_token
        # The region of the data management center for threat analysis. Select the region of the management center based on the region where your assets are located. Valid values:
        # - cn-hangzhou: The assets are located in the Chinese mainland.
        # - ap-southeast-1: The assets are located outside the Chinese mainland.
        self.region_id = region_id
        # The ID of the user whose perspective the administrator switches to.
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.log_project_name is not None:
            result['LogProjectName'] = self.log_project_name

        if self.log_region_id is not None:
            result['LogRegionId'] = self.log_region_id

        if self.log_user_id is not None:
            result['LogUserId'] = self.log_user_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('LogProjectName') is not None:
            self.log_project_name = m.get('LogProjectName')

        if m.get('LogRegionId') is not None:
            self.log_region_id = m.get('LogRegionId')

        if m.get('LogUserId') is not None:
            self.log_user_id = m.get('LogUserId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        return self

