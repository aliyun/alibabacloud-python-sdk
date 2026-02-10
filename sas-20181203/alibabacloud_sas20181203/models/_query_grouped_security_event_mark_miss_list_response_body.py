# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class QueryGroupedSecurityEventMarkMissListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        list: List[main_models.QueryGroupedSecurityEventMarkMissListResponseBodyList] = None,
        message: str = None,
        page_info: main_models.QueryGroupedSecurityEventMarkMissListResponseBodyPageInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code returned. The status code **200** indicates that the request is successful. Other status codes indicate that the request fails. You can identify the cause of the failure based on the status code.
        self.code = code
        # An array that consists of the whitelist rules.
        self.list = list
        # The error message returned.
        self.message = message
        # The pagination information.
        self.page_info = page_info
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
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

        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.QueryGroupedSecurityEventMarkMissListResponseBodyList()
                self.list.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageInfo') is not None:
            temp_model = main_models.QueryGroupedSecurityEventMarkMissListResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryGroupedSecurityEventMarkMissListResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # The page number of the returned page.
        self.current_page = current_page
        # The number of entries returned per page. Default value: **20**.
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

class QueryGroupedSecurityEventMarkMissListResponseBodyList(DaraModel):
    def __init__(
        self,
        ali_uid: int = None,
        disposal_way: str = None,
        event_name: str = None,
        event_name_original: str = None,
        event_type: str = None,
        event_type_original: str = None,
        field: str = None,
        field_value: str = None,
        filed_alias_name: str = None,
        operate: str = None,
        uuids: str = None,
    ):
        # The ID of the user.
        self.ali_uid = ali_uid
        # The handling method. Valid values:
        # 
        # *   **auto_add_white**: Automatically Added to Whitelist
        # *   **defense_not_notification**: Defense Without Notification
        self.disposal_way = disposal_way
        # The name of the alert event. The value indicates a subtype.
        self.event_name = event_name
        # The name of the alert event. The value indicates a type.
        self.event_name_original = event_name_original
        # The subtype of the alert event.
        self.event_type = event_type
        # The type of the alert event.
        self.event_type_original = event_type_original
        # The field that is used in the whitelist rule.
        self.field = field
        # The value of the field.
        self.field_value = field_value
        # The alias of the field.
        self.filed_alias_name = filed_alias_name
        # The operator. Valid values:
        # 
        # *   **contains**: contains
        # *   **notContains**: does not contain
        # *   **strEqual**: equals
        # *   **strNotEqual**: does not equal
        # *   **regex**: regular expression
        self.operate = operate
        # The UUIDs of assets. Multiple UUIDs are separated by commas (,).
        self.uuids = uuids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.disposal_way is not None:
            result['DisposalWay'] = self.disposal_way

        if self.event_name is not None:
            result['EventName'] = self.event_name

        if self.event_name_original is not None:
            result['EventNameOriginal'] = self.event_name_original

        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.event_type_original is not None:
            result['EventTypeOriginal'] = self.event_type_original

        if self.field is not None:
            result['Field'] = self.field

        if self.field_value is not None:
            result['FieldValue'] = self.field_value

        if self.filed_alias_name is not None:
            result['FiledAliasName'] = self.filed_alias_name

        if self.operate is not None:
            result['Operate'] = self.operate

        if self.uuids is not None:
            result['Uuids'] = self.uuids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('DisposalWay') is not None:
            self.disposal_way = m.get('DisposalWay')

        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        if m.get('EventNameOriginal') is not None:
            self.event_name_original = m.get('EventNameOriginal')

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('EventTypeOriginal') is not None:
            self.event_type_original = m.get('EventTypeOriginal')

        if m.get('Field') is not None:
            self.field = m.get('Field')

        if m.get('FieldValue') is not None:
            self.field_value = m.get('FieldValue')

        if m.get('FiledAliasName') is not None:
            self.filed_alias_name = m.get('FiledAliasName')

        if m.get('Operate') is not None:
            self.operate = m.get('Operate')

        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')

        return self

