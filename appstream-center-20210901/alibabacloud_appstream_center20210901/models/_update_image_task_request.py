# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateImageTaskRequest(DaraModel):
    def __init__(
        self,
        biz_region_id: str = None,
        code: str = None,
        status: str = None,
        task_id: str = None,
        task_step: str = None,
        task_type: str = None,
        version_id: str = None,
    ):
        # **Not enabled. Do not pass this parameter.** The task region is determined by the associated creation resource. This parameter is not used to switch regions.
        # 
        # The example "Not applicable (not enabled)" is only a description of the field status and is not a valid parameter value.
        self.biz_region_id = biz_region_id
        # **Not enabled. Do not pass this parameter.** This parameter is not involved in task status updates.
        # 
        # The example "Not applicable (not enabled)" is only a description of the field status and is not a valid parameter value.
        self.code = code
        # The status identifier reported by the creation resource. It must match the task type and the current creation stage. Do not directly use the overall task status returned by GetTask as a substitute.
        # 
        # Valid values for image creation tasks (IMAGE_MANUAL and IMAGE_MANUAL_RETRY):
        # 
        # - **BUILDER_INIT_SUCCESS**: The creation environment is successfully initialized.
        # - **DOWNLOAD_SUCCESS**: The creation resource is successfully downloaded.
        # - **DOWNLOAD_FAILED**: The creation resource fails to be downloaded.
        # - **BUILD_START**: The image creation starts.
        # - **BUILD_SUCCESS**: The application installation and image configuration are successful.
        # - **BUILD_FAILED**: The application installation or image configuration fails.
        # - **BUILD_COMPLETE**: The creation is completed and the subsequent verification process starts.
        # - **BUILD_COMPLETE_SKIP_VALIDATE**: The creation is completed in a compatible state. Whether verification is performed is subject to the task query result.
        # 
        # Valid values for application adaptation tasks:
        # 
        # - **BUILDER_INIT_SUCCESS**: The creation environment is successfully initialized.
        # - **DOWNLOAD_SUCCESS**: The application resource is successfully downloaded.
        # - **DOWNLOAD_FAILED**: The application resource fails to be downloaded.
        # - **BUILD_START**: The application recording starts.
        # - **BUILD_SUCCESS**: The application recording is successful.
        # - **BUILD_FAILED**: The application recording fails.
        # - **NAS_DISPATCH_SUCCESS**: The application files are successfully distributed to NAS.
        # - **NAS_DISPATCH_FAILED**: The application files fail to be distributed to NAS.
        # - **OSS_UPLOAD_SUCCESS**: The application files are successfully uploaded to OSS.
        # - **OSS_UPLOAD_FAILED**: The application files fail to be uploaded to OSS.
        # - **UPLOAD_SUCCESS**: The application files are successfully uploaded.
        # - **UPLOAD_FAILED**: The application files fail to be uploaded.
        # - **BUILD_COMPLETE**: The application creation is completed.
        self.status = status
        # The ID of the task to be updated. The task and its creation resource must already exist.
        # 
        # This parameter is required.
        self.task_id = task_id
        # **Not enabled. Do not pass this parameter.** This parameter does not support updating the task step.
        # 
        # The example "Not applicable (not enabled)" is only a description of the field status and is not a valid parameter value.
        self.task_step = task_step
        # The actual type of the task to be updated, which must match the task specified by TaskId. Status updates support the following application adaptation and manual image creation tasks:
        # 
        # - **ADAPT_AUTO**: Automatic application adaptation creation.
        # - **ADAPT_AUTO_RETRY**: Retry for automatic application adaptation creation.
        # - **ADAPT_MANUAL**: Manual application adaptation creation.
        # - **ADAPT_MANUAL_RETRY**: Retry for manual application adaptation creation.
        # - **IMAGE_MANUAL**: Manual image creation.
        # - **IMAGE_MANUAL_RETRY**: Retry for manual image creation.
        # 
        # This parameter is required.
        self.task_type = task_type
        # **Not enabled. Do not pass this parameter.** This parameter does not support modifying the image version associated with the task.
        # 
        # The example "Not applicable (not enabled)" is only a description of the field status and is not a valid parameter value.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

        if self.code is not None:
            result['Code'] = self.code

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_step is not None:
            result['TaskStep'] = self.task_step

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskStep') is not None:
            self.task_step = m.get('TaskStep')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        return self

