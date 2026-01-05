# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateResourceFileRequest(DaraModel):
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
        resource_file: str = None,
        storage_url: str = None,
        upload_mode: bool = None,
    ):
        # The code for the file. The code format varies based on the file type. To view the code format for a specific file type, go to Operation Center, open the directed acyclic graph (DAG) of a node of the file type, right-click the node, and then select View Code.
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
        # The type of the code for the file.
        # 
        # The code for files varies based on the file type. For more information, see [DataWorks nodes](https://help.aliyun.com/document_detail/600169.html). You can call the [ListFileType](https://help.aliyun.com/document_detail/212428.html) operation to query the type of the code for the file.
        # 
        # This parameter is required.
        self.file_type = file_type
        # The name of the original resource file.
        # 
        # This parameter is required.
        self.origin_resource_name = origin_resource_name
        # The ID of the Alibaba Cloud account used by the file owner. If this parameter is not configured, the ID of the Alibaba Cloud account of the user who calls the operation is used by default.
        self.owner = owner
        # The DataWorks workspace ID. You can log on to the DataWorks console and go to the Workspace page to query the ID. You must configure this parameter to specify the DataWorks workspace to which the operation is applied.
        # 
        # This parameter is required.
        self.project_id = project_id
        # Specifies whether to upload the resource file to a desired compute engine.
        # 
        # This parameter is required.
        self.register_to_calc_engine = register_to_calc_engine
        # The URL of the Object Storage Service (OSS) bucket to which you upload the file. The URL is provided by the POP platform.
        self.resource_file = resource_file
        # The storage path of the resource file in a desired compute engine. This parameter takes effect only for E-MapReduce (EMR) and Cloudera\\"s Distribution including Apache Hadoop (CDH) compute engines. In an EMR compute engine, this parameter is configured in the [osshdfs]://path/to/object format. In a CDH compute engine, this parameter is set to /user/admin/lib by default.
        self.storage_url = storage_url
        # The upload mode of MaxCompute file resources. This parameter takes effect only for MaxCompute file resources. Valid values:
        # 
        # *   true: indicates the resource upload and download mode.
        # *   false: indicates the online editing mode.
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

        if self.resource_file is not None:
            result['ResourceFile'] = self.resource_file

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
            self.resource_file = m.get('ResourceFile')

        if m.get('StorageURL') is not None:
            self.storage_url = m.get('StorageURL')

        if m.get('UploadMode') is not None:
            self.upload_mode = m.get('UploadMode')

        return self

