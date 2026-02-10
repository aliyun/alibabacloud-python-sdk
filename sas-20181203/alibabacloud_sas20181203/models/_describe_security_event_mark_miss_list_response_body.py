# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeSecurityEventMarkMissListResponseBody(DaraModel):
    def __init__(
        self,
        list: List[main_models.DescribeSecurityEventMarkMissListResponseBodyList] = None,
        page_info: main_models.DescribeSecurityEventMarkMissListResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # The ID of the rule.
        self.list = list
        # The pagination information.
        self.page_info = page_info
        # The request ID.
        self.request_id = request_id

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
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.DescribeSecurityEventMarkMissListResponseBodyList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribeSecurityEventMarkMissListResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeSecurityEventMarkMissListResponseBodyPageInfo(DaraModel):
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
        # The number of entries per page. Default value: **20**.
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

class DescribeSecurityEventMarkMissListResponseBodyList(DaraModel):
    def __init__(
        self,
        ali_uid: int = None,
        event_name: str = None,
        event_name_original: str = None,
        event_type: str = None,
        event_type_original: str = None,
        field: str = None,
        field_value: str = None,
        filed_alias_name: str = None,
        id: int = None,
        instance_id: str = None,
        instance_name: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        operate: str = None,
        uuid: str = None,
    ):
        # The user ID.
        self.ali_uid = ali_uid
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
        # The ID of the rule.
        self.id = id
        # The instance ID of the server.
        self.instance_id = instance_id
        # The instance name of the asset.
        self.instance_name = instance_name
        # The public IP address of the server.
        self.internet_ip = internet_ip
        # The private IP address of the server.
        self.intranet_ip = intranet_ip
        # The operator. Valid values:
        # 
        # - **contains**: contains
        # - **notContains**: does not contain
        # - **strEqual**: equals
        # - **strNotEqual**: does not equal
        # - **regex**: regular expression
        self.operate = operate
        # The UUID of the asset.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

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

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        if self.operate is not None:
            result['Operate'] = self.operate

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

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

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        if m.get('Operate') is not None:
            self.operate = m.get('Operate')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

