# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class GetTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetTaskResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code. This parameter is returned when the request fails. A successful response may not contain this parameter.
        self.code = code
        # The task details.
        self.data = data
        # The error or result message. This parameter describes the cause when the request fails. A successful response may not contain this parameter.
        self.message = message
        # The unique identifier of the request. You can provide this value for troubleshooting.
        self.request_id = request_id
        # Indicates whether the request was processed successfully. A value of true indicates that the request was processed successfully. To check whether an asynchronous task is completed, you must query the task status separately.
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
            temp_model = main_models.GetTaskResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        ali_uid: int = None,
        current_task_message: str = None,
        current_task_step: str = None,
        execute_region: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        performance_type: str = None,
        progress: str = None,
        resource_list: List[main_models.GetTaskResponseBodyDataResourceList] = None,
        run_mode: str = None,
        status: str = None,
        system_disk_size: int = None,
        system_image_id: str = None,
        task_id: str = None,
        task_step_list: List[main_models.GetTaskResponseBodyDataTaskStepList] = None,
        task_type: str = None,
    ):
        # The ID of the Alibaba Cloud account to which the resource belongs.
        self.ali_uid = ali_uid
        # The prompt or execution result description of the current task step.
        self.current_task_message = current_task_message
        # The identifier of the step that the task is currently executing. You can call the ListTaskStep operation to query the image creation and application adaptation steps.
        self.current_task_step = current_task_step
        # The ID of the region where the task is actually executed.
        self.execute_region = execute_region
        # The time when the task was created. The time is in ISO 8601 format, accurate to milliseconds, and the time zone offset is +00:00.
        self.gmt_create = gmt_create
        # The time when the task was last updated. The time is in ISO 8601 format, accurate to milliseconds, and the time zone offset is +00:00.
        self.gmt_modified = gmt_modified
        # The compute type of the task creation resource.
        # 
        # Valid values:
        # - **CPU**: CPU compute resource.
        # - **GPU**: GPU compute resource.
        self.performance_type = performance_type
        # **Not enabled. The system does not return valid task progress.** Determine the task execution status based on Status, CurrentTaskStep, and TaskStepList.
        # 
        # The example "Not applicable (not enabled)" is only a description of the field status and is not an actual API response example.
        self.progress = progress
        # The list of resources used for task creation, which corresponds to the creation resources submitted when the task is created.
        self.resource_list = resource_list
        # The running mode of the task creation environment.
        # 
        # Valid values:
        # - **NORMAL**: Normal running mode.
        # - **COMPATIBLE**: Compatible running mode.
        self.run_mode = run_mode
        # The overall status of the task.
        # 
        # Valid values:
        # - **INIT**: The task is initialized.
        # - **START**: The task is being created or executed.
        # - **SUCCESS**: The task is executed successfully.
        # - **FAILED**: The task fails to be executed.
        # - **DELETED**: The task is deleted.
        # 
        # Deleted tasks are not included in the regular valid task query scope.
        self.status = status
        # The capacity of the system cloud disk in the task creation environment. Unit: GiB.
        self.system_disk_size = system_disk_size
        # The ID of the base system image used in the task creation environment.
        self.system_image_id = system_image_id
        # The task ID. You can use this ID to call the GetTask operation to query the task status.
        self.task_id = task_id
        # The list of recorded task execution steps and results.
        self.task_step_list = task_step_list
        # The actual type of the task.
        # 
        # Valid values:
        # - **AUTO_ADAPT**: Automatic adaptation.
        # - **AUTO_CREATE_IMAGE**: Automatic image creation.
        # - **RETRY_ADAPT**: Retry automatic adaptation.
        # - **RETRY_CREATE_IMAGE**: Retry automatic image creation.
        # - **AUTO_OTA_IMAGE**: Automatic image OTA.
        # - **AUTO_CREATE_VHD**: Automatic VHD creation.
        # - **RETRY_VHD**: Retry VHD creation.
        # - **AUTO_CREATE_IMAGE_VHD**: Automatic VHD image creation.
        # - **RETRY_CREATE_IMAGE_VHD**: Retry VHD image creation.
        # - **AUTO_VALIDATE_VHD**: Automatic VHD validation.
        # - **RETRY_VALIDATE_VHD**: Retry VHD validation.
        # - **SYNCHRONIZE_APP_IMAGE**: Synchronize application image.
        # - **APPLY_VHD_BUILDER**: Apply for VHD application recording environment.
        # - **RETRY_VHD_BUILDER**: Retry applying for VHD recording environment.
        # - **ADAPT_AUTO**: Automatic application adaptation creation.
        # - **ADAPT_AUTO_RETRY**: Retry automatic application adaptation creation.
        # - **ADAPT_MANUAL**: Manual application adaptation creation.
        # - **ADAPT_MANUAL_RETRY**: Retry manual application adaptation creation.
        # - **IMAGE_AUTO**: Automatic image creation.
        # - **IMAGE_AUTO_RETRY**: Retry automatic image creation.
        # - **IMAGE_AUTO_VALIDATE**: Automatic image validation.
        # - **IMAGE_AUTO_VALIDATE_RETRY**: Retry automatic image validation.
        # - **IMAGE_MANUAL**: Manual image creation.
        # - **IMAGE_MANUAL_RETRY**: Retry manual image creation.
        # - **DESKTOP_CUSTOM_IMAGE**: Create cloud desktop custom image.
        # - **DESKTOP_CUSTOM_IMAGE_RETRY**: Retry creating cloud desktop custom image.
        # - **DESKTOP_SYNC_IMAGE**: Synchronize cloud desktop image across regions.
        # - **DESKTOP_SYNC_IMAGE_RETRY**: Retry synchronizing cloud desktop image across regions.
        # - **IMAGE_DISTRIBUTE**: Distribute image to multiple regions.
        # - **IMAGE_DISTRIBUTE_RETRY**: Retry image distribution.
        # - **IMAGE_FROM_INSTANCE**: Create image based on instance.
        # - **IMAGE_FROM_INSTANCE_RETRY**: Retry creating image based on instance.
        # - **SNAPSHOT_DISTRIBUTE**: Distribute snapshot to multiple regions.
        # - **SNAPSHOT_DISTRIBUTE_RETRY**: Retry snapshot distribution.
        # - **SNAPSHOT_FROM_DISK**: Create snapshot based on disk.
        # - **SNAPSHOT_FROM_DISK_RETRY**: Retry creating snapshot based on disk.
        # - **IMAGE_CLEAN_AND_CREATE**: Create temporary instance based on image, clean it, and create final image.
        # - **IMAGE_CLEAN_AND_CREATE_RETRY**: Retry creating final image after cleaning.
        self.task_type = task_type

    def validate(self):
        if self.resource_list:
            for v1 in self.resource_list:
                 if v1:
                    v1.validate()
        if self.task_step_list:
            for v1 in self.task_step_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.current_task_message is not None:
            result['CurrentTaskMessage'] = self.current_task_message

        if self.current_task_step is not None:
            result['CurrentTaskStep'] = self.current_task_step

        if self.execute_region is not None:
            result['ExecuteRegion'] = self.execute_region

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.performance_type is not None:
            result['PerformanceType'] = self.performance_type

        if self.progress is not None:
            result['Progress'] = self.progress

        result['ResourceList'] = []
        if self.resource_list is not None:
            for k1 in self.resource_list:
                result['ResourceList'].append(k1.to_map() if k1 else None)

        if self.run_mode is not None:
            result['RunMode'] = self.run_mode

        if self.status is not None:
            result['Status'] = self.status

        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size

        if self.system_image_id is not None:
            result['SystemImageId'] = self.system_image_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        result['TaskStepList'] = []
        if self.task_step_list is not None:
            for k1 in self.task_step_list:
                result['TaskStepList'].append(k1.to_map() if k1 else None)

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('CurrentTaskMessage') is not None:
            self.current_task_message = m.get('CurrentTaskMessage')

        if m.get('CurrentTaskStep') is not None:
            self.current_task_step = m.get('CurrentTaskStep')

        if m.get('ExecuteRegion') is not None:
            self.execute_region = m.get('ExecuteRegion')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('PerformanceType') is not None:
            self.performance_type = m.get('PerformanceType')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        self.resource_list = []
        if m.get('ResourceList') is not None:
            for k1 in m.get('ResourceList'):
                temp_model = main_models.GetTaskResponseBodyDataResourceList()
                self.resource_list.append(temp_model.from_map(k1))

        if m.get('RunMode') is not None:
            self.run_mode = m.get('RunMode')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')

        if m.get('SystemImageId') is not None:
            self.system_image_id = m.get('SystemImageId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        self.task_step_list = []
        if m.get('TaskStepList') is not None:
            for k1 in m.get('TaskStepList'):
                temp_model = main_models.GetTaskResponseBodyDataTaskStepList()
                self.task_step_list.append(temp_model.from_map(k1))

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

class GetTaskResponseBodyDataTaskStepList(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        start_time: int = None,
        status: str = None,
        step_end_time: str = None,
        step_start_time: str = None,
        task_message: str = None,
        task_step: str = None,
    ):
        # The end time of the step. It is a UNIX timestamp calculated from 1970-01-01T00:00:00Z. Unit: milliseconds. This parameter may not be returned if the step has not ended.
        self.end_time = end_time
        # The start time of the step. It is a UNIX timestamp calculated from 1970-01-01T00:00:00Z. Unit: milliseconds.
        self.start_time = start_time
        # The execution status of the step.
        # 
        # Valid values:
        # - **RUNNING**: The step is executing.
        # - **SUCCESS**: The step is executed successfully.
        # - **FAILED**: The step fails to be executed.
        self.status = status
        # The end time of the step in ISO 8601 format, including the time zone offset. In the example, +08:00 indicates UTC+8. This parameter represents the same time as EndTime and is parsed based on the offset in the return value. This parameter may not be returned if the step has not ended.
        self.step_end_time = step_end_time
        # The start time of the step in ISO 8601 format, including the time zone offset. In the example, +08:00 indicates UTC+8. This parameter represents the same time as StartTime and is parsed based on the offset in the return value.
        self.step_start_time = step_start_time
        # The prompt or execution result description of this step.
        self.task_message = task_message
        # The task step identifier corresponding to this record. You can call the ListTaskStep operation to query the image creation and application adaptation steps.
        self.task_step = task_step

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.step_end_time is not None:
            result['StepEndTime'] = self.step_end_time

        if self.step_start_time is not None:
            result['StepStartTime'] = self.step_start_time

        if self.task_message is not None:
            result['TaskMessage'] = self.task_message

        if self.task_step is not None:
            result['TaskStep'] = self.task_step

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StepEndTime') is not None:
            self.step_end_time = m.get('StepEndTime')

        if m.get('StepStartTime') is not None:
            self.step_start_time = m.get('StepStartTime')

        if m.get('TaskMessage') is not None:
            self.task_message = m.get('TaskMessage')

        if m.get('TaskStep') is not None:
            self.task_step = m.get('TaskStep')

        return self

class GetTaskResponseBodyDataResourceList(DaraModel):
    def __init__(
        self,
        resource: str = None,
        resource_type: str = None,
    ):
        # The resource content corresponding to ResourceType. For the URL type, specify or return an accessible resource address.
        self.resource = resource
        # The provision method of the resource content.
        # 
        # Valid values:
        # - **HOSTED**: Hosted resource.
        # - **TEXT**: Text resource.
        # - **URL**: Resource provided through a URL.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource is not None:
            result['Resource'] = self.resource

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

