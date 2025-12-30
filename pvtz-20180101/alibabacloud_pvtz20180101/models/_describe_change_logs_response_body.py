# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pvtz20180101 import models as main_models
from darabonba.model import DaraModel

class DescribeChangeLogsResponseBody(DaraModel):
    def __init__(
        self,
        change_logs: main_models.DescribeChangeLogsResponseBodyChangeLogs = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_items: int = None,
        total_pages: int = None,
    ):
        # The operation logs.
        self.change_logs = change_logs
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_items = total_items
        # The total number of pages returned.
        self.total_pages = total_pages

    def validate(self):
        if self.change_logs:
            self.change_logs.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_logs is not None:
            result['ChangeLogs'] = self.change_logs.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_items is not None:
            result['TotalItems'] = self.total_items

        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeLogs') is not None:
            temp_model = main_models.DescribeChangeLogsResponseBodyChangeLogs()
            self.change_logs = temp_model.from_map(m.get('ChangeLogs'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalItems') is not None:
            self.total_items = m.get('TotalItems')

        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')

        return self

class DescribeChangeLogsResponseBodyChangeLogs(DaraModel):
    def __init__(
        self,
        change_log: List[main_models.DescribeChangeLogsResponseBodyChangeLogsChangeLog] = None,
    ):
        self.change_log = change_log

    def validate(self):
        if self.change_log:
            for v1 in self.change_log:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ChangeLog'] = []
        if self.change_log is not None:
            for k1 in self.change_log:
                result['ChangeLog'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.change_log = []
        if m.get('ChangeLog') is not None:
            for k1 in m.get('ChangeLog'):
                temp_model = main_models.DescribeChangeLogsResponseBodyChangeLogsChangeLog()
                self.change_log.append(temp_model.from_map(k1))

        return self

class DescribeChangeLogsResponseBodyChangeLogsChangeLog(DaraModel):
    def __init__(
        self,
        content: str = None,
        creator_id: str = None,
        creator_sub_type: str = None,
        creator_type: str = None,
        creator_user_id: str = None,
        entity_id: str = None,
        entity_name: str = None,
        id: int = None,
        oper_action: str = None,
        oper_ip: str = None,
        oper_object: str = None,
        oper_time: str = None,
        oper_timestamp: int = None,
    ):
        # The operation content.
        self.content = content
        # The operator ID.
        self.creator_id = creator_id
        # The subtype of the operator. Valid values:
        # 
        # *   CUSTOMER: Alibaba Cloud account
        # *   SUB: RAM user
        # *   STS: assumed role that obtains the Security Token Service (STS) token of a RAM role
        # *   OTHER: other types
        self.creator_sub_type = creator_sub_type
        # The operator type. No value or **USER** is returned for this parameter.
        self.creator_type = creator_type
        # The operator ID.
        self.creator_user_id = creator_user_id
        # The unique ID of the zone, user-defined line, forwarding rule, outbound endpoint, or inbound endpoint.
        self.entity_id = entity_id
        # The name of the object on which the operation was performed, such as the domain name, user-defined line, cache retention domain name, forwarding rule, outbound endpoint, or inbound endpoint.
        self.entity_name = entity_name
        # The ID of the operation log.
        self.id = id
        # The specific operation performed on the object, such as adding, deleting, modifying, or associating the object.
        self.oper_action = oper_action
        # The public IP address of the operator terminal. If the IP address of the operator terminal is a private IP address, the value of this parameter is the public IP address to which the private IP address is mapped after network address translation (NAT).
        self.oper_ip = oper_ip
        # The type of the object on which the operation was performed. Valid values:
        # 
        # *   **PV_ZONE**: the built-in authoritative zone
        # *   **PV_RECORD**: the DNS record
        # *   **RESOLVER_RULE**: the forwarding rule
        # *   **CUSTOM_LINE**: the user-defined line
        # *   **RESOLVER_ENDPOINT**: the outbound endpoint
        # *   **INBOUND_ENDPOINT**: the inbound endpoint
        # *   **CACHE_RESERVE_DOMAIN**: the cache retention domain name
        self.oper_object = oper_object
        # The time when the operation is performed. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.oper_time = oper_time
        # The time when the operation was performed. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.oper_timestamp = oper_timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id

        if self.creator_sub_type is not None:
            result['CreatorSubType'] = self.creator_sub_type

        if self.creator_type is not None:
            result['CreatorType'] = self.creator_type

        if self.creator_user_id is not None:
            result['CreatorUserId'] = self.creator_user_id

        if self.entity_id is not None:
            result['EntityId'] = self.entity_id

        if self.entity_name is not None:
            result['EntityName'] = self.entity_name

        if self.id is not None:
            result['Id'] = self.id

        if self.oper_action is not None:
            result['OperAction'] = self.oper_action

        if self.oper_ip is not None:
            result['OperIp'] = self.oper_ip

        if self.oper_object is not None:
            result['OperObject'] = self.oper_object

        if self.oper_time is not None:
            result['OperTime'] = self.oper_time

        if self.oper_timestamp is not None:
            result['OperTimestamp'] = self.oper_timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')

        if m.get('CreatorSubType') is not None:
            self.creator_sub_type = m.get('CreatorSubType')

        if m.get('CreatorType') is not None:
            self.creator_type = m.get('CreatorType')

        if m.get('CreatorUserId') is not None:
            self.creator_user_id = m.get('CreatorUserId')

        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')

        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('OperAction') is not None:
            self.oper_action = m.get('OperAction')

        if m.get('OperIp') is not None:
            self.oper_ip = m.get('OperIp')

        if m.get('OperObject') is not None:
            self.oper_object = m.get('OperObject')

        if m.get('OperTime') is not None:
            self.oper_time = m.get('OperTime')

        if m.get('OperTimestamp') is not None:
            self.oper_timestamp = m.get('OperTimestamp')

        return self

