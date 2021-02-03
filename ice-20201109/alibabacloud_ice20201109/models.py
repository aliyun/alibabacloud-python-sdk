# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


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
        # 前端编辑器工程数据结构
        self.feextend = feextend

    def validate(self):
        pass

    def to_map(self):
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
        create_time: str = None,
        modified_time: str = None,
        duration: float = None,
    ):
        self.project_id = project_id
        self.title = title
        self.description = description
        self.timeline = timeline
        self.cover_url = cover_url
        self.status = status
        self.create_time = create_time
        self.modified_time = modified_time
        self.duration = duration

    def validate(self):
        pass

    def to_map(self):
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
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.duration is not None:
            result['Duration'] = self.duration
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
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
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
        ignored_list: str = None,
    ):
        # 请求ID
        self.request_id = request_id
        # 出现获取错误的ID或inputUr
        self.ignored_list = ignored_list

    def validate(self):
        pass

    def to_map(self):
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


class DescribeRelatedAuthorizationStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        ossauthorized: bool = None,
        mtsauthorized: bool = None,
        mnsauthorized: bool = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.ossauthorized = ossauthorized
        self.mtsauthorized = mtsauthorized
        self.mnsauthorized = mnsauthorized

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.ossauthorized is not None:
            result['OSSAuthorized'] = self.ossauthorized
        if self.mtsauthorized is not None:
            result['MTSAuthorized'] = self.mtsauthorized
        if self.mnsauthorized is not None:
            result['MNSAuthorized'] = self.mnsauthorized
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


class GetEditingProjectRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        feextend_flag: int = None,
    ):
        # 云剪辑工程ID
        self.project_id = project_id
        # 是否返回编辑器数据结构
        self.feextend_flag = feextend_flag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.feextend_flag is not None:
            result['FEExtendFlag'] = self.feextend_flag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('FEExtendFlag') is not None:
            self.feextend_flag = m.get('FEExtendFlag')
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
        self.status = status

    def validate(self):
        pass

    def to_map(self):
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


class GetMediaInfoRequest(TeaModel):
    def __init__(
        self,
        media_id: str = None,
        input_url: str = None,
    ):
        self.media_id = media_id
        self.input_url = input_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.input_url is not None:
            result['InputURL'] = self.input_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('InputURL') is not None:
            self.input_url = m.get('InputURL')
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

    def validate(self):
        pass

    def to_map(self):
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


class GetMediaProducingJobRequest(TeaModel):
    def __init__(
        self,
        job_id: str = None,
    ):
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
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
        self.status = status
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
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
    ):
        # 素材标签id
        self.media_tag_id = media_tag_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.media_tag_id is not None:
            result['MediaTagId'] = self.media_tag_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaTagId') is not None:
            self.media_tag_id = m.get('MediaTagId')
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
        page_no: int = None,
        page_size: int = None,
        include_file_basic_info: bool = None,
        keyword: str = None,
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
        # 页数
        self.page_no = page_no
        # 分页大小
        self.page_size = page_size
        # 返回值中是否包含文件基础信息
        self.include_file_basic_info = include_file_basic_info
        # 针对媒资标题进行关键词搜索
        self.keyword = keyword

    def validate(self):
        pass

    def to_map(self):
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
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.include_file_basic_info is not None:
            result['IncludeFileBasicInfo'] = self.include_file_basic_info
        if self.keyword is not None:
            result['Keyword'] = self.keyword
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
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('IncludeFileBasicInfo') is not None:
            self.include_file_basic_info = m.get('IncludeFileBasicInfo')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
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


class ListPublicMediaBasicInfosRequest(TeaModel):
    def __init__(
        self,
        media_tag_id: str = None,
        next_token: str = None,
        max_results: int = None,
        page_no: int = None,
        page_size: int = None,
        include_file_basic_info: bool = None,
    ):
        # 标签
        self.media_tag_id = media_tag_id
        # 下一次读取的位置
        self.next_token = next_token
        # 分页大小
        self.max_results = max_results
        # 页数
        self.page_no = page_no
        # 分页大小
        self.page_size = page_size
        # 返回值中是否包含文件基础信息
        self.include_file_basic_info = include_file_basic_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.media_tag_id is not None:
            result['MediaTagId'] = self.media_tag_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
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
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
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

    def validate(self):
        pass

    def to_map(self):
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


class SearchEditingProjectRequest(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
        status: str = None,
        sort_by: str = None,
        next_token: str = None,
        max_results: int = None,
        page_no: int = None,
        page_size: int = None,
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
        # 分页参数
        self.page_no = page_no
        # 分页参数
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
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
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
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
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
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

    def validate(self):
        pass

    def to_map(self):
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

    def validate(self):
        pass

    def to_map(self):
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
        return self


class SubmitMediaProducingJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        project_id: str = None,
        job_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 剪辑工程Id
        self.project_id = project_id
        # 合成作业Id
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
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


class UpdateEditingProjectRequest(TeaModel):
    def __init__(
        self,
        title: str = None,
        description: str = None,
        timeline: str = None,
        cover_url: str = None,
        project_id: str = None,
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
        # 云剪辑工程ID
        self.project_id = project_id
        # 前端编辑器工程数据结构
        self.feextend = feextend

    def validate(self):
        pass

    def to_map(self):
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
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('FEExtend') is not None:
            self.feextend = m.get('FEExtend')
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
        snapshots: str = None,
        dynamic_meta_data_list: str = None,
        user_data: str = None,
        append_tags: bool = None,
        append_snapshots: bool = None,
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
        # 截图
        self.snapshots = snapshots
        # 用户自定义元数据
        self.dynamic_meta_data_list = dynamic_meta_data_list
        # 用户数据，最大1024字节
        self.user_data = user_data
        # 是否以append的形式更新Tags字段
        self.append_tags = append_tags
        # 是否以append的形式更新Snapshots字段
        self.append_snapshots = append_snapshots
        # 是否以append的形式更新DynamicMetaDataList字段
        self.append_dynamic_meta = append_dynamic_meta

    def validate(self):
        pass

    def to_map(self):
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
        if self.snapshots is not None:
            result['Snapshots'] = self.snapshots
        if self.dynamic_meta_data_list is not None:
            result['DynamicMetaDataList'] = self.dynamic_meta_data_list
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.append_tags is not None:
            result['AppendTags'] = self.append_tags
        if self.append_snapshots is not None:
            result['AppendSnapshots'] = self.append_snapshots
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
        if m.get('Snapshots') is not None:
            self.snapshots = m.get('Snapshots')
        if m.get('DynamicMetaDataList') is not None:
            self.dynamic_meta_data_list = m.get('DynamicMetaDataList')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('AppendTags') is not None:
            self.append_tags = m.get('AppendTags')
        if m.get('AppendSnapshots') is not None:
            self.append_snapshots = m.get('AppendSnapshots')
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


