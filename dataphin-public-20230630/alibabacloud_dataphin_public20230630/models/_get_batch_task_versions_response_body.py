# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetBatchTaskVersionsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetBatchTaskVersionsResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

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
            temp_model = main_models.GetBatchTaskVersionsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetBatchTaskVersionsResponseBodyData(DaraModel):
    def __init__(
        self,
        batch_task_version_list: List[main_models.GetBatchTaskVersionsResponseBodyDataBatchTaskVersionList] = None,
    ):
        self.batch_task_version_list = batch_task_version_list

    def validate(self):
        if self.batch_task_version_list:
            for v1 in self.batch_task_version_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BatchTaskVersionList'] = []
        if self.batch_task_version_list is not None:
            for k1 in self.batch_task_version_list:
                result['BatchTaskVersionList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.batch_task_version_list = []
        if m.get('BatchTaskVersionList') is not None:
            for k1 in m.get('BatchTaskVersionList'):
                temp_model = main_models.GetBatchTaskVersionsResponseBodyDataBatchTaskVersionList()
                self.batch_task_version_list.append(temp_model.from_map(k1))

        return self

class GetBatchTaskVersionsResponseBodyDataBatchTaskVersionList(DaraModel):
    def __init__(
        self,
        comment: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        node_id: str = None,
        project_id: int = None,
        published: bool = None,
        user_id: str = None,
        user_name: str = None,
        version: str = None,
    ):
        self.comment = comment
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.node_id = node_id
        self.project_id = project_id
        self.published = published
        self.user_id = user_id
        self.user_name = user_name
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.published is not None:
            result['Published'] = self.published

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_name is not None:
            result['UserName'] = self.user_name

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Published') is not None:
            self.published = m.get('Published')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

