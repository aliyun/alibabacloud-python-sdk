# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class DescribeHuYaRecordByDomainRequest(TeaModel):
    def __init__(
        self,
        business_type: str = None,
        domain: str = None,
        end_time: str = None,
        start_time: str = None,
    ):
        self.business_type = business_type
        self.domain = domain
        self.end_time = end_time
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeHuYaRecordByDomainResponseBodyResultDesc(TeaModel):
    def __init__(
        self,
        business_type: str = None,
        domain: str = None,
        record_duration: int = None,
        record_num: int = None,
        record_type: str = None,
        time: str = None,
    ):
        self.business_type = business_type
        self.domain = domain
        self.record_duration = record_duration
        self.record_num = record_num
        self.record_type = record_type
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.record_duration is not None:
            result['RecordDuration'] = self.record_duration
        if self.record_num is not None:
            result['RecordNum'] = self.record_num
        if self.record_type is not None:
            result['RecordType'] = self.record_type
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('RecordDuration') is not None:
            self.record_duration = m.get('RecordDuration')
        if m.get('RecordNum') is not None:
            self.record_num = m.get('RecordNum')
        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class DescribeHuYaRecordByDomainResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
        result_desc: List[DescribeHuYaRecordByDomainResponseBodyResultDesc] = None,
        status: int = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.result = result
        self.result_desc = result_desc
        self.status = status

    def validate(self):
        if self.result_desc:
            for k in self.result_desc:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        result['ResultDesc'] = []
        if self.result_desc is not None:
            for k in self.result_desc:
                result['ResultDesc'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        self.result_desc = []
        if m.get('ResultDesc') is not None:
            for k in m.get('ResultDesc'):
                temp_model = DescribeHuYaRecordByDomainResponseBodyResultDesc()
                self.result_desc.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeHuYaRecordByDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeHuYaRecordByDomainResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeHuYaRecordByDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHuYaScreenshotByDomainRequest(TeaModel):
    def __init__(
        self,
        business_type: str = None,
        domain: str = None,
        end_time: str = None,
        start_time: str = None,
    ):
        self.business_type = business_type
        self.domain = domain
        self.end_time = end_time
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeHuYaScreenshotByDomainResponseBodyResultDesc(TeaModel):
    def __init__(
        self,
        business_type: str = None,
        domain: str = None,
        screenshot_num: int = None,
        time: str = None,
    ):
        self.business_type = business_type
        self.domain = domain
        self.screenshot_num = screenshot_num
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.screenshot_num is not None:
            result['ScreenshotNum'] = self.screenshot_num
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('ScreenshotNum') is not None:
            self.screenshot_num = m.get('ScreenshotNum')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class DescribeHuYaScreenshotByDomainResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
        result_desc: List[DescribeHuYaScreenshotByDomainResponseBodyResultDesc] = None,
        status: int = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.result = result
        self.result_desc = result_desc
        self.status = status

    def validate(self):
        if self.result_desc:
            for k in self.result_desc:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        result['ResultDesc'] = []
        if self.result_desc is not None:
            for k in self.result_desc:
                result['ResultDesc'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        self.result_desc = []
        if m.get('ResultDesc') is not None:
            for k in m.get('ResultDesc'):
                temp_model = DescribeHuYaScreenshotByDomainResponseBodyResultDesc()
                self.result_desc.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeHuYaScreenshotByDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeHuYaScreenshotByDomainResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeHuYaScreenshotByDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHuYaTranscodeByDomainRequest(TeaModel):
    def __init__(
        self,
        business_type: str = None,
        domain: str = None,
        end_time: str = None,
        start_time: str = None,
    ):
        self.business_type = business_type
        self.domain = domain
        self.end_time = end_time
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeHuYaTranscodeByDomainResponseBodyResultDesc(TeaModel):
    def __init__(
        self,
        business_type: str = None,
        domain: str = None,
        time: str = None,
        transcode_duration: int = None,
        transcode_num: int = None,
        transcode_type: str = None,
    ):
        self.business_type = business_type
        self.domain = domain
        self.time = time
        self.transcode_duration = transcode_duration
        self.transcode_num = transcode_num
        self.transcode_type = transcode_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.time is not None:
            result['Time'] = self.time
        if self.transcode_duration is not None:
            result['TranscodeDuration'] = self.transcode_duration
        if self.transcode_num is not None:
            result['TranscodeNum'] = self.transcode_num
        if self.transcode_type is not None:
            result['TranscodeType'] = self.transcode_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('TranscodeDuration') is not None:
            self.transcode_duration = m.get('TranscodeDuration')
        if m.get('TranscodeNum') is not None:
            self.transcode_num = m.get('TranscodeNum')
        if m.get('TranscodeType') is not None:
            self.transcode_type = m.get('TranscodeType')
        return self


class DescribeHuYaTranscodeByDomainResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
        result_desc: List[DescribeHuYaTranscodeByDomainResponseBodyResultDesc] = None,
        status: int = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.result = result
        self.result_desc = result_desc
        self.status = status

    def validate(self):
        if self.result_desc:
            for k in self.result_desc:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        result['ResultDesc'] = []
        if self.result_desc is not None:
            for k in self.result_desc:
                result['ResultDesc'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        self.result_desc = []
        if m.get('ResultDesc') is not None:
            for k in m.get('ResultDesc'):
                temp_model = DescribeHuYaTranscodeByDomainResponseBodyResultDesc()
                self.result_desc.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeHuYaTranscodeByDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeHuYaTranscodeByDomainResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeHuYaTranscodeByDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMeterBypassRtUsageByTaskProfileRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        end_ts: int = None,
        interval: int = None,
        service_area: str = None,
        start_ts: int = None,
    ):
        self.app_id = app_id
        self.end_ts = end_ts
        self.interval = interval
        self.service_area = service_area
        self.start_ts = start_ts

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.end_ts is not None:
            result['EndTs'] = self.end_ts
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.service_area is not None:
            result['ServiceArea'] = self.service_area
        if self.start_ts is not None:
            result['StartTs'] = self.start_ts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndTs') is not None:
            self.end_ts = m.get('EndTs')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('ServiceArea') is not None:
            self.service_area = m.get('ServiceArea')
        if m.get('StartTs') is not None:
            self.start_ts = m.get('StartTs')
        return self


class DescribeMeterBypassRtUsageByTaskProfileResponseBodyData(TeaModel):
    def __init__(
        self,
        duration: int = None,
        ratio: str = None,
        service_area: str = None,
        task_profile: str = None,
        timestamp: int = None,
        type: str = None,
    ):
        self.duration = duration
        self.ratio = ratio
        self.service_area = service_area
        self.task_profile = task_profile
        self.timestamp = timestamp
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.ratio is not None:
            result['Ratio'] = self.ratio
        if self.service_area is not None:
            result['ServiceArea'] = self.service_area
        if self.task_profile is not None:
            result['TaskProfile'] = self.task_profile
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')
        if m.get('ServiceArea') is not None:
            self.service_area = m.get('ServiceArea')
        if m.get('TaskProfile') is not None:
            self.task_profile = m.get('TaskProfile')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeMeterBypassRtUsageByTaskProfileResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DescribeMeterBypassRtUsageByTaskProfileResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
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
                temp_model = DescribeMeterBypassRtUsageByTaskProfileResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeMeterBypassRtUsageByTaskProfileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeMeterBypassRtUsageByTaskProfileResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeMeterBypassRtUsageByTaskProfileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMeterBypassUsageByTaskProfileRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        end_time: str = None,
        interval: int = None,
        service_area: str = None,
        start_time: str = None,
    ):
        self.app_id = app_id
        self.end_time = end_time
        self.interval = interval
        self.service_area = service_area
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.service_area is not None:
            result['ServiceArea'] = self.service_area
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('ServiceArea') is not None:
            self.service_area = m.get('ServiceArea')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeMeterBypassUsageByTaskProfileResponseBodyData(TeaModel):
    def __init__(
        self,
        duration: int = None,
        ratio: str = None,
        service_area: str = None,
        task_profile: str = None,
        timestamp: int = None,
        type: str = None,
    ):
        self.duration = duration
        self.ratio = ratio
        self.service_area = service_area
        self.task_profile = task_profile
        self.timestamp = timestamp
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.ratio is not None:
            result['Ratio'] = self.ratio
        if self.service_area is not None:
            result['ServiceArea'] = self.service_area
        if self.task_profile is not None:
            result['TaskProfile'] = self.task_profile
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')
        if m.get('ServiceArea') is not None:
            self.service_area = m.get('ServiceArea')
        if m.get('TaskProfile') is not None:
            self.task_profile = m.get('TaskProfile')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeMeterBypassUsageByTaskProfileResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DescribeMeterBypassUsageByTaskProfileResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
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
                temp_model = DescribeMeterBypassUsageByTaskProfileResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeMeterBypassUsageByTaskProfileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeMeterBypassUsageByTaskProfileResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeMeterBypassUsageByTaskProfileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMeterMpuTranscodeRtUsageByTaskProfileRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        end_ts: int = None,
        interval: int = None,
        service_area: str = None,
        start_ts: int = None,
    ):
        self.app_id = app_id
        self.end_ts = end_ts
        self.interval = interval
        self.service_area = service_area
        self.start_ts = start_ts

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.end_ts is not None:
            result['EndTs'] = self.end_ts
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.service_area is not None:
            result['ServiceArea'] = self.service_area
        if self.start_ts is not None:
            result['StartTs'] = self.start_ts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndTs') is not None:
            self.end_ts = m.get('EndTs')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('ServiceArea') is not None:
            self.service_area = m.get('ServiceArea')
        if m.get('StartTs') is not None:
            self.start_ts = m.get('StartTs')
        return self


class DescribeMeterMpuTranscodeRtUsageByTaskProfileResponseBodyData(TeaModel):
    def __init__(
        self,
        duration: int = None,
        service_area: str = None,
        task_profile: str = None,
        time_stamp: int = None,
    ):
        self.duration = duration
        self.service_area = service_area
        self.task_profile = task_profile
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.service_area is not None:
            result['ServiceArea'] = self.service_area
        if self.task_profile is not None:
            result['TaskProfile'] = self.task_profile
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('ServiceArea') is not None:
            self.service_area = m.get('ServiceArea')
        if m.get('TaskProfile') is not None:
            self.task_profile = m.get('TaskProfile')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeMeterMpuTranscodeRtUsageByTaskProfileResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DescribeMeterMpuTranscodeRtUsageByTaskProfileResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
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
                temp_model = DescribeMeterMpuTranscodeRtUsageByTaskProfileResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeMeterMpuTranscodeRtUsageByTaskProfileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeMeterMpuTranscodeRtUsageByTaskProfileResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeMeterMpuTranscodeRtUsageByTaskProfileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMeterRecordRtUsageByTaskProfileRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        end_ts: int = None,
        interval: int = None,
        service_area: str = None,
        start_ts: int = None,
    ):
        self.app_id = app_id
        self.end_ts = end_ts
        self.interval = interval
        self.service_area = service_area
        self.start_ts = start_ts

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.end_ts is not None:
            result['EndTs'] = self.end_ts
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.service_area is not None:
            result['ServiceArea'] = self.service_area
        if self.start_ts is not None:
            result['StartTs'] = self.start_ts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndTs') is not None:
            self.end_ts = m.get('EndTs')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('ServiceArea') is not None:
            self.service_area = m.get('ServiceArea')
        if m.get('StartTs') is not None:
            self.start_ts = m.get('StartTs')
        return self


class DescribeMeterRecordRtUsageByTaskProfileResponseBodyData(TeaModel):
    def __init__(
        self,
        duration: int = None,
        ratio: str = None,
        service_area: str = None,
        task_profile: str = None,
        timestamp: int = None,
        type: str = None,
    ):
        self.duration = duration
        self.ratio = ratio
        self.service_area = service_area
        self.task_profile = task_profile
        self.timestamp = timestamp
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.ratio is not None:
            result['Ratio'] = self.ratio
        if self.service_area is not None:
            result['ServiceArea'] = self.service_area
        if self.task_profile is not None:
            result['TaskProfile'] = self.task_profile
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')
        if m.get('ServiceArea') is not None:
            self.service_area = m.get('ServiceArea')
        if m.get('TaskProfile') is not None:
            self.task_profile = m.get('TaskProfile')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeMeterRecordRtUsageByTaskProfileResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DescribeMeterRecordRtUsageByTaskProfileResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
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
                temp_model = DescribeMeterRecordRtUsageByTaskProfileResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeMeterRecordRtUsageByTaskProfileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeMeterRecordRtUsageByTaskProfileResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeMeterRecordRtUsageByTaskProfileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMeterRecordUsageByTaskProfileRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        end_ts: int = None,
        interval: int = None,
        service_area: str = None,
        start_ts: int = None,
    ):
        self.app_id = app_id
        self.end_ts = end_ts
        self.interval = interval
        self.service_area = service_area
        self.start_ts = start_ts

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.end_ts is not None:
            result['EndTs'] = self.end_ts
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.service_area is not None:
            result['ServiceArea'] = self.service_area
        if self.start_ts is not None:
            result['StartTs'] = self.start_ts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndTs') is not None:
            self.end_ts = m.get('EndTs')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('ServiceArea') is not None:
            self.service_area = m.get('ServiceArea')
        if m.get('StartTs') is not None:
            self.start_ts = m.get('StartTs')
        return self


class DescribeMeterRecordUsageByTaskProfileResponseBodyRecordUsageVoList(TeaModel):
    def __init__(
        self,
        duration: int = None,
        ratio: str = None,
        service_area: str = None,
        task_profile: str = None,
        time_stamp: int = None,
        type: str = None,
    ):
        self.duration = duration
        self.ratio = ratio
        self.service_area = service_area
        self.task_profile = task_profile
        self.time_stamp = time_stamp
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.ratio is not None:
            result['Ratio'] = self.ratio
        if self.service_area is not None:
            result['ServiceArea'] = self.service_area
        if self.task_profile is not None:
            result['TaskProfile'] = self.task_profile
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')
        if m.get('ServiceArea') is not None:
            self.service_area = m.get('ServiceArea')
        if m.get('TaskProfile') is not None:
            self.task_profile = m.get('TaskProfile')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeMeterRecordUsageByTaskProfileResponseBody(TeaModel):
    def __init__(
        self,
        record_usage_vo_list: List[DescribeMeterRecordUsageByTaskProfileResponseBodyRecordUsageVoList] = None,
        request_id: str = None,
    ):
        self.record_usage_vo_list = record_usage_vo_list
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.record_usage_vo_list:
            for k in self.record_usage_vo_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RecordUsageVoList'] = []
        if self.record_usage_vo_list is not None:
            for k in self.record_usage_vo_list:
                result['RecordUsageVoList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.record_usage_vo_list = []
        if m.get('RecordUsageVoList') is not None:
            for k in m.get('RecordUsageVoList'):
                temp_model = DescribeMeterRecordUsageByTaskProfileResponseBodyRecordUsageVoList()
                self.record_usage_vo_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeMeterRecordUsageByTaskProfileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeMeterRecordUsageByTaskProfileResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeMeterRecordUsageByTaskProfileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMeterRtcApproxPeakRateRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        end_ts: int = None,
        interval: int = None,
        service_area: str = None,
        start_ts: int = None,
    ):
        self.app_id = app_id
        self.end_ts = end_ts
        self.interval = interval
        self.service_area = service_area
        self.start_ts = start_ts

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.end_ts is not None:
            result['EndTs'] = self.end_ts
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.service_area is not None:
            result['ServiceArea'] = self.service_area
        if self.start_ts is not None:
            result['StartTs'] = self.start_ts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndTs') is not None:
            self.end_ts = m.get('EndTs')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('ServiceArea') is not None:
            self.service_area = m.get('ServiceArea')
        if m.get('StartTs') is not None:
            self.start_ts = m.get('StartTs')
        return self


class DescribeMeterRtcApproxPeakRateResponseBodyPeakRateVoList(TeaModel):
    def __init__(
        self,
        peak_rate: float = None,
        peak_ts: int = None,
        timestamp: int = None,
    ):
        self.peak_rate = peak_rate
        self.peak_ts = peak_ts
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.peak_rate is not None:
            result['PeakRate'] = self.peak_rate
        if self.peak_ts is not None:
            result['PeakTs'] = self.peak_ts
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PeakRate') is not None:
            self.peak_rate = m.get('PeakRate')
        if m.get('PeakTs') is not None:
            self.peak_ts = m.get('PeakTs')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class DescribeMeterRtcApproxPeakRateResponseBody(TeaModel):
    def __init__(
        self,
        approx_peak_rate: float = None,
        approx_peak_ts: int = None,
        peak_rate_vo_list: List[DescribeMeterRtcApproxPeakRateResponseBodyPeakRateVoList] = None,
        request_id: str = None,
    ):
        self.approx_peak_rate = approx_peak_rate
        self.approx_peak_ts = approx_peak_ts
        self.peak_rate_vo_list = peak_rate_vo_list
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.peak_rate_vo_list:
            for k in self.peak_rate_vo_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approx_peak_rate is not None:
            result['ApproxPeakRate'] = self.approx_peak_rate
        if self.approx_peak_ts is not None:
            result['ApproxPeakTs'] = self.approx_peak_ts
        result['PeakRateVoList'] = []
        if self.peak_rate_vo_list is not None:
            for k in self.peak_rate_vo_list:
                result['PeakRateVoList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApproxPeakRate') is not None:
            self.approx_peak_rate = m.get('ApproxPeakRate')
        if m.get('ApproxPeakTs') is not None:
            self.approx_peak_ts = m.get('ApproxPeakTs')
        self.peak_rate_vo_list = []
        if m.get('PeakRateVoList') is not None:
            for k in m.get('PeakRateVoList'):
                temp_model = DescribeMeterRtcApproxPeakRateResponseBodyPeakRateVoList()
                self.peak_rate_vo_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeMeterRtcApproxPeakRateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeMeterRtcApproxPeakRateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeMeterRtcApproxPeakRateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMeterRtcBandWidthUsageRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        end_ts: int = None,
        interval: int = None,
        service_area: str = None,
        start_ts: int = None,
    ):
        self.app_id = app_id
        self.end_ts = end_ts
        self.interval = interval
        self.service_area = service_area
        self.start_ts = start_ts

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.end_ts is not None:
            result['EndTs'] = self.end_ts
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.service_area is not None:
            result['ServiceArea'] = self.service_area
        if self.start_ts is not None:
            result['StartTs'] = self.start_ts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndTs') is not None:
            self.end_ts = m.get('EndTs')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('ServiceArea') is not None:
            self.service_area = m.get('ServiceArea')
        if m.get('StartTs') is not None:
            self.start_ts = m.get('StartTs')
        return self


class DescribeMeterRtcBandWidthUsageResponseBodyRtcBandWidthUsageVoList(TeaModel):
    def __init__(
        self,
        anchor_peak_rate: float = None,
        anchor_peak_ts: int = None,
        audience_peak_rate: float = None,
        audience_peak_ts: int = None,
        peak_rate: float = None,
        peak_ts: int = None,
        timestamp: int = None,
    ):
        self.anchor_peak_rate = anchor_peak_rate
        self.anchor_peak_ts = anchor_peak_ts
        self.audience_peak_rate = audience_peak_rate
        self.audience_peak_ts = audience_peak_ts
        self.peak_rate = peak_rate
        self.peak_ts = peak_ts
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anchor_peak_rate is not None:
            result['AnchorPeakRate'] = self.anchor_peak_rate
        if self.anchor_peak_ts is not None:
            result['AnchorPeakTs'] = self.anchor_peak_ts
        if self.audience_peak_rate is not None:
            result['AudiencePeakRate'] = self.audience_peak_rate
        if self.audience_peak_ts is not None:
            result['AudiencePeakTs'] = self.audience_peak_ts
        if self.peak_rate is not None:
            result['PeakRate'] = self.peak_rate
        if self.peak_ts is not None:
            result['PeakTs'] = self.peak_ts
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnchorPeakRate') is not None:
            self.anchor_peak_rate = m.get('AnchorPeakRate')
        if m.get('AnchorPeakTs') is not None:
            self.anchor_peak_ts = m.get('AnchorPeakTs')
        if m.get('AudiencePeakRate') is not None:
            self.audience_peak_rate = m.get('AudiencePeakRate')
        if m.get('AudiencePeakTs') is not None:
            self.audience_peak_ts = m.get('AudiencePeakTs')
        if m.get('PeakRate') is not None:
            self.peak_rate = m.get('PeakRate')
        if m.get('PeakTs') is not None:
            self.peak_ts = m.get('PeakTs')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class DescribeMeterRtcBandWidthUsageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        rtc_band_width_usage_vo_list: List[DescribeMeterRtcBandWidthUsageResponseBodyRtcBandWidthUsageVoList] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.rtc_band_width_usage_vo_list = rtc_band_width_usage_vo_list

    def validate(self):
        if self.rtc_band_width_usage_vo_list:
            for k in self.rtc_band_width_usage_vo_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RtcBandWidthUsageVoList'] = []
        if self.rtc_band_width_usage_vo_list is not None:
            for k in self.rtc_band_width_usage_vo_list:
                result['RtcBandWidthUsageVoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.rtc_band_width_usage_vo_list = []
        if m.get('RtcBandWidthUsageVoList') is not None:
            for k in m.get('RtcBandWidthUsageVoList'):
                temp_model = DescribeMeterRtcBandWidthUsageResponseBodyRtcBandWidthUsageVoList()
                self.rtc_band_width_usage_vo_list.append(temp_model.from_map(k))
        return self


class DescribeMeterRtcBandWidthUsageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeMeterRtcBandWidthUsageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeMeterRtcBandWidthUsageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMeterRtcChannelCntDataRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        end_ts: int = None,
        interval: int = None,
        service_area: str = None,
        start_ts: int = None,
    ):
        self.app_id = app_id
        self.end_ts = end_ts
        self.interval = interval
        self.service_area = service_area
        self.start_ts = start_ts

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.end_ts is not None:
            result['EndTs'] = self.end_ts
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.service_area is not None:
            result['ServiceArea'] = self.service_area
        if self.start_ts is not None:
            result['StartTs'] = self.start_ts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndTs') is not None:
            self.end_ts = m.get('EndTs')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('ServiceArea') is not None:
            self.service_area = m.get('ServiceArea')
        if m.get('StartTs') is not None:
            self.start_ts = m.get('StartTs')
        return self


class DescribeMeterRtcChannelCntDataResponseBodyData(TeaModel):
    def __init__(
        self,
        channel_cnt: int = None,
        timestamp: str = None,
    ):
        self.channel_cnt = channel_cnt
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_cnt is not None:
            result['ChannelCnt'] = self.channel_cnt
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelCnt') is not None:
            self.channel_cnt = m.get('ChannelCnt')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class DescribeMeterRtcChannelCntDataResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DescribeMeterRtcChannelCntDataResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
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
                temp_model = DescribeMeterRtcChannelCntDataResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeMeterRtcChannelCntDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeMeterRtcChannelCntDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeMeterRtcChannelCntDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMeterRtcDurationRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        end_ts: int = None,
        interval: int = None,
        service_area: str = None,
        start_ts: int = None,
    ):
        self.app_id = app_id
        self.end_ts = end_ts
        self.interval = interval
        self.service_area = service_area
        self.start_ts = start_ts

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.end_ts is not None:
            result['EndTs'] = self.end_ts
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.service_area is not None:
            result['ServiceArea'] = self.service_area
        if self.start_ts is not None:
            result['StartTs'] = self.start_ts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndTs') is not None:
            self.end_ts = m.get('EndTs')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('ServiceArea') is not None:
            self.service_area = m.get('ServiceArea')
        if m.get('StartTs') is not None:
            self.start_ts = m.get('StartTs')
        return self


class DescribeMeterRtcDurationResponseBodyData(TeaModel):
    def __init__(
        self,
        audio_duration: int = None,
        content_duration: int = None,
        timestamp: int = None,
        total_duration: int = None,
        v_1080duration: int = None,
        v_480duration: int = None,
        v_720duration: int = None,
    ):
        self.audio_duration = audio_duration
        self.content_duration = content_duration
        self.timestamp = timestamp
        self.total_duration = total_duration
        self.v_1080duration = v_1080duration
        self.v_480duration = v_480duration
        self.v_720duration = v_720duration

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_duration is not None:
            result['AudioDuration'] = self.audio_duration
        if self.content_duration is not None:
            result['ContentDuration'] = self.content_duration
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.total_duration is not None:
            result['TotalDuration'] = self.total_duration
        if self.v_1080duration is not None:
            result['V1080Duration'] = self.v_1080duration
        if self.v_480duration is not None:
            result['V480Duration'] = self.v_480duration
        if self.v_720duration is not None:
            result['V720Duration'] = self.v_720duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioDuration') is not None:
            self.audio_duration = m.get('AudioDuration')
        if m.get('ContentDuration') is not None:
            self.content_duration = m.get('ContentDuration')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('TotalDuration') is not None:
            self.total_duration = m.get('TotalDuration')
        if m.get('V1080Duration') is not None:
            self.v_1080duration = m.get('V1080Duration')
        if m.get('V480Duration') is not None:
            self.v_480duration = m.get('V480Duration')
        if m.get('V720Duration') is not None:
            self.v_720duration = m.get('V720Duration')
        return self


class DescribeMeterRtcDurationResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DescribeMeterRtcDurationResponseBodyData] = None,
        ready_ts: int = None,
        request_id: str = None,
    ):
        self.data = data
        self.ready_ts = ready_ts
        # Id of the request
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
        if self.ready_ts is not None:
            result['ReadyTs'] = self.ready_ts
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeMeterRtcDurationResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ReadyTs') is not None:
            self.ready_ts = m.get('ReadyTs')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeMeterRtcDurationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeMeterRtcDurationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeMeterRtcDurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMeterRtcDurationByAppIdRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        end_ts: int = None,
        interval: int = None,
        service_area: str = None,
        start_ts: int = None,
    ):
        self.app_id = app_id
        self.end_ts = end_ts
        self.interval = interval
        self.service_area = service_area
        self.start_ts = start_ts

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.end_ts is not None:
            result['EndTs'] = self.end_ts
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.service_area is not None:
            result['ServiceArea'] = self.service_area
        if self.start_ts is not None:
            result['StartTs'] = self.start_ts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndTs') is not None:
            self.end_ts = m.get('EndTs')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('ServiceArea') is not None:
            self.service_area = m.get('ServiceArea')
        if m.get('StartTs') is not None:
            self.start_ts = m.get('StartTs')
        return self


class DescribeMeterRtcDurationByAppIdResponseBodyData(TeaModel):
    def __init__(
        self,
        audio_duration: int = None,
        content_duration: int = None,
        timestamp: int = None,
        total_duration: int = None,
        v_1080duration: int = None,
        v_360duration: int = None,
        v_720duration: int = None,
    ):
        self.audio_duration = audio_duration
        self.content_duration = content_duration
        self.timestamp = timestamp
        self.total_duration = total_duration
        self.v_1080duration = v_1080duration
        self.v_360duration = v_360duration
        self.v_720duration = v_720duration

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_duration is not None:
            result['AudioDuration'] = self.audio_duration
        if self.content_duration is not None:
            result['ContentDuration'] = self.content_duration
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.total_duration is not None:
            result['TotalDuration'] = self.total_duration
        if self.v_1080duration is not None:
            result['V1080Duration'] = self.v_1080duration
        if self.v_360duration is not None:
            result['V360Duration'] = self.v_360duration
        if self.v_720duration is not None:
            result['V720Duration'] = self.v_720duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioDuration') is not None:
            self.audio_duration = m.get('AudioDuration')
        if m.get('ContentDuration') is not None:
            self.content_duration = m.get('ContentDuration')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('TotalDuration') is not None:
            self.total_duration = m.get('TotalDuration')
        if m.get('V1080Duration') is not None:
            self.v_1080duration = m.get('V1080Duration')
        if m.get('V360Duration') is not None:
            self.v_360duration = m.get('V360Duration')
        if m.get('V720Duration') is not None:
            self.v_720duration = m.get('V720Duration')
        return self


class DescribeMeterRtcDurationByAppIdResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DescribeMeterRtcDurationByAppIdResponseBodyData] = None,
        ready_ts: int = None,
        request_id: str = None,
    ):
        self.data = data
        self.ready_ts = ready_ts
        # Id of the request
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
        if self.ready_ts is not None:
            result['ReadyTs'] = self.ready_ts
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeMeterRtcDurationByAppIdResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ReadyTs') is not None:
            self.ready_ts = m.get('ReadyTs')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeMeterRtcDurationByAppIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeMeterRtcDurationByAppIdResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeMeterRtcDurationByAppIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMeterRtcFlowUsageRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        end_ts: int = None,
        interval: int = None,
        service_area: str = None,
        start_ts: int = None,
    ):
        self.app_id = app_id
        self.end_ts = end_ts
        self.interval = interval
        self.service_area = service_area
        self.start_ts = start_ts

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.end_ts is not None:
            result['EndTs'] = self.end_ts
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.service_area is not None:
            result['ServiceArea'] = self.service_area
        if self.start_ts is not None:
            result['StartTs'] = self.start_ts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndTs') is not None:
            self.end_ts = m.get('EndTs')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('ServiceArea') is not None:
            self.service_area = m.get('ServiceArea')
        if m.get('StartTs') is not None:
            self.start_ts = m.get('StartTs')
        return self


class DescribeMeterRtcFlowUsageResponseBodyRtcFlowUsageVoList(TeaModel):
    def __init__(
        self,
        anchor_flow_value: float = None,
        audience_flow_value: float = None,
        flow_value: float = None,
        timestamp: int = None,
    ):
        self.anchor_flow_value = anchor_flow_value
        self.audience_flow_value = audience_flow_value
        self.flow_value = flow_value
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anchor_flow_value is not None:
            result['AnchorFlowValue'] = self.anchor_flow_value
        if self.audience_flow_value is not None:
            result['AudienceFlowValue'] = self.audience_flow_value
        if self.flow_value is not None:
            result['FlowValue'] = self.flow_value
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnchorFlowValue') is not None:
            self.anchor_flow_value = m.get('AnchorFlowValue')
        if m.get('AudienceFlowValue') is not None:
            self.audience_flow_value = m.get('AudienceFlowValue')
        if m.get('FlowValue') is not None:
            self.flow_value = m.get('FlowValue')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class DescribeMeterRtcFlowUsageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        rtc_flow_usage_vo_list: List[DescribeMeterRtcFlowUsageResponseBodyRtcFlowUsageVoList] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.rtc_flow_usage_vo_list = rtc_flow_usage_vo_list

    def validate(self):
        if self.rtc_flow_usage_vo_list:
            for k in self.rtc_flow_usage_vo_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RtcFlowUsageVoList'] = []
        if self.rtc_flow_usage_vo_list is not None:
            for k in self.rtc_flow_usage_vo_list:
                result['RtcFlowUsageVoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.rtc_flow_usage_vo_list = []
        if m.get('RtcFlowUsageVoList') is not None:
            for k in m.get('RtcFlowUsageVoList'):
                temp_model = DescribeMeterRtcFlowUsageResponseBodyRtcFlowUsageVoList()
                self.rtc_flow_usage_vo_list.append(temp_model.from_map(k))
        return self


class DescribeMeterRtcFlowUsageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeMeterRtcFlowUsageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeMeterRtcFlowUsageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMeterRtcPeakChannelCntDataRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        end_ts: int = None,
        interval: int = None,
        service_area: str = None,
        start_ts: int = None,
    ):
        self.app_id = app_id
        self.end_ts = end_ts
        self.interval = interval
        self.service_area = service_area
        self.start_ts = start_ts

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.end_ts is not None:
            result['EndTs'] = self.end_ts
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.service_area is not None:
            result['ServiceArea'] = self.service_area
        if self.start_ts is not None:
            result['StartTs'] = self.start_ts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndTs') is not None:
            self.end_ts = m.get('EndTs')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('ServiceArea') is not None:
            self.service_area = m.get('ServiceArea')
        if m.get('StartTs') is not None:
            self.start_ts = m.get('StartTs')
        return self


class DescribeMeterRtcPeakChannelCntDataResponseBodyData(TeaModel):
    def __init__(
        self,
        active_channel_peak: int = None,
        active_channel_peak_time: int = None,
        timestamp: int = None,
    ):
        self.active_channel_peak = active_channel_peak
        self.active_channel_peak_time = active_channel_peak_time
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_channel_peak is not None:
            result['ActiveChannelPeak'] = self.active_channel_peak
        if self.active_channel_peak_time is not None:
            result['ActiveChannelPeakTime'] = self.active_channel_peak_time
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveChannelPeak') is not None:
            self.active_channel_peak = m.get('ActiveChannelPeak')
        if m.get('ActiveChannelPeakTime') is not None:
            self.active_channel_peak_time = m.get('ActiveChannelPeakTime')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class DescribeMeterRtcPeakChannelCntDataResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DescribeMeterRtcPeakChannelCntDataResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
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
                temp_model = DescribeMeterRtcPeakChannelCntDataResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeMeterRtcPeakChannelCntDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeMeterRtcPeakChannelCntDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeMeterRtcPeakChannelCntDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMeterRtcPeakUserCntDataRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        end_ts: int = None,
        interval: int = None,
        service_area: str = None,
        start_ts: int = None,
    ):
        self.app_id = app_id
        self.end_ts = end_ts
        self.interval = interval
        self.service_area = service_area
        self.start_ts = start_ts

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.end_ts is not None:
            result['EndTs'] = self.end_ts
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.service_area is not None:
            result['ServiceArea'] = self.service_area
        if self.start_ts is not None:
            result['StartTs'] = self.start_ts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndTs') is not None:
            self.end_ts = m.get('EndTs')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('ServiceArea') is not None:
            self.service_area = m.get('ServiceArea')
        if m.get('StartTs') is not None:
            self.start_ts = m.get('StartTs')
        return self


class DescribeMeterRtcPeakUserCntDataResponseBodyData(TeaModel):
    def __init__(
        self,
        active_user_peak: int = None,
        active_user_peak_time: int = None,
        timestamp: int = None,
    ):
        self.active_user_peak = active_user_peak
        self.active_user_peak_time = active_user_peak_time
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_user_peak is not None:
            result['ActiveUserPeak'] = self.active_user_peak
        if self.active_user_peak_time is not None:
            result['ActiveUserPeakTime'] = self.active_user_peak_time
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveUserPeak') is not None:
            self.active_user_peak = m.get('ActiveUserPeak')
        if m.get('ActiveUserPeakTime') is not None:
            self.active_user_peak_time = m.get('ActiveUserPeakTime')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class DescribeMeterRtcPeakUserCntDataResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DescribeMeterRtcPeakUserCntDataResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
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
                temp_model = DescribeMeterRtcPeakUserCntDataResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeMeterRtcPeakUserCntDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeMeterRtcPeakUserCntDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeMeterRtcPeakUserCntDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMeterRtcRtBandWidthUsageRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        end_ts: int = None,
        interval: int = None,
        service_area: str = None,
        start_ts: int = None,
    ):
        self.app_id = app_id
        self.end_ts = end_ts
        self.interval = interval
        self.service_area = service_area
        self.start_ts = start_ts

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.end_ts is not None:
            result['EndTs'] = self.end_ts
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.service_area is not None:
            result['ServiceArea'] = self.service_area
        if self.start_ts is not None:
            result['StartTs'] = self.start_ts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndTs') is not None:
            self.end_ts = m.get('EndTs')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('ServiceArea') is not None:
            self.service_area = m.get('ServiceArea')
        if m.get('StartTs') is not None:
            self.start_ts = m.get('StartTs')
        return self


class DescribeMeterRtcRtBandWidthUsageResponseBodyData(TeaModel):
    def __init__(
        self,
        anchor_peak_rate: float = None,
        anchor_peak_ts: int = None,
        audience_peak_rate: float = None,
        audience_peak_ts: int = None,
        peak_rate: float = None,
        peak_ts: int = None,
        timestamp: int = None,
    ):
        self.anchor_peak_rate = anchor_peak_rate
        self.anchor_peak_ts = anchor_peak_ts
        self.audience_peak_rate = audience_peak_rate
        self.audience_peak_ts = audience_peak_ts
        self.peak_rate = peak_rate
        self.peak_ts = peak_ts
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anchor_peak_rate is not None:
            result['AnchorPeakRate'] = self.anchor_peak_rate
        if self.anchor_peak_ts is not None:
            result['AnchorPeakTs'] = self.anchor_peak_ts
        if self.audience_peak_rate is not None:
            result['AudiencePeakRate'] = self.audience_peak_rate
        if self.audience_peak_ts is not None:
            result['AudiencePeakTs'] = self.audience_peak_ts
        if self.peak_rate is not None:
            result['PeakRate'] = self.peak_rate
        if self.peak_ts is not None:
            result['PeakTs'] = self.peak_ts
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnchorPeakRate') is not None:
            self.anchor_peak_rate = m.get('AnchorPeakRate')
        if m.get('AnchorPeakTs') is not None:
            self.anchor_peak_ts = m.get('AnchorPeakTs')
        if m.get('AudiencePeakRate') is not None:
            self.audience_peak_rate = m.get('AudiencePeakRate')
        if m.get('AudiencePeakTs') is not None:
            self.audience_peak_ts = m.get('AudiencePeakTs')
        if m.get('PeakRate') is not None:
            self.peak_rate = m.get('PeakRate')
        if m.get('PeakTs') is not None:
            self.peak_ts = m.get('PeakTs')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class DescribeMeterRtcRtBandWidthUsageResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DescribeMeterRtcRtBandWidthUsageResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
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
                temp_model = DescribeMeterRtcRtBandWidthUsageResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeMeterRtcRtBandWidthUsageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeMeterRtcRtBandWidthUsageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeMeterRtcRtBandWidthUsageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMeterRtcRtFlowUsageRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        end_ts: int = None,
        interval: int = None,
        service_area: str = None,
        start_ts: int = None,
    ):
        self.app_id = app_id
        self.end_ts = end_ts
        self.interval = interval
        self.service_area = service_area
        self.start_ts = start_ts

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.end_ts is not None:
            result['EndTs'] = self.end_ts
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.service_area is not None:
            result['ServiceArea'] = self.service_area
        if self.start_ts is not None:
            result['StartTs'] = self.start_ts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndTs') is not None:
            self.end_ts = m.get('EndTs')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('ServiceArea') is not None:
            self.service_area = m.get('ServiceArea')
        if m.get('StartTs') is not None:
            self.start_ts = m.get('StartTs')
        return self


class DescribeMeterRtcRtFlowUsageResponseBodyData(TeaModel):
    def __init__(
        self,
        anchor_flow_value: float = None,
        audience_flow_value: float = None,
        flow_value: float = None,
        timestamp: int = None,
    ):
        self.anchor_flow_value = anchor_flow_value
        self.audience_flow_value = audience_flow_value
        self.flow_value = flow_value
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anchor_flow_value is not None:
            result['AnchorFlowValue'] = self.anchor_flow_value
        if self.audience_flow_value is not None:
            result['AudienceFlowValue'] = self.audience_flow_value
        if self.flow_value is not None:
            result['FlowValue'] = self.flow_value
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnchorFlowValue') is not None:
            self.anchor_flow_value = m.get('AnchorFlowValue')
        if m.get('AudienceFlowValue') is not None:
            self.audience_flow_value = m.get('AudienceFlowValue')
        if m.get('FlowValue') is not None:
            self.flow_value = m.get('FlowValue')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class DescribeMeterRtcRtFlowUsageResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DescribeMeterRtcRtFlowUsageResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
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
                temp_model = DescribeMeterRtcRtFlowUsageResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeMeterRtcRtFlowUsageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeMeterRtcRtFlowUsageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeMeterRtcRtFlowUsageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMeterRtcUserCntDataRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        end_ts: int = None,
        interval: int = None,
        service_area: str = None,
        start_ts: int = None,
    ):
        self.app_id = app_id
        self.end_ts = end_ts
        self.interval = interval
        self.service_area = service_area
        self.start_ts = start_ts

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.end_ts is not None:
            result['EndTs'] = self.end_ts
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.service_area is not None:
            result['ServiceArea'] = self.service_area
        if self.start_ts is not None:
            result['StartTs'] = self.start_ts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndTs') is not None:
            self.end_ts = m.get('EndTs')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('ServiceArea') is not None:
            self.service_area = m.get('ServiceArea')
        if m.get('StartTs') is not None:
            self.start_ts = m.get('StartTs')
        return self


class DescribeMeterRtcUserCntDataResponseBodyData(TeaModel):
    def __init__(
        self,
        active_user_cnt: int = None,
        timestamp: int = None,
    ):
        self.active_user_cnt = active_user_cnt
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_user_cnt is not None:
            result['ActiveUserCnt'] = self.active_user_cnt
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveUserCnt') is not None:
            self.active_user_cnt = m.get('ActiveUserCnt')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class DescribeMeterRtcUserCntDataResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DescribeMeterRtcUserCntDataResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
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
                temp_model = DescribeMeterRtcUserCntDataResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeMeterRtcUserCntDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeMeterRtcUserCntDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeMeterRtcUserCntDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


