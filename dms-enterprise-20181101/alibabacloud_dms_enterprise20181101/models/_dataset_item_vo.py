# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class DatasetItemVO(DaraModel):
    def __init__(
        self,
        async_task_list: List[main_models.AsyncTaskVO] = None,
        dataset_status: int = None,
        dataset_type: int = None,
        digest: str = None,
        file_system: str = None,
        id: str = None,
        key_name: str = None,
        more_info: str = None,
        path: str = None,
        projects_linked: List[main_models.ProjectDetailsLiteVO] = None,
        recent_task_status: int = None,
        remark: str = None,
        schema: str = None,
        table_name: str = None,
        url: str = None,
    ):
        self.async_task_list = async_task_list
        self.dataset_status = dataset_status
        self.dataset_type = dataset_type
        self.digest = digest
        self.file_system = file_system
        self.id = id
        self.key_name = key_name
        self.more_info = more_info
        self.path = path
        self.projects_linked = projects_linked
        self.recent_task_status = recent_task_status
        self.remark = remark
        self.schema = schema
        self.table_name = table_name
        self.url = url

    def validate(self):
        if self.async_task_list:
            for v1 in self.async_task_list:
                 if v1:
                    v1.validate()
        if self.projects_linked:
            for v1 in self.projects_linked:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AsyncTaskList'] = []
        if self.async_task_list is not None:
            for k1 in self.async_task_list:
                result['AsyncTaskList'].append(k1.to_map() if k1 else None)

        if self.dataset_status is not None:
            result['DatasetStatus'] = self.dataset_status

        if self.dataset_type is not None:
            result['DatasetType'] = self.dataset_type

        if self.digest is not None:
            result['Digest'] = self.digest

        if self.file_system is not None:
            result['FileSystem'] = self.file_system

        if self.id is not None:
            result['Id'] = self.id

        if self.key_name is not None:
            result['KeyName'] = self.key_name

        if self.more_info is not None:
            result['MoreInfo'] = self.more_info

        if self.path is not None:
            result['Path'] = self.path

        result['ProjectsLinked'] = []
        if self.projects_linked is not None:
            for k1 in self.projects_linked:
                result['ProjectsLinked'].append(k1.to_map() if k1 else None)

        if self.recent_task_status is not None:
            result['RecentTaskStatus'] = self.recent_task_status

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.schema is not None:
            result['Schema'] = self.schema

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.async_task_list = []
        if m.get('AsyncTaskList') is not None:
            for k1 in m.get('AsyncTaskList'):
                temp_model = main_models.AsyncTaskVO()
                self.async_task_list.append(temp_model.from_map(k1))

        if m.get('DatasetStatus') is not None:
            self.dataset_status = m.get('DatasetStatus')

        if m.get('DatasetType') is not None:
            self.dataset_type = m.get('DatasetType')

        if m.get('Digest') is not None:
            self.digest = m.get('Digest')

        if m.get('FileSystem') is not None:
            self.file_system = m.get('FileSystem')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('KeyName') is not None:
            self.key_name = m.get('KeyName')

        if m.get('MoreInfo') is not None:
            self.more_info = m.get('MoreInfo')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        self.projects_linked = []
        if m.get('ProjectsLinked') is not None:
            for k1 in m.get('ProjectsLinked'):
                temp_model = main_models.ProjectDetailsLiteVO()
                self.projects_linked.append(temp_model.from_map(k1))

        if m.get('RecentTaskStatus') is not None:
            self.recent_task_status = m.get('RecentTaskStatus')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('Schema') is not None:
            self.schema = m.get('Schema')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

