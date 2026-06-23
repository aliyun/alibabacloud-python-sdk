# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import BinaryIO

from darabonba.model import DaraModel

class CreateResourceFileAdvanceRequest(DaraModel):
    def __init__(
        self,
        content: str = None,
        file_description: str = None,
        file_folder_path: str = None,
        file_name: str = None,
        file_type: int = None,
        origin_resource_name: str = None,
        owner: str = None,
        project_id: int = None,
        register_to_calc_engine: bool = None,
        resource_file_object: BinaryIO = None,
        storage_url: str = None,
        upload_mode: bool = None,
    ):
        # The code content of the file. The code format varies depending on the code type (fileType). You can locate a job of the corresponding type in the Operation Center, right-click it, and select View Code to check the specific code format.
        self.content = content
        # The description of the file.
        self.file_description = file_description
        # The path of the file.
        # 
        # This parameter is required.
        self.file_folder_path = file_folder_path
        # The name of the file.
        # 
        # This parameter is required.
        self.file_name = file_name
        # The code type of the file.
        # 
        # Different file types correspond to different code types. For more information, see [DataWorks Node Types](https://help.aliyun.com/document_detail/600169.html).<br>
        # You can also invoke the [ListFileType](https://help.aliyun.com/document_detail/212428.html) API to query the code types of files.
        # 
        # This parameter is required.
        self.file_type = file_type
        # The name of the original resource file.
        # 
        # This parameter is required.
        self.origin_resource_name = origin_resource_name
        # The Alibaba Cloud User ID of the file owner. If this parameter is empty, the Alibaba Cloud User ID of the caller is used by default.
        self.owner = owner
        # The ID of the DataWorks workspace. You can log on to the DataWorks console, go to the workspace configuration page, and obtain the workspace ID. This parameter is required to identify the DataWorks workspace for this API call.
        # 
        # This parameter is required.
        self.project_id = project_id
        # Indicates whether to synchronize and upload the resource to the compute engine.
        # 
        # This parameter is required.
        self.register_to_calc_engine = register_to_calc_engine
        # The OSS URL for file upload provided by POP.
        self.resource_file_object = resource_file_object
        # The Storage Path of the resource file on the compute engine. This field is currently used only by EMR and CDH. The EMR format is [osshdfs]://path/to/object, and for CDH, the default value must be /user/admin/lib.
        self.storage_url = storage_url
        # The upload mode for the resource file. This parameter currently applies only to File-type files in MaxCompute. Valid values:
        # 
        # - true: Downloadable resource mode.
        # 
        # - false: Online-editable text mode.
        self.upload_mode = upload_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.file_description is not None:
            result['FileDescription'] = self.file_description

        if self.file_folder_path is not None:
            result['FileFolderPath'] = self.file_folder_path

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_type is not None:
            result['FileType'] = self.file_type

        if self.origin_resource_name is not None:
            result['OriginResourceName'] = self.origin_resource_name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.register_to_calc_engine is not None:
            result['RegisterToCalcEngine'] = self.register_to_calc_engine

        if self.resource_file_object is not None:
            result['ResourceFile'] = self.resource_file_object

        if self.storage_url is not None:
            result['StorageURL'] = self.storage_url

        if self.upload_mode is not None:
            result['UploadMode'] = self.upload_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('FileDescription') is not None:
            self.file_description = m.get('FileDescription')

        if m.get('FileFolderPath') is not None:
            self.file_folder_path = m.get('FileFolderPath')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')

        if m.get('OriginResourceName') is not None:
            self.origin_resource_name = m.get('OriginResourceName')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RegisterToCalcEngine') is not None:
            self.register_to_calc_engine = m.get('RegisterToCalcEngine')

        if m.get('ResourceFile') is not None:
            self.resource_file_object = m.get('ResourceFile')

        if m.get('StorageURL') is not None:
            self.storage_url = m.get('StorageURL')

        if m.get('UploadMode') is not None:
            self.upload_mode = m.get('UploadMode')

        return self

