# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListResourcesResponseBody(DaraModel):
    def __init__(
        self,
        paging_info: main_models.ListResourcesResponseBodyPagingInfo = None,
        request_id: str = None,
    ):
        # The pagination information.
        self.paging_info = paging_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.paging_info:
            self.paging_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.paging_info is not None:
            result['PagingInfo'] = self.paging_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PagingInfo') is not None:
            temp_model = main_models.ListResourcesResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m.get('PagingInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListResourcesResponseBodyPagingInfo(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        resources: List[main_models.ListResourcesResponseBodyPagingInfoResources] = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The returned resource list.
        self.resources = resources
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.resources:
            for v1 in self.resources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Resources'] = []
        if self.resources is not None:
            for k1 in self.resources:
                result['Resources'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.resources = []
        if m.get('Resources') is not None:
            for k1 in m.get('Resources'):
                temp_model = main_models.ListResourcesResponseBodyPagingInfoResources()
                self.resources.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListResourcesResponseBodyPagingInfoResources(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        data_source: main_models.ListResourcesResponseBodyPagingInfoResourcesDataSource = None,
        id: str = None,
        modify_time: int = None,
        name: str = None,
        owner: str = None,
        project_id: int = None,
        script: main_models.ListResourcesResponseBodyPagingInfoResourcesScript = None,
        source_path: str = None,
        source_type: str = None,
        target_path: str = None,
        target_type: str = None,
        type: str = None,
    ):
        # The time when the file resource was created. This value is a UNIX timestamp.
        self.create_time = create_time
        # The data source.
        self.data_source = data_source
        # The unique identifier of the file resource.
        # 
        # >  Prior to SDK version 8.0.0, this field is of type Long. In SDK version 8.0.0 and later, it is of type String. This change does not affect the normal use of the SDK. The parameter is returned based on the type defined in the SDK. Compilation failures caused by the type change may occur only when you upgrade the SDK across version 8.0.0. In this case, you must manually update the data type.
        self.id = id
        # The timestamp when the file resource was last modified.
        self.modify_time = modify_time
        # The resource name.
        self.name = name
        # The owner of the file resource.
        self.owner = owner
        # The ID of the DataWorks workspace. To obtain the workspace ID, log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and navigate to the workspace configuration page.
        self.project_id = project_id
        # The script information.
        self.script = script
        # Source path of the file resource. This parameter is empty if the type is Local.
        self.source_path = source_path
        # The source storage type of the file resource.
        # 
        # Valid values:
        # 
        # *   Local
        # *   OSS
        self.source_type = source_type
        # The destination storage path.
        self.target_path = target_path
        # The destination storage type.
        # 
        # Valid values:
        # 
        # *   Gateway
        # *   OSS
        # *   HDFS
        self.target_type = target_type
        # The resource type.
        # 
        # Valid values:
        # 
        # *   Python
        # *   Jar
        # *   Archive
        # *   File
        self.type = type

    def validate(self):
        if self.data_source:
            self.data_source.validate()
        if self.script:
            self.script.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.data_source is not None:
            result['DataSource'] = self.data_source.to_map()

        if self.id is not None:
            result['Id'] = self.id

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.script is not None:
            result['Script'] = self.script.to_map()

        if self.source_path is not None:
            result['SourcePath'] = self.source_path

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.target_path is not None:
            result['TargetPath'] = self.target_path

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DataSource') is not None:
            temp_model = main_models.ListResourcesResponseBodyPagingInfoResourcesDataSource()
            self.data_source = temp_model.from_map(m.get('DataSource'))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Script') is not None:
            temp_model = main_models.ListResourcesResponseBodyPagingInfoResourcesScript()
            self.script = temp_model.from_map(m.get('Script'))

        if m.get('SourcePath') is not None:
            self.source_path = m.get('SourcePath')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('TargetPath') is not None:
            self.target_path = m.get('TargetPath')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListResourcesResponseBodyPagingInfoResourcesScript(DaraModel):
    def __init__(
        self,
        id: str = None,
        path: str = None,
        runtime: main_models.ListResourcesResponseBodyPagingInfoResourcesScriptRuntime = None,
    ):
        # The ID of the script.
        # 
        # >  This field is of type Long in SDK versions prior to 8.0.0, and of type String in SDK version 8.0.0 and later. This change does not affect the normal use of the SDK. The parameter is returned based on the type defined in the SDK. Compilation failures caused by the type change may occur only when you upgrade the SDK across version 8.0.0. In this case, you must manually update the data type.
        self.id = id
        # The script path.
        self.path = path
        # Runtime
        self.runtime = runtime

    def validate(self):
        if self.runtime:
            self.runtime.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.path is not None:
            result['Path'] = self.path

        if self.runtime is not None:
            result['Runtime'] = self.runtime.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Runtime') is not None:
            temp_model = main_models.ListResourcesResponseBodyPagingInfoResourcesScriptRuntime()
            self.runtime = temp_model.from_map(m.get('Runtime'))

        return self

class ListResourcesResponseBodyPagingInfoResourcesScriptRuntime(DaraModel):
    def __init__(
        self,
        command: str = None,
    ):
        # Command. This parameter indicates the file type.
        self.command = command

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.command is not None:
            result['Command'] = self.command

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')

        return self

class ListResourcesResponseBodyPagingInfoResourcesDataSource(DaraModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
    ):
        # The name of the data source.
        self.name = name
        # The type of the data source.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

