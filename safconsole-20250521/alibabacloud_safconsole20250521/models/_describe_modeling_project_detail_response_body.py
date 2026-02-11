# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_safconsole20250521 import models as main_models
from darabonba.model import DaraModel

class DescribeModelingProjectDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        request_id: str = None,
        result_object: main_models.DescribeModelingProjectDetailResponseBodyResultObject = None,
        success: bool = None,
    ):
        # Status code. A return value of 200 indicates success.
        self.code = code
        # Request ID.
        self.request_id = request_id
        # Returned result.
        self.result_object = result_object
        # Whether the call was successful.
        # 
        # - **true**: Call succeeded.
        # - **false**: Call failed.
        self.success = success

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultObject') is not None:
            temp_model = main_models.DescribeModelingProjectDetailResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('ResultObject'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeModelingProjectDetailResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        env_status: str = None,
        login_account: str = None,
        machine_spec: str = None,
        manual_phase: str = None,
        modeling_status: str = None,
        poc_tasks: List[main_models.DescribeModelingProjectDetailResponseBodyResultObjectPocTasks] = None,
        project_id: str = None,
        project_name: str = None,
        remark: str = None,
        start_time: int = None,
        synced_files: List[main_models.DescribeModelingProjectDetailResponseBodyResultObjectSyncedFiles] = None,
    ):
        # End time of the security modeling project.
        self.end_time = end_time
        # Security environment status.
        self.env_status = env_status
        # Login account.
        self.login_account = login_account
        # Machine specification.
        self.machine_spec = machine_spec
        # Manual operation phase.
        self.manual_phase = manual_phase
        # Modeling project status.
        self.modeling_status = modeling_status
        # Associated POC tasks.
        self.poc_tasks = poc_tasks
        # Project ID
        self.project_id = project_id
        # Project name.
        self.project_name = project_name
        # Remark information.
        self.remark = remark
        # Start time of the security modeling project.
        self.start_time = start_time
        # Synchronized files.
        self.synced_files = synced_files

    def validate(self):
        if self.poc_tasks:
            for v1 in self.poc_tasks:
                 if v1:
                    v1.validate()
        if self.synced_files:
            for v1 in self.synced_files:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.env_status is not None:
            result['EnvStatus'] = self.env_status

        if self.login_account is not None:
            result['LoginAccount'] = self.login_account

        if self.machine_spec is not None:
            result['MachineSpec'] = self.machine_spec

        if self.manual_phase is not None:
            result['ManualPhase'] = self.manual_phase

        if self.modeling_status is not None:
            result['ModelingStatus'] = self.modeling_status

        result['PocTasks'] = []
        if self.poc_tasks is not None:
            for k1 in self.poc_tasks:
                result['PocTasks'].append(k1.to_map() if k1 else None)

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        result['SyncedFiles'] = []
        if self.synced_files is not None:
            for k1 in self.synced_files:
                result['SyncedFiles'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EnvStatus') is not None:
            self.env_status = m.get('EnvStatus')

        if m.get('LoginAccount') is not None:
            self.login_account = m.get('LoginAccount')

        if m.get('MachineSpec') is not None:
            self.machine_spec = m.get('MachineSpec')

        if m.get('ManualPhase') is not None:
            self.manual_phase = m.get('ManualPhase')

        if m.get('ModelingStatus') is not None:
            self.modeling_status = m.get('ModelingStatus')

        self.poc_tasks = []
        if m.get('PocTasks') is not None:
            for k1 in m.get('PocTasks'):
                temp_model = main_models.DescribeModelingProjectDetailResponseBodyResultObjectPocTasks()
                self.poc_tasks.append(temp_model.from_map(k1))

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        self.synced_files = []
        if m.get('SyncedFiles') is not None:
            for k1 in m.get('SyncedFiles'):
                temp_model = main_models.DescribeModelingProjectDetailResponseBodyResultObjectSyncedFiles()
                self.synced_files.append(temp_model.from_map(k1))

        return self

class DescribeModelingProjectDetailResponseBodyResultObjectSyncedFiles(DaraModel):
    def __init__(
        self,
        deployable: bool = None,
        files: List[main_models.DescribeModelingProjectDetailResponseBodyResultObjectSyncedFilesFiles] = None,
        group_id: int = None,
        group_name: str = None,
        synced_time: str = None,
    ):
        # Whether deployment is supported.
        self.deployable = deployable
        # Files generated by modeling.
        self.files = files
        # Application group ID.
        self.group_id = group_id
        # File group name.
        self.group_name = group_name
        # Synchronization time.
        self.synced_time = synced_time

    def validate(self):
        if self.files:
            for v1 in self.files:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deployable is not None:
            result['Deployable'] = self.deployable

        result['Files'] = []
        if self.files is not None:
            for k1 in self.files:
                result['Files'].append(k1.to_map() if k1 else None)

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.synced_time is not None:
            result['SyncedTime'] = self.synced_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Deployable') is not None:
            self.deployable = m.get('Deployable')

        self.files = []
        if m.get('Files') is not None:
            for k1 in m.get('Files'):
                temp_model = main_models.DescribeModelingProjectDetailResponseBodyResultObjectSyncedFilesFiles()
                self.files.append(temp_model.from_map(k1))

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('SyncedTime') is not None:
            self.synced_time = m.get('SyncedTime')

        return self

class DescribeModelingProjectDetailResponseBodyResultObjectSyncedFilesFiles(DaraModel):
    def __init__(
        self,
        downloadable: bool = None,
        file_id: int = None,
        file_name: str = None,
        visible: bool = None,
    ):
        # Whether it is downloadable.
        self.downloadable = downloadable
        # The ID of the file.
        self.file_id = file_id
        # The name of the file.
        self.file_name = file_name
        # Visibility:
        # 
        # **true**: Visible
        # 
        # **false**: Not visible
        self.visible = visible

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.downloadable is not None:
            result['Downloadable'] = self.downloadable

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.visible is not None:
            result['Visible'] = self.visible

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Downloadable') is not None:
            self.downloadable = m.get('Downloadable')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('Visible') is not None:
            self.visible = m.get('Visible')

        return self

class DescribeModelingProjectDetailResponseBodyResultObjectPocTasks(DaraModel):
    def __init__(
        self,
        file_name: str = None,
        service_code: str = None,
        status: str = None,
        task_name: str = None,
    ):
        # Retrospective file name.
        self.file_name = file_name
        # Service code
        self.service_code = service_code
        # File synchronization status.
        self.status = status
        # Retrospective task name.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.service_code is not None:
            result['ServiceCode'] = self.service_code

        if self.status is not None:
            result['Status'] = self.status

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        return self

