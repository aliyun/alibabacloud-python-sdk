# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class DsgWhiteListQueryListResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        page_data: main_models.DsgWhiteListQueryListResponseBodyPageData = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The pagination information.
        self.page_data = page_data
        # The request ID. You can use the ID to locate logs and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.page_data:
            self.page_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.page_data is not None:
            result['PageData'] = self.page_data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('PageData') is not None:
            temp_model = main_models.DsgWhiteListQueryListResponseBodyPageData()
            self.page_data = temp_model.from_map(m.get('PageData'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DsgWhiteListQueryListResponseBodyPageData(DaraModel):
    def __init__(
        self,
        data: List[main_models.DsgWhiteListQueryListResponseBodyPageDataData] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # A collection of whitelists.
        self.data = data
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of data masking whitelists.
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DsgWhiteListQueryListResponseBodyPageDataData()
                self.data.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DsgWhiteListQueryListResponseBodyPageDataData(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        rule_id: int = None,
        scene_id: int = None,
        start_time: str = None,
        type: str = None,
        user_groups: List[str] = None,
    ):
        # The expiration time of the data masking whitelist cannot be earlier than the time when the data masking whitelist takes effect. Unit: days.
        self.end_time = end_time
        # The time when the whitelist was created.
        self.gmt_create = gmt_create
        # The time when the whitelist was modified.
        self.gmt_modified = gmt_modified
        # The ID of the data masking whitelist.
        self.id = id
        # The ID of the data masking rule.
        self.rule_id = rule_id
        # The ID of the level-2 data masking scenario.
        self.scene_id = scene_id
        # The time when the data masking whitelist takes effect cannot be earlier than the current time. Unit: days.
        self.start_time = start_time
        # The sensitive field type.
        self.type = type
        # A collection of user group names.
        self.user_groups = user_groups

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.type is not None:
            result['Type'] = self.type

        if self.user_groups is not None:
            result['UserGroups'] = self.user_groups

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UserGroups') is not None:
            self.user_groups = m.get('UserGroups')

        return self

