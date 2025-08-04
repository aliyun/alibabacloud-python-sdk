# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class AddCategoryRequest(TeaModel):
    def __init__(
        self,
        category_name: str = None,
        category_type: str = None,
        parent_category_id: str = None,
    ):
        # This parameter is required.
        self.category_name = category_name
        # This parameter is required.
        self.category_type = category_type
        self.parent_category_id = parent_category_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.category_type is not None:
            result['CategoryType'] = self.category_type
        if self.parent_category_id is not None:
            result['ParentCategoryId'] = self.parent_category_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('CategoryType') is not None:
            self.category_type = m.get('CategoryType')
        if m.get('ParentCategoryId') is not None:
            self.parent_category_id = m.get('ParentCategoryId')
        return self


class AddCategoryResponseBodyData(TeaModel):
    def __init__(
        self,
        category_id: str = None,
        category_name: str = None,
    ):
        self.category_id = category_id
        self.category_name = category_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        return self


class AddCategoryResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: AddCategoryResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.status = status
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = AddCategoryResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddCategoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddCategoryResponseBody = None,
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
            temp_model = AddCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddFileRequest(TeaModel):
    def __init__(
        self,
        category_id: str = None,
        category_type: str = None,
        lease_id: str = None,
        original_file_url: str = None,
        parser: str = None,
        tags: List[str] = None,
    ):
        # The primary key ID of the category to which the document is uploaded. This parameter corresponds to the `CategoryId` returned by the [AddCategory](https://www.alibabacloud.com/help/eh/model-studio/developer-reference/api-bailian-2023-12-29-addcategory) operation. You can also click the ID icon next to the category name on the Unstructured Data tab of the [Application Data](https://modelstudio.console.alibabacloud.com/#/data-center) page to view the ID. You can set the parameter to default, which specifies the Default Category created by the system.
        # 
        # This parameter is required.
        self.category_id = category_id
        # The type of the category. Valid values:
        # - UNSTRUCTURED
        # - SESSION_FILE
        self.category_type = category_type
        # The lease ID, which corresponds to the `FileUploadLeaseId` parameter returned by the [ApplyFileUploadLease](https://www.alibabacloud.com/help/en/model-studio/developer-reference/api-bailian-2023-12-29-applyfileuploadlease) operation.
        # 
        # This parameter is required.
        self.lease_id = lease_id
        self.original_file_url = original_file_url
        # The parser. Valid value:
        # 
        # *   DASHSCOPE_DOCMIND: Intelligent document parsing by Alibaba Cloud.
        # 
        # This parameter is required.
        self.parser = parser
        # A list of tags associated with the document. The default value is null, which means no tags. You can specify up to 10 tags.
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.category_type is not None:
            result['CategoryType'] = self.category_type
        if self.lease_id is not None:
            result['LeaseId'] = self.lease_id
        if self.original_file_url is not None:
            result['OriginalFileUrl'] = self.original_file_url
        if self.parser is not None:
            result['Parser'] = self.parser
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CategoryType') is not None:
            self.category_type = m.get('CategoryType')
        if m.get('LeaseId') is not None:
            self.lease_id = m.get('LeaseId')
        if m.get('OriginalFileUrl') is not None:
            self.original_file_url = m.get('OriginalFileUrl')
        if m.get('Parser') is not None:
            self.parser = m.get('Parser')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class AddFileShrinkRequest(TeaModel):
    def __init__(
        self,
        category_id: str = None,
        category_type: str = None,
        lease_id: str = None,
        original_file_url: str = None,
        parser: str = None,
        tags_shrink: str = None,
    ):
        # The primary key ID of the category to which the document is uploaded. This parameter corresponds to the `CategoryId` returned by the [AddCategory](https://www.alibabacloud.com/help/eh/model-studio/developer-reference/api-bailian-2023-12-29-addcategory) operation. You can also click the ID icon next to the category name on the Unstructured Data tab of the [Application Data](https://modelstudio.console.alibabacloud.com/#/data-center) page to view the ID. You can set the parameter to default, which specifies the Default Category created by the system.
        # 
        # This parameter is required.
        self.category_id = category_id
        # The type of the category. Valid values:
        # - UNSTRUCTURED
        # - SESSION_FILE
        self.category_type = category_type
        # The lease ID, which corresponds to the `FileUploadLeaseId` parameter returned by the [ApplyFileUploadLease](https://www.alibabacloud.com/help/en/model-studio/developer-reference/api-bailian-2023-12-29-applyfileuploadlease) operation.
        # 
        # This parameter is required.
        self.lease_id = lease_id
        self.original_file_url = original_file_url
        # The parser. Valid value:
        # 
        # *   DASHSCOPE_DOCMIND: Intelligent document parsing by Alibaba Cloud.
        # 
        # This parameter is required.
        self.parser = parser
        # A list of tags associated with the document. The default value is null, which means no tags. You can specify up to 10 tags.
        self.tags_shrink = tags_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.category_type is not None:
            result['CategoryType'] = self.category_type
        if self.lease_id is not None:
            result['LeaseId'] = self.lease_id
        if self.original_file_url is not None:
            result['OriginalFileUrl'] = self.original_file_url
        if self.parser is not None:
            result['Parser'] = self.parser
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CategoryType') is not None:
            self.category_type = m.get('CategoryType')
        if m.get('LeaseId') is not None:
            self.lease_id = m.get('LeaseId')
        if m.get('OriginalFileUrl') is not None:
            self.original_file_url = m.get('OriginalFileUrl')
        if m.get('Parser') is not None:
            self.parser = m.get('Parser')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        return self


class AddFileResponseBodyData(TeaModel):
    def __init__(
        self,
        file_id: str = None,
        parser: str = None,
    ):
        # The primary key ID of the document. We recommend that you store the ID because it is required for all subsequent API operations related to this document.
        self.file_id = file_id
        # The parser that is used to parse the document. Valid value:
        # 
        # *   DASHSCOPE_DOCMIND: Intelligent document parsing by Alibaba Cloud.
        self.parser = parser

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.parser is not None:
            result['Parser'] = self.parser
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('Parser') is not None:
            self.parser = m.get('Parser')
        return self


class AddFileResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: AddFileResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: str = None,
    ):
        # The status code.
        self.code = code
        # The returned data fields.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The HTTP status code.
        self.status = status
        # Indications whether the call is successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = AddFileResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddFileResponseBody = None,
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
            temp_model = AddFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddFilesFromAuthorizedOssRequestFileDetails(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        oss_key: str = None,
    ):
        # This parameter is required.
        self.file_name = file_name
        # This parameter is required.
        self.oss_key = oss_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        return self


class AddFilesFromAuthorizedOssRequest(TeaModel):
    def __init__(
        self,
        category_id: str = None,
        category_type: str = None,
        file_details: List[AddFilesFromAuthorizedOssRequestFileDetails] = None,
        oss_bucket_name: str = None,
        oss_region_id: str = None,
        tags: List[str] = None,
    ):
        # This parameter is required.
        self.category_id = category_id
        # This parameter is required.
        self.category_type = category_type
        # This parameter is required.
        self.file_details = file_details
        # This parameter is required.
        self.oss_bucket_name = oss_bucket_name
        # This parameter is required.
        self.oss_region_id = oss_region_id
        self.tags = tags

    def validate(self):
        if self.file_details:
            for k in self.file_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.category_type is not None:
            result['CategoryType'] = self.category_type
        result['FileDetails'] = []
        if self.file_details is not None:
            for k in self.file_details:
                result['FileDetails'].append(k.to_map() if k else None)
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.oss_region_id is not None:
            result['OssRegionId'] = self.oss_region_id
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CategoryType') is not None:
            self.category_type = m.get('CategoryType')
        self.file_details = []
        if m.get('FileDetails') is not None:
            for k in m.get('FileDetails'):
                temp_model = AddFilesFromAuthorizedOssRequestFileDetails()
                self.file_details.append(temp_model.from_map(k))
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('OssRegionId') is not None:
            self.oss_region_id = m.get('OssRegionId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class AddFilesFromAuthorizedOssShrinkRequest(TeaModel):
    def __init__(
        self,
        category_id: str = None,
        category_type: str = None,
        file_details_shrink: str = None,
        oss_bucket_name: str = None,
        oss_region_id: str = None,
        tags_shrink: str = None,
    ):
        # This parameter is required.
        self.category_id = category_id
        # This parameter is required.
        self.category_type = category_type
        # This parameter is required.
        self.file_details_shrink = file_details_shrink
        # This parameter is required.
        self.oss_bucket_name = oss_bucket_name
        # This parameter is required.
        self.oss_region_id = oss_region_id
        self.tags_shrink = tags_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.category_type is not None:
            result['CategoryType'] = self.category_type
        if self.file_details_shrink is not None:
            result['FileDetails'] = self.file_details_shrink
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.oss_region_id is not None:
            result['OssRegionId'] = self.oss_region_id
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CategoryType') is not None:
            self.category_type = m.get('CategoryType')
        if m.get('FileDetails') is not None:
            self.file_details_shrink = m.get('FileDetails')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('OssRegionId') is not None:
            self.oss_region_id = m.get('OssRegionId')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        return self


class AddFilesFromAuthorizedOssResponseBodyDataAddFileResultList(TeaModel):
    def __init__(
        self,
        file_id: str = None,
        msg: str = None,
        oss_key: str = None,
        status: str = None,
    ):
        self.file_id = file_id
        self.msg = msg
        self.oss_key = oss_key
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class AddFilesFromAuthorizedOssResponseBodyData(TeaModel):
    def __init__(
        self,
        add_file_result_list: List[AddFilesFromAuthorizedOssResponseBodyDataAddFileResultList] = None,
    ):
        self.add_file_result_list = add_file_result_list

    def validate(self):
        if self.add_file_result_list:
            for k in self.add_file_result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AddFileResultList'] = []
        if self.add_file_result_list is not None:
            for k in self.add_file_result_list:
                result['AddFileResultList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.add_file_result_list = []
        if m.get('AddFileResultList') is not None:
            for k in m.get('AddFileResultList'):
                temp_model = AddFilesFromAuthorizedOssResponseBodyDataAddFileResultList()
                self.add_file_result_list.append(temp_model.from_map(k))
        return self


class AddFilesFromAuthorizedOssResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: AddFilesFromAuthorizedOssResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.status = status
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = AddFilesFromAuthorizedOssResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddFilesFromAuthorizedOssResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddFilesFromAuthorizedOssResponseBody = None,
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
            temp_model = AddFilesFromAuthorizedOssResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApplyFileUploadLeaseRequest(TeaModel):
    def __init__(
        self,
        category_type: str = None,
        file_name: str = None,
        md_5: str = None,
        size_in_bytes: str = None,
        use_internal_endpoint: bool = None,
    ):
        self.category_type = category_type
        # The name of the uploaded document, including the extension. Supported formats: pdf, doc, docx, md, txt, ppt, and pptx. The document name must be 4 to 128 characters in length.
        # 
        # This parameter is required.
        self.file_name = file_name
        # The MD5 value of the uploaded document. This parameter is verified by the server (not in the current version).
        # 
        # This parameter is required.
        self.md_5 = md_5
        # The size of the uploaded document, in bytes. This parameter is verified by the server (not in the current version). Valid values: 1 to 100000000.
        # 
        # This parameter is required.
        self.size_in_bytes = size_in_bytes
        self.use_internal_endpoint = use_internal_endpoint

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_type is not None:
            result['CategoryType'] = self.category_type
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.size_in_bytes is not None:
            result['SizeInBytes'] = self.size_in_bytes
        if self.use_internal_endpoint is not None:
            result['UseInternalEndpoint'] = self.use_internal_endpoint
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryType') is not None:
            self.category_type = m.get('CategoryType')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('SizeInBytes') is not None:
            self.size_in_bytes = m.get('SizeInBytes')
        if m.get('UseInternalEndpoint') is not None:
            self.use_internal_endpoint = m.get('UseInternalEndpoint')
        return self


class ApplyFileUploadLeaseResponseBodyDataParam(TeaModel):
    def __init__(
        self,
        headers: Any = None,
        method: str = None,
        url: str = None,
    ):
        # The key-value pair to be placed in the Header. Both the key and the value are strings.
        self.headers = headers
        # The HTTP call method. Valid values:
        # 
        # *   PUT
        # *   POST
        self.method = method
        # The upload URL of the document.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['Headers'] = self.headers
        if self.method is not None:
            result['Method'] = self.method
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Headers') is not None:
            self.headers = m.get('Headers')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ApplyFileUploadLeaseResponseBodyData(TeaModel):
    def __init__(
        self,
        file_upload_lease_id: str = None,
        param: ApplyFileUploadLeaseResponseBodyDataParam = None,
        type: str = None,
    ):
        # The unique ID of the lease.
        self.file_upload_lease_id = file_upload_lease_id
        # The HTTP request parameters used to upload the document.
        self.param = param
        # The upload method of the document. Valid values:
        # 
        # *   OSS.PreSignedURL
        # *   HTTP
        self.type = type

    def validate(self):
        if self.param:
            self.param.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_upload_lease_id is not None:
            result['FileUploadLeaseId'] = self.file_upload_lease_id
        if self.param is not None:
            result['Param'] = self.param.to_map()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileUploadLeaseId') is not None:
            self.file_upload_lease_id = m.get('FileUploadLeaseId')
        if m.get('Param') is not None:
            temp_model = ApplyFileUploadLeaseResponseBodyDataParam()
            self.param = temp_model.from_map(m['Param'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ApplyFileUploadLeaseResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ApplyFileUploadLeaseResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        # The status code.
        self.code = code
        # The returned data fields.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The HTTP status code.
        self.status = status
        # Indications whether the call is successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ApplyFileUploadLeaseResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ApplyFileUploadLeaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ApplyFileUploadLeaseResponseBody = None,
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
            temp_model = ApplyFileUploadLeaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAndPulishAgentRequestApplicationConfigHistoryConfig(TeaModel):
    def __init__(
        self,
        enable_adb_record: bool = None,
        enable_record: bool = None,
        instance_id: str = None,
        region: str = None,
        store_code: str = None,
    ):
        self.enable_adb_record = enable_adb_record
        self.enable_record = enable_record
        self.instance_id = instance_id
        self.region = region
        self.store_code = store_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_adb_record is not None:
            result['enableAdbRecord'] = self.enable_adb_record
        if self.enable_record is not None:
            result['enableRecord'] = self.enable_record
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.region is not None:
            result['region'] = self.region
        if self.store_code is not None:
            result['storeCode'] = self.store_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enableAdbRecord') is not None:
            self.enable_adb_record = m.get('enableAdbRecord')
        if m.get('enableRecord') is not None:
            self.enable_record = m.get('enableRecord')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('storeCode') is not None:
            self.store_code = m.get('storeCode')
        return self


class CreateAndPulishAgentRequestApplicationConfigLongTermMemory(TeaModel):
    def __init__(
        self,
        enable: bool = None,
    ):
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        return self


class CreateAndPulishAgentRequestApplicationConfigParameters(TeaModel):
    def __init__(
        self,
        dialog_round: int = None,
        max_tokens: int = None,
        temperature: float = None,
    ):
        self.dialog_round = dialog_round
        self.max_tokens = max_tokens
        self.temperature = temperature

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dialog_round is not None:
            result['dialogRound'] = self.dialog_round
        if self.max_tokens is not None:
            result['maxTokens'] = self.max_tokens
        if self.temperature is not None:
            result['temperature'] = self.temperature
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dialogRound') is not None:
            self.dialog_round = m.get('dialogRound')
        if m.get('maxTokens') is not None:
            self.max_tokens = m.get('maxTokens')
        if m.get('temperature') is not None:
            self.temperature = m.get('temperature')
        return self


class CreateAndPulishAgentRequestApplicationConfigRagConfig(TeaModel):
    def __init__(
        self,
        answer_scope: str = None,
        enable_citation: bool = None,
        enable_search: bool = None,
        enable_web_search: bool = None,
        fixed_reply_detail: str = None,
        knowledge_base_code_list: List[str] = None,
        prompt_strategy: str = None,
        rag_reject_type: str = None,
        reject_filter_prompt: str = None,
        reject_filter_type: str = None,
        retrieve_max_length: int = None,
        top_k: int = None,
    ):
        self.answer_scope = answer_scope
        self.enable_citation = enable_citation
        self.enable_search = enable_search
        self.enable_web_search = enable_web_search
        self.fixed_reply_detail = fixed_reply_detail
        self.knowledge_base_code_list = knowledge_base_code_list
        self.prompt_strategy = prompt_strategy
        self.rag_reject_type = rag_reject_type
        self.reject_filter_prompt = reject_filter_prompt
        self.reject_filter_type = reject_filter_type
        self.retrieve_max_length = retrieve_max_length
        self.top_k = top_k

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer_scope is not None:
            result['answerScope'] = self.answer_scope
        if self.enable_citation is not None:
            result['enableCitation'] = self.enable_citation
        if self.enable_search is not None:
            result['enableSearch'] = self.enable_search
        if self.enable_web_search is not None:
            result['enableWebSearch'] = self.enable_web_search
        if self.fixed_reply_detail is not None:
            result['fixedReplyDetail'] = self.fixed_reply_detail
        if self.knowledge_base_code_list is not None:
            result['knowledgeBaseCodeList'] = self.knowledge_base_code_list
        if self.prompt_strategy is not None:
            result['promptStrategy'] = self.prompt_strategy
        if self.rag_reject_type is not None:
            result['ragRejectType'] = self.rag_reject_type
        if self.reject_filter_prompt is not None:
            result['rejectFilterPrompt'] = self.reject_filter_prompt
        if self.reject_filter_type is not None:
            result['rejectFilterType'] = self.reject_filter_type
        if self.retrieve_max_length is not None:
            result['retrieveMaxLength'] = self.retrieve_max_length
        if self.top_k is not None:
            result['topK'] = self.top_k
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('answerScope') is not None:
            self.answer_scope = m.get('answerScope')
        if m.get('enableCitation') is not None:
            self.enable_citation = m.get('enableCitation')
        if m.get('enableSearch') is not None:
            self.enable_search = m.get('enableSearch')
        if m.get('enableWebSearch') is not None:
            self.enable_web_search = m.get('enableWebSearch')
        if m.get('fixedReplyDetail') is not None:
            self.fixed_reply_detail = m.get('fixedReplyDetail')
        if m.get('knowledgeBaseCodeList') is not None:
            self.knowledge_base_code_list = m.get('knowledgeBaseCodeList')
        if m.get('promptStrategy') is not None:
            self.prompt_strategy = m.get('promptStrategy')
        if m.get('ragRejectType') is not None:
            self.rag_reject_type = m.get('ragRejectType')
        if m.get('rejectFilterPrompt') is not None:
            self.reject_filter_prompt = m.get('rejectFilterPrompt')
        if m.get('rejectFilterType') is not None:
            self.reject_filter_type = m.get('rejectFilterType')
        if m.get('retrieveMaxLength') is not None:
            self.retrieve_max_length = m.get('retrieveMaxLength')
        if m.get('topK') is not None:
            self.top_k = m.get('topK')
        return self


class CreateAndPulishAgentRequestApplicationConfigSecurityConfig(TeaModel):
    def __init__(
        self,
        processing_strategy: str = None,
    ):
        self.processing_strategy = processing_strategy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.processing_strategy is not None:
            result['processingStrategy'] = self.processing_strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('processingStrategy') is not None:
            self.processing_strategy = m.get('processingStrategy')
        return self


class CreateAndPulishAgentRequestApplicationConfigTools(TeaModel):
    def __init__(
        self,
        type: str = None,
    ):
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


class CreateAndPulishAgentRequestApplicationConfigWorkFlows(TeaModel):
    def __init__(
        self,
        type: str = None,
    ):
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


class CreateAndPulishAgentRequestApplicationConfig(TeaModel):
    def __init__(
        self,
        history_config: CreateAndPulishAgentRequestApplicationConfigHistoryConfig = None,
        long_term_memory: CreateAndPulishAgentRequestApplicationConfigLongTermMemory = None,
        parameters: CreateAndPulishAgentRequestApplicationConfigParameters = None,
        rag_config: CreateAndPulishAgentRequestApplicationConfigRagConfig = None,
        security_config: CreateAndPulishAgentRequestApplicationConfigSecurityConfig = None,
        tools: List[CreateAndPulishAgentRequestApplicationConfigTools] = None,
        work_flows: List[CreateAndPulishAgentRequestApplicationConfigWorkFlows] = None,
    ):
        self.history_config = history_config
        self.long_term_memory = long_term_memory
        self.parameters = parameters
        self.rag_config = rag_config
        self.security_config = security_config
        self.tools = tools
        self.work_flows = work_flows

    def validate(self):
        if self.history_config:
            self.history_config.validate()
        if self.long_term_memory:
            self.long_term_memory.validate()
        if self.parameters:
            self.parameters.validate()
        if self.rag_config:
            self.rag_config.validate()
        if self.security_config:
            self.security_config.validate()
        if self.tools:
            for k in self.tools:
                if k:
                    k.validate()
        if self.work_flows:
            for k in self.work_flows:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.history_config is not None:
            result['historyConfig'] = self.history_config.to_map()
        if self.long_term_memory is not None:
            result['longTermMemory'] = self.long_term_memory.to_map()
        if self.parameters is not None:
            result['parameters'] = self.parameters.to_map()
        if self.rag_config is not None:
            result['ragConfig'] = self.rag_config.to_map()
        if self.security_config is not None:
            result['securityConfig'] = self.security_config.to_map()
        result['tools'] = []
        if self.tools is not None:
            for k in self.tools:
                result['tools'].append(k.to_map() if k else None)
        result['workFlows'] = []
        if self.work_flows is not None:
            for k in self.work_flows:
                result['workFlows'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('historyConfig') is not None:
            temp_model = CreateAndPulishAgentRequestApplicationConfigHistoryConfig()
            self.history_config = temp_model.from_map(m['historyConfig'])
        if m.get('longTermMemory') is not None:
            temp_model = CreateAndPulishAgentRequestApplicationConfigLongTermMemory()
            self.long_term_memory = temp_model.from_map(m['longTermMemory'])
        if m.get('parameters') is not None:
            temp_model = CreateAndPulishAgentRequestApplicationConfigParameters()
            self.parameters = temp_model.from_map(m['parameters'])
        if m.get('ragConfig') is not None:
            temp_model = CreateAndPulishAgentRequestApplicationConfigRagConfig()
            self.rag_config = temp_model.from_map(m['ragConfig'])
        if m.get('securityConfig') is not None:
            temp_model = CreateAndPulishAgentRequestApplicationConfigSecurityConfig()
            self.security_config = temp_model.from_map(m['securityConfig'])
        self.tools = []
        if m.get('tools') is not None:
            for k in m.get('tools'):
                temp_model = CreateAndPulishAgentRequestApplicationConfigTools()
                self.tools.append(temp_model.from_map(k))
        self.work_flows = []
        if m.get('workFlows') is not None:
            for k in m.get('workFlows'):
                temp_model = CreateAndPulishAgentRequestApplicationConfigWorkFlows()
                self.work_flows.append(temp_model.from_map(k))
        return self


class CreateAndPulishAgentRequestSampleLibrary(TeaModel):
    def __init__(
        self,
        enable_sample: bool = None,
        sample_library_id_list: List[str] = None,
        top_k: int = None,
    ):
        self.enable_sample = enable_sample
        self.sample_library_id_list = sample_library_id_list
        self.top_k = top_k

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_sample is not None:
            result['enableSample'] = self.enable_sample
        if self.sample_library_id_list is not None:
            result['sampleLibraryIdList'] = self.sample_library_id_list
        if self.top_k is not None:
            result['topK'] = self.top_k
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enableSample') is not None:
            self.enable_sample = m.get('enableSample')
        if m.get('sampleLibraryIdList') is not None:
            self.sample_library_id_list = m.get('sampleLibraryIdList')
        if m.get('topK') is not None:
            self.top_k = m.get('topK')
        return self


class CreateAndPulishAgentRequest(TeaModel):
    def __init__(
        self,
        application_config: CreateAndPulishAgentRequestApplicationConfig = None,
        instructions: str = None,
        model_id: str = None,
        name: str = None,
        sample_library: CreateAndPulishAgentRequestSampleLibrary = None,
    ):
        self.application_config = application_config
        self.instructions = instructions
        self.model_id = model_id
        self.name = name
        self.sample_library = sample_library

    def validate(self):
        if self.application_config:
            self.application_config.validate()
        if self.sample_library:
            self.sample_library.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_config is not None:
            result['applicationConfig'] = self.application_config.to_map()
        if self.instructions is not None:
            result['instructions'] = self.instructions
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.name is not None:
            result['name'] = self.name
        if self.sample_library is not None:
            result['sampleLibrary'] = self.sample_library.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applicationConfig') is not None:
            temp_model = CreateAndPulishAgentRequestApplicationConfig()
            self.application_config = temp_model.from_map(m['applicationConfig'])
        if m.get('instructions') is not None:
            self.instructions = m.get('instructions')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('sampleLibrary') is not None:
            temp_model = CreateAndPulishAgentRequestSampleLibrary()
            self.sample_library = temp_model.from_map(m['sampleLibrary'])
        return self


class CreateAndPulishAgentShrinkRequest(TeaModel):
    def __init__(
        self,
        application_config_shrink: str = None,
        instructions: str = None,
        model_id: str = None,
        name: str = None,
        sample_library_shrink: str = None,
    ):
        self.application_config_shrink = application_config_shrink
        self.instructions = instructions
        self.model_id = model_id
        self.name = name
        self.sample_library_shrink = sample_library_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_config_shrink is not None:
            result['applicationConfig'] = self.application_config_shrink
        if self.instructions is not None:
            result['instructions'] = self.instructions
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.name is not None:
            result['name'] = self.name
        if self.sample_library_shrink is not None:
            result['sampleLibrary'] = self.sample_library_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applicationConfig') is not None:
            self.application_config_shrink = m.get('applicationConfig')
        if m.get('instructions') is not None:
            self.instructions = m.get('instructions')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('sampleLibrary') is not None:
            self.sample_library_shrink = m.get('sampleLibrary')
        return self


class CreateAndPulishAgentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateAndPulishAgentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAndPulishAgentResponseBody = None,
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
            temp_model = CreateAndPulishAgentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIndexRequestColumns(TeaModel):
    def __init__(
        self,
        column: str = None,
        is_recall: bool = None,
        is_search: bool = None,
        name: str = None,
        type: str = None,
    ):
        self.column = column
        self.is_recall = is_recall
        self.is_search = is_search
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.column is not None:
            result['Column'] = self.column
        if self.is_recall is not None:
            result['IsRecall'] = self.is_recall
        if self.is_search is not None:
            result['IsSearch'] = self.is_search
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Column') is not None:
            self.column = m.get('Column')
        if m.get('IsRecall') is not None:
            self.is_recall = m.get('IsRecall')
        if m.get('IsSearch') is not None:
            self.is_search = m.get('IsSearch')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateIndexRequestDataSource(TeaModel):
    def __init__(
        self,
        credential_id: str = None,
        credential_key: str = None,
        database: str = None,
        endpoint: str = None,
        is_private_link: bool = None,
        region: str = None,
        sub_path: str = None,
        sub_type: str = None,
        table: str = None,
        type: str = None,
    ):
        # >  This parameter is not available. Do not specify this parameter.
        self.credential_id = credential_id
        # >  This parameter is not available. Do not specify this parameter.
        self.credential_key = credential_key
        # >  This parameter is not available. Do not specify this parameter.
        self.database = database
        # >  This parameter is not available. Do not specify this parameter.
        self.endpoint = endpoint
        # >  This parameter is not available. Do not specify this parameter.
        self.is_private_link = is_private_link
        # >  This parameter is not available. Do not specify this parameter.
        self.region = region
        # >  This parameter is not available. Do not specify this parameter.
        self.sub_path = sub_path
        # >  This parameter is not available. Do not specify this parameter.
        self.sub_type = sub_type
        # >  This parameter is not available. Do not specify this parameter.
        self.table = table
        # >  This parameter is not available. Do not specify this parameter.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_id is not None:
            result['CredentialId'] = self.credential_id
        if self.credential_key is not None:
            result['CredentialKey'] = self.credential_key
        if self.database is not None:
            result['Database'] = self.database
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.is_private_link is not None:
            result['IsPrivateLink'] = self.is_private_link
        if self.region is not None:
            result['Region'] = self.region
        if self.sub_path is not None:
            result['SubPath'] = self.sub_path
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.table is not None:
            result['Table'] = self.table
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialId') is not None:
            self.credential_id = m.get('CredentialId')
        if m.get('CredentialKey') is not None:
            self.credential_key = m.get('CredentialKey')
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('IsPrivateLink') is not None:
            self.is_private_link = m.get('IsPrivateLink')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('SubPath') is not None:
            self.sub_path = m.get('SubPath')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('Table') is not None:
            self.table = m.get('Table')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateIndexRequestMetaExtractColumns(TeaModel):
    def __init__(
        self,
        desc: str = None,
        enable_llm: bool = None,
        enable_search: bool = None,
        key: str = None,
        type: str = None,
        value: str = None,
    ):
        self.desc = desc
        self.enable_llm = enable_llm
        self.enable_search = enable_search
        self.key = key
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.enable_llm is not None:
            result['EnableLlm'] = self.enable_llm
        if self.enable_search is not None:
            result['EnableSearch'] = self.enable_search
        if self.key is not None:
            result['Key'] = self.key
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('EnableLlm') is not None:
            self.enable_llm = m.get('EnableLlm')
        if m.get('EnableSearch') is not None:
            self.enable_search = m.get('EnableSearch')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateIndexRequest(TeaModel):
    def __init__(
        self,
        category_ids: List[str] = None,
        chunk_size: int = None,
        columns: List[CreateIndexRequestColumns] = None,
        create_index_type: str = None,
        data_source: CreateIndexRequestDataSource = None,
        description: str = None,
        document_ids: List[str] = None,
        embedding_model_name: str = None,
        enable_rewrite: bool = None,
        name: str = None,
        overlap_size: int = None,
        rerank_min_score: float = None,
        rerank_model_name: str = None,
        separator: str = None,
        sink_instance_id: str = None,
        sink_region: str = None,
        sink_type: str = None,
        source_type: str = None,
        structure_type: str = None,
        table_ids: List[str] = None,
        chunk_mode: str = None,
        enable_headers: bool = None,
        meta_extract_columns: List[CreateIndexRequestMetaExtractColumns] = None,
    ):
        # The list of primary key IDs of the categories to be imported into the knowledge base.
        self.category_ids = category_ids
        # The estimated length of chunks. The maximum number of characters for a chunk. Texts exceeding this limit are splited. For more information, see [Create a knowledge base](https://www.alibabacloud.com/help/en/model-studio/user-guide/rag-knowledge-base). Valid values: [1-2048].
        # 
        # The default value is empty, which means using the intelligent splitting method.
        # 
        # >  If you specify the `ChunkSize` parameter, you must also specify the `OverlapSize` and `Separator` parameters. If you do not specify these three parameters, the system uses the intelligent splitting method by default.
        self.chunk_size = chunk_size
        self.columns = columns
        self.create_index_type = create_index_type
        # >  This parameter is not available. Do not specify this parameter.
        self.data_source = data_source
        # The description of the knowledge base. The description must be 0 to 1,000 characters in length. This parameter is empty by default.
        self.description = description
        # The list of primary key IDs of the documents to be imported into the knowledge base.
        self.document_ids = document_ids
        # The name of the embedding model. The embedding model converts the original input prompt and knowledge text into numerical vectors for similarity comparison. The default and only model available is DashScope text-embedding-v2. It supports multiple languages including Chinese and English and normalizes the vector results. For more information, see [Create a knowledge base](https://www.alibabacloud.com/help/en/model-studio/user-guide/rag-knowledge-base). Valid value:
        # 
        # *   text-embedding-v2
        # 
        # The default value is null, which means using the text-embedding-v2 model.
        self.embedding_model_name = embedding_model_name
        self.enable_rewrite = enable_rewrite
        # The name of the knowledge base. The name must be 1 to 20 characters in length and can contain characters classified as letter in Unicode, including English letters, Chinese characters, digits, among others. The name can also contain colons (:), underscores (_), periods (.), and hyphens (-).
        # 
        # This parameter is required.
        self.name = name
        # The overlap length. The number of overlapping characters between two consecutive chunks. For more information, see [Create a knowledge base](https://www.alibabacloud.com/help/en/model-studio/user-guide/rag-knowledge-base). Valid values: 0 to 1024.
        # 
        # The default value is empty, which means using the intelligent splitting method.
        self.overlap_size = overlap_size
        # Similarity Threshold. The lowest similarity score of chunks that can be returned. This parameter is used to filter text chunks returned by the rank model. For more information, see [Create a knowledge base](https://www.alibabacloud.com/help/en/model-studio/user-guide/rag-knowledge-base). Valid values: [0.01-1.00].
        # 
        # Default value: 0.20.
        self.rerank_min_score = rerank_min_score
        # The name of the rank model. The rank model is a scoring system outside the knowledge base. It calculates the similarity score of each text chunk in the input question and knowledge base and ranks them in descending order. Then, the model returns the top K chunks with the highest scores. For more information, see [Create a knowledge base](https://www.alibabacloud.com/help/en/model-studio/user-guide/rag-knowledge-base). Valid values:
        # 
        # *   gte-rerank-hybrid
        # *   gte-rerank
        # 
        # The default value is empty, which means using the official gte-rerank-hybrid model.
        # 
        # >  If you need only semantic ranking, we recommend that you use gte-rerank. If you need both semantic ranking and text matching features to ensure relevance, we recommend that you use gte-rerank-hybrid.
        self.rerank_model_name = rerank_model_name
        # The clause identifier. The document is split into chunks based on this identifier. For more information, see [Create a knowledge base](https://www.alibabacloud.com/help/en/model-studio/user-guide/rag-knowledge-base). You can specify multiple identifiers and do not need to add any other characters to separate them. For example: !,\\\\\\n. Valid values:
        # 
        # *   \\n: line break
        # *   ，: Chinese comma
        # *   ,: English comma
        # *   。 : Chinese full stop
        # *   .: English full stop
        # *   ！ : Chinese exclamation point
        # *   ! : English exclamation point
        # *   ；: Chinese semicolon
        # *   ;: English semicolon
        # *   ？: Chinese question mark
        # *   ?: English question mark
        # 
        # The default value is empty, which means using the intelligent splitting method.
        self.separator = separator
        # The ID of the vector storage instance. This parameter is available only when SinkType is set to ADB. You can view the ID on the [Instances](https://gpdbnext.console.aliyun.com/gpdb/list) page of AnalyticDB for PostgreSQL.
        self.sink_instance_id = sink_instance_id
        # The region of the vector storage instance. This parameter is available only when SinkType is set to ADB. You can call the [DescribeRegions](https://www.alibabacloud.com/help/en/analyticdb/analyticdb-for-postgresql/developer-reference/api-gpdb-2016-05-03-describeregions) operation to query the most recent region list.
        self.sink_region = sink_region
        # The vector storage type of the knowledge base. For more information, see [Create a knowledge base](https://www.alibabacloud.com/help/en/model-studio/user-guide/rag-knowledge-base). Valid values:
        # 
        # *   DEFAULT: The built-in vector database.
        # *   ADB: AnalyticDB for PostgreSQL database. If you need advanced features, such as managing, auditing, and monitoring, we recommend that you specify ADB.
        # 
        # >  If you have not used AnalyticDB for AnalyticDB in Model Studio before, go to the [Create Knowledge Base](https://bailian.console.aliyun.com/#/knowledge-base/create) page, select ADB-PG as Vector Storage Type, and follow the instructions to grant permissions. If you specify ADB, you must also specify the `SinkInstanceId` and `SinkRegion` parameters.
        # 
        # This parameter is required.
        self.sink_type = sink_type
        # The data type of [Data Management](https://bailian.console.aliyun.com/#/data-center). For more information, see [Create a knowledge base](https://www.alibabacloud.com/help/en/model-studio/user-guide/rag-knowledge-base). Valid values:
        # 
        # *   DATA_CENTER_CATEGORY: The category type. Import all documents from one or more categories in Data Center.
        # *   DATA_CENTER_FILE: The document type. Import one or more documents from Data Center.
        # 
        # >  If this parameter is set to DATA_CENTER_CATEGORY, you must specify the `CategoryIds` parameter. If this parameter is set to DATA_CENTER_FILE, you must specify the `DocumentIds` parameter.
        # 
        # >  If you want to create an empty knowledge base, you can use an empty category. Set this parameter to DATA_CENTER_CATEGORY. And specify the ID of an empty category for the `CategoryIds` parameter.
        self.source_type = source_type
        # The data type of the knowledge base. For more information, see [Create a knowledge base](https://www.alibabacloud.com/help/en/model-studio/user-guide/rag-knowledge-base). Valid value:
        # 
        # *   unstructured
        # 
        # >  After a knowledge base is created, its data type cannot be changed. You cannot create a structured knowledge base by calling an API operation. Use the console instead.
        # 
        # This parameter is required.
        self.structure_type = structure_type
        self.table_ids = table_ids
        self.chunk_mode = chunk_mode
        self.enable_headers = enable_headers
        self.meta_extract_columns = meta_extract_columns

    def validate(self):
        if self.columns:
            for k in self.columns:
                if k:
                    k.validate()
        if self.data_source:
            self.data_source.validate()
        if self.meta_extract_columns:
            for k in self.meta_extract_columns:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_ids is not None:
            result['CategoryIds'] = self.category_ids
        if self.chunk_size is not None:
            result['ChunkSize'] = self.chunk_size
        result['Columns'] = []
        if self.columns is not None:
            for k in self.columns:
                result['Columns'].append(k.to_map() if k else None)
        if self.create_index_type is not None:
            result['CreateIndexType'] = self.create_index_type
        if self.data_source is not None:
            result['DataSource'] = self.data_source.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.document_ids is not None:
            result['DocumentIds'] = self.document_ids
        if self.embedding_model_name is not None:
            result['EmbeddingModelName'] = self.embedding_model_name
        if self.enable_rewrite is not None:
            result['EnableRewrite'] = self.enable_rewrite
        if self.name is not None:
            result['Name'] = self.name
        if self.overlap_size is not None:
            result['OverlapSize'] = self.overlap_size
        if self.rerank_min_score is not None:
            result['RerankMinScore'] = self.rerank_min_score
        if self.rerank_model_name is not None:
            result['RerankModelName'] = self.rerank_model_name
        if self.separator is not None:
            result['Separator'] = self.separator
        if self.sink_instance_id is not None:
            result['SinkInstanceId'] = self.sink_instance_id
        if self.sink_region is not None:
            result['SinkRegion'] = self.sink_region
        if self.sink_type is not None:
            result['SinkType'] = self.sink_type
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.structure_type is not None:
            result['StructureType'] = self.structure_type
        if self.table_ids is not None:
            result['TableIds'] = self.table_ids
        if self.chunk_mode is not None:
            result['chunkMode'] = self.chunk_mode
        if self.enable_headers is not None:
            result['enableHeaders'] = self.enable_headers
        result['metaExtractColumns'] = []
        if self.meta_extract_columns is not None:
            for k in self.meta_extract_columns:
                result['metaExtractColumns'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryIds') is not None:
            self.category_ids = m.get('CategoryIds')
        if m.get('ChunkSize') is not None:
            self.chunk_size = m.get('ChunkSize')
        self.columns = []
        if m.get('Columns') is not None:
            for k in m.get('Columns'):
                temp_model = CreateIndexRequestColumns()
                self.columns.append(temp_model.from_map(k))
        if m.get('CreateIndexType') is not None:
            self.create_index_type = m.get('CreateIndexType')
        if m.get('DataSource') is not None:
            temp_model = CreateIndexRequestDataSource()
            self.data_source = temp_model.from_map(m['DataSource'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DocumentIds') is not None:
            self.document_ids = m.get('DocumentIds')
        if m.get('EmbeddingModelName') is not None:
            self.embedding_model_name = m.get('EmbeddingModelName')
        if m.get('EnableRewrite') is not None:
            self.enable_rewrite = m.get('EnableRewrite')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OverlapSize') is not None:
            self.overlap_size = m.get('OverlapSize')
        if m.get('RerankMinScore') is not None:
            self.rerank_min_score = m.get('RerankMinScore')
        if m.get('RerankModelName') is not None:
            self.rerank_model_name = m.get('RerankModelName')
        if m.get('Separator') is not None:
            self.separator = m.get('Separator')
        if m.get('SinkInstanceId') is not None:
            self.sink_instance_id = m.get('SinkInstanceId')
        if m.get('SinkRegion') is not None:
            self.sink_region = m.get('SinkRegion')
        if m.get('SinkType') is not None:
            self.sink_type = m.get('SinkType')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('StructureType') is not None:
            self.structure_type = m.get('StructureType')
        if m.get('TableIds') is not None:
            self.table_ids = m.get('TableIds')
        if m.get('chunkMode') is not None:
            self.chunk_mode = m.get('chunkMode')
        if m.get('enableHeaders') is not None:
            self.enable_headers = m.get('enableHeaders')
        self.meta_extract_columns = []
        if m.get('metaExtractColumns') is not None:
            for k in m.get('metaExtractColumns'):
                temp_model = CreateIndexRequestMetaExtractColumns()
                self.meta_extract_columns.append(temp_model.from_map(k))
        return self


class CreateIndexShrinkRequest(TeaModel):
    def __init__(
        self,
        category_ids_shrink: str = None,
        chunk_size: int = None,
        columns_shrink: str = None,
        create_index_type: str = None,
        data_source_shrink: str = None,
        description: str = None,
        document_ids_shrink: str = None,
        embedding_model_name: str = None,
        enable_rewrite: bool = None,
        name: str = None,
        overlap_size: int = None,
        rerank_min_score: float = None,
        rerank_model_name: str = None,
        separator: str = None,
        sink_instance_id: str = None,
        sink_region: str = None,
        sink_type: str = None,
        source_type: str = None,
        structure_type: str = None,
        table_ids_shrink: str = None,
        chunk_mode: str = None,
        enable_headers: bool = None,
        meta_extract_columns_shrink: str = None,
    ):
        # The list of primary key IDs of the categories to be imported into the knowledge base.
        self.category_ids_shrink = category_ids_shrink
        # The estimated length of chunks. The maximum number of characters for a chunk. Texts exceeding this limit are splited. For more information, see [Create a knowledge base](https://www.alibabacloud.com/help/en/model-studio/user-guide/rag-knowledge-base). Valid values: [1-2048].
        # 
        # The default value is empty, which means using the intelligent splitting method.
        # 
        # >  If you specify the `ChunkSize` parameter, you must also specify the `OverlapSize` and `Separator` parameters. If you do not specify these three parameters, the system uses the intelligent splitting method by default.
        self.chunk_size = chunk_size
        self.columns_shrink = columns_shrink
        self.create_index_type = create_index_type
        # >  This parameter is not available. Do not specify this parameter.
        self.data_source_shrink = data_source_shrink
        # The description of the knowledge base. The description must be 0 to 1,000 characters in length. This parameter is empty by default.
        self.description = description
        # The list of primary key IDs of the documents to be imported into the knowledge base.
        self.document_ids_shrink = document_ids_shrink
        # The name of the embedding model. The embedding model converts the original input prompt and knowledge text into numerical vectors for similarity comparison. The default and only model available is DashScope text-embedding-v2. It supports multiple languages including Chinese and English and normalizes the vector results. For more information, see [Create a knowledge base](https://www.alibabacloud.com/help/en/model-studio/user-guide/rag-knowledge-base). Valid value:
        # 
        # *   text-embedding-v2
        # 
        # The default value is null, which means using the text-embedding-v2 model.
        self.embedding_model_name = embedding_model_name
        self.enable_rewrite = enable_rewrite
        # The name of the knowledge base. The name must be 1 to 20 characters in length and can contain characters classified as letter in Unicode, including English letters, Chinese characters, digits, among others. The name can also contain colons (:), underscores (_), periods (.), and hyphens (-).
        # 
        # This parameter is required.
        self.name = name
        # The overlap length. The number of overlapping characters between two consecutive chunks. For more information, see [Create a knowledge base](https://www.alibabacloud.com/help/en/model-studio/user-guide/rag-knowledge-base). Valid values: 0 to 1024.
        # 
        # The default value is empty, which means using the intelligent splitting method.
        self.overlap_size = overlap_size
        # Similarity Threshold. The lowest similarity score of chunks that can be returned. This parameter is used to filter text chunks returned by the rank model. For more information, see [Create a knowledge base](https://www.alibabacloud.com/help/en/model-studio/user-guide/rag-knowledge-base). Valid values: [0.01-1.00].
        # 
        # Default value: 0.20.
        self.rerank_min_score = rerank_min_score
        # The name of the rank model. The rank model is a scoring system outside the knowledge base. It calculates the similarity score of each text chunk in the input question and knowledge base and ranks them in descending order. Then, the model returns the top K chunks with the highest scores. For more information, see [Create a knowledge base](https://www.alibabacloud.com/help/en/model-studio/user-guide/rag-knowledge-base). Valid values:
        # 
        # *   gte-rerank-hybrid
        # *   gte-rerank
        # 
        # The default value is empty, which means using the official gte-rerank-hybrid model.
        # 
        # >  If you need only semantic ranking, we recommend that you use gte-rerank. If you need both semantic ranking and text matching features to ensure relevance, we recommend that you use gte-rerank-hybrid.
        self.rerank_model_name = rerank_model_name
        # The clause identifier. The document is split into chunks based on this identifier. For more information, see [Create a knowledge base](https://www.alibabacloud.com/help/en/model-studio/user-guide/rag-knowledge-base). You can specify multiple identifiers and do not need to add any other characters to separate them. For example: !,\\\\\\n. Valid values:
        # 
        # *   \\n: line break
        # *   ，: Chinese comma
        # *   ,: English comma
        # *   。 : Chinese full stop
        # *   .: English full stop
        # *   ！ : Chinese exclamation point
        # *   ! : English exclamation point
        # *   ；: Chinese semicolon
        # *   ;: English semicolon
        # *   ？: Chinese question mark
        # *   ?: English question mark
        # 
        # The default value is empty, which means using the intelligent splitting method.
        self.separator = separator
        # The ID of the vector storage instance. This parameter is available only when SinkType is set to ADB. You can view the ID on the [Instances](https://gpdbnext.console.aliyun.com/gpdb/list) page of AnalyticDB for PostgreSQL.
        self.sink_instance_id = sink_instance_id
        # The region of the vector storage instance. This parameter is available only when SinkType is set to ADB. You can call the [DescribeRegions](https://www.alibabacloud.com/help/en/analyticdb/analyticdb-for-postgresql/developer-reference/api-gpdb-2016-05-03-describeregions) operation to query the most recent region list.
        self.sink_region = sink_region
        # The vector storage type of the knowledge base. For more information, see [Create a knowledge base](https://www.alibabacloud.com/help/en/model-studio/user-guide/rag-knowledge-base). Valid values:
        # 
        # *   DEFAULT: The built-in vector database.
        # *   ADB: AnalyticDB for PostgreSQL database. If you need advanced features, such as managing, auditing, and monitoring, we recommend that you specify ADB.
        # 
        # >  If you have not used AnalyticDB for AnalyticDB in Model Studio before, go to the [Create Knowledge Base](https://bailian.console.aliyun.com/#/knowledge-base/create) page, select ADB-PG as Vector Storage Type, and follow the instructions to grant permissions. If you specify ADB, you must also specify the `SinkInstanceId` and `SinkRegion` parameters.
        # 
        # This parameter is required.
        self.sink_type = sink_type
        # The data type of [Data Management](https://bailian.console.aliyun.com/#/data-center). For more information, see [Create a knowledge base](https://www.alibabacloud.com/help/en/model-studio/user-guide/rag-knowledge-base). Valid values:
        # 
        # *   DATA_CENTER_CATEGORY: The category type. Import all documents from one or more categories in Data Center.
        # *   DATA_CENTER_FILE: The document type. Import one or more documents from Data Center.
        # 
        # >  If this parameter is set to DATA_CENTER_CATEGORY, you must specify the `CategoryIds` parameter. If this parameter is set to DATA_CENTER_FILE, you must specify the `DocumentIds` parameter.
        # 
        # >  If you want to create an empty knowledge base, you can use an empty category. Set this parameter to DATA_CENTER_CATEGORY. And specify the ID of an empty category for the `CategoryIds` parameter.
        self.source_type = source_type
        # The data type of the knowledge base. For more information, see [Create a knowledge base](https://www.alibabacloud.com/help/en/model-studio/user-guide/rag-knowledge-base). Valid value:
        # 
        # *   unstructured
        # 
        # >  After a knowledge base is created, its data type cannot be changed. You cannot create a structured knowledge base by calling an API operation. Use the console instead.
        # 
        # This parameter is required.
        self.structure_type = structure_type
        self.table_ids_shrink = table_ids_shrink
        self.chunk_mode = chunk_mode
        self.enable_headers = enable_headers
        self.meta_extract_columns_shrink = meta_extract_columns_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_ids_shrink is not None:
            result['CategoryIds'] = self.category_ids_shrink
        if self.chunk_size is not None:
            result['ChunkSize'] = self.chunk_size
        if self.columns_shrink is not None:
            result['Columns'] = self.columns_shrink
        if self.create_index_type is not None:
            result['CreateIndexType'] = self.create_index_type
        if self.data_source_shrink is not None:
            result['DataSource'] = self.data_source_shrink
        if self.description is not None:
            result['Description'] = self.description
        if self.document_ids_shrink is not None:
            result['DocumentIds'] = self.document_ids_shrink
        if self.embedding_model_name is not None:
            result['EmbeddingModelName'] = self.embedding_model_name
        if self.enable_rewrite is not None:
            result['EnableRewrite'] = self.enable_rewrite
        if self.name is not None:
            result['Name'] = self.name
        if self.overlap_size is not None:
            result['OverlapSize'] = self.overlap_size
        if self.rerank_min_score is not None:
            result['RerankMinScore'] = self.rerank_min_score
        if self.rerank_model_name is not None:
            result['RerankModelName'] = self.rerank_model_name
        if self.separator is not None:
            result['Separator'] = self.separator
        if self.sink_instance_id is not None:
            result['SinkInstanceId'] = self.sink_instance_id
        if self.sink_region is not None:
            result['SinkRegion'] = self.sink_region
        if self.sink_type is not None:
            result['SinkType'] = self.sink_type
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.structure_type is not None:
            result['StructureType'] = self.structure_type
        if self.table_ids_shrink is not None:
            result['TableIds'] = self.table_ids_shrink
        if self.chunk_mode is not None:
            result['chunkMode'] = self.chunk_mode
        if self.enable_headers is not None:
            result['enableHeaders'] = self.enable_headers
        if self.meta_extract_columns_shrink is not None:
            result['metaExtractColumns'] = self.meta_extract_columns_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryIds') is not None:
            self.category_ids_shrink = m.get('CategoryIds')
        if m.get('ChunkSize') is not None:
            self.chunk_size = m.get('ChunkSize')
        if m.get('Columns') is not None:
            self.columns_shrink = m.get('Columns')
        if m.get('CreateIndexType') is not None:
            self.create_index_type = m.get('CreateIndexType')
        if m.get('DataSource') is not None:
            self.data_source_shrink = m.get('DataSource')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DocumentIds') is not None:
            self.document_ids_shrink = m.get('DocumentIds')
        if m.get('EmbeddingModelName') is not None:
            self.embedding_model_name = m.get('EmbeddingModelName')
        if m.get('EnableRewrite') is not None:
            self.enable_rewrite = m.get('EnableRewrite')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OverlapSize') is not None:
            self.overlap_size = m.get('OverlapSize')
        if m.get('RerankMinScore') is not None:
            self.rerank_min_score = m.get('RerankMinScore')
        if m.get('RerankModelName') is not None:
            self.rerank_model_name = m.get('RerankModelName')
        if m.get('Separator') is not None:
            self.separator = m.get('Separator')
        if m.get('SinkInstanceId') is not None:
            self.sink_instance_id = m.get('SinkInstanceId')
        if m.get('SinkRegion') is not None:
            self.sink_region = m.get('SinkRegion')
        if m.get('SinkType') is not None:
            self.sink_type = m.get('SinkType')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('StructureType') is not None:
            self.structure_type = m.get('StructureType')
        if m.get('TableIds') is not None:
            self.table_ids_shrink = m.get('TableIds')
        if m.get('chunkMode') is not None:
            self.chunk_mode = m.get('chunkMode')
        if m.get('enableHeaders') is not None:
            self.enable_headers = m.get('enableHeaders')
        if m.get('metaExtractColumns') is not None:
            self.meta_extract_columns_shrink = m.get('metaExtractColumns')
        return self


class CreateIndexResponseBodyData(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        # The primary key ID of the knowledge base, `IndexId`.
        # 
        # >  We recommend that you store this ID. It is required for all subsequent API operations related to this knowledge base.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CreateIndexResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateIndexResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        # HTTP status code
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The status code.
        self.status = status
        # Indications whether the API call is successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateIndexResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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


class CreateMemoryRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
    ):
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        return self


class CreateMemoryResponseBody(TeaModel):
    def __init__(
        self,
        memory_id: str = None,
        request_id: str = None,
    ):
        self.memory_id = memory_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.memory_id is not None:
            result['memoryId'] = self.memory_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('memoryId') is not None:
            self.memory_id = m.get('memoryId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateMemoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateMemoryResponseBody = None,
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
            temp_model = CreateMemoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMemoryNodeRequest(TeaModel):
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


class CreateMemoryNodeResponseBody(TeaModel):
    def __init__(
        self,
        memory_node_id: str = None,
        request_id: str = None,
    ):
        self.memory_node_id = memory_node_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.memory_node_id is not None:
            result['memoryNodeId'] = self.memory_node_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('memoryNodeId') is not None:
            self.memory_node_id = m.get('memoryNodeId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateMemoryNodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateMemoryNodeResponseBody = None,
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
            temp_model = CreateMemoryNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePromptTemplateRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        name: str = None,
    ):
        # This parameter is required.
        self.content = content
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class CreatePromptTemplateResponseBody(TeaModel):
    def __init__(
        self,
        prompt_template_id: str = None,
        request_id: str = None,
    ):
        self.prompt_template_id = prompt_template_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.prompt_template_id is not None:
            result['promptTemplateId'] = self.prompt_template_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('promptTemplateId') is not None:
            self.prompt_template_id = m.get('promptTemplateId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreatePromptTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatePromptTemplateResponseBody = None,
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
            temp_model = CreatePromptTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAgentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeleteAgentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAgentResponseBody = None,
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
            temp_model = DeleteAgentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCategoryResponseBodyData(TeaModel):
    def __init__(
        self,
        category_id: str = None,
    ):
        self.category_id = category_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        return self


class DeleteCategoryResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DeleteCategoryResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        self.code = code
        # data
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.status = status
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DeleteCategoryResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteCategoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCategoryResponseBody = None,
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
            temp_model = DeleteCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFileResponseBodyData(TeaModel):
    def __init__(
        self,
        file_id: str = None,
    ):
        self.file_id = file_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['FileId'] = self.file_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        return self


class DeleteFileResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DeleteFileResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.status = status
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DeleteFileResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteFileResponseBody = None,
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
            temp_model = DeleteFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIndexRequest(TeaModel):
    def __init__(
        self,
        index_id: str = None,
    ):
        # The primary key ID of the knowledge base, which is the `Data.Id` parameter returned by the [CreateIndex](https://www.alibabacloud.com/help/en/model-studio/developer-reference/api-bailian-2023-12-29-createindex) operation.
        # 
        # This parameter is required.
        self.index_id = index_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index_id is not None:
            result['IndexId'] = self.index_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')
        return self


class DeleteIndexResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        # HTTP status code
        self.code = code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The status code.
        self.status = status
        # Indications whether the API call is successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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


class DeleteIndexDocumentRequest(TeaModel):
    def __init__(
        self,
        document_ids: List[str] = None,
        index_id: str = None,
    ):
        # The list of the primary key IDs of the documents.
        # 
        # This parameter is required.
        self.document_ids = document_ids
        # The primary key ID of the knowledge base, which is the `Data.Id` parameter returned by the [CreateIndex](https://www.alibabacloud.com/help/en/model-studio/developer-reference/api-bailian-2023-12-29-createindex) operation.
        # 
        # This parameter is required.
        self.index_id = index_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.document_ids is not None:
            result['DocumentIds'] = self.document_ids
        if self.index_id is not None:
            result['IndexId'] = self.index_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocumentIds') is not None:
            self.document_ids = m.get('DocumentIds')
        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')
        return self


class DeleteIndexDocumentShrinkRequest(TeaModel):
    def __init__(
        self,
        document_ids_shrink: str = None,
        index_id: str = None,
    ):
        # The list of the primary key IDs of the documents.
        # 
        # This parameter is required.
        self.document_ids_shrink = document_ids_shrink
        # The primary key ID of the knowledge base, which is the `Data.Id` parameter returned by the [CreateIndex](https://www.alibabacloud.com/help/en/model-studio/developer-reference/api-bailian-2023-12-29-createindex) operation.
        # 
        # This parameter is required.
        self.index_id = index_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.document_ids_shrink is not None:
            result['DocumentIds'] = self.document_ids_shrink
        if self.index_id is not None:
            result['IndexId'] = self.index_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocumentIds') is not None:
            self.document_ids_shrink = m.get('DocumentIds')
        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')
        return self


class DeleteIndexDocumentResponseBodyData(TeaModel):
    def __init__(
        self,
        deleted_document: List[str] = None,
    ):
        # The list of primary key IDs of documents that are deleted.
        self.deleted_document = deleted_document

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deleted_document is not None:
            result['DeletedDocument'] = self.deleted_document
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeletedDocument') is not None:
            self.deleted_document = m.get('DeletedDocument')
        return self


class DeleteIndexDocumentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DeleteIndexDocumentResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        # HTTP status code
        self.code = code
        # The parameters returned by the operation.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The status code.
        self.status = status
        # Indications whether the API call is successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DeleteIndexDocumentResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteIndexDocumentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteIndexDocumentResponseBody = None,
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
            temp_model = DeleteIndexDocumentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMemoryResponseBody(TeaModel):
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


class DeleteMemoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteMemoryResponseBody = None,
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
            temp_model = DeleteMemoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMemoryNodeResponseBody(TeaModel):
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


class DeleteMemoryNodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteMemoryNodeResponseBody = None,
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
            temp_model = DeleteMemoryNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePromptTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class DeletePromptTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeletePromptTemplateResponseBody = None,
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
            temp_model = DeletePromptTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFileResponseBodyData(TeaModel):
    def __init__(
        self,
        category_id: str = None,
        create_time: str = None,
        file_id: str = None,
        file_name: str = None,
        file_type: str = None,
        parser: str = None,
        size_in_bytes: int = None,
        status: str = None,
        tags: List[str] = None,
    ):
        # The ID of the category to which the document belongs.
        self.category_id = category_id
        # The timestamp when the document was uploaded to Model Studio. Format: yyyy-MM-dd HH:mm:ss. Time zone: UTC + 8.
        self.create_time = create_time
        # The primary key ID of the document.
        self.file_id = file_id
        # The name of the document.
        self.file_name = file_name
        # The file type of the document. The value is an extension. Valid values: pdf, docx, doc, txt, md, pptx, and ppt.
        self.file_type = file_type
        # The parser that is used to parse the document. Valid value:
        # 
        # *   DASHSCOPE_DOCMIND: The default document parser.
        self.parser = parser
        # The size of the document. Unit: bytes.
        self.size_in_bytes = size_in_bytes
        # The status of the document. Valid values:
        # 
        # *   INIT: pending parsing.
        # *   PARSING
        # *   PARSE_SUCCESS
        # *   PARSE_FAILED
        self.status = status
        # The tags that are associated with the document. A document can be associated with multiple tags.
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.parser is not None:
            result['Parser'] = self.parser
        if self.size_in_bytes is not None:
            result['SizeInBytes'] = self.size_in_bytes
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('Parser') is not None:
            self.parser = m.get('Parser')
        if m.get('SizeInBytes') is not None:
            self.size_in_bytes = m.get('SizeInBytes')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class DescribeFileResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeFileResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        # The status code.
        self.code = code
        # The returned data fields.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The HTTP status code.
        self.status = status
        # Indications whether the API call is successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeFileResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFileResponseBody = None,
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
            temp_model = DescribeFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetIndexJobStatusRequest(TeaModel):
    def __init__(
        self,
        index_id: str = None,
        job_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The primary key ID of the knowledge base, which is the `Data.Id` parameter returned by the [CreateIndex](https://www.alibabacloud.com/help/en/model-studio/developer-reference/api-bailian-2023-12-29-createindex) operation.
        # 
        # This parameter is required.
        self.index_id = index_id
        # The knowledge base job ID, which is the `Data.Id` parameter returned by the [SubmitIndexJob](https://www.alibabacloud.com/help/en/model-studio/developer-reference/api-bailian-2023-12-29-submitindexjob) or [SubmitIndexAddDocumentsJob](https://www.alibabacloud.com/help/en/model-studio/developer-reference/api-bailian-2023-12-29-submitindexadddocumentsjob) operations.
        # 
        # This parameter is required.
        self.job_id = job_id
        # Both the [SubmitIndexJob](https://www.alibabacloud.com/help/en/model-studio/developer-reference/api-bailian-2023-12-29-submitindexjob) and [SubmitIndexAddDocumentsJob](https://www.alibabacloud.com/help/en/model-studio/developer-reference/api-bailian-2023-12-29-submitindexadddocumentsjob) operations support batch import of documents. This operation returns both the overall `Status` of the job and the `Document.Status` of each document. If there are a large number of documents, you can use the `PageNumber` parameter to perform a paged query. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of document import jobs that are displayed on each page. No maximum value. Default value: 10.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index_id is not None:
            result['IndexId'] = self.index_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class GetIndexJobStatusResponseBodyDataDocuments(TeaModel):
    def __init__(
        self,
        code: str = None,
        doc_id: str = None,
        doc_name: str = None,
        gmt_modified: int = None,
        message: str = None,
        status: str = None,
    ):
        # HTTP status code
        self.code = code
        # The primary key ID of the document.
        self.doc_id = doc_id
        # The name of the document.
        self.doc_name = doc_name
        self.gmt_modified = gmt_modified
        # The error message.
        self.message = message
        # The import status of the document. Valid values:
        # 
        # *   INSERT_ERROR
        # *   RUNNING
        # *   DELETED
        # *   FINISH
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.doc_id is not None:
            result['DocId'] = self.doc_id
        if self.doc_name is not None:
            result['DocName'] = self.doc_name
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.message is not None:
            result['Message'] = self.message
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DocId') is not None:
            self.doc_id = m.get('DocId')
        if m.get('DocName') is not None:
            self.doc_name = m.get('DocName')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetIndexJobStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        documents: List[GetIndexJobStatusResponseBodyDataDocuments] = None,
        job_id: str = None,
        status: str = None,
    ):
        # The list of imported documents.
        self.documents = documents
        # The ID of the job.
        self.job_id = job_id
        # The status of the knowledge base job. Valid values:
        # 
        # *   COMPLETED
        # *   FAILED
        # *   RUNNING
        # *   PENDING
        self.status = status

    def validate(self):
        if self.documents:
            for k in self.documents:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Documents'] = []
        if self.documents is not None:
            for k in self.documents:
                result['Documents'].append(k.to_map() if k else None)
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.documents = []
        if m.get('Documents') is not None:
            for k in m.get('Documents'):
                temp_model = GetIndexJobStatusResponseBodyDataDocuments()
                self.documents.append(temp_model.from_map(k))
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetIndexJobStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetIndexJobStatusResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        # HTTP status code
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The HTTP status code returned.
        self.status = status
        # Indications whether the API call is successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetIndexJobStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetIndexJobStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetIndexJobStatusResponseBody = None,
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
            temp_model = GetIndexJobStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMemoryResponseBody(TeaModel):
    def __init__(
        self,
        description: str = None,
        memory_id: str = None,
        request_id: str = None,
        workspace_id: str = None,
    ):
        self.description = description
        self.memory_id = memory_id
        self.request_id = request_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.memory_id is not None:
            result['memoryId'] = self.memory_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('memoryId') is not None:
            self.memory_id = m.get('memoryId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class GetMemoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMemoryResponseBody = None,
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
            temp_model = GetMemoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMemoryNodeResponseBody(TeaModel):
    def __init__(
        self,
        content: str = None,
        memory_id: str = None,
        memory_node_id: str = None,
        request_id: str = None,
        workspace_id: str = None,
    ):
        self.content = content
        self.memory_id = memory_id
        self.memory_node_id = memory_node_id
        self.request_id = request_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.memory_id is not None:
            result['memoryId'] = self.memory_id
        if self.memory_node_id is not None:
            result['memoryNodeId'] = self.memory_node_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('memoryId') is not None:
            self.memory_id = m.get('memoryId')
        if m.get('memoryNodeId') is not None:
            self.memory_node_id = m.get('memoryNodeId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class GetMemoryNodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMemoryNodeResponseBody = None,
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
            temp_model = GetMemoryNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPromptTemplateResponseBody(TeaModel):
    def __init__(
        self,
        content: str = None,
        name: str = None,
        prompt_template_id: str = None,
        request_id: str = None,
        variables: List[str] = None,
        workspace_id: str = None,
    ):
        # The template content.
        self.content = content
        # The template name.
        self.name = name
        # The template ID.
        self.prompt_template_id = prompt_template_id
        # The request ID.
        self.request_id = request_id
        # The variables of the template.
        self.variables = variables
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.name is not None:
            result['name'] = self.name
        if self.prompt_template_id is not None:
            result['promptTemplateId'] = self.prompt_template_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.variables is not None:
            result['variables'] = self.variables
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('promptTemplateId') is not None:
            self.prompt_template_id = m.get('promptTemplateId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('variables') is not None:
            self.variables = m.get('variables')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class GetPromptTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPromptTemplateResponseBody = None,
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
            temp_model = GetPromptTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPublishedAgentResponseBodyDataApplicationConfigHistoryConfig(TeaModel):
    def __init__(
        self,
        enable_adb_record: bool = None,
        enable_record: bool = None,
        instance_id: str = None,
        region: str = None,
        store_code: str = None,
    ):
        self.enable_adb_record = enable_adb_record
        self.enable_record = enable_record
        self.instance_id = instance_id
        self.region = region
        self.store_code = store_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_adb_record is not None:
            result['enableAdbRecord'] = self.enable_adb_record
        if self.enable_record is not None:
            result['enableRecord'] = self.enable_record
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.region is not None:
            result['region'] = self.region
        if self.store_code is not None:
            result['storeCode'] = self.store_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enableAdbRecord') is not None:
            self.enable_adb_record = m.get('enableAdbRecord')
        if m.get('enableRecord') is not None:
            self.enable_record = m.get('enableRecord')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('storeCode') is not None:
            self.store_code = m.get('storeCode')
        return self


class GetPublishedAgentResponseBodyDataApplicationConfigLongTermMemory(TeaModel):
    def __init__(
        self,
        enable: bool = None,
    ):
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        return self


class GetPublishedAgentResponseBodyDataApplicationConfigParameters(TeaModel):
    def __init__(
        self,
        dialog_round: int = None,
        max_tokens: int = None,
        temperature: float = None,
    ):
        self.dialog_round = dialog_round
        self.max_tokens = max_tokens
        self.temperature = temperature

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dialog_round is not None:
            result['dialogRound'] = self.dialog_round
        if self.max_tokens is not None:
            result['maxTokens'] = self.max_tokens
        if self.temperature is not None:
            result['temperature'] = self.temperature
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dialogRound') is not None:
            self.dialog_round = m.get('dialogRound')
        if m.get('maxTokens') is not None:
            self.max_tokens = m.get('maxTokens')
        if m.get('temperature') is not None:
            self.temperature = m.get('temperature')
        return self


class GetPublishedAgentResponseBodyDataApplicationConfigRagConfig(TeaModel):
    def __init__(
        self,
        enable_citation: bool = None,
        enable_search: bool = None,
        knowledge_base_code_list: List[str] = None,
        top_k: int = None,
    ):
        self.enable_citation = enable_citation
        self.enable_search = enable_search
        self.knowledge_base_code_list = knowledge_base_code_list
        self.top_k = top_k

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_citation is not None:
            result['enableCitation'] = self.enable_citation
        if self.enable_search is not None:
            result['enableSearch'] = self.enable_search
        if self.knowledge_base_code_list is not None:
            result['knowledgeBaseCodeList'] = self.knowledge_base_code_list
        if self.top_k is not None:
            result['topK'] = self.top_k
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enableCitation') is not None:
            self.enable_citation = m.get('enableCitation')
        if m.get('enableSearch') is not None:
            self.enable_search = m.get('enableSearch')
        if m.get('knowledgeBaseCodeList') is not None:
            self.knowledge_base_code_list = m.get('knowledgeBaseCodeList')
        if m.get('topK') is not None:
            self.top_k = m.get('topK')
        return self


class GetPublishedAgentResponseBodyDataApplicationConfigSecurity(TeaModel):
    def __init__(
        self,
        processing_strategy: str = None,
    ):
        self.processing_strategy = processing_strategy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.processing_strategy is not None:
            result['processingStrategy'] = self.processing_strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('processingStrategy') is not None:
            self.processing_strategy = m.get('processingStrategy')
        return self


class GetPublishedAgentResponseBodyDataApplicationConfigTools(TeaModel):
    def __init__(
        self,
        type: str = None,
    ):
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


class GetPublishedAgentResponseBodyDataApplicationConfigWorkFlows(TeaModel):
    def __init__(
        self,
        type: str = None,
    ):
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


class GetPublishedAgentResponseBodyDataApplicationConfig(TeaModel):
    def __init__(
        self,
        history_config: GetPublishedAgentResponseBodyDataApplicationConfigHistoryConfig = None,
        long_term_memory: GetPublishedAgentResponseBodyDataApplicationConfigLongTermMemory = None,
        parameters: GetPublishedAgentResponseBodyDataApplicationConfigParameters = None,
        rag_config: GetPublishedAgentResponseBodyDataApplicationConfigRagConfig = None,
        security: GetPublishedAgentResponseBodyDataApplicationConfigSecurity = None,
        tools: List[GetPublishedAgentResponseBodyDataApplicationConfigTools] = None,
        work_flows: List[GetPublishedAgentResponseBodyDataApplicationConfigWorkFlows] = None,
    ):
        self.history_config = history_config
        self.long_term_memory = long_term_memory
        self.parameters = parameters
        self.rag_config = rag_config
        self.security = security
        self.tools = tools
        self.work_flows = work_flows

    def validate(self):
        if self.history_config:
            self.history_config.validate()
        if self.long_term_memory:
            self.long_term_memory.validate()
        if self.parameters:
            self.parameters.validate()
        if self.rag_config:
            self.rag_config.validate()
        if self.security:
            self.security.validate()
        if self.tools:
            for k in self.tools:
                if k:
                    k.validate()
        if self.work_flows:
            for k in self.work_flows:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.history_config is not None:
            result['historyConfig'] = self.history_config.to_map()
        if self.long_term_memory is not None:
            result['longTermMemory'] = self.long_term_memory.to_map()
        if self.parameters is not None:
            result['parameters'] = self.parameters.to_map()
        if self.rag_config is not None:
            result['ragConfig'] = self.rag_config.to_map()
        if self.security is not None:
            result['security'] = self.security.to_map()
        result['tools'] = []
        if self.tools is not None:
            for k in self.tools:
                result['tools'].append(k.to_map() if k else None)
        result['workFlows'] = []
        if self.work_flows is not None:
            for k in self.work_flows:
                result['workFlows'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('historyConfig') is not None:
            temp_model = GetPublishedAgentResponseBodyDataApplicationConfigHistoryConfig()
            self.history_config = temp_model.from_map(m['historyConfig'])
        if m.get('longTermMemory') is not None:
            temp_model = GetPublishedAgentResponseBodyDataApplicationConfigLongTermMemory()
            self.long_term_memory = temp_model.from_map(m['longTermMemory'])
        if m.get('parameters') is not None:
            temp_model = GetPublishedAgentResponseBodyDataApplicationConfigParameters()
            self.parameters = temp_model.from_map(m['parameters'])
        if m.get('ragConfig') is not None:
            temp_model = GetPublishedAgentResponseBodyDataApplicationConfigRagConfig()
            self.rag_config = temp_model.from_map(m['ragConfig'])
        if m.get('security') is not None:
            temp_model = GetPublishedAgentResponseBodyDataApplicationConfigSecurity()
            self.security = temp_model.from_map(m['security'])
        self.tools = []
        if m.get('tools') is not None:
            for k in m.get('tools'):
                temp_model = GetPublishedAgentResponseBodyDataApplicationConfigTools()
                self.tools.append(temp_model.from_map(k))
        self.work_flows = []
        if m.get('workFlows') is not None:
            for k in m.get('workFlows'):
                temp_model = GetPublishedAgentResponseBodyDataApplicationConfigWorkFlows()
                self.work_flows.append(temp_model.from_map(k))
        return self


class GetPublishedAgentResponseBodyData(TeaModel):
    def __init__(
        self,
        application_config: GetPublishedAgentResponseBodyDataApplicationConfig = None,
        code: str = None,
        instructions: str = None,
        model_id: str = None,
        name: str = None,
    ):
        self.application_config = application_config
        self.code = code
        self.instructions = instructions
        self.model_id = model_id
        self.name = name

    def validate(self):
        if self.application_config:
            self.application_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_config is not None:
            result['applicationConfig'] = self.application_config.to_map()
        if self.code is not None:
            result['code'] = self.code
        if self.instructions is not None:
            result['instructions'] = self.instructions
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applicationConfig') is not None:
            temp_model = GetPublishedAgentResponseBodyDataApplicationConfig()
            self.application_config = temp_model.from_map(m['applicationConfig'])
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('instructions') is not None:
            self.instructions = m.get('instructions')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class GetPublishedAgentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetPublishedAgentResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetPublishedAgentResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetPublishedAgentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPublishedAgentResponseBody = None,
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
            temp_model = GetPublishedAgentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCategoryRequest(TeaModel):
    def __init__(
        self,
        category_name: str = None,
        category_type: str = None,
        max_results: int = None,
        next_token: str = None,
        parent_category_id: str = None,
    ):
        self.category_name = category_name
        # This parameter is required.
        self.category_type = category_type
        self.max_results = max_results
        self.next_token = next_token
        self.parent_category_id = parent_category_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.category_type is not None:
            result['CategoryType'] = self.category_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.parent_category_id is not None:
            result['ParentCategoryId'] = self.parent_category_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('CategoryType') is not None:
            self.category_type = m.get('CategoryType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ParentCategoryId') is not None:
            self.parent_category_id = m.get('ParentCategoryId')
        return self


class ListCategoryResponseBodyDataCategoryList(TeaModel):
    def __init__(
        self,
        category_id: str = None,
        category_name: str = None,
        category_type: str = None,
        is_default: bool = None,
        parent_category_id: str = None,
    ):
        self.category_id = category_id
        self.category_name = category_name
        self.category_type = category_type
        self.is_default = is_default
        self.parent_category_id = parent_category_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.category_type is not None:
            result['CategoryType'] = self.category_type
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.parent_category_id is not None:
            result['ParentCategoryId'] = self.parent_category_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('CategoryType') is not None:
            self.category_type = m.get('CategoryType')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('ParentCategoryId') is not None:
            self.parent_category_id = m.get('ParentCategoryId')
        return self


class ListCategoryResponseBodyData(TeaModel):
    def __init__(
        self,
        category_list: List[ListCategoryResponseBodyDataCategoryList] = None,
        has_next: bool = None,
        max_results: int = None,
        next_token: str = None,
        total_count: int = None,
    ):
        self.category_list = category_list
        self.has_next = has_next
        self.max_results = max_results
        self.next_token = next_token
        self.total_count = total_count

    def validate(self):
        if self.category_list:
            for k in self.category_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CategoryList'] = []
        if self.category_list is not None:
            for k in self.category_list:
                result['CategoryList'].append(k.to_map() if k else None)
        if self.has_next is not None:
            result['HasNext'] = self.has_next
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.category_list = []
        if m.get('CategoryList') is not None:
            for k in m.get('CategoryList'):
                temp_model = ListCategoryResponseBodyDataCategoryList()
                self.category_list.append(temp_model.from_map(k))
        if m.get('HasNext') is not None:
            self.has_next = m.get('HasNext')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListCategoryResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListCategoryResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.status = status
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListCategoryResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListCategoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCategoryResponseBody = None,
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
            temp_model = ListCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListChunksRequest(TeaModel):
    def __init__(
        self,
        fields: List[str] = None,
        file_id: str = None,
        filed: str = None,
        index_id: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        # An array of field names. This parameter is used to filter non-private fields (prefixed with_underscores) in the Metadata parameter returned by this operation. By default, this parameter is left empty, which means all non-private fields in the Metadata parameter are returned. If you only want specified non-private fields, such as title, set this parameter to title.
        self.fields = fields
        self.file_id = file_id
        # The primary key ID of the document. This parameter is not required for structured knowledge base, but is required for unstructured knowledge base. To view the ID, you can click the ID icon next to the file name on the [Data Management](https://bailian.console.aliyun.com/#/data-center) page. You can filter returned chunks by the document ID. This parameter is left empty by default.
        self.filed = filed
        # The primary key ID of the knowledge base, which is the `Data.Id` parameter returned by the [CreateIndex](https://www.alibabacloud.com/help/en/model-studio/developer-reference/api-bailian-2023-12-29-createindex) operation.
        # 
        # This parameter is required.
        self.index_id = index_id
        # The number of the pages to return. Pages start from page 1. Default value: 1.
        self.page_num = page_num
        # The number of chunks to display on each page. Maximum value: 100. Default value: 10.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fields is not None:
            result['Fields'] = self.fields
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.filed is not None:
            result['Filed'] = self.filed
        if self.index_id is not None:
            result['IndexId'] = self.index_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Fields') is not None:
            self.fields = m.get('Fields')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('Filed') is not None:
            self.filed = m.get('Filed')
        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListChunksResponseBodyDataNodes(TeaModel):
    def __init__(
        self,
        metadata: Any = None,
        score: float = None,
        text: str = None,
    ):
        # The metadata map of the chunk.
        self.metadata = metadata
        # The similarity score of the chunk.
        self.score = score
        # The text of the chunk.
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.score is not None:
            result['Score'] = self.score
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class ListChunksResponseBodyData(TeaModel):
    def __init__(
        self,
        nodes: List[ListChunksResponseBodyDataNodes] = None,
        total: int = None,
    ):
        # The list of chunks.
        self.nodes = nodes
        # The total number of chunks returned.
        self.total = total

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = ListChunksResponseBodyDataNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListChunksResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListChunksResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        # The error code.
        self.code = code
        # The data returned.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The HTTP status code returned.
        self.status = status
        # Indications whether the API call is successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListChunksResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListChunksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListChunksResponseBody = None,
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
            temp_model = ListChunksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFileRequest(TeaModel):
    def __init__(
        self,
        category_id: str = None,
        file_name: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # This parameter is required.
        self.category_id = category_id
        self.file_name = file_name
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListFileResponseBodyDataFileList(TeaModel):
    def __init__(
        self,
        category_id: str = None,
        create_time: str = None,
        file_id: str = None,
        file_name: str = None,
        file_type: str = None,
        parser: str = None,
        size_in_bytes: int = None,
        status: str = None,
        tags: List[str] = None,
    ):
        self.category_id = category_id
        self.create_time = create_time
        self.file_id = file_id
        self.file_name = file_name
        self.file_type = file_type
        self.parser = parser
        self.size_in_bytes = size_in_bytes
        self.status = status
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.parser is not None:
            result['Parser'] = self.parser
        if self.size_in_bytes is not None:
            result['SizeInBytes'] = self.size_in_bytes
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('Parser') is not None:
            self.parser = m.get('Parser')
        if m.get('SizeInBytes') is not None:
            self.size_in_bytes = m.get('SizeInBytes')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class ListFileResponseBodyData(TeaModel):
    def __init__(
        self,
        file_list: List[ListFileResponseBodyDataFileList] = None,
        has_next: bool = None,
        max_results: int = None,
        next_token: str = None,
        total_count: int = None,
    ):
        self.file_list = file_list
        self.has_next = has_next
        self.max_results = max_results
        self.next_token = next_token
        self.total_count = total_count

    def validate(self):
        if self.file_list:
            for k in self.file_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FileList'] = []
        if self.file_list is not None:
            for k in self.file_list:
                result['FileList'].append(k.to_map() if k else None)
        if self.has_next is not None:
            result['HasNext'] = self.has_next
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.file_list = []
        if m.get('FileList') is not None:
            for k in m.get('FileList'):
                temp_model = ListFileResponseBodyDataFileList()
                self.file_list.append(temp_model.from_map(k))
        if m.get('HasNext') is not None:
            self.has_next = m.get('HasNext')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListFileResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListFileResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.status = status
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListFileResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFileResponseBody = None,
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
            temp_model = ListFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIndexDocumentsRequest(TeaModel):
    def __init__(
        self,
        document_name: str = None,
        document_status: str = None,
        enable_name_like: str = None,
        index_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The names of the queried documents. The default value is null, which means the names are not used to filter the results.
        self.document_name = document_name
        # The import status of the documents to be queried. Valid values:
        # 
        # *   INSERT_ERROR
        # *   RUNNING
        # *   DELETED
        # *   FINISH
        # 
        # The default value is null, which means the import status is not used to filter the results.
        self.document_status = document_status
        self.enable_name_like = enable_name_like
        # The primary key ID of the knowledge base, which is the `Data.Id` parameter returned by the [CreateIndex](https://www.alibabacloud.com/help/en/model-studio/developer-reference/api-bailian-2023-12-29-createindex) operation.
        # 
        # This parameter is required.
        self.index_id = index_id
        # The page numbers of the pages to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of documents displayed on each page. No maximum value. Default value: 10.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.document_name is not None:
            result['DocumentName'] = self.document_name
        if self.document_status is not None:
            result['DocumentStatus'] = self.document_status
        if self.enable_name_like is not None:
            result['EnableNameLike'] = self.enable_name_like
        if self.index_id is not None:
            result['IndexId'] = self.index_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocumentName') is not None:
            self.document_name = m.get('DocumentName')
        if m.get('DocumentStatus') is not None:
            self.document_status = m.get('DocumentStatus')
        if m.get('EnableNameLike') is not None:
            self.enable_name_like = m.get('EnableNameLike')
        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListIndexDocumentsResponseBodyDataDocuments(TeaModel):
    def __init__(
        self,
        code: str = None,
        document_type: str = None,
        gmt_modified: int = None,
        id: str = None,
        message: str = None,
        name: str = None,
        size: int = None,
        source_id: str = None,
        status: str = None,
    ):
        # The error status code of document import.
        self.code = code
        # The format of the document. Valid values: pdf, docx, doc, txt, md, pptx, ppt, and EXCEL.
        self.document_type = document_type
        self.gmt_modified = gmt_modified
        # The primary key ID of the document.
        self.id = id
        # The error message of document import.
        self.message = message
        # The name of the document.
        self.name = name
        # The size of the document. Unit: bytes.
        self.size = size
        # For unstructured knowledge base, this parameter is the category ID. To view the category ID, you can click the ID icon next to the category name on the Unstructured Data tab of the [Data Management](https://bailian.console.aliyun.com/#/data-center) page.
        # 
        # For structured knowledge base, this parameter is the data table ID. To view the table ID, you can click the ID icon next to the table name on the Structured Data tab of the [Data Management](https://bailian.console.aliyun.com/#/data-center) page.
        self.source_id = source_id
        # The import status of the document. Valid values:
        # 
        # *   INSERT_ERROR
        # *   RUNNING
        # *   DELETED
        # *   FINISH
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.document_type is not None:
            result['DocumentType'] = self.document_type
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.size is not None:
            result['Size'] = self.size
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DocumentType') is not None:
            self.document_type = m.get('DocumentType')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListIndexDocumentsResponseBodyData(TeaModel):
    def __init__(
        self,
        documents: List[ListIndexDocumentsResponseBodyDataDocuments] = None,
        index_id: str = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The list of documents in the knowledge base.
        self.documents = documents
        # The primary key ID of the knowledge base.
        self.index_id = index_id
        # The specified page number.
        self.page_number = page_number
        # The specified number of documents on each page.
        self.page_size = page_size
        # The total number of documents returned.
        self.total_count = total_count

    def validate(self):
        if self.documents:
            for k in self.documents:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Documents'] = []
        if self.documents is not None:
            for k in self.documents:
                result['Documents'].append(k.to_map() if k else None)
        if self.index_id is not None:
            result['IndexId'] = self.index_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.documents = []
        if m.get('Documents') is not None:
            for k in m.get('Documents'):
                temp_model = ListIndexDocumentsResponseBodyDataDocuments()
                self.documents.append(temp_model.from_map(k))
        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListIndexDocumentsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListIndexDocumentsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        # HTTP status code
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The status code.
        self.status = status
        # Indications whether the API call is successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListIndexDocumentsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListIndexDocumentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListIndexDocumentsResponseBody = None,
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
            temp_model = ListIndexDocumentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIndexFileDetailsRequest(TeaModel):
    def __init__(
        self,
        document_name: str = None,
        document_status: str = None,
        enable_name_like: str = None,
        index_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.document_name = document_name
        self.document_status = document_status
        self.enable_name_like = enable_name_like
        self.index_id = index_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.document_name is not None:
            result['DocumentName'] = self.document_name
        if self.document_status is not None:
            result['DocumentStatus'] = self.document_status
        if self.enable_name_like is not None:
            result['EnableNameLike'] = self.enable_name_like
        if self.index_id is not None:
            result['IndexId'] = self.index_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocumentName') is not None:
            self.document_name = m.get('DocumentName')
        if m.get('DocumentStatus') is not None:
            self.document_status = m.get('DocumentStatus')
        if m.get('EnableNameLike') is not None:
            self.enable_name_like = m.get('EnableNameLike')
        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListIndexFileDetailsResponseBodyDataDocuments(TeaModel):
    def __init__(
        self,
        chunk_mode: str = None,
        chunk_size: str = None,
        code: str = None,
        document_type: str = None,
        enable_headers: str = None,
        gmt_modified: int = None,
        id: str = None,
        message: str = None,
        name: str = None,
        overlap_size: str = None,
        size: int = None,
        source_id: str = None,
        status: str = None,
        separator: str = None,
    ):
        self.chunk_mode = chunk_mode
        self.chunk_size = chunk_size
        self.code = code
        self.document_type = document_type
        self.enable_headers = enable_headers
        self.gmt_modified = gmt_modified
        self.id = id
        self.message = message
        self.name = name
        self.overlap_size = overlap_size
        self.size = size
        self.source_id = source_id
        self.status = status
        self.separator = separator

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chunk_mode is not None:
            result['ChunkMode'] = self.chunk_mode
        if self.chunk_size is not None:
            result['ChunkSize'] = self.chunk_size
        if self.code is not None:
            result['Code'] = self.code
        if self.document_type is not None:
            result['DocumentType'] = self.document_type
        if self.enable_headers is not None:
            result['EnableHeaders'] = self.enable_headers
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.overlap_size is not None:
            result['OverlapSize'] = self.overlap_size
        if self.size is not None:
            result['Size'] = self.size
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.status is not None:
            result['Status'] = self.status
        if self.separator is not None:
            result['separator'] = self.separator
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChunkMode') is not None:
            self.chunk_mode = m.get('ChunkMode')
        if m.get('ChunkSize') is not None:
            self.chunk_size = m.get('ChunkSize')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DocumentType') is not None:
            self.document_type = m.get('DocumentType')
        if m.get('EnableHeaders') is not None:
            self.enable_headers = m.get('EnableHeaders')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OverlapSize') is not None:
            self.overlap_size = m.get('OverlapSize')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('separator') is not None:
            self.separator = m.get('separator')
        return self


class ListIndexFileDetailsResponseBodyData(TeaModel):
    def __init__(
        self,
        documents: List[ListIndexFileDetailsResponseBodyDataDocuments] = None,
        index_id: str = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.documents = documents
        self.index_id = index_id
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.documents:
            for k in self.documents:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Documents'] = []
        if self.documents is not None:
            for k in self.documents:
                result['Documents'].append(k.to_map() if k else None)
        if self.index_id is not None:
            result['IndexId'] = self.index_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.documents = []
        if m.get('Documents') is not None:
            for k in m.get('Documents'):
                temp_model = ListIndexFileDetailsResponseBodyDataDocuments()
                self.documents.append(temp_model.from_map(k))
        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListIndexFileDetailsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListIndexFileDetailsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.status = status
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListIndexFileDetailsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListIndexFileDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListIndexFileDetailsResponseBody = None,
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
            temp_model = ListIndexFileDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIndicesRequest(TeaModel):
    def __init__(
        self,
        index_name: str = None,
        page_number: str = None,
        page_size: str = None,
    ):
        # The name of the knowledge base. You can query knowledge base by name. The name must be 1 to 20 characters in length and can contain characters classified as letter in Unicode, including English letters, Chinese characters, digits, among others. The name can also contain colons (:), underscores (_), periods (.), and hyphens (-).
        # 
        # This parameter is left empty by default, which means that all knowledge bases in the specified workspace are queried.
        self.index_name = index_name
        # The number of the pages to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of knowledge bases to display on each page. No maximum value. Default value: 10.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index_name is not None:
            result['IndexName'] = self.index_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IndexName') is not None:
            self.index_name = m.get('IndexName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListIndicesResponseBodyDataIndices(TeaModel):
    def __init__(
        self,
        chunk_size: int = None,
        confg_model: str = None,
        description: str = None,
        document_ids: List[str] = None,
        embedding_model_name: str = None,
        enable_rewrite: bool = None,
        id: str = None,
        name: str = None,
        overlap_size: int = None,
        rerank_min_score: str = None,
        rerank_model_name: str = None,
        separator: str = None,
        sink_instance_id: str = None,
        sink_region: str = None,
        sink_type: str = None,
        source_type: str = None,
        structure_type: str = None,
    ):
        # The estimated length of chunks. Valid values: [1-2048].
        self.chunk_size = chunk_size
        self.confg_model = confg_model
        # The description of the knowledge base.
        self.description = description
        # The list of the primary key IDs of the documents.
        self.document_ids = document_ids
        # The name of the embedding model. Valid values:
        # 
        # *   text-embedding-v2
        self.embedding_model_name = embedding_model_name
        self.enable_rewrite = enable_rewrite
        # The primary key ID of the knowledge base, which is the `Data.Id` parameter returned by the [CreateIndex](https://www.alibabacloud.com/help/en/model-studio/developer-reference/api-bailian-2023-12-29-createindex) operation.
        self.id = id
        # The name of the knowledge base.
        self.name = name
        # The overlap length. Valid values: [0-1024].
        self.overlap_size = overlap_size
        # Similarity Threshold Valid values: [0.01-1.00].
        self.rerank_min_score = rerank_min_score
        # The name of the rank model. Valid values:
        # 
        # *   gte-rerank-hybrid
        # *   gte-rerank
        self.rerank_model_name = rerank_model_name
        # The clause identifier. Separate multiple clause identifiers with |. Valid values:
        # 
        # *   \\n: line break
        # *   ，: Chinese comma
        # *   ,: English comma
        # *   。 : Chinese full stop
        # *   .: English full stop
        # *   ！ : Chinese exclamation point
        # *   ! : English exclamation point
        # *   ；: Chinese semicolon
        # *   ;: English semicolon
        # *   ？ : Chinese question mark
        # *   ?: English question mark
        self.separator = separator
        # The ID of the vector storage instance.
        self.sink_instance_id = sink_instance_id
        # The region of the vector storage instance.
        self.sink_region = sink_region
        # The vector storage type of the knowledge base. Valid values:
        # 
        # *   ES: Built-in vector database.
        # *   BUILT_IN: Built-in vector database.
        # *   ADB: AnalyticDB for PostgreSQL database.
        self.sink_type = sink_type
        # The data type of [Data Management](https://bailian.console.aliyun.com/#/data-center). For unstructured knowledge base, possible values:
        # 
        # *   DATA_CENTER_CATEGORY: The category type.
        # *   DATA_CENTER_FILE: The document type.
        # 
        # For structured knowledge base, possible values:
        # 
        # *   DATA_CENTER_STRUCTURED_TABLE: The data table type.
        self.source_type = source_type
        # The vector storage type of the knowledge base. Valid values:
        # 
        # *   UNSTRUCTURED
        self.structure_type = structure_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chunk_size is not None:
            result['ChunkSize'] = self.chunk_size
        if self.confg_model is not None:
            result['ConfgModel'] = self.confg_model
        if self.description is not None:
            result['Description'] = self.description
        if self.document_ids is not None:
            result['DocumentIds'] = self.document_ids
        if self.embedding_model_name is not None:
            result['EmbeddingModelName'] = self.embedding_model_name
        if self.enable_rewrite is not None:
            result['EnableRewrite'] = self.enable_rewrite
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.overlap_size is not None:
            result['OverlapSize'] = self.overlap_size
        if self.rerank_min_score is not None:
            result['RerankMinScore'] = self.rerank_min_score
        if self.rerank_model_name is not None:
            result['RerankModelName'] = self.rerank_model_name
        if self.separator is not None:
            result['Separator'] = self.separator
        if self.sink_instance_id is not None:
            result['SinkInstanceId'] = self.sink_instance_id
        if self.sink_region is not None:
            result['SinkRegion'] = self.sink_region
        if self.sink_type is not None:
            result['SinkType'] = self.sink_type
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.structure_type is not None:
            result['StructureType'] = self.structure_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChunkSize') is not None:
            self.chunk_size = m.get('ChunkSize')
        if m.get('ConfgModel') is not None:
            self.confg_model = m.get('ConfgModel')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DocumentIds') is not None:
            self.document_ids = m.get('DocumentIds')
        if m.get('EmbeddingModelName') is not None:
            self.embedding_model_name = m.get('EmbeddingModelName')
        if m.get('EnableRewrite') is not None:
            self.enable_rewrite = m.get('EnableRewrite')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OverlapSize') is not None:
            self.overlap_size = m.get('OverlapSize')
        if m.get('RerankMinScore') is not None:
            self.rerank_min_score = m.get('RerankMinScore')
        if m.get('RerankModelName') is not None:
            self.rerank_model_name = m.get('RerankModelName')
        if m.get('Separator') is not None:
            self.separator = m.get('Separator')
        if m.get('SinkInstanceId') is not None:
            self.sink_instance_id = m.get('SinkInstanceId')
        if m.get('SinkRegion') is not None:
            self.sink_region = m.get('SinkRegion')
        if m.get('SinkType') is not None:
            self.sink_type = m.get('SinkType')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('StructureType') is not None:
            self.structure_type = m.get('StructureType')
        return self


class ListIndicesResponseBodyData(TeaModel):
    def __init__(
        self,
        indices: List[ListIndicesResponseBodyDataIndices] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The list of knowledge bases.
        self.indices = indices
        # The specified page number.
        self.page_number = page_number
        # The specified number of documents on each page.
        self.page_size = page_size
        # The total number of knowledge bases returned.
        self.total_count = total_count

    def validate(self):
        if self.indices:
            for k in self.indices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Indices'] = []
        if self.indices is not None:
            for k in self.indices:
                result['Indices'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.indices = []
        if m.get('Indices') is not None:
            for k in m.get('Indices'):
                temp_model = ListIndicesResponseBodyDataIndices()
                self.indices.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListIndicesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListIndicesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        # HTTP status code
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The HTTP status code returned.
        self.status = status
        # Indications whether the API call is successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListIndicesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListIndicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListIndicesResponseBody = None,
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
            temp_model = ListIndicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMemoriesRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListMemoriesResponseBodyMemories(TeaModel):
    def __init__(
        self,
        description: str = None,
        memory_id: str = None,
    ):
        self.description = description
        self.memory_id = memory_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.memory_id is not None:
            result['memoryId'] = self.memory_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('memoryId') is not None:
            self.memory_id = m.get('memoryId')
        return self


class ListMemoriesResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        memories: List[ListMemoriesResponseBodyMemories] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
        workspace_id: str = None,
    ):
        self.max_results = max_results
        self.memories = memories
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count
        self.workspace_id = workspace_id

    def validate(self):
        if self.memories:
            for k in self.memories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        result['memories'] = []
        if self.memories is not None:
            for k in self.memories:
                result['memories'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        self.memories = []
        if m.get('memories') is not None:
            for k in m.get('memories'):
                temp_model = ListMemoriesResponseBodyMemories()
                self.memories.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class ListMemoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMemoriesResponseBody = None,
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
            temp_model = ListMemoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMemoryNodesRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListMemoryNodesResponseBodyMemoryNodes(TeaModel):
    def __init__(
        self,
        content: str = None,
        memory_node_id: str = None,
    ):
        self.content = content
        self.memory_node_id = memory_node_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.memory_node_id is not None:
            result['memoryNodeId'] = self.memory_node_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('memoryNodeId') is not None:
            self.memory_node_id = m.get('memoryNodeId')
        return self


class ListMemoryNodesResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        memory_nodes: List[ListMemoryNodesResponseBodyMemoryNodes] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        self.memory_nodes = memory_nodes
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.memory_nodes:
            for k in self.memory_nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        result['memoryNodes'] = []
        if self.memory_nodes is not None:
            for k in self.memory_nodes:
                result['memoryNodes'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        self.memory_nodes = []
        if m.get('memoryNodes') is not None:
            for k in m.get('memoryNodes'):
                temp_model = ListMemoryNodesResponseBodyMemoryNodes()
                self.memory_nodes.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListMemoryNodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMemoryNodesResponseBody = None,
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
            temp_model = ListMemoryNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPromptTemplatesRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        name: str = None,
        next_token: str = None,
        type: str = None,
    ):
        # The maximum number of returned entries.
        self.max_results = max_results
        # The keyword that is used to search for templates.
        self.name = name
        # The token that determines the start position of the query. Set this parameter to the value of the NextToken parameter that is returned from the last call.
        self.next_token = next_token
        # The type of the template. Valid values: · System · Custom
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.name is not None:
            result['name'] = self.name
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListPromptTemplatesResponseBodyPromptTemplates(TeaModel):
    def __init__(
        self,
        content: str = None,
        name: str = None,
        prompt_template_id: str = None,
        type: str = None,
        variables: List[str] = None,
    ):
        # The template content
        self.content = content
        # The template name.
        self.name = name
        # The template ID.
        self.prompt_template_id = prompt_template_id
        # The template type.
        self.type = type
        # The variables of the template.
        self.variables = variables

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.name is not None:
            result['name'] = self.name
        if self.prompt_template_id is not None:
            result['promptTemplateId'] = self.prompt_template_id
        if self.type is not None:
            result['type'] = self.type
        if self.variables is not None:
            result['variables'] = self.variables
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('promptTemplateId') is not None:
            self.prompt_template_id = m.get('promptTemplateId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('variables') is not None:
            self.variables = m.get('variables')
        return self


class ListPromptTemplatesResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        prompt_templates: List[ListPromptTemplatesResponseBodyPromptTemplates] = None,
        request_id: str = None,
        total_count: int = None,
        workspace_id: str = None,
    ):
        # The maximum number of returned entries.
        self.max_results = max_results
        # The token that determines the start position of the next query.
        self.next_token = next_token
        # The templates.
        self.prompt_templates = prompt_templates
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        if self.prompt_templates:
            for k in self.prompt_templates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        result['promptTemplates'] = []
        if self.prompt_templates is not None:
            for k in self.prompt_templates:
                result['promptTemplates'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        self.prompt_templates = []
        if m.get('promptTemplates') is not None:
            for k in m.get('promptTemplates'):
                temp_model = ListPromptTemplatesResponseBodyPromptTemplates()
                self.prompt_templates.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class ListPromptTemplatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPromptTemplatesResponseBody = None,
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
            temp_model = ListPromptTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPublishedAgentRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
    ):
        self.page_no = page_no
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListPublishedAgentResponseBodyDataListApplicationConfigHistoryConfig(TeaModel):
    def __init__(
        self,
        enable_adb_record: bool = None,
        enable_record: bool = None,
        instance_id: str = None,
        region: str = None,
        store_code: str = None,
    ):
        self.enable_adb_record = enable_adb_record
        self.enable_record = enable_record
        self.instance_id = instance_id
        self.region = region
        self.store_code = store_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_adb_record is not None:
            result['enableAdbRecord'] = self.enable_adb_record
        if self.enable_record is not None:
            result['enableRecord'] = self.enable_record
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.region is not None:
            result['region'] = self.region
        if self.store_code is not None:
            result['storeCode'] = self.store_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enableAdbRecord') is not None:
            self.enable_adb_record = m.get('enableAdbRecord')
        if m.get('enableRecord') is not None:
            self.enable_record = m.get('enableRecord')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('storeCode') is not None:
            self.store_code = m.get('storeCode')
        return self


class ListPublishedAgentResponseBodyDataListApplicationConfigLongTermMemory(TeaModel):
    def __init__(
        self,
        enable: bool = None,
    ):
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        return self


class ListPublishedAgentResponseBodyDataListApplicationConfigParameters(TeaModel):
    def __init__(
        self,
        dialog_round: int = None,
        max_tokens: int = None,
        temperature: float = None,
    ):
        self.dialog_round = dialog_round
        self.max_tokens = max_tokens
        self.temperature = temperature

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dialog_round is not None:
            result['dialogRound'] = self.dialog_round
        if self.max_tokens is not None:
            result['maxTokens'] = self.max_tokens
        if self.temperature is not None:
            result['temperature'] = self.temperature
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dialogRound') is not None:
            self.dialog_round = m.get('dialogRound')
        if m.get('maxTokens') is not None:
            self.max_tokens = m.get('maxTokens')
        if m.get('temperature') is not None:
            self.temperature = m.get('temperature')
        return self


class ListPublishedAgentResponseBodyDataListApplicationConfigRagConfig(TeaModel):
    def __init__(
        self,
        enable_citation: bool = None,
        enable_search: bool = None,
        knowledge_base_code_list: List[str] = None,
        top_k: int = None,
    ):
        self.enable_citation = enable_citation
        self.enable_search = enable_search
        self.knowledge_base_code_list = knowledge_base_code_list
        self.top_k = top_k

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_citation is not None:
            result['enableCitation'] = self.enable_citation
        if self.enable_search is not None:
            result['enableSearch'] = self.enable_search
        if self.knowledge_base_code_list is not None:
            result['knowledgeBaseCodeList'] = self.knowledge_base_code_list
        if self.top_k is not None:
            result['topK'] = self.top_k
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enableCitation') is not None:
            self.enable_citation = m.get('enableCitation')
        if m.get('enableSearch') is not None:
            self.enable_search = m.get('enableSearch')
        if m.get('knowledgeBaseCodeList') is not None:
            self.knowledge_base_code_list = m.get('knowledgeBaseCodeList')
        if m.get('topK') is not None:
            self.top_k = m.get('topK')
        return self


class ListPublishedAgentResponseBodyDataListApplicationConfigSecurity(TeaModel):
    def __init__(
        self,
        processing_strategy: str = None,
    ):
        self.processing_strategy = processing_strategy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.processing_strategy is not None:
            result['processingStrategy'] = self.processing_strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('processingStrategy') is not None:
            self.processing_strategy = m.get('processingStrategy')
        return self


class ListPublishedAgentResponseBodyDataListApplicationConfigTools(TeaModel):
    def __init__(
        self,
        type: str = None,
    ):
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


class ListPublishedAgentResponseBodyDataListApplicationConfigWorkFlows(TeaModel):
    def __init__(
        self,
        type: str = None,
    ):
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


class ListPublishedAgentResponseBodyDataListApplicationConfig(TeaModel):
    def __init__(
        self,
        history_config: ListPublishedAgentResponseBodyDataListApplicationConfigHistoryConfig = None,
        long_term_memory: ListPublishedAgentResponseBodyDataListApplicationConfigLongTermMemory = None,
        parameters: ListPublishedAgentResponseBodyDataListApplicationConfigParameters = None,
        rag_config: ListPublishedAgentResponseBodyDataListApplicationConfigRagConfig = None,
        security: ListPublishedAgentResponseBodyDataListApplicationConfigSecurity = None,
        tools: List[ListPublishedAgentResponseBodyDataListApplicationConfigTools] = None,
        work_flows: List[ListPublishedAgentResponseBodyDataListApplicationConfigWorkFlows] = None,
    ):
        self.history_config = history_config
        self.long_term_memory = long_term_memory
        self.parameters = parameters
        self.rag_config = rag_config
        self.security = security
        self.tools = tools
        self.work_flows = work_flows

    def validate(self):
        if self.history_config:
            self.history_config.validate()
        if self.long_term_memory:
            self.long_term_memory.validate()
        if self.parameters:
            self.parameters.validate()
        if self.rag_config:
            self.rag_config.validate()
        if self.security:
            self.security.validate()
        if self.tools:
            for k in self.tools:
                if k:
                    k.validate()
        if self.work_flows:
            for k in self.work_flows:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.history_config is not None:
            result['historyConfig'] = self.history_config.to_map()
        if self.long_term_memory is not None:
            result['longTermMemory'] = self.long_term_memory.to_map()
        if self.parameters is not None:
            result['parameters'] = self.parameters.to_map()
        if self.rag_config is not None:
            result['ragConfig'] = self.rag_config.to_map()
        if self.security is not None:
            result['security'] = self.security.to_map()
        result['tools'] = []
        if self.tools is not None:
            for k in self.tools:
                result['tools'].append(k.to_map() if k else None)
        result['workFlows'] = []
        if self.work_flows is not None:
            for k in self.work_flows:
                result['workFlows'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('historyConfig') is not None:
            temp_model = ListPublishedAgentResponseBodyDataListApplicationConfigHistoryConfig()
            self.history_config = temp_model.from_map(m['historyConfig'])
        if m.get('longTermMemory') is not None:
            temp_model = ListPublishedAgentResponseBodyDataListApplicationConfigLongTermMemory()
            self.long_term_memory = temp_model.from_map(m['longTermMemory'])
        if m.get('parameters') is not None:
            temp_model = ListPublishedAgentResponseBodyDataListApplicationConfigParameters()
            self.parameters = temp_model.from_map(m['parameters'])
        if m.get('ragConfig') is not None:
            temp_model = ListPublishedAgentResponseBodyDataListApplicationConfigRagConfig()
            self.rag_config = temp_model.from_map(m['ragConfig'])
        if m.get('security') is not None:
            temp_model = ListPublishedAgentResponseBodyDataListApplicationConfigSecurity()
            self.security = temp_model.from_map(m['security'])
        self.tools = []
        if m.get('tools') is not None:
            for k in m.get('tools'):
                temp_model = ListPublishedAgentResponseBodyDataListApplicationConfigTools()
                self.tools.append(temp_model.from_map(k))
        self.work_flows = []
        if m.get('workFlows') is not None:
            for k in m.get('workFlows'):
                temp_model = ListPublishedAgentResponseBodyDataListApplicationConfigWorkFlows()
                self.work_flows.append(temp_model.from_map(k))
        return self


class ListPublishedAgentResponseBodyDataList(TeaModel):
    def __init__(
        self,
        application_config: ListPublishedAgentResponseBodyDataListApplicationConfig = None,
        code: str = None,
        instructions: str = None,
        model_id: str = None,
        name: str = None,
    ):
        self.application_config = application_config
        self.code = code
        self.instructions = instructions
        self.model_id = model_id
        self.name = name

    def validate(self):
        if self.application_config:
            self.application_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_config is not None:
            result['applicationConfig'] = self.application_config.to_map()
        if self.code is not None:
            result['code'] = self.code
        if self.instructions is not None:
            result['instructions'] = self.instructions
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applicationConfig') is not None:
            temp_model = ListPublishedAgentResponseBodyDataListApplicationConfig()
            self.application_config = temp_model.from_map(m['applicationConfig'])
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('instructions') is not None:
            self.instructions = m.get('instructions')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListPublishedAgentResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[ListPublishedAgentResponseBodyDataList] = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.list = list
        self.page_no = page_no
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListPublishedAgentResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListPublishedAgentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListPublishedAgentResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ListPublishedAgentResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListPublishedAgentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPublishedAgentResponseBody = None,
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
            temp_model = ListPublishedAgentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RetrieveRequestQueryHistory(TeaModel):
    def __init__(
        self,
        content: str = None,
        role: str = None,
    ):
        self.content = content
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.role is not None:
            result['role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('role') is not None:
            self.role = m.get('role')
        return self


class RetrieveRequestRerank(TeaModel):
    def __init__(
        self,
        model_name: str = None,
    ):
        # The name of the rank model. For more information, see [Create a knowledge base](https://www.alibabacloud.com/help/en/model-studio/user-guide/rag-knowledge-base). Valid values:
        # 
        # *   gte-rerank-hybrid: Recommended official model.
        # *   gte-rerank
        self.model_name = model_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        return self


class RetrieveRequestRewrite(TeaModel):
    def __init__(
        self,
        model_name: str = None,
    ):
        # Conversation rewriting model name. The query rewriting model automatically adjusts the original prompt based on the context to improve retrieval performance. Valid value:
        # 
        # *   conv-rewrite-qwen-1.8b
        # 
        # By default, this parameter is left empty, which means conv-rewrite-qwen-1.8b is used.
        self.model_name = model_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        return self


class RetrieveRequest(TeaModel):
    def __init__(
        self,
        dense_similarity_top_k: int = None,
        enable_reranking: bool = None,
        enable_rewrite: bool = None,
        images: List[str] = None,
        index_id: str = None,
        query: str = None,
        query_history: List[RetrieveRequestQueryHistory] = None,
        rerank: List[RetrieveRequestRerank] = None,
        rerank_min_score: float = None,
        rerank_top_n: int = None,
        rewrite: List[RetrieveRequestRewrite] = None,
        save_retriever_history: bool = None,
        search_filters: List[Dict[str, str]] = None,
        sparse_similarity_top_k: int = None,
    ):
        # Vector retrieval top K. After generating vectors based on input text, the top K chunks in the knowledge base that are most similar to the vector representation of the input text are retrieved. Valid values: 0 to 100. The sum of the `DenseSimilarityTopK` and `SparseSimilarityTopK` parameters must be less than or equal to 200.
        # 
        # Default value: 100.
        self.dense_similarity_top_k = dense_similarity_top_k
        # Specifies whether to enable reranking. For more information, see [Create a knowledge base](https://www.alibabacloud.com/help/en/model-studio/user-guide/rag-knowledge-base). Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: true.
        self.enable_reranking = enable_reranking
        # Specifies whether to enable multi-round conversation rewriting. For more information, see [Create a knowledge base](https://www.alibabacloud.com/help/en/model-studio/user-guide/rag-knowledge-base). Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.enable_rewrite = enable_rewrite
        self.images = images
        # The primary key ID of the knowledge base, which is the `Data.Id` parameter returned by the [CreateIndex](https://www.alibabacloud.com/help/en/model-studio/developer-reference/api-bailian-2023-12-29-createindex) operation.
        # 
        # This parameter is required.
        self.index_id = index_id
        # The input query prompt. The length and characters of the query are not limited.
        self.query = query
        self.query_history = query_history
        # Ranking configurations.
        self.rerank = rerank
        # Similarity Threshold The lowest similarity score of chunks that can be returned. This parameter is used to filter text chunks returned by the rank model. For more information, see [Create a knowledge base](https://www.alibabacloud.com/help/en/model-studio/user-guide/rag-knowledge-base). Valid values: [0.01-1.00]. The priority of this parameter is greater than the similarity threshold configured for the knowledge base.
        # 
        # By default, this parameter is left empty. In this case, the similarity threshold of the knowledge base is used.
        self.rerank_min_score = rerank_min_score
        # The top N return data after reranking. Valid values: 1 to 20. Default value: 5.
        self.rerank_top_n = rerank_top_n
        # Conversation rewriting configurations.
        self.rewrite = rewrite
        # Specifies whether to save the retrieve test history. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.save_retriever_history = save_retriever_history
        # Specifies complex filter conditions. For more information about the syntax of SearchFilters, see the SearchFilter syntax section of this topic.
        self.search_filters = search_filters
        # The top K of keyword retrieval. Chunks that exactly match the keywords of the input text are retrieved from the knowledge base. This filters out irrelevant chunks and boosts accuracy. Valid values: 0 to 100. The sum of the `DenseSimilarityTopK` and `SparseSimilarityTopK` parameters must be less than or equal to 200.
        # 
        # Default value: 100.
        self.sparse_similarity_top_k = sparse_similarity_top_k

    def validate(self):
        if self.query_history:
            for k in self.query_history:
                if k:
                    k.validate()
        if self.rerank:
            for k in self.rerank:
                if k:
                    k.validate()
        if self.rewrite:
            for k in self.rewrite:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dense_similarity_top_k is not None:
            result['DenseSimilarityTopK'] = self.dense_similarity_top_k
        if self.enable_reranking is not None:
            result['EnableReranking'] = self.enable_reranking
        if self.enable_rewrite is not None:
            result['EnableRewrite'] = self.enable_rewrite
        if self.images is not None:
            result['Images'] = self.images
        if self.index_id is not None:
            result['IndexId'] = self.index_id
        if self.query is not None:
            result['Query'] = self.query
        result['QueryHistory'] = []
        if self.query_history is not None:
            for k in self.query_history:
                result['QueryHistory'].append(k.to_map() if k else None)
        result['Rerank'] = []
        if self.rerank is not None:
            for k in self.rerank:
                result['Rerank'].append(k.to_map() if k else None)
        if self.rerank_min_score is not None:
            result['RerankMinScore'] = self.rerank_min_score
        if self.rerank_top_n is not None:
            result['RerankTopN'] = self.rerank_top_n
        result['Rewrite'] = []
        if self.rewrite is not None:
            for k in self.rewrite:
                result['Rewrite'].append(k.to_map() if k else None)
        if self.save_retriever_history is not None:
            result['SaveRetrieverHistory'] = self.save_retriever_history
        if self.search_filters is not None:
            result['SearchFilters'] = self.search_filters
        if self.sparse_similarity_top_k is not None:
            result['SparseSimilarityTopK'] = self.sparse_similarity_top_k
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DenseSimilarityTopK') is not None:
            self.dense_similarity_top_k = m.get('DenseSimilarityTopK')
        if m.get('EnableReranking') is not None:
            self.enable_reranking = m.get('EnableReranking')
        if m.get('EnableRewrite') is not None:
            self.enable_rewrite = m.get('EnableRewrite')
        if m.get('Images') is not None:
            self.images = m.get('Images')
        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        self.query_history = []
        if m.get('QueryHistory') is not None:
            for k in m.get('QueryHistory'):
                temp_model = RetrieveRequestQueryHistory()
                self.query_history.append(temp_model.from_map(k))
        self.rerank = []
        if m.get('Rerank') is not None:
            for k in m.get('Rerank'):
                temp_model = RetrieveRequestRerank()
                self.rerank.append(temp_model.from_map(k))
        if m.get('RerankMinScore') is not None:
            self.rerank_min_score = m.get('RerankMinScore')
        if m.get('RerankTopN') is not None:
            self.rerank_top_n = m.get('RerankTopN')
        self.rewrite = []
        if m.get('Rewrite') is not None:
            for k in m.get('Rewrite'):
                temp_model = RetrieveRequestRewrite()
                self.rewrite.append(temp_model.from_map(k))
        if m.get('SaveRetrieverHistory') is not None:
            self.save_retriever_history = m.get('SaveRetrieverHistory')
        if m.get('SearchFilters') is not None:
            self.search_filters = m.get('SearchFilters')
        if m.get('SparseSimilarityTopK') is not None:
            self.sparse_similarity_top_k = m.get('SparseSimilarityTopK')
        return self


class RetrieveShrinkRequest(TeaModel):
    def __init__(
        self,
        dense_similarity_top_k: int = None,
        enable_reranking: bool = None,
        enable_rewrite: bool = None,
        images_shrink: str = None,
        index_id: str = None,
        query: str = None,
        query_history_shrink: str = None,
        rerank_shrink: str = None,
        rerank_min_score: float = None,
        rerank_top_n: int = None,
        rewrite_shrink: str = None,
        save_retriever_history: bool = None,
        search_filters_shrink: str = None,
        sparse_similarity_top_k: int = None,
    ):
        # Vector retrieval top K. After generating vectors based on input text, the top K chunks in the knowledge base that are most similar to the vector representation of the input text are retrieved. Valid values: 0 to 100. The sum of the `DenseSimilarityTopK` and `SparseSimilarityTopK` parameters must be less than or equal to 200.
        # 
        # Default value: 100.
        self.dense_similarity_top_k = dense_similarity_top_k
        # Specifies whether to enable reranking. For more information, see [Create a knowledge base](https://www.alibabacloud.com/help/en/model-studio/user-guide/rag-knowledge-base). Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: true.
        self.enable_reranking = enable_reranking
        # Specifies whether to enable multi-round conversation rewriting. For more information, see [Create a knowledge base](https://www.alibabacloud.com/help/en/model-studio/user-guide/rag-knowledge-base). Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.enable_rewrite = enable_rewrite
        self.images_shrink = images_shrink
        # The primary key ID of the knowledge base, which is the `Data.Id` parameter returned by the [CreateIndex](https://www.alibabacloud.com/help/en/model-studio/developer-reference/api-bailian-2023-12-29-createindex) operation.
        # 
        # This parameter is required.
        self.index_id = index_id
        # The input query prompt. The length and characters of the query are not limited.
        self.query = query
        self.query_history_shrink = query_history_shrink
        # Ranking configurations.
        self.rerank_shrink = rerank_shrink
        # Similarity Threshold The lowest similarity score of chunks that can be returned. This parameter is used to filter text chunks returned by the rank model. For more information, see [Create a knowledge base](https://www.alibabacloud.com/help/en/model-studio/user-guide/rag-knowledge-base). Valid values: [0.01-1.00]. The priority of this parameter is greater than the similarity threshold configured for the knowledge base.
        # 
        # By default, this parameter is left empty. In this case, the similarity threshold of the knowledge base is used.
        self.rerank_min_score = rerank_min_score
        # The top N return data after reranking. Valid values: 1 to 20. Default value: 5.
        self.rerank_top_n = rerank_top_n
        # Conversation rewriting configurations.
        self.rewrite_shrink = rewrite_shrink
        # Specifies whether to save the retrieve test history. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.save_retriever_history = save_retriever_history
        # Specifies complex filter conditions. For more information about the syntax of SearchFilters, see the SearchFilter syntax section of this topic.
        self.search_filters_shrink = search_filters_shrink
        # The top K of keyword retrieval. Chunks that exactly match the keywords of the input text are retrieved from the knowledge base. This filters out irrelevant chunks and boosts accuracy. Valid values: 0 to 100. The sum of the `DenseSimilarityTopK` and `SparseSimilarityTopK` parameters must be less than or equal to 200.
        # 
        # Default value: 100.
        self.sparse_similarity_top_k = sparse_similarity_top_k

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dense_similarity_top_k is not None:
            result['DenseSimilarityTopK'] = self.dense_similarity_top_k
        if self.enable_reranking is not None:
            result['EnableReranking'] = self.enable_reranking
        if self.enable_rewrite is not None:
            result['EnableRewrite'] = self.enable_rewrite
        if self.images_shrink is not None:
            result['Images'] = self.images_shrink
        if self.index_id is not None:
            result['IndexId'] = self.index_id
        if self.query is not None:
            result['Query'] = self.query
        if self.query_history_shrink is not None:
            result['QueryHistory'] = self.query_history_shrink
        if self.rerank_shrink is not None:
            result['Rerank'] = self.rerank_shrink
        if self.rerank_min_score is not None:
            result['RerankMinScore'] = self.rerank_min_score
        if self.rerank_top_n is not None:
            result['RerankTopN'] = self.rerank_top_n
        if self.rewrite_shrink is not None:
            result['Rewrite'] = self.rewrite_shrink
        if self.save_retriever_history is not None:
            result['SaveRetrieverHistory'] = self.save_retriever_history
        if self.search_filters_shrink is not None:
            result['SearchFilters'] = self.search_filters_shrink
        if self.sparse_similarity_top_k is not None:
            result['SparseSimilarityTopK'] = self.sparse_similarity_top_k
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DenseSimilarityTopK') is not None:
            self.dense_similarity_top_k = m.get('DenseSimilarityTopK')
        if m.get('EnableReranking') is not None:
            self.enable_reranking = m.get('EnableReranking')
        if m.get('EnableRewrite') is not None:
            self.enable_rewrite = m.get('EnableRewrite')
        if m.get('Images') is not None:
            self.images_shrink = m.get('Images')
        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('QueryHistory') is not None:
            self.query_history_shrink = m.get('QueryHistory')
        if m.get('Rerank') is not None:
            self.rerank_shrink = m.get('Rerank')
        if m.get('RerankMinScore') is not None:
            self.rerank_min_score = m.get('RerankMinScore')
        if m.get('RerankTopN') is not None:
            self.rerank_top_n = m.get('RerankTopN')
        if m.get('Rewrite') is not None:
            self.rewrite_shrink = m.get('Rewrite')
        if m.get('SaveRetrieverHistory') is not None:
            self.save_retriever_history = m.get('SaveRetrieverHistory')
        if m.get('SearchFilters') is not None:
            self.search_filters_shrink = m.get('SearchFilters')
        if m.get('SparseSimilarityTopK') is not None:
            self.sparse_similarity_top_k = m.get('SparseSimilarityTopK')
        return self


class RetrieveResponseBodyDataNodes(TeaModel):
    def __init__(
        self,
        metadata: Any = None,
        score: float = None,
        text: str = None,
    ):
        # The metadata map of the chunk.
        self.metadata = metadata
        # The similarity score of the chunk. Valid values:[0-1].
        self.score = score
        # The text of the chunk.
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.score is not None:
            result['Score'] = self.score
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class RetrieveResponseBodyData(TeaModel):
    def __init__(
        self,
        nodes: List[RetrieveResponseBodyDataNodes] = None,
    ):
        # The list of queried chunks.
        self.nodes = nodes

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = RetrieveResponseBodyDataNodes()
                self.nodes.append(temp_model.from_map(k))
        return self


class RetrieveResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: RetrieveResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        # HTTP status code
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The HTTP status code returned.
        self.status = status
        # Indications whether the API call is successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = RetrieveResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RetrieveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RetrieveResponseBody = None,
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
            temp_model = RetrieveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitIndexAddDocumentsJobRequest(TeaModel):
    def __init__(
        self,
        category_ids: List[str] = None,
        chunk_mode: str = None,
        chunk_size: int = None,
        document_ids: List[str] = None,
        enable_headers: bool = None,
        index_id: str = None,
        overlap_size: int = None,
        separator: str = None,
        source_type: str = None,
    ):
        # The list of primary key IDs of the category.
        self.category_ids = category_ids
        self.chunk_mode = chunk_mode
        self.chunk_size = chunk_size
        # The list of the primary key IDs of the documents.
        self.document_ids = document_ids
        self.enable_headers = enable_headers
        # The primary key ID of the knowledge base, which is the `Data.Id` parameter returned by the [CreateIndex](https://www.alibabacloud.com/help/en/model-studio/developer-reference/api-bailian-2023-12-29-createindex) operation.
        # 
        # This parameter is required.
        self.index_id = index_id
        self.overlap_size = overlap_size
        self.separator = separator
        # The data type of [Data Management](https://bailian.console.aliyun.com/#/data-center). For more information, see [Create a knowledge base](https://www.alibabacloud.com/help/en/model-studio/user-guide/rag-knowledge-base). Valid values:
        # 
        # *   DATA_CENTER_CATEGORY: The category type. Import all documents from one or more categories in Data Center.
        # *   DATA_CENTER_FILE: The document type. Import one or more documents from Data Center.
        # 
        # >  If this parameter is set to DATA_CENTER_CATEGORY, you must specify the `CategoryIds` parameter. If this parameter is set to DATA_CENTER_FILE, you must specify the `DocumentIds` parameter.
        # 
        # This parameter is required.
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_ids is not None:
            result['CategoryIds'] = self.category_ids
        if self.chunk_mode is not None:
            result['ChunkMode'] = self.chunk_mode
        if self.chunk_size is not None:
            result['ChunkSize'] = self.chunk_size
        if self.document_ids is not None:
            result['DocumentIds'] = self.document_ids
        if self.enable_headers is not None:
            result['EnableHeaders'] = self.enable_headers
        if self.index_id is not None:
            result['IndexId'] = self.index_id
        if self.overlap_size is not None:
            result['OverlapSize'] = self.overlap_size
        if self.separator is not None:
            result['Separator'] = self.separator
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryIds') is not None:
            self.category_ids = m.get('CategoryIds')
        if m.get('ChunkMode') is not None:
            self.chunk_mode = m.get('ChunkMode')
        if m.get('ChunkSize') is not None:
            self.chunk_size = m.get('ChunkSize')
        if m.get('DocumentIds') is not None:
            self.document_ids = m.get('DocumentIds')
        if m.get('EnableHeaders') is not None:
            self.enable_headers = m.get('EnableHeaders')
        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')
        if m.get('OverlapSize') is not None:
            self.overlap_size = m.get('OverlapSize')
        if m.get('Separator') is not None:
            self.separator = m.get('Separator')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class SubmitIndexAddDocumentsJobShrinkRequest(TeaModel):
    def __init__(
        self,
        category_ids_shrink: str = None,
        chunk_mode: str = None,
        chunk_size: int = None,
        document_ids_shrink: str = None,
        enable_headers: bool = None,
        index_id: str = None,
        overlap_size: int = None,
        separator: str = None,
        source_type: str = None,
    ):
        # The list of primary key IDs of the category.
        self.category_ids_shrink = category_ids_shrink
        self.chunk_mode = chunk_mode
        self.chunk_size = chunk_size
        # The list of the primary key IDs of the documents.
        self.document_ids_shrink = document_ids_shrink
        self.enable_headers = enable_headers
        # The primary key ID of the knowledge base, which is the `Data.Id` parameter returned by the [CreateIndex](https://www.alibabacloud.com/help/en/model-studio/developer-reference/api-bailian-2023-12-29-createindex) operation.
        # 
        # This parameter is required.
        self.index_id = index_id
        self.overlap_size = overlap_size
        self.separator = separator
        # The data type of [Data Management](https://bailian.console.aliyun.com/#/data-center). For more information, see [Create a knowledge base](https://www.alibabacloud.com/help/en/model-studio/user-guide/rag-knowledge-base). Valid values:
        # 
        # *   DATA_CENTER_CATEGORY: The category type. Import all documents from one or more categories in Data Center.
        # *   DATA_CENTER_FILE: The document type. Import one or more documents from Data Center.
        # 
        # >  If this parameter is set to DATA_CENTER_CATEGORY, you must specify the `CategoryIds` parameter. If this parameter is set to DATA_CENTER_FILE, you must specify the `DocumentIds` parameter.
        # 
        # This parameter is required.
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_ids_shrink is not None:
            result['CategoryIds'] = self.category_ids_shrink
        if self.chunk_mode is not None:
            result['ChunkMode'] = self.chunk_mode
        if self.chunk_size is not None:
            result['ChunkSize'] = self.chunk_size
        if self.document_ids_shrink is not None:
            result['DocumentIds'] = self.document_ids_shrink
        if self.enable_headers is not None:
            result['EnableHeaders'] = self.enable_headers
        if self.index_id is not None:
            result['IndexId'] = self.index_id
        if self.overlap_size is not None:
            result['OverlapSize'] = self.overlap_size
        if self.separator is not None:
            result['Separator'] = self.separator
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryIds') is not None:
            self.category_ids_shrink = m.get('CategoryIds')
        if m.get('ChunkMode') is not None:
            self.chunk_mode = m.get('ChunkMode')
        if m.get('ChunkSize') is not None:
            self.chunk_size = m.get('ChunkSize')
        if m.get('DocumentIds') is not None:
            self.document_ids_shrink = m.get('DocumentIds')
        if m.get('EnableHeaders') is not None:
            self.enable_headers = m.get('EnableHeaders')
        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')
        if m.get('OverlapSize') is not None:
            self.overlap_size = m.get('OverlapSize')
        if m.get('Separator') is not None:
            self.separator = m.get('Separator')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class SubmitIndexAddDocumentsJobResponseBodyData(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        # The primary key ID of the task, `JobId`.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class SubmitIndexAddDocumentsJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SubmitIndexAddDocumentsJobResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        # HTTP status code
        self.code = code
        # The data returned.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The HTTP status code returned.
        self.status = status
        # Indications whether the API call is successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = SubmitIndexAddDocumentsJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SubmitIndexAddDocumentsJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitIndexAddDocumentsJobResponseBody = None,
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
            temp_model = SubmitIndexAddDocumentsJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitIndexJobRequest(TeaModel):
    def __init__(
        self,
        index_id: str = None,
    ):
        # The primary key ID of the knowledge base, which is the `Data.Id` parameter returned by the [CreateIndex](https://www.alibabacloud.com/help/en/model-studio/developer-reference/api-bailian-2023-12-29-createindex) operation.
        # 
        # This parameter is required.
        self.index_id = index_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index_id is not None:
            result['IndexId'] = self.index_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')
        return self


class SubmitIndexJobResponseBodyData(TeaModel):
    def __init__(
        self,
        id: str = None,
        index_id: str = None,
    ):
        # The primary key ID of the job, which is the `JobId` parameter of the [GetIndexJobStatus](https://www.alibabacloud.com/help/en/model-studio/developer-reference/api-bailian-2023-12-29-getindexjobstatus) operation.
        self.id = id
        # The primary key ID of the knowledge base.
        self.index_id = index_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.index_id is not None:
            result['IndexId'] = self.index_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')
        return self


class SubmitIndexJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SubmitIndexJobResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        # HTTP status code
        self.code = code
        # The data returned.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The status code.
        self.status = status
        # Indications whether the API call is successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = SubmitIndexJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SubmitIndexJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitIndexJobResponseBody = None,
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
            temp_model = SubmitIndexJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAndPublishAgentRequestApplicationConfigHistoryConfig(TeaModel):
    def __init__(
        self,
        enable_adb_record: bool = None,
        enable_record: bool = None,
        instance_id: str = None,
        region: str = None,
        store_code: str = None,
    ):
        self.enable_adb_record = enable_adb_record
        self.enable_record = enable_record
        self.instance_id = instance_id
        self.region = region
        self.store_code = store_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_adb_record is not None:
            result['enableAdbRecord'] = self.enable_adb_record
        if self.enable_record is not None:
            result['enableRecord'] = self.enable_record
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.region is not None:
            result['region'] = self.region
        if self.store_code is not None:
            result['storeCode'] = self.store_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enableAdbRecord') is not None:
            self.enable_adb_record = m.get('enableAdbRecord')
        if m.get('enableRecord') is not None:
            self.enable_record = m.get('enableRecord')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('storeCode') is not None:
            self.store_code = m.get('storeCode')
        return self


class UpdateAndPublishAgentRequestApplicationConfigLongTermMemory(TeaModel):
    def __init__(
        self,
        enable: bool = None,
    ):
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        return self


class UpdateAndPublishAgentRequestApplicationConfigParameters(TeaModel):
    def __init__(
        self,
        dialog_round: int = None,
        max_tokens: int = None,
        temperature: float = None,
    ):
        self.dialog_round = dialog_round
        self.max_tokens = max_tokens
        self.temperature = temperature

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dialog_round is not None:
            result['dialogRound'] = self.dialog_round
        if self.max_tokens is not None:
            result['maxTokens'] = self.max_tokens
        if self.temperature is not None:
            result['temperature'] = self.temperature
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dialogRound') is not None:
            self.dialog_round = m.get('dialogRound')
        if m.get('maxTokens') is not None:
            self.max_tokens = m.get('maxTokens')
        if m.get('temperature') is not None:
            self.temperature = m.get('temperature')
        return self


class UpdateAndPublishAgentRequestApplicationConfigRagConfig(TeaModel):
    def __init__(
        self,
        answer_scope: str = None,
        enable_citation: bool = None,
        enable_search: bool = None,
        enable_web_search: bool = None,
        fixed_reply_detail: str = None,
        knowledge_base_code_list: List[str] = None,
        prompt_strategy: str = None,
        rag_reject_type: str = None,
        reject_filter_prompt: str = None,
        reject_filter_type: str = None,
        retrieve_max_length: int = None,
        top_k: int = None,
    ):
        self.answer_scope = answer_scope
        self.enable_citation = enable_citation
        self.enable_search = enable_search
        self.enable_web_search = enable_web_search
        self.fixed_reply_detail = fixed_reply_detail
        self.knowledge_base_code_list = knowledge_base_code_list
        self.prompt_strategy = prompt_strategy
        self.rag_reject_type = rag_reject_type
        self.reject_filter_prompt = reject_filter_prompt
        self.reject_filter_type = reject_filter_type
        self.retrieve_max_length = retrieve_max_length
        self.top_k = top_k

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer_scope is not None:
            result['answerScope'] = self.answer_scope
        if self.enable_citation is not None:
            result['enableCitation'] = self.enable_citation
        if self.enable_search is not None:
            result['enableSearch'] = self.enable_search
        if self.enable_web_search is not None:
            result['enableWebSearch'] = self.enable_web_search
        if self.fixed_reply_detail is not None:
            result['fixedReplyDetail'] = self.fixed_reply_detail
        if self.knowledge_base_code_list is not None:
            result['knowledgeBaseCodeList'] = self.knowledge_base_code_list
        if self.prompt_strategy is not None:
            result['promptStrategy'] = self.prompt_strategy
        if self.rag_reject_type is not None:
            result['ragRejectType'] = self.rag_reject_type
        if self.reject_filter_prompt is not None:
            result['rejectFilterPrompt'] = self.reject_filter_prompt
        if self.reject_filter_type is not None:
            result['rejectFilterType'] = self.reject_filter_type
        if self.retrieve_max_length is not None:
            result['retrieveMaxLength'] = self.retrieve_max_length
        if self.top_k is not None:
            result['topK'] = self.top_k
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('answerScope') is not None:
            self.answer_scope = m.get('answerScope')
        if m.get('enableCitation') is not None:
            self.enable_citation = m.get('enableCitation')
        if m.get('enableSearch') is not None:
            self.enable_search = m.get('enableSearch')
        if m.get('enableWebSearch') is not None:
            self.enable_web_search = m.get('enableWebSearch')
        if m.get('fixedReplyDetail') is not None:
            self.fixed_reply_detail = m.get('fixedReplyDetail')
        if m.get('knowledgeBaseCodeList') is not None:
            self.knowledge_base_code_list = m.get('knowledgeBaseCodeList')
        if m.get('promptStrategy') is not None:
            self.prompt_strategy = m.get('promptStrategy')
        if m.get('ragRejectType') is not None:
            self.rag_reject_type = m.get('ragRejectType')
        if m.get('rejectFilterPrompt') is not None:
            self.reject_filter_prompt = m.get('rejectFilterPrompt')
        if m.get('rejectFilterType') is not None:
            self.reject_filter_type = m.get('rejectFilterType')
        if m.get('retrieveMaxLength') is not None:
            self.retrieve_max_length = m.get('retrieveMaxLength')
        if m.get('topK') is not None:
            self.top_k = m.get('topK')
        return self


class UpdateAndPublishAgentRequestApplicationConfigSecurity(TeaModel):
    def __init__(
        self,
        processing_strategy: str = None,
    ):
        self.processing_strategy = processing_strategy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.processing_strategy is not None:
            result['processingStrategy'] = self.processing_strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('processingStrategy') is not None:
            self.processing_strategy = m.get('processingStrategy')
        return self


class UpdateAndPublishAgentRequestApplicationConfigTools(TeaModel):
    def __init__(
        self,
        type: str = None,
    ):
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


class UpdateAndPublishAgentRequestApplicationConfigWorkFlows(TeaModel):
    def __init__(
        self,
        type: str = None,
    ):
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


class UpdateAndPublishAgentRequestApplicationConfig(TeaModel):
    def __init__(
        self,
        history_config: UpdateAndPublishAgentRequestApplicationConfigHistoryConfig = None,
        long_term_memory: UpdateAndPublishAgentRequestApplicationConfigLongTermMemory = None,
        parameters: UpdateAndPublishAgentRequestApplicationConfigParameters = None,
        rag_config: UpdateAndPublishAgentRequestApplicationConfigRagConfig = None,
        security: UpdateAndPublishAgentRequestApplicationConfigSecurity = None,
        tools: List[UpdateAndPublishAgentRequestApplicationConfigTools] = None,
        work_flows: List[UpdateAndPublishAgentRequestApplicationConfigWorkFlows] = None,
    ):
        self.history_config = history_config
        self.long_term_memory = long_term_memory
        self.parameters = parameters
        self.rag_config = rag_config
        self.security = security
        self.tools = tools
        self.work_flows = work_flows

    def validate(self):
        if self.history_config:
            self.history_config.validate()
        if self.long_term_memory:
            self.long_term_memory.validate()
        if self.parameters:
            self.parameters.validate()
        if self.rag_config:
            self.rag_config.validate()
        if self.security:
            self.security.validate()
        if self.tools:
            for k in self.tools:
                if k:
                    k.validate()
        if self.work_flows:
            for k in self.work_flows:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.history_config is not None:
            result['historyConfig'] = self.history_config.to_map()
        if self.long_term_memory is not None:
            result['longTermMemory'] = self.long_term_memory.to_map()
        if self.parameters is not None:
            result['parameters'] = self.parameters.to_map()
        if self.rag_config is not None:
            result['ragConfig'] = self.rag_config.to_map()
        if self.security is not None:
            result['security'] = self.security.to_map()
        result['tools'] = []
        if self.tools is not None:
            for k in self.tools:
                result['tools'].append(k.to_map() if k else None)
        result['workFlows'] = []
        if self.work_flows is not None:
            for k in self.work_flows:
                result['workFlows'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('historyConfig') is not None:
            temp_model = UpdateAndPublishAgentRequestApplicationConfigHistoryConfig()
            self.history_config = temp_model.from_map(m['historyConfig'])
        if m.get('longTermMemory') is not None:
            temp_model = UpdateAndPublishAgentRequestApplicationConfigLongTermMemory()
            self.long_term_memory = temp_model.from_map(m['longTermMemory'])
        if m.get('parameters') is not None:
            temp_model = UpdateAndPublishAgentRequestApplicationConfigParameters()
            self.parameters = temp_model.from_map(m['parameters'])
        if m.get('ragConfig') is not None:
            temp_model = UpdateAndPublishAgentRequestApplicationConfigRagConfig()
            self.rag_config = temp_model.from_map(m['ragConfig'])
        if m.get('security') is not None:
            temp_model = UpdateAndPublishAgentRequestApplicationConfigSecurity()
            self.security = temp_model.from_map(m['security'])
        self.tools = []
        if m.get('tools') is not None:
            for k in m.get('tools'):
                temp_model = UpdateAndPublishAgentRequestApplicationConfigTools()
                self.tools.append(temp_model.from_map(k))
        self.work_flows = []
        if m.get('workFlows') is not None:
            for k in m.get('workFlows'):
                temp_model = UpdateAndPublishAgentRequestApplicationConfigWorkFlows()
                self.work_flows.append(temp_model.from_map(k))
        return self


class UpdateAndPublishAgentRequestSampleLibrary(TeaModel):
    def __init__(
        self,
        enable_sample: bool = None,
        sample_library_id_list: List[str] = None,
        top_k: int = None,
    ):
        self.enable_sample = enable_sample
        self.sample_library_id_list = sample_library_id_list
        self.top_k = top_k

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_sample is not None:
            result['enableSample'] = self.enable_sample
        if self.sample_library_id_list is not None:
            result['sampleLibraryIdList'] = self.sample_library_id_list
        if self.top_k is not None:
            result['topK'] = self.top_k
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enableSample') is not None:
            self.enable_sample = m.get('enableSample')
        if m.get('sampleLibraryIdList') is not None:
            self.sample_library_id_list = m.get('sampleLibraryIdList')
        if m.get('topK') is not None:
            self.top_k = m.get('topK')
        return self


class UpdateAndPublishAgentRequest(TeaModel):
    def __init__(
        self,
        application_config: UpdateAndPublishAgentRequestApplicationConfig = None,
        instructions: str = None,
        model_id: str = None,
        name: str = None,
        sample_library: UpdateAndPublishAgentRequestSampleLibrary = None,
    ):
        self.application_config = application_config
        self.instructions = instructions
        self.model_id = model_id
        self.name = name
        self.sample_library = sample_library

    def validate(self):
        if self.application_config:
            self.application_config.validate()
        if self.sample_library:
            self.sample_library.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_config is not None:
            result['applicationConfig'] = self.application_config.to_map()
        if self.instructions is not None:
            result['instructions'] = self.instructions
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.name is not None:
            result['name'] = self.name
        if self.sample_library is not None:
            result['sampleLibrary'] = self.sample_library.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applicationConfig') is not None:
            temp_model = UpdateAndPublishAgentRequestApplicationConfig()
            self.application_config = temp_model.from_map(m['applicationConfig'])
        if m.get('instructions') is not None:
            self.instructions = m.get('instructions')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('sampleLibrary') is not None:
            temp_model = UpdateAndPublishAgentRequestSampleLibrary()
            self.sample_library = temp_model.from_map(m['sampleLibrary'])
        return self


class UpdateAndPublishAgentShrinkRequest(TeaModel):
    def __init__(
        self,
        application_config_shrink: str = None,
        instructions: str = None,
        model_id: str = None,
        name: str = None,
        sample_library_shrink: str = None,
    ):
        self.application_config_shrink = application_config_shrink
        self.instructions = instructions
        self.model_id = model_id
        self.name = name
        self.sample_library_shrink = sample_library_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_config_shrink is not None:
            result['applicationConfig'] = self.application_config_shrink
        if self.instructions is not None:
            result['instructions'] = self.instructions
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.name is not None:
            result['name'] = self.name
        if self.sample_library_shrink is not None:
            result['sampleLibrary'] = self.sample_library_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applicationConfig') is not None:
            self.application_config_shrink = m.get('applicationConfig')
        if m.get('instructions') is not None:
            self.instructions = m.get('instructions')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('sampleLibrary') is not None:
            self.sample_library_shrink = m.get('sampleLibrary')
        return self


class UpdateAndPublishAgentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateAndPublishAgentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAndPublishAgentResponseBody = None,
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
            temp_model = UpdateAndPublishAgentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAndPublishAgentSelectiveRequestApplicationConfigHistoryConfig(TeaModel):
    def __init__(
        self,
        enable_adb_record: bool = None,
        enable_record: bool = None,
        instance_id: str = None,
        region: str = None,
        store_code: str = None,
    ):
        self.enable_adb_record = enable_adb_record
        self.enable_record = enable_record
        self.instance_id = instance_id
        self.region = region
        self.store_code = store_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_adb_record is not None:
            result['enableAdbRecord'] = self.enable_adb_record
        if self.enable_record is not None:
            result['enableRecord'] = self.enable_record
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.region is not None:
            result['region'] = self.region
        if self.store_code is not None:
            result['storeCode'] = self.store_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enableAdbRecord') is not None:
            self.enable_adb_record = m.get('enableAdbRecord')
        if m.get('enableRecord') is not None:
            self.enable_record = m.get('enableRecord')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('storeCode') is not None:
            self.store_code = m.get('storeCode')
        return self


class UpdateAndPublishAgentSelectiveRequestApplicationConfigLongTermMemory(TeaModel):
    def __init__(
        self,
        enable: bool = None,
    ):
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        return self


class UpdateAndPublishAgentSelectiveRequestApplicationConfigParameters(TeaModel):
    def __init__(
        self,
        dialog_round: int = None,
        max_tokens: int = None,
        temperature: float = None,
    ):
        self.dialog_round = dialog_round
        self.max_tokens = max_tokens
        self.temperature = temperature

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dialog_round is not None:
            result['dialogRound'] = self.dialog_round
        if self.max_tokens is not None:
            result['maxTokens'] = self.max_tokens
        if self.temperature is not None:
            result['temperature'] = self.temperature
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dialogRound') is not None:
            self.dialog_round = m.get('dialogRound')
        if m.get('maxTokens') is not None:
            self.max_tokens = m.get('maxTokens')
        if m.get('temperature') is not None:
            self.temperature = m.get('temperature')
        return self


class UpdateAndPublishAgentSelectiveRequestApplicationConfigRagConfig(TeaModel):
    def __init__(
        self,
        answer_scope: str = None,
        enable_citation: bool = None,
        enable_search: bool = None,
        enable_web_search: bool = None,
        fixed_reply_detail: str = None,
        knowledge_base_code_list: List[str] = None,
        prompt_strategy: str = None,
        rag_reject_type: str = None,
        reject_filter_prompt: str = None,
        reject_filter_type: str = None,
        retrieve_max_length: int = None,
        top_k: int = None,
    ):
        self.answer_scope = answer_scope
        self.enable_citation = enable_citation
        self.enable_search = enable_search
        self.enable_web_search = enable_web_search
        self.fixed_reply_detail = fixed_reply_detail
        self.knowledge_base_code_list = knowledge_base_code_list
        self.prompt_strategy = prompt_strategy
        self.rag_reject_type = rag_reject_type
        self.reject_filter_prompt = reject_filter_prompt
        self.reject_filter_type = reject_filter_type
        self.retrieve_max_length = retrieve_max_length
        self.top_k = top_k

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer_scope is not None:
            result['answerScope'] = self.answer_scope
        if self.enable_citation is not None:
            result['enableCitation'] = self.enable_citation
        if self.enable_search is not None:
            result['enableSearch'] = self.enable_search
        if self.enable_web_search is not None:
            result['enableWebSearch'] = self.enable_web_search
        if self.fixed_reply_detail is not None:
            result['fixedReplyDetail'] = self.fixed_reply_detail
        if self.knowledge_base_code_list is not None:
            result['knowledgeBaseCodeList'] = self.knowledge_base_code_list
        if self.prompt_strategy is not None:
            result['promptStrategy'] = self.prompt_strategy
        if self.rag_reject_type is not None:
            result['ragRejectType'] = self.rag_reject_type
        if self.reject_filter_prompt is not None:
            result['rejectFilterPrompt'] = self.reject_filter_prompt
        if self.reject_filter_type is not None:
            result['rejectFilterType'] = self.reject_filter_type
        if self.retrieve_max_length is not None:
            result['retrieveMaxLength'] = self.retrieve_max_length
        if self.top_k is not None:
            result['topK'] = self.top_k
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('answerScope') is not None:
            self.answer_scope = m.get('answerScope')
        if m.get('enableCitation') is not None:
            self.enable_citation = m.get('enableCitation')
        if m.get('enableSearch') is not None:
            self.enable_search = m.get('enableSearch')
        if m.get('enableWebSearch') is not None:
            self.enable_web_search = m.get('enableWebSearch')
        if m.get('fixedReplyDetail') is not None:
            self.fixed_reply_detail = m.get('fixedReplyDetail')
        if m.get('knowledgeBaseCodeList') is not None:
            self.knowledge_base_code_list = m.get('knowledgeBaseCodeList')
        if m.get('promptStrategy') is not None:
            self.prompt_strategy = m.get('promptStrategy')
        if m.get('ragRejectType') is not None:
            self.rag_reject_type = m.get('ragRejectType')
        if m.get('rejectFilterPrompt') is not None:
            self.reject_filter_prompt = m.get('rejectFilterPrompt')
        if m.get('rejectFilterType') is not None:
            self.reject_filter_type = m.get('rejectFilterType')
        if m.get('retrieveMaxLength') is not None:
            self.retrieve_max_length = m.get('retrieveMaxLength')
        if m.get('topK') is not None:
            self.top_k = m.get('topK')
        return self


class UpdateAndPublishAgentSelectiveRequestApplicationConfigSecurity(TeaModel):
    def __init__(
        self,
        processing_strategy: str = None,
    ):
        self.processing_strategy = processing_strategy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.processing_strategy is not None:
            result['processingStrategy'] = self.processing_strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('processingStrategy') is not None:
            self.processing_strategy = m.get('processingStrategy')
        return self


class UpdateAndPublishAgentSelectiveRequestApplicationConfigTools(TeaModel):
    def __init__(
        self,
        type: str = None,
    ):
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


class UpdateAndPublishAgentSelectiveRequestApplicationConfigWorkFlows(TeaModel):
    def __init__(
        self,
        type: str = None,
    ):
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


class UpdateAndPublishAgentSelectiveRequestApplicationConfig(TeaModel):
    def __init__(
        self,
        history_config: UpdateAndPublishAgentSelectiveRequestApplicationConfigHistoryConfig = None,
        long_term_memory: UpdateAndPublishAgentSelectiveRequestApplicationConfigLongTermMemory = None,
        parameters: UpdateAndPublishAgentSelectiveRequestApplicationConfigParameters = None,
        rag_config: UpdateAndPublishAgentSelectiveRequestApplicationConfigRagConfig = None,
        security: UpdateAndPublishAgentSelectiveRequestApplicationConfigSecurity = None,
        tools: List[UpdateAndPublishAgentSelectiveRequestApplicationConfigTools] = None,
        work_flows: List[UpdateAndPublishAgentSelectiveRequestApplicationConfigWorkFlows] = None,
    ):
        self.history_config = history_config
        self.long_term_memory = long_term_memory
        self.parameters = parameters
        self.rag_config = rag_config
        self.security = security
        self.tools = tools
        self.work_flows = work_flows

    def validate(self):
        if self.history_config:
            self.history_config.validate()
        if self.long_term_memory:
            self.long_term_memory.validate()
        if self.parameters:
            self.parameters.validate()
        if self.rag_config:
            self.rag_config.validate()
        if self.security:
            self.security.validate()
        if self.tools:
            for k in self.tools:
                if k:
                    k.validate()
        if self.work_flows:
            for k in self.work_flows:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.history_config is not None:
            result['historyConfig'] = self.history_config.to_map()
        if self.long_term_memory is not None:
            result['longTermMemory'] = self.long_term_memory.to_map()
        if self.parameters is not None:
            result['parameters'] = self.parameters.to_map()
        if self.rag_config is not None:
            result['ragConfig'] = self.rag_config.to_map()
        if self.security is not None:
            result['security'] = self.security.to_map()
        result['tools'] = []
        if self.tools is not None:
            for k in self.tools:
                result['tools'].append(k.to_map() if k else None)
        result['workFlows'] = []
        if self.work_flows is not None:
            for k in self.work_flows:
                result['workFlows'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('historyConfig') is not None:
            temp_model = UpdateAndPublishAgentSelectiveRequestApplicationConfigHistoryConfig()
            self.history_config = temp_model.from_map(m['historyConfig'])
        if m.get('longTermMemory') is not None:
            temp_model = UpdateAndPublishAgentSelectiveRequestApplicationConfigLongTermMemory()
            self.long_term_memory = temp_model.from_map(m['longTermMemory'])
        if m.get('parameters') is not None:
            temp_model = UpdateAndPublishAgentSelectiveRequestApplicationConfigParameters()
            self.parameters = temp_model.from_map(m['parameters'])
        if m.get('ragConfig') is not None:
            temp_model = UpdateAndPublishAgentSelectiveRequestApplicationConfigRagConfig()
            self.rag_config = temp_model.from_map(m['ragConfig'])
        if m.get('security') is not None:
            temp_model = UpdateAndPublishAgentSelectiveRequestApplicationConfigSecurity()
            self.security = temp_model.from_map(m['security'])
        self.tools = []
        if m.get('tools') is not None:
            for k in m.get('tools'):
                temp_model = UpdateAndPublishAgentSelectiveRequestApplicationConfigTools()
                self.tools.append(temp_model.from_map(k))
        self.work_flows = []
        if m.get('workFlows') is not None:
            for k in m.get('workFlows'):
                temp_model = UpdateAndPublishAgentSelectiveRequestApplicationConfigWorkFlows()
                self.work_flows.append(temp_model.from_map(k))
        return self


class UpdateAndPublishAgentSelectiveRequestSampleLibrary(TeaModel):
    def __init__(
        self,
        enable_sample: bool = None,
        sample_library_id_list: List[str] = None,
        top_k: int = None,
    ):
        self.enable_sample = enable_sample
        self.sample_library_id_list = sample_library_id_list
        self.top_k = top_k

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_sample is not None:
            result['enableSample'] = self.enable_sample
        if self.sample_library_id_list is not None:
            result['sampleLibraryIdList'] = self.sample_library_id_list
        if self.top_k is not None:
            result['topK'] = self.top_k
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enableSample') is not None:
            self.enable_sample = m.get('enableSample')
        if m.get('sampleLibraryIdList') is not None:
            self.sample_library_id_list = m.get('sampleLibraryIdList')
        if m.get('topK') is not None:
            self.top_k = m.get('topK')
        return self


class UpdateAndPublishAgentSelectiveRequest(TeaModel):
    def __init__(
        self,
        application_config: UpdateAndPublishAgentSelectiveRequestApplicationConfig = None,
        instructions: str = None,
        model_id: str = None,
        name: str = None,
        sample_library: UpdateAndPublishAgentSelectiveRequestSampleLibrary = None,
    ):
        self.application_config = application_config
        self.instructions = instructions
        self.model_id = model_id
        self.name = name
        self.sample_library = sample_library

    def validate(self):
        if self.application_config:
            self.application_config.validate()
        if self.sample_library:
            self.sample_library.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_config is not None:
            result['applicationConfig'] = self.application_config.to_map()
        if self.instructions is not None:
            result['instructions'] = self.instructions
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.name is not None:
            result['name'] = self.name
        if self.sample_library is not None:
            result['sampleLibrary'] = self.sample_library.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applicationConfig') is not None:
            temp_model = UpdateAndPublishAgentSelectiveRequestApplicationConfig()
            self.application_config = temp_model.from_map(m['applicationConfig'])
        if m.get('instructions') is not None:
            self.instructions = m.get('instructions')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('sampleLibrary') is not None:
            temp_model = UpdateAndPublishAgentSelectiveRequestSampleLibrary()
            self.sample_library = temp_model.from_map(m['sampleLibrary'])
        return self


class UpdateAndPublishAgentSelectiveShrinkRequest(TeaModel):
    def __init__(
        self,
        application_config_shrink: str = None,
        instructions: str = None,
        model_id: str = None,
        name: str = None,
        sample_library_shrink: str = None,
    ):
        self.application_config_shrink = application_config_shrink
        self.instructions = instructions
        self.model_id = model_id
        self.name = name
        self.sample_library_shrink = sample_library_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_config_shrink is not None:
            result['applicationConfig'] = self.application_config_shrink
        if self.instructions is not None:
            result['instructions'] = self.instructions
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.name is not None:
            result['name'] = self.name
        if self.sample_library_shrink is not None:
            result['sampleLibrary'] = self.sample_library_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applicationConfig') is not None:
            self.application_config_shrink = m.get('applicationConfig')
        if m.get('instructions') is not None:
            self.instructions = m.get('instructions')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('sampleLibrary') is not None:
            self.sample_library_shrink = m.get('sampleLibrary')
        return self


class UpdateAndPublishAgentSelectiveResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateAndPublishAgentSelectiveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAndPublishAgentSelectiveResponseBody = None,
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
            temp_model = UpdateAndPublishAgentSelectiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateChunkRequest(TeaModel):
    def __init__(
        self,
        chunk_id: str = None,
        data_id: str = None,
        is_displayed_chunk_content: bool = None,
        pipeline_id: str = None,
        content: str = None,
        title: str = None,
    ):
        # This parameter is required.
        self.chunk_id = chunk_id
        # This parameter is required.
        self.data_id = data_id
        # This parameter is required.
        self.is_displayed_chunk_content = is_displayed_chunk_content
        # This parameter is required.
        self.pipeline_id = pipeline_id
        # This parameter is required.
        self.content = content
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chunk_id is not None:
            result['ChunkId'] = self.chunk_id
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.is_displayed_chunk_content is not None:
            result['IsDisplayedChunkContent'] = self.is_displayed_chunk_content
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.content is not None:
            result['content'] = self.content
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChunkId') is not None:
            self.chunk_id = m.get('ChunkId')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('IsDisplayedChunkContent') is not None:
            self.is_displayed_chunk_content = m.get('IsDisplayedChunkContent')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class UpdateChunkResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.status = status
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateChunkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateChunkResponseBody = None,
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
            temp_model = UpdateChunkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFileTagRequest(TeaModel):
    def __init__(
        self,
        tags: List[str] = None,
    ):
        # This parameter is required.
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class UpdateFileTagShrinkRequest(TeaModel):
    def __init__(
        self,
        tags_shrink: str = None,
    ):
        # This parameter is required.
        self.tags_shrink = tags_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        return self


class UpdateFileTagResponseBodyData(TeaModel):
    def __init__(
        self,
        file_id: str = None,
    ):
        self.file_id = file_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['FileId'] = self.file_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        return self


class UpdateFileTagResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: UpdateFileTagResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # RequestId
        self.request_id = request_id
        self.status = status
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = UpdateFileTagResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateFileTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateFileTagResponseBody = None,
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
            temp_model = UpdateFileTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateMemoryRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
    ):
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        return self


class UpdateMemoryResponseBody(TeaModel):
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


class UpdateMemoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateMemoryResponseBody = None,
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
            temp_model = UpdateMemoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateMemoryNodeRequest(TeaModel):
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


class UpdateMemoryNodeResponseBody(TeaModel):
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


class UpdateMemoryNodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateMemoryNodeResponseBody = None,
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
            temp_model = UpdateMemoryNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePromptTemplateRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        name: str = None,
    ):
        # The template content.
        self.content = content
        # The template name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class UpdatePromptTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class UpdatePromptTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdatePromptTemplateResponseBody = None,
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
            temp_model = UpdatePromptTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


