# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class DescribeAppConfigRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class DescribeAppConfigResponseBodyThresholdConfig(TeaModel):
    def __init__(
        self,
        join_slow_time: int = None,
    ):
        self.join_slow_time = join_slow_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.join_slow_time is not None:
            result['JoinSlowTime'] = self.join_slow_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JoinSlowTime') is not None:
            self.join_slow_time = m.get('JoinSlowTime')
        return self


class DescribeAppConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        threshold_config: DescribeAppConfigResponseBodyThresholdConfig = None,
    ):
        self.request_id = request_id
        self.threshold_config = threshold_config

    def validate(self):
        if self.threshold_config:
            self.threshold_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.threshold_config is not None:
            result['ThresholdConfig'] = self.threshold_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ThresholdConfig') is not None:
            temp_model = DescribeAppConfigResponseBodyThresholdConfig()
            self.threshold_config = temp_model.from_map(m['ThresholdConfig'])
        return self


class DescribeAppConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAppConfigResponseBody = None,
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
            temp_model = DescribeAppConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCallRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        created_ts: int = None,
        destroyed_ts: int = None,
        ext_data_type: str = None,
        query_exp_info: bool = None,
    ):
        self.app_id = app_id
        self.channel_id = channel_id
        self.created_ts = created_ts
        self.destroyed_ts = destroyed_ts
        self.ext_data_type = ext_data_type
        self.query_exp_info = query_exp_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        if self.ext_data_type is not None:
            result['ExtDataType'] = self.ext_data_type
        if self.query_exp_info is not None:
            result['QueryExpInfo'] = self.query_exp_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        if m.get('ExtDataType') is not None:
            self.ext_data_type = m.get('ExtDataType')
        if m.get('QueryExpInfo') is not None:
            self.query_exp_info = m.get('QueryExpInfo')
        return self


class DescribeCallResponseBodyCallInfo(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        call_status: str = None,
        channel_id: str = None,
        created_ts: int = None,
        destroyed_ts: int = None,
        duration: int = None,
    ):
        # App ID。
        self.app_id = app_id
        self.call_status = call_status
        self.channel_id = channel_id
        self.created_ts = created_ts
        self.destroyed_ts = destroyed_ts
        self.duration = duration

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.call_status is not None:
            result['CallStatus'] = self.call_status
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        if self.duration is not None:
            result['Duration'] = self.duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CallStatus') is not None:
            self.call_status = m.get('CallStatus')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        return self


class DescribeCallResponseBodyUserDetailListDurMetricStatData(TeaModel):
    def __init__(
        self,
        pub_audio: int = None,
        pub_video_1080: int = None,
        pub_video_360: int = None,
        pub_video_720: int = None,
        pub_video_screen_share: int = None,
        sub_audio: int = None,
        sub_video_1080: int = None,
        sub_video_360: int = None,
        sub_video_720: int = None,
        sub_video_screen_share: int = None,
    ):
        self.pub_audio = pub_audio
        self.pub_video_1080 = pub_video_1080
        self.pub_video_360 = pub_video_360
        self.pub_video_720 = pub_video_720
        self.pub_video_screen_share = pub_video_screen_share
        self.sub_audio = sub_audio
        self.sub_video_1080 = sub_video_1080
        self.sub_video_360 = sub_video_360
        self.sub_video_720 = sub_video_720
        self.sub_video_screen_share = sub_video_screen_share

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pub_audio is not None:
            result['PubAudio'] = self.pub_audio
        if self.pub_video_1080 is not None:
            result['PubVideo1080'] = self.pub_video_1080
        if self.pub_video_360 is not None:
            result['PubVideo360'] = self.pub_video_360
        if self.pub_video_720 is not None:
            result['PubVideo720'] = self.pub_video_720
        if self.pub_video_screen_share is not None:
            result['PubVideoScreenShare'] = self.pub_video_screen_share
        if self.sub_audio is not None:
            result['SubAudio'] = self.sub_audio
        if self.sub_video_1080 is not None:
            result['SubVideo1080'] = self.sub_video_1080
        if self.sub_video_360 is not None:
            result['SubVideo360'] = self.sub_video_360
        if self.sub_video_720 is not None:
            result['SubVideo720'] = self.sub_video_720
        if self.sub_video_screen_share is not None:
            result['SubVideoScreenShare'] = self.sub_video_screen_share
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PubAudio') is not None:
            self.pub_audio = m.get('PubAudio')
        if m.get('PubVideo1080') is not None:
            self.pub_video_1080 = m.get('PubVideo1080')
        if m.get('PubVideo360') is not None:
            self.pub_video_360 = m.get('PubVideo360')
        if m.get('PubVideo720') is not None:
            self.pub_video_720 = m.get('PubVideo720')
        if m.get('PubVideoScreenShare') is not None:
            self.pub_video_screen_share = m.get('PubVideoScreenShare')
        if m.get('SubAudio') is not None:
            self.sub_audio = m.get('SubAudio')
        if m.get('SubVideo1080') is not None:
            self.sub_video_1080 = m.get('SubVideo1080')
        if m.get('SubVideo360') is not None:
            self.sub_video_360 = m.get('SubVideo360')
        if m.get('SubVideo720') is not None:
            self.sub_video_720 = m.get('SubVideo720')
        if m.get('SubVideoScreenShare') is not None:
            self.sub_video_screen_share = m.get('SubVideoScreenShare')
        return self


class DescribeCallResponseBodyUserDetailListOnlinePeriods(TeaModel):
    def __init__(
        self,
        join_ts: int = None,
        leave_ts: int = None,
    ):
        self.join_ts = join_ts
        self.leave_ts = leave_ts

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.join_ts is not None:
            result['JoinTs'] = self.join_ts
        if self.leave_ts is not None:
            result['LeaveTs'] = self.leave_ts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JoinTs') is not None:
            self.join_ts = m.get('JoinTs')
        if m.get('LeaveTs') is not None:
            self.leave_ts = m.get('LeaveTs')
        return self


class DescribeCallResponseBodyUserDetailList(TeaModel):
    def __init__(
        self,
        call_exp: str = None,
        created_ts: int = None,
        destroyed_ts: int = None,
        dur_metric_stat_data: DescribeCallResponseBodyUserDetailListDurMetricStatData = None,
        duration: int = None,
        location: str = None,
        network: str = None,
        network_list: List[str] = None,
        online_duration: int = None,
        online_periods: List[DescribeCallResponseBodyUserDetailListOnlinePeriods] = None,
        os: str = None,
        os_list: List[str] = None,
        roles: List[str] = None,
        sdk_version: str = None,
        sdk_version_list: List[str] = None,
        user_id: str = None,
        user_id_alias: str = None,
    ):
        self.call_exp = call_exp
        self.created_ts = created_ts
        self.destroyed_ts = destroyed_ts
        self.dur_metric_stat_data = dur_metric_stat_data
        self.duration = duration
        self.location = location
        self.network = network
        self.network_list = network_list
        self.online_duration = online_duration
        self.online_periods = online_periods
        self.os = os
        self.os_list = os_list
        self.roles = roles
        self.sdk_version = sdk_version
        self.sdk_version_list = sdk_version_list
        self.user_id = user_id
        self.user_id_alias = user_id_alias

    def validate(self):
        if self.dur_metric_stat_data:
            self.dur_metric_stat_data.validate()
        if self.online_periods:
            for k in self.online_periods:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_exp is not None:
            result['CallExp'] = self.call_exp
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        if self.dur_metric_stat_data is not None:
            result['DurMetricStatData'] = self.dur_metric_stat_data.to_map()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.location is not None:
            result['Location'] = self.location
        if self.network is not None:
            result['Network'] = self.network
        if self.network_list is not None:
            result['NetworkList'] = self.network_list
        if self.online_duration is not None:
            result['OnlineDuration'] = self.online_duration
        result['OnlinePeriods'] = []
        if self.online_periods is not None:
            for k in self.online_periods:
                result['OnlinePeriods'].append(k.to_map() if k else None)
        if self.os is not None:
            result['Os'] = self.os
        if self.os_list is not None:
            result['OsList'] = self.os_list
        if self.roles is not None:
            result['Roles'] = self.roles
        if self.sdk_version is not None:
            result['SdkVersion'] = self.sdk_version
        if self.sdk_version_list is not None:
            result['SdkVersionList'] = self.sdk_version_list
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_id_alias is not None:
            result['UserIdAlias'] = self.user_id_alias
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallExp') is not None:
            self.call_exp = m.get('CallExp')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        if m.get('DurMetricStatData') is not None:
            temp_model = DescribeCallResponseBodyUserDetailListDurMetricStatData()
            self.dur_metric_stat_data = temp_model.from_map(m['DurMetricStatData'])
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('NetworkList') is not None:
            self.network_list = m.get('NetworkList')
        if m.get('OnlineDuration') is not None:
            self.online_duration = m.get('OnlineDuration')
        self.online_periods = []
        if m.get('OnlinePeriods') is not None:
            for k in m.get('OnlinePeriods'):
                temp_model = DescribeCallResponseBodyUserDetailListOnlinePeriods()
                self.online_periods.append(temp_model.from_map(k))
        if m.get('Os') is not None:
            self.os = m.get('Os')
        if m.get('OsList') is not None:
            self.os_list = m.get('OsList')
        if m.get('Roles') is not None:
            self.roles = m.get('Roles')
        if m.get('SdkVersion') is not None:
            self.sdk_version = m.get('SdkVersion')
        if m.get('SdkVersionList') is not None:
            self.sdk_version_list = m.get('SdkVersionList')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserIdAlias') is not None:
            self.user_id_alias = m.get('UserIdAlias')
        return self


class DescribeCallResponseBody(TeaModel):
    def __init__(
        self,
        call_info: DescribeCallResponseBodyCallInfo = None,
        request_id: str = None,
        user_detail_list: List[DescribeCallResponseBodyUserDetailList] = None,
    ):
        self.call_info = call_info
        self.request_id = request_id
        self.user_detail_list = user_detail_list

    def validate(self):
        if self.call_info:
            self.call_info.validate()
        if self.user_detail_list:
            for k in self.user_detail_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_info is not None:
            result['CallInfo'] = self.call_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['UserDetailList'] = []
        if self.user_detail_list is not None:
            for k in self.user_detail_list:
                result['UserDetailList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallInfo') is not None:
            temp_model = DescribeCallResponseBodyCallInfo()
            self.call_info = temp_model.from_map(m['CallInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.user_detail_list = []
        if m.get('UserDetailList') is not None:
            for k in m.get('UserDetailList'):
                temp_model = DescribeCallResponseBodyUserDetailList()
                self.user_detail_list.append(temp_model.from_map(k))
        return self


class DescribeCallResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCallResponseBody = None,
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
            temp_model = DescribeCallResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCallInfoRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        created_ts: int = None,
        destroyed_ts: int = None,
    ):
        self.app_id = app_id
        self.channel_id = channel_id
        self.created_ts = created_ts
        self.destroyed_ts = destroyed_ts

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        return self


class DescribeCallInfoResponseBodyCallInfo(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        call_status: str = None,
        channel_id: str = None,
        created_ts: int = None,
        destroyed_ts: int = None,
        duration: int = None,
    ):
        self.app_id = app_id
        self.call_status = call_status
        self.channel_id = channel_id
        self.created_ts = created_ts
        self.destroyed_ts = destroyed_ts
        self.duration = duration

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.call_status is not None:
            result['CallStatus'] = self.call_status
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        if self.duration is not None:
            result['Duration'] = self.duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CallStatus') is not None:
            self.call_status = m.get('CallStatus')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        return self


class DescribeCallInfoResponseBody(TeaModel):
    def __init__(
        self,
        call_info: DescribeCallInfoResponseBodyCallInfo = None,
        request_id: str = None,
    ):
        self.call_info = call_info
        self.request_id = request_id

    def validate(self):
        if self.call_info:
            self.call_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_info is not None:
            result['CallInfo'] = self.call_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallInfo') is not None:
            temp_model = DescribeCallInfoResponseBodyCallInfo()
            self.call_info = temp_model.from_map(m['CallInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCallInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCallInfoResponseBody = None,
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
            temp_model = DescribeCallInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCallListRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        call_status: str = None,
        channel_id: str = None,
        end_ts: int = None,
        order_by: str = None,
        page_no: int = None,
        page_size: int = None,
        query_mode: str = None,
        start_ts: int = None,
        user_id: str = None,
    ):
        self.app_id = app_id
        self.call_status = call_status
        self.channel_id = channel_id
        self.end_ts = end_ts
        self.order_by = order_by
        self.page_no = page_no
        self.page_size = page_size
        self.query_mode = query_mode
        self.start_ts = start_ts
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.call_status is not None:
            result['CallStatus'] = self.call_status
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.end_ts is not None:
            result['EndTs'] = self.end_ts
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_mode is not None:
            result['QueryMode'] = self.query_mode
        if self.start_ts is not None:
            result['StartTs'] = self.start_ts
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CallStatus') is not None:
            self.call_status = m.get('CallStatus')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('EndTs') is not None:
            self.end_ts = m.get('EndTs')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryMode') is not None:
            self.query_mode = m.get('QueryMode')
        if m.get('StartTs') is not None:
            self.start_ts = m.get('StartTs')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeCallListResponseBodyCallList(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        bad_exp_user_cnt: int = None,
        call_status: str = None,
        channel_id: str = None,
        created_ts: int = None,
        destroyed_ts: int = None,
        duration: int = None,
        user_cnt: int = None,
    ):
        # App ID。
        self.app_id = app_id
        self.bad_exp_user_cnt = bad_exp_user_cnt
        self.call_status = call_status
        self.channel_id = channel_id
        self.created_ts = created_ts
        self.destroyed_ts = destroyed_ts
        self.duration = duration
        self.user_cnt = user_cnt

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.bad_exp_user_cnt is not None:
            result['BadExpUserCnt'] = self.bad_exp_user_cnt
        if self.call_status is not None:
            result['CallStatus'] = self.call_status
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.user_cnt is not None:
            result['UserCnt'] = self.user_cnt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('BadExpUserCnt') is not None:
            self.bad_exp_user_cnt = m.get('BadExpUserCnt')
        if m.get('CallStatus') is not None:
            self.call_status = m.get('CallStatus')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('UserCnt') is not None:
            self.user_cnt = m.get('UserCnt')
        return self


class DescribeCallListResponseBody(TeaModel):
    def __init__(
        self,
        call_list: List[DescribeCallListResponseBodyCallList] = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total_cnt: int = None,
    ):
        self.call_list = call_list
        self.page_no = page_no
        self.page_size = page_size
        self.request_id = request_id
        self.total_cnt = total_cnt

    def validate(self):
        if self.call_list:
            for k in self.call_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CallList'] = []
        if self.call_list is not None:
            for k in self.call_list:
                result['CallList'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_cnt is not None:
            result['TotalCnt'] = self.total_cnt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.call_list = []
        if m.get('CallList') is not None:
            for k in m.get('CallList'):
                temp_model = DescribeCallListResponseBodyCallList()
                self.call_list.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCnt') is not None:
            self.total_cnt = m.get('TotalCnt')
        return self


class DescribeCallListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCallListResponseBody = None,
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
            temp_model = DescribeCallListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCallUserExpRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        created_ts: int = None,
        destroyed_ts: int = None,
    ):
        self.app_id = app_id
        self.channel_id = channel_id
        self.created_ts = created_ts
        self.destroyed_ts = destroyed_ts

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        return self


class DescribeCallUserExpResponseBodyExpInfoList(TeaModel):
    def __init__(
        self,
        call_exp: str = None,
        user_id: str = None,
    ):
        self.call_exp = call_exp
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_exp is not None:
            result['CallExp'] = self.call_exp
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallExp') is not None:
            self.call_exp = m.get('CallExp')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeCallUserExpResponseBody(TeaModel):
    def __init__(
        self,
        exp_info_list: List[DescribeCallUserExpResponseBodyExpInfoList] = None,
        request_id: str = None,
    ):
        self.exp_info_list = exp_info_list
        self.request_id = request_id

    def validate(self):
        if self.exp_info_list:
            for k in self.exp_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ExpInfoList'] = []
        if self.exp_info_list is not None:
            for k in self.exp_info_list:
                result['ExpInfoList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.exp_info_list = []
        if m.get('ExpInfoList') is not None:
            for k in m.get('ExpInfoList'):
                temp_model = DescribeCallUserExpResponseBodyExpInfoList()
                self.exp_info_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCallUserExpResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCallUserExpResponseBody = None,
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
            temp_model = DescribeCallUserExpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCallUserListRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        created_ts: int = None,
        destroyed_ts: int = None,
        ext_data_type: str = None,
        page_no: int = None,
        page_size: int = None,
        query_exp_info: bool = None,
        role_type: str = None,
        user_id: str = None,
    ):
        self.app_id = app_id
        self.channel_id = channel_id
        self.created_ts = created_ts
        self.destroyed_ts = destroyed_ts
        self.ext_data_type = ext_data_type
        self.page_no = page_no
        self.page_size = page_size
        self.query_exp_info = query_exp_info
        self.role_type = role_type
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        if self.ext_data_type is not None:
            result['ExtDataType'] = self.ext_data_type
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_exp_info is not None:
            result['QueryExpInfo'] = self.query_exp_info
        if self.role_type is not None:
            result['RoleType'] = self.role_type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        if m.get('ExtDataType') is not None:
            self.ext_data_type = m.get('ExtDataType')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryExpInfo') is not None:
            self.query_exp_info = m.get('QueryExpInfo')
        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeCallUserListResponseBodyUserDetailListDurMetricStatData(TeaModel):
    def __init__(
        self,
        pub_audio: int = None,
        pub_video_360: int = None,
        pub_video_720: int = None,
        pub_video_screen_share: int = None,
        sub_audio: int = None,
        sub_video_1080: int = None,
        sub_video_360: int = None,
        sub_video_720: int = None,
        sub_video_screen_share: int = None,
    ):
        self.pub_audio = pub_audio
        self.pub_video_360 = pub_video_360
        self.pub_video_720 = pub_video_720
        self.pub_video_screen_share = pub_video_screen_share
        self.sub_audio = sub_audio
        self.sub_video_1080 = sub_video_1080
        self.sub_video_360 = sub_video_360
        self.sub_video_720 = sub_video_720
        self.sub_video_screen_share = sub_video_screen_share

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pub_audio is not None:
            result['PubAudio'] = self.pub_audio
        if self.pub_video_360 is not None:
            result['PubVideo360'] = self.pub_video_360
        if self.pub_video_720 is not None:
            result['PubVideo720'] = self.pub_video_720
        if self.pub_video_screen_share is not None:
            result['PubVideoScreenShare'] = self.pub_video_screen_share
        if self.sub_audio is not None:
            result['SubAudio'] = self.sub_audio
        if self.sub_video_1080 is not None:
            result['SubVideo1080'] = self.sub_video_1080
        if self.sub_video_360 is not None:
            result['SubVideo360'] = self.sub_video_360
        if self.sub_video_720 is not None:
            result['SubVideo720'] = self.sub_video_720
        if self.sub_video_screen_share is not None:
            result['SubVideoScreenShare'] = self.sub_video_screen_share
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PubAudio') is not None:
            self.pub_audio = m.get('PubAudio')
        if m.get('PubVideo360') is not None:
            self.pub_video_360 = m.get('PubVideo360')
        if m.get('PubVideo720') is not None:
            self.pub_video_720 = m.get('PubVideo720')
        if m.get('PubVideoScreenShare') is not None:
            self.pub_video_screen_share = m.get('PubVideoScreenShare')
        if m.get('SubAudio') is not None:
            self.sub_audio = m.get('SubAudio')
        if m.get('SubVideo1080') is not None:
            self.sub_video_1080 = m.get('SubVideo1080')
        if m.get('SubVideo360') is not None:
            self.sub_video_360 = m.get('SubVideo360')
        if m.get('SubVideo720') is not None:
            self.sub_video_720 = m.get('SubVideo720')
        if m.get('SubVideoScreenShare') is not None:
            self.sub_video_screen_share = m.get('SubVideoScreenShare')
        return self


class DescribeCallUserListResponseBodyUserDetailListOnlinePeriods(TeaModel):
    def __init__(
        self,
        join_ts: int = None,
        leave_ts: int = None,
    ):
        self.join_ts = join_ts
        self.leave_ts = leave_ts

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.join_ts is not None:
            result['JoinTs'] = self.join_ts
        if self.leave_ts is not None:
            result['LeaveTs'] = self.leave_ts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JoinTs') is not None:
            self.join_ts = m.get('JoinTs')
        if m.get('LeaveTs') is not None:
            self.leave_ts = m.get('LeaveTs')
        return self


class DescribeCallUserListResponseBodyUserDetailList(TeaModel):
    def __init__(
        self,
        call_exp: str = None,
        created_ts: int = None,
        destroyed_ts: int = None,
        dur_metric_stat_data: DescribeCallUserListResponseBodyUserDetailListDurMetricStatData = None,
        duration: int = None,
        location: str = None,
        location_cn: str = None,
        location_en: str = None,
        network: str = None,
        network_list: List[str] = None,
        online_duration: int = None,
        online_periods: List[DescribeCallUserListResponseBodyUserDetailListOnlinePeriods] = None,
        os: str = None,
        os_list: List[str] = None,
        roles: List[str] = None,
        sdk_version: str = None,
        sdk_version_list: List[str] = None,
        user_id: str = None,
        user_id_alias: str = None,
    ):
        self.call_exp = call_exp
        self.created_ts = created_ts
        self.destroyed_ts = destroyed_ts
        self.dur_metric_stat_data = dur_metric_stat_data
        self.duration = duration
        self.location = location
        self.location_cn = location_cn
        self.location_en = location_en
        self.network = network
        self.network_list = network_list
        self.online_duration = online_duration
        self.online_periods = online_periods
        self.os = os
        self.os_list = os_list
        self.roles = roles
        self.sdk_version = sdk_version
        self.sdk_version_list = sdk_version_list
        self.user_id = user_id
        self.user_id_alias = user_id_alias

    def validate(self):
        if self.dur_metric_stat_data:
            self.dur_metric_stat_data.validate()
        if self.online_periods:
            for k in self.online_periods:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_exp is not None:
            result['CallExp'] = self.call_exp
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        if self.dur_metric_stat_data is not None:
            result['DurMetricStatData'] = self.dur_metric_stat_data.to_map()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.location is not None:
            result['Location'] = self.location
        if self.location_cn is not None:
            result['LocationCn'] = self.location_cn
        if self.location_en is not None:
            result['LocationEn'] = self.location_en
        if self.network is not None:
            result['Network'] = self.network
        if self.network_list is not None:
            result['NetworkList'] = self.network_list
        if self.online_duration is not None:
            result['OnlineDuration'] = self.online_duration
        result['OnlinePeriods'] = []
        if self.online_periods is not None:
            for k in self.online_periods:
                result['OnlinePeriods'].append(k.to_map() if k else None)
        if self.os is not None:
            result['Os'] = self.os
        if self.os_list is not None:
            result['OsList'] = self.os_list
        if self.roles is not None:
            result['Roles'] = self.roles
        if self.sdk_version is not None:
            result['SdkVersion'] = self.sdk_version
        if self.sdk_version_list is not None:
            result['SdkVersionList'] = self.sdk_version_list
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_id_alias is not None:
            result['UserIdAlias'] = self.user_id_alias
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallExp') is not None:
            self.call_exp = m.get('CallExp')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        if m.get('DurMetricStatData') is not None:
            temp_model = DescribeCallUserListResponseBodyUserDetailListDurMetricStatData()
            self.dur_metric_stat_data = temp_model.from_map(m['DurMetricStatData'])
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('LocationCn') is not None:
            self.location_cn = m.get('LocationCn')
        if m.get('LocationEn') is not None:
            self.location_en = m.get('LocationEn')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('NetworkList') is not None:
            self.network_list = m.get('NetworkList')
        if m.get('OnlineDuration') is not None:
            self.online_duration = m.get('OnlineDuration')
        self.online_periods = []
        if m.get('OnlinePeriods') is not None:
            for k in m.get('OnlinePeriods'):
                temp_model = DescribeCallUserListResponseBodyUserDetailListOnlinePeriods()
                self.online_periods.append(temp_model.from_map(k))
        if m.get('Os') is not None:
            self.os = m.get('Os')
        if m.get('OsList') is not None:
            self.os_list = m.get('OsList')
        if m.get('Roles') is not None:
            self.roles = m.get('Roles')
        if m.get('SdkVersion') is not None:
            self.sdk_version = m.get('SdkVersion')
        if m.get('SdkVersionList') is not None:
            self.sdk_version_list = m.get('SdkVersionList')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserIdAlias') is not None:
            self.user_id_alias = m.get('UserIdAlias')
        return self


class DescribeCallUserListResponseBody(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total_cnt: int = None,
        user_detail_list: List[DescribeCallUserListResponseBodyUserDetailList] = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.request_id = request_id
        self.total_cnt = total_cnt
        self.user_detail_list = user_detail_list

    def validate(self):
        if self.user_detail_list:
            for k in self.user_detail_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_cnt is not None:
            result['TotalCnt'] = self.total_cnt
        result['UserDetailList'] = []
        if self.user_detail_list is not None:
            for k in self.user_detail_list:
                result['UserDetailList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCnt') is not None:
            self.total_cnt = m.get('TotalCnt')
        self.user_detail_list = []
        if m.get('UserDetailList') is not None:
            for k in m.get('UserDetailList'):
                temp_model = DescribeCallUserListResponseBodyUserDetailList()
                self.user_detail_list.append(temp_model.from_map(k))
        return self


class DescribeCallUserListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCallUserListResponseBody = None,
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
            temp_model = DescribeCallUserListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeChannelAreaDistributionStatDataRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        created_ts: int = None,
        destroyed_ts: int = None,
        parent_area: str = None,
    ):
        self.app_id = app_id
        self.channel_id = channel_id
        self.created_ts = created_ts
        self.destroyed_ts = destroyed_ts
        self.parent_area = parent_area

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        if self.parent_area is not None:
            result['ParentArea'] = self.parent_area
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        if m.get('ParentArea') is not None:
            self.parent_area = m.get('ParentArea')
        return self


class DescribeChannelAreaDistributionStatDataResponseBodyAreaStatList(TeaModel):
    def __init__(
        self,
        area_name: str = None,
        call_user_count: int = None,
        high_quality_transmission_rate: str = None,
        pub_user_count: int = None,
        sub_user_count: int = None,
    ):
        self.area_name = area_name
        self.call_user_count = call_user_count
        self.high_quality_transmission_rate = high_quality_transmission_rate
        self.pub_user_count = pub_user_count
        self.sub_user_count = sub_user_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area_name is not None:
            result['AreaName'] = self.area_name
        if self.call_user_count is not None:
            result['CallUserCount'] = self.call_user_count
        if self.high_quality_transmission_rate is not None:
            result['HighQualityTransmissionRate'] = self.high_quality_transmission_rate
        if self.pub_user_count is not None:
            result['PubUserCount'] = self.pub_user_count
        if self.sub_user_count is not None:
            result['SubUserCount'] = self.sub_user_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AreaName') is not None:
            self.area_name = m.get('AreaName')
        if m.get('CallUserCount') is not None:
            self.call_user_count = m.get('CallUserCount')
        if m.get('HighQualityTransmissionRate') is not None:
            self.high_quality_transmission_rate = m.get('HighQualityTransmissionRate')
        if m.get('PubUserCount') is not None:
            self.pub_user_count = m.get('PubUserCount')
        if m.get('SubUserCount') is not None:
            self.sub_user_count = m.get('SubUserCount')
        return self


class DescribeChannelAreaDistributionStatDataResponseBody(TeaModel):
    def __init__(
        self,
        area_stat_list: List[DescribeChannelAreaDistributionStatDataResponseBodyAreaStatList] = None,
        request_id: str = None,
    ):
        self.area_stat_list = area_stat_list
        self.request_id = request_id

    def validate(self):
        if self.area_stat_list:
            for k in self.area_stat_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AreaStatList'] = []
        if self.area_stat_list is not None:
            for k in self.area_stat_list:
                result['AreaStatList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.area_stat_list = []
        if m.get('AreaStatList') is not None:
            for k in m.get('AreaStatList'):
                temp_model = DescribeChannelAreaDistributionStatDataResponseBodyAreaStatList()
                self.area_stat_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeChannelAreaDistributionStatDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeChannelAreaDistributionStatDataResponseBody = None,
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
            temp_model = DescribeChannelAreaDistributionStatDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeChannelDistributionStatDataRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        created_ts: int = None,
        destroyed_ts: int = None,
        stat_dim: str = None,
    ):
        self.app_id = app_id
        self.channel_id = channel_id
        self.created_ts = created_ts
        self.destroyed_ts = destroyed_ts
        self.stat_dim = stat_dim

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        if self.stat_dim is not None:
            result['StatDim'] = self.stat_dim
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        if m.get('StatDim') is not None:
            self.stat_dim = m.get('StatDim')
        return self


class DescribeChannelDistributionStatDataResponseBodyStatList(TeaModel):
    def __init__(
        self,
        call_user_count: int = None,
        call_user_ratio: str = None,
        name: str = None,
    ):
        self.call_user_count = call_user_count
        self.call_user_ratio = call_user_ratio
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_user_count is not None:
            result['CallUserCount'] = self.call_user_count
        if self.call_user_ratio is not None:
            result['CallUserRatio'] = self.call_user_ratio
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallUserCount') is not None:
            self.call_user_count = m.get('CallUserCount')
        if m.get('CallUserRatio') is not None:
            self.call_user_ratio = m.get('CallUserRatio')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeChannelDistributionStatDataResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        stat_list: List[DescribeChannelDistributionStatDataResponseBodyStatList] = None,
    ):
        self.request_id = request_id
        self.stat_list = stat_list

    def validate(self):
        if self.stat_list:
            for k in self.stat_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['StatList'] = []
        if self.stat_list is not None:
            for k in self.stat_list:
                result['StatList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.stat_list = []
        if m.get('StatList') is not None:
            for k in m.get('StatList'):
                temp_model = DescribeChannelDistributionStatDataResponseBodyStatList()
                self.stat_list.append(temp_model.from_map(k))
        return self


class DescribeChannelDistributionStatDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeChannelDistributionStatDataResponseBody = None,
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
            temp_model = DescribeChannelDistributionStatDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeChannelJoinInfoRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        created_ts: int = None,
        destroyed_ts: int = None,
    ):
        self.app_id = app_id
        self.channel_id = channel_id
        self.created_ts = created_ts
        self.destroyed_ts = destroyed_ts

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        return self


class DescribeChannelJoinInfoResponseBody(TeaModel):
    def __init__(
        self,
        join_fast_success_rate: str = None,
        join_slow_threshold: int = None,
        request_id: str = None,
    ):
        self.join_fast_success_rate = join_fast_success_rate
        self.join_slow_threshold = join_slow_threshold
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.join_fast_success_rate is not None:
            result['JoinFastSuccessRate'] = self.join_fast_success_rate
        if self.join_slow_threshold is not None:
            result['JoinSlowThreshold'] = self.join_slow_threshold
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JoinFastSuccessRate') is not None:
            self.join_fast_success_rate = m.get('JoinFastSuccessRate')
        if m.get('JoinSlowThreshold') is not None:
            self.join_slow_threshold = m.get('JoinSlowThreshold')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeChannelJoinInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeChannelJoinInfoResponseBody = None,
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
            temp_model = DescribeChannelJoinInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeChannelOverallDataRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        created_ts: int = None,
        destroyed_ts: int = None,
    ):
        self.app_id = app_id
        self.channel_id = channel_id
        self.created_ts = created_ts
        self.destroyed_ts = destroyed_ts

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        return self


class DescribeChannelOverallDataResponseBodyCallInfo(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        call_status: str = None,
        channel_id: str = None,
        created_ts: int = None,
        destroyed_ts: int = None,
        duration: int = None,
    ):
        self.app_id = app_id
        self.call_status = call_status
        self.channel_id = channel_id
        self.created_ts = created_ts
        self.destroyed_ts = destroyed_ts
        self.duration = duration

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.call_status is not None:
            result['CallStatus'] = self.call_status
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        if self.duration is not None:
            result['Duration'] = self.duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CallStatus') is not None:
            self.call_status = m.get('CallStatus')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        return self


class DescribeChannelOverallDataResponseBodyMetricDatasNodes(TeaModel):
    def __init__(
        self,
        ext: Dict[str, Any] = None,
        x: str = None,
        y: str = None,
    ):
        self.ext = ext
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class DescribeChannelOverallDataResponseBodyMetricDatas(TeaModel):
    def __init__(
        self,
        nodes: List[DescribeChannelOverallDataResponseBodyMetricDatasNodes] = None,
        type: str = None,
    ):
        self.nodes = nodes
        self.type = type

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = DescribeChannelOverallDataResponseBodyMetricDatasNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeChannelOverallDataResponseBodyOverallData(TeaModel):
    def __init__(
        self,
        conn_avg_time: float = None,
        five_sec_join_rate: float = None,
        total_audio_stuck_rate: float = None,
        total_video_stuck_rate: float = None,
        total_video_vague_rate: float = None,
    ):
        self.conn_avg_time = conn_avg_time
        self.five_sec_join_rate = five_sec_join_rate
        self.total_audio_stuck_rate = total_audio_stuck_rate
        self.total_video_stuck_rate = total_video_stuck_rate
        self.total_video_vague_rate = total_video_vague_rate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conn_avg_time is not None:
            result['ConnAvgTime'] = self.conn_avg_time
        if self.five_sec_join_rate is not None:
            result['FiveSecJoinRate'] = self.five_sec_join_rate
        if self.total_audio_stuck_rate is not None:
            result['TotalAudioStuckRate'] = self.total_audio_stuck_rate
        if self.total_video_stuck_rate is not None:
            result['TotalVideoStuckRate'] = self.total_video_stuck_rate
        if self.total_video_vague_rate is not None:
            result['TotalVideoVagueRate'] = self.total_video_vague_rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnAvgTime') is not None:
            self.conn_avg_time = m.get('ConnAvgTime')
        if m.get('FiveSecJoinRate') is not None:
            self.five_sec_join_rate = m.get('FiveSecJoinRate')
        if m.get('TotalAudioStuckRate') is not None:
            self.total_audio_stuck_rate = m.get('TotalAudioStuckRate')
        if m.get('TotalVideoStuckRate') is not None:
            self.total_video_stuck_rate = m.get('TotalVideoStuckRate')
        if m.get('TotalVideoVagueRate') is not None:
            self.total_video_vague_rate = m.get('TotalVideoVagueRate')
        return self


class DescribeChannelOverallDataResponseBody(TeaModel):
    def __init__(
        self,
        call_info: DescribeChannelOverallDataResponseBodyCallInfo = None,
        metric_datas: List[DescribeChannelOverallDataResponseBodyMetricDatas] = None,
        overall_data: DescribeChannelOverallDataResponseBodyOverallData = None,
        request_id: str = None,
    ):
        self.call_info = call_info
        self.metric_datas = metric_datas
        self.overall_data = overall_data
        self.request_id = request_id

    def validate(self):
        if self.call_info:
            self.call_info.validate()
        if self.metric_datas:
            for k in self.metric_datas:
                if k:
                    k.validate()
        if self.overall_data:
            self.overall_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_info is not None:
            result['CallInfo'] = self.call_info.to_map()
        result['MetricDatas'] = []
        if self.metric_datas is not None:
            for k in self.metric_datas:
                result['MetricDatas'].append(k.to_map() if k else None)
        if self.overall_data is not None:
            result['OverallData'] = self.overall_data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallInfo') is not None:
            temp_model = DescribeChannelOverallDataResponseBodyCallInfo()
            self.call_info = temp_model.from_map(m['CallInfo'])
        self.metric_datas = []
        if m.get('MetricDatas') is not None:
            for k in m.get('MetricDatas'):
                temp_model = DescribeChannelOverallDataResponseBodyMetricDatas()
                self.metric_datas.append(temp_model.from_map(k))
        if m.get('OverallData') is not None:
            temp_model = DescribeChannelOverallDataResponseBodyOverallData()
            self.overall_data = temp_model.from_map(m['OverallData'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeChannelOverallDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeChannelOverallDataResponseBody = None,
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
            temp_model = DescribeChannelOverallDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeChannelTopPubUserListRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        created_ts: int = None,
        destroyed_ts: int = None,
    ):
        self.app_id = app_id
        self.channel_id = channel_id
        self.created_ts = created_ts
        self.destroyed_ts = destroyed_ts

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        return self


class DescribeChannelTopPubUserListResponseBodyTopPubUserDetailListOnlinePeriods(TeaModel):
    def __init__(
        self,
        join_ts: int = None,
        leave_ts: int = None,
    ):
        self.join_ts = join_ts
        self.leave_ts = leave_ts

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.join_ts is not None:
            result['JoinTs'] = self.join_ts
        if self.leave_ts is not None:
            result['LeaveTs'] = self.leave_ts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JoinTs') is not None:
            self.join_ts = m.get('JoinTs')
        if m.get('LeaveTs') is not None:
            self.leave_ts = m.get('LeaveTs')
        return self


class DescribeChannelTopPubUserListResponseBodyTopPubUserDetailList(TeaModel):
    def __init__(
        self,
        created_ts: int = None,
        destroyed_ts: int = None,
        duration: int = None,
        location: str = None,
        online_duration: int = None,
        online_periods: List[DescribeChannelTopPubUserListResponseBodyTopPubUserDetailListOnlinePeriods] = None,
        user_id: str = None,
    ):
        self.created_ts = created_ts
        self.destroyed_ts = destroyed_ts
        self.duration = duration
        self.location = location
        self.online_duration = online_duration
        self.online_periods = online_periods
        self.user_id = user_id

    def validate(self):
        if self.online_periods:
            for k in self.online_periods:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.location is not None:
            result['Location'] = self.location
        if self.online_duration is not None:
            result['OnlineDuration'] = self.online_duration
        result['OnlinePeriods'] = []
        if self.online_periods is not None:
            for k in self.online_periods:
                result['OnlinePeriods'].append(k.to_map() if k else None)
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('OnlineDuration') is not None:
            self.online_duration = m.get('OnlineDuration')
        self.online_periods = []
        if m.get('OnlinePeriods') is not None:
            for k in m.get('OnlinePeriods'):
                temp_model = DescribeChannelTopPubUserListResponseBodyTopPubUserDetailListOnlinePeriods()
                self.online_periods.append(temp_model.from_map(k))
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeChannelTopPubUserListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        top_pub_user_detail_list: List[DescribeChannelTopPubUserListResponseBodyTopPubUserDetailList] = None,
    ):
        self.request_id = request_id
        self.top_pub_user_detail_list = top_pub_user_detail_list

    def validate(self):
        if self.top_pub_user_detail_list:
            for k in self.top_pub_user_detail_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TopPubUserDetailList'] = []
        if self.top_pub_user_detail_list is not None:
            for k in self.top_pub_user_detail_list:
                result['TopPubUserDetailList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.top_pub_user_detail_list = []
        if m.get('TopPubUserDetailList') is not None:
            for k in m.get('TopPubUserDetailList'):
                temp_model = DescribeChannelTopPubUserListResponseBodyTopPubUserDetailList()
                self.top_pub_user_detail_list.append(temp_model.from_map(k))
        return self


class DescribeChannelTopPubUserListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeChannelTopPubUserListResponseBody = None,
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
            temp_model = DescribeChannelTopPubUserListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeChannelUserMetricsRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        created_ts: int = None,
        destroyed_ts: int = None,
    ):
        self.app_id = app_id
        self.channel_id = channel_id
        self.created_ts = created_ts
        self.destroyed_ts = destroyed_ts

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        return self


class DescribeChannelUserMetricsResponseBodyMetricDatasNodes(TeaModel):
    def __init__(
        self,
        ext: Dict[str, Any] = None,
        x: str = None,
        y: str = None,
    ):
        self.ext = ext
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class DescribeChannelUserMetricsResponseBodyMetricDatas(TeaModel):
    def __init__(
        self,
        nodes: List[DescribeChannelUserMetricsResponseBodyMetricDatasNodes] = None,
        type: str = None,
    ):
        self.nodes = nodes
        self.type = type

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = DescribeChannelUserMetricsResponseBodyMetricDatasNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeChannelUserMetricsResponseBodyOverallData(TeaModel):
    def __init__(
        self,
        total_bad_exp_num: int = None,
        total_join_fail_num: int = None,
        total_pub_user_num: int = None,
        total_sub_user_num: int = None,
        total_user_num: int = None,
    ):
        self.total_bad_exp_num = total_bad_exp_num
        self.total_join_fail_num = total_join_fail_num
        self.total_pub_user_num = total_pub_user_num
        self.total_sub_user_num = total_sub_user_num
        self.total_user_num = total_user_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_bad_exp_num is not None:
            result['TotalBadExpNum'] = self.total_bad_exp_num
        if self.total_join_fail_num is not None:
            result['TotalJoinFailNum'] = self.total_join_fail_num
        if self.total_pub_user_num is not None:
            result['TotalPubUserNum'] = self.total_pub_user_num
        if self.total_sub_user_num is not None:
            result['TotalSubUserNum'] = self.total_sub_user_num
        if self.total_user_num is not None:
            result['TotalUserNum'] = self.total_user_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalBadExpNum') is not None:
            self.total_bad_exp_num = m.get('TotalBadExpNum')
        if m.get('TotalJoinFailNum') is not None:
            self.total_join_fail_num = m.get('TotalJoinFailNum')
        if m.get('TotalPubUserNum') is not None:
            self.total_pub_user_num = m.get('TotalPubUserNum')
        if m.get('TotalSubUserNum') is not None:
            self.total_sub_user_num = m.get('TotalSubUserNum')
        if m.get('TotalUserNum') is not None:
            self.total_user_num = m.get('TotalUserNum')
        return self


class DescribeChannelUserMetricsResponseBody(TeaModel):
    def __init__(
        self,
        metric_datas: List[DescribeChannelUserMetricsResponseBodyMetricDatas] = None,
        overall_data: DescribeChannelUserMetricsResponseBodyOverallData = None,
        request_id: str = None,
    ):
        self.metric_datas = metric_datas
        self.overall_data = overall_data
        self.request_id = request_id

    def validate(self):
        if self.metric_datas:
            for k in self.metric_datas:
                if k:
                    k.validate()
        if self.overall_data:
            self.overall_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MetricDatas'] = []
        if self.metric_datas is not None:
            for k in self.metric_datas:
                result['MetricDatas'].append(k.to_map() if k else None)
        if self.overall_data is not None:
            result['OverallData'] = self.overall_data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.metric_datas = []
        if m.get('MetricDatas') is not None:
            for k in m.get('MetricDatas'):
                temp_model = DescribeChannelUserMetricsResponseBodyMetricDatas()
                self.metric_datas.append(temp_model.from_map(k))
        if m.get('OverallData') is not None:
            temp_model = DescribeChannelUserMetricsResponseBodyOverallData()
            self.overall_data = temp_model.from_map(m['OverallData'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeChannelUserMetricsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeChannelUserMetricsResponseBody = None,
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
            temp_model = DescribeChannelUserMetricsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEndPointEventListRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        created_ts: int = None,
        destroyed_ts: int = None,
        user_id_list: str = None,
    ):
        self.app_id = app_id
        self.channel_id = channel_id
        self.created_ts = created_ts
        self.destroyed_ts = destroyed_ts
        self.user_id_list = user_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        if self.user_id_list is not None:
            result['UserIdList'] = self.user_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        if m.get('UserIdList') is not None:
            self.user_id_list = m.get('UserIdList')
        return self


class DescribeEndPointEventListResponseBodyNodesEventDataItemsEventList(TeaModel):
    def __init__(
        self,
        acs: str = None,
        event_code: str = None,
        event_name: str = None,
        event_type: str = None,
        os: str = None,
        sdk: str = None,
        stream_name: str = None,
        stream_type: str = None,
        track_code: str = None,
        track_name: str = None,
        ts: int = None,
        ts_in_ms: str = None,
        user_id: str = None,
    ):
        self.acs = acs
        self.event_code = event_code
        self.event_name = event_name
        self.event_type = event_type
        self.os = os
        self.sdk = sdk
        self.stream_name = stream_name
        self.stream_type = stream_type
        self.track_code = track_code
        self.track_name = track_name
        self.ts = ts
        self.ts_in_ms = ts_in_ms
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acs is not None:
            result['Acs'] = self.acs
        if self.event_code is not None:
            result['EventCode'] = self.event_code
        if self.event_name is not None:
            result['EventName'] = self.event_name
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.os is not None:
            result['Os'] = self.os
        if self.sdk is not None:
            result['Sdk'] = self.sdk
        if self.stream_name is not None:
            result['StreamName'] = self.stream_name
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        if self.track_code is not None:
            result['TrackCode'] = self.track_code
        if self.track_name is not None:
            result['TrackName'] = self.track_name
        if self.ts is not None:
            result['Ts'] = self.ts
        if self.ts_in_ms is not None:
            result['TsInMs'] = self.ts_in_ms
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Acs') is not None:
            self.acs = m.get('Acs')
        if m.get('EventCode') is not None:
            self.event_code = m.get('EventCode')
        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('Os') is not None:
            self.os = m.get('Os')
        if m.get('Sdk') is not None:
            self.sdk = m.get('Sdk')
        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        if m.get('TrackCode') is not None:
            self.track_code = m.get('TrackCode')
        if m.get('TrackName') is not None:
            self.track_name = m.get('TrackName')
        if m.get('Ts') is not None:
            self.ts = m.get('Ts')
        if m.get('TsInMs') is not None:
            self.ts_in_ms = m.get('TsInMs')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeEndPointEventListResponseBodyNodesEventDataItems(TeaModel):
    def __init__(
        self,
        event_list: List[DescribeEndPointEventListResponseBodyNodesEventDataItemsEventList] = None,
        ts: int = None,
    ):
        self.event_list = event_list
        self.ts = ts

    def validate(self):
        if self.event_list:
            for k in self.event_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EventList'] = []
        if self.event_list is not None:
            for k in self.event_list:
                result['EventList'].append(k.to_map() if k else None)
        if self.ts is not None:
            result['Ts'] = self.ts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event_list = []
        if m.get('EventList') is not None:
            for k in m.get('EventList'):
                temp_model = DescribeEndPointEventListResponseBodyNodesEventDataItemsEventList()
                self.event_list.append(temp_model.from_map(k))
        if m.get('Ts') is not None:
            self.ts = m.get('Ts')
        return self


class DescribeEndPointEventListResponseBodyNodes(TeaModel):
    def __init__(
        self,
        event_data_items: List[DescribeEndPointEventListResponseBodyNodesEventDataItems] = None,
        user_id: str = None,
    ):
        self.event_data_items = event_data_items
        self.user_id = user_id

    def validate(self):
        if self.event_data_items:
            for k in self.event_data_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EventDataItems'] = []
        if self.event_data_items is not None:
            for k in self.event_data_items:
                result['EventDataItems'].append(k.to_map() if k else None)
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event_data_items = []
        if m.get('EventDataItems') is not None:
            for k in m.get('EventDataItems'):
                temp_model = DescribeEndPointEventListResponseBodyNodesEventDataItems()
                self.event_data_items.append(temp_model.from_map(k))
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeEndPointEventListResponseBody(TeaModel):
    def __init__(
        self,
        nodes: List[DescribeEndPointEventListResponseBodyNodes] = None,
        request_id: str = None,
    ):
        self.nodes = nodes
        self.request_id = request_id

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = DescribeEndPointEventListResponseBodyNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeEndPointEventListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeEndPointEventListResponseBody = None,
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
            temp_model = DescribeEndPointEventListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEndPointMetricDataRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        created_ts: int = None,
        destroyed_ts: int = None,
        metrics: str = None,
        pub_call_id_list: str = None,
        pub_user_id: str = None,
        sub_user_id: str = None,
    ):
        self.app_id = app_id
        self.channel_id = channel_id
        self.created_ts = created_ts
        self.destroyed_ts = destroyed_ts
        self.metrics = metrics
        self.pub_call_id_list = pub_call_id_list
        self.pub_user_id = pub_user_id
        self.sub_user_id = sub_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        if self.metrics is not None:
            result['Metrics'] = self.metrics
        if self.pub_call_id_list is not None:
            result['PubCallIdList'] = self.pub_call_id_list
        if self.pub_user_id is not None:
            result['PubUserId'] = self.pub_user_id
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        if m.get('Metrics') is not None:
            self.metrics = m.get('Metrics')
        if m.get('PubCallIdList') is not None:
            self.pub_call_id_list = m.get('PubCallIdList')
        if m.get('PubUserId') is not None:
            self.pub_user_id = m.get('PubUserId')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class DescribeEndPointMetricDataResponseBodyPubMetricsNodes(TeaModel):
    def __init__(
        self,
        ext: Dict[str, Any] = None,
        x: str = None,
        y: str = None,
    ):
        self.ext = ext
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class DescribeEndPointMetricDataResponseBodyPubMetrics(TeaModel):
    def __init__(
        self,
        nodes: List[DescribeEndPointMetricDataResponseBodyPubMetricsNodes] = None,
        type: str = None,
        user_id: str = None,
    ):
        self.nodes = nodes
        self.type = type
        self.user_id = user_id

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = DescribeEndPointMetricDataResponseBodyPubMetricsNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeEndPointMetricDataResponseBodySubMetricsNodes(TeaModel):
    def __init__(
        self,
        ext: Dict[str, Any] = None,
        x: str = None,
        y: str = None,
    ):
        self.ext = ext
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class DescribeEndPointMetricDataResponseBodySubMetrics(TeaModel):
    def __init__(
        self,
        nodes: List[DescribeEndPointMetricDataResponseBodySubMetricsNodes] = None,
        type: str = None,
        user_id: str = None,
    ):
        self.nodes = nodes
        self.type = type
        self.user_id = user_id

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = DescribeEndPointMetricDataResponseBodySubMetricsNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeEndPointMetricDataResponseBody(TeaModel):
    def __init__(
        self,
        pub_metrics: List[DescribeEndPointMetricDataResponseBodyPubMetrics] = None,
        request_id: str = None,
        sub_metrics: List[DescribeEndPointMetricDataResponseBodySubMetrics] = None,
    ):
        self.pub_metrics = pub_metrics
        self.request_id = request_id
        self.sub_metrics = sub_metrics

    def validate(self):
        if self.pub_metrics:
            for k in self.pub_metrics:
                if k:
                    k.validate()
        if self.sub_metrics:
            for k in self.sub_metrics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PubMetrics'] = []
        if self.pub_metrics is not None:
            for k in self.pub_metrics:
                result['PubMetrics'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SubMetrics'] = []
        if self.sub_metrics is not None:
            for k in self.sub_metrics:
                result['SubMetrics'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.pub_metrics = []
        if m.get('PubMetrics') is not None:
            for k in m.get('PubMetrics'):
                temp_model = DescribeEndPointMetricDataResponseBodyPubMetrics()
                self.pub_metrics.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.sub_metrics = []
        if m.get('SubMetrics') is not None:
            for k in m.get('SubMetrics'):
                temp_model = DescribeEndPointMetricDataResponseBodySubMetrics()
                self.sub_metrics.append(temp_model.from_map(k))
        return self


class DescribeEndPointMetricDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeEndPointMetricDataResponseBody = None,
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
            temp_model = DescribeEndPointMetricDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFaultDiagnosisFactorDistributionStatRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        end_ts: int = None,
        start_ts: int = None,
    ):
        self.app_id = app_id
        self.end_ts = end_ts
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
        if self.start_ts is not None:
            result['StartTs'] = self.start_ts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndTs') is not None:
            self.end_ts = m.get('EndTs')
        if m.get('StartTs') is not None:
            self.start_ts = m.get('StartTs')
        return self


class DescribeFaultDiagnosisFactorDistributionStatResponseBodyStatList(TeaModel):
    def __init__(
        self,
        factor_id: str = None,
        user_count: int = None,
        user_ratio: float = None,
    ):
        self.factor_id = factor_id
        self.user_count = user_count
        self.user_ratio = user_ratio

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.factor_id is not None:
            result['FactorId'] = self.factor_id
        if self.user_count is not None:
            result['UserCount'] = self.user_count
        if self.user_ratio is not None:
            result['UserRatio'] = self.user_ratio
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FactorId') is not None:
            self.factor_id = m.get('FactorId')
        if m.get('UserCount') is not None:
            self.user_count = m.get('UserCount')
        if m.get('UserRatio') is not None:
            self.user_ratio = m.get('UserRatio')
        return self


class DescribeFaultDiagnosisFactorDistributionStatResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        stat_list: List[DescribeFaultDiagnosisFactorDistributionStatResponseBodyStatList] = None,
    ):
        self.request_id = request_id
        self.stat_list = stat_list

    def validate(self):
        if self.stat_list:
            for k in self.stat_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['StatList'] = []
        if self.stat_list is not None:
            for k in self.stat_list:
                result['StatList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.stat_list = []
        if m.get('StatList') is not None:
            for k in m.get('StatList'):
                temp_model = DescribeFaultDiagnosisFactorDistributionStatResponseBodyStatList()
                self.stat_list.append(temp_model.from_map(k))
        return self


class DescribeFaultDiagnosisFactorDistributionStatResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFaultDiagnosisFactorDistributionStatResponseBody = None,
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
            temp_model = DescribeFaultDiagnosisFactorDistributionStatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFaultDiagnosisOverallDataRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        end_ts: int = None,
        start_ts: int = None,
        stat_dim: str = None,
    ):
        self.app_id = app_id
        self.end_ts = end_ts
        self.start_ts = start_ts
        self.stat_dim = stat_dim

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
        if self.start_ts is not None:
            result['StartTs'] = self.start_ts
        if self.stat_dim is not None:
            result['StatDim'] = self.stat_dim
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndTs') is not None:
            self.end_ts = m.get('EndTs')
        if m.get('StartTs') is not None:
            self.start_ts = m.get('StartTs')
        if m.get('StatDim') is not None:
            self.stat_dim = m.get('StatDim')
        return self


class DescribeFaultDiagnosisOverallDataResponseBodyMetricDataNodes(TeaModel):
    def __init__(
        self,
        ext: Dict[str, Any] = None,
        x: str = None,
        y: str = None,
    ):
        self.ext = ext
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class DescribeFaultDiagnosisOverallDataResponseBodyMetricData(TeaModel):
    def __init__(
        self,
        nodes: List[DescribeFaultDiagnosisOverallDataResponseBodyMetricDataNodes] = None,
    ):
        self.nodes = nodes

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = DescribeFaultDiagnosisOverallDataResponseBodyMetricDataNodes()
                self.nodes.append(temp_model.from_map(k))
        return self


class DescribeFaultDiagnosisOverallDataResponseBodyOverallData(TeaModel):
    def __init__(
        self,
        fault_user_count: int = None,
        fault_user_ratio: float = None,
        total_user_count: int = None,
    ):
        self.fault_user_count = fault_user_count
        self.fault_user_ratio = fault_user_ratio
        self.total_user_count = total_user_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fault_user_count is not None:
            result['FaultUserCount'] = self.fault_user_count
        if self.fault_user_ratio is not None:
            result['FaultUserRatio'] = self.fault_user_ratio
        if self.total_user_count is not None:
            result['TotalUserCount'] = self.total_user_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaultUserCount') is not None:
            self.fault_user_count = m.get('FaultUserCount')
        if m.get('FaultUserRatio') is not None:
            self.fault_user_ratio = m.get('FaultUserRatio')
        if m.get('TotalUserCount') is not None:
            self.total_user_count = m.get('TotalUserCount')
        return self


class DescribeFaultDiagnosisOverallDataResponseBody(TeaModel):
    def __init__(
        self,
        metric_data: DescribeFaultDiagnosisOverallDataResponseBodyMetricData = None,
        overall_data: DescribeFaultDiagnosisOverallDataResponseBodyOverallData = None,
        request_id: str = None,
    ):
        self.metric_data = metric_data
        self.overall_data = overall_data
        self.request_id = request_id

    def validate(self):
        if self.metric_data:
            self.metric_data.validate()
        if self.overall_data:
            self.overall_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metric_data is not None:
            result['MetricData'] = self.metric_data.to_map()
        if self.overall_data is not None:
            result['OverallData'] = self.overall_data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetricData') is not None:
            temp_model = DescribeFaultDiagnosisOverallDataResponseBodyMetricData()
            self.metric_data = temp_model.from_map(m['MetricData'])
        if m.get('OverallData') is not None:
            temp_model = DescribeFaultDiagnosisOverallDataResponseBodyOverallData()
            self.overall_data = temp_model.from_map(m['OverallData'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeFaultDiagnosisOverallDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFaultDiagnosisOverallDataResponseBody = None,
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
            temp_model = DescribeFaultDiagnosisOverallDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFaultDiagnosisUserDetailRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        created_ts: int = None,
        fault_type: str = None,
        query_call_user_info: bool = None,
        user_id: str = None,
    ):
        self.app_id = app_id
        self.channel_id = channel_id
        self.created_ts = created_ts
        self.fault_type = fault_type
        self.query_call_user_info = query_call_user_info
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.fault_type is not None:
            result['FaultType'] = self.fault_type
        if self.query_call_user_info is not None:
            result['QueryCallUserInfo'] = self.query_call_user_info
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('FaultType') is not None:
            self.fault_type = m.get('FaultType')
        if m.get('QueryCallUserInfo') is not None:
            self.query_call_user_info = m.get('QueryCallUserInfo')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeFaultDiagnosisUserDetailResponseBodyCallInfo(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        call_status: str = None,
        channel_id: str = None,
        created_ts: int = None,
        destroyed_ts: int = None,
        duration: int = None,
    ):
        # App ID。
        self.app_id = app_id
        self.call_status = call_status
        self.channel_id = channel_id
        self.created_ts = created_ts
        self.destroyed_ts = destroyed_ts
        self.duration = duration

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.call_status is not None:
            result['CallStatus'] = self.call_status
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        if self.duration is not None:
            result['Duration'] = self.duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CallStatus') is not None:
            self.call_status = m.get('CallStatus')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        return self


class DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedEventDatasEventDataItemsEventList(TeaModel):
    def __init__(
        self,
        acs: str = None,
        event_code: str = None,
        event_name: str = None,
        event_type: str = None,
        os: str = None,
        sdk: str = None,
        stream_name: str = None,
        stream_type: str = None,
        track_code: str = None,
        track_name: str = None,
        ts: int = None,
        user_id: str = None,
    ):
        self.acs = acs
        self.event_code = event_code
        self.event_name = event_name
        self.event_type = event_type
        self.os = os
        self.sdk = sdk
        self.stream_name = stream_name
        self.stream_type = stream_type
        self.track_code = track_code
        self.track_name = track_name
        self.ts = ts
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acs is not None:
            result['Acs'] = self.acs
        if self.event_code is not None:
            result['EventCode'] = self.event_code
        if self.event_name is not None:
            result['EventName'] = self.event_name
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.os is not None:
            result['Os'] = self.os
        if self.sdk is not None:
            result['Sdk'] = self.sdk
        if self.stream_name is not None:
            result['StreamName'] = self.stream_name
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        if self.track_code is not None:
            result['TrackCode'] = self.track_code
        if self.track_name is not None:
            result['TrackName'] = self.track_name
        if self.ts is not None:
            result['Ts'] = self.ts
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Acs') is not None:
            self.acs = m.get('Acs')
        if m.get('EventCode') is not None:
            self.event_code = m.get('EventCode')
        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('Os') is not None:
            self.os = m.get('Os')
        if m.get('Sdk') is not None:
            self.sdk = m.get('Sdk')
        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        if m.get('TrackCode') is not None:
            self.track_code = m.get('TrackCode')
        if m.get('TrackName') is not None:
            self.track_name = m.get('TrackName')
        if m.get('Ts') is not None:
            self.ts = m.get('Ts')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedEventDatasEventDataItems(TeaModel):
    def __init__(
        self,
        event_list: List[DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedEventDatasEventDataItemsEventList] = None,
        ts: int = None,
    ):
        self.event_list = event_list
        self.ts = ts

    def validate(self):
        if self.event_list:
            for k in self.event_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EventList'] = []
        if self.event_list is not None:
            for k in self.event_list:
                result['EventList'].append(k.to_map() if k else None)
        if self.ts is not None:
            result['Ts'] = self.ts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event_list = []
        if m.get('EventList') is not None:
            for k in m.get('EventList'):
                temp_model = DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedEventDatasEventDataItemsEventList()
                self.event_list.append(temp_model.from_map(k))
        if m.get('Ts') is not None:
            self.ts = m.get('Ts')
        return self


class DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedEventDatas(TeaModel):
    def __init__(
        self,
        event_data_items: List[DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedEventDatasEventDataItems] = None,
        role: str = None,
        user_id: str = None,
    ):
        self.event_data_items = event_data_items
        self.role = role
        self.user_id = user_id

    def validate(self):
        if self.event_data_items:
            for k in self.event_data_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EventDataItems'] = []
        if self.event_data_items is not None:
            for k in self.event_data_items:
                result['EventDataItems'].append(k.to_map() if k else None)
        if self.role is not None:
            result['Role'] = self.role
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event_data_items = []
        if m.get('EventDataItems') is not None:
            for k in m.get('EventDataItems'):
                temp_model = DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedEventDatasEventDataItems()
                self.event_data_items.append(temp_model.from_map(k))
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedMetricDatasNodes(TeaModel):
    def __init__(
        self,
        ext: Dict[str, Any] = None,
        x: str = None,
        y: str = None,
    ):
        self.ext = ext
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedMetricDatas(TeaModel):
    def __init__(
        self,
        nodes: List[DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedMetricDatasNodes] = None,
        role: str = None,
        type: str = None,
        user_id: str = None,
    ):
        self.nodes = nodes
        self.role = role
        self.type = type
        self.user_id = user_id

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.role is not None:
            result['Role'] = self.role
        if self.type is not None:
            result['Type'] = self.type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedMetricDatasNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeFaultDiagnosisUserDetailResponseBodyFactorList(TeaModel):
    def __init__(
        self,
        factor_id: str = None,
        fault_source: str = None,
        related_event_datas: List[DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedEventDatas] = None,
        related_metric_datas: List[DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedMetricDatas] = None,
    ):
        self.factor_id = factor_id
        self.fault_source = fault_source
        self.related_event_datas = related_event_datas
        self.related_metric_datas = related_metric_datas

    def validate(self):
        if self.related_event_datas:
            for k in self.related_event_datas:
                if k:
                    k.validate()
        if self.related_metric_datas:
            for k in self.related_metric_datas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.factor_id is not None:
            result['FactorId'] = self.factor_id
        if self.fault_source is not None:
            result['FaultSource'] = self.fault_source
        result['RelatedEventDatas'] = []
        if self.related_event_datas is not None:
            for k in self.related_event_datas:
                result['RelatedEventDatas'].append(k.to_map() if k else None)
        result['RelatedMetricDatas'] = []
        if self.related_metric_datas is not None:
            for k in self.related_metric_datas:
                result['RelatedMetricDatas'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FactorId') is not None:
            self.factor_id = m.get('FactorId')
        if m.get('FaultSource') is not None:
            self.fault_source = m.get('FaultSource')
        self.related_event_datas = []
        if m.get('RelatedEventDatas') is not None:
            for k in m.get('RelatedEventDatas'):
                temp_model = DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedEventDatas()
                self.related_event_datas.append(temp_model.from_map(k))
        self.related_metric_datas = []
        if m.get('RelatedMetricDatas') is not None:
            for k in m.get('RelatedMetricDatas'):
                temp_model = DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedMetricDatas()
                self.related_metric_datas.append(temp_model.from_map(k))
        return self


class DescribeFaultDiagnosisUserDetailResponseBodyFaultMetricDataNodes(TeaModel):
    def __init__(
        self,
        x: str = None,
        y: str = None,
    ):
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class DescribeFaultDiagnosisUserDetailResponseBodyFaultMetricData(TeaModel):
    def __init__(
        self,
        nodes: List[DescribeFaultDiagnosisUserDetailResponseBodyFaultMetricDataNodes] = None,
    ):
        self.nodes = nodes

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = DescribeFaultDiagnosisUserDetailResponseBodyFaultMetricDataNodes()
                self.nodes.append(temp_model.from_map(k))
        return self


class DescribeFaultDiagnosisUserDetailResponseBodyUserDetailOnlinePeriods(TeaModel):
    def __init__(
        self,
        join_ts: int = None,
        leave_ts: int = None,
    ):
        self.join_ts = join_ts
        self.leave_ts = leave_ts

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.join_ts is not None:
            result['JoinTs'] = self.join_ts
        if self.leave_ts is not None:
            result['LeaveTs'] = self.leave_ts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JoinTs') is not None:
            self.join_ts = m.get('JoinTs')
        if m.get('LeaveTs') is not None:
            self.leave_ts = m.get('LeaveTs')
        return self


class DescribeFaultDiagnosisUserDetailResponseBodyUserDetail(TeaModel):
    def __init__(
        self,
        created_ts: int = None,
        destroyed_ts: int = None,
        duration: int = None,
        location: str = None,
        network: str = None,
        online_duration: int = None,
        online_periods: List[DescribeFaultDiagnosisUserDetailResponseBodyUserDetailOnlinePeriods] = None,
        os: str = None,
        sdk_version: str = None,
        user_id: str = None,
    ):
        self.created_ts = created_ts
        self.destroyed_ts = destroyed_ts
        self.duration = duration
        self.location = location
        self.network = network
        self.online_duration = online_duration
        self.online_periods = online_periods
        self.os = os
        self.sdk_version = sdk_version
        self.user_id = user_id

    def validate(self):
        if self.online_periods:
            for k in self.online_periods:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.location is not None:
            result['Location'] = self.location
        if self.network is not None:
            result['Network'] = self.network
        if self.online_duration is not None:
            result['OnlineDuration'] = self.online_duration
        result['OnlinePeriods'] = []
        if self.online_periods is not None:
            for k in self.online_periods:
                result['OnlinePeriods'].append(k.to_map() if k else None)
        if self.os is not None:
            result['Os'] = self.os
        if self.sdk_version is not None:
            result['SdkVersion'] = self.sdk_version
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('OnlineDuration') is not None:
            self.online_duration = m.get('OnlineDuration')
        self.online_periods = []
        if m.get('OnlinePeriods') is not None:
            for k in m.get('OnlinePeriods'):
                temp_model = DescribeFaultDiagnosisUserDetailResponseBodyUserDetailOnlinePeriods()
                self.online_periods.append(temp_model.from_map(k))
        if m.get('Os') is not None:
            self.os = m.get('Os')
        if m.get('SdkVersion') is not None:
            self.sdk_version = m.get('SdkVersion')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeFaultDiagnosisUserDetailResponseBody(TeaModel):
    def __init__(
        self,
        call_info: DescribeFaultDiagnosisUserDetailResponseBodyCallInfo = None,
        factor_list: List[DescribeFaultDiagnosisUserDetailResponseBodyFactorList] = None,
        fault_metric_data: DescribeFaultDiagnosisUserDetailResponseBodyFaultMetricData = None,
        network_operators: List[str] = None,
        request_id: str = None,
        user_detail: DescribeFaultDiagnosisUserDetailResponseBodyUserDetail = None,
    ):
        self.call_info = call_info
        self.factor_list = factor_list
        self.fault_metric_data = fault_metric_data
        self.network_operators = network_operators
        self.request_id = request_id
        self.user_detail = user_detail

    def validate(self):
        if self.call_info:
            self.call_info.validate()
        if self.factor_list:
            for k in self.factor_list:
                if k:
                    k.validate()
        if self.fault_metric_data:
            self.fault_metric_data.validate()
        if self.user_detail:
            self.user_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_info is not None:
            result['CallInfo'] = self.call_info.to_map()
        result['FactorList'] = []
        if self.factor_list is not None:
            for k in self.factor_list:
                result['FactorList'].append(k.to_map() if k else None)
        if self.fault_metric_data is not None:
            result['FaultMetricData'] = self.fault_metric_data.to_map()
        if self.network_operators is not None:
            result['NetworkOperators'] = self.network_operators
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_detail is not None:
            result['UserDetail'] = self.user_detail.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallInfo') is not None:
            temp_model = DescribeFaultDiagnosisUserDetailResponseBodyCallInfo()
            self.call_info = temp_model.from_map(m['CallInfo'])
        self.factor_list = []
        if m.get('FactorList') is not None:
            for k in m.get('FactorList'):
                temp_model = DescribeFaultDiagnosisUserDetailResponseBodyFactorList()
                self.factor_list.append(temp_model.from_map(k))
        if m.get('FaultMetricData') is not None:
            temp_model = DescribeFaultDiagnosisUserDetailResponseBodyFaultMetricData()
            self.fault_metric_data = temp_model.from_map(m['FaultMetricData'])
        if m.get('NetworkOperators') is not None:
            self.network_operators = m.get('NetworkOperators')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserDetail') is not None:
            temp_model = DescribeFaultDiagnosisUserDetailResponseBodyUserDetail()
            self.user_detail = temp_model.from_map(m['UserDetail'])
        return self


class DescribeFaultDiagnosisUserDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFaultDiagnosisUserDetailResponseBody = None,
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
            temp_model = DescribeFaultDiagnosisUserDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFaultDiagnosisUserListRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        end_ts: int = None,
        fault_types: str = None,
        page_no: int = None,
        page_size: int = None,
        start_ts: int = None,
        user_id: str = None,
    ):
        self.app_id = app_id
        self.channel_id = channel_id
        self.end_ts = end_ts
        self.fault_types = fault_types
        self.page_no = page_no
        self.page_size = page_size
        self.start_ts = start_ts
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.end_ts is not None:
            result['EndTs'] = self.end_ts
        if self.fault_types is not None:
            result['FaultTypes'] = self.fault_types
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_ts is not None:
            result['StartTs'] = self.start_ts
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('EndTs') is not None:
            self.end_ts = m.get('EndTs')
        if m.get('FaultTypes') is not None:
            self.fault_types = m.get('FaultTypes')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTs') is not None:
            self.start_ts = m.get('StartTs')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeFaultDiagnosisUserListResponseBodyUserListFaultList(TeaModel):
    def __init__(
        self,
        fault_type: str = None,
    ):
        self.fault_type = fault_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fault_type is not None:
            result['FaultType'] = self.fault_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaultType') is not None:
            self.fault_type = m.get('FaultType')
        return self


class DescribeFaultDiagnosisUserListResponseBodyUserList(TeaModel):
    def __init__(
        self,
        channel_created_ts: int = None,
        channel_id: str = None,
        created_ts: int = None,
        destroyed_ts: int = None,
        fault_list: List[DescribeFaultDiagnosisUserListResponseBodyUserListFaultList] = None,
        user_id: str = None,
    ):
        self.channel_created_ts = channel_created_ts
        self.channel_id = channel_id
        self.created_ts = created_ts
        self.destroyed_ts = destroyed_ts
        self.fault_list = fault_list
        self.user_id = user_id

    def validate(self):
        if self.fault_list:
            for k in self.fault_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_created_ts is not None:
            result['ChannelCreatedTs'] = self.channel_created_ts
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        result['FaultList'] = []
        if self.fault_list is not None:
            for k in self.fault_list:
                result['FaultList'].append(k.to_map() if k else None)
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelCreatedTs') is not None:
            self.channel_created_ts = m.get('ChannelCreatedTs')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        self.fault_list = []
        if m.get('FaultList') is not None:
            for k in m.get('FaultList'):
                temp_model = DescribeFaultDiagnosisUserListResponseBodyUserListFaultList()
                self.fault_list.append(temp_model.from_map(k))
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeFaultDiagnosisUserListResponseBody(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total_cnt: int = None,
        user_list: List[DescribeFaultDiagnosisUserListResponseBodyUserList] = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.request_id = request_id
        self.total_cnt = total_cnt
        self.user_list = user_list

    def validate(self):
        if self.user_list:
            for k in self.user_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_cnt is not None:
            result['TotalCnt'] = self.total_cnt
        result['UserList'] = []
        if self.user_list is not None:
            for k in self.user_list:
                result['UserList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCnt') is not None:
            self.total_cnt = m.get('TotalCnt')
        self.user_list = []
        if m.get('UserList') is not None:
            for k in m.get('UserList'):
                temp_model = DescribeFaultDiagnosisUserListResponseBodyUserList()
                self.user_list.append(temp_model.from_map(k))
        return self


class DescribeFaultDiagnosisUserListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFaultDiagnosisUserListResponseBody = None,
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
            temp_model = DescribeFaultDiagnosisUserListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeIceDurPeriodByDaySubTypeRequest(TeaModel):
    def __init__(
        self,
        end_ts: int = None,
        job_type: str = None,
        start_ts: int = None,
        time_zone: str = None,
    ):
        self.end_ts = end_ts
        self.job_type = job_type
        self.start_ts = start_ts
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_ts is not None:
            result['EndTs'] = self.end_ts
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.start_ts is not None:
            result['StartTs'] = self.start_ts
        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTs') is not None:
            self.end_ts = m.get('EndTs')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('StartTs') is not None:
            self.start_ts = m.get('StartTs')
        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')
        return self


class DescribeIceDurPeriodByDaySubTypeResponseBodyJobInfoListSubJobInfoList(TeaModel):
    def __init__(
        self,
        sub_job_duration: int = None,
        sub_job_type: str = None,
    ):
        self.sub_job_duration = sub_job_duration
        self.sub_job_type = sub_job_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sub_job_duration is not None:
            result['SubJobDuration'] = self.sub_job_duration
        if self.sub_job_type is not None:
            result['SubJobType'] = self.sub_job_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubJobDuration') is not None:
            self.sub_job_duration = m.get('SubJobDuration')
        if m.get('SubJobType') is not None:
            self.sub_job_type = m.get('SubJobType')
        return self


class DescribeIceDurPeriodByDaySubTypeResponseBodyJobInfoList(TeaModel):
    def __init__(
        self,
        date_ts: int = None,
        duration: int = None,
        sub_job_info_list: List[DescribeIceDurPeriodByDaySubTypeResponseBodyJobInfoListSubJobInfoList] = None,
    ):
        self.date_ts = date_ts
        self.duration = duration
        self.sub_job_info_list = sub_job_info_list

    def validate(self):
        if self.sub_job_info_list:
            for k in self.sub_job_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_ts is not None:
            result['DateTs'] = self.date_ts
        if self.duration is not None:
            result['Duration'] = self.duration
        result['SubJobInfoList'] = []
        if self.sub_job_info_list is not None:
            for k in self.sub_job_info_list:
                result['SubJobInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DateTs') is not None:
            self.date_ts = m.get('DateTs')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        self.sub_job_info_list = []
        if m.get('SubJobInfoList') is not None:
            for k in m.get('SubJobInfoList'):
                temp_model = DescribeIceDurPeriodByDaySubTypeResponseBodyJobInfoListSubJobInfoList()
                self.sub_job_info_list.append(temp_model.from_map(k))
        return self


class DescribeIceDurPeriodByDaySubTypeResponseBody(TeaModel):
    def __init__(
        self,
        job_info_list: List[DescribeIceDurPeriodByDaySubTypeResponseBodyJobInfoList] = None,
        request_id: str = None,
    ):
        self.job_info_list = job_info_list
        self.request_id = request_id

    def validate(self):
        if self.job_info_list:
            for k in self.job_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['JobInfoList'] = []
        if self.job_info_list is not None:
            for k in self.job_info_list:
                result['JobInfoList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.job_info_list = []
        if m.get('JobInfoList') is not None:
            for k in m.get('JobInfoList'):
                temp_model = DescribeIceDurPeriodByDaySubTypeResponseBodyJobInfoList()
                self.job_info_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeIceDurPeriodByDaySubTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeIceDurPeriodByDaySubTypeResponseBody = None,
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
            temp_model = DescribeIceDurPeriodByDaySubTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeIceDurSummaryOverviewRequest(TeaModel):
    def __init__(
        self,
        cur_ts: int = None,
        time_zone: str = None,
    ):
        self.cur_ts = cur_ts
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cur_ts is not None:
            result['CurTs'] = self.cur_ts
        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurTs') is not None:
            self.cur_ts = m.get('CurTs')
        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')
        return self


class DescribeIceDurSummaryOverviewResponseBodyJobInfoList(TeaModel):
    def __init__(
        self,
        duration: int = None,
        job_type: str = None,
        time_range: str = None,
    ):
        self.duration = duration
        self.job_type = job_type
        self.time_range = time_range

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.time_range is not None:
            result['TimeRange'] = self.time_range
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('TimeRange') is not None:
            self.time_range = m.get('TimeRange')
        return self


class DescribeIceDurSummaryOverviewResponseBody(TeaModel):
    def __init__(
        self,
        job_info_list: List[DescribeIceDurSummaryOverviewResponseBodyJobInfoList] = None,
        request_id: str = None,
    ):
        self.job_info_list = job_info_list
        self.request_id = request_id

    def validate(self):
        if self.job_info_list:
            for k in self.job_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['JobInfoList'] = []
        if self.job_info_list is not None:
            for k in self.job_info_list:
                result['JobInfoList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.job_info_list = []
        if m.get('JobInfoList') is not None:
            for k in m.get('JobInfoList'):
                temp_model = DescribeIceDurSummaryOverviewResponseBodyJobInfoList()
                self.job_info_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeIceDurSummaryOverviewResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeIceDurSummaryOverviewResponseBody = None,
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
            temp_model = DescribeIceDurSummaryOverviewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePubUserListBySubUserRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        created_ts: int = None,
        destroyed_ts: int = None,
        sub_user_id: str = None,
    ):
        self.app_id = app_id
        self.channel_id = channel_id
        self.created_ts = created_ts
        self.destroyed_ts = destroyed_ts
        self.sub_user_id = sub_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class DescribePubUserListBySubUserResponseBodyPubUserDetailListOnlinePeriods(TeaModel):
    def __init__(
        self,
        join_ts: int = None,
        leave_ts: int = None,
    ):
        self.join_ts = join_ts
        self.leave_ts = leave_ts

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.join_ts is not None:
            result['JoinTs'] = self.join_ts
        if self.leave_ts is not None:
            result['LeaveTs'] = self.leave_ts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JoinTs') is not None:
            self.join_ts = m.get('JoinTs')
        if m.get('LeaveTs') is not None:
            self.leave_ts = m.get('LeaveTs')
        return self


class DescribePubUserListBySubUserResponseBodyPubUserDetailList(TeaModel):
    def __init__(
        self,
        call_id_list: List[str] = None,
        client_type: str = None,
        created_ts: int = None,
        destroyed_ts: int = None,
        duration: int = None,
        location: str = None,
        network: str = None,
        network_list: List[str] = None,
        online_duration: int = None,
        online_periods: List[DescribePubUserListBySubUserResponseBodyPubUserDetailListOnlinePeriods] = None,
        os: str = None,
        os_list: List[str] = None,
        roles: List[str] = None,
        sdk_version: str = None,
        sdk_version_list: List[str] = None,
        user_id: str = None,
        user_id_alias: str = None,
    ):
        self.call_id_list = call_id_list
        self.client_type = client_type
        self.created_ts = created_ts
        self.destroyed_ts = destroyed_ts
        self.duration = duration
        self.location = location
        self.network = network
        self.network_list = network_list
        self.online_duration = online_duration
        self.online_periods = online_periods
        self.os = os
        self.os_list = os_list
        self.roles = roles
        self.sdk_version = sdk_version
        self.sdk_version_list = sdk_version_list
        self.user_id = user_id
        self.user_id_alias = user_id_alias

    def validate(self):
        if self.online_periods:
            for k in self.online_periods:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_id_list is not None:
            result['CallIdList'] = self.call_id_list
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.location is not None:
            result['Location'] = self.location
        if self.network is not None:
            result['Network'] = self.network
        if self.network_list is not None:
            result['NetworkList'] = self.network_list
        if self.online_duration is not None:
            result['OnlineDuration'] = self.online_duration
        result['OnlinePeriods'] = []
        if self.online_periods is not None:
            for k in self.online_periods:
                result['OnlinePeriods'].append(k.to_map() if k else None)
        if self.os is not None:
            result['Os'] = self.os
        if self.os_list is not None:
            result['OsList'] = self.os_list
        if self.roles is not None:
            result['Roles'] = self.roles
        if self.sdk_version is not None:
            result['SdkVersion'] = self.sdk_version
        if self.sdk_version_list is not None:
            result['SdkVersionList'] = self.sdk_version_list
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_id_alias is not None:
            result['UserIdAlias'] = self.user_id_alias
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallIdList') is not None:
            self.call_id_list = m.get('CallIdList')
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('NetworkList') is not None:
            self.network_list = m.get('NetworkList')
        if m.get('OnlineDuration') is not None:
            self.online_duration = m.get('OnlineDuration')
        self.online_periods = []
        if m.get('OnlinePeriods') is not None:
            for k in m.get('OnlinePeriods'):
                temp_model = DescribePubUserListBySubUserResponseBodyPubUserDetailListOnlinePeriods()
                self.online_periods.append(temp_model.from_map(k))
        if m.get('Os') is not None:
            self.os = m.get('Os')
        if m.get('OsList') is not None:
            self.os_list = m.get('OsList')
        if m.get('Roles') is not None:
            self.roles = m.get('Roles')
        if m.get('SdkVersion') is not None:
            self.sdk_version = m.get('SdkVersion')
        if m.get('SdkVersionList') is not None:
            self.sdk_version_list = m.get('SdkVersionList')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserIdAlias') is not None:
            self.user_id_alias = m.get('UserIdAlias')
        return self


class DescribePubUserListBySubUserResponseBodySubUserDetailOnlinePeriods(TeaModel):
    def __init__(
        self,
        join_ts: int = None,
        leave_ts: int = None,
    ):
        self.join_ts = join_ts
        self.leave_ts = leave_ts

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.join_ts is not None:
            result['JoinTs'] = self.join_ts
        if self.leave_ts is not None:
            result['LeaveTs'] = self.leave_ts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JoinTs') is not None:
            self.join_ts = m.get('JoinTs')
        if m.get('LeaveTs') is not None:
            self.leave_ts = m.get('LeaveTs')
        return self


class DescribePubUserListBySubUserResponseBodySubUserDetail(TeaModel):
    def __init__(
        self,
        client_type: str = None,
        created_ts: int = None,
        destroyed_ts: int = None,
        duration: int = None,
        location: str = None,
        network: str = None,
        network_list: List[str] = None,
        online_duration: int = None,
        online_periods: List[DescribePubUserListBySubUserResponseBodySubUserDetailOnlinePeriods] = None,
        os: str = None,
        os_list: List[str] = None,
        roles: List[str] = None,
        sdk_version: str = None,
        sdk_version_list: List[str] = None,
        user_id: str = None,
        user_id_alias: str = None,
    ):
        self.client_type = client_type
        self.created_ts = created_ts
        self.destroyed_ts = destroyed_ts
        self.duration = duration
        self.location = location
        self.network = network
        self.network_list = network_list
        self.online_duration = online_duration
        self.online_periods = online_periods
        self.os = os
        self.os_list = os_list
        self.roles = roles
        self.sdk_version = sdk_version
        self.sdk_version_list = sdk_version_list
        self.user_id = user_id
        self.user_id_alias = user_id_alias

    def validate(self):
        if self.online_periods:
            for k in self.online_periods:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.location is not None:
            result['Location'] = self.location
        if self.network is not None:
            result['Network'] = self.network
        if self.network_list is not None:
            result['NetworkList'] = self.network_list
        if self.online_duration is not None:
            result['OnlineDuration'] = self.online_duration
        result['OnlinePeriods'] = []
        if self.online_periods is not None:
            for k in self.online_periods:
                result['OnlinePeriods'].append(k.to_map() if k else None)
        if self.os is not None:
            result['Os'] = self.os
        if self.os_list is not None:
            result['OsList'] = self.os_list
        if self.roles is not None:
            result['Roles'] = self.roles
        if self.sdk_version is not None:
            result['SdkVersion'] = self.sdk_version
        if self.sdk_version_list is not None:
            result['SdkVersionList'] = self.sdk_version_list
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_id_alias is not None:
            result['UserIdAlias'] = self.user_id_alias
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('NetworkList') is not None:
            self.network_list = m.get('NetworkList')
        if m.get('OnlineDuration') is not None:
            self.online_duration = m.get('OnlineDuration')
        self.online_periods = []
        if m.get('OnlinePeriods') is not None:
            for k in m.get('OnlinePeriods'):
                temp_model = DescribePubUserListBySubUserResponseBodySubUserDetailOnlinePeriods()
                self.online_periods.append(temp_model.from_map(k))
        if m.get('Os') is not None:
            self.os = m.get('Os')
        if m.get('OsList') is not None:
            self.os_list = m.get('OsList')
        if m.get('Roles') is not None:
            self.roles = m.get('Roles')
        if m.get('SdkVersion') is not None:
            self.sdk_version = m.get('SdkVersion')
        if m.get('SdkVersionList') is not None:
            self.sdk_version_list = m.get('SdkVersionList')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserIdAlias') is not None:
            self.user_id_alias = m.get('UserIdAlias')
        return self


class DescribePubUserListBySubUserResponseBody(TeaModel):
    def __init__(
        self,
        call_status: str = None,
        pub_user_detail_list: List[DescribePubUserListBySubUserResponseBodyPubUserDetailList] = None,
        request_id: str = None,
        sub_user_detail: DescribePubUserListBySubUserResponseBodySubUserDetail = None,
    ):
        self.call_status = call_status
        self.pub_user_detail_list = pub_user_detail_list
        self.request_id = request_id
        self.sub_user_detail = sub_user_detail

    def validate(self):
        if self.pub_user_detail_list:
            for k in self.pub_user_detail_list:
                if k:
                    k.validate()
        if self.sub_user_detail:
            self.sub_user_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_status is not None:
            result['CallStatus'] = self.call_status
        result['PubUserDetailList'] = []
        if self.pub_user_detail_list is not None:
            for k in self.pub_user_detail_list:
                result['PubUserDetailList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_user_detail is not None:
            result['SubUserDetail'] = self.sub_user_detail.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallStatus') is not None:
            self.call_status = m.get('CallStatus')
        self.pub_user_detail_list = []
        if m.get('PubUserDetailList') is not None:
            for k in m.get('PubUserDetailList'):
                temp_model = DescribePubUserListBySubUserResponseBodyPubUserDetailList()
                self.pub_user_detail_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubUserDetail') is not None:
            temp_model = DescribePubUserListBySubUserResponseBodySubUserDetail()
            self.sub_user_detail = temp_model.from_map(m['SubUserDetail'])
        return self


class DescribePubUserListBySubUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePubUserListBySubUserResponseBody = None,
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
            temp_model = DescribePubUserListBySubUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeQoeMetricDataRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        created_ts: int = None,
        destroyed_ts: int = None,
        user_id: str = None,
    ):
        self.app_id = app_id
        self.channel_id = channel_id
        self.created_ts = created_ts
        self.destroyed_ts = destroyed_ts
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeQoeMetricDataResponseBodyAudioDataNodes(TeaModel):
    def __init__(
        self,
        x: str = None,
        y: str = None,
    ):
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class DescribeQoeMetricDataResponseBodyAudioData(TeaModel):
    def __init__(
        self,
        nodes: List[DescribeQoeMetricDataResponseBodyAudioDataNodes] = None,
        type: str = None,
        user_id: str = None,
    ):
        self.nodes = nodes
        self.type = type
        self.user_id = user_id

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = DescribeQoeMetricDataResponseBodyAudioDataNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeQoeMetricDataResponseBodyVideoDataNodes(TeaModel):
    def __init__(
        self,
        x: str = None,
        y: str = None,
    ):
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class DescribeQoeMetricDataResponseBodyVideoData(TeaModel):
    def __init__(
        self,
        nodes: List[DescribeQoeMetricDataResponseBodyVideoDataNodes] = None,
        type: str = None,
        user_id: str = None,
    ):
        self.nodes = nodes
        self.type = type
        self.user_id = user_id

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = DescribeQoeMetricDataResponseBodyVideoDataNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeQoeMetricDataResponseBody(TeaModel):
    def __init__(
        self,
        audio_data: List[DescribeQoeMetricDataResponseBodyAudioData] = None,
        request_id: str = None,
        video_data: List[DescribeQoeMetricDataResponseBodyVideoData] = None,
    ):
        self.audio_data = audio_data
        self.request_id = request_id
        self.video_data = video_data

    def validate(self):
        if self.audio_data:
            for k in self.audio_data:
                if k:
                    k.validate()
        if self.video_data:
            for k in self.video_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AudioData'] = []
        if self.audio_data is not None:
            for k in self.audio_data:
                result['AudioData'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['VideoData'] = []
        if self.video_data is not None:
            for k in self.video_data:
                result['VideoData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.audio_data = []
        if m.get('AudioData') is not None:
            for k in m.get('AudioData'):
                temp_model = DescribeQoeMetricDataResponseBodyAudioData()
                self.audio_data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.video_data = []
        if m.get('VideoData') is not None:
            for k in m.get('VideoData'):
                temp_model = DescribeQoeMetricDataResponseBodyVideoData()
                self.video_data.append(temp_model.from_map(k))
        return self


class DescribeQoeMetricDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeQoeMetricDataResponseBody = None,
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
            temp_model = DescribeQoeMetricDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeQualityAreaDistributionStatDataRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        end_date: int = None,
        parent_area: str = None,
        start_date: int = None,
    ):
        self.app_id = app_id
        self.end_date = end_date
        self.parent_area = parent_area
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.parent_area is not None:
            result['ParentArea'] = self.parent_area
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('ParentArea') is not None:
            self.parent_area = m.get('ParentArea')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class DescribeQualityAreaDistributionStatDataResponseBodyQualityStatDataList(TeaModel):
    def __init__(
        self,
        audio_delay: int = None,
        audio_high_quality_transmission_rate: str = None,
        audio_speak_out_duration: int = None,
        audio_stuck_rate: str = None,
        call_duration_ratio: str = None,
        join_channel_suc_five_sec_rate: str = None,
        join_channel_suc_rate: str = None,
        name: str = None,
        video_delay: int = None,
        video_first_pic_duration: int = None,
        video_high_quality_transmission_rate: str = None,
        video_stuck_rate: str = None,
    ):
        self.audio_delay = audio_delay
        self.audio_high_quality_transmission_rate = audio_high_quality_transmission_rate
        self.audio_speak_out_duration = audio_speak_out_duration
        self.audio_stuck_rate = audio_stuck_rate
        self.call_duration_ratio = call_duration_ratio
        self.join_channel_suc_five_sec_rate = join_channel_suc_five_sec_rate
        self.join_channel_suc_rate = join_channel_suc_rate
        self.name = name
        self.video_delay = video_delay
        self.video_first_pic_duration = video_first_pic_duration
        self.video_high_quality_transmission_rate = video_high_quality_transmission_rate
        self.video_stuck_rate = video_stuck_rate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_delay is not None:
            result['AudioDelay'] = self.audio_delay
        if self.audio_high_quality_transmission_rate is not None:
            result['AudioHighQualityTransmissionRate'] = self.audio_high_quality_transmission_rate
        if self.audio_speak_out_duration is not None:
            result['AudioSpeakOutDuration'] = self.audio_speak_out_duration
        if self.audio_stuck_rate is not None:
            result['AudioStuckRate'] = self.audio_stuck_rate
        if self.call_duration_ratio is not None:
            result['CallDurationRatio'] = self.call_duration_ratio
        if self.join_channel_suc_five_sec_rate is not None:
            result['JoinChannelSucFiveSecRate'] = self.join_channel_suc_five_sec_rate
        if self.join_channel_suc_rate is not None:
            result['JoinChannelSucRate'] = self.join_channel_suc_rate
        if self.name is not None:
            result['Name'] = self.name
        if self.video_delay is not None:
            result['VideoDelay'] = self.video_delay
        if self.video_first_pic_duration is not None:
            result['VideoFirstPicDuration'] = self.video_first_pic_duration
        if self.video_high_quality_transmission_rate is not None:
            result['VideoHighQualityTransmissionRate'] = self.video_high_quality_transmission_rate
        if self.video_stuck_rate is not None:
            result['VideoStuckRate'] = self.video_stuck_rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioDelay') is not None:
            self.audio_delay = m.get('AudioDelay')
        if m.get('AudioHighQualityTransmissionRate') is not None:
            self.audio_high_quality_transmission_rate = m.get('AudioHighQualityTransmissionRate')
        if m.get('AudioSpeakOutDuration') is not None:
            self.audio_speak_out_duration = m.get('AudioSpeakOutDuration')
        if m.get('AudioStuckRate') is not None:
            self.audio_stuck_rate = m.get('AudioStuckRate')
        if m.get('CallDurationRatio') is not None:
            self.call_duration_ratio = m.get('CallDurationRatio')
        if m.get('JoinChannelSucFiveSecRate') is not None:
            self.join_channel_suc_five_sec_rate = m.get('JoinChannelSucFiveSecRate')
        if m.get('JoinChannelSucRate') is not None:
            self.join_channel_suc_rate = m.get('JoinChannelSucRate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('VideoDelay') is not None:
            self.video_delay = m.get('VideoDelay')
        if m.get('VideoFirstPicDuration') is not None:
            self.video_first_pic_duration = m.get('VideoFirstPicDuration')
        if m.get('VideoHighQualityTransmissionRate') is not None:
            self.video_high_quality_transmission_rate = m.get('VideoHighQualityTransmissionRate')
        if m.get('VideoStuckRate') is not None:
            self.video_stuck_rate = m.get('VideoStuckRate')
        return self


class DescribeQualityAreaDistributionStatDataResponseBody(TeaModel):
    def __init__(
        self,
        quality_stat_data_list: List[DescribeQualityAreaDistributionStatDataResponseBodyQualityStatDataList] = None,
        request_id: str = None,
    ):
        self.quality_stat_data_list = quality_stat_data_list
        self.request_id = request_id

    def validate(self):
        if self.quality_stat_data_list:
            for k in self.quality_stat_data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['QualityStatDataList'] = []
        if self.quality_stat_data_list is not None:
            for k in self.quality_stat_data_list:
                result['QualityStatDataList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.quality_stat_data_list = []
        if m.get('QualityStatDataList') is not None:
            for k in m.get('QualityStatDataList'):
                temp_model = DescribeQualityAreaDistributionStatDataResponseBodyQualityStatDataList()
                self.quality_stat_data_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeQualityAreaDistributionStatDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeQualityAreaDistributionStatDataResponseBody = None,
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
            temp_model = DescribeQualityAreaDistributionStatDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeQualityDistributionStatDataRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        end_date: int = None,
        start_date: int = None,
        stat_dim: str = None,
    ):
        self.app_id = app_id
        self.end_date = end_date
        self.start_date = start_date
        self.stat_dim = stat_dim

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.stat_dim is not None:
            result['StatDim'] = self.stat_dim
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('StatDim') is not None:
            self.stat_dim = m.get('StatDim')
        return self


class DescribeQualityDistributionStatDataResponseBodyQualityStatDataList(TeaModel):
    def __init__(
        self,
        audio_delay: int = None,
        audio_high_quality_transmission_rate: str = None,
        audio_speak_out_duration: int = None,
        audio_stuck_rate: str = None,
        call_duration_ratio: str = None,
        join_channel_suc_five_sec_rate: str = None,
        join_channel_suc_rate: str = None,
        name: str = None,
        video_delay: int = None,
        video_first_pic_duration: int = None,
        video_high_quality_transmission_rate: str = None,
        video_stuck_rate: str = None,
    ):
        self.audio_delay = audio_delay
        self.audio_high_quality_transmission_rate = audio_high_quality_transmission_rate
        self.audio_speak_out_duration = audio_speak_out_duration
        self.audio_stuck_rate = audio_stuck_rate
        self.call_duration_ratio = call_duration_ratio
        self.join_channel_suc_five_sec_rate = join_channel_suc_five_sec_rate
        self.join_channel_suc_rate = join_channel_suc_rate
        self.name = name
        self.video_delay = video_delay
        self.video_first_pic_duration = video_first_pic_duration
        self.video_high_quality_transmission_rate = video_high_quality_transmission_rate
        self.video_stuck_rate = video_stuck_rate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_delay is not None:
            result['AudioDelay'] = self.audio_delay
        if self.audio_high_quality_transmission_rate is not None:
            result['AudioHighQualityTransmissionRate'] = self.audio_high_quality_transmission_rate
        if self.audio_speak_out_duration is not None:
            result['AudioSpeakOutDuration'] = self.audio_speak_out_duration
        if self.audio_stuck_rate is not None:
            result['AudioStuckRate'] = self.audio_stuck_rate
        if self.call_duration_ratio is not None:
            result['CallDurationRatio'] = self.call_duration_ratio
        if self.join_channel_suc_five_sec_rate is not None:
            result['JoinChannelSucFiveSecRate'] = self.join_channel_suc_five_sec_rate
        if self.join_channel_suc_rate is not None:
            result['JoinChannelSucRate'] = self.join_channel_suc_rate
        if self.name is not None:
            result['Name'] = self.name
        if self.video_delay is not None:
            result['VideoDelay'] = self.video_delay
        if self.video_first_pic_duration is not None:
            result['VideoFirstPicDuration'] = self.video_first_pic_duration
        if self.video_high_quality_transmission_rate is not None:
            result['VideoHighQualityTransmissionRate'] = self.video_high_quality_transmission_rate
        if self.video_stuck_rate is not None:
            result['VideoStuckRate'] = self.video_stuck_rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioDelay') is not None:
            self.audio_delay = m.get('AudioDelay')
        if m.get('AudioHighQualityTransmissionRate') is not None:
            self.audio_high_quality_transmission_rate = m.get('AudioHighQualityTransmissionRate')
        if m.get('AudioSpeakOutDuration') is not None:
            self.audio_speak_out_duration = m.get('AudioSpeakOutDuration')
        if m.get('AudioStuckRate') is not None:
            self.audio_stuck_rate = m.get('AudioStuckRate')
        if m.get('CallDurationRatio') is not None:
            self.call_duration_ratio = m.get('CallDurationRatio')
        if m.get('JoinChannelSucFiveSecRate') is not None:
            self.join_channel_suc_five_sec_rate = m.get('JoinChannelSucFiveSecRate')
        if m.get('JoinChannelSucRate') is not None:
            self.join_channel_suc_rate = m.get('JoinChannelSucRate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('VideoDelay') is not None:
            self.video_delay = m.get('VideoDelay')
        if m.get('VideoFirstPicDuration') is not None:
            self.video_first_pic_duration = m.get('VideoFirstPicDuration')
        if m.get('VideoHighQualityTransmissionRate') is not None:
            self.video_high_quality_transmission_rate = m.get('VideoHighQualityTransmissionRate')
        if m.get('VideoStuckRate') is not None:
            self.video_stuck_rate = m.get('VideoStuckRate')
        return self


class DescribeQualityDistributionStatDataResponseBody(TeaModel):
    def __init__(
        self,
        quality_stat_data_list: List[DescribeQualityDistributionStatDataResponseBodyQualityStatDataList] = None,
        request_id: str = None,
    ):
        self.quality_stat_data_list = quality_stat_data_list
        self.request_id = request_id

    def validate(self):
        if self.quality_stat_data_list:
            for k in self.quality_stat_data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['QualityStatDataList'] = []
        if self.quality_stat_data_list is not None:
            for k in self.quality_stat_data_list:
                result['QualityStatDataList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.quality_stat_data_list = []
        if m.get('QualityStatDataList') is not None:
            for k in m.get('QualityStatDataList'):
                temp_model = DescribeQualityDistributionStatDataResponseBodyQualityStatDataList()
                self.quality_stat_data_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeQualityDistributionStatDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeQualityDistributionStatDataResponseBody = None,
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
            temp_model = DescribeQualityDistributionStatDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeQualityOsSdkVersionDistributionStatDataRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        end_date: int = None,
        start_date: int = None,
    ):
        self.app_id = app_id
        self.end_date = end_date
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class DescribeQualityOsSdkVersionDistributionStatDataResponseBodyQualityOsSdkVersionStatDataList(TeaModel):
    def __init__(
        self,
        audio_delay: int = None,
        audio_high_quality_transmission_rate: str = None,
        audio_speak_out_duration: int = None,
        audio_stuck_rate: str = None,
        call_duration_ratio: str = None,
        join_channel_suc_five_sec_rate: str = None,
        join_channel_suc_rate: str = None,
        name: str = None,
        os: str = None,
        video_delay: int = None,
        video_first_pic_duration: int = None,
        video_high_quality_transmission_rate: str = None,
        video_stuck_rate: str = None,
    ):
        self.audio_delay = audio_delay
        self.audio_high_quality_transmission_rate = audio_high_quality_transmission_rate
        self.audio_speak_out_duration = audio_speak_out_duration
        self.audio_stuck_rate = audio_stuck_rate
        self.call_duration_ratio = call_duration_ratio
        self.join_channel_suc_five_sec_rate = join_channel_suc_five_sec_rate
        self.join_channel_suc_rate = join_channel_suc_rate
        self.name = name
        self.os = os
        self.video_delay = video_delay
        self.video_first_pic_duration = video_first_pic_duration
        self.video_high_quality_transmission_rate = video_high_quality_transmission_rate
        self.video_stuck_rate = video_stuck_rate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_delay is not None:
            result['AudioDelay'] = self.audio_delay
        if self.audio_high_quality_transmission_rate is not None:
            result['AudioHighQualityTransmissionRate'] = self.audio_high_quality_transmission_rate
        if self.audio_speak_out_duration is not None:
            result['AudioSpeakOutDuration'] = self.audio_speak_out_duration
        if self.audio_stuck_rate is not None:
            result['AudioStuckRate'] = self.audio_stuck_rate
        if self.call_duration_ratio is not None:
            result['CallDurationRatio'] = self.call_duration_ratio
        if self.join_channel_suc_five_sec_rate is not None:
            result['JoinChannelSucFiveSecRate'] = self.join_channel_suc_five_sec_rate
        if self.join_channel_suc_rate is not None:
            result['JoinChannelSucRate'] = self.join_channel_suc_rate
        if self.name is not None:
            result['Name'] = self.name
        if self.os is not None:
            result['Os'] = self.os
        if self.video_delay is not None:
            result['VideoDelay'] = self.video_delay
        if self.video_first_pic_duration is not None:
            result['VideoFirstPicDuration'] = self.video_first_pic_duration
        if self.video_high_quality_transmission_rate is not None:
            result['VideoHighQualityTransmissionRate'] = self.video_high_quality_transmission_rate
        if self.video_stuck_rate is not None:
            result['VideoStuckRate'] = self.video_stuck_rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioDelay') is not None:
            self.audio_delay = m.get('AudioDelay')
        if m.get('AudioHighQualityTransmissionRate') is not None:
            self.audio_high_quality_transmission_rate = m.get('AudioHighQualityTransmissionRate')
        if m.get('AudioSpeakOutDuration') is not None:
            self.audio_speak_out_duration = m.get('AudioSpeakOutDuration')
        if m.get('AudioStuckRate') is not None:
            self.audio_stuck_rate = m.get('AudioStuckRate')
        if m.get('CallDurationRatio') is not None:
            self.call_duration_ratio = m.get('CallDurationRatio')
        if m.get('JoinChannelSucFiveSecRate') is not None:
            self.join_channel_suc_five_sec_rate = m.get('JoinChannelSucFiveSecRate')
        if m.get('JoinChannelSucRate') is not None:
            self.join_channel_suc_rate = m.get('JoinChannelSucRate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Os') is not None:
            self.os = m.get('Os')
        if m.get('VideoDelay') is not None:
            self.video_delay = m.get('VideoDelay')
        if m.get('VideoFirstPicDuration') is not None:
            self.video_first_pic_duration = m.get('VideoFirstPicDuration')
        if m.get('VideoHighQualityTransmissionRate') is not None:
            self.video_high_quality_transmission_rate = m.get('VideoHighQualityTransmissionRate')
        if m.get('VideoStuckRate') is not None:
            self.video_stuck_rate = m.get('VideoStuckRate')
        return self


class DescribeQualityOsSdkVersionDistributionStatDataResponseBody(TeaModel):
    def __init__(
        self,
        quality_os_sdk_version_stat_data_list: List[DescribeQualityOsSdkVersionDistributionStatDataResponseBodyQualityOsSdkVersionStatDataList] = None,
        request_id: str = None,
    ):
        self.quality_os_sdk_version_stat_data_list = quality_os_sdk_version_stat_data_list
        self.request_id = request_id

    def validate(self):
        if self.quality_os_sdk_version_stat_data_list:
            for k in self.quality_os_sdk_version_stat_data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['QualityOsSdkVersionStatDataList'] = []
        if self.quality_os_sdk_version_stat_data_list is not None:
            for k in self.quality_os_sdk_version_stat_data_list:
                result['QualityOsSdkVersionStatDataList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.quality_os_sdk_version_stat_data_list = []
        if m.get('QualityOsSdkVersionStatDataList') is not None:
            for k in m.get('QualityOsSdkVersionStatDataList'):
                temp_model = DescribeQualityOsSdkVersionDistributionStatDataResponseBodyQualityOsSdkVersionStatDataList()
                self.quality_os_sdk_version_stat_data_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeQualityOsSdkVersionDistributionStatDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeQualityOsSdkVersionDistributionStatDataResponseBody = None,
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
            temp_model = DescribeQualityOsSdkVersionDistributionStatDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeQualityOverallDataRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        end_date: int = None,
        start_date: int = None,
        types: str = None,
    ):
        self.app_id = app_id
        self.end_date = end_date
        self.start_date = start_date
        self.types = types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.types is not None:
            result['Types'] = self.types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Types') is not None:
            self.types = m.get('Types')
        return self


class DescribeQualityOverallDataResponseBodyQualityOverallDataNodes(TeaModel):
    def __init__(
        self,
        x: str = None,
        y: str = None,
    ):
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class DescribeQualityOverallDataResponseBodyQualityOverallData(TeaModel):
    def __init__(
        self,
        average: str = None,
        nodes: List[DescribeQualityOverallDataResponseBodyQualityOverallDataNodes] = None,
        type: str = None,
    ):
        self.average = average
        self.nodes = nodes
        self.type = type

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.average is not None:
            result['Average'] = self.average
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Average') is not None:
            self.average = m.get('Average')
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = DescribeQualityOverallDataResponseBodyQualityOverallDataNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeQualityOverallDataResponseBody(TeaModel):
    def __init__(
        self,
        quality_overall_data: List[DescribeQualityOverallDataResponseBodyQualityOverallData] = None,
        request_id: str = None,
    ):
        self.quality_overall_data = quality_overall_data
        self.request_id = request_id

    def validate(self):
        if self.quality_overall_data:
            for k in self.quality_overall_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['QualityOverallData'] = []
        if self.quality_overall_data is not None:
            for k in self.quality_overall_data:
                result['QualityOverallData'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.quality_overall_data = []
        if m.get('QualityOverallData') is not None:
            for k in m.get('QualityOverallData'):
                temp_model = DescribeQualityOverallDataResponseBodyQualityOverallData()
                self.quality_overall_data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeQualityOverallDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeQualityOverallDataResponseBody = None,
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
            temp_model = DescribeQualityOverallDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUsageAreaDistributionStatDataRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        end_date: str = None,
        parent_area: str = None,
        start_date: str = None,
    ):
        self.app_id = app_id
        self.end_date = end_date
        self.parent_area = parent_area
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.parent_area is not None:
            result['ParentArea'] = self.parent_area
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('ParentArea') is not None:
            self.parent_area = m.get('ParentArea')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class DescribeUsageAreaDistributionStatDataResponseBodyUsageAreaStatList(TeaModel):
    def __init__(
        self,
        audio_call_duration: int = None,
        name: str = None,
        total_call_duration: int = None,
        video_call_duration: int = None,
    ):
        self.audio_call_duration = audio_call_duration
        self.name = name
        self.total_call_duration = total_call_duration
        self.video_call_duration = video_call_duration

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_call_duration is not None:
            result['AudioCallDuration'] = self.audio_call_duration
        if self.name is not None:
            result['Name'] = self.name
        if self.total_call_duration is not None:
            result['TotalCallDuration'] = self.total_call_duration
        if self.video_call_duration is not None:
            result['VideoCallDuration'] = self.video_call_duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioCallDuration') is not None:
            self.audio_call_duration = m.get('AudioCallDuration')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TotalCallDuration') is not None:
            self.total_call_duration = m.get('TotalCallDuration')
        if m.get('VideoCallDuration') is not None:
            self.video_call_duration = m.get('VideoCallDuration')
        return self


class DescribeUsageAreaDistributionStatDataResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        usage_area_stat_list: List[DescribeUsageAreaDistributionStatDataResponseBodyUsageAreaStatList] = None,
    ):
        self.request_id = request_id
        self.usage_area_stat_list = usage_area_stat_list

    def validate(self):
        if self.usage_area_stat_list:
            for k in self.usage_area_stat_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['UsageAreaStatList'] = []
        if self.usage_area_stat_list is not None:
            for k in self.usage_area_stat_list:
                result['UsageAreaStatList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.usage_area_stat_list = []
        if m.get('UsageAreaStatList') is not None:
            for k in m.get('UsageAreaStatList'):
                temp_model = DescribeUsageAreaDistributionStatDataResponseBodyUsageAreaStatList()
                self.usage_area_stat_list.append(temp_model.from_map(k))
        return self


class DescribeUsageAreaDistributionStatDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeUsageAreaDistributionStatDataResponseBody = None,
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
            temp_model = DescribeUsageAreaDistributionStatDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUsageDistributionStatDataRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        end_date: int = None,
        start_date: int = None,
        stat_dim: str = None,
    ):
        self.app_id = app_id
        self.end_date = end_date
        self.start_date = start_date
        self.stat_dim = stat_dim

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.stat_dim is not None:
            result['StatDim'] = self.stat_dim
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('StatDim') is not None:
            self.stat_dim = m.get('StatDim')
        return self


class DescribeUsageDistributionStatDataResponseBodyUsageStatList(TeaModel):
    def __init__(
        self,
        audio_call_duration: int = None,
        call_duration_ratio: str = None,
        name: str = None,
        total_call_duration: int = None,
        video_call_duration: int = None,
    ):
        self.audio_call_duration = audio_call_duration
        self.call_duration_ratio = call_duration_ratio
        self.name = name
        self.total_call_duration = total_call_duration
        self.video_call_duration = video_call_duration

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_call_duration is not None:
            result['AudioCallDuration'] = self.audio_call_duration
        if self.call_duration_ratio is not None:
            result['CallDurationRatio'] = self.call_duration_ratio
        if self.name is not None:
            result['Name'] = self.name
        if self.total_call_duration is not None:
            result['TotalCallDuration'] = self.total_call_duration
        if self.video_call_duration is not None:
            result['VideoCallDuration'] = self.video_call_duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioCallDuration') is not None:
            self.audio_call_duration = m.get('AudioCallDuration')
        if m.get('CallDurationRatio') is not None:
            self.call_duration_ratio = m.get('CallDurationRatio')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TotalCallDuration') is not None:
            self.total_call_duration = m.get('TotalCallDuration')
        if m.get('VideoCallDuration') is not None:
            self.video_call_duration = m.get('VideoCallDuration')
        return self


class DescribeUsageDistributionStatDataResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        usage_stat_list: List[DescribeUsageDistributionStatDataResponseBodyUsageStatList] = None,
    ):
        self.request_id = request_id
        self.usage_stat_list = usage_stat_list

    def validate(self):
        if self.usage_stat_list:
            for k in self.usage_stat_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['UsageStatList'] = []
        if self.usage_stat_list is not None:
            for k in self.usage_stat_list:
                result['UsageStatList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.usage_stat_list = []
        if m.get('UsageStatList') is not None:
            for k in m.get('UsageStatList'):
                temp_model = DescribeUsageDistributionStatDataResponseBodyUsageStatList()
                self.usage_stat_list.append(temp_model.from_map(k))
        return self


class DescribeUsageDistributionStatDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeUsageDistributionStatDataResponseBody = None,
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
            temp_model = DescribeUsageDistributionStatDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUsageOsSdkVersionDistributionStatDataRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        end_date: int = None,
        start_date: int = None,
    ):
        self.app_id = app_id
        self.end_date = end_date
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class DescribeUsageOsSdkVersionDistributionStatDataResponseBodyUsageOsSdkVersionStatList(TeaModel):
    def __init__(
        self,
        audio_call_duration: int = None,
        call_duration_ratio: str = None,
        name: str = None,
        os: str = None,
        total_call_duration: int = None,
        video_call_duration: int = None,
    ):
        self.audio_call_duration = audio_call_duration
        self.call_duration_ratio = call_duration_ratio
        self.name = name
        self.os = os
        self.total_call_duration = total_call_duration
        self.video_call_duration = video_call_duration

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_call_duration is not None:
            result['AudioCallDuration'] = self.audio_call_duration
        if self.call_duration_ratio is not None:
            result['CallDurationRatio'] = self.call_duration_ratio
        if self.name is not None:
            result['Name'] = self.name
        if self.os is not None:
            result['Os'] = self.os
        if self.total_call_duration is not None:
            result['TotalCallDuration'] = self.total_call_duration
        if self.video_call_duration is not None:
            result['VideoCallDuration'] = self.video_call_duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioCallDuration') is not None:
            self.audio_call_duration = m.get('AudioCallDuration')
        if m.get('CallDurationRatio') is not None:
            self.call_duration_ratio = m.get('CallDurationRatio')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Os') is not None:
            self.os = m.get('Os')
        if m.get('TotalCallDuration') is not None:
            self.total_call_duration = m.get('TotalCallDuration')
        if m.get('VideoCallDuration') is not None:
            self.video_call_duration = m.get('VideoCallDuration')
        return self


class DescribeUsageOsSdkVersionDistributionStatDataResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        usage_os_sdk_version_stat_list: List[DescribeUsageOsSdkVersionDistributionStatDataResponseBodyUsageOsSdkVersionStatList] = None,
    ):
        self.request_id = request_id
        self.usage_os_sdk_version_stat_list = usage_os_sdk_version_stat_list

    def validate(self):
        if self.usage_os_sdk_version_stat_list:
            for k in self.usage_os_sdk_version_stat_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['UsageOsSdkVersionStatList'] = []
        if self.usage_os_sdk_version_stat_list is not None:
            for k in self.usage_os_sdk_version_stat_list:
                result['UsageOsSdkVersionStatList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.usage_os_sdk_version_stat_list = []
        if m.get('UsageOsSdkVersionStatList') is not None:
            for k in m.get('UsageOsSdkVersionStatList'):
                temp_model = DescribeUsageOsSdkVersionDistributionStatDataResponseBodyUsageOsSdkVersionStatList()
                self.usage_os_sdk_version_stat_list.append(temp_model.from_map(k))
        return self


class DescribeUsageOsSdkVersionDistributionStatDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeUsageOsSdkVersionDistributionStatDataResponseBody = None,
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
            temp_model = DescribeUsageOsSdkVersionDistributionStatDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUsageOverallDataRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        end_date: int = None,
        start_date: int = None,
        types: str = None,
    ):
        self.app_id = app_id
        self.end_date = end_date
        self.start_date = start_date
        self.types = types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.types is not None:
            result['Types'] = self.types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Types') is not None:
            self.types = m.get('Types')
        return self


class DescribeUsageOverallDataResponseBodyUsageOverallDataNodes(TeaModel):
    def __init__(
        self,
        x: str = None,
        y: str = None,
    ):
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class DescribeUsageOverallDataResponseBodyUsageOverallData(TeaModel):
    def __init__(
        self,
        nodes: List[DescribeUsageOverallDataResponseBodyUsageOverallDataNodes] = None,
        type: str = None,
    ):
        self.nodes = nodes
        self.type = type

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = DescribeUsageOverallDataResponseBodyUsageOverallDataNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeUsageOverallDataResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        usage_overall_data: List[DescribeUsageOverallDataResponseBodyUsageOverallData] = None,
    ):
        self.request_id = request_id
        self.usage_overall_data = usage_overall_data

    def validate(self):
        if self.usage_overall_data:
            for k in self.usage_overall_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['UsageOverallData'] = []
        if self.usage_overall_data is not None:
            for k in self.usage_overall_data:
                result['UsageOverallData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.usage_overall_data = []
        if m.get('UsageOverallData') is not None:
            for k in m.get('UsageOverallData'):
                temp_model = DescribeUsageOverallDataResponseBodyUsageOverallData()
                self.usage_overall_data.append(temp_model.from_map(k))
        return self


class DescribeUsageOverallDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeUsageOverallDataResponseBody = None,
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
            temp_model = DescribeUsageOverallDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


