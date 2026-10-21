# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteLogStoreRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        log_project_name: str = None,
        log_region_id: str = None,
        log_store_name: str = None,
        log_user_id: int = None,
        region_id: str = None,
        role_for: int = None,
    ):
        # The language of the response. Valid values:
        # - **zh** (default): Chinese.
        # - **en**: English.
        # > Note: This parameter is required in practice. If this parameter is not specified, the API returns a 400 error: "The specified Lang can not be empty."
        self.lang = lang
        # The Simple Log Service project name.
        # > Note: This parameter is required in practice. If this parameter is not specified, the API returns a 400 error: "SLS log project name is empty."
        self.log_project_name = log_project_name
        # The log storage region ID.
        self.log_region_id = log_region_id
        # The Simple Log Service LogStore name.
        self.log_store_name = log_store_name
        # The user ID for data access.
        self.log_user_id = log_user_id
        # The region where the Cloud Threat Detection and Response (CTDR) data management center is located. Specify the management center based on the region of your assets. Valid values:
        # - cn-hangzhou: Your assets belong to the Chinese mainland.
        # - ap-southeast-1: Your assets belong to regions outside China.
        self.region_id = region_id
        # The user ID that the administrator switches to when viewing from the perspective of another member.
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

        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name

        if self.log_user_id is not None:
            result['LogUserId'] = self.log_user_id

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

        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')

        if m.get('LogUserId') is not None:
            self.log_user_id = m.get('LogUserId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        return self

