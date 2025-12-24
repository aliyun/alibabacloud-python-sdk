# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_schedulerx320240624 import models as main_models
from darabonba.model import DaraModel

class GetAppResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetAppResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        # -
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

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
            temp_model = main_models.GetAppResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetAppResponseBodyData(DaraModel):
    def __init__(
        self,
        access_token: str = None,
        app_name: str = None,
        app_type: int = None,
        creator: str = None,
        enable_log: bool = None,
        executor_num: int = None,
        id: int = None,
        job_num: int = None,
        label_route_strategy: int = None,
        leader: str = None,
        max_concurrency: int = None,
        max_jobs: int = None,
        title: str = None,
        updater: str = None,
    ):
        # AccessToken。
        self.access_token = access_token
        self.app_name = app_name
        self.app_type = app_type
        self.creator = creator
        self.enable_log = enable_log
        self.executor_num = executor_num
        self.id = id
        self.job_num = job_num
        self.label_route_strategy = label_route_strategy
        self.leader = leader
        self.max_concurrency = max_concurrency
        self.max_jobs = max_jobs
        self.title = title
        self.updater = updater

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_token is not None:
            result['AccessToken'] = self.access_token

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.enable_log is not None:
            result['EnableLog'] = self.enable_log

        if self.executor_num is not None:
            result['ExecutorNum'] = self.executor_num

        if self.id is not None:
            result['Id'] = self.id

        if self.job_num is not None:
            result['JobNum'] = self.job_num

        if self.label_route_strategy is not None:
            result['LabelRouteStrategy'] = self.label_route_strategy

        if self.leader is not None:
            result['Leader'] = self.leader

        if self.max_concurrency is not None:
            result['MaxConcurrency'] = self.max_concurrency

        if self.max_jobs is not None:
            result['MaxJobs'] = self.max_jobs

        if self.title is not None:
            result['Title'] = self.title

        if self.updater is not None:
            result['Updater'] = self.updater

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('EnableLog') is not None:
            self.enable_log = m.get('EnableLog')

        if m.get('ExecutorNum') is not None:
            self.executor_num = m.get('ExecutorNum')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('JobNum') is not None:
            self.job_num = m.get('JobNum')

        if m.get('LabelRouteStrategy') is not None:
            self.label_route_strategy = m.get('LabelRouteStrategy')

        if m.get('Leader') is not None:
            self.leader = m.get('Leader')

        if m.get('MaxConcurrency') is not None:
            self.max_concurrency = m.get('MaxConcurrency')

        if m.get('MaxJobs') is not None:
            self.max_jobs = m.get('MaxJobs')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Updater') is not None:
            self.updater = m.get('Updater')

        return self

