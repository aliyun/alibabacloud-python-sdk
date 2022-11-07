# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict


class CreateAlarmEventRequest(TeaModel):
    def __init__(
        self,
        alarm_id: str = None,
        alarm_timestamp: int = None,
        app_key: str = None,
        app_secret: str = None,
        attach: str = None,
        dynamic_alarm_id: str = None,
        impact: str = None,
        link: str = None,
        message: str = None,
        region: str = None,
        source_key: str = None,
        source_system: str = None,
        strategy: str = None,
        title: str = None,
        uid: str = None,
    ):
        self.alarm_id = alarm_id
        self.alarm_timestamp = alarm_timestamp
        self.app_key = app_key
        self.app_secret = app_secret
        self.attach = attach
        self.dynamic_alarm_id = dynamic_alarm_id
        self.impact = impact
        self.link = link
        self.message = message
        self.region = region
        self.source_key = source_key
        self.source_system = source_system
        self.strategy = strategy
        self.title = title
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id
        if self.alarm_timestamp is not None:
            result['AlarmTimestamp'] = self.alarm_timestamp
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret
        if self.attach is not None:
            result['Attach'] = self.attach
        if self.dynamic_alarm_id is not None:
            result['DynamicAlarmId'] = self.dynamic_alarm_id
        if self.impact is not None:
            result['Impact'] = self.impact
        if self.link is not None:
            result['Link'] = self.link
        if self.message is not None:
            result['Message'] = self.message
        if self.region is not None:
            result['Region'] = self.region
        if self.source_key is not None:
            result['SourceKey'] = self.source_key
        if self.source_system is not None:
            result['SourceSystem'] = self.source_system
        if self.strategy is not None:
            result['Strategy'] = self.strategy
        if self.title is not None:
            result['Title'] = self.title
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')
        if m.get('AlarmTimestamp') is not None:
            self.alarm_timestamp = m.get('AlarmTimestamp')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('AppSecret') is not None:
            self.app_secret = m.get('AppSecret')
        if m.get('Attach') is not None:
            self.attach = m.get('Attach')
        if m.get('DynamicAlarmId') is not None:
            self.dynamic_alarm_id = m.get('DynamicAlarmId')
        if m.get('Impact') is not None:
            self.impact = m.get('Impact')
        if m.get('Link') is not None:
            self.link = m.get('Link')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('SourceKey') is not None:
            self.source_key = m.get('SourceKey')
        if m.get('SourceSystem') is not None:
            self.source_system = m.get('SourceSystem')
        if m.get('Strategy') is not None:
            self.strategy = m.get('Strategy')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class CreateAlarmEventResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateAlarmEventResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAlarmEventResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateAlarmEventResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFaultDetailRequest(TeaModel):
    def __init__(
        self,
        app_key: str = None,
        app_secret: str = None,
        vid: str = None,
    ):
        self.app_key = app_key
        self.app_secret = app_secret
        self.vid = vid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret
        if self.vid is not None:
            result['Vid'] = self.vid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('AppSecret') is not None:
            self.app_secret = m.get('AppSecret')
        if m.get('Vid') is not None:
            self.vid = m.get('Vid')
        return self


class GetFaultDetailResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetFaultDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFaultDetailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetFaultDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReportInfluenceRequest(TeaModel):
    def __init__(
        self,
        app_key: str = None,
        app_secret: str = None,
        area: str = None,
        channel_code: str = None,
        cluster: str = None,
        create_id: str = None,
        customer_impact_desc: str = None,
        fault_vid: str = None,
        issue_desc: str = None,
        product_line_id: int = None,
        regions: str = None,
        room: str = None,
        time: int = None,
        total_desc: str = None,
    ):
        self.app_key = app_key
        self.app_secret = app_secret
        self.area = area
        self.channel_code = channel_code
        self.cluster = cluster
        self.create_id = create_id
        self.customer_impact_desc = customer_impact_desc
        self.fault_vid = fault_vid
        self.issue_desc = issue_desc
        self.product_line_id = product_line_id
        self.regions = regions
        self.room = room
        self.time = time
        self.total_desc = total_desc

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret
        if self.area is not None:
            result['Area'] = self.area
        if self.channel_code is not None:
            result['ChannelCode'] = self.channel_code
        if self.cluster is not None:
            result['Cluster'] = self.cluster
        if self.create_id is not None:
            result['CreateId'] = self.create_id
        if self.customer_impact_desc is not None:
            result['CustomerImpactDesc'] = self.customer_impact_desc
        if self.fault_vid is not None:
            result['FaultVid'] = self.fault_vid
        if self.issue_desc is not None:
            result['IssueDesc'] = self.issue_desc
        if self.product_line_id is not None:
            result['ProductLineId'] = self.product_line_id
        if self.regions is not None:
            result['Regions'] = self.regions
        if self.room is not None:
            result['Room'] = self.room
        if self.time is not None:
            result['Time'] = self.time
        if self.total_desc is not None:
            result['TotalDesc'] = self.total_desc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('AppSecret') is not None:
            self.app_secret = m.get('AppSecret')
        if m.get('Area') is not None:
            self.area = m.get('Area')
        if m.get('ChannelCode') is not None:
            self.channel_code = m.get('ChannelCode')
        if m.get('Cluster') is not None:
            self.cluster = m.get('Cluster')
        if m.get('CreateId') is not None:
            self.create_id = m.get('CreateId')
        if m.get('CustomerImpactDesc') is not None:
            self.customer_impact_desc = m.get('CustomerImpactDesc')
        if m.get('FaultVid') is not None:
            self.fault_vid = m.get('FaultVid')
        if m.get('IssueDesc') is not None:
            self.issue_desc = m.get('IssueDesc')
        if m.get('ProductLineId') is not None:
            self.product_line_id = m.get('ProductLineId')
        if m.get('Regions') is not None:
            self.regions = m.get('Regions')
        if m.get('Room') is not None:
            self.room = m.get('Room')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('TotalDesc') is not None:
            self.total_desc = m.get('TotalDesc')
        return self


class ReportInfluenceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ReportInfluenceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReportInfluenceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ReportInfluenceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReportReasonDetailRequest(TeaModel):
    def __init__(
        self,
        app_key: str = None,
        app_secret: str = None,
        channel_code: str = None,
        create_id: str = None,
        detail_url: str = None,
        fault_vid: str = None,
        reason: str = None,
    ):
        self.app_key = app_key
        self.app_secret = app_secret
        self.channel_code = channel_code
        self.create_id = create_id
        self.detail_url = detail_url
        self.fault_vid = fault_vid
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret
        if self.channel_code is not None:
            result['ChannelCode'] = self.channel_code
        if self.create_id is not None:
            result['CreateId'] = self.create_id
        if self.detail_url is not None:
            result['DetailUrl'] = self.detail_url
        if self.fault_vid is not None:
            result['FaultVid'] = self.fault_vid
        if self.reason is not None:
            result['Reason'] = self.reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('AppSecret') is not None:
            self.app_secret = m.get('AppSecret')
        if m.get('ChannelCode') is not None:
            self.channel_code = m.get('ChannelCode')
        if m.get('CreateId') is not None:
            self.create_id = m.get('CreateId')
        if m.get('DetailUrl') is not None:
            self.detail_url = m.get('DetailUrl')
        if m.get('FaultVid') is not None:
            self.fault_vid = m.get('FaultVid')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        return self


class ReportReasonDetailResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ReportReasonDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReportReasonDetailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ReportReasonDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReportRecoverActionRequest(TeaModel):
    def __init__(
        self,
        action_type: int = None,
        app_key: str = None,
        app_secret: str = None,
        channel_code: str = None,
        create_id: str = None,
        current_desc: str = None,
        current_progress: int = None,
        expected_repaired_time: int = None,
        fault_vid: str = None,
        is_recovery: int = None,
        product_line_id: int = None,
        recovery_duration: int = None,
        recovery_time: int = None,
    ):
        self.action_type = action_type
        self.app_key = app_key
        self.app_secret = app_secret
        self.channel_code = channel_code
        self.create_id = create_id
        self.current_desc = current_desc
        self.current_progress = current_progress
        self.expected_repaired_time = expected_repaired_time
        self.fault_vid = fault_vid
        self.is_recovery = is_recovery
        self.product_line_id = product_line_id
        self.recovery_duration = recovery_duration
        self.recovery_time = recovery_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret
        if self.channel_code is not None:
            result['ChannelCode'] = self.channel_code
        if self.create_id is not None:
            result['CreateId'] = self.create_id
        if self.current_desc is not None:
            result['CurrentDesc'] = self.current_desc
        if self.current_progress is not None:
            result['CurrentProgress'] = self.current_progress
        if self.expected_repaired_time is not None:
            result['ExpectedRepairedTime'] = self.expected_repaired_time
        if self.fault_vid is not None:
            result['FaultVid'] = self.fault_vid
        if self.is_recovery is not None:
            result['IsRecovery'] = self.is_recovery
        if self.product_line_id is not None:
            result['ProductLineId'] = self.product_line_id
        if self.recovery_duration is not None:
            result['RecoveryDuration'] = self.recovery_duration
        if self.recovery_time is not None:
            result['RecoveryTime'] = self.recovery_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('AppSecret') is not None:
            self.app_secret = m.get('AppSecret')
        if m.get('ChannelCode') is not None:
            self.channel_code = m.get('ChannelCode')
        if m.get('CreateId') is not None:
            self.create_id = m.get('CreateId')
        if m.get('CurrentDesc') is not None:
            self.current_desc = m.get('CurrentDesc')
        if m.get('CurrentProgress') is not None:
            self.current_progress = m.get('CurrentProgress')
        if m.get('ExpectedRepairedTime') is not None:
            self.expected_repaired_time = m.get('ExpectedRepairedTime')
        if m.get('FaultVid') is not None:
            self.fault_vid = m.get('FaultVid')
        if m.get('IsRecovery') is not None:
            self.is_recovery = m.get('IsRecovery')
        if m.get('ProductLineId') is not None:
            self.product_line_id = m.get('ProductLineId')
        if m.get('RecoveryDuration') is not None:
            self.recovery_duration = m.get('RecoveryDuration')
        if m.get('RecoveryTime') is not None:
            self.recovery_time = m.get('RecoveryTime')
        return self


class ReportRecoverActionResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ReportRecoverActionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReportRecoverActionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ReportRecoverActionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


