# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class DescribeCallResponseBody(DaraModel):
    def __init__(
        self,
        call_info: main_models.DescribeCallResponseBodyCallInfo = None,
        request_id: str = None,
        user_detail_list: List[main_models.DescribeCallResponseBodyUserDetailList] = None,
    ):
        self.call_info = call_info
        self.request_id = request_id
        self.user_detail_list = user_detail_list

    def validate(self):
        if self.call_info:
            self.call_info.validate()
        if self.user_detail_list:
            for v1 in self.user_detail_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_info is not None:
            result['CallInfo'] = self.call_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['UserDetailList'] = []
        if self.user_detail_list is not None:
            for k1 in self.user_detail_list:
                result['UserDetailList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallInfo') is not None:
            temp_model = main_models.DescribeCallResponseBodyCallInfo()
            self.call_info = temp_model.from_map(m.get('CallInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.user_detail_list = []
        if m.get('UserDetailList') is not None:
            for k1 in m.get('UserDetailList'):
                temp_model = main_models.DescribeCallResponseBodyUserDetailList()
                self.user_detail_list.append(temp_model.from_map(k1))

        return self

class DescribeCallResponseBodyUserDetailList(DaraModel):
    def __init__(
        self,
        call_exp: str = None,
        created_ts: int = None,
        destroyed_ts: int = None,
        dur_metric_stat_data: main_models.DescribeCallResponseBodyUserDetailListDurMetricStatData = None,
        duration: int = None,
        location: str = None,
        network: str = None,
        network_list: List[str] = None,
        online_duration: int = None,
        online_periods: List[main_models.DescribeCallResponseBodyUserDetailListOnlinePeriods] = None,
        os: str = None,
        os_list: List[str] = None,
        roles: List[str] = None,
        sdk_version: str = None,
        sdk_version_list: List[str] = None,
        user_id: str = None,
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

    def validate(self):
        if self.dur_metric_stat_data:
            self.dur_metric_stat_data.validate()
        if self.online_periods:
            for v1 in self.online_periods:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
            for k1 in self.online_periods:
                result['OnlinePeriods'].append(k1.to_map() if k1 else None)

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
            temp_model = main_models.DescribeCallResponseBodyUserDetailListDurMetricStatData()
            self.dur_metric_stat_data = temp_model.from_map(m.get('DurMetricStatData'))

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
            for k1 in m.get('OnlinePeriods'):
                temp_model = main_models.DescribeCallResponseBodyUserDetailListOnlinePeriods()
                self.online_periods.append(temp_model.from_map(k1))

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

        return self

class DescribeCallResponseBodyUserDetailListOnlinePeriods(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class DescribeCallResponseBodyUserDetailListDurMetricStatData(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class DescribeCallResponseBodyCallInfo(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

