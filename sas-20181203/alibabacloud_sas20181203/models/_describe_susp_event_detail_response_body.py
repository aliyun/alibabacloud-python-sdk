# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeSuspEventDetailResponseBody(DaraModel):
    def __init__(
        self,
        alarm_unique_info: str = None,
        can_be_deal_on_line: bool = None,
        data_source: str = None,
        details: List[main_models.DescribeSuspEventDetailResponseBodyDetails] = None,
        event_desc: str = None,
        event_name: str = None,
        event_status: str = None,
        event_type_desc: str = None,
        id: int = None,
        instance_name: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        last_time: str = None,
        level: str = None,
        operate_error_code: str = None,
        operate_msg: str = None,
        request_id: str = None,
        sale_version: str = None,
        uuid: str = None,
    ):
        # The unique ID of the alarm event.
        # > If querying the anomaly information of a single alarm event, you need to provide the unique ID of the alarm event, which can be obtained by calling the [DescribeSuspEvents](~~DescribeSuspEvents~~) interface.
        self.alarm_unique_info = alarm_unique_info
        # Indicates whether the online processing of exceptions is supported, such as blocking an exception, adding an exception to the whitelist, and ignoring an exception. Valid values:
        # 
        # *   **true**: The online processing of exceptions is supported.
        # *   **false**: The online processing of exceptions is not supported.
        self.can_be_deal_on_line = can_be_deal_on_line
        # The data source of the exception.
        self.data_source = data_source
        # An array that consists of the details of the exception.
        self.details = details
        # The description of the exception.
        self.event_desc = event_desc
        # The name of the exception.
        self.event_name = event_name
        # The status of the exception. Valid values:
        # 
        # *   **1**: pending handling
        # *   **2**: ignored
        # *   **4**: confirmed
        # *   **8**: marked as a false positive
        # *   **16**: handling
        # *   **32**: handled
        # *   **64**: expired
        self.event_status = event_status
        # The type of the exception.
        self.event_type_desc = event_type_desc
        # The ID of the exception.
        self.id = id
        # The name of the server on which the exception was detected.
        self.instance_name = instance_name
        # The public IP address of the server on which the exception was detected.
        self.internet_ip = internet_ip
        # The private IP address of the server on which the exception was detected.
        self.intranet_ip = intranet_ip
        # The time when the exception was last detected.
        self.last_time = last_time
        # The risk level of the exception. Valid values:
        # 
        # *   **serious**
        # *   **suspicious**
        # *   **remind**
        self.level = level
        # The code that indicates the handling result of the exception.
        self.operate_error_code = operate_error_code
        # The message that indicates the handling result of the exception.
        self.operate_msg = operate_msg
        # The ID of the request.
        self.request_id = request_id
        # The edition of Security Center in which the exception can be detected. Valid values:
        # 
        # *   **0**: Basic edition
        # *   **1**: Advanced edition
        # *   **2**: Enterprise edition
        self.sale_version = sale_version
        # The UUID of the server on which the exception was detected.
        self.uuid = uuid

    def validate(self):
        if self.details:
            for v1 in self.details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_unique_info is not None:
            result['AlarmUniqueInfo'] = self.alarm_unique_info

        if self.can_be_deal_on_line is not None:
            result['CanBeDealOnLine'] = self.can_be_deal_on_line

        if self.data_source is not None:
            result['DataSource'] = self.data_source

        result['Details'] = []
        if self.details is not None:
            for k1 in self.details:
                result['Details'].append(k1.to_map() if k1 else None)

        if self.event_desc is not None:
            result['EventDesc'] = self.event_desc

        if self.event_name is not None:
            result['EventName'] = self.event_name

        if self.event_status is not None:
            result['EventStatus'] = self.event_status

        if self.event_type_desc is not None:
            result['EventTypeDesc'] = self.event_type_desc

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        if self.last_time is not None:
            result['LastTime'] = self.last_time

        if self.level is not None:
            result['Level'] = self.level

        if self.operate_error_code is not None:
            result['OperateErrorCode'] = self.operate_error_code

        if self.operate_msg is not None:
            result['OperateMsg'] = self.operate_msg

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sale_version is not None:
            result['SaleVersion'] = self.sale_version

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmUniqueInfo') is not None:
            self.alarm_unique_info = m.get('AlarmUniqueInfo')

        if m.get('CanBeDealOnLine') is not None:
            self.can_be_deal_on_line = m.get('CanBeDealOnLine')

        if m.get('DataSource') is not None:
            self.data_source = m.get('DataSource')

        self.details = []
        if m.get('Details') is not None:
            for k1 in m.get('Details'):
                temp_model = main_models.DescribeSuspEventDetailResponseBodyDetails()
                self.details.append(temp_model.from_map(k1))

        if m.get('EventDesc') is not None:
            self.event_desc = m.get('EventDesc')

        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        if m.get('EventStatus') is not None:
            self.event_status = m.get('EventStatus')

        if m.get('EventTypeDesc') is not None:
            self.event_type_desc = m.get('EventTypeDesc')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        if m.get('LastTime') is not None:
            self.last_time = m.get('LastTime')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('OperateErrorCode') is not None:
            self.operate_error_code = m.get('OperateErrorCode')

        if m.get('OperateMsg') is not None:
            self.operate_msg = m.get('OperateMsg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SaleVersion') is not None:
            self.sale_version = m.get('SaleVersion')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

class DescribeSuspEventDetailResponseBodyDetails(DaraModel):
    def __init__(
        self,
        name_display: str = None,
        type: str = None,
        value: str = None,
    ):
        # The display name of the alert event.
        self.name_display = name_display
        # The format in which the details of the exception are displayed.
        # 
        # Valid values:
        # 
        # *   **text**
        # *   **html**
        self.type = type
        # The attribute information about the exception. For example, if the exception is associated with an alert that is triggered by an unusual logon, the information can include the time when the logon is initiated and the location from which the logon is initiated. If the exception is associated with an alert that is triggered by a webshell file, the information can include the path of the trojan file and the type of the trojan.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name_display is not None:
            result['NameDisplay'] = self.name_display

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NameDisplay') is not None:
            self.name_display = m.get('NameDisplay')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

