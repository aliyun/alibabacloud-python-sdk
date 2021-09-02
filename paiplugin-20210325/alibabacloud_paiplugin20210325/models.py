# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CreateSignatureRequest(TeaModel):
    def __init__(
        self,
        certificates: str = None,
        description: str = None,
        name: str = None,
        power_of_attorney: str = None,
        process_instance_id: str = None,
    ):
        # 签名归属方的三证合一，OSS地址，必须以https开头，使用前需要授权
        self.certificates = certificates
        # 申请说明
        self.description = description
        # 签名名称
        self.name = name
        # 授权委托书(Power of attorney)， OSS地址，必须以https或oss开头，使用前需要授权，同上
        self.power_of_attorney = power_of_attorney
        # 无需填写
        self.process_instance_id = process_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificates is not None:
            result['Certificates'] = self.certificates
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.power_of_attorney is not None:
            result['PowerOfAttorney'] = self.power_of_attorney
        if self.process_instance_id is not None:
            result['ProcessInstanceID'] = self.process_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Certificates') is not None:
            self.certificates = m.get('Certificates')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PowerOfAttorney') is not None:
            self.power_of_attorney = m.get('PowerOfAttorney')
        if m.get('ProcessInstanceID') is not None:
            self.process_instance_id = m.get('ProcessInstanceID')
        return self


class CreateSignatureResponseBodyData(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        id: str = None,
        name: str = None,
        status: int = None,
        updated_time: str = None,
    ):
        # 创建时间 (UTC+8)
        self.created_time = created_time
        # ID UUID
        self.id = id
        # 签名名称
        self.name = name
        # 审核状态
        # - 0 : 审核中
        # - 1 : 审核通过
        # - 2 : 审核不通过
        self.status = status
        # 更新时间 (UTC+8)
        self.updated_time = updated_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.id is not None:
            result['ID'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('ID') is not None:
            self.id = m.get('ID')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        return self


class CreateSignatureResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateSignatureResponseBodyData = None,
        error_code: int = None,
        error_message: str = None,
    ):
        # 返回数据
        self.data = data
        # 错误码
        self.error_code = error_code
        # 错误信息
        self.error_message = error_message

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateSignatureResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        return self


class CreateSignatureResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSignatureResponseBody = None,
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
            temp_model = CreateSignatureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTemplateResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        error_code: int = None,
        error_message: str = None,
    ):
        # 返回数据
        self.data = data
        # 错误码
        self.error_code = error_code
        # 错误信息
        self.error_message = error_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
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


class CreateTemplateRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        description: str = None,
        name: str = None,
        process_instance_id: str = None,
        signature_id: str = None,
        type: int = None,
    ):
        # 模板内容，请注意控制总字数在70个字以内，超出部分按长短信收费，按67个字为单位记一条短信，必须在结尾添加”回T退订“
        self.content = content
        # 申请说明
        self.description = description
        # 模板名称
        self.name = name
        # 无需填写
        self.process_instance_id = process_instance_id
        # 签名ID
        self.signature_id = signature_id
        # 模板类型：
        # 0：验证码。
        # 1：短信通知。
        # 2：推广短信。
        # 3：国际/港澳台消息。
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.process_instance_id is not None:
            result['ProcessInstanceID'] = self.process_instance_id
        if self.signature_id is not None:
            result['SignatureID'] = self.signature_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProcessInstanceID') is not None:
            self.process_instance_id = m.get('ProcessInstanceID')
        if m.get('SignatureID') is not None:
            self.signature_id = m.get('SignatureID')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateTemplateResponseBodyData(TeaModel):
    def __init__(
        self,
        content: str = None,
        created_time: str = None,
        id: str = None,
        name: str = None,
        status: int = None,
        template_code: str = None,
        updated_time: str = None,
    ):
        # 模板内容，长度:2-30
        self.content = content
        # 创建时间 (UTC+8)
        self.created_time = created_time
        # ID UUID
        self.id = id
        # 签名名称
        self.name = name
        # 审核状态
        # - 0 : 审核中
        # - 1 : 审核通过
        # - 2 : 审核不通过
        self.status = status
        # 模板Code
        self.template_code = template_code
        # 更新时间 (UTC+8)
        self.updated_time = updated_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.id is not None:
            result['ID'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('ID') is not None:
            self.id = m.get('ID')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        return self


class CreateTemplateResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateTemplateResponseBodyData = None,
        error_code: int = None,
        error_message: str = None,
    ):
        # 返回数据
        self.data = data
        # 错误码
        self.error_code = error_code
        # 错误信息
        self.error_message = error_message

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateTemplateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        return self


class CreateTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateTemplateResponseBody = None,
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
            temp_model = CreateTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTemplatesRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        status: int = None,
    ):
        # 模板名称，用于名称过滤或搜索，使用%name%模糊匹配
        self.name = name
        # 分页数，从1开始，默认为1
        self.page_number = page_number
        # 分页大小，默认为10
        self.page_size = page_size
        # 审核状态过滤
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListTemplatesResponseBodyDataTemplates(TeaModel):
    def __init__(
        self,
        content: str = None,
        created_time: str = None,
        id: str = None,
        name: str = None,
        status: int = None,
        template_code: str = None,
        updated_time: str = None,
    ):
        # 模板内容，长度:2-30
        self.content = content
        # 创建时间 (UTC+8)
        self.created_time = created_time
        # ID UUID
        self.id = id
        # 签名名称
        self.name = name
        # 审核状态
        # - 0 : 审核中
        # - 1 : 审核通过
        # - 2 : 审核不通过
        self.status = status
        # 模板Code
        self.template_code = template_code
        # 更新时间 (UTC+8)
        self.updated_time = updated_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.id is not None:
            result['ID'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('ID') is not None:
            self.id = m.get('ID')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        return self


class ListTemplatesResponseBodyData(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        templates: List[ListTemplatesResponseBodyDataTemplates] = None,
        total_count: int = None,
    ):
        # 分页数，从1开始，默认为1
        self.page_number = page_number
        # 分页大小，默认为10
        self.page_size = page_size
        # 模板列表
        self.templates = templates
        # 总模板数量
        self.total_count = total_count

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
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Templates'] = []
        if self.templates is not None:
            for k in self.templates:
                result['Templates'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.templates = []
        if m.get('Templates') is not None:
            for k in m.get('Templates'):
                temp_model = ListTemplatesResponseBodyDataTemplates()
                self.templates.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTemplatesResponseBody(TeaModel):
    def __init__(
        self,
        data: ListTemplatesResponseBodyData = None,
        error_code: int = None,
        error_message: str = None,
    ):
        # 返回数据
        self.data = data
        # 错误码
        self.error_code = error_code
        # 错误信息
        self.error_message = error_message

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListTemplatesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
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


class DeleteScheduleResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        error_code: int = None,
        error_message: str = None,
    ):
        # 返回数据
        self.data = data
        # 错误码
        self.error_code = error_code
        # 错误信息
        self.error_message = error_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        return self


class DeleteScheduleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteScheduleResponseBody = None,
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
            temp_model = DeleteScheduleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTemplateResponseBodyData(TeaModel):
    def __init__(
        self,
        content: str = None,
        created_time: str = None,
        description: str = None,
        id: str = None,
        name: str = None,
        reason: str = None,
        status: int = None,
        template_code: str = None,
        updated_time: str = None,
    ):
        # 模板内容
        self.content = content
        # 创建时间 (UTC+8)
        self.created_time = created_time
        # 申请说明
        self.description = description
        # ID UUID
        self.id = id
        # 签名名称
        self.name = name
        # 审核结果说明
        self.reason = reason
        # 审核状态
        # - 0 : 审核中
        # - 1 : 审核通过
        # - 2 : 审核不通过
        self.status = status
        # 模板Code
        self.template_code = template_code
        # 更新时间 (UTC+8)
        self.updated_time = updated_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['ID'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.status is not None:
            result['Status'] = self.status
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ID') is not None:
            self.id = m.get('ID')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        return self


class GetTemplateResponseBody(TeaModel):
    def __init__(
        self,
        data: GetTemplateResponseBodyData = None,
        error_code: int = None,
        error_message: str = None,
    ):
        # 返回数据
        self.data = data
        # 错误码
        self.error_code = error_code
        # 错误信息
        self.error_message = error_message

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetTemplateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
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


class ListSignaturesRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        status: int = None,
    ):
        # 签名名称，用于名称过滤或搜索，使用%name%模糊匹配
        self.name = name
        # 分页数，从1开始，默认为1
        self.page_number = page_number
        # 分页大小，默认为10
        self.page_size = page_size
        # 审核状态过滤
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListSignaturesResponseBodyDataSignatures(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        id: str = None,
        name: str = None,
        status: int = None,
        updated_time: str = None,
    ):
        # 创建时间 (UTC+8)
        self.created_time = created_time
        # ID UUID
        self.id = id
        # 签名名称
        self.name = name
        # 审核状态
        # - 0 : 审核中
        # - 1 : 审核通过
        # - 2 : 审核不通过
        self.status = status
        # 更新时间 (UTC+8)
        self.updated_time = updated_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.id is not None:
            result['ID'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('ID') is not None:
            self.id = m.get('ID')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        return self


class ListSignaturesResponseBodyData(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        signatures: List[ListSignaturesResponseBodyDataSignatures] = None,
        total_count: int = None,
    ):
        # 分页数，从1开始，默认为1
        self.page_number = page_number
        # 分页大小，默认为10
        self.page_size = page_size
        # 签名列表
        self.signatures = signatures
        # 总签名数量
        self.total_count = total_count

    def validate(self):
        if self.signatures:
            for k in self.signatures:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Signatures'] = []
        if self.signatures is not None:
            for k in self.signatures:
                result['Signatures'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.signatures = []
        if m.get('Signatures') is not None:
            for k in m.get('Signatures'):
                temp_model = ListSignaturesResponseBodyDataSignatures()
                self.signatures.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListSignaturesResponseBody(TeaModel):
    def __init__(
        self,
        data: ListSignaturesResponseBodyData = None,
        error_code: int = None,
        error_message: str = None,
    ):
        # 返回数据
        self.data = data
        # 错误码
        self.error_code = error_code
        # 错误信息
        self.error_message = error_message

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListSignaturesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        return self


class ListSignaturesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSignaturesResponseBody = None,
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
            temp_model = ListSignaturesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSignatureResponseBodyData(TeaModel):
    def __init__(
        self,
        certificates: str = None,
        created_time: str = None,
        description: str = None,
        id: str = None,
        name: str = None,
        power_of_attorney: str = None,
        reason: str = None,
        status: int = None,
        updated_time: str = None,
    ):
        # 签名归属方的三证合一，OSS地址，必须以https开头，使用前需要授权
        self.certificates = certificates
        # 创建时间 (UTC+8)
        self.created_time = created_time
        # 申请说明
        self.description = description
        # ID UUID
        self.id = id
        # 签名名称
        self.name = name
        # 授权委托书(Power of attorney)， OSS地址，必须以https或oss开头，使用前需要授权，同上
        self.power_of_attorney = power_of_attorney
        # 审核结果说明
        self.reason = reason
        # 审核状态
        # - 0 : 审核中
        # - 1 : 审核通过
        # - 2 : 审核不通过
        self.status = status
        # 更新时间 (UTC+8)
        self.updated_time = updated_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificates is not None:
            result['Certificates'] = self.certificates
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['ID'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.power_of_attorney is not None:
            result['PowerOfAttorney'] = self.power_of_attorney
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.status is not None:
            result['Status'] = self.status
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Certificates') is not None:
            self.certificates = m.get('Certificates')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ID') is not None:
            self.id = m.get('ID')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PowerOfAttorney') is not None:
            self.power_of_attorney = m.get('PowerOfAttorney')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        return self


class GetSignatureResponseBody(TeaModel):
    def __init__(
        self,
        data: GetSignatureResponseBodyData = None,
        error_code: int = None,
        error_message: str = None,
    ):
        # 返回数据
        self.data = data
        # 错误码
        self.error_code = error_code
        # 错误信息
        self.error_message = error_message

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetSignatureResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        return self


class GetSignatureResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSignatureResponseBody = None,
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
            temp_model = GetSignatureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateScheduleRequest(TeaModel):
    def __init__(
        self,
        data_address: str = None,
        data_source: int = None,
        ding_bot_keyword: str = None,
        ding_bot_token: str = None,
        name: str = None,
        partition: str = None,
        phone_number_column: str = None,
        send_time: str = None,
        signature_id: str = None,
        template_code_column: str = None,
        template_id: str = None,
    ):
        # 数据源地址
        # - 0: project/table
        # MaxCompute项目名和表名，使用前需要授权
        # - 1: oss地址 https://bucket.endpoint/path/to/file
        # OSS地址，必须以https开头，使用前需要授权，如 https://bucket.endpoint/path/to/file
        self.data_address = data_address
        # 数据源类型
        # - 0: MaxCompute
        # - 1: CSV
        # 数据源类型为CSV时，可以提供不带header的CSV文件或带header的CSV文件
        # 不带header的CSV文件每行为一个手机号
        # 使用带header的CSV文件，如果不指定手机号列名，默认使用第一列为手机号
        # 其他列可用于替换模板中的形如${variable}的变量，实现个性化发送
        self.data_source = data_source
        # 钉钉机器人关键词
        self.ding_bot_keyword = ding_bot_keyword
        # 钉钉机器人token
        self.ding_bot_token = ding_bot_token
        # 发送计划名称
        self.name = name
        # 分区表达式
        self.partition = partition
        # 手机号列名
        self.phone_number_column = phone_number_column
        # 发布时间 (UTC+8)，建议距现在10分钟后，不能距现在超过一年，否则会发生回绕，格式必须是2020-01-01 12:00:00
        self.send_time = send_time
        # 签名ID
        self.signature_id = signature_id
        # 模板号列名(可选)
        self.template_code_column = template_code_column
        # 模板ID
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_address is not None:
            result['DataAddress'] = self.data_address
        if self.data_source is not None:
            result['DataSource'] = self.data_source
        if self.ding_bot_keyword is not None:
            result['DingBotKeyword'] = self.ding_bot_keyword
        if self.ding_bot_token is not None:
            result['DingBotToken'] = self.ding_bot_token
        if self.name is not None:
            result['Name'] = self.name
        if self.partition is not None:
            result['Partition'] = self.partition
        if self.phone_number_column is not None:
            result['PhoneNumberColumn'] = self.phone_number_column
        if self.send_time is not None:
            result['SendTime'] = self.send_time
        if self.signature_id is not None:
            result['SignatureID'] = self.signature_id
        if self.template_code_column is not None:
            result['TemplateCodeColumn'] = self.template_code_column
        if self.template_id is not None:
            result['TemplateID'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataAddress') is not None:
            self.data_address = m.get('DataAddress')
        if m.get('DataSource') is not None:
            self.data_source = m.get('DataSource')
        if m.get('DingBotKeyword') is not None:
            self.ding_bot_keyword = m.get('DingBotKeyword')
        if m.get('DingBotToken') is not None:
            self.ding_bot_token = m.get('DingBotToken')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Partition') is not None:
            self.partition = m.get('Partition')
        if m.get('PhoneNumberColumn') is not None:
            self.phone_number_column = m.get('PhoneNumberColumn')
        if m.get('SendTime') is not None:
            self.send_time = m.get('SendTime')
        if m.get('SignatureID') is not None:
            self.signature_id = m.get('SignatureID')
        if m.get('TemplateCodeColumn') is not None:
            self.template_code_column = m.get('TemplateCodeColumn')
        if m.get('TemplateID') is not None:
            self.template_id = m.get('TemplateID')
        return self


class CreateScheduleResponseBodyData(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        id: str = None,
        name: str = None,
        send_time: str = None,
        signature_id: str = None,
        status: int = None,
        template_id: str = None,
        updated_time: str = None,
    ):
        # 创建时间 (UTC+8)
        self.created_time = created_time
        # ID
        self.id = id
        # 发送计划名称
        self.name = name
        # 发布时间 (UTC+8)
        self.send_time = send_time
        # 签名ID
        self.signature_id = signature_id
        # 状态
        # - 0: 检查中
        # - 1: 检查成功
        # - 2: 检查失败
        # - 3: 发送中
        # - 4: 发送成功
        # - 5: 发送失败
        self.status = status
        # 模板ID
        self.template_id = template_id
        # 更新时间 (UTC+8)
        self.updated_time = updated_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.id is not None:
            result['ID'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.send_time is not None:
            result['SendTime'] = self.send_time
        if self.signature_id is not None:
            result['SignatureID'] = self.signature_id
        if self.status is not None:
            result['Status'] = self.status
        if self.template_id is not None:
            result['TemplateID'] = self.template_id
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('ID') is not None:
            self.id = m.get('ID')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SendTime') is not None:
            self.send_time = m.get('SendTime')
        if m.get('SignatureID') is not None:
            self.signature_id = m.get('SignatureID')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateID') is not None:
            self.template_id = m.get('TemplateID')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        return self


class CreateScheduleResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateScheduleResponseBodyData = None,
        error_code: int = None,
        error_message: str = None,
    ):
        # 返回数据
        self.data = data
        # 错误码
        self.error_code = error_code
        # 错误信息
        self.error_message = error_message

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateScheduleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        return self


class CreateScheduleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateScheduleResponseBody = None,
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
            temp_model = CreateScheduleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSchedulesRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        status: int = None,
    ):
        # 发送计划名称，用于名称过滤或搜索，使用%name%模糊匹配
        self.name = name
        # 分页数，从1开始，默认为1
        self.page_number = page_number
        # 分页大小，默认为10
        self.page_size = page_size
        # 发送状态过滤
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListSchedulesResponseBodyDataSchedules(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        id: str = None,
        name: str = None,
        send_time: str = None,
        signature_id: str = None,
        status: int = None,
        template_id: str = None,
        updated_time: str = None,
    ):
        # 创建时间 (UTC+8)
        self.created_time = created_time
        # ID
        self.id = id
        # 发送计划名称
        self.name = name
        # 发布时间 (UTC+8)
        self.send_time = send_time
        # 签名ID
        self.signature_id = signature_id
        # 状态
        # - 0: 检查中
        # - 1: 检查成功
        # - 2: 检查失败
        # - 3: 发送中
        # - 4: 发送成功
        # - 5: 发送失败
        self.status = status
        # 模板ID
        self.template_id = template_id
        # 更新时间 (UTC+8)
        self.updated_time = updated_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.id is not None:
            result['ID'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.send_time is not None:
            result['SendTime'] = self.send_time
        if self.signature_id is not None:
            result['SignatureID'] = self.signature_id
        if self.status is not None:
            result['Status'] = self.status
        if self.template_id is not None:
            result['TemplateID'] = self.template_id
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('ID') is not None:
            self.id = m.get('ID')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SendTime') is not None:
            self.send_time = m.get('SendTime')
        if m.get('SignatureID') is not None:
            self.signature_id = m.get('SignatureID')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateID') is not None:
            self.template_id = m.get('TemplateID')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        return self


class ListSchedulesResponseBodyData(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        schedules: List[ListSchedulesResponseBodyDataSchedules] = None,
        total_count: int = None,
    ):
        # 分页数，从1开始，默认为1
        self.page_number = page_number
        # 分页大小，默认为10
        self.page_size = page_size
        # 发送计划列表
        self.schedules = schedules
        # 总发送计划数量
        self.total_count = total_count

    def validate(self):
        if self.schedules:
            for k in self.schedules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Schedules'] = []
        if self.schedules is not None:
            for k in self.schedules:
                result['Schedules'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.schedules = []
        if m.get('Schedules') is not None:
            for k in m.get('Schedules'):
                temp_model = ListSchedulesResponseBodyDataSchedules()
                self.schedules.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListSchedulesResponseBody(TeaModel):
    def __init__(
        self,
        data: ListSchedulesResponseBodyData = None,
        error_code: int = None,
        error_message: str = None,
    ):
        # 返回数据
        self.data = data
        # 错误码
        self.error_code = error_code
        # 错误信息
        self.error_message = error_message

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListSchedulesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        return self


class ListSchedulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSchedulesResponseBody = None,
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
            temp_model = ListSchedulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSignatureResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        error_code: int = None,
        error_message: str = None,
    ):
        # 返回数据
        self.data = data
        # 错误码
        self.error_code = error_code
        # 错误信息
        self.error_message = error_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        return self


class DeleteSignatureResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteSignatureResponseBody = None,
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
            temp_model = DeleteSignatureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


