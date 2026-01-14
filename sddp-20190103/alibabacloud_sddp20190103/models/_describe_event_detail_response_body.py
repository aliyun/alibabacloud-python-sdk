# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sddp20190103 import models as main_models
from darabonba.model import DaraModel

class DescribeEventDetailResponseBody(DaraModel):
    def __init__(
        self,
        event: main_models.DescribeEventDetailResponseBodyEvent = None,
        request_id: str = None,
    ):
        # The details of the anomalous event.
        self.event = event
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.event:
            self.event.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event is not None:
            result['Event'] = self.event.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Event') is not None:
            temp_model = main_models.DescribeEventDetailResponseBodyEvent()
            self.event = temp_model.from_map(m.get('Event'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeEventDetailResponseBodyEvent(DaraModel):
    def __init__(
        self,
        alert_time: int = None,
        backed: bool = None,
        data_instance: str = None,
        deal_display_name: str = None,
        deal_login_name: str = None,
        deal_reason: str = None,
        deal_time: int = None,
        deal_user_id: int = None,
        detail: main_models.DescribeEventDetailResponseBodyEventDetail = None,
        display_name: str = None,
        event_time: int = None,
        handle_info_list: List[main_models.DescribeEventDetailResponseBodyEventHandleInfoList] = None,
        id: int = None,
        log_detail: str = None,
        login_name: str = None,
        new_alarm: bool = None,
        product_code: str = None,
        status: int = None,
        status_name: str = None,
        sub_type_code: str = None,
        sub_type_name: str = None,
        type_code: str = None,
        type_name: str = None,
        user_id: int = None,
    ):
        # The time when the alert for the anomalous event was generated. The value is a UNIX timestamp. Unit: milliseconds.
        self.alert_time = alert_time
        # Indicates whether the handling result of the anomalous event is used to enhance the detection of anomalous events. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        # 
        # > If you enhance the detection of anomalous events, the detection accuracy and the rate of triggering alerts for anomalous events are improved.
        self.backed = backed
        # The instance name of the service in which the anomalous event was detected.
        self.data_instance = data_instance
        # The display name of the account that is used to handle the anomalous event.
        self.deal_display_name = deal_display_name
        # The username of the account that is used to handle the anomalous event.
        self.deal_login_name = deal_login_name
        # The reason why the anomalous event is handled.
        self.deal_reason = deal_reason
        # The time when the anomalous event was handled. The value is a UNIX timestamp. Unit: milliseconds.
        self.deal_time = deal_time
        # The ID of the account that is used to handle the anomalous event.
        self.deal_user_id = deal_user_id
        # The content in the details of the anomalous event.
        self.detail = detail
        # The display name of the account that triggered the anomalous event.
        self.display_name = display_name
        # The time when the anomalous event occurred. The value is a UNIX timestamp. Unit: milliseconds.
        self.event_time = event_time
        # An array that consists of the handling records of the anomalous event.
        self.handle_info_list = handle_info_list
        # The unique ID of the anomalous event.
        self.id = id
        # The details of the alert logs.
        self.log_detail = log_detail
        # The username of the account that triggered the anomalous event.
        self.login_name = login_name
        # Whether it is a new version of the alarm. Value:
        # - **true**: Yes. 
        # - **false**: No.
        self.new_alarm = new_alarm
        # The name of the service in which the anomalous event was detected. Valid values include **MaxCompute, OSS, ADS, OTS, and RDS**.
        self.product_code = product_code
        # The handling status for the anomalous event. Valid values:
        # 
        # *   **0**: unhandled
        # *   **1**: confirmed
        # *   **2**: marked as false positive
        self.status = status
        # The name of the handling status for the anomalous event.
        self.status_name = status_name
        # The code of the anomalous event subtype.
        self.sub_type_code = sub_type_code
        # The name of the anomalous event subtype.
        self.sub_type_name = sub_type_name
        # The code of the anomalous event type.
        self.type_code = type_code
        # The name of the anomalous event type. Valid values:
        # 
        # *   **01**: anomalous permission usage
        # *   **02**: anomalous data flow
        # *   **03**: anomalous data operation
        self.type_name = type_name
        # The ID of the account that triggered the anomalous event.
        self.user_id = user_id

    def validate(self):
        if self.detail:
            self.detail.validate()
        if self.handle_info_list:
            for v1 in self.handle_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_time is not None:
            result['AlertTime'] = self.alert_time

        if self.backed is not None:
            result['Backed'] = self.backed

        if self.data_instance is not None:
            result['DataInstance'] = self.data_instance

        if self.deal_display_name is not None:
            result['DealDisplayName'] = self.deal_display_name

        if self.deal_login_name is not None:
            result['DealLoginName'] = self.deal_login_name

        if self.deal_reason is not None:
            result['DealReason'] = self.deal_reason

        if self.deal_time is not None:
            result['DealTime'] = self.deal_time

        if self.deal_user_id is not None:
            result['DealUserId'] = self.deal_user_id

        if self.detail is not None:
            result['Detail'] = self.detail.to_map()

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.event_time is not None:
            result['EventTime'] = self.event_time

        result['HandleInfoList'] = []
        if self.handle_info_list is not None:
            for k1 in self.handle_info_list:
                result['HandleInfoList'].append(k1.to_map() if k1 else None)

        if self.id is not None:
            result['Id'] = self.id

        if self.log_detail is not None:
            result['LogDetail'] = self.log_detail

        if self.login_name is not None:
            result['LoginName'] = self.login_name

        if self.new_alarm is not None:
            result['NewAlarm'] = self.new_alarm

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.status is not None:
            result['Status'] = self.status

        if self.status_name is not None:
            result['StatusName'] = self.status_name

        if self.sub_type_code is not None:
            result['SubTypeCode'] = self.sub_type_code

        if self.sub_type_name is not None:
            result['SubTypeName'] = self.sub_type_name

        if self.type_code is not None:
            result['TypeCode'] = self.type_code

        if self.type_name is not None:
            result['TypeName'] = self.type_name

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertTime') is not None:
            self.alert_time = m.get('AlertTime')

        if m.get('Backed') is not None:
            self.backed = m.get('Backed')

        if m.get('DataInstance') is not None:
            self.data_instance = m.get('DataInstance')

        if m.get('DealDisplayName') is not None:
            self.deal_display_name = m.get('DealDisplayName')

        if m.get('DealLoginName') is not None:
            self.deal_login_name = m.get('DealLoginName')

        if m.get('DealReason') is not None:
            self.deal_reason = m.get('DealReason')

        if m.get('DealTime') is not None:
            self.deal_time = m.get('DealTime')

        if m.get('DealUserId') is not None:
            self.deal_user_id = m.get('DealUserId')

        if m.get('Detail') is not None:
            temp_model = main_models.DescribeEventDetailResponseBodyEventDetail()
            self.detail = temp_model.from_map(m.get('Detail'))

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')

        self.handle_info_list = []
        if m.get('HandleInfoList') is not None:
            for k1 in m.get('HandleInfoList'):
                temp_model = main_models.DescribeEventDetailResponseBodyEventHandleInfoList()
                self.handle_info_list.append(temp_model.from_map(k1))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LogDetail') is not None:
            self.log_detail = m.get('LogDetail')

        if m.get('LoginName') is not None:
            self.login_name = m.get('LoginName')

        if m.get('NewAlarm') is not None:
            self.new_alarm = m.get('NewAlarm')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusName') is not None:
            self.status_name = m.get('StatusName')

        if m.get('SubTypeCode') is not None:
            self.sub_type_code = m.get('SubTypeCode')

        if m.get('SubTypeName') is not None:
            self.sub_type_name = m.get('SubTypeName')

        if m.get('TypeCode') is not None:
            self.type_code = m.get('TypeCode')

        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class DescribeEventDetailResponseBodyEventHandleInfoList(DaraModel):
    def __init__(
        self,
        current_value: str = None,
        disable_time: int = None,
        enable_time: int = None,
        handler_name: str = None,
        handler_type: str = None,
        handler_value: int = None,
        id: int = None,
        status: int = None,
    ):
        # The account that is used to handle the anomalous event.
        self.current_value = current_value
        # The time when the account is disabled. The value is a UNIX timestamp. Unit: milliseconds.
        self.disable_time = disable_time
        # The time when the disabled account is enabled. The value is a UNIX timestamp. Unit: milliseconds.
        self.enable_time = enable_time
        # The handling method.
        self.handler_name = handler_name
        # The type of the handling method.
        self.handler_type = handler_type
        # The duration for which the handling operation takes effect. If you leave this parameter empty, the handling operation is permanently valid. Unit: minutes.
        self.handler_value = handler_value
        # The ID of the handling rule.
        self.id = id
        # The status of the account that triggered the anomalous event. Valid values:
        # 
        # *   **0**: disabled
        # *   **1**: enabled
        # *   **-1**: failed to disable the account
        # *   **-2**: failed to enable the account
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_value is not None:
            result['CurrentValue'] = self.current_value

        if self.disable_time is not None:
            result['DisableTime'] = self.disable_time

        if self.enable_time is not None:
            result['EnableTime'] = self.enable_time

        if self.handler_name is not None:
            result['HandlerName'] = self.handler_name

        if self.handler_type is not None:
            result['HandlerType'] = self.handler_type

        if self.handler_value is not None:
            result['HandlerValue'] = self.handler_value

        if self.id is not None:
            result['Id'] = self.id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentValue') is not None:
            self.current_value = m.get('CurrentValue')

        if m.get('DisableTime') is not None:
            self.disable_time = m.get('DisableTime')

        if m.get('EnableTime') is not None:
            self.enable_time = m.get('EnableTime')

        if m.get('HandlerName') is not None:
            self.handler_name = m.get('HandlerName')

        if m.get('HandlerType') is not None:
            self.handler_type = m.get('HandlerType')

        if m.get('HandlerValue') is not None:
            self.handler_value = m.get('HandlerValue')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeEventDetailResponseBodyEventDetail(DaraModel):
    def __init__(
        self,
        chart: List[main_models.DescribeEventDetailResponseBodyEventDetailChart] = None,
        content: List[main_models.DescribeEventDetailResponseBodyEventDetailContent] = None,
        resource_info: List[main_models.DescribeEventDetailResponseBodyEventDetailResourceInfo] = None,
    ):
        # The baseline behavior chart of the anomalous event.
        self.chart = chart
        # The content in the anomalous event.
        self.content = content
        # An array that consists of the source from which the information of the anomalous event is recorded.
        self.resource_info = resource_info

    def validate(self):
        if self.chart:
            for v1 in self.chart:
                 if v1:
                    v1.validate()
        if self.content:
            for v1 in self.content:
                 if v1:
                    v1.validate()
        if self.resource_info:
            for v1 in self.resource_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Chart'] = []
        if self.chart is not None:
            for k1 in self.chart:
                result['Chart'].append(k1.to_map() if k1 else None)

        result['Content'] = []
        if self.content is not None:
            for k1 in self.content:
                result['Content'].append(k1.to_map() if k1 else None)

        result['ResourceInfo'] = []
        if self.resource_info is not None:
            for k1 in self.resource_info:
                result['ResourceInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.chart = []
        if m.get('Chart') is not None:
            for k1 in m.get('Chart'):
                temp_model = main_models.DescribeEventDetailResponseBodyEventDetailChart()
                self.chart.append(temp_model.from_map(k1))

        self.content = []
        if m.get('Content') is not None:
            for k1 in m.get('Content'):
                temp_model = main_models.DescribeEventDetailResponseBodyEventDetailContent()
                self.content.append(temp_model.from_map(k1))

        self.resource_info = []
        if m.get('ResourceInfo') is not None:
            for k1 in m.get('ResourceInfo'):
                temp_model = main_models.DescribeEventDetailResponseBodyEventDetailResourceInfo()
                self.resource_info.append(temp_model.from_map(k1))

        return self

class DescribeEventDetailResponseBodyEventDetailResourceInfo(DaraModel):
    def __init__(
        self,
        label: str = None,
        value: str = None,
    ):
        # The source title.
        self.label = label
        # The source description.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label is not None:
            result['Label'] = self.label

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeEventDetailResponseBodyEventDetailContent(DaraModel):
    def __init__(
        self,
        label: str = None,
        name: str = None,
        value: str = None,
    ):
        # The title of the content in the anomalous event.
        self.label = label
        # Exception event name.
        self.name = name
        # The description of the content in the anomalous event.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label is not None:
            result['Label'] = self.label

        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeEventDetailResponseBodyEventDetailChart(DaraModel):
    def __init__(
        self,
        chat_type: int = None,
        data: main_models.DescribeEventDetailResponseBodyEventDetailChartData = None,
        label: str = None,
        name: str = None,
        type: str = None,
        xlabel: str = None,
        ylabel: str = None,
        zlabel: str = None,
    ):
        # The type of the chart. Valid values:
        # 
        # *   **1**: column chart
        # *   **2**: line chart
        # 
        # >This field will be returned only when NewAlarm is true.
        self.chat_type = chat_type
        # The data in the baseline behavior profile of the anomalous event.
        self.data = data
        # The name of the baseline behavior chart of the anomalous event.
        self.label = label
        # Icon title.
        # 
        # >This field will be returned only when NewAlarm is true.
        self.name = name
        # The type of the chart. Valid values:
        # 
        # *   **1**: column chart
        # *   **2**: line chart
        self.type = type
        # The descriptive label of data items on the X axis.
        self.xlabel = xlabel
        # The descriptive label of data items on the Y axis.
        self.ylabel = ylabel
        # The descriptive label of data items on the Z axis.
        # 
        # >This field will be returned only when NewAlarm is true.
        self.zlabel = zlabel

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chat_type is not None:
            result['ChatType'] = self.chat_type

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.label is not None:
            result['Label'] = self.label

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        if self.xlabel is not None:
            result['XLabel'] = self.xlabel

        if self.ylabel is not None:
            result['YLabel'] = self.ylabel

        if self.zlabel is not None:
            result['ZLabel'] = self.zlabel

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChatType') is not None:
            self.chat_type = m.get('ChatType')

        if m.get('Data') is not None:
            temp_model = main_models.DescribeEventDetailResponseBodyEventDetailChartData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('XLabel') is not None:
            self.xlabel = m.get('XLabel')

        if m.get('YLabel') is not None:
            self.ylabel = m.get('YLabel')

        if m.get('ZLabel') is not None:
            self.zlabel = m.get('ZLabel')

        return self

class DescribeEventDetailResponseBodyEventDetailChartData(DaraModel):
    def __init__(
        self,
        x: List[str] = None,
        y: List[str] = None,
        z: List[str] = None,
    ):
        # The value of the data item on the X axis.
        self.x = x
        # The value of the data item on the Y axis.
        self.y = y
        # The value of the data item for the Z axis.
        self.z = z

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.x is not None:
            result['X'] = self.x

        if self.y is not None:
            result['Y'] = self.y

        if self.z is not None:
            result['Z'] = self.z

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        if m.get('Z') is not None:
            self.z = m.get('Z')

        return self

