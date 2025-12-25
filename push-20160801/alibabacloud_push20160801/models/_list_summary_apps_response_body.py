# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_push20160801 import models as main_models
from darabonba.model import DaraModel

class ListSummaryAppsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        summary_app_infos: main_models.ListSummaryAppsResponseBodySummaryAppInfos = None,
    ):
        self.request_id = request_id
        self.summary_app_infos = summary_app_infos

    def validate(self):
        if self.summary_app_infos:
            self.summary_app_infos.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.summary_app_infos is not None:
            result['SummaryAppInfos'] = self.summary_app_infos.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SummaryAppInfos') is not None:
            temp_model = main_models.ListSummaryAppsResponseBodySummaryAppInfos()
            self.summary_app_infos = temp_model.from_map(m.get('SummaryAppInfos'))

        return self

class ListSummaryAppsResponseBodySummaryAppInfos(DaraModel):
    def __init__(
        self,
        summary_app_info: List[main_models.ListSummaryAppsResponseBodySummaryAppInfosSummaryAppInfo] = None,
    ):
        self.summary_app_info = summary_app_info

    def validate(self):
        if self.summary_app_info:
            for v1 in self.summary_app_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SummaryAppInfo'] = []
        if self.summary_app_info is not None:
            for k1 in self.summary_app_info:
                result['SummaryAppInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.summary_app_info = []
        if m.get('SummaryAppInfo') is not None:
            for k1 in m.get('SummaryAppInfo'):
                temp_model = main_models.ListSummaryAppsResponseBodySummaryAppInfosSummaryAppInfo()
                self.summary_app_info.append(temp_model.from_map(k1))

        return self

class ListSummaryAppsResponseBodySummaryAppInfosSummaryAppInfo(DaraModel):
    def __init__(
        self,
        app_key: int = None,
        app_name: str = None,
    ):
        self.app_key = app_key
        self.app_name = app_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_key is not None:
            result['AppKey'] = self.app_key

        if self.app_name is not None:
            result['AppName'] = self.app_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        return self

