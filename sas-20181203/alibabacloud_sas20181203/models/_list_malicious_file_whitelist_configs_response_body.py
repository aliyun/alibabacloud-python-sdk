# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListMaliciousFileWhitelistConfigsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        list: List[main_models.ListMaliciousFileWhitelistConfigsResponseBodyList] = None,
        message: str = None,
        page_info: main_models.ListMaliciousFileWhitelistConfigsResponseBodyPageInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. The status code **200** indicates that the request was successful. Other status codes indicate that the request failed. You can identify the cause of the failure based on the status code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The alert whitelist rules of sensitive files that are detected by using the agentless detection feature.
        self.list = list
        # The returned message.
        self.message = message
        # The pagination information.
        self.page_info = page_info
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.ListMaliciousFileWhitelistConfigsResponseBodyList()
                self.list.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageInfo') is not None:
            temp_model = main_models.ListMaliciousFileWhitelistConfigsResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListMaliciousFileWhitelistConfigsResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # The page number.
        self.current_page = current_page
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListMaliciousFileWhitelistConfigsResponseBodyList(DaraModel):
    def __init__(
        self,
        count: str = None,
        event_name: str = None,
        field: str = None,
        field_value: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        operator: str = None,
        remark: str = None,
        source: str = None,
        target_type: str = None,
        target_value: str = None,
    ):
        # The number of the assets on which the rule takes effect.
        # 
        # >  The value of this parameter is returned only if the value of TargetType is SELECTION_KEY.
        self.count = count
        # The name of the alert.
        # 
        # *   The value is fixed as ALL, which indicates all alert types.
        self.event_name = event_name
        # The field that is used in the whitelist rule.
        self.field = field
        # The value of the field that is used in the whitelist rule.
        self.field_value = field_value
        # The time when the rule was created.
        self.gmt_create = gmt_create
        # The time when the rule was modified.
        self.gmt_modified = gmt_modified
        # The ID of the rule.
        self.id = id
        # The logical operator of the whitelist rule.
        # 
        # *   The value is fixed as strEqual, which indicates the equality operator (=).
        self.operator = operator
        # Remark
        self.remark = remark
        # The feature to which this operation belongs.
        # 
        # *   The value is fixed as agentless, which indicates the agentless detection feature.
        self.source = source
        # The type of the assets on which the rule takes effect. Valid values:
        # 
        # *   ALL: all assets
        # *   SELECTION_KEY: selected assets
        self.target_type = target_type
        # The assets on which the rule takes effect. Valid values:
        # 
        # *   ALL: all assets
        # *   Others: selected assets
        self.target_value = target_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.event_name is not None:
            result['EventName'] = self.event_name

        if self.field is not None:
            result['Field'] = self.field

        if self.field_value is not None:
            result['FieldValue'] = self.field_value

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.source is not None:
            result['Source'] = self.source

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        if self.target_value is not None:
            result['TargetValue'] = self.target_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        if m.get('Field') is not None:
            self.field = m.get('Field')

        if m.get('FieldValue') is not None:
            self.field_value = m.get('FieldValue')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        if m.get('TargetValue') is not None:
            self.target_value = m.get('TargetValue')

        return self

