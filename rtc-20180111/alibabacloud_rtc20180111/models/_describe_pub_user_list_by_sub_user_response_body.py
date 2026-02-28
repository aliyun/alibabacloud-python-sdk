# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class DescribePubUserListBySubUserResponseBody(DaraModel):
    def __init__(
        self,
        call_status: str = None,
        pub_user_detail_list: List[main_models.DescribePubUserListBySubUserResponseBodyPubUserDetailList] = None,
        request_id: str = None,
        sub_user_detail: main_models.DescribePubUserListBySubUserResponseBodySubUserDetail = None,
    ):
        self.call_status = call_status
        self.pub_user_detail_list = pub_user_detail_list
        self.request_id = request_id
        self.sub_user_detail = sub_user_detail

    def validate(self):
        if self.pub_user_detail_list:
            for v1 in self.pub_user_detail_list:
                 if v1:
                    v1.validate()
        if self.sub_user_detail:
            self.sub_user_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_status is not None:
            result['CallStatus'] = self.call_status

        result['PubUserDetailList'] = []
        if self.pub_user_detail_list is not None:
            for k1 in self.pub_user_detail_list:
                result['PubUserDetailList'].append(k1.to_map() if k1 else None)

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
            for k1 in m.get('PubUserDetailList'):
                temp_model = main_models.DescribePubUserListBySubUserResponseBodyPubUserDetailList()
                self.pub_user_detail_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SubUserDetail') is not None:
            temp_model = main_models.DescribePubUserListBySubUserResponseBodySubUserDetail()
            self.sub_user_detail = temp_model.from_map(m.get('SubUserDetail'))

        return self

class DescribePubUserListBySubUserResponseBodySubUserDetail(DaraModel):
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
        online_periods: List[main_models.DescribePubUserListBySubUserResponseBodySubUserDetailOnlinePeriods] = None,
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
            for v1 in self.online_periods:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
            for k1 in m.get('OnlinePeriods'):
                temp_model = main_models.DescribePubUserListBySubUserResponseBodySubUserDetailOnlinePeriods()
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

        if m.get('UserIdAlias') is not None:
            self.user_id_alias = m.get('UserIdAlias')

        return self

class DescribePubUserListBySubUserResponseBodySubUserDetailOnlinePeriods(DaraModel):
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

class DescribePubUserListBySubUserResponseBodyPubUserDetailList(DaraModel):
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
        online_periods: List[main_models.DescribePubUserListBySubUserResponseBodyPubUserDetailListOnlinePeriods] = None,
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
            for v1 in self.online_periods:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
            for k1 in m.get('OnlinePeriods'):
                temp_model = main_models.DescribePubUserListBySubUserResponseBodyPubUserDetailListOnlinePeriods()
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

        if m.get('UserIdAlias') is not None:
            self.user_id_alias = m.get('UserIdAlias')

        return self

class DescribePubUserListBySubUserResponseBodyPubUserDetailListOnlinePeriods(DaraModel):
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

