# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CreateScreenSettingRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        logo_power: bool = None,
        logo_url: str = None,
        monitor_url: str = None,
        screen_data_map: str = None,
        screen_default: int = None,
        title: str = None,
    ):
        self.id = id
        # This parameter is required.
        self.logo_power = logo_power
        # This parameter is required.
        self.logo_url = logo_url
        self.monitor_url = monitor_url
        # This parameter is required.
        self.screen_data_map = screen_data_map
        self.screen_default = screen_default
        # This parameter is required.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.logo_power is not None:
            result['LogoPower'] = self.logo_power
        if self.logo_url is not None:
            result['LogoUrl'] = self.logo_url
        if self.monitor_url is not None:
            result['MonitorUrl'] = self.monitor_url
        if self.screen_data_map is not None:
            result['ScreenDataMap'] = self.screen_data_map
        if self.screen_default is not None:
            result['ScreenDefault'] = self.screen_default
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LogoPower') is not None:
            self.logo_power = m.get('LogoPower')
        if m.get('LogoUrl') is not None:
            self.logo_url = m.get('LogoUrl')
        if m.get('MonitorUrl') is not None:
            self.monitor_url = m.get('MonitorUrl')
        if m.get('ScreenDataMap') is not None:
            self.screen_data_map = m.get('ScreenDataMap')
        if m.get('ScreenDefault') is not None:
            self.screen_default = m.get('ScreenDefault')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class CreateScreenSettingResponseBody(TeaModel):
    def __init__(
        self,
        id: int = None,
        request_id: str = None,
    ):
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateScreenSettingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateScreenSettingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateScreenSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteScreenSettingRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteScreenSettingResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteScreenSettingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteScreenSettingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteScreenSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScreenAlarmEventListRequest(TeaModel):
    def __init__(
        self,
        alarm_event_name: str = None,
        alarm_event_type: str = None,
        current_page: int = None,
        dealed: str = None,
        from_: str = None,
        lang: str = None,
        levels: str = None,
        page_size: str = None,
        remark: str = None,
        time_end: str = None,
        time_start: str = None,
    ):
        self.alarm_event_name = alarm_event_name
        self.alarm_event_type = alarm_event_type
        # This parameter is required.
        self.current_page = current_page
        self.dealed = dealed
        # This parameter is required.
        self.from_ = from_
        self.lang = lang
        self.levels = levels
        # This parameter is required.
        self.page_size = page_size
        self.remark = remark
        self.time_end = time_end
        self.time_start = time_start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_event_name is not None:
            result['AlarmEventName'] = self.alarm_event_name
        if self.alarm_event_type is not None:
            result['AlarmEventType'] = self.alarm_event_type
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.dealed is not None:
            result['Dealed'] = self.dealed
        if self.from_ is not None:
            result['From'] = self.from_
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.levels is not None:
            result['Levels'] = self.levels
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.time_end is not None:
            result['TimeEnd'] = self.time_end
        if self.time_start is not None:
            result['TimeStart'] = self.time_start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmEventName') is not None:
            self.alarm_event_name = m.get('AlarmEventName')
        if m.get('AlarmEventType') is not None:
            self.alarm_event_type = m.get('AlarmEventType')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Dealed') is not None:
            self.dealed = m.get('Dealed')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Levels') is not None:
            self.levels = m.get('Levels')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('TimeEnd') is not None:
            self.time_end = m.get('TimeEnd')
        if m.get('TimeStart') is not None:
            self.time_start = m.get('TimeStart')
        return self


class DescribeScreenAlarmEventListResponseBodyPageInfo(TeaModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.count = count
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeScreenAlarmEventListResponseBodySuspEvents(TeaModel):
    def __init__(
        self,
        alarm_event_name: str = None,
        alarm_event_type: str = None,
        alarm_unique_info: str = None,
        can_be_deal_on_line: bool = None,
        can_cancel_fault: bool = None,
        data_source: str = None,
        dealed: bool = None,
        description: str = None,
        end_time: int = None,
        instance_name: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        level: str = None,
        sale_version: str = None,
        solution: str = None,
        start_time: int = None,
        suspicious_event_count: int = None,
        uuid: str = None,
    ):
        self.alarm_event_name = alarm_event_name
        self.alarm_event_type = alarm_event_type
        self.alarm_unique_info = alarm_unique_info
        self.can_be_deal_on_line = can_be_deal_on_line
        self.can_cancel_fault = can_cancel_fault
        self.data_source = data_source
        self.dealed = dealed
        self.description = description
        self.end_time = end_time
        self.instance_name = instance_name
        self.internet_ip = internet_ip
        self.intranet_ip = intranet_ip
        self.level = level
        self.sale_version = sale_version
        self.solution = solution
        self.start_time = start_time
        self.suspicious_event_count = suspicious_event_count
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_event_name is not None:
            result['AlarmEventName'] = self.alarm_event_name
        if self.alarm_event_type is not None:
            result['AlarmEventType'] = self.alarm_event_type
        if self.alarm_unique_info is not None:
            result['AlarmUniqueInfo'] = self.alarm_unique_info
        if self.can_be_deal_on_line is not None:
            result['CanBeDealOnLine'] = self.can_be_deal_on_line
        if self.can_cancel_fault is not None:
            result['CanCancelFault'] = self.can_cancel_fault
        if self.data_source is not None:
            result['DataSource'] = self.data_source
        if self.dealed is not None:
            result['Dealed'] = self.dealed
        if self.description is not None:
            result['Description'] = self.description
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip
        if self.level is not None:
            result['Level'] = self.level
        if self.sale_version is not None:
            result['SaleVersion'] = self.sale_version
        if self.solution is not None:
            result['Solution'] = self.solution
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.suspicious_event_count is not None:
            result['SuspiciousEventCount'] = self.suspicious_event_count
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmEventName') is not None:
            self.alarm_event_name = m.get('AlarmEventName')
        if m.get('AlarmEventType') is not None:
            self.alarm_event_type = m.get('AlarmEventType')
        if m.get('AlarmUniqueInfo') is not None:
            self.alarm_unique_info = m.get('AlarmUniqueInfo')
        if m.get('CanBeDealOnLine') is not None:
            self.can_be_deal_on_line = m.get('CanBeDealOnLine')
        if m.get('CanCancelFault') is not None:
            self.can_cancel_fault = m.get('CanCancelFault')
        if m.get('DataSource') is not None:
            self.data_source = m.get('DataSource')
        if m.get('Dealed') is not None:
            self.dealed = m.get('Dealed')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('SaleVersion') is not None:
            self.sale_version = m.get('SaleVersion')
        if m.get('Solution') is not None:
            self.solution = m.get('Solution')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('SuspiciousEventCount') is not None:
            self.suspicious_event_count = m.get('SuspiciousEventCount')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class DescribeScreenAlarmEventListResponseBody(TeaModel):
    def __init__(
        self,
        page_info: DescribeScreenAlarmEventListResponseBodyPageInfo = None,
        request_id: str = None,
        susp_events: List[DescribeScreenAlarmEventListResponseBodySuspEvents] = None,
    ):
        self.page_info = page_info
        self.request_id = request_id
        self.susp_events = susp_events

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.susp_events:
            for k in self.susp_events:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SuspEvents'] = []
        if self.susp_events is not None:
            for k in self.susp_events:
                result['SuspEvents'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = DescribeScreenAlarmEventListResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.susp_events = []
        if m.get('SuspEvents') is not None:
            for k in m.get('SuspEvents'):
                temp_model = DescribeScreenAlarmEventListResponseBodySuspEvents()
                self.susp_events.append(temp_model.from_map(k))
        return self


class DescribeScreenAlarmEventListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeScreenAlarmEventListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeScreenAlarmEventListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScreenAttackAnalysisDataRequest(TeaModel):
    def __init__(
        self,
        base_64: str = None,
        current_page: int = None,
        data: str = None,
        end_time: int = None,
        page_size: int = None,
        start_time: int = None,
        type: str = None,
    ):
        self.base_64 = base_64
        self.current_page = current_page
        self.data = data
        # This parameter is required.
        self.end_time = end_time
        self.page_size = page_size
        # This parameter is required.
        self.start_time = start_time
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_64 is not None:
            result['Base64'] = self.base_64
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.data is not None:
            result['Data'] = self.data
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Base64') is not None:
            self.base_64 = m.get('Base64')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeScreenAttackAnalysisDataResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        page: int = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
    ):
        self.data = data
        self.page = page
        self.page_size = page_size
        self.request_id = request_id
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeScreenAttackAnalysisDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeScreenAttackAnalysisDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeScreenAttackAnalysisDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScreenCloudHcRiskResponseBodyCloudHcRiskItems(TeaModel):
    def __init__(
        self,
        affect_count: int = None,
        check_item: str = None,
        level: str = None,
        pass_: bool = None,
    ):
        self.affect_count = affect_count
        self.check_item = check_item
        self.level = level
        self.pass_ = pass_

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.affect_count is not None:
            result['AffectCount'] = self.affect_count
        if self.check_item is not None:
            result['CheckItem'] = self.check_item
        if self.level is not None:
            result['Level'] = self.level
        if self.pass_ is not None:
            result['Pass'] = self.pass_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AffectCount') is not None:
            self.affect_count = m.get('AffectCount')
        if m.get('CheckItem') is not None:
            self.check_item = m.get('CheckItem')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Pass') is not None:
            self.pass_ = m.get('Pass')
        return self


class DescribeScreenCloudHcRiskResponseBody(TeaModel):
    def __init__(
        self,
        cloud_hc_risk_items: List[DescribeScreenCloudHcRiskResponseBodyCloudHcRiskItems] = None,
        request_id: str = None,
    ):
        self.cloud_hc_risk_items = cloud_hc_risk_items
        self.request_id = request_id

    def validate(self):
        if self.cloud_hc_risk_items:
            for k in self.cloud_hc_risk_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CloudHcRiskItems'] = []
        if self.cloud_hc_risk_items is not None:
            for k in self.cloud_hc_risk_items:
                result['CloudHcRiskItems'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cloud_hc_risk_items = []
        if m.get('CloudHcRiskItems') is not None:
            for k in m.get('CloudHcRiskItems'):
                temp_model = DescribeScreenCloudHcRiskResponseBodyCloudHcRiskItems()
                self.cloud_hc_risk_items.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeScreenCloudHcRiskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeScreenCloudHcRiskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeScreenCloudHcRiskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScreenDataMapResponseBodySasScreenTypeListTypeDataDate(TeaModel):
    def __init__(
        self,
        unit: str = None,
        value: str = None,
    ):
        self.unit = unit
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.unit is not None:
            result['Unit'] = self.unit
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Unit') is not None:
            self.unit = m.get('Unit')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeScreenDataMapResponseBodySasScreenTypeListTypeData(TeaModel):
    def __init__(
        self,
        code: str = None,
        date: List[DescribeScreenDataMapResponseBodySasScreenTypeListTypeDataDate] = None,
        id: str = None,
        title: str = None,
    ):
        self.code = code
        self.date = date
        self.id = id
        self.title = title

    def validate(self):
        if self.date:
            for k in self.date:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Date'] = []
        if self.date is not None:
            for k in self.date:
                result['Date'].append(k.to_map() if k else None)
        if self.id is not None:
            result['Id'] = self.id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.date = []
        if m.get('Date') is not None:
            for k in m.get('Date'):
                temp_model = DescribeScreenDataMapResponseBodySasScreenTypeListTypeDataDate()
                self.date.append(temp_model.from_map(k))
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class DescribeScreenDataMapResponseBodySasScreenTypeList(TeaModel):
    def __init__(
        self,
        type: str = None,
        type_code: str = None,
        type_data: List[DescribeScreenDataMapResponseBodySasScreenTypeListTypeData] = None,
    ):
        self.type = type
        self.type_code = type_code
        self.type_data = type_data

    def validate(self):
        if self.type_data:
            for k in self.type_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.type_code is not None:
            result['TypeCode'] = self.type_code
        result['TypeData'] = []
        if self.type_data is not None:
            for k in self.type_data:
                result['TypeData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('TypeCode') is not None:
            self.type_code = m.get('TypeCode')
        self.type_data = []
        if m.get('TypeData') is not None:
            for k in m.get('TypeData'):
                temp_model = DescribeScreenDataMapResponseBodySasScreenTypeListTypeData()
                self.type_data.append(temp_model.from_map(k))
        return self


class DescribeScreenDataMapResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        sas_screen_type_list: List[DescribeScreenDataMapResponseBodySasScreenTypeList] = None,
    ):
        self.request_id = request_id
        self.sas_screen_type_list = sas_screen_type_list

    def validate(self):
        if self.sas_screen_type_list:
            for k in self.sas_screen_type_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SasScreenTypeList'] = []
        if self.sas_screen_type_list is not None:
            for k in self.sas_screen_type_list:
                result['SasScreenTypeList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.sas_screen_type_list = []
        if m.get('SasScreenTypeList') is not None:
            for k in m.get('SasScreenTypeList'):
                temp_model = DescribeScreenDataMapResponseBodySasScreenTypeList()
                self.sas_screen_type_list.append(temp_model.from_map(k))
        return self


class DescribeScreenDataMapResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeScreenDataMapResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeScreenDataMapResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScreenEmerRiskResponseBodyCloudHcRiskItems(TeaModel):
    def __init__(
        self,
        affect_count: int = None,
        level: str = None,
        vul_name: str = None,
    ):
        self.affect_count = affect_count
        self.level = level
        self.vul_name = vul_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.affect_count is not None:
            result['AffectCount'] = self.affect_count
        if self.level is not None:
            result['Level'] = self.level
        if self.vul_name is not None:
            result['VulName'] = self.vul_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AffectCount') is not None:
            self.affect_count = m.get('AffectCount')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('VulName') is not None:
            self.vul_name = m.get('VulName')
        return self


class DescribeScreenEmerRiskResponseBody(TeaModel):
    def __init__(
        self,
        cloud_hc_risk_items: List[DescribeScreenEmerRiskResponseBodyCloudHcRiskItems] = None,
        request_id: str = None,
    ):
        self.cloud_hc_risk_items = cloud_hc_risk_items
        self.request_id = request_id

    def validate(self):
        if self.cloud_hc_risk_items:
            for k in self.cloud_hc_risk_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CloudHcRiskItems'] = []
        if self.cloud_hc_risk_items is not None:
            for k in self.cloud_hc_risk_items:
                result['CloudHcRiskItems'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cloud_hc_risk_items = []
        if m.get('CloudHcRiskItems') is not None:
            for k in m.get('CloudHcRiskItems'):
                temp_model = DescribeScreenEmerRiskResponseBodyCloudHcRiskItems()
                self.cloud_hc_risk_items.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeScreenEmerRiskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeScreenEmerRiskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeScreenEmerRiskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScreenHostStatisticsResponseBodyData(TeaModel):
    def __init__(
        self,
        safe_count: List[str] = None,
        susp_event_machine_names: List[str] = None,
        susp_event_uuids: List[str] = None,
        weakness_machine_names: List[str] = None,
        weakness_uuids: List[str] = None,
    ):
        self.safe_count = safe_count
        self.susp_event_machine_names = susp_event_machine_names
        self.susp_event_uuids = susp_event_uuids
        self.weakness_machine_names = weakness_machine_names
        self.weakness_uuids = weakness_uuids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.safe_count is not None:
            result['SafeCount'] = self.safe_count
        if self.susp_event_machine_names is not None:
            result['SuspEventMachineNames'] = self.susp_event_machine_names
        if self.susp_event_uuids is not None:
            result['SuspEventUuids'] = self.susp_event_uuids
        if self.weakness_machine_names is not None:
            result['WeaknessMachineNames'] = self.weakness_machine_names
        if self.weakness_uuids is not None:
            result['WeaknessUuids'] = self.weakness_uuids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SafeCount') is not None:
            self.safe_count = m.get('SafeCount')
        if m.get('SuspEventMachineNames') is not None:
            self.susp_event_machine_names = m.get('SuspEventMachineNames')
        if m.get('SuspEventUuids') is not None:
            self.susp_event_uuids = m.get('SuspEventUuids')
        if m.get('WeaknessMachineNames') is not None:
            self.weakness_machine_names = m.get('WeaknessMachineNames')
        if m.get('WeaknessUuids') is not None:
            self.weakness_uuids = m.get('WeaknessUuids')
        return self


class DescribeScreenHostStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeScreenHostStatisticsResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeScreenHostStatisticsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeScreenHostStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeScreenHostStatisticsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeScreenHostStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScreenOperateInfoRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        start_time: int = None,
    ):
        self.lang = lang
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeScreenOperateInfoResponseBody(TeaModel):
    def __init__(
        self,
        date_array: List[str] = None,
        health_check_dealed_count: int = None,
        health_check_value_array: List[str] = None,
        request_id: str = None,
        security_event_dealed_count: int = None,
        susp_event_value_array: List[str] = None,
        vul_value_array: List[str] = None,
        vulnerability_dealed_count: int = None,
    ):
        self.date_array = date_array
        self.health_check_dealed_count = health_check_dealed_count
        self.health_check_value_array = health_check_value_array
        self.request_id = request_id
        self.security_event_dealed_count = security_event_dealed_count
        self.susp_event_value_array = susp_event_value_array
        self.vul_value_array = vul_value_array
        self.vulnerability_dealed_count = vulnerability_dealed_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_array is not None:
            result['DateArray'] = self.date_array
        if self.health_check_dealed_count is not None:
            result['HealthCheckDealedCount'] = self.health_check_dealed_count
        if self.health_check_value_array is not None:
            result['HealthCheckValueArray'] = self.health_check_value_array
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.security_event_dealed_count is not None:
            result['SecurityEventDealedCount'] = self.security_event_dealed_count
        if self.susp_event_value_array is not None:
            result['SuspEventValueArray'] = self.susp_event_value_array
        if self.vul_value_array is not None:
            result['VulValueArray'] = self.vul_value_array
        if self.vulnerability_dealed_count is not None:
            result['VulnerabilityDealedCount'] = self.vulnerability_dealed_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DateArray') is not None:
            self.date_array = m.get('DateArray')
        if m.get('HealthCheckDealedCount') is not None:
            self.health_check_dealed_count = m.get('HealthCheckDealedCount')
        if m.get('HealthCheckValueArray') is not None:
            self.health_check_value_array = m.get('HealthCheckValueArray')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecurityEventDealedCount') is not None:
            self.security_event_dealed_count = m.get('SecurityEventDealedCount')
        if m.get('SuspEventValueArray') is not None:
            self.susp_event_value_array = m.get('SuspEventValueArray')
        if m.get('VulValueArray') is not None:
            self.vul_value_array = m.get('VulValueArray')
        if m.get('VulnerabilityDealedCount') is not None:
            self.vulnerability_dealed_count = m.get('VulnerabilityDealedCount')
        return self


class DescribeScreenOperateInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeScreenOperateInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeScreenOperateInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScreenOssUploadInfoResponseBody(TeaModel):
    def __init__(
        self,
        access_id: str = None,
        expire: int = None,
        host: str = None,
        key: str = None,
        policy: str = None,
        request_id: str = None,
        security_token: str = None,
        signature: str = None,
    ):
        self.access_id = access_id
        self.expire = expire
        self.host = host
        self.key = key
        self.policy = policy
        self.request_id = request_id
        self.security_token = security_token
        self.signature = signature

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.host is not None:
            result['Host'] = self.host
        if self.key is not None:
            result['Key'] = self.key
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.signature is not None:
            result['Signature'] = self.signature
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        return self


class DescribeScreenOssUploadInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeScreenOssUploadInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeScreenOssUploadInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScreenScoreThreadRequest(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        start_time: int = None,
    ):
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeScreenScoreThreadResponseBodyData(TeaModel):
    def __init__(
        self,
        socre_thread: List[str] = None,
        socre_thread_date: List[str] = None,
    ):
        self.socre_thread = socre_thread
        self.socre_thread_date = socre_thread_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.socre_thread is not None:
            result['SocreThread'] = self.socre_thread
        if self.socre_thread_date is not None:
            result['SocreThreadDate'] = self.socre_thread_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SocreThread') is not None:
            self.socre_thread = m.get('SocreThread')
        if m.get('SocreThreadDate') is not None:
            self.socre_thread_date = m.get('SocreThreadDate')
        return self


class DescribeScreenScoreThreadResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeScreenScoreThreadResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeScreenScoreThreadResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeScreenScoreThreadResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeScreenScoreThreadResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeScreenScoreThreadResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScreenSecurityStatInfoResponseBodyAttackEvent(TeaModel):
    def __init__(
        self,
        date_array: List[str] = None,
        total_count: int = None,
        value_array: List[str] = None,
    ):
        self.date_array = date_array
        self.total_count = total_count
        self.value_array = value_array

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_array is not None:
            result['DateArray'] = self.date_array
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.value_array is not None:
            result['ValueArray'] = self.value_array
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DateArray') is not None:
            self.date_array = m.get('DateArray')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('ValueArray') is not None:
            self.value_array = m.get('ValueArray')
        return self


class DescribeScreenSecurityStatInfoResponseBodyHealthCheck(TeaModel):
    def __init__(
        self,
        date_array: List[str] = None,
        high_count: int = None,
        high_list: List[str] = None,
        levels_on: List[str] = None,
        low_count: int = None,
        low_list: List[str] = None,
        medium_count: int = None,
        medium_list: List[str] = None,
        total_count: int = None,
        value_array: List[str] = None,
    ):
        self.date_array = date_array
        self.high_count = high_count
        self.high_list = high_list
        self.levels_on = levels_on
        self.low_count = low_count
        self.low_list = low_list
        self.medium_count = medium_count
        self.medium_list = medium_list
        self.total_count = total_count
        self.value_array = value_array

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_array is not None:
            result['DateArray'] = self.date_array
        if self.high_count is not None:
            result['HighCount'] = self.high_count
        if self.high_list is not None:
            result['HighList'] = self.high_list
        if self.levels_on is not None:
            result['LevelsOn'] = self.levels_on
        if self.low_count is not None:
            result['LowCount'] = self.low_count
        if self.low_list is not None:
            result['LowList'] = self.low_list
        if self.medium_count is not None:
            result['MediumCount'] = self.medium_count
        if self.medium_list is not None:
            result['MediumList'] = self.medium_list
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.value_array is not None:
            result['ValueArray'] = self.value_array
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DateArray') is not None:
            self.date_array = m.get('DateArray')
        if m.get('HighCount') is not None:
            self.high_count = m.get('HighCount')
        if m.get('HighList') is not None:
            self.high_list = m.get('HighList')
        if m.get('LevelsOn') is not None:
            self.levels_on = m.get('LevelsOn')
        if m.get('LowCount') is not None:
            self.low_count = m.get('LowCount')
        if m.get('LowList') is not None:
            self.low_list = m.get('LowList')
        if m.get('MediumCount') is not None:
            self.medium_count = m.get('MediumCount')
        if m.get('MediumList') is not None:
            self.medium_list = m.get('MediumList')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('ValueArray') is not None:
            self.value_array = m.get('ValueArray')
        return self


class DescribeScreenSecurityStatInfoResponseBodySecurityEvent(TeaModel):
    def __init__(
        self,
        date_array: List[str] = None,
        levels_on: List[str] = None,
        remind_count: int = None,
        remind_list: List[str] = None,
        serious_count: int = None,
        serious_list: List[str] = None,
        suspicious_count: int = None,
        suspicious_list: List[str] = None,
        total_count: int = None,
        value_array: List[str] = None,
    ):
        self.date_array = date_array
        self.levels_on = levels_on
        self.remind_count = remind_count
        self.remind_list = remind_list
        self.serious_count = serious_count
        self.serious_list = serious_list
        self.suspicious_count = suspicious_count
        self.suspicious_list = suspicious_list
        self.total_count = total_count
        self.value_array = value_array

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_array is not None:
            result['DateArray'] = self.date_array
        if self.levels_on is not None:
            result['LevelsOn'] = self.levels_on
        if self.remind_count is not None:
            result['RemindCount'] = self.remind_count
        if self.remind_list is not None:
            result['RemindList'] = self.remind_list
        if self.serious_count is not None:
            result['SeriousCount'] = self.serious_count
        if self.serious_list is not None:
            result['SeriousList'] = self.serious_list
        if self.suspicious_count is not None:
            result['SuspiciousCount'] = self.suspicious_count
        if self.suspicious_list is not None:
            result['SuspiciousList'] = self.suspicious_list
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.value_array is not None:
            result['ValueArray'] = self.value_array
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DateArray') is not None:
            self.date_array = m.get('DateArray')
        if m.get('LevelsOn') is not None:
            self.levels_on = m.get('LevelsOn')
        if m.get('RemindCount') is not None:
            self.remind_count = m.get('RemindCount')
        if m.get('RemindList') is not None:
            self.remind_list = m.get('RemindList')
        if m.get('SeriousCount') is not None:
            self.serious_count = m.get('SeriousCount')
        if m.get('SeriousList') is not None:
            self.serious_list = m.get('SeriousList')
        if m.get('SuspiciousCount') is not None:
            self.suspicious_count = m.get('SuspiciousCount')
        if m.get('SuspiciousList') is not None:
            self.suspicious_list = m.get('SuspiciousList')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('ValueArray') is not None:
            self.value_array = m.get('ValueArray')
        return self


class DescribeScreenSecurityStatInfoResponseBodyVulnerability(TeaModel):
    def __init__(
        self,
        asap_count: int = None,
        asap_list: List[str] = None,
        date_array: List[str] = None,
        later_count: int = None,
        later_list: List[str] = None,
        levels_on: List[str] = None,
        nntf_count: int = None,
        nntf_list: List[str] = None,
        total_count: int = None,
        value_array: List[str] = None,
    ):
        self.asap_count = asap_count
        self.asap_list = asap_list
        self.date_array = date_array
        self.later_count = later_count
        self.later_list = later_list
        self.levels_on = levels_on
        self.nntf_count = nntf_count
        self.nntf_list = nntf_list
        self.total_count = total_count
        self.value_array = value_array

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asap_count is not None:
            result['AsapCount'] = self.asap_count
        if self.asap_list is not None:
            result['AsapList'] = self.asap_list
        if self.date_array is not None:
            result['DateArray'] = self.date_array
        if self.later_count is not None:
            result['LaterCount'] = self.later_count
        if self.later_list is not None:
            result['LaterList'] = self.later_list
        if self.levels_on is not None:
            result['LevelsOn'] = self.levels_on
        if self.nntf_count is not None:
            result['NntfCount'] = self.nntf_count
        if self.nntf_list is not None:
            result['NntfList'] = self.nntf_list
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.value_array is not None:
            result['ValueArray'] = self.value_array
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsapCount') is not None:
            self.asap_count = m.get('AsapCount')
        if m.get('AsapList') is not None:
            self.asap_list = m.get('AsapList')
        if m.get('DateArray') is not None:
            self.date_array = m.get('DateArray')
        if m.get('LaterCount') is not None:
            self.later_count = m.get('LaterCount')
        if m.get('LaterList') is not None:
            self.later_list = m.get('LaterList')
        if m.get('LevelsOn') is not None:
            self.levels_on = m.get('LevelsOn')
        if m.get('NntfCount') is not None:
            self.nntf_count = m.get('NntfCount')
        if m.get('NntfList') is not None:
            self.nntf_list = m.get('NntfList')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('ValueArray') is not None:
            self.value_array = m.get('ValueArray')
        return self


class DescribeScreenSecurityStatInfoResponseBody(TeaModel):
    def __init__(
        self,
        attack_event: DescribeScreenSecurityStatInfoResponseBodyAttackEvent = None,
        health_check: DescribeScreenSecurityStatInfoResponseBodyHealthCheck = None,
        request_id: str = None,
        security_event: DescribeScreenSecurityStatInfoResponseBodySecurityEvent = None,
        vulnerability: DescribeScreenSecurityStatInfoResponseBodyVulnerability = None,
    ):
        self.attack_event = attack_event
        self.health_check = health_check
        self.request_id = request_id
        self.security_event = security_event
        self.vulnerability = vulnerability

    def validate(self):
        if self.attack_event:
            self.attack_event.validate()
        if self.health_check:
            self.health_check.validate()
        if self.security_event:
            self.security_event.validate()
        if self.vulnerability:
            self.vulnerability.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attack_event is not None:
            result['AttackEvent'] = self.attack_event.to_map()
        if self.health_check is not None:
            result['HealthCheck'] = self.health_check.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.security_event is not None:
            result['SecurityEvent'] = self.security_event.to_map()
        if self.vulnerability is not None:
            result['Vulnerability'] = self.vulnerability.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttackEvent') is not None:
            temp_model = DescribeScreenSecurityStatInfoResponseBodyAttackEvent()
            self.attack_event = temp_model.from_map(m['AttackEvent'])
        if m.get('HealthCheck') is not None:
            temp_model = DescribeScreenSecurityStatInfoResponseBodyHealthCheck()
            self.health_check = temp_model.from_map(m['HealthCheck'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecurityEvent') is not None:
            temp_model = DescribeScreenSecurityStatInfoResponseBodySecurityEvent()
            self.security_event = temp_model.from_map(m['SecurityEvent'])
        if m.get('Vulnerability') is not None:
            temp_model = DescribeScreenSecurityStatInfoResponseBodyVulnerability()
            self.vulnerability = temp_model.from_map(m['Vulnerability'])
        return self


class DescribeScreenSecurityStatInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeScreenSecurityStatInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeScreenSecurityStatInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScreenSettingRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeScreenSettingResponseBody(TeaModel):
    def __init__(
        self,
        logo_power: bool = None,
        logo_url: str = None,
        monitor_url: str = None,
        request_id: str = None,
        screen_data_map: str = None,
        screen_default: int = None,
        screen_id: int = None,
        title: str = None,
    ):
        self.logo_power = logo_power
        self.logo_url = logo_url
        self.monitor_url = monitor_url
        self.request_id = request_id
        self.screen_data_map = screen_data_map
        self.screen_default = screen_default
        self.screen_id = screen_id
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logo_power is not None:
            result['LogoPower'] = self.logo_power
        if self.logo_url is not None:
            result['LogoUrl'] = self.logo_url
        if self.monitor_url is not None:
            result['MonitorUrl'] = self.monitor_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.screen_data_map is not None:
            result['ScreenDataMap'] = self.screen_data_map
        if self.screen_default is not None:
            result['ScreenDefault'] = self.screen_default
        if self.screen_id is not None:
            result['ScreenId'] = self.screen_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogoPower') is not None:
            self.logo_power = m.get('LogoPower')
        if m.get('LogoUrl') is not None:
            self.logo_url = m.get('LogoUrl')
        if m.get('MonitorUrl') is not None:
            self.monitor_url = m.get('MonitorUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScreenDataMap') is not None:
            self.screen_data_map = m.get('ScreenDataMap')
        if m.get('ScreenDefault') is not None:
            self.screen_default = m.get('ScreenDefault')
        if m.get('ScreenId') is not None:
            self.screen_id = m.get('ScreenId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class DescribeScreenSettingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeScreenSettingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeScreenSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScreenSummaryInfoResponseBody(TeaModel):
    def __init__(
        self,
        aegis_client_offline_count: int = None,
        aegis_client_online_count: int = None,
        request_id: str = None,
        security_score: int = None,
    ):
        self.aegis_client_offline_count = aegis_client_offline_count
        self.aegis_client_online_count = aegis_client_online_count
        self.request_id = request_id
        self.security_score = security_score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aegis_client_offline_count is not None:
            result['AegisClientOfflineCount'] = self.aegis_client_offline_count
        if self.aegis_client_online_count is not None:
            result['AegisClientOnlineCount'] = self.aegis_client_online_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.security_score is not None:
            result['SecurityScore'] = self.security_score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AegisClientOfflineCount') is not None:
            self.aegis_client_offline_count = m.get('AegisClientOfflineCount')
        if m.get('AegisClientOnlineCount') is not None:
            self.aegis_client_online_count = m.get('AegisClientOnlineCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecurityScore') is not None:
            self.security_score = m.get('SecurityScore')
        return self


class DescribeScreenSummaryInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeScreenSummaryInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeScreenSummaryInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScreenTitlesResponseBodySasScreenSettingList(TeaModel):
    def __init__(
        self,
        screen_id: int = None,
        screen_title: str = None,
    ):
        self.screen_id = screen_id
        self.screen_title = screen_title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.screen_id is not None:
            result['ScreenID'] = self.screen_id
        if self.screen_title is not None:
            result['ScreenTitle'] = self.screen_title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ScreenID') is not None:
            self.screen_id = m.get('ScreenID')
        if m.get('ScreenTitle') is not None:
            self.screen_title = m.get('ScreenTitle')
        return self


class DescribeScreenTitlesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        sas_screen_setting_list: List[DescribeScreenTitlesResponseBodySasScreenSettingList] = None,
    ):
        self.request_id = request_id
        self.sas_screen_setting_list = sas_screen_setting_list

    def validate(self):
        if self.sas_screen_setting_list:
            for k in self.sas_screen_setting_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SasScreenSettingList'] = []
        if self.sas_screen_setting_list is not None:
            for k in self.sas_screen_setting_list:
                result['SasScreenSettingList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.sas_screen_setting_list = []
        if m.get('SasScreenSettingList') is not None:
            for k in m.get('SasScreenSettingList'):
                temp_model = DescribeScreenTitlesResponseBodySasScreenSettingList()
                self.sas_screen_setting_list.append(temp_model.from_map(k))
        return self


class DescribeScreenTitlesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeScreenTitlesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeScreenTitlesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScreenUploadPictureRequest(TeaModel):
    def __init__(
        self,
        logo_url: str = None,
    ):
        # This parameter is required.
        self.logo_url = logo_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logo_url is not None:
            result['LogoUrl'] = self.logo_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogoUrl') is not None:
            self.logo_url = m.get('LogoUrl')
        return self


class DescribeScreenUploadPictureResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        url: str = None,
    ):
        self.request_id = request_id
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeScreenUploadPictureResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeScreenUploadPictureResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeScreenUploadPictureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScreenVersionConfigResponseBody(TeaModel):
    def __init__(
        self,
        asset_level: int = None,
        instance_id: str = None,
        is_trial_version: int = None,
        release_time: int = None,
        request_id: str = None,
        sas_log: int = None,
        sas_screen: int = None,
        version: int = None,
    ):
        self.asset_level = asset_level
        self.instance_id = instance_id
        self.is_trial_version = is_trial_version
        self.release_time = release_time
        self.request_id = request_id
        self.sas_log = sas_log
        self.sas_screen = sas_screen
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asset_level is not None:
            result['AssetLevel'] = self.asset_level
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.is_trial_version is not None:
            result['IsTrialVersion'] = self.is_trial_version
        if self.release_time is not None:
            result['ReleaseTime'] = self.release_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sas_log is not None:
            result['SasLog'] = self.sas_log
        if self.sas_screen is not None:
            result['SasScreen'] = self.sas_screen
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetLevel') is not None:
            self.asset_level = m.get('AssetLevel')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IsTrialVersion') is not None:
            self.is_trial_version = m.get('IsTrialVersion')
        if m.get('ReleaseTime') is not None:
            self.release_time = m.get('ReleaseTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SasLog') is not None:
            self.sas_log = m.get('SasLog')
        if m.get('SasScreen') is not None:
            self.sas_screen = m.get('SasScreen')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeScreenVersionConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeScreenVersionConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeScreenVersionConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFileDetectResultInnerRequest(TeaModel):
    def __init__(
        self,
        dna_hash_key_list: List[str] = None,
        hash_key_list: List[str] = None,
        level: int = None,
        source_ip: str = None,
        type: int = None,
    ):
        self.dna_hash_key_list = dna_hash_key_list
        # This parameter is required.
        self.hash_key_list = hash_key_list
        self.level = level
        self.source_ip = source_ip
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dna_hash_key_list is not None:
            result['DnaHashKeyList'] = self.dna_hash_key_list
        if self.hash_key_list is not None:
            result['HashKeyList'] = self.hash_key_list
        if self.level is not None:
            result['Level'] = self.level
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DnaHashKeyList') is not None:
            self.dna_hash_key_list = m.get('DnaHashKeyList')
        if m.get('HashKeyList') is not None:
            self.hash_key_list = m.get('HashKeyList')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetFileDetectResultInnerResponseBodyResultList(TeaModel):
    def __init__(
        self,
        code: str = None,
        expire_time: str = None,
        ext: str = None,
        hash_key: str = None,
        message: str = None,
        result: int = None,
        score: int = None,
        virus_type: str = None,
    ):
        self.code = code
        self.expire_time = expire_time
        self.ext = ext
        self.hash_key = hash_key
        self.message = message
        self.result = result
        self.score = score
        self.virus_type = virus_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.hash_key is not None:
            result['HashKey'] = self.hash_key
        if self.message is not None:
            result['Message'] = self.message
        if self.result is not None:
            result['Result'] = self.result
        if self.score is not None:
            result['Score'] = self.score
        if self.virus_type is not None:
            result['VirusType'] = self.virus_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('HashKey') is not None:
            self.hash_key = m.get('HashKey')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('VirusType') is not None:
            self.virus_type = m.get('VirusType')
        return self


class GetFileDetectResultInnerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_list: List[GetFileDetectResultInnerResponseBodyResultList] = None,
    ):
        self.request_id = request_id
        self.result_list = result_list

    def validate(self):
        if self.result_list:
            for k in self.result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ResultList'] = []
        if self.result_list is not None:
            for k in self.result_list:
                result['ResultList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result_list = []
        if m.get('ResultList') is not None:
            for k in m.get('ResultList'):
                temp_model = GetFileDetectResultInnerResponseBodyResultList()
                self.result_list.append(temp_model.from_map(k))
        return self


class GetFileDetectResultInnerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFileDetectResultInnerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetFileDetectResultInnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGlobalUserConfigRequest(TeaModel):
    def __init__(
        self,
        module_list: List[str] = None,
    ):
        self.module_list = module_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.module_list is not None:
            result['ModuleList'] = self.module_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModuleList') is not None:
            self.module_list = m.get('ModuleList')
        return self


class ListGlobalUserConfigShrinkRequest(TeaModel):
    def __init__(
        self,
        module_list_shrink: str = None,
    ):
        self.module_list_shrink = module_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.module_list_shrink is not None:
            result['ModuleList'] = self.module_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModuleList') is not None:
            self.module_list_shrink = m.get('ModuleList')
        return self


class ListGlobalUserConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        global_config_switch: bool = None,
        module_name: str = None,
    ):
        self.global_config_switch = global_config_switch
        self.module_name = module_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.global_config_switch is not None:
            result['GlobalConfigSwitch'] = self.global_config_switch
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GlobalConfigSwitch') is not None:
            self.global_config_switch = m.get('GlobalConfigSwitch')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        return self


class ListGlobalUserConfigResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListGlobalUserConfigResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListGlobalUserConfigResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListGlobalUserConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListGlobalUserConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListGlobalUserConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


