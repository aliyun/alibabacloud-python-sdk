# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDataLimitsRequest(DaraModel):
    def __init__(
        self,
        audit_status: int = None,
        check_status: int = None,
        current_page: int = None,
        datamask_status: int = None,
        enable: int = None,
        end_time: int = None,
        engine_type: str = None,
        feature_type: int = None,
        lang: str = None,
        member_account: int = None,
        page_size: int = None,
        parent_id: str = None,
        resource_type: int = None,
        service_region_id: str = None,
        start_time: int = None,
    ):
        # The audit status. Valid values:
        # - **1**: audit enabled.
        # - **0**: audit disabled.
        self.audit_status = audit_status
        # The data detection status. Valid values:
        # - **0**: ready.
        # - **1**: running.
        # - **2**: connectivity test in progress.
        # - **3**: connectivity test passed.
        # - **4**: connectivity test failed.
        self.check_status = check_status
        # Settings the page number of the current page when you perform a paged query. For more information about paging, refer to the paging parameters.
        self.current_page = current_page
        # The data masking permission status. Valid values:
        # - **1**: enabled.
        # - **0**: disabled.
        self.datamask_status = datamask_status
        # The detection permission status. Valid values:
        # - **1**: enabled.
        # - **0**: disabled.
        self.enable = enable
        # The end of the creation time range. Format: timestamp. Unit: milliseconds.
        self.end_time = end_time
        # The database type. Valid values: **MySQL**, **SQLServer**, **Oracle**, **PostgreSQL**, **MongoDB**, and others.
        self.engine_type = engine_type
        # This parameter is deprecated.
        self.feature_type = feature_type
        # The language of the request and response. Valid values:
        # - **zh**: Chinese.
        # - **en**: English.
        self.lang = lang
        # The ID of the member accounts.
        self.member_account = member_account
        # The maximum number of entries to return on each page when you perform a paged query. For more information about paging, refer to the paging parameters.
        self.page_size = page_size
        # The ID of the parent asset to which the data asset belongs. Valid values:
        # - The project name or ID for MaxCompute.
        # - The bucket name or ID for OSS.
        # - The instance name or ID, or the database name or ID for RDS.
        self.parent_id = parent_id
        # Required. The type of the product to which the data asset belongs. Valid values:
        # - **1**: MaxCompute
        # - **2**: OSS
        # - **3**: ADS
        # - **4**: OTS
        # - **5**: RDS
        # - **6**: SELF_DB
        self.resource_type = resource_type
        # The region where the asset resides.
        self.service_region_id = service_region_id
        # The start of the creation time range. Format: timestamp. Unit: milliseconds.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status

        if self.check_status is not None:
            result['CheckStatus'] = self.check_status

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.datamask_status is not None:
            result['DatamaskStatus'] = self.datamask_status

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.engine_type is not None:
            result['EngineType'] = self.engine_type

        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.member_account is not None:
            result['MemberAccount'] = self.member_account

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.service_region_id is not None:
            result['ServiceRegionId'] = self.service_region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')

        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('DatamaskStatus') is not None:
            self.datamask_status = m.get('DatamaskStatus')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')

        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MemberAccount') is not None:
            self.member_account = m.get('MemberAccount')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('ServiceRegionId') is not None:
            self.service_region_id = m.get('ServiceRegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

