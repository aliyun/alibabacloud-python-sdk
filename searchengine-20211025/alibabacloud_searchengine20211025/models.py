# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class ErrorResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ResultClusterValue(TeaModel):
    def __init__(
        self,
        build_parallel_num: int = None,
        merge_parallel_num: int = None,
    ):
        # The maximum number of full indexes that can be concurrently built.
        self.build_parallel_num = build_parallel_num
        # The maximum number of full indexes that can be concurrently merged.
        self.merge_parallel_num = merge_parallel_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_parallel_num is not None:
            result['buildParallelNum'] = self.build_parallel_num
        if self.merge_parallel_num is not None:
            result['mergeParallelNum'] = self.merge_parallel_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('buildParallelNum') is not None:
            self.build_parallel_num = m.get('buildParallelNum')
        if m.get('mergeParallelNum') is not None:
            self.merge_parallel_num = m.get('mergeParallelNum')
        return self


class ResultDatabasesFunctionsValue(TeaModel):
    def __init__(
        self,
        name: str = None,
        signatures: str = None,
    ):
        self.name = name
        self.signatures = signatures

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.signatures is not None:
            result['signatures'] = self.signatures
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('signatures') is not None:
            self.signatures = m.get('signatures')
        return self


class ResultValue(TeaModel):
    def __init__(
        self,
        pause_all: bool = None,
        pause_index: bool = None,
        pause_index_batch: bool = None,
        pause_biz: bool = None,
        pause_runtime: bool = None,
    ):
        # Indicates whether all pushes are suspended.
        self.pause_all = pause_all
        # Indicates whether the push is suspended for the new full index version.
        self.pause_index = pause_index
        # Indicates whether the push is suspended for the incremental indexes.
        self.pause_index_batch = pause_index_batch
        # Indicates whether the push is suspended for the configuration.
        self.pause_biz = pause_biz
        # Indicates whether the push is suspended for the real-time incremental indexes.
        self.pause_runtime = pause_runtime

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pause_all is not None:
            result['pauseAll'] = self.pause_all
        if self.pause_index is not None:
            result['pauseIndex'] = self.pause_index
        if self.pause_index_batch is not None:
            result['pauseIndexBatch'] = self.pause_index_batch
        if self.pause_biz is not None:
            result['pauseBiz'] = self.pause_biz
        if self.pause_runtime is not None:
            result['pauseRuntime'] = self.pause_runtime
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pauseAll') is not None:
            self.pause_all = m.get('pauseAll')
        if m.get('pauseIndex') is not None:
            self.pause_index = m.get('pauseIndex')
        if m.get('pauseIndexBatch') is not None:
            self.pause_index_batch = m.get('pauseIndexBatch')
        if m.get('pauseBiz') is not None:
            self.pause_biz = m.get('pauseBiz')
        if m.get('pauseRuntime') is not None:
            self.pause_runtime = m.get('pauseRuntime')
        return self


class VariablesValueFuncValue(TeaModel):
    def __init__(
        self,
        func_class_name: str = None,
        template: str = None,
    ):
        # The class name of the function variable.
        self.func_class_name = func_class_name
        # The template of the function variable.
        self.template = template

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.func_class_name is not None:
            result['funcClassName'] = self.func_class_name
        if self.template is not None:
            result['template'] = self.template
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('funcClassName') is not None:
            self.func_class_name = m.get('funcClassName')
        if m.get('template') is not None:
            self.template = m.get('template')
        return self


class VariablesValue(TeaModel):
    def __init__(
        self,
        disable_modify: bool = None,
        is_modify: bool = None,
        value: str = None,
        description: str = None,
        template_value: str = None,
        type: str = None,
        func_value: VariablesValueFuncValue = None,
    ):
        # Specifies whether the variable is not allowed to be modified.
        self.disable_modify = disable_modify
        # Specifies whether the variable is modified.
        self.is_modify = is_modify
        # The variable value.
        self.value = value
        # The description of the variable.
        self.description = description
        # The template value of the variable.
        self.template_value = template_value
        # The variable type. Valid values:
        # 
        # *   NORMAL: common variable
        # *   FUNCTION: function variable
        self.type = type
        # The function variables.
        self.func_value = func_value

    def validate(self):
        if self.func_value:
            self.func_value.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disable_modify is not None:
            result['disableModify'] = self.disable_modify
        if self.is_modify is not None:
            result['isModify'] = self.is_modify
        if self.value is not None:
            result['value'] = self.value
        if self.description is not None:
            result['description'] = self.description
        if self.template_value is not None:
            result['templateValue'] = self.template_value
        if self.type is not None:
            result['type'] = self.type
        if self.func_value is not None:
            result['funcValue'] = self.func_value.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('disableModify') is not None:
            self.disable_modify = m.get('disableModify')
        if m.get('isModify') is not None:
            self.is_modify = m.get('isModify')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('templateValue') is not None:
            self.template_value = m.get('templateValue')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('funcValue') is not None:
            temp_model = VariablesValueFuncValue()
            self.func_value = temp_model.from_map(m['funcValue'])
        return self


class ConfigValueFilesConfigVariablesValue(TeaModel):
    def __init__(
        self,
        description: str = None,
        disable_modify: bool = None,
        is_modify: bool = None,
        type: str = None,
        value: str = None,
    ):
        # The description of the variable.
        self.description = description
        # Specifies whether the variable is not allowed to be modified.
        self.disable_modify = disable_modify
        # Specifies whether the variable is modified.
        self.is_modify = is_modify
        # The variable type. Valid values: NORMAL: common variable. FUNCTION: function variable.
        self.type = type
        # The variable value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.disable_modify is not None:
            result['disableModify'] = self.disable_modify
        if self.is_modify is not None:
            result['isModify'] = self.is_modify
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('disableModify') is not None:
            self.disable_modify = m.get('disableModify')
        if m.get('isModify') is not None:
            self.is_modify = m.get('isModify')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ConfigValueFilesConfig(TeaModel):
    def __init__(
        self,
        content: str = None,
        variables: Dict[str, ConfigValueFilesConfigVariablesValue] = None,
    ):
        # The file content.
        self.content = content
        # The variables.
        self.variables = variables

    def validate(self):
        if self.variables:
            for v in self.variables.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        result['variables'] = {}
        if self.variables is not None:
            for k, v in self.variables.items():
                result['variables'][k] = v.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        self.variables = {}
        if m.get('variables') is not None:
            for k, v in m.get('variables').items():
                temp_model = ConfigValueFilesConfigVariablesValue()
                self.variables[k] = temp_model.from_map(v)
        return self


class ConfigValueFiles(TeaModel):
    def __init__(
        self,
        operate_type: str = None,
        parent_full_path: str = None,
        file_name: str = None,
        config: ConfigValueFilesConfig = None,
        dir_name: str = None,
    ):
        # The operation type. Valid values: UPDATE and DELETE. Default value: UPDATE.
        self.operate_type = operate_type
        # The path of the parent directory.
        self.parent_full_path = parent_full_path
        # The file name.
        self.file_name = file_name
        # The configuration to be modified.
        self.config = config
        # The directory name.
        self.dir_name = dir_name

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operate_type is not None:
            result['operateType'] = self.operate_type
        if self.parent_full_path is not None:
            result['parentFullPath'] = self.parent_full_path
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.config is not None:
            result['config'] = self.config.to_map()
        if self.dir_name is not None:
            result['dirName'] = self.dir_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('operateType') is not None:
            self.operate_type = m.get('operateType')
        if m.get('parentFullPath') is not None:
            self.parent_full_path = m.get('parentFullPath')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('config') is not None:
            temp_model = ConfigValueFilesConfig()
            self.config = temp_model.from_map(m['config'])
        if m.get('dirName') is not None:
            self.dir_name = m.get('dirName')
        return self


class ConfigValue(TeaModel):
    def __init__(
        self,
        desc: str = None,
        files: List[ConfigValueFiles] = None,
    ):
        # The description of the offline configuration.
        self.desc = desc
        # The files to be modified.
        self.files = files

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['desc'] = self.desc
        result['files'] = []
        if self.files is not None:
            for k in self.files:
                result['files'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        self.files = []
        if m.get('files') is not None:
            for k in m.get('files'):
                temp_model = ConfigValueFiles()
                self.files.append(temp_model.from_map(k))
        return self


class BodyValue(TeaModel):
    def __init__(
        self,
        pause_all: bool = None,
        pause_index: bool = None,
        pause_index_batch: bool = None,
        pause_biz: bool = None,
        pause_runtime: bool = None,
    ):
        # Specifies whether to suspend all pushes.
        self.pause_all = pause_all
        # Specifies whether to suspend the push for the new full index version.
        self.pause_index = pause_index
        # Specifies whether to suspend the push for the incremental indexes.
        self.pause_index_batch = pause_index_batch
        # Specifies whether to suspend the push for the configuration.
        self.pause_biz = pause_biz
        # Specifies whether to suspend the push for the real-time incremental indexes.
        self.pause_runtime = pause_runtime

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pause_all is not None:
            result['pauseAll'] = self.pause_all
        if self.pause_index is not None:
            result['pauseIndex'] = self.pause_index
        if self.pause_index_batch is not None:
            result['pauseIndexBatch'] = self.pause_index_batch
        if self.pause_biz is not None:
            result['pauseBiz'] = self.pause_biz
        if self.pause_runtime is not None:
            result['pauseRuntime'] = self.pause_runtime
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pauseAll') is not None:
            self.pause_all = m.get('pauseAll')
        if m.get('pauseIndex') is not None:
            self.pause_index = m.get('pauseIndex')
        if m.get('pauseIndexBatch') is not None:
            self.pause_index_batch = m.get('pauseIndexBatch')
        if m.get('pauseBiz') is not None:
            self.pause_biz = m.get('pauseBiz')
        if m.get('pauseRuntime') is not None:
            self.pause_runtime = m.get('pauseRuntime')
        return self


class FilesConfigVariablesValue(TeaModel):
    def __init__(
        self,
        description: str = None,
        disable_modify: bool = None,
        is_modify: bool = None,
        type: str = None,
        value: str = None,
    ):
        # The description of the variable.
        self.description = description
        # Specifies whether the variable is not allowed to be modified.
        self.disable_modify = disable_modify
        # Specifies whether the variable is modified.
        self.is_modify = is_modify
        # The variable type. Valid values: NORMAL: common variable. FUNCTION: function variable.
        self.type = type
        # The variable value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.disable_modify is not None:
            result['disableModify'] = self.disable_modify
        if self.is_modify is not None:
            result['isModify'] = self.is_modify
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('disableModify') is not None:
            self.disable_modify = m.get('disableModify')
        if m.get('isModify') is not None:
            self.is_modify = m.get('isModify')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class BuildIndexRequest(TeaModel):
    def __init__(
        self,
        build_mode: str = None,
        data_source_name: str = None,
        data_source_type: str = None,
        data_time_sec: int = None,
        domain: str = None,
        generation: int = None,
        partition: str = None,
    ):
        # The reindexing method. Valid values: api: API data source. indexRecover: data recovery by using indexing.
        self.build_mode = build_mode
        # The name of the data source.
        self.data_source_name = data_source_name
        # The type of the data source.
        self.data_source_type = data_source_type
        # The timestamp in seconds. The value must be of the INTEGER type. This parameter is required if you specify an API data source.
        self.data_time_sec = data_time_sec
        # The data center in which the data source is deployed.
        self.domain = domain
        # The data restoration version.
        self.generation = generation
        # The partition in the MaxCompute table. This parameter is required if type is set to odps.
        self.partition = partition

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_mode is not None:
            result['buildMode'] = self.build_mode
        if self.data_source_name is not None:
            result['dataSourceName'] = self.data_source_name
        if self.data_source_type is not None:
            result['dataSourceType'] = self.data_source_type
        if self.data_time_sec is not None:
            result['dataTimeSec'] = self.data_time_sec
        if self.domain is not None:
            result['domain'] = self.domain
        if self.generation is not None:
            result['generation'] = self.generation
        if self.partition is not None:
            result['partition'] = self.partition
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('buildMode') is not None:
            self.build_mode = m.get('buildMode')
        if m.get('dataSourceName') is not None:
            self.data_source_name = m.get('dataSourceName')
        if m.get('dataSourceType') is not None:
            self.data_source_type = m.get('dataSourceType')
        if m.get('dataTimeSec') is not None:
            self.data_time_sec = m.get('dataTimeSec')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('generation') is not None:
            self.generation = m.get('generation')
        if m.get('partition') is not None:
            self.partition = m.get('partition')
        return self


class BuildIndexResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # id of request
        self.request_id = request_id
        # The list of clusters
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class BuildIndexResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BuildIndexResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BuildIndexResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeResourceGroupRequest(TeaModel):
    def __init__(
        self,
        new_resource_group_id: str = None,
        resource_type: str = None,
    ):
        # new resource group id
        self.new_resource_group_id = new_resource_group_id
        # The resource type.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_resource_group_id is not None:
            result['newResourceGroupId'] = self.new_resource_group_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('newResourceGroupId') is not None:
            self.new_resource_group_id = m.get('newResourceGroupId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class ChangeResourceGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ChangeResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChangeResourceGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ChangeResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloneSqlInstanceRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        target_folder_id: int = None,
    ):
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.target_folder_id = target_folder_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.target_folder_id is not None:
            result['targetFolderId'] = self.target_folder_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('targetFolderId') is not None:
            self.target_folder_id = m.get('targetFolderId')
        return self


class CloneSqlInstanceResponseBodyResult(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        instance_id: int = None,
        is_dir: int = None,
        name: str = None,
        parent: int = None,
        template_id: int = None,
        type: str = None,
    ):
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.instance_id = instance_id
        self.is_dir = is_dir
        self.name = name
        self.parent = parent
        self.template_id = template_id
        # table, instance, template, function
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.is_dir is not None:
            result['isDir'] = self.is_dir
        if self.name is not None:
            result['name'] = self.name
        if self.parent is not None:
            result['parent'] = self.parent
        if self.template_id is not None:
            result['templateId'] = self.template_id
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('isDir') is not None:
            self.is_dir = m.get('isDir')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parent') is not None:
            self.parent = m.get('parent')
        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CloneSqlInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: CloneSqlInstanceResponseBodyResult = None,
    ):
        # id of request
        self.request_id = request_id
        # NodeVO
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = CloneSqlInstanceResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class CloneSqlInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CloneSqlInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CloneSqlInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAliasRequest(TeaModel):
    def __init__(
        self,
        alias: str = None,
        index: str = None,
        new_mode: bool = None,
    ):
        # alias name
        self.alias = alias
        # index name
        self.index = index
        # Specifies whether the OpenSearch Vector Search Edition instance is of the new version.
        self.new_mode = new_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['alias'] = self.alias
        if self.index is not None:
            result['index'] = self.index
        if self.new_mode is not None:
            result['newMode'] = self.new_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alias') is not None:
            self.alias = m.get('alias')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('newMode') is not None:
            self.new_mode = m.get('newMode')
        return self


class CreateAliasResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # id of request
        self.request_id = request_id
        # Map
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class CreateAliasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAliasResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAliasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateClusterRequestDataNode(TeaModel):
    def __init__(
        self,
        number: int = None,
        partition: str = None,
    ):
        # The number of Searcher workers.
        self.number = number
        # The number of shards.
        self.partition = partition

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.number is not None:
            result['number'] = self.number
        if self.partition is not None:
            result['partition'] = self.partition
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('number') is not None:
            self.number = m.get('number')
        if m.get('partition') is not None:
            self.partition = m.get('partition')
        return self


class CreateClusterRequestQueryNode(TeaModel):
    def __init__(
        self,
        number: int = None,
    ):
        # The number of QRS workers.
        self.number = number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.number is not None:
            result['number'] = self.number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('number') is not None:
            self.number = m.get('number')
        return self


class CreateClusterRequest(TeaModel):
    def __init__(
        self,
        auto_load: bool = None,
        data_node: CreateClusterRequestDataNode = None,
        description: str = None,
        name: str = None,
        query_node: CreateClusterRequestQueryNode = None,
    ):
        # Specifies whether to enable automatic connection.
        self.auto_load = auto_load
        # The details of the Searcher workers.
        self.data_node = data_node
        # The description of the cluster.
        self.description = description
        # The cluster name.
        self.name = name
        # The details of the Query Result Searcher (QRS) workers.
        self.query_node = query_node

    def validate(self):
        if self.data_node:
            self.data_node.validate()
        if self.query_node:
            self.query_node.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_load is not None:
            result['autoLoad'] = self.auto_load
        if self.data_node is not None:
            result['dataNode'] = self.data_node.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.query_node is not None:
            result['queryNode'] = self.query_node.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoLoad') is not None:
            self.auto_load = m.get('autoLoad')
        if m.get('dataNode') is not None:
            temp_model = CreateClusterRequestDataNode()
            self.data_node = temp_model.from_map(m['dataNode'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('queryNode') is not None:
            temp_model = CreateClusterRequestQueryNode()
            self.query_node = temp_model.from_map(m['queryNode'])
        return self


class CreateClusterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The result.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class CreateClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateClusterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateConfigDirRequest(TeaModel):
    def __init__(
        self,
        dir_name: str = None,
        parent_full_path: str = None,
    ):
        # The directory name.
        self.dir_name = dir_name
        # The path of the parent directory.
        self.parent_full_path = parent_full_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dir_name is not None:
            result['dirName'] = self.dir_name
        if self.parent_full_path is not None:
            result['parentFullPath'] = self.parent_full_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dirName') is not None:
            self.dir_name = m.get('dirName')
        if m.get('parentFullPath') is not None:
            self.parent_full_path = m.get('parentFullPath')
        return self


class CreateConfigDirResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The result.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class CreateConfigDirResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateConfigDirResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateConfigDirResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateConfigFileRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        oss_path: str = None,
        parent_full_path: str = None,
    ):
        # The name of the directory.
        self.file_name = file_name
        # The Object Storage Service (OSS) URL of the file.
        self.oss_path = oss_path
        # The path of the parent directory.
        self.parent_full_path = parent_full_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.oss_path is not None:
            result['ossPath'] = self.oss_path
        if self.parent_full_path is not None:
            result['parentFullPath'] = self.parent_full_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('ossPath') is not None:
            self.oss_path = m.get('ossPath')
        if m.get('parentFullPath') is not None:
            self.parent_full_path = m.get('parentFullPath')
        return self


class CreateConfigFileResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The result.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class CreateConfigFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateConfigFileResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateConfigFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDataSourceRequestConfig(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        access_secret: str = None,
        bucket: str = None,
        endpoint: str = None,
        namespace: str = None,
        oss_path: str = None,
        partition: str = None,
        path: str = None,
        project: str = None,
        table: str = None,
    ):
        # The AccessKey ID of the MaxCompute data source.
        self.access_key = access_key
        # The AccessKey secret of the MaxCompute data source.
        self.access_secret = access_secret
        # The name of the OSS bucket.
        self.bucket = bucket
        # The endpoint of the MaxCompute or Object Storage Service (OSS) data source.
        self.endpoint = endpoint
        # The namespace.
        self.namespace = namespace
        # The path of the OSS object.
        self.oss_path = oss_path
        # The partition in the MaxCompute table.
        self.partition = partition
        # The file path in the Apsara File Storage for HDFS file system.
        self.path = path
        # The name of the MaxCompute project that is used as the data source.
        self.project = project
        # The name of the MaxCompute table that is used as the data source.
        self.table = table

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.access_secret is not None:
            result['accessSecret'] = self.access_secret
        if self.bucket is not None:
            result['bucket'] = self.bucket
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.oss_path is not None:
            result['ossPath'] = self.oss_path
        if self.partition is not None:
            result['partition'] = self.partition
        if self.path is not None:
            result['path'] = self.path
        if self.project is not None:
            result['project'] = self.project
        if self.table is not None:
            result['table'] = self.table
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('accessSecret') is not None:
            self.access_secret = m.get('accessSecret')
        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('ossPath') is not None:
            self.oss_path = m.get('ossPath')
        if m.get('partition') is not None:
            self.partition = m.get('partition')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('table') is not None:
            self.table = m.get('table')
        return self


class CreateDataSourceRequestSaroConfig(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        table_name: str = None,
    ):
        # The namespace of the SARO data source.
        self.namespace = namespace
        # The name of the SARO table.
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.table_name is not None:
            result['tableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        return self


class CreateDataSourceRequest(TeaModel):
    def __init__(
        self,
        auto_build_index: bool = None,
        config: CreateDataSourceRequestConfig = None,
        domain: str = None,
        name: str = None,
        saro_config: CreateDataSourceRequestSaroConfig = None,
        type: str = None,
        dry_run: bool = None,
    ):
        # Specifies whether to automatically rebuild the index.
        self.auto_build_index = auto_build_index
        # The configuration information.
        self.config = config
        # The data center in which the data source is deployed.
        self.domain = domain
        # The name of the data source.
        self.name = name
        # The configurations of the SARO data source.
        self.saro_config = saro_config
        # The type of the data source. Valid values: odps, oss, and swift.
        self.type = type
        # Specifies whether to perform a dry run. This parameter is only used to check whether the data source is valid. Valid values: true and false.
        self.dry_run = dry_run

    def validate(self):
        if self.config:
            self.config.validate()
        if self.saro_config:
            self.saro_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_build_index is not None:
            result['autoBuildIndex'] = self.auto_build_index
        if self.config is not None:
            result['config'] = self.config.to_map()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.name is not None:
            result['name'] = self.name
        if self.saro_config is not None:
            result['saroConfig'] = self.saro_config.to_map()
        if self.type is not None:
            result['type'] = self.type
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoBuildIndex') is not None:
            self.auto_build_index = m.get('autoBuildIndex')
        if m.get('config') is not None:
            temp_model = CreateDataSourceRequestConfig()
            self.config = temp_model.from_map(m['config'])
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('saroConfig') is not None:
            temp_model = CreateDataSourceRequestSaroConfig()
            self.saro_config = temp_model.from_map(m['saroConfig'])
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class CreateDataSourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The returned results.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class CreateDataSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDataSourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateDataSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFolderRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        parent: int = None,
        type: str = None,
    ):
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.parent = parent
        # table, instance, template, function
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.parent is not None:
            result['parent'] = self.parent
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parent') is not None:
            self.parent = m.get('parent')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateFolderResponseBodyResult(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        instance_id: int = None,
        is_dir: int = None,
        name: str = None,
        parent: int = None,
        template_id: int = None,
        type: str = None,
    ):
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.instance_id = instance_id
        self.is_dir = is_dir
        self.name = name
        self.parent = parent
        self.template_id = template_id
        # table, instance, template, function
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.is_dir is not None:
            result['isDir'] = self.is_dir
        if self.name is not None:
            result['name'] = self.name
        if self.parent is not None:
            result['parent'] = self.parent
        if self.template_id is not None:
            result['templateId'] = self.template_id
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('isDir') is not None:
            self.is_dir = m.get('isDir')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parent') is not None:
            self.parent = m.get('parent')
        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateFolderResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: CreateFolderResponseBodyResult = None,
    ):
        # id of request
        self.request_id = request_id
        # NodeVO
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = CreateFolderResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class CreateFolderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFolderResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateFolderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIndexRequestDataSourceInfoConfig(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        access_secret: str = None,
        bucket: str = None,
        endpoint: str = None,
        namespace: str = None,
        oss_path: str = None,
        partition: str = None,
        path: str = None,
        project: str = None,
        table: str = None,
    ):
        # The AccessKey ID of the MaxCompute data source.
        self.access_key = access_key
        # The AccessKey secret of the MaxCompute data source.
        self.access_secret = access_secret
        # The name of the OSS bucket.
        self.bucket = bucket
        # The endpoint of the MaxCompute or Object Storage Service (OSS) data source.
        self.endpoint = endpoint
        # The namespace name.
        self.namespace = namespace
        # The path of the OSS object.
        self.oss_path = oss_path
        # The partition in the MaxCompute table. This parameter is required if type is set to odps.
        self.partition = partition
        # The path of the Apsara File Storage for HDFS data source.
        self.path = path
        # The name of the MaxCompute project that is used as the data source.
        self.project = project
        # The table name.
        self.table = table

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.access_secret is not None:
            result['accessSecret'] = self.access_secret
        if self.bucket is not None:
            result['bucket'] = self.bucket
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.oss_path is not None:
            result['ossPath'] = self.oss_path
        if self.partition is not None:
            result['partition'] = self.partition
        if self.path is not None:
            result['path'] = self.path
        if self.project is not None:
            result['project'] = self.project
        if self.table is not None:
            result['table'] = self.table
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('accessSecret') is not None:
            self.access_secret = m.get('accessSecret')
        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('ossPath') is not None:
            self.oss_path = m.get('ossPath')
        if m.get('partition') is not None:
            self.partition = m.get('partition')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('table') is not None:
            self.table = m.get('table')
        return self


class CreateIndexRequestDataSourceInfoSaroConfig(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        table_name: str = None,
    ):
        # The namespace of the SARO data source.
        self.namespace = namespace
        # The name of the SARO table.
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.table_name is not None:
            result['tableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        return self


class CreateIndexRequestDataSourceInfo(TeaModel):
    def __init__(
        self,
        auto_build_index: bool = None,
        config: CreateIndexRequestDataSourceInfoConfig = None,
        data_time_sec: int = None,
        domain: str = None,
        name: str = None,
        process_parallel_num: int = None,
        process_partition_count: int = None,
        saro_config: CreateIndexRequestDataSourceInfoSaroConfig = None,
        type: str = None,
    ):
        # Specifies whether to enable automatic full indexing.
        self.auto_build_index = auto_build_index
        # The information about the MaxCompute data source.
        self.config = config
        # The start timestamp from which incremental data is retrieved.
        self.data_time_sec = data_time_sec
        # The data center in which the data source is deployed.
        self.domain = domain
        # The name of the data source.
        self.name = name
        # The maximum number of full indexes that can be concurrently processed.
        self.process_parallel_num = process_parallel_num
        # The number of resources used for data update.
        self.process_partition_count = process_partition_count
        # The configurations of the SARO data source.
        self.saro_config = saro_config
        # The type of the data source. Valid values:
        # 
        # *   odps
        # *   swift
        # *   saro
        # *   oss
        self.type = type

    def validate(self):
        if self.config:
            self.config.validate()
        if self.saro_config:
            self.saro_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_build_index is not None:
            result['autoBuildIndex'] = self.auto_build_index
        if self.config is not None:
            result['config'] = self.config.to_map()
        if self.data_time_sec is not None:
            result['dataTimeSec'] = self.data_time_sec
        if self.domain is not None:
            result['domain'] = self.domain
        if self.name is not None:
            result['name'] = self.name
        if self.process_parallel_num is not None:
            result['processParallelNum'] = self.process_parallel_num
        if self.process_partition_count is not None:
            result['processPartitionCount'] = self.process_partition_count
        if self.saro_config is not None:
            result['saroConfig'] = self.saro_config.to_map()
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoBuildIndex') is not None:
            self.auto_build_index = m.get('autoBuildIndex')
        if m.get('config') is not None:
            temp_model = CreateIndexRequestDataSourceInfoConfig()
            self.config = temp_model.from_map(m['config'])
        if m.get('dataTimeSec') is not None:
            self.data_time_sec = m.get('dataTimeSec')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('processParallelNum') is not None:
            self.process_parallel_num = m.get('processParallelNum')
        if m.get('processPartitionCount') is not None:
            self.process_partition_count = m.get('processPartitionCount')
        if m.get('saroConfig') is not None:
            temp_model = CreateIndexRequestDataSourceInfoSaroConfig()
            self.saro_config = temp_model.from_map(m['saroConfig'])
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateIndexRequest(TeaModel):
    def __init__(
        self,
        build_parallel_num: int = None,
        content: str = None,
        data_source: str = None,
        data_source_info: CreateIndexRequestDataSourceInfo = None,
        domain: str = None,
        extend: Dict[str, Any] = None,
        merge_parallel_num: int = None,
        name: str = None,
        partition: int = None,
        dry_run: bool = None,
    ):
        # The maximum number of full indexes that can be concurrently built.
        self.build_parallel_num = build_parallel_num
        # The index schema.
        self.content = content
        # The name of the data source.
        self.data_source = data_source
        # The information about the data source. This parameter is required for an OpenSearch Vector Search Edition instance of the new version.
        self.data_source_info = data_source_info
        # The data center in which the data source is deployed.
        self.domain = domain
        # The extended content of the field configuration. key specifies the vector field and the field that requires embedding.
        self.extend = extend
        # The maximum number of full indexes that can be concurrently merged.
        self.merge_parallel_num = merge_parallel_num
        # The index name.
        self.name = name
        # The number of data shards.
        self.partition = partition
        # Specifies whether to perform only a dry run, without performing the actual request. The system only checks the validity of the data source. Valid values:
        # 
        # *   true
        # *   false
        self.dry_run = dry_run

    def validate(self):
        if self.data_source_info:
            self.data_source_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_parallel_num is not None:
            result['buildParallelNum'] = self.build_parallel_num
        if self.content is not None:
            result['content'] = self.content
        if self.data_source is not None:
            result['dataSource'] = self.data_source
        if self.data_source_info is not None:
            result['dataSourceInfo'] = self.data_source_info.to_map()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.extend is not None:
            result['extend'] = self.extend
        if self.merge_parallel_num is not None:
            result['mergeParallelNum'] = self.merge_parallel_num
        if self.name is not None:
            result['name'] = self.name
        if self.partition is not None:
            result['partition'] = self.partition
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('buildParallelNum') is not None:
            self.build_parallel_num = m.get('buildParallelNum')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('dataSource') is not None:
            self.data_source = m.get('dataSource')
        if m.get('dataSourceInfo') is not None:
            temp_model = CreateIndexRequestDataSourceInfo()
            self.data_source_info = temp_model.from_map(m['dataSourceInfo'])
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('extend') is not None:
            self.extend = m.get('extend')
        if m.get('mergeParallelNum') is not None:
            self.merge_parallel_num = m.get('mergeParallelNum')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('partition') is not None:
            self.partition = m.get('partition')
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class CreateIndexResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The results returned.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class CreateIndexResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateIndexResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateIndexResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceRequestComponents(TeaModel):
    def __init__(
        self,
        code: str = None,
        value: str = None,
    ):
        # The code of the specification, which must be consistent with the value that you specify on the buy page.
        self.code = code
        # The value of the specification.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class CreateInstanceRequestOrder(TeaModel):
    def __init__(
        self,
        auto_renew: bool = None,
        duration: int = None,
        pricing_cycle: str = None,
    ):
        # Specifies whether to enable auto-renewal. Valid values: true and false.
        self.auto_renew = auto_renew
        # The billing duration. Valid values: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, and 12.
        self.duration = duration
        # The unit of the billing duration. Valid values: Month and Year.
        self.pricing_cycle = pricing_cycle

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['autoRenew'] = self.auto_renew
        if self.duration is not None:
            result['duration'] = self.duration
        if self.pricing_cycle is not None:
            result['pricingCycle'] = self.pricing_cycle
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoRenew') is not None:
            self.auto_renew = m.get('autoRenew')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('pricingCycle') is not None:
            self.pricing_cycle = m.get('pricingCycle')
        return self


class CreateInstanceRequest(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        components: List[CreateInstanceRequestComponents] = None,
        order: CreateInstanceRequestOrder = None,
    ):
        # The billing method of the instance. Valid values: PREPAY: subscription. If you set this parameter to PREPAY, make sure that your Alibaba Cloud account supports balance payment or credit card payment. Otherwise, the system returns the InvalidPayMethod error message. If you set this parameter to PREPAY, you must also specify paymentInfo. POSTPAY: pay-as-you-go. This billing method is not supported.
        self.charge_type = charge_type
        # The information about the instance specification.
        self.components = components
        # The billing information.
        self.order = order

    def validate(self):
        if self.components:
            for k in self.components:
                if k:
                    k.validate()
        if self.order:
            self.order.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        result['components'] = []
        if self.components is not None:
            for k in self.components:
                result['components'].append(k.to_map() if k else None)
        if self.order is not None:
            result['order'] = self.order.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        self.components = []
        if m.get('components') is not None:
            for k in m.get('components'):
                temp_model = CreateInstanceRequestComponents()
                self.components.append(temp_model.from_map(k))
        if m.get('order') is not None:
            temp_model = CreateInstanceRequestOrder()
            self.order = temp_model.from_map(m['order'])
        return self


class CreateInstanceResponseBodyResult(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # The instance ID.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self


class CreateInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: CreateInstanceResponseBodyResult = None,
    ):
        # The ID of the request
        self.request_id = request_id
        # The results returned.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = CreateInstanceResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class CreateInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePublicUrlResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The result.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class CreatePublicUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatePublicUrlResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreatePublicUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSqlInstanceRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        parent: int = None,
    ):
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.parent = parent

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.parent is not None:
            result['parent'] = self.parent
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parent') is not None:
            self.parent = m.get('parent')
        return self


class CreateSqlInstanceResponseBodyResult(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        instance_id: int = None,
        is_dir: int = None,
        name: str = None,
        parent: int = None,
        template_id: int = None,
        type: str = None,
    ):
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.instance_id = instance_id
        self.is_dir = is_dir
        self.name = name
        self.parent = parent
        self.template_id = template_id
        # table, instance, template, function
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.is_dir is not None:
            result['isDir'] = self.is_dir
        if self.name is not None:
            result['name'] = self.name
        if self.parent is not None:
            result['parent'] = self.parent
        if self.template_id is not None:
            result['templateId'] = self.template_id
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('isDir') is not None:
            self.is_dir = m.get('isDir')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parent') is not None:
            self.parent = m.get('parent')
        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateSqlInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: CreateSqlInstanceResponseBodyResult = None,
    ):
        # id of request
        self.request_id = request_id
        # NodeVO
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = CreateSqlInstanceResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class CreateSqlInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSqlInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateSqlInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTableRequestDataProcessConfigParamsSrcFieldConfig(TeaModel):
    def __init__(
        self,
        oss_bucket: str = None,
        oss_endpoint: str = None,
        uid: str = None,
    ):
        # The OSS bucket.
        self.oss_bucket = oss_bucket
        # The OSS endpoint.
        self.oss_endpoint = oss_endpoint
        # The ID of the Alibaba Cloud account.
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss_bucket is not None:
            result['ossBucket'] = self.oss_bucket
        if self.oss_endpoint is not None:
            result['ossEndpoint'] = self.oss_endpoint
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ossBucket') is not None:
            self.oss_bucket = m.get('ossBucket')
        if m.get('ossEndpoint') is not None:
            self.oss_endpoint = m.get('ossEndpoint')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class CreateTableRequestDataProcessConfigParams(TeaModel):
    def __init__(
        self,
        src_field_config: CreateTableRequestDataProcessConfigParamsSrcFieldConfig = None,
        vector_modal: str = None,
        vector_model: str = None,
    ):
        # The source of the data to be vectorized.
        self.src_field_config = src_field_config
        # The data type.
        self.vector_modal = vector_modal
        # The vectorization model.
        self.vector_model = vector_model

    def validate(self):
        if self.src_field_config:
            self.src_field_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.src_field_config is not None:
            result['srcFieldConfig'] = self.src_field_config.to_map()
        if self.vector_modal is not None:
            result['vectorModal'] = self.vector_modal
        if self.vector_model is not None:
            result['vectorModel'] = self.vector_model
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('srcFieldConfig') is not None:
            temp_model = CreateTableRequestDataProcessConfigParamsSrcFieldConfig()
            self.src_field_config = temp_model.from_map(m['srcFieldConfig'])
        if m.get('vectorModal') is not None:
            self.vector_modal = m.get('vectorModal')
        if m.get('vectorModel') is not None:
            self.vector_model = m.get('vectorModel')
        return self


class CreateTableRequestDataProcessConfig(TeaModel):
    def __init__(
        self,
        dst_field: str = None,
        operator: str = None,
        params: CreateTableRequestDataProcessConfigParams = None,
        src_field: str = None,
    ):
        # The destination field.
        self.dst_field = dst_field
        # The method used to process the field. Valid values: copy and vectorize. A value of copy specifies that the value of the source field is copied to the destination field. A value of vectorize specifies that the value of the source field is vectorized by a vectorization model and the output vector is stored in the destination field.
        self.operator = operator
        # The information about the model.
        self.params = params
        # The source field.
        self.src_field = src_field

    def validate(self):
        if self.params:
            self.params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dst_field is not None:
            result['dstField'] = self.dst_field
        if self.operator is not None:
            result['operator'] = self.operator
        if self.params is not None:
            result['params'] = self.params.to_map()
        if self.src_field is not None:
            result['srcField'] = self.src_field
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dstField') is not None:
            self.dst_field = m.get('dstField')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('params') is not None:
            temp_model = CreateTableRequestDataProcessConfigParams()
            self.params = temp_model.from_map(m['params'])
        if m.get('srcField') is not None:
            self.src_field = m.get('srcField')
        return self


class CreateTableRequestDataSourceConfig(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        access_secret: str = None,
        bucket: str = None,
        endpoint: str = None,
        oss_path: str = None,
        partition: str = None,
        project: str = None,
        table: str = None,
    ):
        # The AccessKey ID of the MaxCompute data source.
        self.access_key = access_key
        # The AccessKey secret of the MaxCompute data source.
        self.access_secret = access_secret
        # The OSS bucket.
        self.bucket = bucket
        # The endpoint of the MaxCompute data source.
        self.endpoint = endpoint
        # The Object Storage Service (OSS) path.
        self.oss_path = oss_path
        # The partition in the MaxCompute table. This parameter is required if type is set to odps.
        self.partition = partition
        # The name of the MaxCompute project that is used as the data source.
        self.project = project
        # The name of the MaxCompute table that is used as the data source.
        self.table = table

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.access_secret is not None:
            result['accessSecret'] = self.access_secret
        if self.bucket is not None:
            result['bucket'] = self.bucket
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.oss_path is not None:
            result['ossPath'] = self.oss_path
        if self.partition is not None:
            result['partition'] = self.partition
        if self.project is not None:
            result['project'] = self.project
        if self.table is not None:
            result['table'] = self.table
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('accessSecret') is not None:
            self.access_secret = m.get('accessSecret')
        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('ossPath') is not None:
            self.oss_path = m.get('ossPath')
        if m.get('partition') is not None:
            self.partition = m.get('partition')
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('table') is not None:
            self.table = m.get('table')
        return self


class CreateTableRequestDataSource(TeaModel):
    def __init__(
        self,
        auto_build_index: bool = None,
        config: CreateTableRequestDataSourceConfig = None,
        data_time_sec: int = None,
        type: str = None,
    ):
        # Specifies whether to automatically rebuild the index.
        self.auto_build_index = auto_build_index
        # The configurations of the data source.
        self.config = config
        # The start timestamp from which incremental data is retrieved.
        self.data_time_sec = data_time_sec
        # The data source type. Valid values: odps, swift, and oss.
        self.type = type

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_build_index is not None:
            result['autoBuildIndex'] = self.auto_build_index
        if self.config is not None:
            result['config'] = self.config.to_map()
        if self.data_time_sec is not None:
            result['dataTimeSec'] = self.data_time_sec
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoBuildIndex') is not None:
            self.auto_build_index = m.get('autoBuildIndex')
        if m.get('config') is not None:
            temp_model = CreateTableRequestDataSourceConfig()
            self.config = temp_model.from_map(m['config'])
        if m.get('dataTimeSec') is not None:
            self.data_time_sec = m.get('dataTimeSec')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateTableRequestVectorIndexAdvanceParams(TeaModel):
    def __init__(
        self,
        build_index_params: str = None,
        linear_build_threshold: str = None,
        min_scan_doc_cnt: str = None,
        search_index_params: str = None,
    ):
        # The index building parameters.
        self.build_index_params = build_index_params
        # The threshold for linear building.
        self.linear_build_threshold = linear_build_threshold
        # The minimum number of retrieved candidate sets.
        self.min_scan_doc_cnt = min_scan_doc_cnt
        # The index retrieval parameters.
        self.search_index_params = search_index_params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_index_params is not None:
            result['buildIndexParams'] = self.build_index_params
        if self.linear_build_threshold is not None:
            result['linearBuildThreshold'] = self.linear_build_threshold
        if self.min_scan_doc_cnt is not None:
            result['minScanDocCnt'] = self.min_scan_doc_cnt
        if self.search_index_params is not None:
            result['searchIndexParams'] = self.search_index_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('buildIndexParams') is not None:
            self.build_index_params = m.get('buildIndexParams')
        if m.get('linearBuildThreshold') is not None:
            self.linear_build_threshold = m.get('linearBuildThreshold')
        if m.get('minScanDocCnt') is not None:
            self.min_scan_doc_cnt = m.get('minScanDocCnt')
        if m.get('searchIndexParams') is not None:
            self.search_index_params = m.get('searchIndexParams')
        return self


class CreateTableRequestVectorIndex(TeaModel):
    def __init__(
        self,
        advance_params: CreateTableRequestVectorIndexAdvanceParams = None,
        dimension: str = None,
        distance_type: str = None,
        index_name: str = None,
        namespace: str = None,
        sparse_index_field: str = None,
        sparse_value_field: str = None,
        vector_field: str = None,
        vector_index_type: str = None,
    ):
        # The configurations of the index schema.
        self.advance_params = advance_params
        # The dimension of the vector.
        self.dimension = dimension
        # The distance type.
        self.distance_type = distance_type
        # The name of the index schema.
        self.index_name = index_name
        # The namespace field.
        self.namespace = namespace
        # The field that stores the indexes of the elements in sparse vectors.
        self.sparse_index_field = sparse_index_field
        # The field that stores the elements in sparse vectors.
        self.sparse_value_field = sparse_value_field
        # The vector field.
        self.vector_field = vector_field
        # The vector retrieval algorithm.
        self.vector_index_type = vector_index_type

    def validate(self):
        if self.advance_params:
            self.advance_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advance_params is not None:
            result['advanceParams'] = self.advance_params.to_map()
        if self.dimension is not None:
            result['dimension'] = self.dimension
        if self.distance_type is not None:
            result['distanceType'] = self.distance_type
        if self.index_name is not None:
            result['indexName'] = self.index_name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.sparse_index_field is not None:
            result['sparseIndexField'] = self.sparse_index_field
        if self.sparse_value_field is not None:
            result['sparseValueField'] = self.sparse_value_field
        if self.vector_field is not None:
            result['vectorField'] = self.vector_field
        if self.vector_index_type is not None:
            result['vectorIndexType'] = self.vector_index_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('advanceParams') is not None:
            temp_model = CreateTableRequestVectorIndexAdvanceParams()
            self.advance_params = temp_model.from_map(m['advanceParams'])
        if m.get('dimension') is not None:
            self.dimension = m.get('dimension')
        if m.get('distanceType') is not None:
            self.distance_type = m.get('distanceType')
        if m.get('indexName') is not None:
            self.index_name = m.get('indexName')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('sparseIndexField') is not None:
            self.sparse_index_field = m.get('sparseIndexField')
        if m.get('sparseValueField') is not None:
            self.sparse_value_field = m.get('sparseValueField')
        if m.get('vectorField') is not None:
            self.vector_field = m.get('vectorField')
        if m.get('vectorIndexType') is not None:
            self.vector_index_type = m.get('vectorIndexType')
        return self


class CreateTableRequest(TeaModel):
    def __init__(
        self,
        data_process_config: List[CreateTableRequestDataProcessConfig] = None,
        data_processor_count: int = None,
        data_source: CreateTableRequestDataSource = None,
        field_schema: Dict[str, str] = None,
        name: str = None,
        partition_count: int = None,
        primary_key: str = None,
        raw_schema: str = None,
        vector_index: List[CreateTableRequestVectorIndex] = None,
        dry_run: bool = None,
    ):
        # The configurations about field processing.
        self.data_process_config = data_process_config
        # The number of resources used for data update.
        self.data_processor_count = data_processor_count
        # The configurations of the data source.
        self.data_source = data_source
        # The fields.
        self.field_schema = field_schema
        # The index name.
        self.name = name
        # The number of data shards.
        self.partition_count = partition_count
        # The primary key field.
        self.primary_key = primary_key
        # The instance schema. If this parameter is specified, the parameters about the index are not required.
        self.raw_schema = raw_schema
        # The index schema.
        self.vector_index = vector_index
        # Specifies whether to perform only a dry run, without performing the actual request. The system only checks the validity of the data source. Valid values:
        # 
        # *   true
        # *   false
        self.dry_run = dry_run

    def validate(self):
        if self.data_process_config:
            for k in self.data_process_config:
                if k:
                    k.validate()
        if self.data_source:
            self.data_source.validate()
        if self.vector_index:
            for k in self.vector_index:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['dataProcessConfig'] = []
        if self.data_process_config is not None:
            for k in self.data_process_config:
                result['dataProcessConfig'].append(k.to_map() if k else None)
        if self.data_processor_count is not None:
            result['dataProcessorCount'] = self.data_processor_count
        if self.data_source is not None:
            result['dataSource'] = self.data_source.to_map()
        if self.field_schema is not None:
            result['fieldSchema'] = self.field_schema
        if self.name is not None:
            result['name'] = self.name
        if self.partition_count is not None:
            result['partitionCount'] = self.partition_count
        if self.primary_key is not None:
            result['primaryKey'] = self.primary_key
        if self.raw_schema is not None:
            result['rawSchema'] = self.raw_schema
        result['vectorIndex'] = []
        if self.vector_index is not None:
            for k in self.vector_index:
                result['vectorIndex'].append(k.to_map() if k else None)
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_process_config = []
        if m.get('dataProcessConfig') is not None:
            for k in m.get('dataProcessConfig'):
                temp_model = CreateTableRequestDataProcessConfig()
                self.data_process_config.append(temp_model.from_map(k))
        if m.get('dataProcessorCount') is not None:
            self.data_processor_count = m.get('dataProcessorCount')
        if m.get('dataSource') is not None:
            temp_model = CreateTableRequestDataSource()
            self.data_source = temp_model.from_map(m['dataSource'])
        if m.get('fieldSchema') is not None:
            self.field_schema = m.get('fieldSchema')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('partitionCount') is not None:
            self.partition_count = m.get('partitionCount')
        if m.get('primaryKey') is not None:
            self.primary_key = m.get('primaryKey')
        if m.get('rawSchema') is not None:
            self.raw_schema = m.get('rawSchema')
        self.vector_index = []
        if m.get('vectorIndex') is not None:
            for k in m.get('vectorIndex'):
                temp_model = CreateTableRequestVectorIndex()
                self.vector_index.append(temp_model.from_map(k))
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class CreateTableResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # id of request
        self.request_id = request_id
        # Map
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class CreateTableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTableResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAdvanceConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The result.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class DeleteAdvanceConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAdvanceConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteAdvanceConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAliasResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # id of request
        self.request_id = request_id
        # Map
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class DeleteAliasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAliasResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteAliasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteConfigDirRequest(TeaModel):
    def __init__(
        self,
        dir_name: str = None,
        parent_full_path: str = None,
    ):
        # The directory name.
        # 
        # This parameter is required.
        self.dir_name = dir_name
        # The path of the parent directory.
        # 
        # This parameter is required.
        self.parent_full_path = parent_full_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dir_name is not None:
            result['dirName'] = self.dir_name
        if self.parent_full_path is not None:
            result['parentFullPath'] = self.parent_full_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dirName') is not None:
            self.dir_name = m.get('dirName')
        if m.get('parentFullPath') is not None:
            self.parent_full_path = m.get('parentFullPath')
        return self


class DeleteConfigDirResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The result.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class DeleteConfigDirResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteConfigDirResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteConfigDirResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteConfigFileRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        parent_full_path: str = None,
    ):
        # The file name.
        # 
        # This parameter is required.
        self.file_name = file_name
        # The path of the parent directory.
        # 
        # This parameter is required.
        self.parent_full_path = parent_full_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.parent_full_path is not None:
            result['parentFullPath'] = self.parent_full_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('parentFullPath') is not None:
            self.parent_full_path = m.get('parentFullPath')
        return self


class DeleteConfigFileResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The result.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class DeleteConfigFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteConfigFileResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteConfigFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDataSourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The ID of the request
        self.request_id = request_id
        # The result returned
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class DeleteDataSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDataSourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteDataSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFolderResponseBodyResult(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, str] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The result
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class DeleteFolderResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DeleteFolderResponseBodyResult = None,
    ):
        # id of request
        self.request_id = request_id
        # Response<Map<String, String>>
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = DeleteFolderResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class DeleteFolderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteFolderResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteFolderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIndexRequest(TeaModel):
    def __init__(
        self,
        data_source: str = None,
        delete_data_source: bool = None,
    ):
        # The data source.
        # 
        # This parameter is required.
        self.data_source = data_source
        # Specifies whether to delete the data source.
        self.delete_data_source = delete_data_source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source is not None:
            result['dataSource'] = self.data_source
        if self.delete_data_source is not None:
            result['deleteDataSource'] = self.delete_data_source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataSource') is not None:
            self.data_source = m.get('dataSource')
        if m.get('deleteDataSource') is not None:
            self.delete_data_source = m.get('deleteDataSource')
        return self


class DeleteIndexResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # id of request
        self.request_id = request_id
        # The information about the index
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class DeleteIndexResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteIndexResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteIndexResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIndexVersionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # id of request
        self.request_id = request_id
        # The result
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class DeleteIndexVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteIndexVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteIndexVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The ID of the request
        self.request_id = request_id
        # The result returned
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class DeleteInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePublicUrlResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The result.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class DeletePublicUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeletePublicUrlResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeletePublicUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSqlInstanceResponseBodyResult(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, str] = None,
    ):
        # id of request
        self.request_id = request_id
        # The result.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class DeleteSqlInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DeleteSqlInstanceResponseBodyResult = None,
    ):
        # id of request
        self.request_id = request_id
        # Response<Map<String, String>>
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = DeleteSqlInstanceResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class DeleteSqlInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSqlInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteSqlInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTableResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # requestId
        self.request_id = request_id
        # Map
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class DeleteTableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteTableResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
    ):
        # The language of the response. Default value: zh-cn.
        self.accept_language = accept_language

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['acceptLanguage'] = self.accept_language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acceptLanguage') is not None:
            self.accept_language = m.get('acceptLanguage')
        return self


class DescribeRegionsResponseBodyResult(TeaModel):
    def __init__(
        self,
        endpoint: str = None,
        local_name: str = None,
        region_id: str = None,
    ):
        # The endpoint of the region.
        self.endpoint = endpoint
        # The name of the region.
        self.local_name = local_name
        # The ID of the region. Valid values:
        # 
        # cn-hangzhou: China (Hangzhou)
        # 
        # cn-shanghai: China (Shanghai)
        # 
        # cn-qingdao: China (Qingdao)
        # 
        # cn-beijing: China (Beijing)
        # 
        # cn-zhangjiakou: China (Zhangjiakou)
        # 
        # cn-shenzhen: China (Shenzhen)
        # 
        # ap-southeast-1: Singapore (Singapore)
        # 
        # cn-internal: Internal Center
        # 
        # cn-zhangbei-in: Internal Center (Zhangjiakou)
        # 
        # us-west-1-in: Internal Center (US)
        # 
        # rus-west-1-in: Internal Center (Russia)
        # 
        # cn-daily: Daily Environment
        # 
        # cn-test: Joint Debugging
        # 
        # pre-hangzhou: China (Hangzhou)-Staging
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.local_name is not None:
            result['localName'] = self.local_name
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('localName') is not None:
            self.local_name = m.get('localName')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[DescribeRegionsResponseBodyResult] = None,
    ):
        # id of request
        self.request_id = request_id
        # The result.
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = DescribeRegionsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRegionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteSqlInstanceRequest(TeaModel):
    def __init__(
        self,
        combine_param: Dict[str, Any] = None,
        content: str = None,
        domain: str = None,
        dynamic_param: Dict[str, Any] = None,
        kvpair: Dict[str, Any] = None,
        params: Dict[str, Any] = None,
        static_param: Dict[str, Any] = None,
    ):
        self.combine_param = combine_param
        # This parameter is required.
        self.content = content
        self.domain = domain
        self.dynamic_param = dynamic_param
        self.kvpair = kvpair
        self.params = params
        self.static_param = static_param

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.combine_param is not None:
            result['combineParam'] = self.combine_param
        if self.content is not None:
            result['content'] = self.content
        if self.domain is not None:
            result['domain'] = self.domain
        if self.dynamic_param is not None:
            result['dynamicParam'] = self.dynamic_param
        if self.kvpair is not None:
            result['kvpair'] = self.kvpair
        if self.params is not None:
            result['params'] = self.params
        if self.static_param is not None:
            result['staticParam'] = self.static_param
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('combineParam') is not None:
            self.combine_param = m.get('combineParam')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('dynamicParam') is not None:
            self.dynamic_param = m.get('dynamicParam')
        if m.get('kvpair') is not None:
            self.kvpair = m.get('kvpair')
        if m.get('params') is not None:
            self.params = m.get('params')
        if m.get('staticParam') is not None:
            self.static_param = m.get('staticParam')
        return self


class ExecuteSqlInstanceResponseBodyResult(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        instance_id: int = None,
        is_dir: int = None,
        name: str = None,
        parent: int = None,
        template_id: int = None,
        type: str = None,
    ):
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.instance_id = instance_id
        self.is_dir = is_dir
        self.name = name
        self.parent = parent
        self.template_id = template_id
        # table, instance, template, function
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.is_dir is not None:
            result['isDir'] = self.is_dir
        if self.name is not None:
            result['name'] = self.name
        if self.parent is not None:
            result['parent'] = self.parent
        if self.template_id is not None:
            result['templateId'] = self.template_id
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('isDir') is not None:
            self.is_dir = m.get('isDir')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parent') is not None:
            self.parent = m.get('parent')
        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ExecuteSqlInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ExecuteSqlInstanceResponseBodyResult = None,
    ):
        # id of request
        self.request_id = request_id
        # NodeVO
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = ExecuteSqlInstanceResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class ExecuteSqlInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExecuteSqlInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ExecuteSqlInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ForceSwitchResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The index information.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ForceSwitchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ForceSwitchResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ForceSwitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAdvanceConfigRequest(TeaModel):
    def __init__(
        self,
        type: str = None,
    ):
        # *   The type of the advanced configuration. Valid values: -ONLINE: online configuration
        # *   \\-ONLINE_CAVA: online Cava configuration
        # *   \\-ONLINE_PLUGIN: online plug-in configuration
        # *   \\-ONLINE_QUERY: query configuration
        # *   \\-OFFLINE_DICT: offline dictionary configuration
        # *   \\-OFFLINE_TABLE: offline table configuration
        # *   \\-OFFLINE_COMMON: offline configuration
        # *   \\-OFFLINE_PLUGIN: offline plug-in configuration
        # *   \\-OFFLINE_INDEX: index configuration
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetAdvanceConfigResponseBodyResultFiles(TeaModel):
    def __init__(
        self,
        full_path_name: str = None,
        is_dir: bool = None,
        is_template: bool = None,
        name: str = None,
    ):
        # The file path.
        self.full_path_name = full_path_name
        # Indicates whether the file is a directory.
        self.is_dir = is_dir
        # Indicates whether the file is a container.
        self.is_template = is_template
        # The file name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.full_path_name is not None:
            result['fullPathName'] = self.full_path_name
        if self.is_dir is not None:
            result['isDir'] = self.is_dir
        if self.is_template is not None:
            result['isTemplate'] = self.is_template
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fullPathName') is not None:
            self.full_path_name = m.get('fullPathName')
        if m.get('isDir') is not None:
            self.is_dir = m.get('isDir')
        if m.get('isTemplate') is not None:
            self.is_template = m.get('isTemplate')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class GetAdvanceConfigResponseBodyResult(TeaModel):
    def __init__(
        self,
        content: str = None,
        content_type: str = None,
        desc: str = None,
        files: List[GetAdvanceConfigResponseBodyResultFiles] = None,
        name: str = None,
        status: str = None,
        update_time: int = None,
    ):
        # The content of the advanced configuration that is returned.
        self.content = content
        # The type of the configuration content. Valid values: FILE, GIT, HTTP, and ODPS.
        self.content_type = content_type
        # The description of the advanced configuration.
        self.desc = desc
        # The files.
        self.files = files
        # The name of the advanced configuration.
        self.name = name
        # The status of the advanced configuration. Valid values: drafting: The advanced configuration is in the draft state. used: The advanced configuration is being used. unused: The advanced configuration is not used. trash: The advanced configuration is being deleted.
        self.status = status
        # The time when the advanced configuration was updated.
        self.update_time = update_time

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.content_type is not None:
            result['contentType'] = self.content_type
        if self.desc is not None:
            result['desc'] = self.desc
        result['files'] = []
        if self.files is not None:
            for k in self.files:
                result['files'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        self.files = []
        if m.get('files') is not None:
            for k in m.get('files'):
                temp_model = GetAdvanceConfigResponseBodyResultFiles()
                self.files.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class GetAdvanceConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: GetAdvanceConfigResponseBodyResult = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The result.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = GetAdvanceConfigResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class GetAdvanceConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAdvanceConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAdvanceConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAdvanceConfigFileRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
    ):
        # The name of the file
        # 
        # This parameter is required.
        self.file_name = file_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['fileName'] = self.file_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        return self


class GetAdvanceConfigFileResponseBodyResult(TeaModel):
    def __init__(
        self,
        content: str = None,
    ):
        # The file content.
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        return self


class GetAdvanceConfigFileResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: GetAdvanceConfigFileResponseBodyResult = None,
    ):
        # id of request
        self.request_id = request_id
        # The result.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = GetAdvanceConfigFileResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class GetAdvanceConfigFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAdvanceConfigFileResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAdvanceConfigFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetClusterResponseBodyResultDataNode(TeaModel):
    def __init__(
        self,
        name: str = None,
        number: int = None,
        partition: int = None,
    ):
        # The name of the Searcher worker.
        self.name = name
        # The number of replicas.
        self.number = number
        # The number of partitions.
        self.partition = partition

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.number is not None:
            result['number'] = self.number
        if self.partition is not None:
            result['partition'] = self.partition
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('number') is not None:
            self.number = m.get('number')
        if m.get('partition') is not None:
            self.partition = m.get('partition')
        return self


class GetClusterResponseBodyResultQueryNode(TeaModel):
    def __init__(
        self,
        name: str = None,
        number: int = None,
        partition: int = None,
    ):
        # The name of the QRS worker.
        self.name = name
        # The number of nodes.
        self.number = number
        # The number of replicas.
        self.partition = partition

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.number is not None:
            result['number'] = self.number
        if self.partition is not None:
            result['partition'] = self.partition
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('number') is not None:
            self.number = m.get('number')
        if m.get('partition') is not None:
            self.partition = m.get('partition')
        return self


class GetClusterResponseBodyResult(TeaModel):
    def __init__(
        self,
        config: Dict[str, dict] = None,
        config_update_time: str = None,
        create_time: str = None,
        current_advance_config_version: str = None,
        current_online_config_version: str = None,
        data_node: GetClusterResponseBodyResultDataNode = None,
        description: str = None,
        latest_advance_config_version: str = None,
        latest_online_config_version: str = None,
        name: str = None,
        query_node: GetClusterResponseBodyResultQueryNode = None,
        status: str = None,
    ):
        # The configuration information.
        self.config = config
        # The time when the cluster was updated.
        self.config_update_time = config_update_time
        # The time when the cluster was created.
        self.create_time = create_time
        # The effective advanced configuration version.
        self.current_advance_config_version = current_advance_config_version
        # The effective online configuration version.
        self.current_online_config_version = current_online_config_version
        # The specifications of Searcher workers.
        self.data_node = data_node
        # The description of the cluster.
        self.description = description
        # The latest advanced configuration version.
        self.latest_advance_config_version = latest_advance_config_version
        # The latest online configuration version.
        self.latest_online_config_version = latest_online_config_version
        # The cluster name.
        self.name = name
        # The specifications of Query Result Searcher (QRS) workers.
        self.query_node = query_node
        # The creation status of the cluster. Valid values: NEW and PUBLISH. NEW indicates that the cluster is being created. PUBLISH indicates that the cluster is created.
        self.status = status

    def validate(self):
        if self.data_node:
            self.data_node.validate()
        if self.query_node:
            self.query_node.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['config'] = self.config
        if self.config_update_time is not None:
            result['configUpdateTime'] = self.config_update_time
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.current_advance_config_version is not None:
            result['currentAdvanceConfigVersion'] = self.current_advance_config_version
        if self.current_online_config_version is not None:
            result['currentOnlineConfigVersion'] = self.current_online_config_version
        if self.data_node is not None:
            result['dataNode'] = self.data_node.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.latest_advance_config_version is not None:
            result['latestAdvanceConfigVersion'] = self.latest_advance_config_version
        if self.latest_online_config_version is not None:
            result['latestOnlineConfigVersion'] = self.latest_online_config_version
        if self.name is not None:
            result['name'] = self.name
        if self.query_node is not None:
            result['queryNode'] = self.query_node.to_map()
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            self.config = m.get('config')
        if m.get('configUpdateTime') is not None:
            self.config_update_time = m.get('configUpdateTime')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('currentAdvanceConfigVersion') is not None:
            self.current_advance_config_version = m.get('currentAdvanceConfigVersion')
        if m.get('currentOnlineConfigVersion') is not None:
            self.current_online_config_version = m.get('currentOnlineConfigVersion')
        if m.get('dataNode') is not None:
            temp_model = GetClusterResponseBodyResultDataNode()
            self.data_node = temp_model.from_map(m['dataNode'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('latestAdvanceConfigVersion') is not None:
            self.latest_advance_config_version = m.get('latestAdvanceConfigVersion')
        if m.get('latestOnlineConfigVersion') is not None:
            self.latest_online_config_version = m.get('latestOnlineConfigVersion')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('queryNode') is not None:
            temp_model = GetClusterResponseBodyResultQueryNode()
            self.query_node = temp_model.from_map(m['queryNode'])
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetClusterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: GetClusterResponseBodyResult = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The clusters.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = GetClusterResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class GetClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetClusterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetClusterRunTimeInfoResponseBodyResultDataNodesConfigStatusList(TeaModel):
    def __init__(
        self,
        config_update_time: str = None,
        done_percent: int = None,
        done_size: int = None,
        name: str = None,
        total_size: int = None,
    ):
        # The time when the configuration was last updated.
        self.config_update_time = config_update_time
        # The configuration progress. Unit: percentage.
        self.done_percent = done_percent
        # The number of processed Searcher workers in the cluster.
        self.done_size = done_size
        # The cluster name.
        self.name = name
        # The total number of Searcher workers in the cluster.
        self.total_size = total_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_update_time is not None:
            result['configUpdateTime'] = self.config_update_time
        if self.done_percent is not None:
            result['donePercent'] = self.done_percent
        if self.done_size is not None:
            result['doneSize'] = self.done_size
        if self.name is not None:
            result['name'] = self.name
        if self.total_size is not None:
            result['totalSize'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configUpdateTime') is not None:
            self.config_update_time = m.get('configUpdateTime')
        if m.get('donePercent') is not None:
            self.done_percent = m.get('donePercent')
        if m.get('doneSize') is not None:
            self.done_size = m.get('doneSize')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
        return self


class GetClusterRunTimeInfoResponseBodyResultDataNodesDataStatusListAdvanceConfigInfo(TeaModel):
    def __init__(
        self,
        config_meta_name: str = None,
        version: int = None,
    ):
        # The name of the index configuration.
        self.config_meta_name = config_meta_name
        # The version number.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_meta_name is not None:
            result['configMetaName'] = self.config_meta_name
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configMetaName') is not None:
            self.config_meta_name = m.get('configMetaName')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetClusterRunTimeInfoResponseBodyResultDataNodesDataStatusListIndexConfigInfo(TeaModel):
    def __init__(
        self,
        config_meta_name: str = None,
        version: int = None,
    ):
        # The name of the index configuration.
        self.config_meta_name = config_meta_name
        # The version of the index template.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_meta_name is not None:
            result['configMetaName'] = self.config_meta_name
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configMetaName') is not None:
            self.config_meta_name = m.get('configMetaName')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetClusterRunTimeInfoResponseBodyResultDataNodesDataStatusList(TeaModel):
    def __init__(
        self,
        advance_config_info: GetClusterRunTimeInfoResponseBodyResultDataNodesDataStatusListAdvanceConfigInfo = None,
        deploy_failed_worker: List[str] = None,
        doc_size: int = None,
        done_percent: int = None,
        done_size: int = None,
        error_msg: str = None,
        full_update_time: str = None,
        full_version: int = None,
        inc_update_time: str = None,
        inc_version: int = None,
        index_config_info: GetClusterRunTimeInfoResponseBodyResultDataNodesDataStatusListIndexConfigInfo = None,
        index_size: int = None,
        lack_disk_worker: List[str] = None,
        lack_mem_worker: List[str] = None,
        name: str = None,
        total_size: int = None,
    ):
        # The information about the advanced configuration.
        self.advance_config_info = advance_config_info
        # The name of the worker that failed due to a deployment failure.
        self.deploy_failed_worker = deploy_failed_worker
        # The storage capacity. Unit: GB.
        self.doc_size = doc_size
        # The configuration progress. Unit: percentage.
        self.done_percent = done_percent
        # The number of processed QRS workers in the cluster.
        self.done_size = done_size
        # The error message.
        self.error_msg = error_msg
        # The time when full data in the index was last updated.
        self.full_update_time = full_update_time
        # The time when the full index version was generated.
        self.full_version = full_version
        # The time when incremental data in the index was last updated.
        self.inc_update_time = inc_update_time
        # The time when the incremental index version was generated.
        self.inc_version = inc_version
        # The information about the index configuration.
        self.index_config_info = index_config_info
        # The index size.
        self.index_size = index_size
        # The name of the worker that failed due to insufficient disks.
        self.lack_disk_worker = lack_disk_worker
        # The name of the worker that failed due to insufficient memory.
        self.lack_mem_worker = lack_mem_worker
        # The name of the QRS worker.
        self.name = name
        # The total number of QRS workers in the cluster.
        self.total_size = total_size

    def validate(self):
        if self.advance_config_info:
            self.advance_config_info.validate()
        if self.index_config_info:
            self.index_config_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advance_config_info is not None:
            result['advanceConfigInfo'] = self.advance_config_info.to_map()
        if self.deploy_failed_worker is not None:
            result['deployFailedWorker'] = self.deploy_failed_worker
        if self.doc_size is not None:
            result['docSize'] = self.doc_size
        if self.done_percent is not None:
            result['donePercent'] = self.done_percent
        if self.done_size is not None:
            result['doneSize'] = self.done_size
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.full_update_time is not None:
            result['fullUpdateTime'] = self.full_update_time
        if self.full_version is not None:
            result['fullVersion'] = self.full_version
        if self.inc_update_time is not None:
            result['incUpdateTime'] = self.inc_update_time
        if self.inc_version is not None:
            result['incVersion'] = self.inc_version
        if self.index_config_info is not None:
            result['indexConfigInfo'] = self.index_config_info.to_map()
        if self.index_size is not None:
            result['indexSize'] = self.index_size
        if self.lack_disk_worker is not None:
            result['lackDiskWorker'] = self.lack_disk_worker
        if self.lack_mem_worker is not None:
            result['lackMemWorker'] = self.lack_mem_worker
        if self.name is not None:
            result['name'] = self.name
        if self.total_size is not None:
            result['totalSize'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('advanceConfigInfo') is not None:
            temp_model = GetClusterRunTimeInfoResponseBodyResultDataNodesDataStatusListAdvanceConfigInfo()
            self.advance_config_info = temp_model.from_map(m['advanceConfigInfo'])
        if m.get('deployFailedWorker') is not None:
            self.deploy_failed_worker = m.get('deployFailedWorker')
        if m.get('docSize') is not None:
            self.doc_size = m.get('docSize')
        if m.get('donePercent') is not None:
            self.done_percent = m.get('donePercent')
        if m.get('doneSize') is not None:
            self.done_size = m.get('doneSize')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('fullUpdateTime') is not None:
            self.full_update_time = m.get('fullUpdateTime')
        if m.get('fullVersion') is not None:
            self.full_version = m.get('fullVersion')
        if m.get('incUpdateTime') is not None:
            self.inc_update_time = m.get('incUpdateTime')
        if m.get('incVersion') is not None:
            self.inc_version = m.get('incVersion')
        if m.get('indexConfigInfo') is not None:
            temp_model = GetClusterRunTimeInfoResponseBodyResultDataNodesDataStatusListIndexConfigInfo()
            self.index_config_info = temp_model.from_map(m['indexConfigInfo'])
        if m.get('indexSize') is not None:
            self.index_size = m.get('indexSize')
        if m.get('lackDiskWorker') is not None:
            self.lack_disk_worker = m.get('lackDiskWorker')
        if m.get('lackMemWorker') is not None:
            self.lack_mem_worker = m.get('lackMemWorker')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
        return self


class GetClusterRunTimeInfoResponseBodyResultDataNodesServiceStatus(TeaModel):
    def __init__(
        self,
        done_percent: int = None,
        done_size: int = None,
        name: str = None,
        total_size: int = None,
    ):
        # The process progress of QRS workers in the cluster. Unit: percentage.
        self.done_percent = done_percent
        # The number of processed QRS workers in the cluster.
        self.done_size = done_size
        # The name of the QRS worker.
        self.name = name
        # The total number of QRS workers in the cluster.
        self.total_size = total_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.done_percent is not None:
            result['donePercent'] = self.done_percent
        if self.done_size is not None:
            result['doneSize'] = self.done_size
        if self.name is not None:
            result['name'] = self.name
        if self.total_size is not None:
            result['totalSize'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('donePercent') is not None:
            self.done_percent = m.get('donePercent')
        if m.get('doneSize') is not None:
            self.done_size = m.get('doneSize')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
        return self


class GetClusterRunTimeInfoResponseBodyResultDataNodes(TeaModel):
    def __init__(
        self,
        config_status_list: List[GetClusterRunTimeInfoResponseBodyResultDataNodesConfigStatusList] = None,
        data_status_list: List[GetClusterRunTimeInfoResponseBodyResultDataNodesDataStatusList] = None,
        service_status: GetClusterRunTimeInfoResponseBodyResultDataNodesServiceStatus = None,
    ):
        # The configuration status.
        self.config_status_list = config_status_list
        # The data of the Searcher worker.
        self.data_status_list = data_status_list
        # The service status of the QRS worker.
        self.service_status = service_status

    def validate(self):
        if self.config_status_list:
            for k in self.config_status_list:
                if k:
                    k.validate()
        if self.data_status_list:
            for k in self.data_status_list:
                if k:
                    k.validate()
        if self.service_status:
            self.service_status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['configStatusList'] = []
        if self.config_status_list is not None:
            for k in self.config_status_list:
                result['configStatusList'].append(k.to_map() if k else None)
        result['dataStatusList'] = []
        if self.data_status_list is not None:
            for k in self.data_status_list:
                result['dataStatusList'].append(k.to_map() if k else None)
        if self.service_status is not None:
            result['serviceStatus'] = self.service_status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_status_list = []
        if m.get('configStatusList') is not None:
            for k in m.get('configStatusList'):
                temp_model = GetClusterRunTimeInfoResponseBodyResultDataNodesConfigStatusList()
                self.config_status_list.append(temp_model.from_map(k))
        self.data_status_list = []
        if m.get('dataStatusList') is not None:
            for k in m.get('dataStatusList'):
                temp_model = GetClusterRunTimeInfoResponseBodyResultDataNodesDataStatusList()
                self.data_status_list.append(temp_model.from_map(k))
        if m.get('serviceStatus') is not None:
            temp_model = GetClusterRunTimeInfoResponseBodyResultDataNodesServiceStatus()
            self.service_status = temp_model.from_map(m['serviceStatus'])
        return self


class GetClusterRunTimeInfoResponseBodyResultQueryNodeConfigStatusList(TeaModel):
    def __init__(
        self,
        config_update_time: str = None,
        done_percent: int = None,
        done_size: int = None,
        name: str = None,
        total_size: int = None,
    ):
        # The time when the configuration was last updated.
        self.config_update_time = config_update_time
        # The process progress of QRS workers in the cluster. Unit: percentage.
        self.done_percent = done_percent
        # The number of processed QRS workers in the cluster.
        self.done_size = done_size
        # The cluster name.
        self.name = name
        # The total number of QRS workers in the cluster.
        self.total_size = total_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_update_time is not None:
            result['configUpdateTime'] = self.config_update_time
        if self.done_percent is not None:
            result['donePercent'] = self.done_percent
        if self.done_size is not None:
            result['doneSize'] = self.done_size
        if self.name is not None:
            result['name'] = self.name
        if self.total_size is not None:
            result['totalSize'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configUpdateTime') is not None:
            self.config_update_time = m.get('configUpdateTime')
        if m.get('donePercent') is not None:
            self.done_percent = m.get('donePercent')
        if m.get('doneSize') is not None:
            self.done_size = m.get('doneSize')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
        return self


class GetClusterRunTimeInfoResponseBodyResultQueryNodeServiceStatus(TeaModel):
    def __init__(
        self,
        done_percent: int = None,
        done_size: int = None,
        name: str = None,
        total_size: int = None,
    ):
        # The process progress of QRS workers in the cluster. Unit: percentage.
        self.done_percent = done_percent
        # The number of processed QRS workers in the cluster.
        self.done_size = done_size
        # The cluster name.
        self.name = name
        # The total number of QRS workers in the cluster.
        self.total_size = total_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.done_percent is not None:
            result['donePercent'] = self.done_percent
        if self.done_size is not None:
            result['doneSize'] = self.done_size
        if self.name is not None:
            result['name'] = self.name
        if self.total_size is not None:
            result['totalSize'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('donePercent') is not None:
            self.done_percent = m.get('donePercent')
        if m.get('doneSize') is not None:
            self.done_size = m.get('doneSize')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
        return self


class GetClusterRunTimeInfoResponseBodyResultQueryNode(TeaModel):
    def __init__(
        self,
        config_status_list: List[GetClusterRunTimeInfoResponseBodyResultQueryNodeConfigStatusList] = None,
        service_status: GetClusterRunTimeInfoResponseBodyResultQueryNodeServiceStatus = None,
    ):
        # The configuration status.
        self.config_status_list = config_status_list
        # The service status of the QRS worker.
        self.service_status = service_status

    def validate(self):
        if self.config_status_list:
            for k in self.config_status_list:
                if k:
                    k.validate()
        if self.service_status:
            self.service_status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['configStatusList'] = []
        if self.config_status_list is not None:
            for k in self.config_status_list:
                result['configStatusList'].append(k.to_map() if k else None)
        if self.service_status is not None:
            result['serviceStatus'] = self.service_status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_status_list = []
        if m.get('configStatusList') is not None:
            for k in m.get('configStatusList'):
                temp_model = GetClusterRunTimeInfoResponseBodyResultQueryNodeConfigStatusList()
                self.config_status_list.append(temp_model.from_map(k))
        if m.get('serviceStatus') is not None:
            temp_model = GetClusterRunTimeInfoResponseBodyResultQueryNodeServiceStatus()
            self.service_status = temp_model.from_map(m['serviceStatus'])
        return self


class GetClusterRunTimeInfoResponseBodyResult(TeaModel):
    def __init__(
        self,
        cluster_name: str = None,
        data_nodes: List[GetClusterRunTimeInfoResponseBodyResultDataNodes] = None,
        query_node: GetClusterRunTimeInfoResponseBodyResultQueryNode = None,
    ):
        # The cluster name.
        self.cluster_name = cluster_name
        # The information about the Searcher workers.
        self.data_nodes = data_nodes
        # The information about the Query Result Searcher (QRS) workers.
        self.query_node = query_node

    def validate(self):
        if self.data_nodes:
            for k in self.data_nodes:
                if k:
                    k.validate()
        if self.query_node:
            self.query_node.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_name is not None:
            result['clusterName'] = self.cluster_name
        result['dataNodes'] = []
        if self.data_nodes is not None:
            for k in self.data_nodes:
                result['dataNodes'].append(k.to_map() if k else None)
        if self.query_node is not None:
            result['queryNode'] = self.query_node.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        self.data_nodes = []
        if m.get('dataNodes') is not None:
            for k in m.get('dataNodes'):
                temp_model = GetClusterRunTimeInfoResponseBodyResultDataNodes()
                self.data_nodes.append(temp_model.from_map(k))
        if m.get('queryNode') is not None:
            temp_model = GetClusterRunTimeInfoResponseBodyResultQueryNode()
            self.query_node = temp_model.from_map(m['queryNode'])
        return self


class GetClusterRunTimeInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[GetClusterRunTimeInfoResponseBodyResult] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The result.
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = GetClusterRunTimeInfoResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class GetClusterRunTimeInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetClusterRunTimeInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetClusterRunTimeInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDataSourceResponseBodyResult(TeaModel):
    def __init__(
        self,
        domain: str = None,
        indexes: List[str] = None,
        last_ful_time: int = None,
        name: str = None,
        status: str = None,
        type: str = None,
    ):
        # The data center where the data source is deployed in offline mode
        self.domain = domain
        # The list of index information
        self.indexes = indexes
        # The time when the full data of the data source was last queried.
        self.last_ful_time = last_ful_time
        # The name of the data source.
        self.name = name
        # The status of the data source. Valid values: new: The data source is being created. publish: The data source is in the normal state. trash: The data source is being deleted.
        self.status = status
        # The type of the data source
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.indexes is not None:
            result['indexes'] = self.indexes
        if self.last_ful_time is not None:
            result['lastFulTime'] = self.last_ful_time
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('indexes') is not None:
            self.indexes = m.get('indexes')
        if m.get('lastFulTime') is not None:
            self.last_ful_time = m.get('lastFulTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetDataSourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: GetDataSourceResponseBodyResult = None,
    ):
        # Id of the request
        self.request_id = request_id
        # The information about the data source.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = GetDataSourceResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class GetDataSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDataSourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDataSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDataSourceDeployResponseBodyResultExtendHdfs(TeaModel):
    def __init__(
        self,
        path: str = None,
    ):
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('path') is not None:
            self.path = m.get('path')
        return self


class GetDataSourceDeployResponseBodyResultExtendOdps(TeaModel):
    def __init__(
        self,
        partitions: Dict[str, str] = None,
    ):
        self.partitions = partitions

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.partitions is not None:
            result['partitions'] = self.partitions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('partitions') is not None:
            self.partitions = m.get('partitions')
        return self


class GetDataSourceDeployResponseBodyResultExtendOss(TeaModel):
    def __init__(
        self,
        path: str = None,
    ):
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('path') is not None:
            self.path = m.get('path')
        return self


class GetDataSourceDeployResponseBodyResultExtendSaro(TeaModel):
    def __init__(
        self,
        path: str = None,
        version: str = None,
    ):
        self.path = path
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['path'] = self.path
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetDataSourceDeployResponseBodyResultExtend(TeaModel):
    def __init__(
        self,
        hdfs: GetDataSourceDeployResponseBodyResultExtendHdfs = None,
        odps: GetDataSourceDeployResponseBodyResultExtendOdps = None,
        oss: GetDataSourceDeployResponseBodyResultExtendOss = None,
        saro: GetDataSourceDeployResponseBodyResultExtendSaro = None,
    ):
        self.hdfs = hdfs
        self.odps = odps
        self.oss = oss
        self.saro = saro

    def validate(self):
        if self.hdfs:
            self.hdfs.validate()
        if self.odps:
            self.odps.validate()
        if self.oss:
            self.oss.validate()
        if self.saro:
            self.saro.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hdfs is not None:
            result['hdfs'] = self.hdfs.to_map()
        if self.odps is not None:
            result['odps'] = self.odps.to_map()
        if self.oss is not None:
            result['oss'] = self.oss.to_map()
        if self.saro is not None:
            result['saro'] = self.saro.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hdfs') is not None:
            temp_model = GetDataSourceDeployResponseBodyResultExtendHdfs()
            self.hdfs = temp_model.from_map(m['hdfs'])
        if m.get('odps') is not None:
            temp_model = GetDataSourceDeployResponseBodyResultExtendOdps()
            self.odps = temp_model.from_map(m['odps'])
        if m.get('oss') is not None:
            temp_model = GetDataSourceDeployResponseBodyResultExtendOss()
            self.oss = temp_model.from_map(m['oss'])
        if m.get('saro') is not None:
            temp_model = GetDataSourceDeployResponseBodyResultExtendSaro()
            self.saro = temp_model.from_map(m['saro'])
        return self


class GetDataSourceDeployResponseBodyResultProcessor(TeaModel):
    def __init__(
        self,
        args: str = None,
        resource: str = None,
    ):
        # The startup parameters of the process.
        self.args = args
        # The resource information.
        self.resource = resource

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.args is not None:
            result['args'] = self.args
        if self.resource is not None:
            result['resource'] = self.resource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('args') is not None:
            self.args = m.get('args')
        if m.get('resource') is not None:
            self.resource = m.get('resource')
        return self


class GetDataSourceDeployResponseBodyResultStorage(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        access_secret: str = None,
        bucket: str = None,
        endpoint: str = None,
        namespace: str = None,
        oss_path: str = None,
        partition: str = None,
        path: str = None,
        project: str = None,
        table: str = None,
    ):
        # The AccessKey ID of the MaxCompute data source.
        self.access_key = access_key
        # The AccessKey secret of the MaxCompute data source.
        self.access_secret = access_secret
        # The name of the OSS bucket.
        self.bucket = bucket
        # The endpoint of the MaxCompute data source.
        self.endpoint = endpoint
        self.namespace = namespace
        # The Object Storage Service (OSS) path.
        self.oss_path = oss_path
        # The partition in the MaxCompute table. Example: ds=20180102.
        self.partition = partition
        self.path = path
        self.project = project
        self.table = table

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.access_secret is not None:
            result['accessSecret'] = self.access_secret
        if self.bucket is not None:
            result['bucket'] = self.bucket
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.oss_path is not None:
            result['ossPath'] = self.oss_path
        if self.partition is not None:
            result['partition'] = self.partition
        if self.path is not None:
            result['path'] = self.path
        if self.project is not None:
            result['project'] = self.project
        if self.table is not None:
            result['table'] = self.table
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('accessSecret') is not None:
            self.access_secret = m.get('accessSecret')
        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('ossPath') is not None:
            self.oss_path = m.get('ossPath')
        if m.get('partition') is not None:
            self.partition = m.get('partition')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('table') is not None:
            self.table = m.get('table')
        return self


class GetDataSourceDeployResponseBodyResultSwift(TeaModel):
    def __init__(
        self,
        topic: str = None,
        zk: str = None,
    ):
        # The topic.
        self.topic = topic
        # zk
        self.zk = zk

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.topic is not None:
            result['topic'] = self.topic
        if self.zk is not None:
            result['zk'] = self.zk
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('topic') is not None:
            self.topic = m.get('topic')
        if m.get('zk') is not None:
            self.zk = m.get('zk')
        return self


class GetDataSourceDeployResponseBodyResult(TeaModel):
    def __init__(
        self,
        auto_build_index: bool = None,
        extend: GetDataSourceDeployResponseBodyResultExtend = None,
        processor: GetDataSourceDeployResponseBodyResultProcessor = None,
        storage: GetDataSourceDeployResponseBodyResultStorage = None,
        swift: GetDataSourceDeployResponseBodyResultSwift = None,
    ):
        self.auto_build_index = auto_build_index
        self.extend = extend
        # The parameters of the process.
        self.processor = processor
        # The information about the data source.
        self.storage = storage
        # The information about the incremental data source Swift.
        self.swift = swift

    def validate(self):
        if self.extend:
            self.extend.validate()
        if self.processor:
            self.processor.validate()
        if self.storage:
            self.storage.validate()
        if self.swift:
            self.swift.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_build_index is not None:
            result['autoBuildIndex'] = self.auto_build_index
        if self.extend is not None:
            result['extend'] = self.extend.to_map()
        if self.processor is not None:
            result['processor'] = self.processor.to_map()
        if self.storage is not None:
            result['storage'] = self.storage.to_map()
        if self.swift is not None:
            result['swift'] = self.swift.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoBuildIndex') is not None:
            self.auto_build_index = m.get('autoBuildIndex')
        if m.get('extend') is not None:
            temp_model = GetDataSourceDeployResponseBodyResultExtend()
            self.extend = temp_model.from_map(m['extend'])
        if m.get('processor') is not None:
            temp_model = GetDataSourceDeployResponseBodyResultProcessor()
            self.processor = temp_model.from_map(m['processor'])
        if m.get('storage') is not None:
            temp_model = GetDataSourceDeployResponseBodyResultStorage()
            self.storage = temp_model.from_map(m['storage'])
        if m.get('swift') is not None:
            temp_model = GetDataSourceDeployResponseBodyResultSwift()
            self.swift = temp_model.from_map(m['swift'])
        return self


class GetDataSourceDeployResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: GetDataSourceDeployResponseBodyResult = None,
    ):
        # requestId
        self.request_id = request_id
        # The result.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = GetDataSourceDeployResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class GetDataSourceDeployResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDataSourceDeployResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDataSourceDeployResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDatabaseSchemaResponseBodyResult(TeaModel):
    def __init__(
        self,
        field_name: str = None,
        field_type: str = None,
        field_type_detail: Dict[str, Any] = None,
        index_name: str = None,
        index_type: str = None,
    ):
        self.field_name = field_name
        self.field_type = field_type
        self.field_type_detail = field_type_detail
        self.index_name = index_name
        self.index_type = index_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_name is not None:
            result['fieldName'] = self.field_name
        if self.field_type is not None:
            result['fieldType'] = self.field_type
        if self.field_type_detail is not None:
            result['fieldTypeDetail'] = self.field_type_detail
        if self.index_name is not None:
            result['indexName'] = self.index_name
        if self.index_type is not None:
            result['indexType'] = self.index_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fieldName') is not None:
            self.field_name = m.get('fieldName')
        if m.get('fieldType') is not None:
            self.field_type = m.get('fieldType')
        if m.get('fieldTypeDetail') is not None:
            self.field_type_detail = m.get('fieldTypeDetail')
        if m.get('indexName') is not None:
            self.index_name = m.get('indexName')
        if m.get('indexType') is not None:
            self.index_type = m.get('indexType')
        return self


class GetDatabaseSchemaResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[GetDatabaseSchemaResponseBodyResult] = None,
    ):
        # id of request
        self.request_id = request_id
        # List
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = GetDatabaseSchemaResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class GetDatabaseSchemaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDatabaseSchemaResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDatabaseSchemaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDeployGraphResponseBodyResultGraphIndexMetas(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        name: str = None,
        table_deploy_id: int = None,
        table_name: str = None,
        tag: str = None,
        zone_name: str = None,
    ):
        # The name of the data center.
        self.domain_name = domain_name
        # The index name.
        self.name = name
        # The deployment ID of the table.
        self.table_deploy_id = table_deploy_id
        # The name of the data source.
        self.table_name = table_name
        # The tag.
        self.tag = tag
        # The name of the QRS worker.
        self.zone_name = zone_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
        if self.name is not None:
            result['name'] = self.name
        if self.table_deploy_id is not None:
            result['tableDeployId'] = self.table_deploy_id
        if self.table_name is not None:
            result['tableName'] = self.table_name
        if self.tag is not None:
            result['tag'] = self.tag
        if self.zone_name is not None:
            result['zoneName'] = self.zone_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('tableDeployId') is not None:
            self.table_deploy_id = m.get('tableDeployId')
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        return self


class GetDeployGraphResponseBodyResultGraphOnlineMaster(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        hippo_id: str = None,
        id: int = None,
        name: str = None,
    ):
        # The name of the data center.
        self.domain_name = domain_name
        # The resource ID.
        self.hippo_id = hippo_id
        # The ID of the data center.
        self.id = id
        # The name of the online cluster.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
        if self.hippo_id is not None:
            result['hippoId'] = self.hippo_id
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        if m.get('hippoId') is not None:
            self.hippo_id = m.get('hippoId')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class GetDeployGraphResponseBodyResultGraphTableMetas(TeaModel):
    def __init__(
        self,
        build_deploy_id: int = None,
        domain_name: str = None,
        name: str = None,
        table_deploy_id: int = None,
        tag: str = None,
        type: str = None,
    ):
        # The ID of the offline deployment.
        self.build_deploy_id = build_deploy_id
        # The name of the data center.
        self.domain_name = domain_name
        # The name of the data source.
        self.name = name
        # The deployment ID of the table.
        self.table_deploy_id = table_deploy_id
        # The tag.
        self.tag = tag
        # The type of the data source.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_deploy_id is not None:
            result['buildDeployId'] = self.build_deploy_id
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
        if self.name is not None:
            result['name'] = self.name
        if self.table_deploy_id is not None:
            result['tableDeployId'] = self.table_deploy_id
        if self.tag is not None:
            result['tag'] = self.tag
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('buildDeployId') is not None:
            self.build_deploy_id = m.get('buildDeployId')
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('tableDeployId') is not None:
            self.table_deploy_id = m.get('tableDeployId')
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetDeployGraphResponseBodyResultGraphZoneMetas(TeaModel):
    def __init__(
        self,
        domain_info: str = None,
        name: str = None,
        suez_admin_name: str = None,
        tag: str = None,
        type: str = None,
    ):
        # The name of the data center.
        self.domain_info = domain_info
        # The name of the Query Result Searcher (QRS) worker.
        self.name = name
        # The name of the service that is used to manage the relationships between online clusters and indexes.
        self.suez_admin_name = suez_admin_name
        # The tag.
        self.tag = tag
        # The node type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_info is not None:
            result['domainInfo'] = self.domain_info
        if self.name is not None:
            result['name'] = self.name
        if self.suez_admin_name is not None:
            result['suezAdminName'] = self.suez_admin_name
        if self.tag is not None:
            result['tag'] = self.tag
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainInfo') is not None:
            self.domain_info = m.get('domainInfo')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('suezAdminName') is not None:
            self.suez_admin_name = m.get('suezAdminName')
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetDeployGraphResponseBodyResultGraph(TeaModel):
    def __init__(
        self,
        index_metas: List[GetDeployGraphResponseBodyResultGraphIndexMetas] = None,
        online_master: List[GetDeployGraphResponseBodyResultGraphOnlineMaster] = None,
        table_index_relation: Dict[str, List[str]] = None,
        table_metas: List[GetDeployGraphResponseBodyResultGraphTableMetas] = None,
        zone_index_relation: Dict[str, List[str]] = None,
        zone_metas: List[GetDeployGraphResponseBodyResultGraphZoneMetas] = None,
    ):
        # The index metadata.
        self.index_metas = index_metas
        # The metadata of online clusters.
        self.online_master = online_master
        # The association relationships between data sources and indexes.
        self.table_index_relation = table_index_relation
        # The metadata of data sources.
        self.table_metas = table_metas
        # The association relationships between zones and indexes.
        self.zone_index_relation = zone_index_relation
        # The zone metadata.
        self.zone_metas = zone_metas

    def validate(self):
        if self.index_metas:
            for k in self.index_metas:
                if k:
                    k.validate()
        if self.online_master:
            for k in self.online_master:
                if k:
                    k.validate()
        if self.table_metas:
            for k in self.table_metas:
                if k:
                    k.validate()
        if self.zone_metas:
            for k in self.zone_metas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['indexMetas'] = []
        if self.index_metas is not None:
            for k in self.index_metas:
                result['indexMetas'].append(k.to_map() if k else None)
        result['onlineMaster'] = []
        if self.online_master is not None:
            for k in self.online_master:
                result['onlineMaster'].append(k.to_map() if k else None)
        if self.table_index_relation is not None:
            result['tableIndexRelation'] = self.table_index_relation
        result['tableMetas'] = []
        if self.table_metas is not None:
            for k in self.table_metas:
                result['tableMetas'].append(k.to_map() if k else None)
        if self.zone_index_relation is not None:
            result['zoneIndexRelation'] = self.zone_index_relation
        result['zoneMetas'] = []
        if self.zone_metas is not None:
            for k in self.zone_metas:
                result['zoneMetas'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.index_metas = []
        if m.get('indexMetas') is not None:
            for k in m.get('indexMetas'):
                temp_model = GetDeployGraphResponseBodyResultGraphIndexMetas()
                self.index_metas.append(temp_model.from_map(k))
        self.online_master = []
        if m.get('onlineMaster') is not None:
            for k in m.get('onlineMaster'):
                temp_model = GetDeployGraphResponseBodyResultGraphOnlineMaster()
                self.online_master.append(temp_model.from_map(k))
        if m.get('tableIndexRelation') is not None:
            self.table_index_relation = m.get('tableIndexRelation')
        self.table_metas = []
        if m.get('tableMetas') is not None:
            for k in m.get('tableMetas'):
                temp_model = GetDeployGraphResponseBodyResultGraphTableMetas()
                self.table_metas.append(temp_model.from_map(k))
        if m.get('zoneIndexRelation') is not None:
            self.zone_index_relation = m.get('zoneIndexRelation')
        self.zone_metas = []
        if m.get('zoneMetas') is not None:
            for k in m.get('zoneMetas'):
                temp_model = GetDeployGraphResponseBodyResultGraphZoneMetas()
                self.zone_metas.append(temp_model.from_map(k))
        return self


class GetDeployGraphResponseBodyResult(TeaModel):
    def __init__(
        self,
        graph: GetDeployGraphResponseBodyResultGraph = None,
    ):
        # The deployment information.
        self.graph = graph

    def validate(self):
        if self.graph:
            self.graph.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.graph is not None:
            result['graph'] = self.graph.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('graph') is not None:
            temp_model = GetDeployGraphResponseBodyResultGraph()
            self.graph = temp_model.from_map(m['graph'])
        return self


class GetDeployGraphResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: GetDeployGraphResponseBodyResult = None,
    ):
        # Id of the request
        self.request_id = request_id
        # The results returned.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = GetDeployGraphResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class GetDeployGraphResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDeployGraphResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDeployGraphResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFileRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
    ):
        # The name of the file in full path
        # 
        # This parameter is required.
        self.file_name = file_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['fileName'] = self.file_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        return self


class GetFileResponseBodyResult(TeaModel):
    def __init__(
        self,
        content: str = None,
        data_source: str = None,
        extend: Dict[str, List[str]] = None,
        full_path_name: str = None,
        is_dir: bool = None,
        name: str = None,
        partition: int = None,
    ):
        # The file content.
        self.content = content
        # The data source.
        self.data_source = data_source
        self.extend = extend
        # The full path of the file.
        self.full_path_name = full_path_name
        # Indicates whether the file is a directory.
        self.is_dir = is_dir
        # The file name.
        self.name = name
        # The number of shards.
        self.partition = partition

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.data_source is not None:
            result['dataSource'] = self.data_source
        if self.extend is not None:
            result['extend'] = self.extend
        if self.full_path_name is not None:
            result['fullPathName'] = self.full_path_name
        if self.is_dir is not None:
            result['isDir'] = self.is_dir
        if self.name is not None:
            result['name'] = self.name
        if self.partition is not None:
            result['partition'] = self.partition
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('dataSource') is not None:
            self.data_source = m.get('dataSource')
        if m.get('extend') is not None:
            self.extend = m.get('extend')
        if m.get('fullPathName') is not None:
            self.full_path_name = m.get('fullPathName')
        if m.get('isDir') is not None:
            self.is_dir = m.get('isDir')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('partition') is not None:
            self.partition = m.get('partition')
        return self


class GetFileResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: GetFileResponseBodyResult = None,
    ):
        # id of request
        self.request_id = request_id
        # The index information.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = GetFileResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class GetFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFileResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetIndexResponseBodyResultDataSourceInfoConfig(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        access_secret: str = None,
        bucket: str = None,
        endpoint: str = None,
        namespace: str = None,
        oss_path: str = None,
        partition: str = None,
        path: str = None,
        project: str = None,
        table: str = None,
    ):
        # The AccessKey ID of the MaxCompute data source.
        self.access_key = access_key
        # The AccessKey secret of the MaxCompute data source.
        self.access_secret = access_secret
        # The name of the OSS bucket.
        self.bucket = bucket
        # The endpoint of the MaxCompute data source.
        self.endpoint = endpoint
        # The namespace. This parameter is applicable to the SARO data source used in the intranet of Alibaba Group.
        self.namespace = namespace
        # The Object Storage Service (OSS) path.
        self.oss_path = oss_path
        # The partition in the MaxCompute table. Example: ds=20180102.
        self.partition = partition
        # The file path in the Apsara File Storage for HDFS file system.
        self.path = path
        # The name of the MaxCompute project that is used as the data source.
        self.project = project
        # The name of the MaxCompute table that is used as the data source.
        self.table = table

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.access_secret is not None:
            result['accessSecret'] = self.access_secret
        if self.bucket is not None:
            result['bucket'] = self.bucket
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.oss_path is not None:
            result['ossPath'] = self.oss_path
        if self.partition is not None:
            result['partition'] = self.partition
        if self.path is not None:
            result['path'] = self.path
        if self.project is not None:
            result['project'] = self.project
        if self.table is not None:
            result['table'] = self.table
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('accessSecret') is not None:
            self.access_secret = m.get('accessSecret')
        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('ossPath') is not None:
            self.oss_path = m.get('ossPath')
        if m.get('partition') is not None:
            self.partition = m.get('partition')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('table') is not None:
            self.table = m.get('table')
        return self


class GetIndexResponseBodyResultDataSourceInfoSaroConfig(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        table_name: str = None,
    ):
        # The namespace of the SARO data source.
        self.namespace = namespace
        # The name of the SARO table.
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.table_name is not None:
            result['tableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        return self


class GetIndexResponseBodyResultDataSourceInfo(TeaModel):
    def __init__(
        self,
        auto_build_index: bool = None,
        config: GetIndexResponseBodyResultDataSourceInfoConfig = None,
        domain: str = None,
        name: str = None,
        process_parallel_num: int = None,
        process_partition_count: int = None,
        saro_config: GetIndexResponseBodyResultDataSourceInfoSaroConfig = None,
        type: str = None,
    ):
        # Indicates whether the automatic full indexing feature is enabled.
        self.auto_build_index = auto_build_index
        # The configuration of MaxCompute data sources.
        self.config = config
        # The data center in which the data source is deployed.
        self.domain = domain
        # The name of the data source.
        self.name = name
        # The maximum number of full indexes that can be concurrently processed.
        self.process_parallel_num = process_parallel_num
        # The number of resources used for data update.
        self.process_partition_count = process_partition_count
        # The configurations of the SARO data source.
        self.saro_config = saro_config
        # The type of the data source. Valid values: odps, swift, saro, oss, and unKnow.
        self.type = type

    def validate(self):
        if self.config:
            self.config.validate()
        if self.saro_config:
            self.saro_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_build_index is not None:
            result['autoBuildIndex'] = self.auto_build_index
        if self.config is not None:
            result['config'] = self.config.to_map()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.name is not None:
            result['name'] = self.name
        if self.process_parallel_num is not None:
            result['processParallelNum'] = self.process_parallel_num
        if self.process_partition_count is not None:
            result['processPartitionCount'] = self.process_partition_count
        if self.saro_config is not None:
            result['saroConfig'] = self.saro_config.to_map()
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoBuildIndex') is not None:
            self.auto_build_index = m.get('autoBuildIndex')
        if m.get('config') is not None:
            temp_model = GetIndexResponseBodyResultDataSourceInfoConfig()
            self.config = temp_model.from_map(m['config'])
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('processParallelNum') is not None:
            self.process_parallel_num = m.get('processParallelNum')
        if m.get('processPartitionCount') is not None:
            self.process_partition_count = m.get('processPartitionCount')
        if m.get('saroConfig') is not None:
            temp_model = GetIndexResponseBodyResultDataSourceInfoSaroConfig()
            self.saro_config = temp_model.from_map(m['saroConfig'])
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetIndexResponseBodyResultVersionsFiles(TeaModel):
    def __init__(
        self,
        full_path_name: str = None,
        is_dir: bool = None,
        is_template: bool = None,
        name: str = None,
    ):
        # The full path of the file.
        self.full_path_name = full_path_name
        # Indicates whether the file is a directory.
        self.is_dir = is_dir
        # Indicates whether the file is a template.
        self.is_template = is_template
        # The file name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.full_path_name is not None:
            result['fullPathName'] = self.full_path_name
        if self.is_dir is not None:
            result['isDir'] = self.is_dir
        if self.is_template is not None:
            result['isTemplate'] = self.is_template
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fullPathName') is not None:
            self.full_path_name = m.get('fullPathName')
        if m.get('isDir') is not None:
            self.is_dir = m.get('isDir')
        if m.get('isTemplate') is not None:
            self.is_template = m.get('isTemplate')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class GetIndexResponseBodyResultVersions(TeaModel):
    def __init__(
        self,
        desc: str = None,
        files: List[GetIndexResponseBodyResultVersionsFiles] = None,
        name: str = None,
        status: str = None,
        update_time: int = None,
        version_id: int = None,
    ):
        # The description of the version.
        self.desc = desc
        # The information about the files.
        self.files = files
        # The version name.
        self.name = name
        # The status of the index version. Valid values:
        # 
        # *   NEW: The index version is created.
        # *   PUBLISH: The index version is normal.
        # *   IN_USE: The index version is in use.
        # *   NOT_USE: The index version is not used.
        # *   STOP_USE: The index version is being stopped.
        # *   RESTORE_USE: The index version is being restored.
        # *   FAIL: The index version failed to be created.
        self.status = status
        # The time when the index version was updated.
        self.update_time = update_time
        # The version ID.
        self.version_id = version_id

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['desc'] = self.desc
        result['files'] = []
        if self.files is not None:
            for k in self.files:
                result['files'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.version_id is not None:
            result['versionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        self.files = []
        if m.get('files') is not None:
            for k in m.get('files'):
                temp_model = GetIndexResponseBodyResultVersionsFiles()
                self.files.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        return self


class GetIndexResponseBodyResult(TeaModel):
    def __init__(
        self,
        cluster: Dict[str, ResultClusterValue] = None,
        config: Dict[str, dict] = None,
        config_when_build: Dict[str, dict] = None,
        content: str = None,
        data_source: str = None,
        data_source_info: GetIndexResponseBodyResultDataSourceInfo = None,
        description: str = None,
        domain: str = None,
        extend: Dict[str, List[str]] = None,
        full_update_time: str = None,
        full_version: int = None,
        inc_update_time: str = None,
        index_size: int = None,
        index_status: str = None,
        name: str = None,
        partition: int = None,
        versions: List[GetIndexResponseBodyResultVersions] = None,
    ):
        # The cluster information.
        self.cluster = cluster
        # The configuration information.
        self.config = config
        # The configuration that takes effect next time.
        self.config_when_build = config_when_build
        # The file content.
        self.content = content
        # The name of the data source.
        self.data_source = data_source
        # The information about the data source.
        self.data_source_info = data_source_info
        # The description of the index version.
        self.description = description
        # The deployment name of the index.
        self.domain = domain
        self.extend = extend
        # The time when full data in the index was last updated.
        self.full_update_time = full_update_time
        # The data version.
        self.full_version = full_version
        # The time when incremental data in the index was last updated.
        self.inc_update_time = inc_update_time
        # The index size.
        self.index_size = index_size
        # The status of the index version. Valid values:
        # 
        # *   NEW: The index version is created.
        # *   PUBLISH: The index version is normal.
        # *   IN_USE: The index version is in use.
        # *   NOT_USE: The index version is not used.
        # *   STOP_USE: The index version is being stopped.
        # *   RESTORE_USE: The index version is being restored.
        # *   FAIL: The index version failed to be created.
        self.index_status = index_status
        # The index name.
        self.name = name
        # The number of shards.
        self.partition = partition
        # The information about the versions.
        self.versions = versions

    def validate(self):
        if self.cluster:
            for v in self.cluster.values():
                if v:
                    v.validate()
        if self.data_source_info:
            self.data_source_info.validate()
        if self.versions:
            for k in self.versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['cluster'] = {}
        if self.cluster is not None:
            for k, v in self.cluster.items():
                result['cluster'][k] = v.to_map()
        if self.config is not None:
            result['config'] = self.config
        if self.config_when_build is not None:
            result['configWhenBuild'] = self.config_when_build
        if self.content is not None:
            result['content'] = self.content
        if self.data_source is not None:
            result['dataSource'] = self.data_source
        if self.data_source_info is not None:
            result['dataSourceInfo'] = self.data_source_info.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.domain is not None:
            result['domain'] = self.domain
        if self.extend is not None:
            result['extend'] = self.extend
        if self.full_update_time is not None:
            result['fullUpdateTime'] = self.full_update_time
        if self.full_version is not None:
            result['fullVersion'] = self.full_version
        if self.inc_update_time is not None:
            result['incUpdateTime'] = self.inc_update_time
        if self.index_size is not None:
            result['indexSize'] = self.index_size
        if self.index_status is not None:
            result['indexStatus'] = self.index_status
        if self.name is not None:
            result['name'] = self.name
        if self.partition is not None:
            result['partition'] = self.partition
        result['versions'] = []
        if self.versions is not None:
            for k in self.versions:
                result['versions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cluster = {}
        if m.get('cluster') is not None:
            for k, v in m.get('cluster').items():
                temp_model = ResultClusterValue()
                self.cluster[k] = temp_model.from_map(v)
        if m.get('config') is not None:
            self.config = m.get('config')
        if m.get('configWhenBuild') is not None:
            self.config_when_build = m.get('configWhenBuild')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('dataSource') is not None:
            self.data_source = m.get('dataSource')
        if m.get('dataSourceInfo') is not None:
            temp_model = GetIndexResponseBodyResultDataSourceInfo()
            self.data_source_info = temp_model.from_map(m['dataSourceInfo'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('extend') is not None:
            self.extend = m.get('extend')
        if m.get('fullUpdateTime') is not None:
            self.full_update_time = m.get('fullUpdateTime')
        if m.get('fullVersion') is not None:
            self.full_version = m.get('fullVersion')
        if m.get('incUpdateTime') is not None:
            self.inc_update_time = m.get('incUpdateTime')
        if m.get('indexSize') is not None:
            self.index_size = m.get('indexSize')
        if m.get('indexStatus') is not None:
            self.index_status = m.get('indexStatus')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('partition') is not None:
            self.partition = m.get('partition')
        self.versions = []
        if m.get('versions') is not None:
            for k in m.get('versions'):
                temp_model = GetIndexResponseBodyResultVersions()
                self.versions.append(temp_model.from_map(k))
        return self


class GetIndexResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: GetIndexResponseBodyResult = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The index information.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = GetIndexResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class GetIndexResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetIndexResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetIndexResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetIndexOnlineStrategyResponseBodyResult(TeaModel):
    def __init__(
        self,
        change_rate: int = None,
    ):
        # The index change rate.
        self.change_rate = change_rate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_rate is not None:
            result['changeRate'] = self.change_rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('changeRate') is not None:
            self.change_rate = m.get('changeRate')
        return self


class GetIndexOnlineStrategyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: GetIndexOnlineStrategyResponseBodyResult = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The result.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = GetIndexOnlineStrategyResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class GetIndexOnlineStrategyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetIndexOnlineStrategyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetIndexOnlineStrategyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetIndexVersionResponseBodyResultIndexVersions(TeaModel):
    def __init__(
        self,
        build_deploy_id: str = None,
        current_version: int = None,
        index_name: str = None,
        versions: List[int] = None,
    ):
        # The ID of the offline deployment.
        self.build_deploy_id = build_deploy_id
        # The current online version number.
        self.current_version = current_version
        # The name of the index table.
        self.index_name = index_name
        # The index versions.
        self.versions = versions

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_deploy_id is not None:
            result['buildDeployId'] = self.build_deploy_id
        if self.current_version is not None:
            result['currentVersion'] = self.current_version
        if self.index_name is not None:
            result['indexName'] = self.index_name
        if self.versions is not None:
            result['versions'] = self.versions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('buildDeployId') is not None:
            self.build_deploy_id = m.get('buildDeployId')
        if m.get('currentVersion') is not None:
            self.current_version = m.get('currentVersion')
        if m.get('indexName') is not None:
            self.index_name = m.get('indexName')
        if m.get('versions') is not None:
            self.versions = m.get('versions')
        return self


class GetIndexVersionResponseBodyResult(TeaModel):
    def __init__(
        self,
        cluster: str = None,
        index_versions: List[GetIndexVersionResponseBodyResultIndexVersions] = None,
    ):
        # The cluster name.
        self.cluster = cluster
        # The index versions.
        self.index_versions = index_versions

    def validate(self):
        if self.index_versions:
            for k in self.index_versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster is not None:
            result['cluster'] = self.cluster
        result['indexVersions'] = []
        if self.index_versions is not None:
            for k in self.index_versions:
                result['indexVersions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        self.index_versions = []
        if m.get('indexVersions') is not None:
            for k in m.get('indexVersions'):
                temp_model = GetIndexVersionResponseBodyResultIndexVersions()
                self.index_versions.append(temp_model.from_map(k))
        return self


class GetIndexVersionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: GetIndexVersionResponseBodyResult = None,
    ):
        # id of request
        self.request_id = request_id
        # The clusters.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = GetIndexVersionResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class GetIndexVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetIndexVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetIndexVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceResponseBodyResultNetwork(TeaModel):
    def __init__(
        self,
        allow: str = None,
        endpoint: str = None,
        public_endpoint: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        self.allow = allow
        self.endpoint = endpoint
        self.public_endpoint = public_endpoint
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow is not None:
            result['allow'] = self.allow
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.public_endpoint is not None:
            result['publicEndpoint'] = self.public_endpoint
        if self.v_switch_id is not None:
            result['vSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allow') is not None:
            self.allow = m.get('allow')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('publicEndpoint') is not None:
            self.public_endpoint = m.get('publicEndpoint')
        if m.get('vSwitchId') is not None:
            self.v_switch_id = m.get('vSwitchId')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self


class GetInstanceResponseBodyResultSpecQrsResource(TeaModel):
    def __init__(
        self,
        category: str = None,
        cpu: int = None,
        disk: int = None,
        mem: int = None,
        node_count: int = None,
    ):
        self.category = category
        self.cpu = cpu
        self.disk = disk
        self.mem = mem
        self.node_count = node_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.cpu is not None:
            result['cpu'] = self.cpu
        if self.disk is not None:
            result['disk'] = self.disk
        if self.mem is not None:
            result['mem'] = self.mem
        if self.node_count is not None:
            result['nodeCount'] = self.node_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        if m.get('disk') is not None:
            self.disk = m.get('disk')
        if m.get('mem') is not None:
            self.mem = m.get('mem')
        if m.get('nodeCount') is not None:
            self.node_count = m.get('nodeCount')
        return self


class GetInstanceResponseBodyResultSpecSearchResource(TeaModel):
    def __init__(
        self,
        category: str = None,
        cpu: int = None,
        disk: int = None,
        mem: int = None,
        node_count: int = None,
    ):
        self.category = category
        self.cpu = cpu
        self.disk = disk
        self.mem = mem
        self.node_count = node_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.cpu is not None:
            result['cpu'] = self.cpu
        if self.disk is not None:
            result['disk'] = self.disk
        if self.mem is not None:
            result['mem'] = self.mem
        if self.node_count is not None:
            result['nodeCount'] = self.node_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        if m.get('disk') is not None:
            self.disk = m.get('disk')
        if m.get('mem') is not None:
            self.mem = m.get('mem')
        if m.get('nodeCount') is not None:
            self.node_count = m.get('nodeCount')
        return self


class GetInstanceResponseBodyResultSpec(TeaModel):
    def __init__(
        self,
        qrs_resource: GetInstanceResponseBodyResultSpecQrsResource = None,
        search_resource: GetInstanceResponseBodyResultSpecSearchResource = None,
    ):
        self.qrs_resource = qrs_resource
        self.search_resource = search_resource

    def validate(self):
        if self.qrs_resource:
            self.qrs_resource.validate()
        if self.search_resource:
            self.search_resource.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.qrs_resource is not None:
            result['qrsResource'] = self.qrs_resource.to_map()
        if self.search_resource is not None:
            result['searchResource'] = self.search_resource.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('qrsResource') is not None:
            temp_model = GetInstanceResponseBodyResultSpecQrsResource()
            self.qrs_resource = temp_model.from_map(m['qrsResource'])
        if m.get('searchResource') is not None:
            temp_model = GetInstanceResponseBodyResultSpecSearchResource()
            self.search_resource = temp_model.from_map(m['searchResource'])
        return self


class GetInstanceResponseBodyResultTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetInstanceResponseBodyResult(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        commodity_code: str = None,
        create_time: str = None,
        description: str = None,
        edition: str = None,
        expired_time: str = None,
        in_debt: bool = None,
        instance_id: str = None,
        lock_mode: str = None,
        network: GetInstanceResponseBodyResultNetwork = None,
        new_mode: bool = None,
        no_qrs: bool = None,
        resource_group_id: str = None,
        spec: GetInstanceResponseBodyResultSpec = None,
        status: str = None,
        tags: List[GetInstanceResponseBodyResultTags] = None,
        update_time: str = None,
        user_name: str = None,
        version: str = None,
    ):
        # The billing method.
        self.charge_type = charge_type
        # The commodity code of the instance.
        self.commodity_code = commodity_code
        # The time when the instance was created.
        self.create_time = create_time
        # The description of the instance.
        self.description = description
        self.edition = edition
        # The time when the instance expires.
        self.expired_time = expired_time
        # Indicates whether an overdue payment is involved.
        self.in_debt = in_debt
        # The instance ID.
        self.instance_id = instance_id
        # The lock status.
        self.lock_mode = lock_mode
        self.network = network
        self.new_mode = new_mode
        self.no_qrs = no_qrs
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.spec = spec
        # The status of the instance. Valid values:
        # 
        # *   INIT: being initialized
        # *   WAIT_CONFIG: to be configured
        # *   CONFIG_UPDATING: configuration taking effect
        # *   READY: normal
        self.status = status
        # The tags of the instance.
        self.tags = tags
        # The time when the instance was updated.
        self.update_time = update_time
        self.user_name = user_name
        self.version = version

    def validate(self):
        if self.network:
            self.network.validate()
        if self.spec:
            self.spec.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.edition is not None:
            result['edition'] = self.edition
        if self.expired_time is not None:
            result['expiredTime'] = self.expired_time
        if self.in_debt is not None:
            result['inDebt'] = self.in_debt
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.lock_mode is not None:
            result['lockMode'] = self.lock_mode
        if self.network is not None:
            result['network'] = self.network.to_map()
        if self.new_mode is not None:
            result['newMode'] = self.new_mode
        if self.no_qrs is not None:
            result['noQrs'] = self.no_qrs
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        if self.status is not None:
            result['status'] = self.status
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.user_name is not None:
            result['userName'] = self.user_name
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('edition') is not None:
            self.edition = m.get('edition')
        if m.get('expiredTime') is not None:
            self.expired_time = m.get('expiredTime')
        if m.get('inDebt') is not None:
            self.in_debt = m.get('inDebt')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('lockMode') is not None:
            self.lock_mode = m.get('lockMode')
        if m.get('network') is not None:
            temp_model = GetInstanceResponseBodyResultNetwork()
            self.network = temp_model.from_map(m['network'])
        if m.get('newMode') is not None:
            self.new_mode = m.get('newMode')
        if m.get('noQrs') is not None:
            self.no_qrs = m.get('noQrs')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('spec') is not None:
            temp_model = GetInstanceResponseBodyResultSpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('status') is not None:
            self.status = m.get('status')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = GetInstanceResponseBodyResultTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: GetInstanceResponseBodyResult = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The results returned.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = GetInstanceResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class GetInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNodeConfigRequest(TeaModel):
    def __init__(
        self,
        cluster_name: str = None,
        name: str = None,
        type: str = None,
    ):
        # The name of the cluster
        self.cluster_name = cluster_name
        # The node name.
        self.name = name
        # The node type. Valid values:
        # 
        # *   qrs: Query Result Searcher (QRS) worker
        # *   search: Search worker
        # *   index: index
        # *   cluster: cluster
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_name is not None:
            result['clusterName'] = self.cluster_name
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetNodeConfigResponseBodyResult(TeaModel):
    def __init__(
        self,
        active: bool = None,
        data_duplicate_number: int = None,
        data_fragment_number: int = None,
        flow_ratio: int = None,
        min_service_percent: int = None,
        published: bool = None,
    ):
        # Indicates whether the index is effective online.
        self.active = active
        # The number of data replicas.
        self.data_duplicate_number = data_duplicate_number
        # The number of data shards.
        self.data_fragment_number = data_fragment_number
        # The traffic percentage.
        self.flow_ratio = flow_ratio
        # The minimum service ratio.
        self.min_service_percent = min_service_percent
        # Indicates whether the cluster is mounted.
        self.published = published

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.data_duplicate_number is not None:
            result['dataDuplicateNumber'] = self.data_duplicate_number
        if self.data_fragment_number is not None:
            result['dataFragmentNumber'] = self.data_fragment_number
        if self.flow_ratio is not None:
            result['flowRatio'] = self.flow_ratio
        if self.min_service_percent is not None:
            result['minServicePercent'] = self.min_service_percent
        if self.published is not None:
            result['published'] = self.published
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('dataDuplicateNumber') is not None:
            self.data_duplicate_number = m.get('dataDuplicateNumber')
        if m.get('dataFragmentNumber') is not None:
            self.data_fragment_number = m.get('dataFragmentNumber')
        if m.get('flowRatio') is not None:
            self.flow_ratio = m.get('flowRatio')
        if m.get('minServicePercent') is not None:
            self.min_service_percent = m.get('minServicePercent')
        if m.get('published') is not None:
            self.published = m.get('published')
        return self


class GetNodeConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: GetNodeConfigResponseBodyResult = None,
    ):
        # Id of the request
        self.request_id = request_id
        # The result set.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = GetNodeConfigResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class GetNodeConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetNodeConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetNodeConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSqlInstanceRequest(TeaModel):
    def __init__(
        self,
        version: int = None,
    ):
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetSqlInstanceResponseBodyResult(TeaModel):
    def __init__(
        self,
        combine_params: str = None,
        comment: str = None,
        content: str = None,
        dynamic_params: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        instance_id: int = None,
        kvpairs: str = None,
        related_template_id: int = None,
        static_params: str = None,
        template_params: str = None,
        version: int = None,
    ):
        self.combine_params = combine_params
        self.comment = comment
        self.content = content
        self.dynamic_params = dynamic_params
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.instance_id = instance_id
        self.kvpairs = kvpairs
        self.related_template_id = related_template_id
        self.static_params = static_params
        self.template_params = template_params
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.combine_params is not None:
            result['combineParams'] = self.combine_params
        if self.comment is not None:
            result['comment'] = self.comment
        if self.content is not None:
            result['content'] = self.content
        if self.dynamic_params is not None:
            result['dynamicParams'] = self.dynamic_params
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.kvpairs is not None:
            result['kvpairs'] = self.kvpairs
        if self.related_template_id is not None:
            result['relatedTemplateId'] = self.related_template_id
        if self.static_params is not None:
            result['staticParams'] = self.static_params
        if self.template_params is not None:
            result['templateParams'] = self.template_params
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('combineParams') is not None:
            self.combine_params = m.get('combineParams')
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('dynamicParams') is not None:
            self.dynamic_params = m.get('dynamicParams')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('kvpairs') is not None:
            self.kvpairs = m.get('kvpairs')
        if m.get('relatedTemplateId') is not None:
            self.related_template_id = m.get('relatedTemplateId')
        if m.get('staticParams') is not None:
            self.static_params = m.get('staticParams')
        if m.get('templateParams') is not None:
            self.template_params = m.get('templateParams')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetSqlInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: GetSqlInstanceResponseBodyResult = None,
    ):
        # id of request
        self.request_id = request_id
        # InstanceVersionVO
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = GetSqlInstanceResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class GetSqlInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSqlInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetSqlInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTableResponseBodyResultDataProcessConfigParamsSrcFieldConfig(TeaModel):
    def __init__(
        self,
        oss_bucket: str = None,
        oss_endpoint: str = None,
        uid: str = None,
    ):
        # OSS Bucket
        self.oss_bucket = oss_bucket
        # The Object Storage Service (OSS) endpoint.
        self.oss_endpoint = oss_endpoint
        # The ID of the Alibaba Cloud account.
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss_bucket is not None:
            result['ossBucket'] = self.oss_bucket
        if self.oss_endpoint is not None:
            result['ossEndpoint'] = self.oss_endpoint
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ossBucket') is not None:
            self.oss_bucket = m.get('ossBucket')
        if m.get('ossEndpoint') is not None:
            self.oss_endpoint = m.get('ossEndpoint')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class GetTableResponseBodyResultDataProcessConfigParams(TeaModel):
    def __init__(
        self,
        src_field_config: GetTableResponseBodyResultDataProcessConfigParamsSrcFieldConfig = None,
        vector_modal: str = None,
        vector_model: str = None,
    ):
        # The source of the data to be vectorized.
        self.src_field_config = src_field_config
        # The data type.
        self.vector_modal = vector_modal
        # The vectorization model.
        self.vector_model = vector_model

    def validate(self):
        if self.src_field_config:
            self.src_field_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.src_field_config is not None:
            result['srcFieldConfig'] = self.src_field_config.to_map()
        if self.vector_modal is not None:
            result['vectorModal'] = self.vector_modal
        if self.vector_model is not None:
            result['vectorModel'] = self.vector_model
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('srcFieldConfig') is not None:
            temp_model = GetTableResponseBodyResultDataProcessConfigParamsSrcFieldConfig()
            self.src_field_config = temp_model.from_map(m['srcFieldConfig'])
        if m.get('vectorModal') is not None:
            self.vector_modal = m.get('vectorModal')
        if m.get('vectorModel') is not None:
            self.vector_model = m.get('vectorModel')
        return self


class GetTableResponseBodyResultDataProcessConfig(TeaModel):
    def __init__(
        self,
        dst_field: str = None,
        operator: str = None,
        params: GetTableResponseBodyResultDataProcessConfigParams = None,
        src_field: str = None,
    ):
        # The destination field.
        self.dst_field = dst_field
        # The method used to process the field. Valid values: copy and vectorize. A value of copy indicates that the value of the source field is copied to the destination field. A value of vectorize indicates that the value of the source field is vectorized by a vectorization model and the output vector is stored in the destination field.
        self.operator = operator
        # The information about the model.
        self.params = params
        # The source field.
        self.src_field = src_field

    def validate(self):
        if self.params:
            self.params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dst_field is not None:
            result['dstField'] = self.dst_field
        if self.operator is not None:
            result['operator'] = self.operator
        if self.params is not None:
            result['params'] = self.params.to_map()
        if self.src_field is not None:
            result['srcField'] = self.src_field
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dstField') is not None:
            self.dst_field = m.get('dstField')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('params') is not None:
            temp_model = GetTableResponseBodyResultDataProcessConfigParams()
            self.params = temp_model.from_map(m['params'])
        if m.get('srcField') is not None:
            self.src_field = m.get('srcField')
        return self


class GetTableResponseBodyResultDataSourceConfig(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        access_secret: str = None,
        bucket: str = None,
        endpoint: str = None,
        namespace: str = None,
        oss_path: str = None,
        partition: str = None,
        path: str = None,
        project: str = None,
        table: str = None,
    ):
        # AK
        self.access_key = access_key
        # AS
        self.access_secret = access_secret
        self.bucket = bucket
        self.endpoint = endpoint
        self.namespace = namespace
        self.oss_path = oss_path
        self.partition = partition
        self.path = path
        self.project = project
        self.table = table

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.access_secret is not None:
            result['accessSecret'] = self.access_secret
        if self.bucket is not None:
            result['bucket'] = self.bucket
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.oss_path is not None:
            result['ossPath'] = self.oss_path
        if self.partition is not None:
            result['partition'] = self.partition
        if self.path is not None:
            result['path'] = self.path
        if self.project is not None:
            result['project'] = self.project
        if self.table is not None:
            result['table'] = self.table
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('accessSecret') is not None:
            self.access_secret = m.get('accessSecret')
        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('ossPath') is not None:
            self.oss_path = m.get('ossPath')
        if m.get('partition') is not None:
            self.partition = m.get('partition')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('table') is not None:
            self.table = m.get('table')
        return self


class GetTableResponseBodyResultDataSource(TeaModel):
    def __init__(
        self,
        auto_build_index: bool = None,
        config: GetTableResponseBodyResultDataSourceConfig = None,
        data_time_sec: int = None,
        type: str = None,
    ):
        self.auto_build_index = auto_build_index
        self.config = config
        self.data_time_sec = data_time_sec
        self.type = type

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_build_index is not None:
            result['autoBuildIndex'] = self.auto_build_index
        if self.config is not None:
            result['config'] = self.config.to_map()
        if self.data_time_sec is not None:
            result['dataTimeSec'] = self.data_time_sec
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoBuildIndex') is not None:
            self.auto_build_index = m.get('autoBuildIndex')
        if m.get('config') is not None:
            temp_model = GetTableResponseBodyResultDataSourceConfig()
            self.config = temp_model.from_map(m['config'])
        if m.get('dataTimeSec') is not None:
            self.data_time_sec = m.get('dataTimeSec')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetTableResponseBodyResultVectorIndexAdvanceParams(TeaModel):
    def __init__(
        self,
        build_index_params: str = None,
        linear_build_threshold: str = None,
        min_scan_doc_cnt: str = None,
        search_index_params: str = None,
    ):
        # The index building parameters.
        self.build_index_params = build_index_params
        # The threshold for linear building.
        self.linear_build_threshold = linear_build_threshold
        # The minimum number of retrieved candidate sets.
        self.min_scan_doc_cnt = min_scan_doc_cnt
        # The index retrieval parameters.
        self.search_index_params = search_index_params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_index_params is not None:
            result['buildIndexParams'] = self.build_index_params
        if self.linear_build_threshold is not None:
            result['linearBuildThreshold'] = self.linear_build_threshold
        if self.min_scan_doc_cnt is not None:
            result['minScanDocCnt'] = self.min_scan_doc_cnt
        if self.search_index_params is not None:
            result['searchIndexParams'] = self.search_index_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('buildIndexParams') is not None:
            self.build_index_params = m.get('buildIndexParams')
        if m.get('linearBuildThreshold') is not None:
            self.linear_build_threshold = m.get('linearBuildThreshold')
        if m.get('minScanDocCnt') is not None:
            self.min_scan_doc_cnt = m.get('minScanDocCnt')
        if m.get('searchIndexParams') is not None:
            self.search_index_params = m.get('searchIndexParams')
        return self


class GetTableResponseBodyResultVectorIndex(TeaModel):
    def __init__(
        self,
        advance_params: GetTableResponseBodyResultVectorIndexAdvanceParams = None,
        dimension: str = None,
        distance_type: str = None,
        index_name: str = None,
        namespace: str = None,
        sparse_index_field: str = None,
        sparse_value_field: str = None,
        vector_field: str = None,
        vector_index_type: str = None,
    ):
        # The configurations of the index schema.
        self.advance_params = advance_params
        # The dimension of the vector.
        self.dimension = dimension
        # The distance type.
        self.distance_type = distance_type
        # The name of the index schema.
        self.index_name = index_name
        # The namespace field.
        self.namespace = namespace
        # The field that stores the indexes of the elements in sparse vectors.
        self.sparse_index_field = sparse_index_field
        # The field that stores the elements in sparse vectors.
        self.sparse_value_field = sparse_value_field
        # The vector field.
        self.vector_field = vector_field
        # The vector retrieval algorithm.
        self.vector_index_type = vector_index_type

    def validate(self):
        if self.advance_params:
            self.advance_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advance_params is not None:
            result['advanceParams'] = self.advance_params.to_map()
        if self.dimension is not None:
            result['dimension'] = self.dimension
        if self.distance_type is not None:
            result['distanceType'] = self.distance_type
        if self.index_name is not None:
            result['indexName'] = self.index_name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.sparse_index_field is not None:
            result['sparseIndexField'] = self.sparse_index_field
        if self.sparse_value_field is not None:
            result['sparseValueField'] = self.sparse_value_field
        if self.vector_field is not None:
            result['vectorField'] = self.vector_field
        if self.vector_index_type is not None:
            result['vectorIndexType'] = self.vector_index_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('advanceParams') is not None:
            temp_model = GetTableResponseBodyResultVectorIndexAdvanceParams()
            self.advance_params = temp_model.from_map(m['advanceParams'])
        if m.get('dimension') is not None:
            self.dimension = m.get('dimension')
        if m.get('distanceType') is not None:
            self.distance_type = m.get('distanceType')
        if m.get('indexName') is not None:
            self.index_name = m.get('indexName')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('sparseIndexField') is not None:
            self.sparse_index_field = m.get('sparseIndexField')
        if m.get('sparseValueField') is not None:
            self.sparse_value_field = m.get('sparseValueField')
        if m.get('vectorField') is not None:
            self.vector_field = m.get('vectorField')
        if m.get('vectorIndexType') is not None:
            self.vector_index_type = m.get('vectorIndexType')
        return self


class GetTableResponseBodyResult(TeaModel):
    def __init__(
        self,
        data_process_config: List[GetTableResponseBodyResultDataProcessConfig] = None,
        data_processor_count: int = None,
        data_source: GetTableResponseBodyResultDataSource = None,
        field_schema: Dict[str, str] = None,
        name: str = None,
        partition_count: int = None,
        primary_key: str = None,
        raw_schema: str = None,
        status: str = None,
        vector_index: List[GetTableResponseBodyResultVectorIndex] = None,
    ):
        # The configurations about field processing.
        self.data_process_config = data_process_config
        self.data_processor_count = data_processor_count
        self.data_source = data_source
        # The field. The value is a key-value pair in which the key indicates the field name and value indicates the field type.
        self.field_schema = field_schema
        self.name = name
        self.partition_count = partition_count
        self.primary_key = primary_key
        self.raw_schema = raw_schema
        # The state of the index table. Valid values: NEW, PUBLISH, IN_USE, NOT_USE, STOP_USE, RESTORE_USE, and FAIL. After an index is created in an OpenSearch Retrieval Engine Edition instance, the index enters the IN_USE state. If the first full index fails to be created in an OpenSearch Vector Search Edition instance of the new version, the index is in the FAIL state.
        self.status = status
        # The index schema.
        self.vector_index = vector_index

    def validate(self):
        if self.data_process_config:
            for k in self.data_process_config:
                if k:
                    k.validate()
        if self.data_source:
            self.data_source.validate()
        if self.vector_index:
            for k in self.vector_index:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['dataProcessConfig'] = []
        if self.data_process_config is not None:
            for k in self.data_process_config:
                result['dataProcessConfig'].append(k.to_map() if k else None)
        if self.data_processor_count is not None:
            result['dataProcessorCount'] = self.data_processor_count
        if self.data_source is not None:
            result['dataSource'] = self.data_source.to_map()
        if self.field_schema is not None:
            result['fieldSchema'] = self.field_schema
        if self.name is not None:
            result['name'] = self.name
        if self.partition_count is not None:
            result['partitionCount'] = self.partition_count
        if self.primary_key is not None:
            result['primaryKey'] = self.primary_key
        if self.raw_schema is not None:
            result['rawSchema'] = self.raw_schema
        if self.status is not None:
            result['status'] = self.status
        result['vectorIndex'] = []
        if self.vector_index is not None:
            for k in self.vector_index:
                result['vectorIndex'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_process_config = []
        if m.get('dataProcessConfig') is not None:
            for k in m.get('dataProcessConfig'):
                temp_model = GetTableResponseBodyResultDataProcessConfig()
                self.data_process_config.append(temp_model.from_map(k))
        if m.get('dataProcessorCount') is not None:
            self.data_processor_count = m.get('dataProcessorCount')
        if m.get('dataSource') is not None:
            temp_model = GetTableResponseBodyResultDataSource()
            self.data_source = temp_model.from_map(m['dataSource'])
        if m.get('fieldSchema') is not None:
            self.field_schema = m.get('fieldSchema')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('partitionCount') is not None:
            self.partition_count = m.get('partitionCount')
        if m.get('primaryKey') is not None:
            self.primary_key = m.get('primaryKey')
        if m.get('rawSchema') is not None:
            self.raw_schema = m.get('rawSchema')
        if m.get('status') is not None:
            self.status = m.get('status')
        self.vector_index = []
        if m.get('vectorIndex') is not None:
            for k in m.get('vectorIndex'):
                temp_model = GetTableResponseBodyResultVectorIndex()
                self.vector_index.append(temp_model.from_map(k))
        return self


class GetTableResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: GetTableResponseBodyResult = None,
    ):
        # requestId
        self.request_id = request_id
        # The results returned.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = GetTableResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class GetTableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTableResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTableGenerationResponseBodyResult(TeaModel):
    def __init__(
        self,
        generation_id: int = None,
        status: str = None,
    ):
        # generationId
        self.generation_id = generation_id
        # starting, building, ready, stopped, failed
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.generation_id is not None:
            result['generationId'] = self.generation_id
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('generationId') is not None:
            self.generation_id = m.get('generationId')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetTableGenerationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: GetTableGenerationResponseBodyResult = None,
    ):
        # requestId
        self.request_id = request_id
        # The result returned.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = GetTableGenerationResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class GetTableGenerationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTableGenerationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTableGenerationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAdvanceConfigDirRequest(TeaModel):
    def __init__(
        self,
        dir_name: str = None,
    ):
        # The name of the directory
        # 
        # This parameter is required.
        self.dir_name = dir_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dir_name is not None:
            result['dirName'] = self.dir_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dirName') is not None:
            self.dir_name = m.get('dirName')
        return self


class ListAdvanceConfigDirResponseBodyResult(TeaModel):
    def __init__(
        self,
        full_path_name: str = None,
        is_dir: bool = None,
        is_template: bool = None,
        name: str = None,
    ):
        # The absolute path in which the file is stored.
        self.full_path_name = full_path_name
        # Indicates whether the file is a directory. Valid values: true and false.
        self.is_dir = is_dir
        # Indicates whether the file is a template. Valid values: **true** and **false**.
        self.is_template = is_template
        # The cluster name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.full_path_name is not None:
            result['fullPathName'] = self.full_path_name
        if self.is_dir is not None:
            result['isDir'] = self.is_dir
        if self.is_template is not None:
            result['isTemplate'] = self.is_template
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fullPathName') is not None:
            self.full_path_name = m.get('fullPathName')
        if m.get('isDir') is not None:
            self.is_dir = m.get('isDir')
        if m.get('isTemplate') is not None:
            self.is_template = m.get('isTemplate')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListAdvanceConfigDirResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListAdvanceConfigDirResponseBodyResult] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The advanced configuration files.
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListAdvanceConfigDirResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListAdvanceConfigDirResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAdvanceConfigDirResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAdvanceConfigDirResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAdvanceConfigsRequest(TeaModel):
    def __init__(
        self,
        data_source_name: str = None,
        index_name: str = None,
        new_mode: bool = None,
        type: str = None,
    ):
        # The name of the data source.
        self.data_source_name = data_source_name
        # The index name.
        self.index_name = index_name
        # Specifies whether the OpenSearch Vector Search Edition instance is of the new version.
        self.new_mode = new_mode
        # The type of advanced configurations that you want to query. Valid values: - online -offline (default)
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_name is not None:
            result['dataSourceName'] = self.data_source_name
        if self.index_name is not None:
            result['indexName'] = self.index_name
        if self.new_mode is not None:
            result['newMode'] = self.new_mode
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataSourceName') is not None:
            self.data_source_name = m.get('dataSourceName')
        if m.get('indexName') is not None:
            self.index_name = m.get('indexName')
        if m.get('newMode') is not None:
            self.new_mode = m.get('newMode')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListAdvanceConfigsResponseBodyResultFiles(TeaModel):
    def __init__(
        self,
        full_path_name: str = None,
        is_dir: bool = None,
        is_template: bool = None,
        name: str = None,
    ):
        # The absolute path in which the file is stored.
        self.full_path_name = full_path_name
        # Indicates whether the file is a directory. Valid values: true and false.
        self.is_dir = is_dir
        # Indicates whether the file is a template. Valid values: true and false.
        self.is_template = is_template
        # The file name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.full_path_name is not None:
            result['fullPathName'] = self.full_path_name
        if self.is_dir is not None:
            result['isDir'] = self.is_dir
        if self.is_template is not None:
            result['isTemplate'] = self.is_template
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fullPathName') is not None:
            self.full_path_name = m.get('fullPathName')
        if m.get('isDir') is not None:
            self.is_dir = m.get('isDir')
        if m.get('isTemplate') is not None:
            self.is_template = m.get('isTemplate')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListAdvanceConfigsResponseBodyResult(TeaModel):
    def __init__(
        self,
        advance_config_type: str = None,
        content: str = None,
        content_type: str = None,
        creator: str = None,
        desc: str = None,
        files: List[ListAdvanceConfigsResponseBodyResultFiles] = None,
        name: str = None,
        status: str = None,
        update_time: int = None,
    ):
        # *   The type of the advanced configuration. Valid values: -ONLINE: online configuration
        # *   \\-ONLINE_CAVA: online Cava configuration
        # *   \\-ONLINE_PLUGIN: online plug-in configuration
        # *   \\-ONLINE_QUERY: query configuration
        # *   \\-OFFLINE_DICT: offline dictionary configuration
        # *   \\-OFFLINE_TABLE: offline table configuration
        # *   \\-OFFLINE_COMMON: offline configuration
        # *   \\-OFFLINE_PLUGIN: offline plug-in configuration
        # *   \\-OFFLINE_INDEX: index configuration
        self.advance_config_type = advance_config_type
        # The content of the advanced configuration that is returned.
        self.content = content
        # The type of the configuration content. Valid values: FILE, GIT, HTTP, and ODPS.
        self.content_type = content_type
        # The Alibaba Cloud account ID of the user who created the advanced configuration.
        self.creator = creator
        # The description of the advanced configuration.
        self.desc = desc
        # The files.
        self.files = files
        # The name of the advanced configuration.
        self.name = name
        # The status of the advanced configuration. Valid values: drafting: The advanced configuration is in the draft state. used: The advanced configuration is being used. unused: The advanced configuration is not used. trash: The advanced configuration is being deleted.
        self.status = status
        # The time when the advanced configuration was updated.
        self.update_time = update_time

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advance_config_type is not None:
            result['advanceConfigType'] = self.advance_config_type
        if self.content is not None:
            result['content'] = self.content
        if self.content_type is not None:
            result['contentType'] = self.content_type
        if self.creator is not None:
            result['creator'] = self.creator
        if self.desc is not None:
            result['desc'] = self.desc
        result['files'] = []
        if self.files is not None:
            for k in self.files:
                result['files'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('advanceConfigType') is not None:
            self.advance_config_type = m.get('advanceConfigType')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        self.files = []
        if m.get('files') is not None:
            for k in m.get('files'):
                temp_model = ListAdvanceConfigsResponseBodyResultFiles()
                self.files.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class ListAdvanceConfigsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListAdvanceConfigsResponseBodyResult] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The advanced configurations.
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListAdvanceConfigsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListAdvanceConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAdvanceConfigsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAdvanceConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAliasesResponseBodyResult(TeaModel):
    def __init__(
        self,
        alias: str = None,
        index: str = None,
    ):
        # alias name
        self.alias = alias
        # index name
        self.index = index

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['alias'] = self.alias
        if self.index is not None:
            result['index'] = self.index
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alias') is not None:
            self.alias = m.get('alias')
        if m.get('index') is not None:
            self.index = m.get('index')
        return self


class ListAliasesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListAliasesResponseBodyResult] = None,
    ):
        # id of request
        self.request_id = request_id
        # List
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListAliasesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListAliasesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAliasesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAliasesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClusterNamesResponseBodyResult(TeaModel):
    def __init__(
        self,
        description: str = None,
        id: int = None,
        name: str = None,
    ):
        # The description of the cluster.
        self.description = description
        # The cluster ID.
        self.id = id
        # The cluster name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListClusterNamesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ListClusterNamesResponseBodyResult = None,
    ):
        # id of request
        self.request_id = request_id
        # The result set.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = ListClusterNamesResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class ListClusterNamesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListClusterNamesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListClusterNamesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClusterTasksResponseBodyResultTags(TeaModel):
    def __init__(
        self,
        msg: str = None,
        tag_level: str = None,
    ):
        # The tag content.
        self.msg = msg
        # The tag level.
        self.tag_level = tag_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msg is not None:
            result['msg'] = self.msg
        if self.tag_level is not None:
            result['tagLevel'] = self.tag_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('tagLevel') is not None:
            self.tag_level = m.get('tagLevel')
        return self


class ListClusterTasksResponseBodyResultTaskNodes(TeaModel):
    def __init__(
        self,
        finish_date: str = None,
        index: int = None,
        name: str = None,
        status: str = None,
    ):
        # The time when the task was complete.
        self.finish_date = finish_date
        # The ordinal number of the task.
        self.index = index
        # The task name.
        self.name = name
        # The task status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.finish_date is not None:
            result['finishDate'] = self.finish_date
        if self.index is not None:
            result['index'] = self.index
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('finishDate') is not None:
            self.finish_date = m.get('finishDate')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListClusterTasksResponseBodyResult(TeaModel):
    def __init__(
        self,
        extra_attribute: str = None,
        field_3: str = None,
        fsm_id: str = None,
        group_type: str = None,
        name: str = None,
        status: str = None,
        tags: List[ListClusterTasksResponseBodyResultTags] = None,
        task_nodes: List[ListClusterTasksResponseBodyResultTaskNodes] = None,
        time: str = None,
        type: str = None,
        user: str = None,
    ):
        # The additional attributes of the card.
        self.extra_attribute = extra_attribute
        # The field3 field that was passed when the FSM was created.
        self.field_3 = field_3
        # The ID of the finite state machine (FSM).
        self.fsm_id = fsm_id
        # The change group type.
        self.group_type = group_type
        # The card name.
        self.name = name
        # The FSM status.
        self.status = status
        # The tags of the progress bar.
        self.tags = tags
        # The task information.
        self.task_nodes = task_nodes
        # The timestamp of the card.
        self.time = time
        # The card type.
        self.type = type
        # The user who triggered the generation of the FSM process.
        self.user = user

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.task_nodes:
            for k in self.task_nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra_attribute is not None:
            result['extraAttribute'] = self.extra_attribute
        if self.field_3 is not None:
            result['field3'] = self.field_3
        if self.fsm_id is not None:
            result['fsmId'] = self.fsm_id
        if self.group_type is not None:
            result['groupType'] = self.group_type
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        result['taskNodes'] = []
        if self.task_nodes is not None:
            for k in self.task_nodes:
                result['taskNodes'].append(k.to_map() if k else None)
        if self.time is not None:
            result['time'] = self.time
        if self.type is not None:
            result['type'] = self.type
        if self.user is not None:
            result['user'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('extraAttribute') is not None:
            self.extra_attribute = m.get('extraAttribute')
        if m.get('field3') is not None:
            self.field_3 = m.get('field3')
        if m.get('fsmId') is not None:
            self.fsm_id = m.get('fsmId')
        if m.get('groupType') is not None:
            self.group_type = m.get('groupType')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = ListClusterTasksResponseBodyResultTags()
                self.tags.append(temp_model.from_map(k))
        self.task_nodes = []
        if m.get('taskNodes') is not None:
            for k in m.get('taskNodes'):
                temp_model = ListClusterTasksResponseBodyResultTaskNodes()
                self.task_nodes.append(temp_model.from_map(k))
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('user') is not None:
            self.user = m.get('user')
        return self


class ListClusterTasksResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListClusterTasksResponseBodyResult] = None,
    ):
        # id of request
        self.request_id = request_id
        # The index information.
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListClusterTasksResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListClusterTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListClusterTasksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListClusterTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClustersResponseBodyResultDataNode(TeaModel):
    def __init__(
        self,
        name: str = None,
        number: int = None,
        partition: int = None,
    ):
        # The name of the Searcher worker.
        self.name = name
        # The number of Searcher workers.
        self.number = number
        # The ID of the partition that is stored on the Searcher worker.
        self.partition = partition

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.number is not None:
            result['number'] = self.number
        if self.partition is not None:
            result['partition'] = self.partition
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('number') is not None:
            self.number = m.get('number')
        if m.get('partition') is not None:
            self.partition = m.get('partition')
        return self


class ListClustersResponseBodyResultQueryNode(TeaModel):
    def __init__(
        self,
        name: str = None,
        number: int = None,
        partition: int = None,
    ):
        # The name of the QRS worker.
        self.name = name
        # The number of QRS workers.
        self.number = number
        # The ID of the partition that is stored on the QRS worker.
        self.partition = partition

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.number is not None:
            result['number'] = self.number
        if self.partition is not None:
            result['partition'] = self.partition
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('number') is not None:
            self.number = m.get('number')
        if m.get('partition') is not None:
            self.partition = m.get('partition')
        return self


class ListClustersResponseBodyResult(TeaModel):
    def __init__(
        self,
        config: Dict[str, dict] = None,
        config_update_time: str = None,
        create_time: str = None,
        current_advance_config_version: str = None,
        current_offline_dict_config_version: str = None,
        current_online_config_version: str = None,
        current_online_query_config_version: str = None,
        data_node: ListClustersResponseBodyResultDataNode = None,
        description: str = None,
        latest_advance_config_version: str = None,
        latest_offline_dict_config_version: str = None,
        latest_online_config_version: str = None,
        latest_online_query_config_version: str = None,
        name: str = None,
        query_node: ListClustersResponseBodyResultQueryNode = None,
        status: str = None,
    ):
        # The configuration information.
        self.config = config
        # The time when the configuration was updated.
        self.config_update_time = config_update_time
        # The time when the cluster was created.
        self.create_time = create_time
        # The effective advanced configuration version.
        self.current_advance_config_version = current_advance_config_version
        # The effective dictionary configuration version.
        self.current_offline_dict_config_version = current_offline_dict_config_version
        # The effective online configuration version.
        self.current_online_config_version = current_online_config_version
        # The effective query configuration version.
        self.current_online_query_config_version = current_online_query_config_version
        # The information about Searcher workers.
        self.data_node = data_node
        # The description of the cluster.
        self.description = description
        # The latest advanced configuration version.
        self.latest_advance_config_version = latest_advance_config_version
        # The latest dictionary configuration version.
        self.latest_offline_dict_config_version = latest_offline_dict_config_version
        # The latest online configuration version.
        self.latest_online_config_version = latest_online_config_version
        # The latest query configuration version.
        self.latest_online_query_config_version = latest_online_query_config_version
        # The cluster name.
        self.name = name
        # The information about Query Result Searcher (QRS) workers.
        self.query_node = query_node
        # The cluster status. Valid values: running: The cluster is running. starting: The cluster is being started. stopping: The cluster is being stopped. stopped: The cluster is stopped.
        self.status = status

    def validate(self):
        if self.data_node:
            self.data_node.validate()
        if self.query_node:
            self.query_node.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['config'] = self.config
        if self.config_update_time is not None:
            result['configUpdateTime'] = self.config_update_time
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.current_advance_config_version is not None:
            result['currentAdvanceConfigVersion'] = self.current_advance_config_version
        if self.current_offline_dict_config_version is not None:
            result['currentOfflineDictConfigVersion'] = self.current_offline_dict_config_version
        if self.current_online_config_version is not None:
            result['currentOnlineConfigVersion'] = self.current_online_config_version
        if self.current_online_query_config_version is not None:
            result['currentOnlineQueryConfigVersion'] = self.current_online_query_config_version
        if self.data_node is not None:
            result['dataNode'] = self.data_node.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.latest_advance_config_version is not None:
            result['latestAdvanceConfigVersion'] = self.latest_advance_config_version
        if self.latest_offline_dict_config_version is not None:
            result['latestOfflineDictConfigVersion'] = self.latest_offline_dict_config_version
        if self.latest_online_config_version is not None:
            result['latestOnlineConfigVersion'] = self.latest_online_config_version
        if self.latest_online_query_config_version is not None:
            result['latestOnlineQueryConfigVersion'] = self.latest_online_query_config_version
        if self.name is not None:
            result['name'] = self.name
        if self.query_node is not None:
            result['queryNode'] = self.query_node.to_map()
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            self.config = m.get('config')
        if m.get('configUpdateTime') is not None:
            self.config_update_time = m.get('configUpdateTime')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('currentAdvanceConfigVersion') is not None:
            self.current_advance_config_version = m.get('currentAdvanceConfigVersion')
        if m.get('currentOfflineDictConfigVersion') is not None:
            self.current_offline_dict_config_version = m.get('currentOfflineDictConfigVersion')
        if m.get('currentOnlineConfigVersion') is not None:
            self.current_online_config_version = m.get('currentOnlineConfigVersion')
        if m.get('currentOnlineQueryConfigVersion') is not None:
            self.current_online_query_config_version = m.get('currentOnlineQueryConfigVersion')
        if m.get('dataNode') is not None:
            temp_model = ListClustersResponseBodyResultDataNode()
            self.data_node = temp_model.from_map(m['dataNode'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('latestAdvanceConfigVersion') is not None:
            self.latest_advance_config_version = m.get('latestAdvanceConfigVersion')
        if m.get('latestOfflineDictConfigVersion') is not None:
            self.latest_offline_dict_config_version = m.get('latestOfflineDictConfigVersion')
        if m.get('latestOnlineConfigVersion') is not None:
            self.latest_online_config_version = m.get('latestOnlineConfigVersion')
        if m.get('latestOnlineQueryConfigVersion') is not None:
            self.latest_online_query_config_version = m.get('latestOnlineQueryConfigVersion')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('queryNode') is not None:
            temp_model = ListClustersResponseBodyResultQueryNode()
            self.query_node = temp_model.from_map(m['queryNode'])
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListClustersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListClustersResponseBodyResult] = None,
    ):
        # id of request
        self.request_id = request_id
        # The clusters.
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListClustersResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListClustersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListClustersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataSourceSchemasResponseBodyResultPrimaryKey(TeaModel):
    def __init__(
        self,
        has_primary_key_attribute: bool = None,
        is_primary_key: bool = None,
        is_primary_key_sorted: bool = None,
    ):
        # Indicates whether the field has the primary key attribute. Valid values: **true** and **false**.
        self.has_primary_key_attribute = has_primary_key_attribute
        # Indicates whether the field is the primary key. Valid values: **true** and **false**.
        self.is_primary_key = is_primary_key
        # Indicates whether the field can be sorted. Valid values: **true** and **false**.
        self.is_primary_key_sorted = is_primary_key_sorted

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_primary_key_attribute is not None:
            result['hasPrimaryKeyAttribute'] = self.has_primary_key_attribute
        if self.is_primary_key is not None:
            result['isPrimaryKey'] = self.is_primary_key
        if self.is_primary_key_sorted is not None:
            result['isPrimaryKeySorted'] = self.is_primary_key_sorted
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hasPrimaryKeyAttribute') is not None:
            self.has_primary_key_attribute = m.get('hasPrimaryKeyAttribute')
        if m.get('isPrimaryKey') is not None:
            self.is_primary_key = m.get('isPrimaryKey')
        if m.get('isPrimaryKeySorted') is not None:
            self.is_primary_key_sorted = m.get('isPrimaryKeySorted')
        return self


class ListDataSourceSchemasResponseBodyResult(TeaModel):
    def __init__(
        self,
        add_index: bool = None,
        attribute: bool = None,
        custom: bool = None,
        name: str = None,
        primary_key: ListDataSourceSchemasResponseBodyResultPrimaryKey = None,
        summary: bool = None,
        type: str = None,
    ):
        # Indicates whether the field has the index attribute. Valid values: **true** and **false**.
        self.add_index = add_index
        # Indicates whether the field is an attribute field. Valid values: **true** and **false**.
        self.attribute = attribute
        # Indicates whether the field is a custom field. Valid values: **true** and **false**.
        self.custom = custom
        # The field name.
        self.name = name
        # The primary key field.
        self.primary_key = primary_key
        # Indicates whether the field can be displayed. Valid values: **true** and **false**.
        self.summary = summary
        # The field type.
        self.type = type

    def validate(self):
        if self.primary_key:
            self.primary_key.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_index is not None:
            result['addIndex'] = self.add_index
        if self.attribute is not None:
            result['attribute'] = self.attribute
        if self.custom is not None:
            result['custom'] = self.custom
        if self.name is not None:
            result['name'] = self.name
        if self.primary_key is not None:
            result['primaryKey'] = self.primary_key.to_map()
        if self.summary is not None:
            result['summary'] = self.summary
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('addIndex') is not None:
            self.add_index = m.get('addIndex')
        if m.get('attribute') is not None:
            self.attribute = m.get('attribute')
        if m.get('custom') is not None:
            self.custom = m.get('custom')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('primaryKey') is not None:
            temp_model = ListDataSourceSchemasResponseBodyResultPrimaryKey()
            self.primary_key = temp_model.from_map(m['primaryKey'])
        if m.get('summary') is not None:
            self.summary = m.get('summary')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListDataSourceSchemasResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListDataSourceSchemasResponseBodyResult] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The results returned.
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListDataSourceSchemasResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListDataSourceSchemasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDataSourceSchemasResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDataSourceSchemasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataSourceTasksResponseBodyResultTags(TeaModel):
    def __init__(
        self,
        msg: str = None,
        tag_level: str = None,
    ):
        # The tag content.
        self.msg = msg
        # The tag level.
        self.tag_level = tag_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msg is not None:
            result['msg'] = self.msg
        if self.tag_level is not None:
            result['tagLevel'] = self.tag_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('tagLevel') is not None:
            self.tag_level = m.get('tagLevel')
        return self


class ListDataSourceTasksResponseBodyResultTaskNodes(TeaModel):
    def __init__(
        self,
        finish_date: str = None,
        index: int = None,
        name: str = None,
        status: str = None,
    ):
        # The time when the task was complete.
        self.finish_date = finish_date
        # The ordinal number of the task.
        self.index = index
        # The task name.
        self.name = name
        # The task status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.finish_date is not None:
            result['finishDate'] = self.finish_date
        if self.index is not None:
            result['index'] = self.index
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('finishDate') is not None:
            self.finish_date = m.get('finishDate')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListDataSourceTasksResponseBodyResult(TeaModel):
    def __init__(
        self,
        extra_attribute: str = None,
        field_3: str = None,
        fsm_id: str = None,
        group_type: str = None,
        name: str = None,
        status: str = None,
        tags: List[ListDataSourceTasksResponseBodyResultTags] = None,
        task_nodes: List[ListDataSourceTasksResponseBodyResultTaskNodes] = None,
        time: str = None,
        type: str = None,
        user: str = None,
    ):
        # The additional attributes of the card.
        self.extra_attribute = extra_attribute
        # The field3 field that was passed when the FSM was created.
        self.field_3 = field_3
        # The ID of the finite state machine (FSM).
        self.fsm_id = fsm_id
        # The change group type.
        self.group_type = group_type
        # The card name.
        self.name = name
        # The FSM status.
        self.status = status
        # The tags of the progress bar.
        self.tags = tags
        # The task information.
        self.task_nodes = task_nodes
        # The timestamp of the card.
        self.time = time
        # The card type.
        self.type = type
        # The user who triggered the generation of the FSM process.
        self.user = user

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.task_nodes:
            for k in self.task_nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra_attribute is not None:
            result['extraAttribute'] = self.extra_attribute
        if self.field_3 is not None:
            result['field3'] = self.field_3
        if self.fsm_id is not None:
            result['fsmId'] = self.fsm_id
        if self.group_type is not None:
            result['groupType'] = self.group_type
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        result['taskNodes'] = []
        if self.task_nodes is not None:
            for k in self.task_nodes:
                result['taskNodes'].append(k.to_map() if k else None)
        if self.time is not None:
            result['time'] = self.time
        if self.type is not None:
            result['type'] = self.type
        if self.user is not None:
            result['user'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('extraAttribute') is not None:
            self.extra_attribute = m.get('extraAttribute')
        if m.get('field3') is not None:
            self.field_3 = m.get('field3')
        if m.get('fsmId') is not None:
            self.fsm_id = m.get('fsmId')
        if m.get('groupType') is not None:
            self.group_type = m.get('groupType')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = ListDataSourceTasksResponseBodyResultTags()
                self.tags.append(temp_model.from_map(k))
        self.task_nodes = []
        if m.get('taskNodes') is not None:
            for k in m.get('taskNodes'):
                temp_model = ListDataSourceTasksResponseBodyResultTaskNodes()
                self.task_nodes.append(temp_model.from_map(k))
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('user') is not None:
            self.user = m.get('user')
        return self


class ListDataSourceTasksResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListDataSourceTasksResponseBodyResult] = None,
    ):
        # id of request
        self.request_id = request_id
        # The index information.
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListDataSourceTasksResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListDataSourceTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDataSourceTasksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDataSourceTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataSourcesResponseBodyResult(TeaModel):
    def __init__(
        self,
        domain: str = None,
        indexes: List[str] = None,
        last_ful_time: int = None,
        name: str = None,
        status: str = None,
        type: str = None,
    ):
        # The data center in which the data source is deployed.
        self.domain = domain
        # The indexes.
        self.indexes = indexes
        # The time when the full data of the data source was last queried.
        self.last_ful_time = last_ful_time
        # The name of the data source.
        self.name = name
        # The status of the data source. Valid values: new: The data source is being created. publish: The data source is in the normal state. trash: The data source is being deleted.
        self.status = status
        # The type of the data source.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.indexes is not None:
            result['indexes'] = self.indexes
        if self.last_ful_time is not None:
            result['lastFulTime'] = self.last_ful_time
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('indexes') is not None:
            self.indexes = m.get('indexes')
        if m.get('lastFulTime') is not None:
            self.last_ful_time = m.get('lastFulTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListDataSourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListDataSourcesResponseBodyResult] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The results returned.
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListDataSourcesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListDataSourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDataSourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDataSourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDatabasesResponseBodyResultDatabasesSqlInstances(TeaModel):
    def __init__(
        self,
        children: List[Any] = None,
        id: int = None,
        instance_id: int = None,
        is_dir: int = None,
        name: str = None,
        parent: int = None,
        template_id: int = None,
        type: str = None,
    ):
        self.children = children
        self.id = id
        self.instance_id = instance_id
        self.is_dir = is_dir
        self.name = name
        self.parent = parent
        self.template_id = template_id
        # table, instance, template, function
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.children is not None:
            result['children'] = self.children
        if self.id is not None:
            result['id'] = self.id
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.is_dir is not None:
            result['isDir'] = self.is_dir
        if self.name is not None:
            result['name'] = self.name
        if self.parent is not None:
            result['parent'] = self.parent
        if self.template_id is not None:
            result['templateId'] = self.template_id
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('children') is not None:
            self.children = m.get('children')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('isDir') is not None:
            self.is_dir = m.get('isDir')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parent') is not None:
            self.parent = m.get('parent')
        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListDatabasesResponseBodyResultDatabasesTables(TeaModel):
    def __init__(
        self,
        children: List[Any] = None,
        id: int = None,
        instance_id: int = None,
        is_dir: int = None,
        name: str = None,
        parent: int = None,
        template_id: int = None,
        type: str = None,
    ):
        self.children = children
        self.id = id
        self.instance_id = instance_id
        self.is_dir = is_dir
        self.name = name
        self.parent = parent
        self.template_id = template_id
        # table, instance, template, function
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.children is not None:
            result['children'] = self.children
        if self.id is not None:
            result['id'] = self.id
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.is_dir is not None:
            result['isDir'] = self.is_dir
        if self.name is not None:
            result['name'] = self.name
        if self.parent is not None:
            result['parent'] = self.parent
        if self.template_id is not None:
            result['templateId'] = self.template_id
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('children') is not None:
            self.children = m.get('children')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('isDir') is not None:
            self.is_dir = m.get('isDir')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parent') is not None:
            self.parent = m.get('parent')
        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListDatabasesResponseBodyResultDatabasesTemplates(TeaModel):
    def __init__(
        self,
        children: List[Any] = None,
        id: int = None,
        instance_id: int = None,
        is_dir: int = None,
        name: str = None,
        parent: int = None,
        template_id: int = None,
        type: str = None,
    ):
        self.children = children
        self.id = id
        self.instance_id = instance_id
        self.is_dir = is_dir
        self.name = name
        self.parent = parent
        self.template_id = template_id
        # table, instance, template, function
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.children is not None:
            result['children'] = self.children
        if self.id is not None:
            result['id'] = self.id
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.is_dir is not None:
            result['isDir'] = self.is_dir
        if self.name is not None:
            result['name'] = self.name
        if self.parent is not None:
            result['parent'] = self.parent
        if self.template_id is not None:
            result['templateId'] = self.template_id
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('children') is not None:
            self.children = m.get('children')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('isDir') is not None:
            self.is_dir = m.get('isDir')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parent') is not None:
            self.parent = m.get('parent')
        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListDatabasesResponseBodyResultDatabases(TeaModel):
    def __init__(
        self,
        database: str = None,
        functions: Dict[str, List[ResultDatabasesFunctionsValue]] = None,
        sql_instances: List[ListDatabasesResponseBodyResultDatabasesSqlInstances] = None,
        tables: List[ListDatabasesResponseBodyResultDatabasesTables] = None,
        templates: List[ListDatabasesResponseBodyResultDatabasesTemplates] = None,
    ):
        self.database = database
        self.functions = functions
        self.sql_instances = sql_instances
        self.tables = tables
        self.templates = templates

    def validate(self):
        if self.functions:
            for v in self.functions.values():
                for k1 in v:
                    if k1:
                        k1.validate()
        if self.sql_instances:
            for k in self.sql_instances:
                if k:
                    k.validate()
        if self.tables:
            for k in self.tables:
                if k:
                    k.validate()
        if self.templates:
            for k in self.templates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database is not None:
            result['database'] = self.database
        result['functions'] = {}
        if self.functions is not None:
            for k, v in self.functions.items():
                l1 = []
                for k1 in v:
                    l1.append(k1.to_map() if k1 else None)
                result['functions'][k] = l1
        result['sqlInstances'] = []
        if self.sql_instances is not None:
            for k in self.sql_instances:
                result['sqlInstances'].append(k.to_map() if k else None)
        result['tables'] = []
        if self.tables is not None:
            for k in self.tables:
                result['tables'].append(k.to_map() if k else None)
        result['templates'] = []
        if self.templates is not None:
            for k in self.templates:
                result['templates'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('database') is not None:
            self.database = m.get('database')
        self.functions = {}
        if m.get('functions') is not None:
            for k, v in m.get('functions').items():
                l1 = []
                for k1 in v:
                    temp_model = ResultDatabasesFunctionsValue()
                    l1.append(temp_model.from_map(k1))
                self.functions['k'] = l1
        self.sql_instances = []
        if m.get('sqlInstances') is not None:
            for k in m.get('sqlInstances'):
                temp_model = ListDatabasesResponseBodyResultDatabasesSqlInstances()
                self.sql_instances.append(temp_model.from_map(k))
        self.tables = []
        if m.get('tables') is not None:
            for k in m.get('tables'):
                temp_model = ListDatabasesResponseBodyResultDatabasesTables()
                self.tables.append(temp_model.from_map(k))
        self.templates = []
        if m.get('templates') is not None:
            for k in m.get('templates'):
                temp_model = ListDatabasesResponseBodyResultDatabasesTemplates()
                self.templates.append(temp_model.from_map(k))
        return self


class ListDatabasesResponseBodyResult(TeaModel):
    def __init__(
        self,
        databases: List[ListDatabasesResponseBodyResultDatabases] = None,
    ):
        self.databases = databases

    def validate(self):
        if self.databases:
            for k in self.databases:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['databases'] = []
        if self.databases is not None:
            for k in self.databases:
                result['databases'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.databases = []
        if m.get('databases') is not None:
            for k in m.get('databases'):
                temp_model = ListDatabasesResponseBodyResultDatabases()
                self.databases.append(temp_model.from_map(k))
        return self


class ListDatabasesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ListDatabasesResponseBodyResult = None,
    ):
        # id of request
        self.request_id = request_id
        # NodeTreeVO
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = ListDatabasesResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class ListDatabasesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDatabasesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDatabasesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDateSourceGenerationsRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        valid_status: bool = None,
    ):
        # The data center where the data source is deployed.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # Specifies the index versions to be returned. Valid values:
        # 
        # 1.  true (default): returns the index versions that are complete and not expired.
        # 2.  false: returns all index versions.
        self.valid_status = valid_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
        if self.valid_status is not None:
            result['validStatus'] = self.valid_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        if m.get('validStatus') is not None:
            self.valid_status = m.get('validStatus')
        return self


class ListDateSourceGenerationsResponseBodyResult(TeaModel):
    def __init__(
        self,
        build_deploy_id: int = None,
        create_time: int = None,
        data_dump_root: str = None,
        generation: int = None,
        partition: Dict[str, int] = None,
        status: str = None,
        timestamp: int = None,
    ):
        # The ID of the offline deployment.
        self.build_deploy_id = build_deploy_id
        # The timestamp that was generated when the index building was started.
        self.create_time = create_time
        # The path of the dumped index in the Apsara File Storage for HDFS file system.
        self.data_dump_root = data_dump_root
        # The ID of the full index version.
        self.generation = generation
        # The shards of the index version. The value is a key-value pair in which the key indicates the index name and the value indicates the number of shards. The number of value shards.
        self.partition = partition
        # The status of the index version.
        self.status = status
        # The start timestamp from which incremental data is retrieved.
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_deploy_id is not None:
            result['buildDeployId'] = self.build_deploy_id
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.data_dump_root is not None:
            result['dataDumpRoot'] = self.data_dump_root
        if self.generation is not None:
            result['generation'] = self.generation
        if self.partition is not None:
            result['partition'] = self.partition
        if self.status is not None:
            result['status'] = self.status
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('buildDeployId') is not None:
            self.build_deploy_id = m.get('buildDeployId')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('dataDumpRoot') is not None:
            self.data_dump_root = m.get('dataDumpRoot')
        if m.get('generation') is not None:
            self.generation = m.get('generation')
        if m.get('partition') is not None:
            self.partition = m.get('partition')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        return self


class ListDateSourceGenerationsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListDateSourceGenerationsResponseBodyResult] = None,
    ):
        # id of request
        self.request_id = request_id
        # List
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListDateSourceGenerationsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListDateSourceGenerationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDateSourceGenerationsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDateSourceGenerationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIndexRecoverRecordsResponseBody(TeaModel):
    def __init__(
        self,
        desc: str = None,
        finished_time: str = None,
        generation_id: str = None,
    ):
        # The description.
        self.desc = desc
        # The time when the index version was published.
        self.finished_time = finished_time
        # The ID of the full index version.
        self.generation_id = generation_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['desc'] = self.desc
        if self.finished_time is not None:
            result['finishedTime'] = self.finished_time
        if self.generation_id is not None:
            result['generationId'] = self.generation_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('finishedTime') is not None:
            self.finished_time = m.get('finishedTime')
        if m.get('generationId') is not None:
            self.generation_id = m.get('generationId')
        return self


class ListIndexRecoverRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListIndexRecoverRecordsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListIndexRecoverRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIndexesRequest(TeaModel):
    def __init__(
        self,
        new_mode: bool = None,
    ):
        # Specifies whether the OpenSearch Vector Search Edition instance is of the new version.
        self.new_mode = new_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_mode is not None:
            result['newMode'] = self.new_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('newMode') is not None:
            self.new_mode = m.get('newMode')
        return self


class ListIndexesResponseBodyResultDataSourceInfoConfig(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        access_secret: str = None,
        bucket: str = None,
        endpoint: str = None,
        namespace: str = None,
        oss_path: str = None,
        partition: str = None,
        path: str = None,
        project: str = None,
        table: str = None,
    ):
        # The AccessKey ID of the MaxCompute data source.
        self.access_key = access_key
        # The AccessKey secret of the MaxCompute data source.
        self.access_secret = access_secret
        # The OSS bucket.
        self.bucket = bucket
        # The endpoint of the MaxCompute data source.
        self.endpoint = endpoint
        # The namespace. This parameter is applicable to the SARO data source used in the intranet of Alibaba Group.
        self.namespace = namespace
        # The Object Storage Service (OSS) path.
        self.oss_path = oss_path
        # The shard name.
        self.partition = partition
        # The file path in the Apsara File Storage for HDFS file system.
        self.path = path
        # The name of the MaxCompute project that is used as the data source.
        self.project = project
        # The name of the MaxCompute table that is used as the data source.
        self.table = table

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.access_secret is not None:
            result['accessSecret'] = self.access_secret
        if self.bucket is not None:
            result['bucket'] = self.bucket
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.oss_path is not None:
            result['ossPath'] = self.oss_path
        if self.partition is not None:
            result['partition'] = self.partition
        if self.path is not None:
            result['path'] = self.path
        if self.project is not None:
            result['project'] = self.project
        if self.table is not None:
            result['table'] = self.table
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('accessSecret') is not None:
            self.access_secret = m.get('accessSecret')
        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('ossPath') is not None:
            self.oss_path = m.get('ossPath')
        if m.get('partition') is not None:
            self.partition = m.get('partition')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('table') is not None:
            self.table = m.get('table')
        return self


class ListIndexesResponseBodyResultDataSourceInfoSaroConfig(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        table_name: str = None,
    ):
        # The namespace of the SARO data source.
        self.namespace = namespace
        # The name of the SARO table.
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.table_name is not None:
            result['tableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        return self


class ListIndexesResponseBodyResultDataSourceInfo(TeaModel):
    def __init__(
        self,
        auto_build_index: bool = None,
        config: ListIndexesResponseBodyResultDataSourceInfoConfig = None,
        domain: str = None,
        name: str = None,
        process_partition_count: int = None,
        saro_config: ListIndexesResponseBodyResultDataSourceInfoSaroConfig = None,
        type: str = None,
    ):
        # Indicates whether the automatic full indexing feature is enabled.
        self.auto_build_index = auto_build_index
        # The configuration of MaxCompute data sources.
        self.config = config
        # The data center in which the data source is deployed.
        self.domain = domain
        # The name of the data source.
        self.name = name
        # The number of resources used for data update.
        self.process_partition_count = process_partition_count
        # The configurations of the SARO data source.
        self.saro_config = saro_config
        # The type of the data source. Valid values: odps, swift, saro, oss, and unKnow.
        self.type = type

    def validate(self):
        if self.config:
            self.config.validate()
        if self.saro_config:
            self.saro_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_build_index is not None:
            result['autoBuildIndex'] = self.auto_build_index
        if self.config is not None:
            result['config'] = self.config.to_map()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.name is not None:
            result['name'] = self.name
        if self.process_partition_count is not None:
            result['processPartitionCount'] = self.process_partition_count
        if self.saro_config is not None:
            result['saroConfig'] = self.saro_config.to_map()
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoBuildIndex') is not None:
            self.auto_build_index = m.get('autoBuildIndex')
        if m.get('config') is not None:
            temp_model = ListIndexesResponseBodyResultDataSourceInfoConfig()
            self.config = temp_model.from_map(m['config'])
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('processPartitionCount') is not None:
            self.process_partition_count = m.get('processPartitionCount')
        if m.get('saroConfig') is not None:
            temp_model = ListIndexesResponseBodyResultDataSourceInfoSaroConfig()
            self.saro_config = temp_model.from_map(m['saroConfig'])
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListIndexesResponseBodyResultVersionsFiles(TeaModel):
    def __init__(
        self,
        full_path_name: str = None,
        is_dir: bool = None,
        is_template: bool = None,
        name: str = None,
    ):
        # The full path of the file.
        self.full_path_name = full_path_name
        # Indicates whether the file is a directory.
        self.is_dir = is_dir
        # Indicates whether the file is a template.
        self.is_template = is_template
        # The file name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.full_path_name is not None:
            result['fullPathName'] = self.full_path_name
        if self.is_dir is not None:
            result['isDir'] = self.is_dir
        if self.is_template is not None:
            result['isTemplate'] = self.is_template
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fullPathName') is not None:
            self.full_path_name = m.get('fullPathName')
        if m.get('isDir') is not None:
            self.is_dir = m.get('isDir')
        if m.get('isTemplate') is not None:
            self.is_template = m.get('isTemplate')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListIndexesResponseBodyResultVersions(TeaModel):
    def __init__(
        self,
        desc: str = None,
        files: List[ListIndexesResponseBodyResultVersionsFiles] = None,
        name: str = None,
        status: str = None,
        update_time: int = None,
        version_id: int = None,
    ):
        # The description of the index version.
        self.desc = desc
        # The files.
        self.files = files
        # The name of the index version.
        self.name = name
        # The status of the index version. Valid values:
        # 
        # *   NEW: The index version is created.
        # *   PUBLISH: The index version is normal.
        # *   IN_USE: The index version is in use.
        # *   NOT_USE: The index version is not used.
        # *   STOP_USE: The index version is being stopped.
        # *   RESTORE_USE: The index version is being restored.
        # *   FAIL: The index version failed to be created.
        self.status = status
        # The time when the index version was updated.
        self.update_time = update_time
        # The ID of the index version. If the index version is modified, the returned value is null.
        self.version_id = version_id

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['desc'] = self.desc
        result['files'] = []
        if self.files is not None:
            for k in self.files:
                result['files'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.version_id is not None:
            result['versionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        self.files = []
        if m.get('files') is not None:
            for k in m.get('files'):
                temp_model = ListIndexesResponseBodyResultVersionsFiles()
                self.files.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        return self


class ListIndexesResponseBodyResult(TeaModel):
    def __init__(
        self,
        content: str = None,
        data_source: str = None,
        data_source_info: ListIndexesResponseBodyResultDataSourceInfo = None,
        description: str = None,
        domain: str = None,
        full_update_time: str = None,
        full_version: int = None,
        inc_update_time: str = None,
        index_size: int = None,
        index_status: str = None,
        name: str = None,
        partition: int = None,
        versions: List[ListIndexesResponseBodyResultVersions] = None,
    ):
        # The index schema, which is a JSON string.
        self.content = content
        # The name of the data source.
        self.data_source = data_source
        # The information about the data source.
        self.data_source_info = data_source_info
        # The description.
        self.description = description
        # The deployment name of the index.
        self.domain = domain
        # The time when full data in the index was last updated.
        self.full_update_time = full_update_time
        # The full version of the index.
        self.full_version = full_version
        # The time when incremental data in the index was last updated.
        self.inc_update_time = inc_update_time
        # The index size.
        self.index_size = index_size
        # The index ststus. Valid values: NEW and PUBLISH.
        self.index_status = index_status
        # The index name.
        self.name = name
        # The number of shards.
        self.partition = partition
        # The index versions.
        self.versions = versions

    def validate(self):
        if self.data_source_info:
            self.data_source_info.validate()
        if self.versions:
            for k in self.versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.data_source is not None:
            result['dataSource'] = self.data_source
        if self.data_source_info is not None:
            result['dataSourceInfo'] = self.data_source_info.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.domain is not None:
            result['domain'] = self.domain
        if self.full_update_time is not None:
            result['fullUpdateTime'] = self.full_update_time
        if self.full_version is not None:
            result['fullVersion'] = self.full_version
        if self.inc_update_time is not None:
            result['incUpdateTime'] = self.inc_update_time
        if self.index_size is not None:
            result['indexSize'] = self.index_size
        if self.index_status is not None:
            result['indexStatus'] = self.index_status
        if self.name is not None:
            result['name'] = self.name
        if self.partition is not None:
            result['partition'] = self.partition
        result['versions'] = []
        if self.versions is not None:
            for k in self.versions:
                result['versions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('dataSource') is not None:
            self.data_source = m.get('dataSource')
        if m.get('dataSourceInfo') is not None:
            temp_model = ListIndexesResponseBodyResultDataSourceInfo()
            self.data_source_info = temp_model.from_map(m['dataSourceInfo'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('fullUpdateTime') is not None:
            self.full_update_time = m.get('fullUpdateTime')
        if m.get('fullVersion') is not None:
            self.full_version = m.get('fullVersion')
        if m.get('incUpdateTime') is not None:
            self.inc_update_time = m.get('incUpdateTime')
        if m.get('indexSize') is not None:
            self.index_size = m.get('indexSize')
        if m.get('indexStatus') is not None:
            self.index_status = m.get('indexStatus')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('partition') is not None:
            self.partition = m.get('partition')
        self.versions = []
        if m.get('versions') is not None:
            for k in m.get('versions'):
                temp_model = ListIndexesResponseBodyResultVersions()
                self.versions.append(temp_model.from_map(k))
        return self


class ListIndexesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListIndexesResponseBodyResult] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The details of indexes.
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListIndexesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListIndexesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListIndexesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListIndexesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstanceSpecsRequest(TeaModel):
    def __init__(
        self,
        type: str = None,
    ):
        # The node type. Valid values:
        # 
        # *   qrs: Query Result Searcher (QRS) Worker
        # *   search: Searcher Worker
        # *   index: index node
        # *   cluster: cluster
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListInstanceSpecsResponseBodyResult(TeaModel):
    def __init__(
        self,
        cpu: int = None,
        max_disk: int = None,
        mem: int = None,
        min_disk: int = None,
    ):
        # The number of vCPUs.
        self.cpu = cpu
        # The maximum storage of a single data node. Unit: GB.
        self.max_disk = max_disk
        # The memory of the instance. Unit: GB.
        self.mem = mem
        # The minimum storage of a single data node. Unit: GB.
        self.min_disk = min_disk

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['cpu'] = self.cpu
        if self.max_disk is not None:
            result['maxDisk'] = self.max_disk
        if self.mem is not None:
            result['mem'] = self.mem
        if self.min_disk is not None:
            result['minDisk'] = self.min_disk
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        if m.get('maxDisk') is not None:
            self.max_disk = m.get('maxDisk')
        if m.get('mem') is not None:
            self.mem = m.get('mem')
        if m.get('minDisk') is not None:
            self.min_disk = m.get('minDisk')
        return self


class ListInstanceSpecsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListInstanceSpecsResponseBodyResult] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The instance types.
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListInstanceSpecsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListInstanceSpecsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInstanceSpecsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListInstanceSpecsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstancesRequestTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ListInstancesRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        edition: str = None,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        tags: List[ListInstancesRequestTags] = None,
    ):
        # The description of the instance. You can use this description to filter instances. Fuzzy match is supported.
        self.description = description
        # The instance type. Valid values: vector: OpenSearch Vector Search Edition instance. engine: OpenSearch Retrieval Engine Edition instance.
        self.edition = edition
        # The instance ID.
        self.instance_id = instance_id
        # The number of the page to return. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values: 1 to 50. Default value: 10.
        self.page_size = page_size
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        # The tags of the instance.
        self.tags = tags

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.edition is not None:
            result['edition'] = self.edition
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('edition') is not None:
            self.edition = m.get('edition')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = ListInstancesRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListInstancesShrinkRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        edition: str = None,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        tags_shrink: str = None,
    ):
        # The description of the instance. You can use this description to filter instances. Fuzzy match is supported.
        self.description = description
        # The instance type. Valid values: vector: OpenSearch Vector Search Edition instance. engine: OpenSearch Retrieval Engine Edition instance.
        self.edition = edition
        # The instance ID.
        self.instance_id = instance_id
        # The number of the page to return. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values: 1 to 50. Default value: 10.
        self.page_size = page_size
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        # The tags of the instance.
        self.tags_shrink = tags_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.edition is not None:
            result['edition'] = self.edition
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.tags_shrink is not None:
            result['tags'] = self.tags_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('edition') is not None:
            self.edition = m.get('edition')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('tags') is not None:
            self.tags_shrink = m.get('tags')
        return self


class ListInstancesResponseBodyResultNetwork(TeaModel):
    def __init__(
        self,
        allow: str = None,
        endpoint: str = None,
        public_endpoint: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        self.allow = allow
        # The instance endpoint.
        self.endpoint = endpoint
        self.public_endpoint = public_endpoint
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The ID of the virtual private cloud (VPC) in which the instance is deployed.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow is not None:
            result['allow'] = self.allow
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.public_endpoint is not None:
            result['publicEndpoint'] = self.public_endpoint
        if self.v_switch_id is not None:
            result['vSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allow') is not None:
            self.allow = m.get('allow')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('publicEndpoint') is not None:
            self.public_endpoint = m.get('publicEndpoint')
        if m.get('vSwitchId') is not None:
            self.v_switch_id = m.get('vSwitchId')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self


class ListInstancesResponseBodyResultSpecQrsResource(TeaModel):
    def __init__(
        self,
        category: str = None,
        cpu: int = None,
        disk: int = None,
        mem: int = None,
        node_count: int = None,
    ):
        self.category = category
        self.cpu = cpu
        self.disk = disk
        self.mem = mem
        self.node_count = node_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.cpu is not None:
            result['cpu'] = self.cpu
        if self.disk is not None:
            result['disk'] = self.disk
        if self.mem is not None:
            result['mem'] = self.mem
        if self.node_count is not None:
            result['nodeCount'] = self.node_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        if m.get('disk') is not None:
            self.disk = m.get('disk')
        if m.get('mem') is not None:
            self.mem = m.get('mem')
        if m.get('nodeCount') is not None:
            self.node_count = m.get('nodeCount')
        return self


class ListInstancesResponseBodyResultSpecSearchResource(TeaModel):
    def __init__(
        self,
        category: str = None,
        cpu: int = None,
        disk: int = None,
        mem: int = None,
        node_count: int = None,
    ):
        self.category = category
        self.cpu = cpu
        self.disk = disk
        self.mem = mem
        self.node_count = node_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.cpu is not None:
            result['cpu'] = self.cpu
        if self.disk is not None:
            result['disk'] = self.disk
        if self.mem is not None:
            result['mem'] = self.mem
        if self.node_count is not None:
            result['nodeCount'] = self.node_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        if m.get('disk') is not None:
            self.disk = m.get('disk')
        if m.get('mem') is not None:
            self.mem = m.get('mem')
        if m.get('nodeCount') is not None:
            self.node_count = m.get('nodeCount')
        return self


class ListInstancesResponseBodyResultSpec(TeaModel):
    def __init__(
        self,
        qrs_resource: ListInstancesResponseBodyResultSpecQrsResource = None,
        search_resource: ListInstancesResponseBodyResultSpecSearchResource = None,
    ):
        self.qrs_resource = qrs_resource
        self.search_resource = search_resource

    def validate(self):
        if self.qrs_resource:
            self.qrs_resource.validate()
        if self.search_resource:
            self.search_resource.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.qrs_resource is not None:
            result['qrsResource'] = self.qrs_resource.to_map()
        if self.search_resource is not None:
            result['searchResource'] = self.search_resource.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('qrsResource') is not None:
            temp_model = ListInstancesResponseBodyResultSpecQrsResource()
            self.qrs_resource = temp_model.from_map(m['qrsResource'])
        if m.get('searchResource') is not None:
            temp_model = ListInstancesResponseBodyResultSpecSearchResource()
            self.search_resource = temp_model.from_map(m['searchResource'])
        return self


class ListInstancesResponseBodyResultTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ListInstancesResponseBodyResult(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        commodity_code: str = None,
        create_time: str = None,
        description: str = None,
        edition: str = None,
        expired_time: str = None,
        in_debt: bool = None,
        instance_id: str = None,
        lock_mode: str = None,
        network: ListInstancesResponseBodyResultNetwork = None,
        no_qrs: bool = None,
        resource_group_id: str = None,
        spec: ListInstancesResponseBodyResultSpec = None,
        status: str = None,
        tags: List[ListInstancesResponseBodyResultTags] = None,
        update_time: str = None,
        user_name: str = None,
        version: str = None,
    ):
        # The billing method.
        self.charge_type = charge_type
        # The commodity code of the instance.
        self.commodity_code = commodity_code
        # The time when the instance was created.
        self.create_time = create_time
        # The description of the instance.
        self.description = description
        self.edition = edition
        # The time when the instance expires.
        self.expired_time = expired_time
        # Indicates whether an overdue payment is involved.
        self.in_debt = in_debt
        # The instance ID.
        self.instance_id = instance_id
        # The lock state of the instance.
        self.lock_mode = lock_mode
        # The network information of the instance.
        self.network = network
        self.no_qrs = no_qrs
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.spec = spec
        # The instance status.
        self.status = status
        # The tags of the instance.
        self.tags = tags
        # The time when the instance was updated.
        self.update_time = update_time
        self.user_name = user_name
        self.version = version

    def validate(self):
        if self.network:
            self.network.validate()
        if self.spec:
            self.spec.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.edition is not None:
            result['edition'] = self.edition
        if self.expired_time is not None:
            result['expiredTime'] = self.expired_time
        if self.in_debt is not None:
            result['inDebt'] = self.in_debt
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.lock_mode is not None:
            result['lockMode'] = self.lock_mode
        if self.network is not None:
            result['network'] = self.network.to_map()
        if self.no_qrs is not None:
            result['noQrs'] = self.no_qrs
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        if self.status is not None:
            result['status'] = self.status
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.user_name is not None:
            result['userName'] = self.user_name
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('edition') is not None:
            self.edition = m.get('edition')
        if m.get('expiredTime') is not None:
            self.expired_time = m.get('expiredTime')
        if m.get('inDebt') is not None:
            self.in_debt = m.get('inDebt')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('lockMode') is not None:
            self.lock_mode = m.get('lockMode')
        if m.get('network') is not None:
            temp_model = ListInstancesResponseBodyResultNetwork()
            self.network = temp_model.from_map(m['network'])
        if m.get('noQrs') is not None:
            self.no_qrs = m.get('noQrs')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('spec') is not None:
            temp_model = ListInstancesResponseBodyResultSpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('status') is not None:
            self.status = m.get('status')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = ListInstancesResponseBodyResultTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListInstancesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListInstancesResponseBodyResult] = None,
        total_count: int = None,
    ):
        # The ID of the request
        self.request_id = request_id
        # The results returned.
        self.result = result
        # The total number of entries returned
        self.total_count = total_count

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListInstancesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLogsRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        page_num: str = None,
        page_size: str = None,
        query: str = None,
        start_time: str = None,
        type: str = None,
    ):
        # The end tim. The value is a timestamp in seconds.
        self.end_time = end_time
        # The number of entries per num. Default value: 1.
        self.page_num = page_num
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The query statement
        self.query = query
        # The start time. The value is a timestamp in seconds.
        self.start_time = start_time
        # -push   -select
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.query is not None:
            result['query'] = self.query
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListLogsResponseBodyResult(TeaModel):
    def __init__(
        self,
        result: List[Any] = None,
        total_count: int = None,
    ):
        # The result.
        self.result = result
        # The total number of entries returned
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListLogsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ListLogsResponseBodyResult = None,
    ):
        # id of request
        self.request_id = request_id
        # ListResult
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = ListLogsResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class ListLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListLogsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOnlineConfigsRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
    ):
        # The name of the domain
        # 
        # This parameter is required.
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        return self


class ListOnlineConfigsResponseBodyResult(TeaModel):
    def __init__(
        self,
        config: str = None,
        index_name: str = None,
    ):
        # The configuration information
        self.config = config
        # The name of the index
        self.index_name = index_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['config'] = self.config
        if self.index_name is not None:
            result['indexName'] = self.index_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            self.config = m.get('config')
        if m.get('indexName') is not None:
            self.index_name = m.get('indexName')
        return self


class ListOnlineConfigsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListOnlineConfigsResponseBodyResult] = None,
    ):
        # id of request
        self.request_id = request_id
        # List
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListOnlineConfigsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListOnlineConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListOnlineConfigsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListOnlineConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPausePolicysResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, ResultValue] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The result.
        self.result = result

    def validate(self):
        if self.result:
            for v in self.result.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = {}
        if self.result is not None:
            for k, v in self.result.items():
                result['result'][k] = v.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = {}
        if m.get('result') is not None:
            for k, v in m.get('result').items():
                temp_model = ResultValue()
                self.result[k] = temp_model.from_map(v)
        return self


class ListPausePolicysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPausePolicysResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListPausePolicysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPostQueryResultRequest(TeaModel):
    def __init__(
        self,
        address: str = None,
        body: Dict[str, Any] = None,
        type: str = None,
    ):
        # The instance endpoint.
        self.address = address
        # The request body.
        self.body = body
        # The query type. Valid values: sql: SQL query. ha3: Havenask query.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['address'] = self.address
        if self.body is not None:
            result['body'] = self.body
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            self.address = m.get('address')
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListPostQueryResultResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Any = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The result.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ListPostQueryResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPostQueryResultResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListPostQueryResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListQueryResultRequest(TeaModel):
    def __init__(
        self,
        query: str = None,
        sql: str = None,
    ):
        # The query statement
        self.query = query
        # The SQL statement that is executed in the query
        self.sql = sql

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.query is not None:
            result['query'] = self.query
        if self.sql is not None:
            result['sql'] = self.sql
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('sql') is not None:
            self.sql = m.get('sql')
        return self


class ListQueryResultResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListQueryResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListQueryResultResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListQueryResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRestQueryResultRequest(TeaModel):
    def __init__(
        self,
        address: str = None,
        index_name: str = None,
        query: Dict[str, Any] = None,
    ):
        # The instance endpoint.
        self.address = address
        # The name of the index table.
        self.index_name = index_name
        # The rest query statement.
        self.query = query

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['address'] = self.address
        if self.index_name is not None:
            result['indexName'] = self.index_name
        if self.query is not None:
            result['query'] = self.query
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            self.address = m.get('address')
        if m.get('indexName') is not None:
            self.index_name = m.get('indexName')
        if m.get('query') is not None:
            self.query = m.get('query')
        return self


class ListRestQueryResultResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Any = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The result.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ListRestQueryResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRestQueryResultResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListRestQueryResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSchemasRequest(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        access_secret: str = None,
        endpoint: str = None,
        namespace: str = None,
        partition: str = None,
        project: str = None,
        table: str = None,
        type: str = None,
    ):
        # The AccessKey ID of the MaxCompute data source.
        self.access_key = access_key
        # The AccessKey secret of the MaxCompute data source.
        self.access_secret = access_secret
        # The endpoint of the MaxCompute data source.
        self.endpoint = endpoint
        # The namespace of the SARO data source.
        self.namespace = namespace
        # The shard name.
        self.partition = partition
        # The name of the MaxCompute project that is used as the data source.
        self.project = project
        # The name of the MaxCompute table that is used as the data source.
        self.table = table
        # The type of the data source. Valid values: odps, swift, saro, oss, and unKnow.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.access_secret is not None:
            result['accessSecret'] = self.access_secret
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.partition is not None:
            result['partition'] = self.partition
        if self.project is not None:
            result['project'] = self.project
        if self.table is not None:
            result['table'] = self.table
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('accessSecret') is not None:
            self.access_secret = m.get('accessSecret')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('partition') is not None:
            self.partition = m.get('partition')
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('table') is not None:
            self.table = m.get('table')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListSchemasResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Any = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The result.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ListSchemasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSchemasResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListSchemasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTableGenerationsResponseBodyResult(TeaModel):
    def __init__(
        self,
        generation_id: int = None,
    ):
        # The ID of the full index version.
        self.generation_id = generation_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.generation_id is not None:
            result['generationId'] = self.generation_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('generationId') is not None:
            self.generation_id = m.get('generationId')
        return self


class ListTableGenerationsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListTableGenerationsResponseBodyResult] = None,
    ):
        # requestId
        self.request_id = request_id
        # The result.
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListTableGenerationsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListTableGenerationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTableGenerationsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTableGenerationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTablesRequest(TeaModel):
    def __init__(
        self,
        new_mode: bool = None,
    ):
        # Specifies whether the OpenSearch Vector Search Edition instance is of the new version.
        self.new_mode = new_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_mode is not None:
            result['newMode'] = self.new_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('newMode') is not None:
            self.new_mode = m.get('newMode')
        return self


class ListTablesResponseBodyResult(TeaModel):
    def __init__(
        self,
        index_status: str = None,
        name: str = None,
        status: str = None,
    ):
        # The state of the index table. Valid values: NEW, PUBLISH, IN_USE, NOT_USE, STOP_USE, RESTORE_USE, and FAIL. After an index is created in an OpenSearch Retrieval Engine Edition instance, the index enters the IN_USE state. If the first full index fails to be created in an OpenSearch Vector Search Edition instance of the new version, the index is in the FAIL state.
        self.index_status = index_status
        # The index name.
        self.name = name
        # The state of the index table. Valid values: NEW, PUBLISH, IN_USE, NOT_USE, STOP_USE, RESTORE_USE, and FAIL. After an index is created in an OpenSearch Retrieval Engine Edition instance, the index enters the IN_USE state. If the first full index fails to be created in an OpenSearch Vector Search Edition instance of the new version, the index is in the FAIL state.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index_status is not None:
            result['indexStatus'] = self.index_status
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('indexStatus') is not None:
            self.index_status = m.get('indexStatus')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListTablesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListTablesResponseBodyResult] = None,
    ):
        # requestId
        self.request_id = request_id
        # The result.
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListTablesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListTablesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTablesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTablesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        self.next_token = next_token
        self.resource_id = resource_id
        # This parameter is required.
        self.resource_type = resource_type
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        result['tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        self.tag = []
        if m.get('tag') is not None:
            for k in m.get('tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesShrinkRequest(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        resource_id_shrink: str = None,
        resource_type: str = None,
        tag_shrink: str = None,
    ):
        self.next_token = next_token
        self.resource_id_shrink = resource_id_shrink
        # This parameter is required.
        self.resource_type = resource_type
        self.tag_shrink = tag_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.resource_id_shrink is not None:
            result['resourceId'] = self.resource_id_shrink
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.tag_shrink is not None:
            result['tag'] = self.tag_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('resourceId') is not None:
            self.resource_id_shrink = m.get('resourceId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('tag') is not None:
            self.tag_shrink = m.get('tag')
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.tag_key is not None:
            result['tagKey'] = self.tag_key
        if self.tag_value is not None:
            result['tagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('tagKey') is not None:
            self.tag_key = m.get('tagKey')
        if m.get('tagValue') is not None:
            self.tag_value = m.get('tagValue')
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_resources: List[ListTagResourcesResponseBodyTagResources] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['tagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['tagResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.tag_resources = []
        if m.get('tagResources') is not None:
            for k in m.get('tagResources'):
                temp_model = ListTagResourcesResponseBodyTagResources()
                self.tag_resources.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTasksRequest(TeaModel):
    def __init__(
        self,
        end: int = None,
        start: int = None,
    ):
        # The timestamp that indicates the end of the time range to query.
        self.end = end
        # The timestamp that indicates the beginning of the time range to query.
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['end'] = self.end
        if self.start is not None:
            result['start'] = self.start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('end') is not None:
            self.end = m.get('end')
        if m.get('start') is not None:
            self.start = m.get('start')
        return self


class ListTasksResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Any = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The result.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ListTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTasksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVectorQueryResultRequest(TeaModel):
    def __init__(
        self,
        address: str = None,
        body: Dict[str, Any] = None,
        query_type: str = None,
        vector_query_type: str = None,
    ):
        # The instance endpoint.
        self.address = address
        # The request body.
        self.body = body
        # The query type. Valid values: vector, primary_key, and vector_text.
        self.query_type = query_type
        # The vector query type. Valid values: vector, image, and text.
        self.vector_query_type = vector_query_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['address'] = self.address
        if self.body is not None:
            result['body'] = self.body
        if self.query_type is not None:
            result['queryType'] = self.query_type
        if self.vector_query_type is not None:
            result['vectorQueryType'] = self.vector_query_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            self.address = m.get('address')
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('queryType') is not None:
            self.query_type = m.get('queryType')
        if m.get('vectorQueryType') is not None:
            self.vector_query_type = m.get('vectorQueryType')
        return self


class ListVectorQueryResultResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Any = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The result.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ListVectorQueryResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListVectorQueryResultResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListVectorQueryResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAdvanceConfigRequestFiles(TeaModel):
    def __init__(
        self,
        full_path_name: str = None,
        is_dir: bool = None,
        is_template: bool = None,
        name: str = None,
    ):
        # The full path of the file.
        self.full_path_name = full_path_name
        # Specifies whether the file is a directory.
        self.is_dir = is_dir
        # Specifies whether the file is a template.
        self.is_template = is_template
        # The node name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.full_path_name is not None:
            result['fullPathName'] = self.full_path_name
        if self.is_dir is not None:
            result['isDir'] = self.is_dir
        if self.is_template is not None:
            result['isTemplate'] = self.is_template
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fullPathName') is not None:
            self.full_path_name = m.get('fullPathName')
        if m.get('isDir') is not None:
            self.is_dir = m.get('isDir')
        if m.get('isTemplate') is not None:
            self.is_template = m.get('isTemplate')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ModifyAdvanceConfigRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        content_type: str = None,
        desc: str = None,
        files: List[ModifyAdvanceConfigRequestFiles] = None,
        name: str = None,
        status: str = None,
        update_time: int = None,
    ):
        # The content of the advanced configuration that is returned.
        self.content = content
        # The type of the configuration content. Valid values: FILE, GIT, HTTP, and ODPS.
        self.content_type = content_type
        # The description of the advanced configuration.
        self.desc = desc
        # The files.
        self.files = files
        # The name of the advanced configuration.
        self.name = name
        # The status of the advanced configuration. Valid values: drafting: The advanced configuration is in the draft state. used: The advanced configuration is being used. unused: The advanced configuration is not used. trash: The advanced configuration is being deleted.
        self.status = status
        # The time when the advanced configuration was updated.
        self.update_time = update_time

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.content_type is not None:
            result['contentType'] = self.content_type
        if self.desc is not None:
            result['desc'] = self.desc
        result['files'] = []
        if self.files is not None:
            for k in self.files:
                result['files'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        self.files = []
        if m.get('files') is not None:
            for k in m.get('files'):
                temp_model = ModifyAdvanceConfigRequestFiles()
                self.files.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class ModifyAdvanceConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The result.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ModifyAdvanceConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyAdvanceConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyAdvanceConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAdvanceConfigFileRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        variables: Dict[str, VariablesValue] = None,
        file_name: str = None,
    ):
        # The file content.
        self.content = content
        # The variables.
        self.variables = variables
        # The name of the file.
        # 
        # This parameter is required.
        self.file_name = file_name

    def validate(self):
        if self.variables:
            for v in self.variables.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        result['variables'] = {}
        if self.variables is not None:
            for k, v in self.variables.items():
                result['variables'][k] = v.to_map()
        if self.file_name is not None:
            result['fileName'] = self.file_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        self.variables = {}
        if m.get('variables') is not None:
            for k, v in m.get('variables').items():
                temp_model = VariablesValue()
                self.variables[k] = temp_model.from_map(v)
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        return self


class ModifyAdvanceConfigFileResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # id of request
        self.request_id = request_id
        # The result.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ModifyAdvanceConfigFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyAdvanceConfigFileResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyAdvanceConfigFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAliasRequest(TeaModel):
    def __init__(
        self,
        alias: str = None,
        index: str = None,
    ):
        # alias name
        self.alias = alias
        # index name
        self.index = index

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['alias'] = self.alias
        if self.index is not None:
            result['index'] = self.index
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alias') is not None:
            self.alias = m.get('alias')
        if m.get('index') is not None:
            self.index = m.get('index')
        return self


class ModifyAliasResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # id of request
        self.request_id = request_id
        # Map
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ModifyAliasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyAliasResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyAliasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyClusterDescRequest(TeaModel):
    def __init__(
        self,
        body: Dict[str, Any] = None,
    ):
        # The request body.
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class ModifyClusterDescResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The ID of the request
        self.request_id = request_id
        # The result.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ModifyClusterDescResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyClusterDescResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyClusterDescResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyClusterOfflineConfigRequest(TeaModel):
    def __init__(
        self,
        build_mode: str = None,
        config: Dict[str, int] = None,
        data_source_name: str = None,
        data_source_type: str = None,
        data_time_sec: int = None,
        domain: str = None,
        generation: int = None,
        partition: str = None,
        push_mode: str = None,
    ):
        # The reindexing method. Valid values: api: API data source. indexRecover: data recovery by using indexing.
        self.build_mode = build_mode
        # The configuration name, which is stored as a key.
        self.config = config
        # The name of the data source.
        self.data_source_name = data_source_name
        # The type of the data source. Valid values: odps: MaxCompute. swift: Swift. unKnow: unknown type.
        self.data_source_type = data_source_type
        # This parameter is required when index building by using API data sources is triggered.
        self.data_time_sec = data_time_sec
        # The data center in which the data source is deployed.
        self.domain = domain
        # The ID of the full index version.
        self.generation = generation
        # This parameter is required when index building for full data in a MaxCompute data source is triggered.
        self.partition = partition
        # The push mode of the configuration. By default, only the configuration is pushed.
        self.push_mode = push_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_mode is not None:
            result['buildMode'] = self.build_mode
        if self.config is not None:
            result['config'] = self.config
        if self.data_source_name is not None:
            result['dataSourceName'] = self.data_source_name
        if self.data_source_type is not None:
            result['dataSourceType'] = self.data_source_type
        if self.data_time_sec is not None:
            result['dataTimeSec'] = self.data_time_sec
        if self.domain is not None:
            result['domain'] = self.domain
        if self.generation is not None:
            result['generation'] = self.generation
        if self.partition is not None:
            result['partition'] = self.partition
        if self.push_mode is not None:
            result['pushMode'] = self.push_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('buildMode') is not None:
            self.build_mode = m.get('buildMode')
        if m.get('config') is not None:
            self.config = m.get('config')
        if m.get('dataSourceName') is not None:
            self.data_source_name = m.get('dataSourceName')
        if m.get('dataSourceType') is not None:
            self.data_source_type = m.get('dataSourceType')
        if m.get('dataTimeSec') is not None:
            self.data_time_sec = m.get('dataTimeSec')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('generation') is not None:
            self.generation = m.get('generation')
        if m.get('partition') is not None:
            self.partition = m.get('partition')
        if m.get('pushMode') is not None:
            self.push_mode = m.get('pushMode')
        return self


class ModifyClusterOfflineConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The ID of the request
        self.request_id = request_id
        # The result
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ModifyClusterOfflineConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyClusterOfflineConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyClusterOfflineConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyClusterOnlineConfigRequest(TeaModel):
    def __init__(
        self,
        clusters: List[str] = None,
        config: Dict[str, int] = None,
    ):
        # The cluster information.
        self.clusters = clusters
        # The configuration information.
        self.config = config

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clusters is not None:
            result['clusters'] = self.clusters
        if self.config is not None:
            result['config'] = self.config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusters') is not None:
            self.clusters = m.get('clusters')
        if m.get('config') is not None:
            self.config = m.get('config')
        return self


class ModifyClusterOnlineConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The ID of the request
        self.request_id = request_id
        # Map
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ModifyClusterOnlineConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyClusterOnlineConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyClusterOnlineConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDataSourceDeployRequestExtendHdfs(TeaModel):
    def __init__(
        self,
        path: str = None,
    ):
        # The path of the Apsara File Storage for HDFS data source.
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('path') is not None:
            self.path = m.get('path')
        return self


class ModifyDataSourceDeployRequestExtendOdps(TeaModel):
    def __init__(
        self,
        partitions: Dict[str, str] = None,
    ):
        # The partitions in the MaxCompute table.
        self.partitions = partitions

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.partitions is not None:
            result['partitions'] = self.partitions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('partitions') is not None:
            self.partitions = m.get('partitions')
        return self


class ModifyDataSourceDeployRequestExtendOss(TeaModel):
    def __init__(
        self,
        path: str = None,
    ):
        # The path of the OSS data source.
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('path') is not None:
            self.path = m.get('path')
        return self


class ModifyDataSourceDeployRequestExtendSaro(TeaModel):
    def __init__(
        self,
        path: str = None,
        version: str = None,
    ):
        # The path of the SARO data source.
        self.path = path
        # The version number of the SARO data source.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['path'] = self.path
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ModifyDataSourceDeployRequestExtend(TeaModel):
    def __init__(
        self,
        hdfs: ModifyDataSourceDeployRequestExtendHdfs = None,
        odps: ModifyDataSourceDeployRequestExtendOdps = None,
        oss: ModifyDataSourceDeployRequestExtendOss = None,
        saro: ModifyDataSourceDeployRequestExtendSaro = None,
    ):
        # The information about the Apsara File Storage for HDFS data source.
        self.hdfs = hdfs
        # The information about the MaxCompute data source.
        self.odps = odps
        # The information about the OSS data source.
        self.oss = oss
        # The information about the SARO data source. This parameter is applicable to the SARO data source used in the intranet of Alibaba Group.
        self.saro = saro

    def validate(self):
        if self.hdfs:
            self.hdfs.validate()
        if self.odps:
            self.odps.validate()
        if self.oss:
            self.oss.validate()
        if self.saro:
            self.saro.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hdfs is not None:
            result['hdfs'] = self.hdfs.to_map()
        if self.odps is not None:
            result['odps'] = self.odps.to_map()
        if self.oss is not None:
            result['oss'] = self.oss.to_map()
        if self.saro is not None:
            result['saro'] = self.saro.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hdfs') is not None:
            temp_model = ModifyDataSourceDeployRequestExtendHdfs()
            self.hdfs = temp_model.from_map(m['hdfs'])
        if m.get('odps') is not None:
            temp_model = ModifyDataSourceDeployRequestExtendOdps()
            self.odps = temp_model.from_map(m['odps'])
        if m.get('oss') is not None:
            temp_model = ModifyDataSourceDeployRequestExtendOss()
            self.oss = temp_model.from_map(m['oss'])
        if m.get('saro') is not None:
            temp_model = ModifyDataSourceDeployRequestExtendSaro()
            self.saro = temp_model.from_map(m['saro'])
        return self


class ModifyDataSourceDeployRequestProcessor(TeaModel):
    def __init__(
        self,
        args: str = None,
        resource: str = None,
    ):
        # The startup parameters of the process.
        self.args = args
        # The resource information.
        self.resource = resource

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.args is not None:
            result['args'] = self.args
        if self.resource is not None:
            result['resource'] = self.resource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('args') is not None:
            self.args = m.get('args')
        if m.get('resource') is not None:
            self.resource = m.get('resource')
        return self


class ModifyDataSourceDeployRequestStorage(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        access_secret: str = None,
        bucket: str = None,
        endpoint: str = None,
        namespace: str = None,
        oss_path: str = None,
        partition: str = None,
        path: str = None,
        project: str = None,
        table: str = None,
    ):
        # The AccessKey ID of the MaxCompute data source.
        self.access_key = access_key
        # The AccessKey secret of the MaxCompute data source.
        self.access_secret = access_secret
        # The name of the OSS bucket.
        self.bucket = bucket
        # The endpoint of the MaxCompute data source.
        self.endpoint = endpoint
        # The namespace. This parameter is applicable to the SARO data source used in the intranet of Alibaba Group.
        self.namespace = namespace
        # The Object Storage Service (OSS) path.
        self.oss_path = oss_path
        # The partition in the MaxCompute table.
        self.partition = partition
        # The file path in the Apsara File Storage for HDFS file system.
        self.path = path
        # The name of the MaxCompute project that is used as the data source.
        self.project = project
        # The name of the MaxCompute table that is used as the data source.
        self.table = table

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.access_secret is not None:
            result['accessSecret'] = self.access_secret
        if self.bucket is not None:
            result['bucket'] = self.bucket
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.oss_path is not None:
            result['ossPath'] = self.oss_path
        if self.partition is not None:
            result['partition'] = self.partition
        if self.path is not None:
            result['path'] = self.path
        if self.project is not None:
            result['project'] = self.project
        if self.table is not None:
            result['table'] = self.table
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('accessSecret') is not None:
            self.access_secret = m.get('accessSecret')
        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('ossPath') is not None:
            self.oss_path = m.get('ossPath')
        if m.get('partition') is not None:
            self.partition = m.get('partition')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('table') is not None:
            self.table = m.get('table')
        return self


class ModifyDataSourceDeployRequestSwift(TeaModel):
    def __init__(
        self,
        topic: str = None,
        zk: str = None,
    ):
        # The topic.
        self.topic = topic
        # zk
        self.zk = zk

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.topic is not None:
            result['topic'] = self.topic
        if self.zk is not None:
            result['zk'] = self.zk
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('topic') is not None:
            self.topic = m.get('topic')
        if m.get('zk') is not None:
            self.zk = m.get('zk')
        return self


class ModifyDataSourceDeployRequest(TeaModel):
    def __init__(
        self,
        auto_build_index: bool = None,
        extend: ModifyDataSourceDeployRequestExtend = None,
        processor: ModifyDataSourceDeployRequestProcessor = None,
        storage: ModifyDataSourceDeployRequestStorage = None,
        swift: ModifyDataSourceDeployRequestSwift = None,
        dry_run: bool = None,
        generation_id: int = None,
    ):
        # Specifies whether to enable the automatic full indexing feature.
        self.auto_build_index = auto_build_index
        # The extended information.
        self.extend = extend
        # The parameters of the process.
        self.processor = processor
        # The information about the data source.
        self.storage = storage
        # The information about the incremental data source Swift.
        self.swift = swift
        # Specifies whether to perform only a dry run, without performing the actual request. The system only checks the validity of the data source. Valid values: true and false.
        self.dry_run = dry_run
        # The ID of the full index version.
        self.generation_id = generation_id

    def validate(self):
        if self.extend:
            self.extend.validate()
        if self.processor:
            self.processor.validate()
        if self.storage:
            self.storage.validate()
        if self.swift:
            self.swift.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_build_index is not None:
            result['autoBuildIndex'] = self.auto_build_index
        if self.extend is not None:
            result['extend'] = self.extend.to_map()
        if self.processor is not None:
            result['processor'] = self.processor.to_map()
        if self.storage is not None:
            result['storage'] = self.storage.to_map()
        if self.swift is not None:
            result['swift'] = self.swift.to_map()
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        if self.generation_id is not None:
            result['generationId'] = self.generation_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoBuildIndex') is not None:
            self.auto_build_index = m.get('autoBuildIndex')
        if m.get('extend') is not None:
            temp_model = ModifyDataSourceDeployRequestExtend()
            self.extend = temp_model.from_map(m['extend'])
        if m.get('processor') is not None:
            temp_model = ModifyDataSourceDeployRequestProcessor()
            self.processor = temp_model.from_map(m['processor'])
        if m.get('storage') is not None:
            temp_model = ModifyDataSourceDeployRequestStorage()
            self.storage = temp_model.from_map(m['storage'])
        if m.get('swift') is not None:
            temp_model = ModifyDataSourceDeployRequestSwift()
            self.swift = temp_model.from_map(m['swift'])
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        if m.get('generationId') is not None:
            self.generation_id = m.get('generationId')
        return self


class ModifyDataSourceDeployResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The result.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ModifyDataSourceDeployResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDataSourceDeployResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyDataSourceDeployResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyFileRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        partition: int = None,
        file_name: str = None,
    ):
        # The file content.
        self.content = content
        # The number of shards.
        self.partition = partition
        # The name of the file in the full path
        # 
        # This parameter is required.
        self.file_name = file_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.partition is not None:
            result['partition'] = self.partition
        if self.file_name is not None:
            result['fileName'] = self.file_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('partition') is not None:
            self.partition = m.get('partition')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        return self


class ModifyFileResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # id of request
        self.request_id = request_id
        # The information about the index
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ModifyFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyFileResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyIndexRequestDataSourceInfoConfig(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        access_secret: str = None,
        bucket: str = None,
        endpoint: str = None,
        namespace: str = None,
        oss_path: str = None,
        partition: str = None,
        path: str = None,
        project: str = None,
        table: str = None,
    ):
        # The AccessKey ID of the MaxCompute data source.
        self.access_key = access_key
        # The AccessKey secret of the MaxCompute data source.
        self.access_secret = access_secret
        # The name of the OSS bucket.
        self.bucket = bucket
        # The endpoint of the MaxCompute data source.
        self.endpoint = endpoint
        # The namespace. This parameter is applicable to the SARO data source used in the intranet of Alibaba Group.
        self.namespace = namespace
        # The Object Storage Service (OSS) path.
        self.oss_path = oss_path
        # The partition in the MaxCompute table. Example: ds=20180102.
        self.partition = partition
        # The file path in the Apsara File Storage for HDFS file system.
        self.path = path
        # The name of the MaxCompute project that is used as the data source.
        self.project = project
        # The name of the MaxCompute table that is used as the data source.
        self.table = table

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.access_secret is not None:
            result['accessSecret'] = self.access_secret
        if self.bucket is not None:
            result['bucket'] = self.bucket
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.oss_path is not None:
            result['ossPath'] = self.oss_path
        if self.partition is not None:
            result['partition'] = self.partition
        if self.path is not None:
            result['path'] = self.path
        if self.project is not None:
            result['project'] = self.project
        if self.table is not None:
            result['table'] = self.table
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('accessSecret') is not None:
            self.access_secret = m.get('accessSecret')
        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('ossPath') is not None:
            self.oss_path = m.get('ossPath')
        if m.get('partition') is not None:
            self.partition = m.get('partition')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('table') is not None:
            self.table = m.get('table')
        return self


class ModifyIndexRequestDataSourceInfoSaroConfig(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        table_name: str = None,
    ):
        # The namespace to which the SARO data source belongs.
        self.namespace = namespace
        # The name of the SARO table.
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.table_name is not None:
            result['tableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        return self


class ModifyIndexRequestDataSourceInfo(TeaModel):
    def __init__(
        self,
        auto_build_index: bool = None,
        build_mode: str = None,
        config: ModifyIndexRequestDataSourceInfoConfig = None,
        data_time_sec: int = None,
        domain: str = None,
        generation: int = None,
        name: str = None,
        process_parallel_num: int = None,
        process_partition_count: int = None,
        saro_config: ModifyIndexRequestDataSourceInfoSaroConfig = None,
        type: str = None,
    ):
        # Specifies whether to enable the automatic full indexing feature.
        self.auto_build_index = auto_build_index
        # The reindexing method. Valid values: api: API data source. indexRecover: data recovery by using indexing.
        self.build_mode = build_mode
        # The configurations of the MaxCompute data source.
        self.config = config
        # The start timestamp from which incremental data is retrieved.
        self.data_time_sec = data_time_sec
        # The offline deployment name of the data source.
        self.domain = domain
        # The ID of the index version from which data is restored.
        self.generation = generation
        # The name of the data source.
        self.name = name
        # The maximum number of full indexes that can be concurrently processed.
        self.process_parallel_num = process_parallel_num
        # The number of resources used for data update.
        self.process_partition_count = process_partition_count
        # The configurations of the SARO data source.
        self.saro_config = saro_config
        # The type of the data source. Valid values: odps, swift, saro, oss, and unKnow.
        self.type = type

    def validate(self):
        if self.config:
            self.config.validate()
        if self.saro_config:
            self.saro_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_build_index is not None:
            result['autoBuildIndex'] = self.auto_build_index
        if self.build_mode is not None:
            result['buildMode'] = self.build_mode
        if self.config is not None:
            result['config'] = self.config.to_map()
        if self.data_time_sec is not None:
            result['dataTimeSec'] = self.data_time_sec
        if self.domain is not None:
            result['domain'] = self.domain
        if self.generation is not None:
            result['generation'] = self.generation
        if self.name is not None:
            result['name'] = self.name
        if self.process_parallel_num is not None:
            result['processParallelNum'] = self.process_parallel_num
        if self.process_partition_count is not None:
            result['processPartitionCount'] = self.process_partition_count
        if self.saro_config is not None:
            result['saroConfig'] = self.saro_config.to_map()
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoBuildIndex') is not None:
            self.auto_build_index = m.get('autoBuildIndex')
        if m.get('buildMode') is not None:
            self.build_mode = m.get('buildMode')
        if m.get('config') is not None:
            temp_model = ModifyIndexRequestDataSourceInfoConfig()
            self.config = temp_model.from_map(m['config'])
        if m.get('dataTimeSec') is not None:
            self.data_time_sec = m.get('dataTimeSec')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('generation') is not None:
            self.generation = m.get('generation')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('processParallelNum') is not None:
            self.process_parallel_num = m.get('processParallelNum')
        if m.get('processPartitionCount') is not None:
            self.process_partition_count = m.get('processPartitionCount')
        if m.get('saroConfig') is not None:
            temp_model = ModifyIndexRequestDataSourceInfoSaroConfig()
            self.saro_config = temp_model.from_map(m['saroConfig'])
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ModifyIndexRequest(TeaModel):
    def __init__(
        self,
        build_parallel_num: int = None,
        cluster: Dict[str, dict] = None,
        cluster_config_name: str = None,
        config: Dict[str, ConfigValue] = None,
        content: str = None,
        data_source: str = None,
        data_source_info: ModifyIndexRequestDataSourceInfo = None,
        description: str = None,
        domain: str = None,
        merge_parallel_num: int = None,
        partition: int = None,
        push_mode: str = None,
        dry_run: bool = None,
    ):
        # The maximum number of full indexes that can be concurrently built.
        self.build_parallel_num = build_parallel_num
        # The cluster information.
        self.cluster = cluster
        # The name of the configuration file.
        self.cluster_config_name = cluster_config_name
        # The information about the offline configuration.
        self.config = config
        # The file content.
        self.content = content
        # The name of the data source.
        self.data_source = data_source
        # The information about the data source, which is required for the new version of OpenSearch Vector Search Edition.
        self.data_source_info = data_source_info
        # The description of the data source.
        self.description = description
        # The name of the data center in which the data source is deployed.
        self.domain = domain
        # The maximum number of full indexes that can be concurrently merged.
        self.merge_parallel_num = merge_parallel_num
        # The number of shards.
        self.partition = partition
        # The push mode of the configuration. By default, only the configuration is pushed.
        self.push_mode = push_mode
        # Specifies whether to check the validity of input parameters. Default value: false.
        # 
        # Valid values:
        # 
        # *   **true**: checks only the validity of input parameters.
        # *   **false**: checks the validity of input parameters and creates an attribution configuration.
        self.dry_run = dry_run

    def validate(self):
        if self.config:
            for v in self.config.values():
                if v:
                    v.validate()
        if self.data_source_info:
            self.data_source_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_parallel_num is not None:
            result['buildParallelNum'] = self.build_parallel_num
        if self.cluster is not None:
            result['cluster'] = self.cluster
        if self.cluster_config_name is not None:
            result['clusterConfigName'] = self.cluster_config_name
        result['config'] = {}
        if self.config is not None:
            for k, v in self.config.items():
                result['config'][k] = v.to_map()
        if self.content is not None:
            result['content'] = self.content
        if self.data_source is not None:
            result['dataSource'] = self.data_source
        if self.data_source_info is not None:
            result['dataSourceInfo'] = self.data_source_info.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.domain is not None:
            result['domain'] = self.domain
        if self.merge_parallel_num is not None:
            result['mergeParallelNum'] = self.merge_parallel_num
        if self.partition is not None:
            result['partition'] = self.partition
        if self.push_mode is not None:
            result['pushMode'] = self.push_mode
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('buildParallelNum') is not None:
            self.build_parallel_num = m.get('buildParallelNum')
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('clusterConfigName') is not None:
            self.cluster_config_name = m.get('clusterConfigName')
        self.config = {}
        if m.get('config') is not None:
            for k, v in m.get('config').items():
                temp_model = ConfigValue()
                self.config[k] = temp_model.from_map(v)
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('dataSource') is not None:
            self.data_source = m.get('dataSource')
        if m.get('dataSourceInfo') is not None:
            temp_model = ModifyIndexRequestDataSourceInfo()
            self.data_source_info = temp_model.from_map(m['dataSourceInfo'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('mergeParallelNum') is not None:
            self.merge_parallel_num = m.get('mergeParallelNum')
        if m.get('partition') is not None:
            self.partition = m.get('partition')
        if m.get('pushMode') is not None:
            self.push_mode = m.get('pushMode')
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class ModifyIndexResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Any = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The result.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ModifyIndexResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyIndexResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyIndexResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyIndexOnlineStrategyRequest(TeaModel):
    def __init__(
        self,
        change_rate: int = None,
    ):
        # The index change rate.
        self.change_rate = change_rate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_rate is not None:
            result['changeRate'] = self.change_rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('changeRate') is not None:
            self.change_rate = m.get('changeRate')
        return self


class ModifyIndexOnlineStrategyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The result.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ModifyIndexOnlineStrategyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyIndexOnlineStrategyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyIndexOnlineStrategyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyIndexPartitionRequestIndexInfos(TeaModel):
    def __init__(
        self,
        index_name: str = None,
        parallel_num: int = None,
        partition_count: int = None,
    ):
        # The index name.
        self.index_name = index_name
        # The concurrency. Default value: 1.
        self.parallel_num = parallel_num
        # The number of shards.
        self.partition_count = partition_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index_name is not None:
            result['indexName'] = self.index_name
        if self.parallel_num is not None:
            result['parallelNum'] = self.parallel_num
        if self.partition_count is not None:
            result['partitionCount'] = self.partition_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('indexName') is not None:
            self.index_name = m.get('indexName')
        if m.get('parallelNum') is not None:
            self.parallel_num = m.get('parallelNum')
        if m.get('partitionCount') is not None:
            self.partition_count = m.get('partitionCount')
        return self


class ModifyIndexPartitionRequest(TeaModel):
    def __init__(
        self,
        data_source_name: str = None,
        domain_name: str = None,
        generation: int = None,
        index_infos: List[ModifyIndexPartitionRequestIndexInfos] = None,
    ):
        # The name of the data source.
        self.data_source_name = data_source_name
        # The data center.
        self.domain_name = domain_name
        # The primary key.
        self.generation = generation
        # The index information.
        self.index_infos = index_infos

    def validate(self):
        if self.index_infos:
            for k in self.index_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_name is not None:
            result['dataSourceName'] = self.data_source_name
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
        if self.generation is not None:
            result['generation'] = self.generation
        result['indexInfos'] = []
        if self.index_infos is not None:
            for k in self.index_infos:
                result['indexInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataSourceName') is not None:
            self.data_source_name = m.get('dataSourceName')
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        if m.get('generation') is not None:
            self.generation = m.get('generation')
        self.index_infos = []
        if m.get('indexInfos') is not None:
            for k in m.get('indexInfos'):
                temp_model = ModifyIndexPartitionRequestIndexInfos()
                self.index_infos.append(temp_model.from_map(k))
        return self


class ModifyIndexPartitionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # id of request
        self.request_id = request_id
        # Map
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ModifyIndexPartitionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyIndexPartitionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyIndexPartitionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyIndexVersionRequestBody(TeaModel):
    def __init__(
        self,
        build_deploy_id: str = None,
        index_name: str = None,
        version: str = None,
    ):
        # The deployment ID of the data source.
        self.build_deploy_id = build_deploy_id
        # The index name.
        self.index_name = index_name
        # The index version.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_deploy_id is not None:
            result['buildDeployId'] = self.build_deploy_id
        if self.index_name is not None:
            result['indexName'] = self.index_name
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('buildDeployId') is not None:
            self.build_deploy_id = m.get('buildDeployId')
        if m.get('indexName') is not None:
            self.index_name = m.get('indexName')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ModifyIndexVersionRequest(TeaModel):
    def __init__(
        self,
        body: List[ModifyIndexVersionRequestBody] = None,
    ):
        # The request body.
        self.body = body

    def validate(self):
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = ModifyIndexVersionRequestBody()
                self.body.append(temp_model.from_map(k))
        return self


class ModifyIndexVersionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # id of request
        self.request_id = request_id
        # result
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ModifyIndexVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyIndexVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyIndexVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyNodeConfigRequest(TeaModel):
    def __init__(
        self,
        active: bool = None,
        data_duplicate_number: int = None,
        data_fragment_number: int = None,
        flow_ratio: int = None,
        min_service_percent: int = None,
        published: bool = None,
        cluster_name: str = None,
        data_source_name: str = None,
        name: str = None,
        type: str = None,
    ):
        # Specifies whether to enable the index.
        self.active = active
        # The number of data replicas.
        self.data_duplicate_number = data_duplicate_number
        # The number of data shards.
        self.data_fragment_number = data_fragment_number
        # The traffic percentage.
        self.flow_ratio = flow_ratio
        # The minimum service ratio.
        self.min_service_percent = min_service_percent
        # Specifies whether to mount the cluster.
        self.published = published
        # The name of the cluster.
        self.cluster_name = cluster_name
        # The name of the data source. Valid values: -search: search for data. -not_search: do not search for data.
        self.data_source_name = data_source_name
        # The name of the configuration before the modification.
        # 
        # This parameter is required.
        self.name = name
        # The type of the algorithm. Valid values:
        # 
        # *   pop: a popularity model.
        # *   cp: a category prediction model.
        # *   hot: a top search model.
        # *   hint: a hint model.
        # *   suggest: a drop-down suggestions model.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.data_duplicate_number is not None:
            result['dataDuplicateNumber'] = self.data_duplicate_number
        if self.data_fragment_number is not None:
            result['dataFragmentNumber'] = self.data_fragment_number
        if self.flow_ratio is not None:
            result['flowRatio'] = self.flow_ratio
        if self.min_service_percent is not None:
            result['minServicePercent'] = self.min_service_percent
        if self.published is not None:
            result['published'] = self.published
        if self.cluster_name is not None:
            result['clusterName'] = self.cluster_name
        if self.data_source_name is not None:
            result['dataSourceName'] = self.data_source_name
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('dataDuplicateNumber') is not None:
            self.data_duplicate_number = m.get('dataDuplicateNumber')
        if m.get('dataFragmentNumber') is not None:
            self.data_fragment_number = m.get('dataFragmentNumber')
        if m.get('flowRatio') is not None:
            self.flow_ratio = m.get('flowRatio')
        if m.get('minServicePercent') is not None:
            self.min_service_percent = m.get('minServicePercent')
        if m.get('published') is not None:
            self.published = m.get('published')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('dataSourceName') is not None:
            self.data_source_name = m.get('dataSourceName')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ModifyNodeConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # id of request
        self.request_id = request_id
        # The information about the index
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ModifyNodeConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyNodeConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyNodeConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyOnlineConfigRequest(TeaModel):
    def __init__(
        self,
        body: Dict[str, str] = None,
    ):
        # The request body.
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class ModifyOnlineConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # id of request
        self.request_id = request_id
        # Map
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ModifyOnlineConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyOnlineConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyOnlineConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyPasswordRequest(TeaModel):
    def __init__(
        self,
        password: str = None,
        username: str = None,
    ):
        # The password.
        self.password = password
        # The username.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.password is not None:
            result['password'] = self.password
        if self.username is not None:
            result['username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('username') is not None:
            self.username = m.get('username')
        return self


class ModifyPasswordResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The ID of the request
        self.request_id = request_id
        # The result
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ModifyPasswordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyPasswordResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyPausePolicyRequest(TeaModel):
    def __init__(
        self,
        body: Dict[str, BodyValue] = None,
    ):
        # The request body.
        self.body = body

    def validate(self):
        if self.body:
            for v in self.body.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['body'] = {}
        if self.body is not None:
            for k, v in self.body.items():
                result['body'][k] = v.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.body = {}
        if m.get('body') is not None:
            for k, v in m.get('body').items():
                temp_model = BodyValue()
                self.body[k] = temp_model.from_map(v)
        return self


class ModifyPausePolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The result.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ModifyPausePolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyPausePolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyPausePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyPublicUrlIpListRequest(TeaModel):
    def __init__(
        self,
        body: Dict[str, str] = None,
    ):
        # The request body.
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class ModifyPublicUrlIpListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The result.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ModifyPublicUrlIpListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyPublicUrlIpListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyPublicUrlIpListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyTableRequestDataProcessConfigParamsSrcFieldConfig(TeaModel):
    def __init__(
        self,
        oss_bucket: str = None,
        oss_endpoint: str = None,
        uid: str = None,
    ):
        # The name of the OSS bucket.
        self.oss_bucket = oss_bucket
        # The OSS endpoint.
        self.oss_endpoint = oss_endpoint
        # The ID of the Alibaba Cloud account.
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss_bucket is not None:
            result['ossBucket'] = self.oss_bucket
        if self.oss_endpoint is not None:
            result['ossEndpoint'] = self.oss_endpoint
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ossBucket') is not None:
            self.oss_bucket = m.get('ossBucket')
        if m.get('ossEndpoint') is not None:
            self.oss_endpoint = m.get('ossEndpoint')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class ModifyTableRequestDataProcessConfigParams(TeaModel):
    def __init__(
        self,
        src_field_config: ModifyTableRequestDataProcessConfigParamsSrcFieldConfig = None,
        vector_modal: str = None,
        vector_model: str = None,
    ):
        # The source of the data to be vectorized.
        self.src_field_config = src_field_config
        # The data type.
        self.vector_modal = vector_modal
        # The vectorization model.
        self.vector_model = vector_model

    def validate(self):
        if self.src_field_config:
            self.src_field_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.src_field_config is not None:
            result['srcFieldConfig'] = self.src_field_config.to_map()
        if self.vector_modal is not None:
            result['vectorModal'] = self.vector_modal
        if self.vector_model is not None:
            result['vectorModel'] = self.vector_model
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('srcFieldConfig') is not None:
            temp_model = ModifyTableRequestDataProcessConfigParamsSrcFieldConfig()
            self.src_field_config = temp_model.from_map(m['srcFieldConfig'])
        if m.get('vectorModal') is not None:
            self.vector_modal = m.get('vectorModal')
        if m.get('vectorModel') is not None:
            self.vector_model = m.get('vectorModel')
        return self


class ModifyTableRequestDataProcessConfig(TeaModel):
    def __init__(
        self,
        dst_field: str = None,
        operator: str = None,
        params: ModifyTableRequestDataProcessConfigParams = None,
        src_field: str = None,
    ):
        # The destination field.
        self.dst_field = dst_field
        # The method used to process the field. Valid values: copy and vectorize. A value of copy specifies that the value of the source field is copied to the destination field. A value of vectorize specifies that the value of the source field is vectorized by a vectorization model and the output vector is stored in the destination field.
        self.operator = operator
        # The information about the model.
        self.params = params
        # The source field.
        self.src_field = src_field

    def validate(self):
        if self.params:
            self.params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dst_field is not None:
            result['dstField'] = self.dst_field
        if self.operator is not None:
            result['operator'] = self.operator
        if self.params is not None:
            result['params'] = self.params.to_map()
        if self.src_field is not None:
            result['srcField'] = self.src_field
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dstField') is not None:
            self.dst_field = m.get('dstField')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('params') is not None:
            temp_model = ModifyTableRequestDataProcessConfigParams()
            self.params = temp_model.from_map(m['params'])
        if m.get('srcField') is not None:
            self.src_field = m.get('srcField')
        return self


class ModifyTableRequestDataSourceConfig(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        access_secret: str = None,
        bucket: str = None,
        endpoint: str = None,
        oss_path: str = None,
        partition: str = None,
        project: str = None,
        table: str = None,
    ):
        # The AccessKey ID of the MaxCompute data source.
        self.access_key = access_key
        # The AccessKey secret of the MaxCompute data source.
        self.access_secret = access_secret
        # The name of the OSS bucket.
        self.bucket = bucket
        # The endpoint of the MaxCompute data source.
        self.endpoint = endpoint
        # The path of the Object Storage Service (OSS) object.
        self.oss_path = oss_path
        # The partition in the MaxCompute table.
        self.partition = partition
        # The name of the MaxCompute project that is used as the data source.
        self.project = project
        # The name of the MaxCompute table that is used as the data source.
        self.table = table

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.access_secret is not None:
            result['accessSecret'] = self.access_secret
        if self.bucket is not None:
            result['bucket'] = self.bucket
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.oss_path is not None:
            result['ossPath'] = self.oss_path
        if self.partition is not None:
            result['partition'] = self.partition
        if self.project is not None:
            result['project'] = self.project
        if self.table is not None:
            result['table'] = self.table
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('accessSecret') is not None:
            self.access_secret = m.get('accessSecret')
        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('ossPath') is not None:
            self.oss_path = m.get('ossPath')
        if m.get('partition') is not None:
            self.partition = m.get('partition')
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('table') is not None:
            self.table = m.get('table')
        return self


class ModifyTableRequestDataSource(TeaModel):
    def __init__(
        self,
        auto_build_index: bool = None,
        config: ModifyTableRequestDataSourceConfig = None,
        data_time_sec: int = None,
    ):
        # Specifies whether to automatically rebuild the index.
        self.auto_build_index = auto_build_index
        # The configurations of the data source.
        self.config = config
        # The start timestamp from which incremental data is retrieved.
        self.data_time_sec = data_time_sec

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_build_index is not None:
            result['autoBuildIndex'] = self.auto_build_index
        if self.config is not None:
            result['config'] = self.config.to_map()
        if self.data_time_sec is not None:
            result['dataTimeSec'] = self.data_time_sec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoBuildIndex') is not None:
            self.auto_build_index = m.get('autoBuildIndex')
        if m.get('config') is not None:
            temp_model = ModifyTableRequestDataSourceConfig()
            self.config = temp_model.from_map(m['config'])
        if m.get('dataTimeSec') is not None:
            self.data_time_sec = m.get('dataTimeSec')
        return self


class ModifyTableRequestVectorIndexAdvanceParams(TeaModel):
    def __init__(
        self,
        build_index_params: str = None,
        linear_build_threshold: str = None,
        min_scan_doc_cnt: str = None,
        search_index_params: str = None,
    ):
        # The index building parameters.
        self.build_index_params = build_index_params
        # The threshold for linear building.
        self.linear_build_threshold = linear_build_threshold
        # The minimum number of retrieved candidate sets.
        self.min_scan_doc_cnt = min_scan_doc_cnt
        # The index retrieval parameters.
        self.search_index_params = search_index_params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_index_params is not None:
            result['buildIndexParams'] = self.build_index_params
        if self.linear_build_threshold is not None:
            result['linearBuildThreshold'] = self.linear_build_threshold
        if self.min_scan_doc_cnt is not None:
            result['minScanDocCnt'] = self.min_scan_doc_cnt
        if self.search_index_params is not None:
            result['searchIndexParams'] = self.search_index_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('buildIndexParams') is not None:
            self.build_index_params = m.get('buildIndexParams')
        if m.get('linearBuildThreshold') is not None:
            self.linear_build_threshold = m.get('linearBuildThreshold')
        if m.get('minScanDocCnt') is not None:
            self.min_scan_doc_cnt = m.get('minScanDocCnt')
        if m.get('searchIndexParams') is not None:
            self.search_index_params = m.get('searchIndexParams')
        return self


class ModifyTableRequestVectorIndex(TeaModel):
    def __init__(
        self,
        advance_params: ModifyTableRequestVectorIndexAdvanceParams = None,
        dimension: str = None,
        distance_type: str = None,
        index_name: str = None,
        namespace: str = None,
        sparse_index_field: str = None,
        sparse_value_field: str = None,
        vector_field: str = None,
        vector_index_type: str = None,
    ):
        # The configurations of the index schema.
        self.advance_params = advance_params
        # The dimension of the vector.
        self.dimension = dimension
        # The distance type.
        self.distance_type = distance_type
        # The name of the index schema.
        self.index_name = index_name
        # The namespace field.
        self.namespace = namespace
        # The field that stores the indexes of the elements in sparse vectors.
        self.sparse_index_field = sparse_index_field
        # The field that stores the elements in sparse vectors.
        self.sparse_value_field = sparse_value_field
        # The vector field.
        self.vector_field = vector_field
        # The vector retrieval algorithm.
        self.vector_index_type = vector_index_type

    def validate(self):
        if self.advance_params:
            self.advance_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advance_params is not None:
            result['advanceParams'] = self.advance_params.to_map()
        if self.dimension is not None:
            result['dimension'] = self.dimension
        if self.distance_type is not None:
            result['distanceType'] = self.distance_type
        if self.index_name is not None:
            result['indexName'] = self.index_name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.sparse_index_field is not None:
            result['sparseIndexField'] = self.sparse_index_field
        if self.sparse_value_field is not None:
            result['sparseValueField'] = self.sparse_value_field
        if self.vector_field is not None:
            result['vectorField'] = self.vector_field
        if self.vector_index_type is not None:
            result['vectorIndexType'] = self.vector_index_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('advanceParams') is not None:
            temp_model = ModifyTableRequestVectorIndexAdvanceParams()
            self.advance_params = temp_model.from_map(m['advanceParams'])
        if m.get('dimension') is not None:
            self.dimension = m.get('dimension')
        if m.get('distanceType') is not None:
            self.distance_type = m.get('distanceType')
        if m.get('indexName') is not None:
            self.index_name = m.get('indexName')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('sparseIndexField') is not None:
            self.sparse_index_field = m.get('sparseIndexField')
        if m.get('sparseValueField') is not None:
            self.sparse_value_field = m.get('sparseValueField')
        if m.get('vectorField') is not None:
            self.vector_field = m.get('vectorField')
        if m.get('vectorIndexType') is not None:
            self.vector_index_type = m.get('vectorIndexType')
        return self


class ModifyTableRequest(TeaModel):
    def __init__(
        self,
        data_process_config: List[ModifyTableRequestDataProcessConfig] = None,
        data_source: ModifyTableRequestDataSource = None,
        field_schema: Dict[str, str] = None,
        partition_count: int = None,
        primary_key: str = None,
        raw_schema: str = None,
        vector_index: List[ModifyTableRequestVectorIndex] = None,
        dry_run: bool = None,
    ):
        # The configurations about field processing.
        self.data_process_config = data_process_config
        # The configurations of the data source.
        self.data_source = data_source
        # The fields.
        self.field_schema = field_schema
        # The number of data shards.
        self.partition_count = partition_count
        # The primary key field.
        self.primary_key = primary_key
        # The instance schema. If this parameter is specified, the parameters about the index are not required.
        self.raw_schema = raw_schema
        # The index schema.
        self.vector_index = vector_index
        # Specifies whether to perform only a dry run, without performing the actual request. The system only checks the validity of the data source. Valid values:
        # 
        # *   true
        # *   false
        self.dry_run = dry_run

    def validate(self):
        if self.data_process_config:
            for k in self.data_process_config:
                if k:
                    k.validate()
        if self.data_source:
            self.data_source.validate()
        if self.vector_index:
            for k in self.vector_index:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['dataProcessConfig'] = []
        if self.data_process_config is not None:
            for k in self.data_process_config:
                result['dataProcessConfig'].append(k.to_map() if k else None)
        if self.data_source is not None:
            result['dataSource'] = self.data_source.to_map()
        if self.field_schema is not None:
            result['fieldSchema'] = self.field_schema
        if self.partition_count is not None:
            result['partitionCount'] = self.partition_count
        if self.primary_key is not None:
            result['primaryKey'] = self.primary_key
        if self.raw_schema is not None:
            result['rawSchema'] = self.raw_schema
        result['vectorIndex'] = []
        if self.vector_index is not None:
            for k in self.vector_index:
                result['vectorIndex'].append(k.to_map() if k else None)
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_process_config = []
        if m.get('dataProcessConfig') is not None:
            for k in m.get('dataProcessConfig'):
                temp_model = ModifyTableRequestDataProcessConfig()
                self.data_process_config.append(temp_model.from_map(k))
        if m.get('dataSource') is not None:
            temp_model = ModifyTableRequestDataSource()
            self.data_source = temp_model.from_map(m['dataSource'])
        if m.get('fieldSchema') is not None:
            self.field_schema = m.get('fieldSchema')
        if m.get('partitionCount') is not None:
            self.partition_count = m.get('partitionCount')
        if m.get('primaryKey') is not None:
            self.primary_key = m.get('primaryKey')
        if m.get('rawSchema') is not None:
            self.raw_schema = m.get('rawSchema')
        self.vector_index = []
        if m.get('vectorIndex') is not None:
            for k in m.get('vectorIndex'):
                temp_model = ModifyTableRequestVectorIndex()
                self.vector_index.append(temp_model.from_map(k))
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class ModifyTableResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # id of request
        self.request_id = request_id
        # Map
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ModifyTableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyTableResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishAdvanceConfigRequestFilesConfig(TeaModel):
    def __init__(
        self,
        content: str = None,
        variables: Dict[str, FilesConfigVariablesValue] = None,
    ):
        # The file content.
        self.content = content
        # The variables.
        self.variables = variables

    def validate(self):
        if self.variables:
            for v in self.variables.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        result['variables'] = {}
        if self.variables is not None:
            for k, v in self.variables.items():
                result['variables'][k] = v.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        self.variables = {}
        if m.get('variables') is not None:
            for k, v in m.get('variables').items():
                temp_model = FilesConfigVariablesValue()
                self.variables[k] = temp_model.from_map(v)
        return self


class PublishAdvanceConfigRequestFiles(TeaModel):
    def __init__(
        self,
        config: PublishAdvanceConfigRequestFilesConfig = None,
        dir_name: str = None,
        file_name: str = None,
        operate_type: str = None,
        oss_path: str = None,
        parent_full_path: str = None,
    ):
        # The information about the advanced configuration.
        self.config = config
        # The directory name.
        self.dir_name = dir_name
        # The file name.
        self.file_name = file_name
        # The operation type. Valid values: UPDATE and DELETE. Default value: UPDATE.
        self.operate_type = operate_type
        # The path of the Object Storage Service (OSS) object.
        self.oss_path = oss_path
        # The path of the parent directory.
        self.parent_full_path = parent_full_path

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['config'] = self.config.to_map()
        if self.dir_name is not None:
            result['dirName'] = self.dir_name
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.operate_type is not None:
            result['operateType'] = self.operate_type
        if self.oss_path is not None:
            result['ossPath'] = self.oss_path
        if self.parent_full_path is not None:
            result['parentFullPath'] = self.parent_full_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            temp_model = PublishAdvanceConfigRequestFilesConfig()
            self.config = temp_model.from_map(m['config'])
        if m.get('dirName') is not None:
            self.dir_name = m.get('dirName')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('operateType') is not None:
            self.operate_type = m.get('operateType')
        if m.get('ossPath') is not None:
            self.oss_path = m.get('ossPath')
        if m.get('parentFullPath') is not None:
            self.parent_full_path = m.get('parentFullPath')
        return self


class PublishAdvanceConfigRequest(TeaModel):
    def __init__(
        self,
        desc: str = None,
        files: List[PublishAdvanceConfigRequestFiles] = None,
    ):
        # The description of the advanced configuration.
        self.desc = desc
        # The files.
        self.files = files

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['desc'] = self.desc
        result['files'] = []
        if self.files is not None:
            for k in self.files:
                result['files'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        self.files = []
        if m.get('files') is not None:
            for k in m.get('files'):
                temp_model = PublishAdvanceConfigRequestFiles()
                self.files.append(temp_model.from_map(k))
        return self


class PublishAdvanceConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The ID of the request
        self.request_id = request_id
        # The result returned
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class PublishAdvanceConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PublishAdvanceConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PublishAdvanceConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishIndexVersionRequest(TeaModel):
    def __init__(
        self,
        body: Dict[str, Any] = None,
    ):
        # The request body.
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class PublishIndexVersionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # id of request
        self.request_id = request_id
        # The information about the index
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class PublishIndexVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PublishIndexVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PublishIndexVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushDocumentsRequest(TeaModel):
    def __init__(
        self,
        body: List[Any] = None,
        pk_field: str = None,
    ):
        # The request body.
        self.body = body
        # The primary key field.
        self.pk_field = pk_field

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.pk_field is not None:
            result['pkField'] = self.pk_field
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('pkField') is not None:
            self.pk_field = m.get('pkField')
        return self


class PushDocumentsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The result.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class PushDocumentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PushDocumentsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PushDocumentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecoverIndexRequest(TeaModel):
    def __init__(
        self,
        build_deploy_id: int = None,
        data_source_name: str = None,
        generation: str = None,
        index_name: str = None,
    ):
        # The deployment ID of the data source.
        self.build_deploy_id = build_deploy_id
        # The name of the data source.
        self.data_source_name = data_source_name
        # The ID of the full index version.
        self.generation = generation
        # The index name.
        self.index_name = index_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_deploy_id is not None:
            result['buildDeployId'] = self.build_deploy_id
        if self.data_source_name is not None:
            result['dataSourceName'] = self.data_source_name
        if self.generation is not None:
            result['generation'] = self.generation
        if self.index_name is not None:
            result['indexName'] = self.index_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('buildDeployId') is not None:
            self.build_deploy_id = m.get('buildDeployId')
        if m.get('dataSourceName') is not None:
            self.data_source_name = m.get('dataSourceName')
        if m.get('generation') is not None:
            self.generation = m.get('generation')
        if m.get('indexName') is not None:
            self.index_name = m.get('indexName')
        return self


class RecoverIndexResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The result returned by data search.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class RecoverIndexResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RecoverIndexResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RecoverIndexResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReindexRequest(TeaModel):
    def __init__(
        self,
        data_time_sec: int = None,
        oss_data_path: str = None,
        partition: str = None,
    ):
        # The timestamp in seconds. The value must be of the INTEGER type. This parameter is required if you specify an API data source.
        self.data_time_sec = data_time_sec
        # oss data path
        self.oss_data_path = oss_data_path
        # The partition in the MaxCompute table. This parameter is required if type is set to odps.
        self.partition = partition

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_time_sec is not None:
            result['dataTimeSec'] = self.data_time_sec
        if self.oss_data_path is not None:
            result['ossDataPath'] = self.oss_data_path
        if self.partition is not None:
            result['partition'] = self.partition
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataTimeSec') is not None:
            self.data_time_sec = m.get('dataTimeSec')
        if m.get('ossDataPath') is not None:
            self.oss_data_path = m.get('ossDataPath')
        if m.get('partition') is not None:
            self.partition = m.get('partition')
        return self


class ReindexResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # requestId
        self.request_id = request_id
        # Map
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ReindexResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReindexResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ReindexResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveClusterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # id of request
        self.request_id = request_id
        # The result
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class RemoveClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveClusterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RemoveClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenameFolderRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class RenameFolderResponseBodyResult(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        instance_id: int = None,
        is_dir: int = None,
        name: str = None,
        parent: int = None,
        template_id: int = None,
        type: str = None,
    ):
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.instance_id = instance_id
        self.is_dir = is_dir
        self.name = name
        self.parent = parent
        self.template_id = template_id
        # table, instance, template, function
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.is_dir is not None:
            result['isDir'] = self.is_dir
        if self.name is not None:
            result['name'] = self.name
        if self.parent is not None:
            result['parent'] = self.parent
        if self.template_id is not None:
            result['templateId'] = self.template_id
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('isDir') is not None:
            self.is_dir = m.get('isDir')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parent') is not None:
            self.parent = m.get('parent')
        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class RenameFolderResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: RenameFolderResponseBodyResult = None,
    ):
        # id of request
        self.request_id = request_id
        # NodeVO
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = RenameFolderResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class RenameFolderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RenameFolderResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RenameFolderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartIndexResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The index map.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class StartIndexResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartIndexResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StartIndexResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopIndexResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The index map.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class StopIndexResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopIndexResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StopIndexResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # id of request
        self.request_id = request_id
        # The information about the index
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class StopTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StopTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        # This parameter is required.
        self.resource_id = resource_id
        # This parameter is required.
        self.resource_type = resource_type
        # This parameter is required.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        result['tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        self.tag = []
        if m.get('tag') is not None:
            for k in m.get('tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag_key: List[str] = None,
    ):
        self.all = all
        # This parameter is required.
        self.resource_id = resource_id
        # This parameter is required.
        self.resource_type = resource_type
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['all'] = self.all
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.tag_key is not None:
            result['tagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('all') is not None:
            self.all = m.get('all')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('tagKey') is not None:
            self.tag_key = m.get('tagKey')
        return self


class UntagResourcesShrinkRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        resource_id_shrink: str = None,
        resource_type: str = None,
        tag_key_shrink: str = None,
    ):
        self.all = all
        # This parameter is required.
        self.resource_id_shrink = resource_id_shrink
        # This parameter is required.
        self.resource_type = resource_type
        self.tag_key_shrink = tag_key_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['all'] = self.all
        if self.resource_id_shrink is not None:
            result['resourceId'] = self.resource_id_shrink
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.tag_key_shrink is not None:
            result['tagKey'] = self.tag_key_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('all') is not None:
            self.all = m.get('all')
        if m.get('resourceId') is not None:
            self.resource_id_shrink = m.get('resourceId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('tagKey') is not None:
            self.tag_key_shrink = m.get('tagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        tequest_id: str = None,
    ):
        self.tequest_id = tequest_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tequest_id is not None:
            result['tequestId'] = self.tequest_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tequestId') is not None:
            self.tequest_id = m.get('tequestId')
        return self


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UntagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInstanceRequestComponents(TeaModel):
    def __init__(
        self,
        code: str = None,
        value: str = None,
    ):
        # The code of the specification, which must be consistent with the value that you specify on the buy page.
        self.code = code
        # The value of the specification.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class UpdateInstanceRequest(TeaModel):
    def __init__(
        self,
        components: List[UpdateInstanceRequestComponents] = None,
        description: str = None,
        order_type: str = None,
    ):
        # The information about the instance specification.
        self.components = components
        # The description of the instance.
        self.description = description
        # The type of the order. Valid values: UPGRADE and DOWNGRADE. UPGRADE upgrades the instance specifications. DOWNGRADE: downgrades the instance specifications.
        self.order_type = order_type

    def validate(self):
        if self.components:
            for k in self.components:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['components'] = []
        if self.components is not None:
            for k in self.components:
                result['components'].append(k.to_map() if k else None)
        if self.description is not None:
            result['description'] = self.description
        if self.order_type is not None:
            result['orderType'] = self.order_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.components = []
        if m.get('components') is not None:
            for k in m.get('components'):
                temp_model = UpdateInstanceRequestComponents()
                self.components.append(temp_model.from_map(k))
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('orderType') is not None:
            self.order_type = m.get('orderType')
        return self


class UpdateInstanceResponseBodyResult(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        commodity_code: str = None,
        create_time: str = None,
        description: str = None,
        expired_time: str = None,
        in_debt: bool = None,
        instance_id: str = None,
        lock_mode: str = None,
        resource_group_id: str = None,
        status: str = None,
        update_time: str = None,
    ):
        # The billing method.
        self.charge_type = charge_type
        # The commodity code of the instance.
        self.commodity_code = commodity_code
        # The time when the instance was created
        self.create_time = create_time
        # The description of the instance
        self.description = description
        # The time when the instance expires
        self.expired_time = expired_time
        # Indicates whether an overdue payment is involved
        self.in_debt = in_debt
        # The instance ID.
        self.instance_id = instance_id
        # The lock status
        self.lock_mode = lock_mode
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The instance status.
        self.status = status
        # The time when the instance was last updated
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.expired_time is not None:
            result['expiredTime'] = self.expired_time
        if self.in_debt is not None:
            result['inDebt'] = self.in_debt
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.lock_mode is not None:
            result['lockMode'] = self.lock_mode
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.status is not None:
            result['status'] = self.status
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('expiredTime') is not None:
            self.expired_time = m.get('expiredTime')
        if m.get('inDebt') is not None:
            self.in_debt = m.get('inDebt')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('lockMode') is not None:
            self.lock_mode = m.get('lockMode')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class UpdateInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: UpdateInstanceResponseBodyResult = None,
    ):
        # The ID of the request
        self.request_id = request_id
        # The results returned.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = UpdateInstanceResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class UpdateInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSqlInstanceContentRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
    ):
        # This parameter is required.
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        return self


class UpdateSqlInstanceContentResponseBodyResult(TeaModel):
    def __init__(
        self,
        combine_params: str = None,
        comment: str = None,
        content: str = None,
        dynamic_params: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        instance_id: int = None,
        kvpairs: str = None,
        related_template_id: int = None,
        static_params: str = None,
        template_params: str = None,
        version: int = None,
    ):
        self.combine_params = combine_params
        self.comment = comment
        self.content = content
        self.dynamic_params = dynamic_params
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.instance_id = instance_id
        self.kvpairs = kvpairs
        self.related_template_id = related_template_id
        self.static_params = static_params
        self.template_params = template_params
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.combine_params is not None:
            result['combineParams'] = self.combine_params
        if self.comment is not None:
            result['comment'] = self.comment
        if self.content is not None:
            result['content'] = self.content
        if self.dynamic_params is not None:
            result['dynamicParams'] = self.dynamic_params
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.kvpairs is not None:
            result['kvpairs'] = self.kvpairs
        if self.related_template_id is not None:
            result['relatedTemplateId'] = self.related_template_id
        if self.static_params is not None:
            result['staticParams'] = self.static_params
        if self.template_params is not None:
            result['templateParams'] = self.template_params
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('combineParams') is not None:
            self.combine_params = m.get('combineParams')
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('dynamicParams') is not None:
            self.dynamic_params = m.get('dynamicParams')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('kvpairs') is not None:
            self.kvpairs = m.get('kvpairs')
        if m.get('relatedTemplateId') is not None:
            self.related_template_id = m.get('relatedTemplateId')
        if m.get('staticParams') is not None:
            self.static_params = m.get('staticParams')
        if m.get('templateParams') is not None:
            self.template_params = m.get('templateParams')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class UpdateSqlInstanceContentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: UpdateSqlInstanceContentResponseBodyResult = None,
    ):
        # id of request
        self.request_id = request_id
        # InstanceVersionVO
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = UpdateSqlInstanceContentResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class UpdateSqlInstanceContentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateSqlInstanceContentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateSqlInstanceContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSqlInstanceNameRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class UpdateSqlInstanceNameResponseBodyResult(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        instance_id: int = None,
        is_dir: int = None,
        name: str = None,
        parent: int = None,
        template_id: int = None,
        type: str = None,
    ):
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.instance_id = instance_id
        self.is_dir = is_dir
        self.name = name
        self.parent = parent
        self.template_id = template_id
        # table, instance, template, function
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.is_dir is not None:
            result['isDir'] = self.is_dir
        if self.name is not None:
            result['name'] = self.name
        if self.parent is not None:
            result['parent'] = self.parent
        if self.template_id is not None:
            result['templateId'] = self.template_id
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('isDir') is not None:
            self.is_dir = m.get('isDir')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parent') is not None:
            self.parent = m.get('parent')
        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class UpdateSqlInstanceNameResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: UpdateSqlInstanceNameResponseBodyResult = None,
    ):
        # id of request
        self.request_id = request_id
        # NodeVO
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = UpdateSqlInstanceNameResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class UpdateSqlInstanceNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateSqlInstanceNameResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateSqlInstanceNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSqlInstanceParamsRequest(TeaModel):
    def __init__(
        self,
        combine_param: Dict[str, Any] = None,
        dynamic_param: Dict[str, Any] = None,
        kvpair: Dict[str, Any] = None,
        params: Dict[str, Any] = None,
        static_param: Dict[str, Any] = None,
    ):
        self.combine_param = combine_param
        self.dynamic_param = dynamic_param
        self.kvpair = kvpair
        self.params = params
        self.static_param = static_param

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.combine_param is not None:
            result['combineParam'] = self.combine_param
        if self.dynamic_param is not None:
            result['dynamicParam'] = self.dynamic_param
        if self.kvpair is not None:
            result['kvpair'] = self.kvpair
        if self.params is not None:
            result['params'] = self.params
        if self.static_param is not None:
            result['staticParam'] = self.static_param
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('combineParam') is not None:
            self.combine_param = m.get('combineParam')
        if m.get('dynamicParam') is not None:
            self.dynamic_param = m.get('dynamicParam')
        if m.get('kvpair') is not None:
            self.kvpair = m.get('kvpair')
        if m.get('params') is not None:
            self.params = m.get('params')
        if m.get('staticParam') is not None:
            self.static_param = m.get('staticParam')
        return self


class UpdateSqlInstanceParamsResponseBodyResult(TeaModel):
    def __init__(
        self,
        combine_params: str = None,
        comment: str = None,
        content: str = None,
        dynamic_params: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        instance_id: int = None,
        kvpairs: str = None,
        related_template_id: int = None,
        static_params: str = None,
        template_params: str = None,
        version: int = None,
    ):
        self.combine_params = combine_params
        self.comment = comment
        self.content = content
        self.dynamic_params = dynamic_params
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.instance_id = instance_id
        self.kvpairs = kvpairs
        self.related_template_id = related_template_id
        self.static_params = static_params
        self.template_params = template_params
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.combine_params is not None:
            result['combineParams'] = self.combine_params
        if self.comment is not None:
            result['comment'] = self.comment
        if self.content is not None:
            result['content'] = self.content
        if self.dynamic_params is not None:
            result['dynamicParams'] = self.dynamic_params
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.kvpairs is not None:
            result['kvpairs'] = self.kvpairs
        if self.related_template_id is not None:
            result['relatedTemplateId'] = self.related_template_id
        if self.static_params is not None:
            result['staticParams'] = self.static_params
        if self.template_params is not None:
            result['templateParams'] = self.template_params
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('combineParams') is not None:
            self.combine_params = m.get('combineParams')
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('dynamicParams') is not None:
            self.dynamic_params = m.get('dynamicParams')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('kvpairs') is not None:
            self.kvpairs = m.get('kvpairs')
        if m.get('relatedTemplateId') is not None:
            self.related_template_id = m.get('relatedTemplateId')
        if m.get('staticParams') is not None:
            self.static_params = m.get('staticParams')
        if m.get('templateParams') is not None:
            self.template_params = m.get('templateParams')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class UpdateSqlInstanceParamsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: UpdateSqlInstanceParamsResponseBodyResult = None,
    ):
        # id of request
        self.request_id = request_id
        # InstanceVersionVO
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = UpdateSqlInstanceParamsResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class UpdateSqlInstanceParamsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateSqlInstanceParamsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateSqlInstanceParamsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


