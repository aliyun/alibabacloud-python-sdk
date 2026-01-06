# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class QueryLiveWatchUserListResponseBody(DaraModel):
    def __init__(
        self,
        org_uses_list: List[main_models.QueryLiveWatchUserListResponseBodyOrgUsesList] = None,
        out_org_user_list: List[main_models.QueryLiveWatchUserListResponseBodyOutOrgUserList] = None,
        request_id: str = None,
    ):
        self.org_uses_list = org_uses_list
        self.out_org_user_list = out_org_user_list
        # requestId
        self.request_id = request_id

    def validate(self):
        if self.org_uses_list:
            for v1 in self.org_uses_list:
                 if v1:
                    v1.validate()
        if self.out_org_user_list:
            for v1 in self.out_org_user_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['orgUsesList'] = []
        if self.org_uses_list is not None:
            for k1 in self.org_uses_list:
                result['orgUsesList'].append(k1.to_map() if k1 else None)

        result['outOrgUserList'] = []
        if self.out_org_user_list is not None:
            for k1 in self.out_org_user_list:
                result['outOrgUserList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.org_uses_list = []
        if m.get('orgUsesList') is not None:
            for k1 in m.get('orgUsesList'):
                temp_model = main_models.QueryLiveWatchUserListResponseBodyOrgUsesList()
                self.org_uses_list.append(temp_model.from_map(k1))

        self.out_org_user_list = []
        if m.get('outOrgUserList') is not None:
            for k1 in m.get('outOrgUserList'):
                temp_model = main_models.QueryLiveWatchUserListResponseBodyOutOrgUserList()
                self.out_org_user_list.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class QueryLiveWatchUserListResponseBodyOutOrgUserList(DaraModel):
    def __init__(
        self,
        name: str = None,
        watch_live_time: int = None,
        watch_playback_time: int = None,
        watch_progress_ms: int = None,
    ):
        self.name = name
        self.watch_live_time = watch_live_time
        self.watch_playback_time = watch_playback_time
        self.watch_progress_ms = watch_progress_ms

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.watch_live_time is not None:
            result['WatchLiveTime'] = self.watch_live_time

        if self.watch_playback_time is not None:
            result['WatchPlaybackTime'] = self.watch_playback_time

        if self.watch_progress_ms is not None:
            result['WatchProgressMs'] = self.watch_progress_ms

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('WatchLiveTime') is not None:
            self.watch_live_time = m.get('WatchLiveTime')

        if m.get('WatchPlaybackTime') is not None:
            self.watch_playback_time = m.get('WatchPlaybackTime')

        if m.get('WatchProgressMs') is not None:
            self.watch_progress_ms = m.get('WatchProgressMs')

        return self

class QueryLiveWatchUserListResponseBodyOrgUsesList(DaraModel):
    def __init__(
        self,
        dept_name: str = None,
        name: str = None,
        user_id: str = None,
        watch_live_time: int = None,
        watch_playback_time: int = None,
        watch_progress_ms: int = None,
    ):
        self.dept_name = dept_name
        self.name = name
        self.user_id = user_id
        self.watch_live_time = watch_live_time
        self.watch_playback_time = watch_playback_time
        self.watch_progress_ms = watch_progress_ms

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dept_name is not None:
            result['DeptName'] = self.dept_name

        if self.name is not None:
            result['Name'] = self.name

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.watch_live_time is not None:
            result['WatchLiveTime'] = self.watch_live_time

        if self.watch_playback_time is not None:
            result['WatchPlaybackTime'] = self.watch_playback_time

        if self.watch_progress_ms is not None:
            result['WatchProgressMs'] = self.watch_progress_ms

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeptName') is not None:
            self.dept_name = m.get('DeptName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('WatchLiveTime') is not None:
            self.watch_live_time = m.get('WatchLiveTime')

        if m.get('WatchPlaybackTime') is not None:
            self.watch_playback_time = m.get('WatchPlaybackTime')

        if m.get('WatchProgressMs') is not None:
            self.watch_progress_ms = m.get('WatchProgressMs')

        return self

