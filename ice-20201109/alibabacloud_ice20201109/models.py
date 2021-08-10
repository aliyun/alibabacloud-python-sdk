# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class ListSmartJobsRequest(TeaModel):
    def __init__(
        self,
        status: int = None,
        next_token: str = None,
        max_results: int = None,
        page_no: int = None,
        page_size: int = None,
        job_type: str = None,
        sort_by: str = None,
        job_state: str = None,
    ):
        self.status = status
        self.next_token = next_token
        self.max_results = max_results
        self.page_no = page_no
        self.page_size = page_size
        self.job_type = job_type
        self.sort_by = sort_by
        self.job_state = job_state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.job_state is not None:
            result['JobState'] = self.job_state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('JobState') is not None:
            self.job_state = m.get('JobState')
        return self


class ListSmartJobsResponseBodySmartJobListInputConfig(TeaModel):
    def __init__(
        self,
        input_file: str = None,
        keyword: str = None,
    ):
        self.input_file = input_file
        self.keyword = keyword

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_file is not None:
            result['InputFile'] = self.input_file
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputFile') is not None:
            self.input_file = m.get('InputFile')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        return self


class ListSmartJobsResponseBodySmartJobListOutputConfig(TeaModel):
    def __init__(
        self,
        bucket: str = None,
        object: str = None,
    ):
        self.bucket = bucket
        self.object = object

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.object is not None:
            result['Object'] = self.object
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        return self


class ListSmartJobsResponseBodySmartJobList(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        title: str = None,
        description: str = None,
        user_id: int = None,
        job_type: str = None,
        editing_config: str = None,
        user_data: str = None,
        job_state: str = None,
        create_time: str = None,
        modified_time: str = None,
        input_config: ListSmartJobsResponseBodySmartJobListInputConfig = None,
        output_config: ListSmartJobsResponseBodySmartJobListOutputConfig = None,
    ):
        self.job_id = job_id
        self.title = title
        self.description = description
        self.user_id = user_id
        self.job_type = job_type
        self.editing_config = editing_config
        self.user_data = user_data
        self.job_state = job_state
        self.create_time = create_time
        self.modified_time = modified_time
        self.input_config = input_config
        self.output_config = output_config

    def validate(self):
        if self.input_config:
            self.input_config.validate()
        if self.output_config:
            self.output_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.title is not None:
            result['Title'] = self.title
        if self.description is not None:
            result['Description'] = self.description
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.editing_config is not None:
            result['EditingConfig'] = self.editing_config
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.job_state is not None:
            result['JobState'] = self.job_state
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.input_config is not None:
            result['InputConfig'] = self.input_config.to_map()
        if self.output_config is not None:
            result['OutputConfig'] = self.output_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('EditingConfig') is not None:
            self.editing_config = m.get('EditingConfig')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('JobState') is not None:
            self.job_state = m.get('JobState')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('InputConfig') is not None:
            temp_model = ListSmartJobsResponseBodySmartJobListInputConfig()
            self.input_config = temp_model.from_map(m['InputConfig'])
        if m.get('OutputConfig') is not None:
            temp_model = ListSmartJobsResponseBodySmartJobListOutputConfig()
            self.output_config = temp_model.from_map(m['OutputConfig'])
        return self


class ListSmartJobsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        smart_job_list: List[ListSmartJobsResponseBodySmartJobList] = None,
        next_token: str = None,
        max_results: str = None,
        total_count: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.smart_job_list = smart_job_list
        self.next_token = next_token
        self.max_results = max_results
        self.total_count = total_count

    def validate(self):
        if self.smart_job_list:
            for k in self.smart_job_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SmartJobList'] = []
        if self.smart_job_list is not None:
            for k in self.smart_job_list:
                result['SmartJobList'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.smart_job_list = []
        if m.get('SmartJobList') is not None:
            for k in m.get('SmartJobList'):
                temp_model = ListSmartJobsResponseBodySmartJobList()
                self.smart_job_list.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListSmartJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSmartJobsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListSmartJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRelatedAuthorizationStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        ossauthorized: bool = None,
        mtsauthorized: bool = None,
        mnsauthorized: bool = None,
        authorized: bool = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.ossauthorized = ossauthorized
        self.mtsauthorized = mtsauthorized
        self.mnsauthorized = mnsauthorized
        self.authorized = authorized

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.ossauthorized is not None:
            result['OSSAuthorized'] = self.ossauthorized
        if self.mtsauthorized is not None:
            result['MTSAuthorized'] = self.mtsauthorized
        if self.mnsauthorized is not None:
            result['MNSAuthorized'] = self.mnsauthorized
        if self.authorized is not None:
            result['Authorized'] = self.authorized
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OSSAuthorized') is not None:
            self.ossauthorized = m.get('OSSAuthorized')
        if m.get('MTSAuthorized') is not None:
            self.mtsauthorized = m.get('MTSAuthorized')
        if m.get('MNSAuthorized') is not None:
            self.mnsauthorized = m.get('MNSAuthorized')
        if m.get('Authorized') is not None:
            self.authorized = m.get('Authorized')
        return self


class DescribeRelatedAuthorizationStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRelatedAuthorizationStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRelatedAuthorizationStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSmartJobRequest(TeaModel):
    def __init__(
        self,
        job_id: str = None,
    ):
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class DeleteSmartJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        state: str = None,
        job_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.state = state
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.state is not None:
            result['State'] = self.state
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class DeleteSmartJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteSmartJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteSmartJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddTemplateRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        config: str = None,
        cover_url: str = None,
        preview_media: str = None,
        status: str = None,
        source: str = None,
        related_mediaids: str = None,
    ):
        # 模板名称
        self.name = name
        # 模板类型，取值范围：Timeline
        self.type = type
        # 参见Timeline模板Config文档
        self.config = config
        # 模板封面
        self.cover_url = cover_url
        # 预览视频媒资id
        self.preview_media = preview_media
        # 模板状态
        self.status = status
        # 模板创建来源，默认OpenAPI
        self.source = source
        # 模板相关素材，模板编辑器使用
        self.related_mediaids = related_mediaids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.config is not None:
            result['Config'] = self.config
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.preview_media is not None:
            result['PreviewMedia'] = self.preview_media
        if self.status is not None:
            result['Status'] = self.status
        if self.source is not None:
            result['Source'] = self.source
        if self.related_mediaids is not None:
            result['RelatedMediaids'] = self.related_mediaids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('PreviewMedia') is not None:
            self.preview_media = m.get('PreviewMedia')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('RelatedMediaids') is not None:
            self.related_mediaids = m.get('RelatedMediaids')
        return self


class AddTemplateResponseBodyTemplate(TeaModel):
    def __init__(
        self,
        template_id: str = None,
        name: str = None,
        type: str = None,
        config: str = None,
        cover_url: str = None,
        preview_media: str = None,
        status: str = None,
        create_source: str = None,
        modified_source: str = None,
    ):
        # 模板Id
        self.template_id = template_id
        # 模板名称
        self.name = name
        # 模板类型
        self.type = type
        # 参见Timeline模板Config文档
        self.config = config
        # 模板封面
        self.cover_url = cover_url
        # 预览视频媒资id
        self.preview_media = preview_media
        # 模板状态
        self.status = status
        # 模板创建来源
        self.create_source = create_source
        # 模板修改来源
        self.modified_source = modified_source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.config is not None:
            result['Config'] = self.config
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.preview_media is not None:
            result['PreviewMedia'] = self.preview_media
        if self.status is not None:
            result['Status'] = self.status
        if self.create_source is not None:
            result['CreateSource'] = self.create_source
        if self.modified_source is not None:
            result['ModifiedSource'] = self.modified_source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('PreviewMedia') is not None:
            self.preview_media = m.get('PreviewMedia')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreateSource') is not None:
            self.create_source = m.get('CreateSource')
        if m.get('ModifiedSource') is not None:
            self.modified_source = m.get('ModifiedSource')
        return self


class AddTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        template: AddTemplateResponseBodyTemplate = None,
    ):
        # 请求ID
        self.request_id = request_id
        # 模板信息
        self.template = template

    def validate(self):
        if self.template:
            self.template.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template is not None:
            result['Template'] = self.template.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Template') is not None:
            temp_model = AddTemplateResponseBodyTemplate()
            self.template = temp_model.from_map(m['Template'])
        return self


class AddTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddTemplateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEditingProjectRequest(TeaModel):
    def __init__(
        self,
        title: str = None,
        description: str = None,
        timeline: str = None,
        cover_url: str = None,
        project_id: str = None,
    ):
        # 云剪辑工程标题
        self.title = title
        # 云剪辑工程描述
        self.description = description
        # 云剪辑工程时间线，Json格式
        self.timeline = timeline
        # 云剪辑工程封面
        self.cover_url = cover_url
        # 云剪辑工程ID
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.title is not None:
            result['Title'] = self.title
        if self.description is not None:
            result['Description'] = self.description
        if self.timeline is not None:
            result['Timeline'] = self.timeline
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Timeline') is not None:
            self.timeline = m.get('Timeline')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class UpdateEditingProjectResponseBody(TeaModel):
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
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateEditingProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateEditingProjectResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateEditingProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMediaProducingJobsRequest(TeaModel):
    def __init__(
        self,
        status: str = None,
    ):
        # 查询以下状态的合成任务，支持多值，以英文逗号分隔
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListMediaProducingJobsResponseBodyMediaProducingJobList(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        project_id: str = None,
        media_id: str = None,
        media_url: str = None,
        template_id: str = None,
        clips_param: str = None,
        duration: float = None,
        create_time: str = None,
        complete_time: str = None,
        modified_time: str = None,
        status: str = None,
        code: str = None,
        message: str = None,
    ):
        self.job_id = job_id
        self.project_id = project_id
        self.media_id = media_id
        self.media_url = media_url
        self.template_id = template_id
        self.clips_param = clips_param
        self.duration = duration
        self.create_time = create_time
        self.complete_time = complete_time
        self.modified_time = modified_time
        self.status = status
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.media_url is not None:
            result['MediaURL'] = self.media_url
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.clips_param is not None:
            result['ClipsParam'] = self.clips_param
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.status is not None:
            result['Status'] = self.status
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('MediaURL') is not None:
            self.media_url = m.get('MediaURL')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('ClipsParam') is not None:
            self.clips_param = m.get('ClipsParam')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class ListMediaProducingJobsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        media_producing_job_list: List[ListMediaProducingJobsResponseBodyMediaProducingJobList] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.media_producing_job_list = media_producing_job_list

    def validate(self):
        if self.media_producing_job_list:
            for k in self.media_producing_job_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['MediaProducingJobList'] = []
        if self.media_producing_job_list is not None:
            for k in self.media_producing_job_list:
                result['MediaProducingJobList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.media_producing_job_list = []
        if m.get('MediaProducingJobList') is not None:
            for k in m.get('MediaProducingJobList'):
                temp_model = ListMediaProducingJobsResponseBodyMediaProducingJobList()
                self.media_producing_job_list.append(temp_model.from_map(k))
        return self


class ListMediaProducingJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListMediaProducingJobsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListMediaProducingJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEditingProjectMaterialsRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
    ):
        # 云剪辑工程ID
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class GetEditingProjectMaterialsResponseBodyMediaInfosMediaBasicInfo(TeaModel):
    def __init__(
        self,
        media_id: str = None,
        input_url: str = None,
        media_type: str = None,
        business_type: str = None,
        source: str = None,
        title: str = None,
        description: str = None,
        category: str = None,
        media_tags: str = None,
        cover_url: str = None,
        user_data: str = None,
        snapshots: str = None,
        status: str = None,
        transcode_status: str = None,
        create_time: str = None,
        modified_time: str = None,
        deleted_time: str = None,
        sprite_images: str = None,
    ):
        # MediaId
        self.media_id = media_id
        # 待注册的媒资在相应系统中的地址
        self.input_url = input_url
        # 媒资媒体类型
        self.media_type = media_type
        # 媒资业务类型
        self.business_type = business_type
        # 来源
        self.source = source
        # 标题
        self.title = title
        # 内容描述
        self.description = description
        # 分类
        self.category = category
        # 标签
        self.media_tags = media_tags
        # 封面地址
        self.cover_url = cover_url
        # 用户数据
        self.user_data = user_data
        # 截图
        self.snapshots = snapshots
        # 资源状态
        self.status = status
        # 转码状态
        self.transcode_status = transcode_status
        # 媒资创建时间
        self.create_time = create_time
        # 媒资修改时间
        self.modified_time = modified_time
        # 媒资删除时间
        self.deleted_time = deleted_time
        # 雪碧图
        self.sprite_images = sprite_images

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.input_url is not None:
            result['InputURL'] = self.input_url
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.source is not None:
            result['Source'] = self.source
        if self.title is not None:
            result['Title'] = self.title
        if self.description is not None:
            result['Description'] = self.description
        if self.category is not None:
            result['Category'] = self.category
        if self.media_tags is not None:
            result['MediaTags'] = self.media_tags
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.snapshots is not None:
            result['Snapshots'] = self.snapshots
        if self.status is not None:
            result['Status'] = self.status
        if self.transcode_status is not None:
            result['TranscodeStatus'] = self.transcode_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.deleted_time is not None:
            result['DeletedTime'] = self.deleted_time
        if self.sprite_images is not None:
            result['SpriteImages'] = self.sprite_images
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('InputURL') is not None:
            self.input_url = m.get('InputURL')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('MediaTags') is not None:
            self.media_tags = m.get('MediaTags')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('Snapshots') is not None:
            self.snapshots = m.get('Snapshots')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TranscodeStatus') is not None:
            self.transcode_status = m.get('TranscodeStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('DeletedTime') is not None:
            self.deleted_time = m.get('DeletedTime')
        if m.get('SpriteImages') is not None:
            self.sprite_images = m.get('SpriteImages')
        return self


class GetEditingProjectMaterialsResponseBodyMediaInfosFileInfoListFileBasicInfo(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_status: str = None,
        file_type: str = None,
        file_size: str = None,
        file_url: str = None,
        region: str = None,
        format_name: str = None,
        duration: str = None,
        bitrate: str = None,
        width: str = None,
        height: str = None,
    ):
        # 文件名
        self.file_name = file_name
        # 文件状态
        self.file_status = file_status
        # 文件类型
        self.file_type = file_type
        # 文件大小（字节）
        self.file_size = file_size
        # 文件oss地址
        self.file_url = file_url
        # 文件存储区域
        self.region = region
        # 封装格式
        self.format_name = format_name
        # 时长
        self.duration = duration
        # 码率
        self.bitrate = bitrate
        # 宽
        self.width = width
        # 高
        self.height = height

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_status is not None:
            result['FileStatus'] = self.file_status
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.region is not None:
            result['Region'] = self.region
        if self.format_name is not None:
            result['FormatName'] = self.format_name
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileStatus') is not None:
            self.file_status = m.get('FileStatus')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('FormatName') is not None:
            self.format_name = m.get('FormatName')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class GetEditingProjectMaterialsResponseBodyMediaInfosFileInfoList(TeaModel):
    def __init__(
        self,
        file_basic_info: GetEditingProjectMaterialsResponseBodyMediaInfosFileInfoListFileBasicInfo = None,
    ):
        # 文件基础信息，包含时长，大小等
        self.file_basic_info = file_basic_info

    def validate(self):
        if self.file_basic_info:
            self.file_basic_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_basic_info is not None:
            result['FileBasicInfo'] = self.file_basic_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileBasicInfo') is not None:
            temp_model = GetEditingProjectMaterialsResponseBodyMediaInfosFileInfoListFileBasicInfo()
            self.file_basic_info = temp_model.from_map(m['FileBasicInfo'])
        return self


class GetEditingProjectMaterialsResponseBodyMediaInfos(TeaModel):
    def __init__(
        self,
        media_id: str = None,
        media_basic_info: GetEditingProjectMaterialsResponseBodyMediaInfosMediaBasicInfo = None,
        file_info_list: List[GetEditingProjectMaterialsResponseBodyMediaInfosFileInfoList] = None,
    ):
        # 媒资ID
        self.media_id = media_id
        # BasicInfo
        self.media_basic_info = media_basic_info
        # FileInfos
        self.file_info_list = file_info_list

    def validate(self):
        if self.media_basic_info:
            self.media_basic_info.validate()
        if self.file_info_list:
            for k in self.file_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.media_basic_info is not None:
            result['MediaBasicInfo'] = self.media_basic_info.to_map()
        result['FileInfoList'] = []
        if self.file_info_list is not None:
            for k in self.file_info_list:
                result['FileInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('MediaBasicInfo') is not None:
            temp_model = GetEditingProjectMaterialsResponseBodyMediaInfosMediaBasicInfo()
            self.media_basic_info = temp_model.from_map(m['MediaBasicInfo'])
        self.file_info_list = []
        if m.get('FileInfoList') is not None:
            for k in m.get('FileInfoList'):
                temp_model = GetEditingProjectMaterialsResponseBodyMediaInfosFileInfoList()
                self.file_info_list.append(temp_model.from_map(k))
        return self


class GetEditingProjectMaterialsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        project_id: str = None,
        media_infos: List[GetEditingProjectMaterialsResponseBodyMediaInfos] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.project_id = project_id
        # 符合要求的媒资集合
        self.media_infos = media_infos

    def validate(self):
        if self.media_infos:
            for k in self.media_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        result['MediaInfos'] = []
        if self.media_infos is not None:
            for k in self.media_infos:
                result['MediaInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        self.media_infos = []
        if m.get('MediaInfos') is not None:
            for k in m.get('MediaInfos'):
                temp_model = GetEditingProjectMaterialsResponseBodyMediaInfos()
                self.media_infos.append(temp_model.from_map(k))
        return self


class GetEditingProjectMaterialsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetEditingProjectMaterialsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetEditingProjectMaterialsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDefaultStorageLocationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        storage_type: str = None,
        bucket: str = None,
        path: str = None,
        status: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 存储类型
        self.storage_type = storage_type
        # oss bucket 名称
        self.bucket = bucket
        # 路径
        self.path = path
        # 状态
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.path is not None:
            result['Path'] = self.path
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetDefaultStorageLocationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDefaultStorageLocationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetDefaultStorageLocationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMediaInfosRequest(TeaModel):
    def __init__(
        self,
        media_ids: str = None,
        input_urls: str = None,
    ):
        # ICE 媒资ID
        self.media_ids = media_ids
        # 待注册的媒资在相应系统中的地址
        self.input_urls = input_urls

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_ids is not None:
            result['MediaIds'] = self.media_ids
        if self.input_urls is not None:
            result['InputURLs'] = self.input_urls
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaIds') is not None:
            self.media_ids = m.get('MediaIds')
        if m.get('InputURLs') is not None:
            self.input_urls = m.get('InputURLs')
        return self


class DeleteMediaInfosResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        ignored_list: List[str] = None,
    ):
        # 请求ID
        self.request_id = request_id
        # 出现获取错误的ID或inputUr
        self.ignored_list = ignored_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.ignored_list is not None:
            result['IgnoredList'] = self.ignored_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('IgnoredList') is not None:
            self.ignored_list = m.get('IgnoredList')
        return self


class DeleteMediaInfosResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteMediaInfosResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteMediaInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetEventCallbackRequest(TeaModel):
    def __init__(
        self,
        callback_queue_name: str = None,
        event_type_list: str = None,
    ):
        self.callback_queue_name = callback_queue_name
        self.event_type_list = event_type_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.callback_queue_name is not None:
            result['CallbackQueueName'] = self.callback_queue_name
        if self.event_type_list is not None:
            result['EventTypeList'] = self.event_type_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallbackQueueName') is not None:
            self.callback_queue_name = m.get('CallbackQueueName')
        if m.get('EventTypeList') is not None:
            self.event_type_list = m.get('EventTypeList')
        return self


class SetEventCallbackResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 是否设置成功
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetEventCallbackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetEventCallbackResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetEventCallbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTemplateRequest(TeaModel):
    def __init__(
        self,
        template_id: str = None,
    ):
        # 模板Id
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class GetTemplateResponseBodyTemplate(TeaModel):
    def __init__(
        self,
        template_id: str = None,
        name: str = None,
        type: str = None,
        config: str = None,
        preview_media: str = None,
        status: str = None,
        create_source: str = None,
        modified_source: str = None,
        preview_media_status: str = None,
        creation_time: str = None,
        modified_time: str = None,
        cover_url: str = None,
        clips_param: str = None,
    ):
        # 模板ID
        self.template_id = template_id
        # 模板名称
        self.name = name
        # 模板类型
        self.type = type
        # 模板配置
        self.config = config
        # 预览素材
        self.preview_media = preview_media
        # 模板状态
        self.status = status
        # 创建来源
        self.create_source = create_source
        # 修改来源
        self.modified_source = modified_source
        # 预览素材状态
        self.preview_media_status = preview_media_status
        # 创建时间
        self.creation_time = creation_time
        # 修改时间
        self.modified_time = modified_time
        # 封面URL
        self.cover_url = cover_url
        # 提交合成任务的ClipsParam参数
        self.clips_param = clips_param

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.config is not None:
            result['Config'] = self.config
        if self.preview_media is not None:
            result['PreviewMedia'] = self.preview_media
        if self.status is not None:
            result['Status'] = self.status
        if self.create_source is not None:
            result['CreateSource'] = self.create_source
        if self.modified_source is not None:
            result['ModifiedSource'] = self.modified_source
        if self.preview_media_status is not None:
            result['PreviewMediaStatus'] = self.preview_media_status
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.clips_param is not None:
            result['ClipsParam'] = self.clips_param
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('PreviewMedia') is not None:
            self.preview_media = m.get('PreviewMedia')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreateSource') is not None:
            self.create_source = m.get('CreateSource')
        if m.get('ModifiedSource') is not None:
            self.modified_source = m.get('ModifiedSource')
        if m.get('PreviewMediaStatus') is not None:
            self.preview_media_status = m.get('PreviewMediaStatus')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('ClipsParam') is not None:
            self.clips_param = m.get('ClipsParam')
        return self


class GetTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        template: GetTemplateResponseBodyTemplate = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.template = template

    def validate(self):
        if self.template:
            self.template.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template is not None:
            result['Template'] = self.template.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Template') is not None:
            temp_model = GetTemplateResponseBodyTemplate()
            self.template = temp_model.from_map(m['Template'])
        return self


class GetTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetTemplateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RegisterMediaInfoRequest(TeaModel):
    def __init__(
        self,
        input_url: str = None,
        media_type: str = None,
        business_type: str = None,
        title: str = None,
        description: str = None,
        category: str = None,
        media_tags: str = None,
        cover_url: str = None,
        dynamic_meta_data_list: str = None,
        user_data: str = None,
        overwrite: bool = None,
        client_token: str = None,
        register_config: str = None,
    ):
        # 媒资媒体url
        self.input_url = input_url
        # 媒资媒体类型
        self.media_type = media_type
        # 媒资业务类型
        self.business_type = business_type
        # 标题
        self.title = title
        # 描述
        self.description = description
        # 分类
        self.category = category
        # 标签,如果有多个标签用逗号隔开
        self.media_tags = media_tags
        # 封面图，仅视频媒资有效
        self.cover_url = cover_url
        # 用户自定义元数据
        self.dynamic_meta_data_list = dynamic_meta_data_list
        # 用户数据，最大1024字节
        self.user_data = user_data
        # 是否覆盖已有媒资
        self.overwrite = overwrite
        # 客户端token
        self.client_token = client_token
        # 注册媒资的配置
        self.register_config = register_config

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_url is not None:
            result['InputURL'] = self.input_url
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.title is not None:
            result['Title'] = self.title
        if self.description is not None:
            result['Description'] = self.description
        if self.category is not None:
            result['Category'] = self.category
        if self.media_tags is not None:
            result['MediaTags'] = self.media_tags
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.dynamic_meta_data_list is not None:
            result['DynamicMetaDataList'] = self.dynamic_meta_data_list
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.overwrite is not None:
            result['Overwrite'] = self.overwrite
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.register_config is not None:
            result['RegisterConfig'] = self.register_config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputURL') is not None:
            self.input_url = m.get('InputURL')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('MediaTags') is not None:
            self.media_tags = m.get('MediaTags')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('DynamicMetaDataList') is not None:
            self.dynamic_meta_data_list = m.get('DynamicMetaDataList')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('Overwrite') is not None:
            self.overwrite = m.get('Overwrite')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegisterConfig') is not None:
            self.register_config = m.get('RegisterConfig')
        return self


class RegisterMediaInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        media_id: str = None,
    ):
        # 请求ID
        self.request_id = request_id
        # ICE媒资ID
        self.media_id = media_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        return self


class RegisterMediaInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RegisterMediaInfoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RegisterMediaInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEditingProjectRequest(TeaModel):
    def __init__(
        self,
        title: str = None,
        description: str = None,
        timeline: str = None,
        cover_url: str = None,
        feextend: str = None,
    ):
        # 云剪辑工程标题
        self.title = title
        # 云剪辑工程描述
        self.description = description
        # 云剪辑工程时间线，Json格式
        self.timeline = timeline
        # 云剪辑工程封面
        self.cover_url = cover_url
        # FEExtend
        self.feextend = feextend

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.title is not None:
            result['Title'] = self.title
        if self.description is not None:
            result['Description'] = self.description
        if self.timeline is not None:
            result['Timeline'] = self.timeline
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.feextend is not None:
            result['FEExtend'] = self.feextend
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Timeline') is not None:
            self.timeline = m.get('Timeline')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('FEExtend') is not None:
            self.feextend = m.get('FEExtend')
        return self


class CreateEditingProjectResponseBodyProject(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        title: str = None,
        description: str = None,
        timeline: str = None,
        cover_url: str = None,
        status: int = None,
        status_name: str = None,
        create_time: str = None,
        modified_time: str = None,
        duration: float = None,
        create_source: str = None,
        modified_source: str = None,
        template_type: str = None,
    ):
        self.project_id = project_id
        self.title = title
        self.description = description
        self.timeline = timeline
        self.cover_url = cover_url
        self.status = status
        self.status_name = status_name
        self.create_time = create_time
        self.modified_time = modified_time
        self.duration = duration
        self.create_source = create_source
        self.modified_source = modified_source
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.title is not None:
            result['Title'] = self.title
        if self.description is not None:
            result['Description'] = self.description
        if self.timeline is not None:
            result['Timeline'] = self.timeline
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.status is not None:
            result['Status'] = self.status
        if self.status_name is not None:
            result['StatusName'] = self.status_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.create_source is not None:
            result['CreateSource'] = self.create_source
        if self.modified_source is not None:
            result['ModifiedSource'] = self.modified_source
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Timeline') is not None:
            self.timeline = m.get('Timeline')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusName') is not None:
            self.status_name = m.get('StatusName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('CreateSource') is not None:
            self.create_source = m.get('CreateSource')
        if m.get('ModifiedSource') is not None:
            self.modified_source = m.get('ModifiedSource')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class CreateEditingProjectResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        project: CreateEditingProjectResponseBodyProject = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.project = project

    def validate(self):
        if self.project:
            self.project.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.project is not None:
            result['Project'] = self.project.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Project') is not None:
            temp_model = CreateEditingProjectResponseBodyProject()
            self.project = temp_model.from_map(m['Project'])
        return self


class CreateEditingProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateEditingProjectResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateEditingProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchGetMediaInfosRequest(TeaModel):
    def __init__(
        self,
        media_ids: str = None,
        addition_type: str = None,
    ):
        self.media_ids = media_ids
        self.addition_type = addition_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_ids is not None:
            result['MediaIds'] = self.media_ids
        if self.addition_type is not None:
            result['AdditionType'] = self.addition_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaIds') is not None:
            self.media_ids = m.get('MediaIds')
        if m.get('AdditionType') is not None:
            self.addition_type = m.get('AdditionType')
        return self


class BatchGetMediaInfosResponseBodyMediaInfosMediaBasicInfo(TeaModel):
    def __init__(
        self,
        media_id: str = None,
        input_url: str = None,
        media_type: str = None,
        business_type: str = None,
        source: str = None,
        title: str = None,
        description: str = None,
        category: str = None,
        media_tags: str = None,
        cover_url: str = None,
        user_data: str = None,
        snapshots: str = None,
        status: str = None,
        transcode_status: str = None,
        create_time: str = None,
        modified_time: str = None,
        deleted_time: str = None,
        sprite_images: str = None,
    ):
        # MediaId
        self.media_id = media_id
        # 待注册的媒资在相应系统中的地址
        self.input_url = input_url
        # 媒资媒体类型
        self.media_type = media_type
        # 媒资业务类型
        self.business_type = business_type
        # 来源
        self.source = source
        # 标题
        self.title = title
        # 内容描述
        self.description = description
        # 分类
        self.category = category
        # 标签
        self.media_tags = media_tags
        # 封面地址
        self.cover_url = cover_url
        # 用户数据
        self.user_data = user_data
        # 截图
        self.snapshots = snapshots
        # 资源状态
        self.status = status
        # 转码状态
        self.transcode_status = transcode_status
        # 媒资创建时间
        self.create_time = create_time
        # 媒资修改时间
        self.modified_time = modified_time
        # 媒资删除时间
        self.deleted_time = deleted_time
        # 雪碧图
        self.sprite_images = sprite_images

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.input_url is not None:
            result['InputURL'] = self.input_url
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.source is not None:
            result['Source'] = self.source
        if self.title is not None:
            result['Title'] = self.title
        if self.description is not None:
            result['Description'] = self.description
        if self.category is not None:
            result['Category'] = self.category
        if self.media_tags is not None:
            result['MediaTags'] = self.media_tags
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.snapshots is not None:
            result['Snapshots'] = self.snapshots
        if self.status is not None:
            result['Status'] = self.status
        if self.transcode_status is not None:
            result['TranscodeStatus'] = self.transcode_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.deleted_time is not None:
            result['DeletedTime'] = self.deleted_time
        if self.sprite_images is not None:
            result['SpriteImages'] = self.sprite_images
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('InputURL') is not None:
            self.input_url = m.get('InputURL')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('MediaTags') is not None:
            self.media_tags = m.get('MediaTags')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('Snapshots') is not None:
            self.snapshots = m.get('Snapshots')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TranscodeStatus') is not None:
            self.transcode_status = m.get('TranscodeStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('DeletedTime') is not None:
            self.deleted_time = m.get('DeletedTime')
        if m.get('SpriteImages') is not None:
            self.sprite_images = m.get('SpriteImages')
        return self


class BatchGetMediaInfosResponseBodyMediaInfosFileInfoListFileBasicInfo(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_status: str = None,
        file_type: str = None,
        file_size: str = None,
        file_url: str = None,
        region: str = None,
        format_name: str = None,
        duration: str = None,
        bitrate: str = None,
        width: str = None,
        height: str = None,
    ):
        # 文件名
        self.file_name = file_name
        # 文件状态
        self.file_status = file_status
        # 文件类型
        self.file_type = file_type
        # 文件大小（字节）
        self.file_size = file_size
        # 文件oss地址
        self.file_url = file_url
        # 文件存储区域
        self.region = region
        # 封装格式
        self.format_name = format_name
        # 时长
        self.duration = duration
        # 码率
        self.bitrate = bitrate
        # 宽
        self.width = width
        # 高
        self.height = height

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_status is not None:
            result['FileStatus'] = self.file_status
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.region is not None:
            result['Region'] = self.region
        if self.format_name is not None:
            result['FormatName'] = self.format_name
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileStatus') is not None:
            self.file_status = m.get('FileStatus')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('FormatName') is not None:
            self.format_name = m.get('FormatName')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class BatchGetMediaInfosResponseBodyMediaInfosFileInfoList(TeaModel):
    def __init__(
        self,
        file_basic_info: BatchGetMediaInfosResponseBodyMediaInfosFileInfoListFileBasicInfo = None,
    ):
        # 文件基础信息，包含时长，大小等
        self.file_basic_info = file_basic_info

    def validate(self):
        if self.file_basic_info:
            self.file_basic_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_basic_info is not None:
            result['FileBasicInfo'] = self.file_basic_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileBasicInfo') is not None:
            temp_model = BatchGetMediaInfosResponseBodyMediaInfosFileInfoListFileBasicInfo()
            self.file_basic_info = temp_model.from_map(m['FileBasicInfo'])
        return self


class BatchGetMediaInfosResponseBodyMediaInfos(TeaModel):
    def __init__(
        self,
        media_id: str = None,
        media_basic_info: BatchGetMediaInfosResponseBodyMediaInfosMediaBasicInfo = None,
        file_info_list: List[BatchGetMediaInfosResponseBodyMediaInfosFileInfoList] = None,
    ):
        # 媒资ID
        self.media_id = media_id
        # BasicInfo
        self.media_basic_info = media_basic_info
        # FileInfos
        self.file_info_list = file_info_list

    def validate(self):
        if self.media_basic_info:
            self.media_basic_info.validate()
        if self.file_info_list:
            for k in self.file_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.media_basic_info is not None:
            result['MediaBasicInfo'] = self.media_basic_info.to_map()
        result['FileInfoList'] = []
        if self.file_info_list is not None:
            for k in self.file_info_list:
                result['FileInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('MediaBasicInfo') is not None:
            temp_model = BatchGetMediaInfosResponseBodyMediaInfosMediaBasicInfo()
            self.media_basic_info = temp_model.from_map(m['MediaBasicInfo'])
        self.file_info_list = []
        if m.get('FileInfoList') is not None:
            for k in m.get('FileInfoList'):
                temp_model = BatchGetMediaInfosResponseBodyMediaInfosFileInfoList()
                self.file_info_list.append(temp_model.from_map(k))
        return self


class BatchGetMediaInfosResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        media_infos: List[BatchGetMediaInfosResponseBodyMediaInfos] = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 符合要求的媒资集合
        self.media_infos = media_infos

    def validate(self):
        if self.media_infos:
            for k in self.media_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['MediaInfos'] = []
        if self.media_infos is not None:
            for k in self.media_infos:
                result['MediaInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.media_infos = []
        if m.get('MediaInfos') is not None:
            for k in m.get('MediaInfos'):
                temp_model = BatchGetMediaInfosResponseBodyMediaInfos()
                self.media_infos.append(temp_model.from_map(k))
        return self


class BatchGetMediaInfosResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchGetMediaInfosResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = BatchGetMediaInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDefaultStorageLocationRequest(TeaModel):
    def __init__(
        self,
        storage_type: str = None,
        bucket: str = None,
        path: str = None,
    ):
        self.storage_type = storage_type
        self.bucket = bucket
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class SetDefaultStorageLocationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetDefaultStorageLocationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetDefaultStorageLocationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetDefaultStorageLocationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateMediaInfoRequest(TeaModel):
    def __init__(
        self,
        media_id: str = None,
        input_url: str = None,
        business_type: str = None,
        title: str = None,
        description: str = None,
        category: str = None,
        media_tags: str = None,
        cover_url: str = None,
        dynamic_meta_data_list: str = None,
        user_data: str = None,
        append_tags: bool = None,
        append_dynamic_meta: bool = None,
    ):
        # 媒资Id
        self.media_id = media_id
        # 媒资媒体类型
        self.input_url = input_url
        # 媒资业务类型
        self.business_type = business_type
        # 标题
        self.title = title
        # 描述
        self.description = description
        # 分类
        self.category = category
        # 标签,如果有多个标签用逗号隔开
        self.media_tags = media_tags
        # 封面图，仅视频媒资有效
        self.cover_url = cover_url
        # 用户自定义元数据
        self.dynamic_meta_data_list = dynamic_meta_data_list
        # 用户数据，最大1024字节
        self.user_data = user_data
        # 是否以append的形式更新Tags字段
        self.append_tags = append_tags
        # 是否以append的形式更新DynamicMetaDataList字段
        self.append_dynamic_meta = append_dynamic_meta

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.input_url is not None:
            result['InputURL'] = self.input_url
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.title is not None:
            result['Title'] = self.title
        if self.description is not None:
            result['Description'] = self.description
        if self.category is not None:
            result['Category'] = self.category
        if self.media_tags is not None:
            result['MediaTags'] = self.media_tags
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.dynamic_meta_data_list is not None:
            result['DynamicMetaDataList'] = self.dynamic_meta_data_list
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.append_tags is not None:
            result['AppendTags'] = self.append_tags
        if self.append_dynamic_meta is not None:
            result['AppendDynamicMeta'] = self.append_dynamic_meta
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('InputURL') is not None:
            self.input_url = m.get('InputURL')
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('MediaTags') is not None:
            self.media_tags = m.get('MediaTags')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('DynamicMetaDataList') is not None:
            self.dynamic_meta_data_list = m.get('DynamicMetaDataList')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('AppendTags') is not None:
            self.append_tags = m.get('AppendTags')
        if m.get('AppendDynamicMeta') is not None:
            self.append_dynamic_meta = m.get('AppendDynamicMeta')
        return self


class UpdateMediaInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        media_id: str = None,
    ):
        # 请求ID
        self.request_id = request_id
        # ICE媒资ID
        self.media_id = media_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        return self


class UpdateMediaInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateMediaInfoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateMediaInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMediaProducingJobRequest(TeaModel):
    def __init__(
        self,
        job_id: str = None,
    ):
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class GetMediaProducingJobResponseBodyMediaProducingJob(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        project_id: str = None,
        media_id: str = None,
        media_url: str = None,
        timeline: str = None,
        template_id: str = None,
        clips_param: str = None,
        duration: float = None,
        create_time: str = None,
        complete_time: str = None,
        modified_time: str = None,
        status: str = None,
        code: str = None,
        message: str = None,
    ):
        self.job_id = job_id
        self.project_id = project_id
        self.media_id = media_id
        self.media_url = media_url
        self.timeline = timeline
        self.template_id = template_id
        self.clips_param = clips_param
        self.duration = duration
        self.create_time = create_time
        self.complete_time = complete_time
        self.modified_time = modified_time
        self.status = status
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.media_url is not None:
            result['MediaURL'] = self.media_url
        if self.timeline is not None:
            result['Timeline'] = self.timeline
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.clips_param is not None:
            result['ClipsParam'] = self.clips_param
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.status is not None:
            result['Status'] = self.status
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('MediaURL') is not None:
            self.media_url = m.get('MediaURL')
        if m.get('Timeline') is not None:
            self.timeline = m.get('Timeline')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('ClipsParam') is not None:
            self.clips_param = m.get('ClipsParam')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class GetMediaProducingJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        media_producing_job: GetMediaProducingJobResponseBodyMediaProducingJob = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.media_producing_job = media_producing_job

    def validate(self):
        if self.media_producing_job:
            self.media_producing_job.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.media_producing_job is not None:
            result['MediaProducingJob'] = self.media_producing_job.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MediaProducingJob') is not None:
            temp_model = GetMediaProducingJobResponseBodyMediaProducingJob()
            self.media_producing_job = temp_model.from_map(m['MediaProducingJob'])
        return self


class GetMediaProducingJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetMediaProducingJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetMediaProducingJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeIceProductStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        iceservice_avaliable: bool = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.iceservice_avaliable = iceservice_avaliable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.iceservice_avaliable is not None:
            result['ICEServiceAvaliable'] = self.iceservice_avaliable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ICEServiceAvaliable') is not None:
            self.iceservice_avaliable = m.get('ICEServiceAvaliable')
        return self


class DescribeIceProductStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeIceProductStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeIceProductStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMediaBasicInfosRequest(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
        media_type: str = None,
        business_type: str = None,
        source: str = None,
        category: str = None,
        status: str = None,
        next_token: str = None,
        max_results: int = None,
        sort_by: str = None,
        include_file_basic_info: bool = None,
    ):
        # 创建时间
        self.start_time = start_time
        # 结束时间
        self.end_time = end_time
        # 媒资媒体类型
        self.media_type = media_type
        # 媒资业务类型
        self.business_type = business_type
        # 来源
        self.source = source
        # 分类
        self.category = category
        # 资源状态
        self.status = status
        # 页号
        self.next_token = next_token
        # 分页大小
        self.max_results = max_results
        # 排序
        self.sort_by = sort_by
        # 返回值中是否包含文件基础信息
        self.include_file_basic_info = include_file_basic_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.source is not None:
            result['Source'] = self.source
        if self.category is not None:
            result['Category'] = self.category
        if self.status is not None:
            result['Status'] = self.status
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.include_file_basic_info is not None:
            result['IncludeFileBasicInfo'] = self.include_file_basic_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('IncludeFileBasicInfo') is not None:
            self.include_file_basic_info = m.get('IncludeFileBasicInfo')
        return self


class ListMediaBasicInfosResponseBodyMediaInfosMediaBasicInfo(TeaModel):
    def __init__(
        self,
        media_id: str = None,
        input_url: str = None,
        media_type: str = None,
        business_type: str = None,
        source: str = None,
        title: str = None,
        description: str = None,
        category: str = None,
        media_tags: str = None,
        cover_url: str = None,
        user_data: str = None,
        snapshots: str = None,
        status: str = None,
        transcode_status: str = None,
        create_time: str = None,
        modified_time: str = None,
        deleted_time: str = None,
        sprite_images: str = None,
    ):
        # MediaId
        self.media_id = media_id
        # 待注册的媒资在相应系统中的地址
        self.input_url = input_url
        # 媒资媒体类型
        self.media_type = media_type
        # 媒资业务类型
        self.business_type = business_type
        # 来源
        self.source = source
        # 标题
        self.title = title
        # 内容描述
        self.description = description
        # 分类
        self.category = category
        # 标签
        self.media_tags = media_tags
        # 封面地址
        self.cover_url = cover_url
        # 用户数据
        self.user_data = user_data
        # 截图
        self.snapshots = snapshots
        # 资源状态
        self.status = status
        # 转码状态
        self.transcode_status = transcode_status
        # 媒资创建时间
        self.create_time = create_time
        # 媒资修改时间
        self.modified_time = modified_time
        # 媒资删除时间
        self.deleted_time = deleted_time
        # 雪碧图
        self.sprite_images = sprite_images

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.input_url is not None:
            result['InputURL'] = self.input_url
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.source is not None:
            result['Source'] = self.source
        if self.title is not None:
            result['Title'] = self.title
        if self.description is not None:
            result['Description'] = self.description
        if self.category is not None:
            result['Category'] = self.category
        if self.media_tags is not None:
            result['MediaTags'] = self.media_tags
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.snapshots is not None:
            result['Snapshots'] = self.snapshots
        if self.status is not None:
            result['Status'] = self.status
        if self.transcode_status is not None:
            result['TranscodeStatus'] = self.transcode_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.deleted_time is not None:
            result['DeletedTime'] = self.deleted_time
        if self.sprite_images is not None:
            result['SpriteImages'] = self.sprite_images
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('InputURL') is not None:
            self.input_url = m.get('InputURL')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('MediaTags') is not None:
            self.media_tags = m.get('MediaTags')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('Snapshots') is not None:
            self.snapshots = m.get('Snapshots')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TranscodeStatus') is not None:
            self.transcode_status = m.get('TranscodeStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('DeletedTime') is not None:
            self.deleted_time = m.get('DeletedTime')
        if m.get('SpriteImages') is not None:
            self.sprite_images = m.get('SpriteImages')
        return self


class ListMediaBasicInfosResponseBodyMediaInfosFileInfoListFileBasicInfo(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_status: str = None,
        file_type: str = None,
        file_size: str = None,
        file_url: str = None,
        region: str = None,
        format_name: str = None,
        duration: str = None,
        bitrate: str = None,
        width: str = None,
        height: str = None,
    ):
        # 文件名
        self.file_name = file_name
        # 文件状态
        self.file_status = file_status
        # 文件类型
        self.file_type = file_type
        # 文件大小（字节）
        self.file_size = file_size
        # 文件oss地址
        self.file_url = file_url
        # 文件存储区域
        self.region = region
        # 封装格式
        self.format_name = format_name
        # 时长
        self.duration = duration
        # 码率
        self.bitrate = bitrate
        # 宽
        self.width = width
        # 高
        self.height = height

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_status is not None:
            result['FileStatus'] = self.file_status
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.region is not None:
            result['Region'] = self.region
        if self.format_name is not None:
            result['FormatName'] = self.format_name
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileStatus') is not None:
            self.file_status = m.get('FileStatus')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('FormatName') is not None:
            self.format_name = m.get('FormatName')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class ListMediaBasicInfosResponseBodyMediaInfosFileInfoList(TeaModel):
    def __init__(
        self,
        file_basic_info: ListMediaBasicInfosResponseBodyMediaInfosFileInfoListFileBasicInfo = None,
    ):
        # 文件基础信息，包含时长，大小等
        self.file_basic_info = file_basic_info

    def validate(self):
        if self.file_basic_info:
            self.file_basic_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_basic_info is not None:
            result['FileBasicInfo'] = self.file_basic_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileBasicInfo') is not None:
            temp_model = ListMediaBasicInfosResponseBodyMediaInfosFileInfoListFileBasicInfo()
            self.file_basic_info = temp_model.from_map(m['FileBasicInfo'])
        return self


class ListMediaBasicInfosResponseBodyMediaInfos(TeaModel):
    def __init__(
        self,
        media_id: str = None,
        media_basic_info: ListMediaBasicInfosResponseBodyMediaInfosMediaBasicInfo = None,
        file_info_list: List[ListMediaBasicInfosResponseBodyMediaInfosFileInfoList] = None,
    ):
        # 媒资ID
        self.media_id = media_id
        # BasicInfo
        self.media_basic_info = media_basic_info
        # FileInfos
        self.file_info_list = file_info_list

    def validate(self):
        if self.media_basic_info:
            self.media_basic_info.validate()
        if self.file_info_list:
            for k in self.file_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.media_basic_info is not None:
            result['MediaBasicInfo'] = self.media_basic_info.to_map()
        result['FileInfoList'] = []
        if self.file_info_list is not None:
            for k in self.file_info_list:
                result['FileInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('MediaBasicInfo') is not None:
            temp_model = ListMediaBasicInfosResponseBodyMediaInfosMediaBasicInfo()
            self.media_basic_info = temp_model.from_map(m['MediaBasicInfo'])
        self.file_info_list = []
        if m.get('FileInfoList') is not None:
            for k in m.get('FileInfoList'):
                temp_model = ListMediaBasicInfosResponseBodyMediaInfosFileInfoList()
                self.file_info_list.append(temp_model.from_map(k))
        return self


class ListMediaBasicInfosResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        media_infos: List[ListMediaBasicInfosResponseBodyMediaInfos] = None,
        next_token: str = None,
        max_results: int = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 符合要求的媒资总数
        self.total_count = total_count
        # 符合要求的媒资集合
        self.media_infos = media_infos
        self.next_token = next_token
        self.max_results = max_results

    def validate(self):
        if self.media_infos:
            for k in self.media_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['MediaInfos'] = []
        if self.media_infos is not None:
            for k in self.media_infos:
                result['MediaInfos'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.media_infos = []
        if m.get('MediaInfos') is not None:
            for k in m.get('MediaInfos'):
                temp_model = ListMediaBasicInfosResponseBodyMediaInfos()
                self.media_infos.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListMediaBasicInfosResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListMediaBasicInfosResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListMediaBasicInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitSubtitleProduceJobRequest(TeaModel):
    def __init__(
        self,
        editing_config: str = None,
        type: str = None,
        output_config: str = None,
        input_config: str = None,
        is_async: int = None,
        title: str = None,
        description: str = None,
        user_data: str = None,
    ):
        self.editing_config = editing_config
        self.type = type
        self.output_config = output_config
        self.input_config = input_config
        self.is_async = is_async
        self.title = title
        self.description = description
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.editing_config is not None:
            result['EditingConfig'] = self.editing_config
        if self.type is not None:
            result['Type'] = self.type
        if self.output_config is not None:
            result['OutputConfig'] = self.output_config
        if self.input_config is not None:
            result['InputConfig'] = self.input_config
        if self.is_async is not None:
            result['IsAsync'] = self.is_async
        if self.title is not None:
            result['Title'] = self.title
        if self.description is not None:
            result['Description'] = self.description
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EditingConfig') is not None:
            self.editing_config = m.get('EditingConfig')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('OutputConfig') is not None:
            self.output_config = m.get('OutputConfig')
        if m.get('InputConfig') is not None:
            self.input_config = m.get('InputConfig')
        if m.get('IsAsync') is not None:
            self.is_async = m.get('IsAsync')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class SubmitSubtitleProduceJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        job_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class SubmitSubtitleProduceJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SubmitSubtitleProduceJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SubmitSubtitleProduceJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitKeyWordCutJobRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        input_file: str = None,
        user_data: str = None,
        title: str = None,
        description: str = None,
    ):
        self.keyword = keyword
        self.input_file = input_file
        self.user_data = user_data
        self.title = title
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.input_file is not None:
            result['InputFile'] = self.input_file
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.title is not None:
            result['Title'] = self.title
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('InputFile') is not None:
            self.input_file = m.get('InputFile')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class SubmitKeyWordCutJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        job_id: str = None,
        output: str = None,
        state: str = None,
        user_data: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.job_id = job_id
        self.output = output
        self.state = state
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.output is not None:
            result['Output'] = self.output
        if self.state is not None:
            result['State'] = self.state
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class SubmitKeyWordCutJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SubmitKeyWordCutJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SubmitKeyWordCutJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddEditingProjectMaterialsRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        material_maps: str = None,
    ):
        # 云剪辑工程ID
        self.project_id = project_id
        # 素材ID
        self.material_maps = material_maps

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.material_maps is not None:
            result['MaterialMaps'] = self.material_maps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('MaterialMaps') is not None:
            self.material_maps = m.get('MaterialMaps')
        return self


class AddEditingProjectMaterialsResponseBodyMediaInfosMediaBasicInfo(TeaModel):
    def __init__(
        self,
        media_id: str = None,
        input_url: str = None,
        media_type: str = None,
        business_type: str = None,
        source: str = None,
        title: str = None,
        description: str = None,
        category: str = None,
        media_tags: str = None,
        cover_url: str = None,
        user_data: str = None,
        snapshots: str = None,
        status: str = None,
        transcode_status: str = None,
        create_time: str = None,
        modified_time: str = None,
        deleted_time: str = None,
        sprite_images: str = None,
    ):
        # MediaId
        self.media_id = media_id
        # 待注册的媒资在相应系统中的地址
        self.input_url = input_url
        # 媒资媒体类型
        self.media_type = media_type
        # 媒资业务类型
        self.business_type = business_type
        # 来源
        self.source = source
        # 标题
        self.title = title
        # 内容描述
        self.description = description
        # 分类
        self.category = category
        # 标签
        self.media_tags = media_tags
        # 封面地址
        self.cover_url = cover_url
        # 用户数据
        self.user_data = user_data
        # 截图
        self.snapshots = snapshots
        # 资源状态
        self.status = status
        # 转码状态
        self.transcode_status = transcode_status
        # 媒资创建时间
        self.create_time = create_time
        # 媒资修改时间
        self.modified_time = modified_time
        # 媒资删除时间
        self.deleted_time = deleted_time
        # 雪碧图
        self.sprite_images = sprite_images

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.input_url is not None:
            result['InputURL'] = self.input_url
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.source is not None:
            result['Source'] = self.source
        if self.title is not None:
            result['Title'] = self.title
        if self.description is not None:
            result['Description'] = self.description
        if self.category is not None:
            result['Category'] = self.category
        if self.media_tags is not None:
            result['MediaTags'] = self.media_tags
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.snapshots is not None:
            result['Snapshots'] = self.snapshots
        if self.status is not None:
            result['Status'] = self.status
        if self.transcode_status is not None:
            result['TranscodeStatus'] = self.transcode_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.deleted_time is not None:
            result['DeletedTime'] = self.deleted_time
        if self.sprite_images is not None:
            result['SpriteImages'] = self.sprite_images
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('InputURL') is not None:
            self.input_url = m.get('InputURL')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('MediaTags') is not None:
            self.media_tags = m.get('MediaTags')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('Snapshots') is not None:
            self.snapshots = m.get('Snapshots')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TranscodeStatus') is not None:
            self.transcode_status = m.get('TranscodeStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('DeletedTime') is not None:
            self.deleted_time = m.get('DeletedTime')
        if m.get('SpriteImages') is not None:
            self.sprite_images = m.get('SpriteImages')
        return self


class AddEditingProjectMaterialsResponseBodyMediaInfosFileInfoListFileBasicInfo(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_status: str = None,
        file_type: str = None,
        file_size: str = None,
        file_url: str = None,
        region: str = None,
        format_name: str = None,
        duration: str = None,
        bitrate: str = None,
        width: str = None,
        height: str = None,
    ):
        # 文件名
        self.file_name = file_name
        # 文件状态
        self.file_status = file_status
        # 文件类型
        self.file_type = file_type
        # 文件大小（字节）
        self.file_size = file_size
        # 文件oss地址
        self.file_url = file_url
        # 文件存储区域
        self.region = region
        # 封装格式
        self.format_name = format_name
        # 时长
        self.duration = duration
        # 码率
        self.bitrate = bitrate
        # 宽
        self.width = width
        # 高
        self.height = height

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_status is not None:
            result['FileStatus'] = self.file_status
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.region is not None:
            result['Region'] = self.region
        if self.format_name is not None:
            result['FormatName'] = self.format_name
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileStatus') is not None:
            self.file_status = m.get('FileStatus')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('FormatName') is not None:
            self.format_name = m.get('FormatName')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class AddEditingProjectMaterialsResponseBodyMediaInfosFileInfoList(TeaModel):
    def __init__(
        self,
        file_basic_info: AddEditingProjectMaterialsResponseBodyMediaInfosFileInfoListFileBasicInfo = None,
    ):
        # 文件基础信息，包含时长，大小等
        self.file_basic_info = file_basic_info

    def validate(self):
        if self.file_basic_info:
            self.file_basic_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_basic_info is not None:
            result['FileBasicInfo'] = self.file_basic_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileBasicInfo') is not None:
            temp_model = AddEditingProjectMaterialsResponseBodyMediaInfosFileInfoListFileBasicInfo()
            self.file_basic_info = temp_model.from_map(m['FileBasicInfo'])
        return self


class AddEditingProjectMaterialsResponseBodyMediaInfos(TeaModel):
    def __init__(
        self,
        media_id: str = None,
        media_basic_info: AddEditingProjectMaterialsResponseBodyMediaInfosMediaBasicInfo = None,
        file_info_list: List[AddEditingProjectMaterialsResponseBodyMediaInfosFileInfoList] = None,
    ):
        # 媒资ID
        self.media_id = media_id
        # BasicInfo
        self.media_basic_info = media_basic_info
        # FileInfos
        self.file_info_list = file_info_list

    def validate(self):
        if self.media_basic_info:
            self.media_basic_info.validate()
        if self.file_info_list:
            for k in self.file_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.media_basic_info is not None:
            result['MediaBasicInfo'] = self.media_basic_info.to_map()
        result['FileInfoList'] = []
        if self.file_info_list is not None:
            for k in self.file_info_list:
                result['FileInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('MediaBasicInfo') is not None:
            temp_model = AddEditingProjectMaterialsResponseBodyMediaInfosMediaBasicInfo()
            self.media_basic_info = temp_model.from_map(m['MediaBasicInfo'])
        self.file_info_list = []
        if m.get('FileInfoList') is not None:
            for k in m.get('FileInfoList'):
                temp_model = AddEditingProjectMaterialsResponseBodyMediaInfosFileInfoList()
                self.file_info_list.append(temp_model.from_map(k))
        return self


class AddEditingProjectMaterialsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        project_id: str = None,
        media_infos: List[AddEditingProjectMaterialsResponseBodyMediaInfos] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.project_id = project_id
        # 符合要求的媒资集合
        self.media_infos = media_infos

    def validate(self):
        if self.media_infos:
            for k in self.media_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        result['MediaInfos'] = []
        if self.media_infos is not None:
            for k in self.media_infos:
                result['MediaInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        self.media_infos = []
        if m.get('MediaInfos') is not None:
            for k in m.get('MediaInfos'):
                temp_model = AddEditingProjectMaterialsResponseBodyMediaInfos()
                self.media_infos.append(temp_model.from_map(k))
        return self


class AddEditingProjectMaterialsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddEditingProjectMaterialsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddEditingProjectMaterialsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitASRJobRequest(TeaModel):
    def __init__(
        self,
        input_file: str = None,
        user_data: str = None,
        title: str = None,
        description: str = None,
        start_time: str = None,
        duration: str = None,
    ):
        self.input_file = input_file
        self.user_data = user_data
        self.title = title
        self.description = description
        # 开始时间
        self.start_time = start_time
        # 持续时间
        self.duration = duration

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_file is not None:
            result['InputFile'] = self.input_file
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.title is not None:
            result['Title'] = self.title
        if self.description is not None:
            result['Description'] = self.description
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.duration is not None:
            result['Duration'] = self.duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputFile') is not None:
            self.input_file = m.get('InputFile')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        return self


class SubmitASRJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        job_id: str = None,
        output: str = None,
        state: str = None,
        user_data: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.job_id = job_id
        self.output = output
        self.state = state
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.output is not None:
            result['Output'] = self.output
        if self.state is not None:
            result['State'] = self.state
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class SubmitASRJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SubmitASRJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SubmitASRJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEditingProjectRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
    ):
        # 云剪辑工程ID
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class GetEditingProjectResponseBodyProject(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        title: str = None,
        timeline: str = None,
        description: str = None,
        cover_url: str = None,
        create_time: str = None,
        modified_time: str = None,
        duration: int = None,
        status: str = None,
        create_source: str = None,
        template_type: str = None,
        modified_source: str = None,
    ):
        # 云剪辑工程ID
        self.project_id = project_id
        # 云剪辑工程标题
        self.title = title
        # 云剪辑工程时间线
        self.timeline = timeline
        # 云剪辑工程描述
        self.description = description
        # 云剪辑工程封面
        self.cover_url = cover_url
        # 云剪辑工程创建时间
        self.create_time = create_time
        # 云剪辑工程最新修改时间
        self.modified_time = modified_time
        # 云剪辑工程总时长
        self.duration = duration
        # 云剪辑工程状态
        self.status = status
        # 云剪辑工程创建来源
        self.create_source = create_source
        # 云剪辑工程模板类型
        self.template_type = template_type
        # 云剪辑工程修改来源
        self.modified_source = modified_source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.title is not None:
            result['Title'] = self.title
        if self.timeline is not None:
            result['Timeline'] = self.timeline
        if self.description is not None:
            result['Description'] = self.description
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.status is not None:
            result['Status'] = self.status
        if self.create_source is not None:
            result['CreateSource'] = self.create_source
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.modified_source is not None:
            result['ModifiedSource'] = self.modified_source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Timeline') is not None:
            self.timeline = m.get('Timeline')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreateSource') is not None:
            self.create_source = m.get('CreateSource')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('ModifiedSource') is not None:
            self.modified_source = m.get('ModifiedSource')
        return self


class GetEditingProjectResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        project: GetEditingProjectResponseBodyProject = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.project = project

    def validate(self):
        if self.project:
            self.project.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.project is not None:
            result['Project'] = self.project.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Project') is not None:
            temp_model = GetEditingProjectResponseBodyProject()
            self.project = temp_model.from_map(m['Project'])
        return self


class GetEditingProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetEditingProjectResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetEditingProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSysTemplatesRequest(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        max_results: int = None,
        type: str = None,
    ):
        # 标记当前开始读取的位置，置空表示从头开始
        self.next_token = next_token
        # 本次读取的最大数据记录数量
        self.max_results = max_results
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListSysTemplatesResponseBodyTemplates(TeaModel):
    def __init__(
        self,
        template_id: str = None,
        name: str = None,
        type: str = None,
        config: str = None,
    ):
        self.template_id = template_id
        self.name = name
        self.type = type
        self.config = config

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.config is not None:
            result['Config'] = self.config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        return self


class ListSysTemplatesResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        next_token: str = None,
        max_results: int = None,
        templates: List[ListSysTemplatesResponseBodyTemplates] = None,
    ):
        # TotalCount本次请求条件下的数据总量，此参数为可选参数，默认可不返回
        self.total_count = total_count
        # Id of the request
        self.request_id = request_id
        # 表示当前调用返回读取到的位置，空代表数据已经读取完毕
        self.next_token = next_token
        # MaxResults本次请求所返回的最大记录条数
        self.max_results = max_results
        self.templates = templates

    def validate(self):
        if self.templates:
            for k in self.templates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        result['Templates'] = []
        if self.templates is not None:
            for k in self.templates:
                result['Templates'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        self.templates = []
        if m.get('Templates') is not None:
            for k in m.get('Templates'):
                temp_model = ListSysTemplatesResponseBodyTemplates()
                self.templates.append(temp_model.from_map(k))
        return self


class ListSysTemplatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSysTemplatesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListSysTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTemplateRequest(TeaModel):
    def __init__(
        self,
        template_ids: str = None,
    ):
        # 模板id，多个id用英文逗号隔开
        self.template_ids = template_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_ids is not None:
            result['TemplateIds'] = self.template_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateIds') is not None:
            self.template_ids = m.get('TemplateIds')
        return self


class DeleteTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteTemplateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitIRJobRequest(TeaModel):
    def __init__(
        self,
        input_file: str = None,
        user_data: str = None,
        title: str = None,
        description: str = None,
    ):
        self.input_file = input_file
        self.user_data = user_data
        self.title = title
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_file is not None:
            result['InputFile'] = self.input_file
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.title is not None:
            result['Title'] = self.title
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputFile') is not None:
            self.input_file = m.get('InputFile')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class SubmitIRJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        job_id: str = None,
        output: str = None,
        state: str = None,
        user_data: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.job_id = job_id
        self.output = output
        self.state = state
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.output is not None:
            result['Output'] = self.output
        if self.state is not None:
            result['State'] = self.state
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class SubmitIRJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SubmitIRJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SubmitIRJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEditingProjectMaterialsRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        material_ids: str = None,
        material_type: str = None,
    ):
        # 云剪辑工程ID
        self.project_id = project_id
        # 素材ID
        self.material_ids = material_ids
        # 素材类型
        self.material_type = material_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.material_ids is not None:
            result['MaterialIds'] = self.material_ids
        if self.material_type is not None:
            result['MaterialType'] = self.material_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('MaterialIds') is not None:
            self.material_ids = m.get('MaterialIds')
        if m.get('MaterialType') is not None:
            self.material_type = m.get('MaterialType')
        return self


class DeleteEditingProjectMaterialsResponseBody(TeaModel):
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
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteEditingProjectMaterialsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteEditingProjectMaterialsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteEditingProjectMaterialsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchEditingProjectRequest(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
        status: str = None,
        sort_by: str = None,
        next_token: str = None,
        max_results: int = None,
        create_source: str = None,
        template_type: str = None,
    ):
        # CreateTime（创建时间）的开始时间
        self.start_time = start_time
        # CreationTime（创建时间）的结束时间
        self.end_time = end_time
        # 云剪辑工程状态。多个用逗号分隔
        self.status = status
        # 结果排序方式
        self.sort_by = sort_by
        # 分页参数
        self.next_token = next_token
        # 分页参数
        self.max_results = max_results
        # 创建来源
        self.create_source = create_source
        # 模板类型
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.status is not None:
            result['Status'] = self.status
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.create_source is not None:
            result['CreateSource'] = self.create_source
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('CreateSource') is not None:
            self.create_source = m.get('CreateSource')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class SearchEditingProjectResponseBodyProjectList(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        title: str = None,
        timeline: str = None,
        description: str = None,
        cover_url: str = None,
        create_time: str = None,
        modified_time: str = None,
        duration: int = None,
        status: str = None,
        error_code: str = None,
        error_message: str = None,
        create_source: str = None,
        modified_source: str = None,
        template_type: str = None,
    ):
        # 云剪辑工程ID
        self.project_id = project_id
        # 云剪辑工程标题
        self.title = title
        # 云剪辑工程时间线
        self.timeline = timeline
        # 云剪辑工程描述
        self.description = description
        # 云剪辑工程封面
        self.cover_url = cover_url
        # 云剪辑工程创建时间
        self.create_time = create_time
        # 云剪辑工程最新修改时间
        self.modified_time = modified_time
        # 云剪辑工程总时长
        self.duration = duration
        # 云剪辑工程状态
        self.status = status
        # 云剪辑工程合成失败的错误码
        self.error_code = error_code
        # 云剪辑工程合成失败的消息
        self.error_message = error_message
        # 创建来源
        self.create_source = create_source
        # 最后一次修改来源
        self.modified_source = modified_source
        # 模板类型
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.title is not None:
            result['Title'] = self.title
        if self.timeline is not None:
            result['Timeline'] = self.timeline
        if self.description is not None:
            result['Description'] = self.description
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.status is not None:
            result['Status'] = self.status
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.create_source is not None:
            result['CreateSource'] = self.create_source
        if self.modified_source is not None:
            result['ModifiedSource'] = self.modified_source
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Timeline') is not None:
            self.timeline = m.get('Timeline')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('CreateSource') is not None:
            self.create_source = m.get('CreateSource')
        if m.get('ModifiedSource') is not None:
            self.modified_source = m.get('ModifiedSource')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class SearchEditingProjectResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        project_list: List[SearchEditingProjectResponseBodyProjectList] = None,
        max_results: int = None,
        total_count: int = None,
        next_token: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 云剪辑工程列表
        self.project_list = project_list
        # 云剪辑工程总数
        self.max_results = max_results
        self.total_count = total_count
        self.next_token = next_token

    def validate(self):
        if self.project_list:
            for k in self.project_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ProjectList'] = []
        if self.project_list is not None:
            for k in self.project_list:
                result['ProjectList'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.project_list = []
        if m.get('ProjectList') is not None:
            for k in m.get('ProjectList'):
                temp_model = SearchEditingProjectResponseBodyProjectList()
                self.project_list.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class SearchEditingProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SearchEditingProjectResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SearchEditingProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTemplatesRequest(TeaModel):
    def __init__(
        self,
        type: str = None,
        status: str = None,
        create_source: str = None,
        keyword: str = None,
        sort_type: str = None,
    ):
        # 模板类型
        self.type = type
        # 模板状态
        self.status = status
        # 创建来源
        self.create_source = create_source
        # 搜索关键词，可以根据模板id和title搜索
        self.keyword = keyword
        # 排序参数，默认根据创建时间倒序
        self.sort_type = sort_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.status is not None:
            result['Status'] = self.status
        if self.create_source is not None:
            result['CreateSource'] = self.create_source
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.sort_type is not None:
            result['SortType'] = self.sort_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreateSource') is not None:
            self.create_source = m.get('CreateSource')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('SortType') is not None:
            self.sort_type = m.get('SortType')
        return self


class ListTemplatesResponseBodyTemplates(TeaModel):
    def __init__(
        self,
        template_id: str = None,
        name: str = None,
        type: str = None,
        config: str = None,
        preview_media: str = None,
        status: str = None,
        create_source: str = None,
        modified_source: str = None,
        preview_media_status: str = None,
        creation_time: str = None,
        modified_time: str = None,
        cover_url: str = None,
        clips_param: str = None,
    ):
        # 模板ID
        self.template_id = template_id
        # 模板名称
        self.name = name
        # 模板类型
        self.type = type
        # 模板配置
        self.config = config
        # 预览素材
        self.preview_media = preview_media
        # 模板状态
        self.status = status
        # 创建来源
        self.create_source = create_source
        # 修改来源
        self.modified_source = modified_source
        # 预览素材状态
        self.preview_media_status = preview_media_status
        # 创建时间
        self.creation_time = creation_time
        # 修改时间
        self.modified_time = modified_time
        # 封面URL
        self.cover_url = cover_url
        # ClipsParam
        self.clips_param = clips_param

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.config is not None:
            result['Config'] = self.config
        if self.preview_media is not None:
            result['PreviewMedia'] = self.preview_media
        if self.status is not None:
            result['Status'] = self.status
        if self.create_source is not None:
            result['CreateSource'] = self.create_source
        if self.modified_source is not None:
            result['ModifiedSource'] = self.modified_source
        if self.preview_media_status is not None:
            result['PreviewMediaStatus'] = self.preview_media_status
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.clips_param is not None:
            result['ClipsParam'] = self.clips_param
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('PreviewMedia') is not None:
            self.preview_media = m.get('PreviewMedia')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreateSource') is not None:
            self.create_source = m.get('CreateSource')
        if m.get('ModifiedSource') is not None:
            self.modified_source = m.get('ModifiedSource')
        if m.get('PreviewMediaStatus') is not None:
            self.preview_media_status = m.get('PreviewMediaStatus')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('ClipsParam') is not None:
            self.clips_param = m.get('ClipsParam')
        return self


class ListTemplatesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        templates: List[ListTemplatesResponseBodyTemplates] = None,
    ):
        # 请求ID
        self.request_id = request_id
        # 本次请求条件下的数据总量。
        self.total_count = total_count
        self.templates = templates

    def validate(self):
        if self.templates:
            for k in self.templates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Templates'] = []
        if self.templates is not None:
            for k in self.templates:
                result['Templates'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.templates = []
        if m.get('Templates') is not None:
            for k in m.get('Templates'):
                temp_model = ListTemplatesResponseBodyTemplates()
                self.templates.append(temp_model.from_map(k))
        return self


class ListTemplatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTemplatesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEditingProjectsRequest(TeaModel):
    def __init__(
        self,
        project_ids: str = None,
    ):
        # 云剪辑工程ID。支持多个云剪辑工程，以逗号分隔。
        self.project_ids = project_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_ids is not None:
            result['ProjectIds'] = self.project_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectIds') is not None:
            self.project_ids = m.get('ProjectIds')
        return self


class DeleteEditingProjectsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        ignored_list: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.ignored_list = ignored_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.ignored_list is not None:
            result['IgnoredList'] = self.ignored_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('IgnoredList') is not None:
            self.ignored_list = m.get('IgnoredList')
        return self


class DeleteEditingProjectsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteEditingProjectsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteEditingProjectsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMediaInfoRequest(TeaModel):
    def __init__(
        self,
        media_id: str = None,
        input_url: str = None,
        output_type: str = None,
    ):
        self.media_id = media_id
        self.input_url = input_url
        self.output_type = output_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.input_url is not None:
            result['InputURL'] = self.input_url
        if self.output_type is not None:
            result['OutputType'] = self.output_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('InputURL') is not None:
            self.input_url = m.get('InputURL')
        if m.get('OutputType') is not None:
            self.output_type = m.get('OutputType')
        return self


class GetMediaInfoResponseBodyMediaInfoMediaBasicInfo(TeaModel):
    def __init__(
        self,
        media_id: str = None,
        input_url: str = None,
        media_type: str = None,
        business_type: str = None,
        source: str = None,
        title: str = None,
        description: str = None,
        category: str = None,
        media_tags: str = None,
        cover_url: str = None,
        user_data: str = None,
        status: str = None,
        create_time: str = None,
        modified_time: str = None,
        deleted_time: str = None,
        sprite_images: str = None,
    ):
        # MediaId
        self.media_id = media_id
        # 待注册的媒资在相应系统中的地址
        self.input_url = input_url
        # 媒资媒体类型
        self.media_type = media_type
        # 媒资业务类型
        self.business_type = business_type
        # 来源
        self.source = source
        # 标题
        self.title = title
        # 内容描述
        self.description = description
        # 分类
        self.category = category
        # 标签
        self.media_tags = media_tags
        # 封面地址
        self.cover_url = cover_url
        # 用户数据
        self.user_data = user_data
        # 资源状态
        self.status = status
        # 媒资创建时间
        self.create_time = create_time
        # 媒资修改时间
        self.modified_time = modified_time
        # 媒资删除时间
        self.deleted_time = deleted_time
        # 雪碧图
        self.sprite_images = sprite_images

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.input_url is not None:
            result['InputURL'] = self.input_url
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.source is not None:
            result['Source'] = self.source
        if self.title is not None:
            result['Title'] = self.title
        if self.description is not None:
            result['Description'] = self.description
        if self.category is not None:
            result['Category'] = self.category
        if self.media_tags is not None:
            result['MediaTags'] = self.media_tags
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.status is not None:
            result['Status'] = self.status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.deleted_time is not None:
            result['DeletedTime'] = self.deleted_time
        if self.sprite_images is not None:
            result['SpriteImages'] = self.sprite_images
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('InputURL') is not None:
            self.input_url = m.get('InputURL')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('MediaTags') is not None:
            self.media_tags = m.get('MediaTags')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('DeletedTime') is not None:
            self.deleted_time = m.get('DeletedTime')
        if m.get('SpriteImages') is not None:
            self.sprite_images = m.get('SpriteImages')
        return self


class GetMediaInfoResponseBodyMediaInfoDynamicMetaDataList(TeaModel):
    def __init__(
        self,
        in_: float = None,
        out: float = None,
        type: str = None,
        data: str = None,
    ):
        # 开始时间
        self.in_ = in_
        # 结束时间
        self.out = out
        # 类型
        self.type = type
        # 元数据json string
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.in_ is not None:
            result['In'] = self.in_
        if self.out is not None:
            result['Out'] = self.out
        if self.type is not None:
            result['Type'] = self.type
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('In') is not None:
            self.in_ = m.get('In')
        if m.get('Out') is not None:
            self.out = m.get('Out')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class GetMediaInfoResponseBodyMediaInfoAiRoughDataList(TeaModel):
    def __init__(
        self,
        type: str = None,
        result: str = None,
    ):
        # AI类型
        self.type = type
        # AI原始结果
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class GetMediaInfoResponseBodyMediaInfoFileInfoListFileBasicInfo(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_status: str = None,
        file_type: str = None,
        file_size: str = None,
        file_url: str = None,
        region: str = None,
        format_name: str = None,
        duration: str = None,
        bitrate: str = None,
        width: str = None,
        height: str = None,
    ):
        # 文件名
        self.file_name = file_name
        # 文件状态
        self.file_status = file_status
        # 文件类型
        self.file_type = file_type
        # 文件大小（字节）
        self.file_size = file_size
        # 文件oss地址
        self.file_url = file_url
        # 文件存储区域
        self.region = region
        # 封装格式
        self.format_name = format_name
        # 时长
        self.duration = duration
        # 码率
        self.bitrate = bitrate
        # 宽
        self.width = width
        # 高
        self.height = height

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_status is not None:
            result['FileStatus'] = self.file_status
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.region is not None:
            result['Region'] = self.region
        if self.format_name is not None:
            result['FormatName'] = self.format_name
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileStatus') is not None:
            self.file_status = m.get('FileStatus')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('FormatName') is not None:
            self.format_name = m.get('FormatName')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class GetMediaInfoResponseBodyMediaInfoFileInfoListAudioStreamInfoList(TeaModel):
    def __init__(
        self,
        index: str = None,
        codec_name: str = None,
        codec_long_name: str = None,
        codec_time_base: str = None,
        codec_tag_string: str = None,
        codec_tag: str = None,
        profile: str = None,
        sample_fmt: str = None,
        sample_rate: str = None,
        channels: str = None,
        channel_layout: str = None,
        timebase: str = None,
        start_time: str = None,
        duration: str = None,
        bitrate: str = None,
        fps: str = None,
        num_frames: str = None,
        lang: str = None,
    ):
        # 音频流序号
        self.index = index
        # 编码格式简述名
        self.codec_name = codec_name
        # 编码格式长述名
        self.codec_long_name = codec_long_name
        # 编码时基
        self.codec_time_base = codec_time_base
        # 编码格式标记文本
        self.codec_tag_string = codec_tag_string
        # 编码格式标记
        self.codec_tag = codec_tag
        # 编码预置
        self.profile = profile
        # 采样格式
        self.sample_fmt = sample_fmt
        # 采样率
        self.sample_rate = sample_rate
        # 声道数
        self.channels = channels
        # 声道输出样式
        self.channel_layout = channel_layout
        # 时基
        self.timebase = timebase
        # 起始时间
        self.start_time = start_time
        # 时长
        self.duration = duration
        # 码率
        self.bitrate = bitrate
        # 音频帧率
        self.fps = fps
        # 总帧数
        self.num_frames = num_frames
        # 语言
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.codec_name is not None:
            result['CodecName'] = self.codec_name
        if self.codec_long_name is not None:
            result['CodecLongName'] = self.codec_long_name
        if self.codec_time_base is not None:
            result['CodecTimeBase'] = self.codec_time_base
        if self.codec_tag_string is not None:
            result['CodecTagString'] = self.codec_tag_string
        if self.codec_tag is not None:
            result['CodecTag'] = self.codec_tag
        if self.profile is not None:
            result['Profile'] = self.profile
        if self.sample_fmt is not None:
            result['SampleFmt'] = self.sample_fmt
        if self.sample_rate is not None:
            result['SampleRate'] = self.sample_rate
        if self.channels is not None:
            result['Channels'] = self.channels
        if self.channel_layout is not None:
            result['ChannelLayout'] = self.channel_layout
        if self.timebase is not None:
            result['Timebase'] = self.timebase
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.fps is not None:
            result['Fps'] = self.fps
        if self.num_frames is not None:
            result['NumFrames'] = self.num_frames
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('CodecName') is not None:
            self.codec_name = m.get('CodecName')
        if m.get('CodecLongName') is not None:
            self.codec_long_name = m.get('CodecLongName')
        if m.get('CodecTimeBase') is not None:
            self.codec_time_base = m.get('CodecTimeBase')
        if m.get('CodecTagString') is not None:
            self.codec_tag_string = m.get('CodecTagString')
        if m.get('CodecTag') is not None:
            self.codec_tag = m.get('CodecTag')
        if m.get('Profile') is not None:
            self.profile = m.get('Profile')
        if m.get('SampleFmt') is not None:
            self.sample_fmt = m.get('SampleFmt')
        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')
        if m.get('Channels') is not None:
            self.channels = m.get('Channels')
        if m.get('ChannelLayout') is not None:
            self.channel_layout = m.get('ChannelLayout')
        if m.get('Timebase') is not None:
            self.timebase = m.get('Timebase')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('Fps') is not None:
            self.fps = m.get('Fps')
        if m.get('NumFrames') is not None:
            self.num_frames = m.get('NumFrames')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class GetMediaInfoResponseBodyMediaInfoFileInfoListVideoStreamInfoList(TeaModel):
    def __init__(
        self,
        index: str = None,
        codec_name: str = None,
        codec_long_name: str = None,
        profile: str = None,
        codec_time_base: str = None,
        codec_tag_string: str = None,
        codec_tag: str = None,
        width: str = None,
        height: str = None,
        has_bframes: str = None,
        sar: str = None,
        dar: str = None,
        pix_fmt: str = None,
        level: str = None,
        fps: str = None,
        avg_fps: str = None,
        timebase: str = None,
        start_time: str = None,
        duration: str = None,
        bitrate: str = None,
        num_frames: str = None,
        lang: str = None,
        rotate: str = None,
        nb_frames: str = None,
    ):
        # 视频流序号
        self.index = index
        # 编码格式简述名
        self.codec_name = codec_name
        # 编码格式长述名
        self.codec_long_name = codec_long_name
        # 编码预置
        self.profile = profile
        # 编码时基
        self.codec_time_base = codec_time_base
        # 编码格式标记文本
        self.codec_tag_string = codec_tag_string
        # 编码格式标记
        self.codec_tag = codec_tag
        # 宽
        self.width = width
        # 高
        self.height = height
        # 是否有B帧
        self.has_bframes = has_bframes
        # 编码信号分辨率比
        self.sar = sar
        # 编码显示分辨率比
        self.dar = dar
        # 像素格式
        self.pix_fmt = pix_fmt
        # 编码等级
        self.level = level
        # 视频帧率
        self.fps = fps
        # 平均帧率
        self.avg_fps = avg_fps
        # 时基
        self.timebase = timebase
        # 起始时间
        self.start_time = start_time
        # 时长
        self.duration = duration
        # 码率
        self.bitrate = bitrate
        # 总帧数
        self.num_frames = num_frames
        # 语言
        self.lang = lang
        # 旋转
        self.rotate = rotate
        # 总帧数
        self.nb_frames = nb_frames

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.codec_name is not None:
            result['CodecName'] = self.codec_name
        if self.codec_long_name is not None:
            result['CodecLongName'] = self.codec_long_name
        if self.profile is not None:
            result['Profile'] = self.profile
        if self.codec_time_base is not None:
            result['CodecTimeBase'] = self.codec_time_base
        if self.codec_tag_string is not None:
            result['CodecTagString'] = self.codec_tag_string
        if self.codec_tag is not None:
            result['CodecTag'] = self.codec_tag
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.has_bframes is not None:
            result['HasBFrames'] = self.has_bframes
        if self.sar is not None:
            result['Sar'] = self.sar
        if self.dar is not None:
            result['Dar'] = self.dar
        if self.pix_fmt is not None:
            result['PixFmt'] = self.pix_fmt
        if self.level is not None:
            result['Level'] = self.level
        if self.fps is not None:
            result['Fps'] = self.fps
        if self.avg_fps is not None:
            result['AvgFPS'] = self.avg_fps
        if self.timebase is not None:
            result['Timebase'] = self.timebase
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.num_frames is not None:
            result['NumFrames'] = self.num_frames
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.rotate is not None:
            result['Rotate'] = self.rotate
        if self.nb_frames is not None:
            result['Nb_frames'] = self.nb_frames
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('CodecName') is not None:
            self.codec_name = m.get('CodecName')
        if m.get('CodecLongName') is not None:
            self.codec_long_name = m.get('CodecLongName')
        if m.get('Profile') is not None:
            self.profile = m.get('Profile')
        if m.get('CodecTimeBase') is not None:
            self.codec_time_base = m.get('CodecTimeBase')
        if m.get('CodecTagString') is not None:
            self.codec_tag_string = m.get('CodecTagString')
        if m.get('CodecTag') is not None:
            self.codec_tag = m.get('CodecTag')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('HasBFrames') is not None:
            self.has_bframes = m.get('HasBFrames')
        if m.get('Sar') is not None:
            self.sar = m.get('Sar')
        if m.get('Dar') is not None:
            self.dar = m.get('Dar')
        if m.get('PixFmt') is not None:
            self.pix_fmt = m.get('PixFmt')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Fps') is not None:
            self.fps = m.get('Fps')
        if m.get('AvgFPS') is not None:
            self.avg_fps = m.get('AvgFPS')
        if m.get('Timebase') is not None:
            self.timebase = m.get('Timebase')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('NumFrames') is not None:
            self.num_frames = m.get('NumFrames')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Rotate') is not None:
            self.rotate = m.get('Rotate')
        if m.get('Nb_frames') is not None:
            self.nb_frames = m.get('Nb_frames')
        return self


class GetMediaInfoResponseBodyMediaInfoFileInfoListSubtitleStreamInfoList(TeaModel):
    def __init__(
        self,
        index: str = None,
        codec_name: str = None,
        codec_long_name: str = None,
        codec_time_base: str = None,
        codec_tag_string: str = None,
        codec_tag: str = None,
        timebase: str = None,
        start_time: str = None,
        duration: str = None,
        lang: str = None,
    ):
        # 音频流序号
        self.index = index
        # 编码格式简述名
        self.codec_name = codec_name
        # 编码格式长述名
        self.codec_long_name = codec_long_name
        # 编码时基
        self.codec_time_base = codec_time_base
        # 编码格式标记文本
        self.codec_tag_string = codec_tag_string
        # 编码格式标记
        self.codec_tag = codec_tag
        # 时基
        self.timebase = timebase
        # 起始时间
        self.start_time = start_time
        # 时长
        self.duration = duration
        # 语言
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.codec_name is not None:
            result['CodecName'] = self.codec_name
        if self.codec_long_name is not None:
            result['CodecLongName'] = self.codec_long_name
        if self.codec_time_base is not None:
            result['CodecTimeBase'] = self.codec_time_base
        if self.codec_tag_string is not None:
            result['CodecTagString'] = self.codec_tag_string
        if self.codec_tag is not None:
            result['CodecTag'] = self.codec_tag
        if self.timebase is not None:
            result['Timebase'] = self.timebase
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('CodecName') is not None:
            self.codec_name = m.get('CodecName')
        if m.get('CodecLongName') is not None:
            self.codec_long_name = m.get('CodecLongName')
        if m.get('CodecTimeBase') is not None:
            self.codec_time_base = m.get('CodecTimeBase')
        if m.get('CodecTagString') is not None:
            self.codec_tag_string = m.get('CodecTagString')
        if m.get('CodecTag') is not None:
            self.codec_tag = m.get('CodecTag')
        if m.get('Timebase') is not None:
            self.timebase = m.get('Timebase')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class GetMediaInfoResponseBodyMediaInfoFileInfoList(TeaModel):
    def __init__(
        self,
        file_basic_info: GetMediaInfoResponseBodyMediaInfoFileInfoListFileBasicInfo = None,
        audio_stream_info_list: List[GetMediaInfoResponseBodyMediaInfoFileInfoListAudioStreamInfoList] = None,
        video_stream_info_list: List[GetMediaInfoResponseBodyMediaInfoFileInfoListVideoStreamInfoList] = None,
        subtitle_stream_info_list: List[GetMediaInfoResponseBodyMediaInfoFileInfoListSubtitleStreamInfoList] = None,
    ):
        # 文件基础信息，包含时长，大小等
        self.file_basic_info = file_basic_info
        # 音频流信息，一个媒资可能有多条音频流
        self.audio_stream_info_list = audio_stream_info_list
        # 视频流信息，一个媒资可能有多条视频流
        self.video_stream_info_list = video_stream_info_list
        # 字幕流信息，一个媒资可能有多条字幕流
        self.subtitle_stream_info_list = subtitle_stream_info_list

    def validate(self):
        if self.file_basic_info:
            self.file_basic_info.validate()
        if self.audio_stream_info_list:
            for k in self.audio_stream_info_list:
                if k:
                    k.validate()
        if self.video_stream_info_list:
            for k in self.video_stream_info_list:
                if k:
                    k.validate()
        if self.subtitle_stream_info_list:
            for k in self.subtitle_stream_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_basic_info is not None:
            result['FileBasicInfo'] = self.file_basic_info.to_map()
        result['AudioStreamInfoList'] = []
        if self.audio_stream_info_list is not None:
            for k in self.audio_stream_info_list:
                result['AudioStreamInfoList'].append(k.to_map() if k else None)
        result['VideoStreamInfoList'] = []
        if self.video_stream_info_list is not None:
            for k in self.video_stream_info_list:
                result['VideoStreamInfoList'].append(k.to_map() if k else None)
        result['SubtitleStreamInfoList'] = []
        if self.subtitle_stream_info_list is not None:
            for k in self.subtitle_stream_info_list:
                result['SubtitleStreamInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileBasicInfo') is not None:
            temp_model = GetMediaInfoResponseBodyMediaInfoFileInfoListFileBasicInfo()
            self.file_basic_info = temp_model.from_map(m['FileBasicInfo'])
        self.audio_stream_info_list = []
        if m.get('AudioStreamInfoList') is not None:
            for k in m.get('AudioStreamInfoList'):
                temp_model = GetMediaInfoResponseBodyMediaInfoFileInfoListAudioStreamInfoList()
                self.audio_stream_info_list.append(temp_model.from_map(k))
        self.video_stream_info_list = []
        if m.get('VideoStreamInfoList') is not None:
            for k in m.get('VideoStreamInfoList'):
                temp_model = GetMediaInfoResponseBodyMediaInfoFileInfoListVideoStreamInfoList()
                self.video_stream_info_list.append(temp_model.from_map(k))
        self.subtitle_stream_info_list = []
        if m.get('SubtitleStreamInfoList') is not None:
            for k in m.get('SubtitleStreamInfoList'):
                temp_model = GetMediaInfoResponseBodyMediaInfoFileInfoListSubtitleStreamInfoList()
                self.subtitle_stream_info_list.append(temp_model.from_map(k))
        return self


class GetMediaInfoResponseBodyMediaInfo(TeaModel):
    def __init__(
        self,
        media_id: str = None,
        media_basic_info: GetMediaInfoResponseBodyMediaInfoMediaBasicInfo = None,
        dynamic_meta_data_list: List[GetMediaInfoResponseBodyMediaInfoDynamicMetaDataList] = None,
        ai_rough_data_list: List[GetMediaInfoResponseBodyMediaInfoAiRoughDataList] = None,
        file_info_list: List[GetMediaInfoResponseBodyMediaInfoFileInfoList] = None,
    ):
        # 媒资ID
        self.media_id = media_id
        # BasicInfo
        self.media_basic_info = media_basic_info
        # 其他元数据
        self.dynamic_meta_data_list = dynamic_meta_data_list
        # AIMetadata
        self.ai_rough_data_list = ai_rough_data_list
        # FileInfos
        self.file_info_list = file_info_list

    def validate(self):
        if self.media_basic_info:
            self.media_basic_info.validate()
        if self.dynamic_meta_data_list:
            for k in self.dynamic_meta_data_list:
                if k:
                    k.validate()
        if self.ai_rough_data_list:
            for k in self.ai_rough_data_list:
                if k:
                    k.validate()
        if self.file_info_list:
            for k in self.file_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.media_basic_info is not None:
            result['MediaBasicInfo'] = self.media_basic_info.to_map()
        result['DynamicMetaDataList'] = []
        if self.dynamic_meta_data_list is not None:
            for k in self.dynamic_meta_data_list:
                result['DynamicMetaDataList'].append(k.to_map() if k else None)
        result['AiRoughDataList'] = []
        if self.ai_rough_data_list is not None:
            for k in self.ai_rough_data_list:
                result['AiRoughDataList'].append(k.to_map() if k else None)
        result['FileInfoList'] = []
        if self.file_info_list is not None:
            for k in self.file_info_list:
                result['FileInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('MediaBasicInfo') is not None:
            temp_model = GetMediaInfoResponseBodyMediaInfoMediaBasicInfo()
            self.media_basic_info = temp_model.from_map(m['MediaBasicInfo'])
        self.dynamic_meta_data_list = []
        if m.get('DynamicMetaDataList') is not None:
            for k in m.get('DynamicMetaDataList'):
                temp_model = GetMediaInfoResponseBodyMediaInfoDynamicMetaDataList()
                self.dynamic_meta_data_list.append(temp_model.from_map(k))
        self.ai_rough_data_list = []
        if m.get('AiRoughDataList') is not None:
            for k in m.get('AiRoughDataList'):
                temp_model = GetMediaInfoResponseBodyMediaInfoAiRoughDataList()
                self.ai_rough_data_list.append(temp_model.from_map(k))
        self.file_info_list = []
        if m.get('FileInfoList') is not None:
            for k in m.get('FileInfoList'):
                temp_model = GetMediaInfoResponseBodyMediaInfoFileInfoList()
                self.file_info_list.append(temp_model.from_map(k))
        return self


class GetMediaInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        media_info: GetMediaInfoResponseBodyMediaInfo = None,
    ):
        # RequestId
        self.request_id = request_id
        self.media_info = media_info

    def validate(self):
        if self.media_info:
            self.media_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.media_info is not None:
            result['MediaInfo'] = self.media_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MediaInfo') is not None:
            temp_model = GetMediaInfoResponseBodyMediaInfo()
            self.media_info = temp_model.from_map(m['MediaInfo'])
        return self


class GetMediaInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetMediaInfoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetMediaInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitSmartJobRequest(TeaModel):
    def __init__(
        self,
        editing_config: str = None,
        output_config: str = None,
        input_config: str = None,
        title: str = None,
        description: str = None,
        user_data: str = None,
        job_type: str = None,
    ):
        self.editing_config = editing_config
        self.output_config = output_config
        self.input_config = input_config
        self.title = title
        self.description = description
        self.user_data = user_data
        self.job_type = job_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.editing_config is not None:
            result['EditingConfig'] = self.editing_config
        if self.output_config is not None:
            result['OutputConfig'] = self.output_config
        if self.input_config is not None:
            result['InputConfig'] = self.input_config
        if self.title is not None:
            result['Title'] = self.title
        if self.description is not None:
            result['Description'] = self.description
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.job_type is not None:
            result['JobType'] = self.job_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EditingConfig') is not None:
            self.editing_config = m.get('EditingConfig')
        if m.get('OutputConfig') is not None:
            self.output_config = m.get('OutputConfig')
        if m.get('InputConfig') is not None:
            self.input_config = m.get('InputConfig')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        return self


class SubmitSmartJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        job_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class SubmitSmartJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SubmitSmartJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SubmitSmartJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitDelogoJobRequest(TeaModel):
    def __init__(
        self,
        input_file: str = None,
        user_data: str = None,
        title: str = None,
        description: str = None,
        output_config: str = None,
        input_type: str = None,
        overwrite: bool = None,
        output_media_target: str = None,
    ):
        # 输入文件
        self.input_file = input_file
        self.user_data = user_data
        self.title = title
        self.description = description
        # 输出bucket
        self.output_config = output_config
        # 输入文件类型
        self.input_type = input_type
        # 是否强制覆盖现有OSS文件
        self.overwrite = overwrite
        # 输出类型
        self.output_media_target = output_media_target

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_file is not None:
            result['InputFile'] = self.input_file
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.title is not None:
            result['Title'] = self.title
        if self.description is not None:
            result['Description'] = self.description
        if self.output_config is not None:
            result['OutputConfig'] = self.output_config
        if self.input_type is not None:
            result['InputType'] = self.input_type
        if self.overwrite is not None:
            result['Overwrite'] = self.overwrite
        if self.output_media_target is not None:
            result['OutputMediaTarget'] = self.output_media_target
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputFile') is not None:
            self.input_file = m.get('InputFile')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('OutputConfig') is not None:
            self.output_config = m.get('OutputConfig')
        if m.get('InputType') is not None:
            self.input_type = m.get('InputType')
        if m.get('Overwrite') is not None:
            self.overwrite = m.get('Overwrite')
        if m.get('OutputMediaTarget') is not None:
            self.output_media_target = m.get('OutputMediaTarget')
        return self


class SubmitDelogoJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        job_id: str = None,
        output: str = None,
        state: str = None,
        user_data: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.job_id = job_id
        self.output = output
        self.state = state
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.output is not None:
            result['Output'] = self.output
        if self.state is not None:
            result['State'] = self.state
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class SubmitDelogoJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SubmitDelogoJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SubmitDelogoJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTemplateRequest(TeaModel):
    def __init__(
        self,
        template_id: str = None,
        name: str = None,
        config: str = None,
        cover_url: str = None,
        preview_media: str = None,
        status: str = None,
        source: str = None,
    ):
        # 模板ID
        self.template_id = template_id
        # 模板名称
        self.name = name
        # 参见Timeline模板Config文档
        self.config = config
        # 模板封面
        self.cover_url = cover_url
        # 预览视频媒资id
        self.preview_media = preview_media
        # 模板状态
        self.status = status
        # 修改来源，默认OpenAPI
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.name is not None:
            result['Name'] = self.name
        if self.config is not None:
            result['Config'] = self.config
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.preview_media is not None:
            result['PreviewMedia'] = self.preview_media
        if self.status is not None:
            result['Status'] = self.status
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('PreviewMedia') is not None:
            self.preview_media = m.get('PreviewMedia')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class UpdateTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateTemplateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitAudioProduceJobRequest(TeaModel):
    def __init__(
        self,
        editing_config: str = None,
        output_config: str = None,
        input_config: str = None,
        title: str = None,
        description: str = None,
        user_data: str = None,
        overwrite: bool = None,
    ):
        self.editing_config = editing_config
        self.output_config = output_config
        self.input_config = input_config
        self.title = title
        self.description = description
        self.user_data = user_data
        self.overwrite = overwrite

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.editing_config is not None:
            result['EditingConfig'] = self.editing_config
        if self.output_config is not None:
            result['OutputConfig'] = self.output_config
        if self.input_config is not None:
            result['InputConfig'] = self.input_config
        if self.title is not None:
            result['Title'] = self.title
        if self.description is not None:
            result['Description'] = self.description
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.overwrite is not None:
            result['Overwrite'] = self.overwrite
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EditingConfig') is not None:
            self.editing_config = m.get('EditingConfig')
        if m.get('OutputConfig') is not None:
            self.output_config = m.get('OutputConfig')
        if m.get('InputConfig') is not None:
            self.input_config = m.get('InputConfig')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('Overwrite') is not None:
            self.overwrite = m.get('Overwrite')
        return self


class SubmitAudioProduceJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        job_id: str = None,
        state: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 任务ID
        self.job_id = job_id
        # 任务状态
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class SubmitAudioProduceJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SubmitAudioProduceJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SubmitAudioProduceJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitMediaProducingJobRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        timeline: str = None,
        template_id: str = None,
        clips_param: str = None,
        project_metadata: str = None,
        output_media_target: str = None,
        output_media_config: str = None,
        user_data: str = None,
        client_token: str = None,
        source: str = None,
    ):
        self.project_id = project_id
        self.timeline = timeline
        self.template_id = template_id
        self.clips_param = clips_param
        self.project_metadata = project_metadata
        self.output_media_target = output_media_target
        self.output_media_config = output_media_config
        self.user_data = user_data
        self.client_token = client_token
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.timeline is not None:
            result['Timeline'] = self.timeline
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.clips_param is not None:
            result['ClipsParam'] = self.clips_param
        if self.project_metadata is not None:
            result['ProjectMetadata'] = self.project_metadata
        if self.output_media_target is not None:
            result['OutputMediaTarget'] = self.output_media_target
        if self.output_media_config is not None:
            result['OutputMediaConfig'] = self.output_media_config
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Timeline') is not None:
            self.timeline = m.get('Timeline')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('ClipsParam') is not None:
            self.clips_param = m.get('ClipsParam')
        if m.get('ProjectMetadata') is not None:
            self.project_metadata = m.get('ProjectMetadata')
        if m.get('OutputMediaTarget') is not None:
            self.output_media_target = m.get('OutputMediaTarget')
        if m.get('OutputMediaConfig') is not None:
            self.output_media_config = m.get('OutputMediaConfig')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class SubmitMediaProducingJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        project_id: str = None,
        job_id: str = None,
        media_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 剪辑工程Id
        self.project_id = project_id
        # 合成作业Id
        self.job_id = job_id
        # 合成媒资Id
        self.media_id = media_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        return self


class SubmitMediaProducingJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SubmitMediaProducingJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SubmitMediaProducingJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSmartJobRequest(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        feextend: str = None,
    ):
        self.job_id = job_id
        self.feextend = feextend

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.feextend is not None:
            result['FEExtend'] = self.feextend
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('FEExtend') is not None:
            self.feextend = m.get('FEExtend')
        return self


class UpdateSmartJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        job_id: str = None,
        feextend: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.job_id = job_id
        self.feextend = feextend

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.feextend is not None:
            result['FEExtend'] = self.feextend
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('FEExtend') is not None:
            self.feextend = m.get('FEExtend')
        return self


class UpdateSmartJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateSmartJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateSmartJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAllPublicMediaTagsRequest(TeaModel):
    def __init__(
        self,
        business_type: str = None,
    ):
        # 媒资业务类型
        self.business_type = business_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        return self


class ListAllPublicMediaTagsResponseBodyMediaTagList(TeaModel):
    def __init__(
        self,
        media_tag_id: str = None,
        media_tag_name_chinese: str = None,
        media_tag_name_english: str = None,
    ):
        # 素材标签id
        self.media_tag_id = media_tag_id
        # 素材标签中文名
        self.media_tag_name_chinese = media_tag_name_chinese
        # 素材标签英文名
        self.media_tag_name_english = media_tag_name_english

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_tag_id is not None:
            result['MediaTagId'] = self.media_tag_id
        if self.media_tag_name_chinese is not None:
            result['MediaTagNameChinese'] = self.media_tag_name_chinese
        if self.media_tag_name_english is not None:
            result['MediaTagNameEnglish'] = self.media_tag_name_english
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaTagId') is not None:
            self.media_tag_id = m.get('MediaTagId')
        if m.get('MediaTagNameChinese') is not None:
            self.media_tag_name_chinese = m.get('MediaTagNameChinese')
        if m.get('MediaTagNameEnglish') is not None:
            self.media_tag_name_english = m.get('MediaTagNameEnglish')
        return self


class ListAllPublicMediaTagsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        media_tag_list: List[ListAllPublicMediaTagsResponseBodyMediaTagList] = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 公共素材库标签列表
        self.media_tag_list = media_tag_list

    def validate(self):
        if self.media_tag_list:
            for k in self.media_tag_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['MediaTagList'] = []
        if self.media_tag_list is not None:
            for k in self.media_tag_list:
                result['MediaTagList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.media_tag_list = []
        if m.get('MediaTagList') is not None:
            for k in m.get('MediaTagList'):
                temp_model = ListAllPublicMediaTagsResponseBodyMediaTagList()
                self.media_tag_list.append(temp_model.from_map(k))
        return self


class ListAllPublicMediaTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAllPublicMediaTagsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAllPublicMediaTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitMattingJobRequest(TeaModel):
    def __init__(
        self,
        input_file: str = None,
        user_data: str = None,
        title: str = None,
        description: str = None,
        output_config: str = None,
        input_type: str = None,
        overwrite: str = None,
        output_media_target: str = None,
    ):
        # 输入文件
        self.input_file = input_file
        self.user_data = user_data
        self.title = title
        self.description = description
        # 输出bucket
        self.output_config = output_config
        # 输入文件类型
        self.input_type = input_type
        # 是否强制覆盖现有OSS文件
        self.overwrite = overwrite
        # 输出类型
        self.output_media_target = output_media_target

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_file is not None:
            result['InputFile'] = self.input_file
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.title is not None:
            result['Title'] = self.title
        if self.description is not None:
            result['Description'] = self.description
        if self.output_config is not None:
            result['OutputConfig'] = self.output_config
        if self.input_type is not None:
            result['InputType'] = self.input_type
        if self.overwrite is not None:
            result['Overwrite'] = self.overwrite
        if self.output_media_target is not None:
            result['OutputMediaTarget'] = self.output_media_target
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputFile') is not None:
            self.input_file = m.get('InputFile')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('OutputConfig') is not None:
            self.output_config = m.get('OutputConfig')
        if m.get('InputType') is not None:
            self.input_type = m.get('InputType')
        if m.get('Overwrite') is not None:
            self.overwrite = m.get('Overwrite')
        if m.get('OutputMediaTarget') is not None:
            self.output_media_target = m.get('OutputMediaTarget')
        return self


class SubmitMattingJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        job_id: str = None,
        output: str = None,
        state: str = None,
        user_data: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.job_id = job_id
        self.output = output
        self.state = state
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.output is not None:
            result['Output'] = self.output
        if self.state is not None:
            result['State'] = self.state
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class SubmitMattingJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SubmitMattingJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SubmitMattingJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEventCallbackResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        callback_queue_name: str = None,
        event_type_list: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.callback_queue_name = callback_queue_name
        self.event_type_list = event_type_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.callback_queue_name is not None:
            result['CallbackQueueName'] = self.callback_queue_name
        if self.event_type_list is not None:
            result['EventTypeList'] = self.event_type_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CallbackQueueName') is not None:
            self.callback_queue_name = m.get('CallbackQueueName')
        if m.get('EventTypeList') is not None:
            self.event_type_list = m.get('EventTypeList')
        return self


class GetEventCallbackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetEventCallbackResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetEventCallbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPublicMediaBasicInfosRequest(TeaModel):
    def __init__(
        self,
        media_tag_id: str = None,
        next_token: str = None,
        max_results: int = None,
        include_file_basic_info: bool = None,
    ):
        # 标签
        self.media_tag_id = media_tag_id
        # 下一次读取的位置
        self.next_token = next_token
        # 分页大小
        self.max_results = max_results
        # 返回值中是否包含文件基础信息
        self.include_file_basic_info = include_file_basic_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_tag_id is not None:
            result['MediaTagId'] = self.media_tag_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.include_file_basic_info is not None:
            result['IncludeFileBasicInfo'] = self.include_file_basic_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaTagId') is not None:
            self.media_tag_id = m.get('MediaTagId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('IncludeFileBasicInfo') is not None:
            self.include_file_basic_info = m.get('IncludeFileBasicInfo')
        return self


class ListPublicMediaBasicInfosResponseBodyMediaInfosMediaBasicInfo(TeaModel):
    def __init__(
        self,
        media_id: str = None,
        input_url: str = None,
        media_type: str = None,
        business_type: str = None,
        source: str = None,
        title: str = None,
        description: str = None,
        category: str = None,
        media_tags: str = None,
        cover_url: str = None,
        user_data: str = None,
        snapshots: str = None,
        status: str = None,
        transcode_status: str = None,
        create_time: str = None,
        modified_time: str = None,
        deleted_time: str = None,
    ):
        # MediaId
        self.media_id = media_id
        # 待注册的媒资在相应系统中的地址
        self.input_url = input_url
        # 媒资媒体类型
        self.media_type = media_type
        # 媒资业务类型
        self.business_type = business_type
        # 来源
        self.source = source
        # 标题
        self.title = title
        # 内容描述
        self.description = description
        # 分类
        self.category = category
        # 标签
        self.media_tags = media_tags
        # 封面地址
        self.cover_url = cover_url
        # 用户数据
        self.user_data = user_data
        # 截图
        self.snapshots = snapshots
        # 资源状态
        self.status = status
        # 转码状态
        self.transcode_status = transcode_status
        # 媒资创建时间
        self.create_time = create_time
        # 媒资修改时间
        self.modified_time = modified_time
        # 媒资删除时间
        self.deleted_time = deleted_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.input_url is not None:
            result['InputURL'] = self.input_url
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.source is not None:
            result['Source'] = self.source
        if self.title is not None:
            result['Title'] = self.title
        if self.description is not None:
            result['Description'] = self.description
        if self.category is not None:
            result['Category'] = self.category
        if self.media_tags is not None:
            result['MediaTags'] = self.media_tags
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.snapshots is not None:
            result['Snapshots'] = self.snapshots
        if self.status is not None:
            result['Status'] = self.status
        if self.transcode_status is not None:
            result['TranscodeStatus'] = self.transcode_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.deleted_time is not None:
            result['DeletedTime'] = self.deleted_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('InputURL') is not None:
            self.input_url = m.get('InputURL')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('MediaTags') is not None:
            self.media_tags = m.get('MediaTags')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('Snapshots') is not None:
            self.snapshots = m.get('Snapshots')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TranscodeStatus') is not None:
            self.transcode_status = m.get('TranscodeStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('DeletedTime') is not None:
            self.deleted_time = m.get('DeletedTime')
        return self


class ListPublicMediaBasicInfosResponseBodyMediaInfosFileInfoListFileBasicInfo(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_status: str = None,
        file_type: str = None,
        file_size: str = None,
        file_url: str = None,
        region: str = None,
        format_name: str = None,
        duration: str = None,
        bitrate: str = None,
        width: str = None,
        height: str = None,
    ):
        # 文件名
        self.file_name = file_name
        # 文件状态
        self.file_status = file_status
        # 文件类型
        self.file_type = file_type
        # 文件大小（字节）
        self.file_size = file_size
        # 文件oss地址
        self.file_url = file_url
        # 文件存储区域
        self.region = region
        # 封装格式
        self.format_name = format_name
        # 时长
        self.duration = duration
        # 码率
        self.bitrate = bitrate
        # 宽
        self.width = width
        # 高
        self.height = height

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_status is not None:
            result['FileStatus'] = self.file_status
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.region is not None:
            result['Region'] = self.region
        if self.format_name is not None:
            result['FormatName'] = self.format_name
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileStatus') is not None:
            self.file_status = m.get('FileStatus')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('FormatName') is not None:
            self.format_name = m.get('FormatName')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class ListPublicMediaBasicInfosResponseBodyMediaInfosFileInfoList(TeaModel):
    def __init__(
        self,
        file_basic_info: ListPublicMediaBasicInfosResponseBodyMediaInfosFileInfoListFileBasicInfo = None,
    ):
        # 文件基础信息，包含时长，大小等
        self.file_basic_info = file_basic_info

    def validate(self):
        if self.file_basic_info:
            self.file_basic_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_basic_info is not None:
            result['FileBasicInfo'] = self.file_basic_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileBasicInfo') is not None:
            temp_model = ListPublicMediaBasicInfosResponseBodyMediaInfosFileInfoListFileBasicInfo()
            self.file_basic_info = temp_model.from_map(m['FileBasicInfo'])
        return self


class ListPublicMediaBasicInfosResponseBodyMediaInfos(TeaModel):
    def __init__(
        self,
        media_id: str = None,
        media_basic_info: ListPublicMediaBasicInfosResponseBodyMediaInfosMediaBasicInfo = None,
        file_info_list: List[ListPublicMediaBasicInfosResponseBodyMediaInfosFileInfoList] = None,
    ):
        # 媒资ID
        self.media_id = media_id
        # BasicInfo
        self.media_basic_info = media_basic_info
        # FileInfos
        self.file_info_list = file_info_list

    def validate(self):
        if self.media_basic_info:
            self.media_basic_info.validate()
        if self.file_info_list:
            for k in self.file_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.media_basic_info is not None:
            result['MediaBasicInfo'] = self.media_basic_info.to_map()
        result['FileInfoList'] = []
        if self.file_info_list is not None:
            for k in self.file_info_list:
                result['FileInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('MediaBasicInfo') is not None:
            temp_model = ListPublicMediaBasicInfosResponseBodyMediaInfosMediaBasicInfo()
            self.media_basic_info = temp_model.from_map(m['MediaBasicInfo'])
        self.file_info_list = []
        if m.get('FileInfoList') is not None:
            for k in m.get('FileInfoList'):
                temp_model = ListPublicMediaBasicInfosResponseBodyMediaInfosFileInfoList()
                self.file_info_list.append(temp_model.from_map(k))
        return self


class ListPublicMediaBasicInfosResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        media_infos: List[ListPublicMediaBasicInfosResponseBodyMediaInfos] = None,
        next_token: str = None,
        max_results: int = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 符合要求的媒资总数
        self.total_count = total_count
        # 符合要求的媒资集合
        self.media_infos = media_infos
        self.next_token = next_token
        self.max_results = max_results

    def validate(self):
        if self.media_infos:
            for k in self.media_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['MediaInfos'] = []
        if self.media_infos is not None:
            for k in self.media_infos:
                result['MediaInfos'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.media_infos = []
        if m.get('MediaInfos') is not None:
            for k in m.get('MediaInfos'):
                temp_model = ListPublicMediaBasicInfosResponseBodyMediaInfos()
                self.media_infos.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListPublicMediaBasicInfosResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListPublicMediaBasicInfosResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListPublicMediaBasicInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitCoverJobRequest(TeaModel):
    def __init__(
        self,
        input_file: str = None,
        user_data: str = None,
        title: str = None,
        description: str = None,
        output_config: str = None,
    ):
        # 输入文件
        self.input_file = input_file
        self.user_data = user_data
        self.title = title
        self.description = description
        # 输出bucket
        self.output_config = output_config

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_file is not None:
            result['InputFile'] = self.input_file
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.title is not None:
            result['Title'] = self.title
        if self.description is not None:
            result['Description'] = self.description
        if self.output_config is not None:
            result['OutputConfig'] = self.output_config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputFile') is not None:
            self.input_file = m.get('InputFile')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('OutputConfig') is not None:
            self.output_config = m.get('OutputConfig')
        return self


class SubmitCoverJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        job_id: str = None,
        output: str = None,
        state: str = None,
        user_data: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.job_id = job_id
        self.output = output
        self.state = state
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.output is not None:
            result['Output'] = self.output
        if self.state is not None:
            result['State'] = self.state
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class SubmitCoverJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SubmitCoverJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SubmitCoverJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSmartHandleJobRequest(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        with_ai_result: str = None,
    ):
        self.job_id = job_id
        self.with_ai_result = with_ai_result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.with_ai_result is not None:
            result['WithAiResult'] = self.with_ai_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('WithAiResult') is not None:
            self.with_ai_result = m.get('WithAiResult')
        return self


class GetSmartHandleJobResponseBodySmartJobInfoInputConfig(TeaModel):
    def __init__(
        self,
        input_file: str = None,
        job_parameters: str = None,
    ):
        self.input_file = input_file
        self.job_parameters = job_parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_file is not None:
            result['InputFile'] = self.input_file
        if self.job_parameters is not None:
            result['JobParameters'] = self.job_parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputFile') is not None:
            self.input_file = m.get('InputFile')
        if m.get('JobParameters') is not None:
            self.job_parameters = m.get('JobParameters')
        return self


class GetSmartHandleJobResponseBodySmartJobInfo(TeaModel):
    def __init__(
        self,
        title: str = None,
        description: str = None,
        user_id: str = None,
        editing_config: str = None,
        input_config: GetSmartHandleJobResponseBodySmartJobInfoInputConfig = None,
        output_config: str = None,
        create_time: str = None,
        modified_time: str = None,
        job_type: str = None,
    ):
        self.title = title
        self.description = description
        self.user_id = user_id
        self.editing_config = editing_config
        self.input_config = input_config
        self.output_config = output_config
        self.create_time = create_time
        self.modified_time = modified_time
        self.job_type = job_type

    def validate(self):
        if self.input_config:
            self.input_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.title is not None:
            result['Title'] = self.title
        if self.description is not None:
            result['Description'] = self.description
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.editing_config is not None:
            result['EditingConfig'] = self.editing_config
        if self.input_config is not None:
            result['InputConfig'] = self.input_config.to_map()
        if self.output_config is not None:
            result['outputConfig'] = self.output_config
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.job_type is not None:
            result['JobType'] = self.job_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('EditingConfig') is not None:
            self.editing_config = m.get('EditingConfig')
        if m.get('InputConfig') is not None:
            temp_model = GetSmartHandleJobResponseBodySmartJobInfoInputConfig()
            self.input_config = temp_model.from_map(m['InputConfig'])
        if m.get('outputConfig') is not None:
            self.output_config = m.get('outputConfig')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        return self


class GetSmartHandleJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        job_id: str = None,
        output: str = None,
        state: str = None,
        user_data: str = None,
        feextend: str = None,
        smart_job_info: GetSmartHandleJobResponseBodySmartJobInfo = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.job_id = job_id
        self.output = output
        self.state = state
        self.user_data = user_data
        self.feextend = feextend
        self.smart_job_info = smart_job_info

    def validate(self):
        if self.smart_job_info:
            self.smart_job_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.output is not None:
            result['Output'] = self.output
        if self.state is not None:
            result['State'] = self.state
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.feextend is not None:
            result['FEExtend'] = self.feextend
        if self.smart_job_info is not None:
            result['SmartJobInfo'] = self.smart_job_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('FEExtend') is not None:
            self.feextend = m.get('FEExtend')
        if m.get('SmartJobInfo') is not None:
            temp_model = GetSmartHandleJobResponseBodySmartJobInfo()
            self.smart_job_info = temp_model.from_map(m['SmartJobInfo'])
        return self


class GetSmartHandleJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSmartHandleJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetSmartHandleJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitH2VJobRequest(TeaModel):
    def __init__(
        self,
        input_file: str = None,
        user_data: str = None,
        title: str = None,
        description: str = None,
        output_config: str = None,
        input_type: str = None,
        overwrite: bool = None,
        output_media_target: str = None,
    ):
        # 输入文件
        self.input_file = input_file
        self.user_data = user_data
        self.title = title
        self.description = description
        # 输出bucket
        self.output_config = output_config
        # 输入文件类型
        self.input_type = input_type
        # 是否强制覆盖现有OSS文件
        self.overwrite = overwrite
        # 输出类型
        self.output_media_target = output_media_target

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_file is not None:
            result['InputFile'] = self.input_file
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.title is not None:
            result['Title'] = self.title
        if self.description is not None:
            result['Description'] = self.description
        if self.output_config is not None:
            result['OutputConfig'] = self.output_config
        if self.input_type is not None:
            result['InputType'] = self.input_type
        if self.overwrite is not None:
            result['Overwrite'] = self.overwrite
        if self.output_media_target is not None:
            result['OutputMediaTarget'] = self.output_media_target
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputFile') is not None:
            self.input_file = m.get('InputFile')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('OutputConfig') is not None:
            self.output_config = m.get('OutputConfig')
        if m.get('InputType') is not None:
            self.input_type = m.get('InputType')
        if m.get('Overwrite') is not None:
            self.overwrite = m.get('Overwrite')
        if m.get('OutputMediaTarget') is not None:
            self.output_media_target = m.get('OutputMediaTarget')
        return self


class SubmitH2VJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        job_id: str = None,
        output: str = None,
        state: str = None,
        user_data: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.job_id = job_id
        self.output = output
        self.state = state
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.output is not None:
            result['Output'] = self.output
        if self.state is not None:
            result['State'] = self.state
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class SubmitH2VJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SubmitH2VJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SubmitH2VJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitPPTCutJobRequest(TeaModel):
    def __init__(
        self,
        input_file: str = None,
        user_data: str = None,
        title: str = None,
        description: str = None,
    ):
        self.input_file = input_file
        self.user_data = user_data
        self.title = title
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_file is not None:
            result['InputFile'] = self.input_file
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.title is not None:
            result['Title'] = self.title
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputFile') is not None:
            self.input_file = m.get('InputFile')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class SubmitPPTCutJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        job_id: str = None,
        output: str = None,
        state: str = None,
        user_data: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.job_id = job_id
        self.output = output
        self.state = state
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.output is not None:
            result['Output'] = self.output
        if self.state is not None:
            result['State'] = self.state
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class SubmitPPTCutJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SubmitPPTCutJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SubmitPPTCutJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


